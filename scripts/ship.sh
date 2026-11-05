#!/usr/bin/env bash
# Build, commit, deploy: the only way changes leave this machine (2026-11-05).
#   scripts/ship.sh "commit message"
# Each step runs only if the one before it exited 0; the first failure stops everything after it.
#   1. the build (scripts/concept/build_stand.py, every check). If it fails only because Google Fonts couldn't be
#      reached (exit 3 from check_overflow), it runs once more; a second failure of any kind stops here.
#   2. git add -A, then git commit. scripts/hooks/pre-commit refuses unless the tree is the one the build stamped.
#   3. git push to origin/main, which deploys. scripts/hooks/pre-push refuses unless HEAD is the stamped tree.
#   4. waits for the GitHub Pages deploy and fails if it does.
# Exit codes: 0 shipped; 1 the build failed; 3 the build failed twice on fonts only; 4 nothing to commit;
# 5 the hooks aren't installed; 6 commit or push refused; 7 the deploy failed.
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
msg="${1:?usage: scripts/ship.sh \"commit message\"}"

if [ "$(git config core.hooksPath || true)" != "scripts/hooks" ]; then
  echo "ship: the hooks aren't installed (git config core.hooksPath scripts/hooks). Nothing built, committed or pushed." >&2
  exit 5
fi

build() {   # the build's exit code, its output kept in .build.log (git-ignored by *.log)
  set +e
  python3 scripts/concept/build_stand.py > .build.log 2>&1
  local rc=$?
  set -e
  grep -E '^(check_|build:|.*failed|.*FAIL|    )' .build.log || true
  return $rc
}

echo "ship: building"
rc=0; build || rc=$?
if [ "$rc" -eq 3 ]; then
  echo "ship: the build failed only on fonts that didn't load (Google Fonts unreachable); retrying once"
  rc=0; build || rc=$?
  if [ "$rc" -eq 3 ]; then
    echo "ship: STOPPED. The build failed on fonts twice; nothing was committed or pushed. Full log: .build.log" >&2
    exit 3
  fi
fi
if [ "$rc" -ne 0 ]; then
  echo "ship: STOPPED. The build failed (exit $rc); nothing was committed or pushed. Full log: .build.log" >&2
  exit 1
fi
if [ ! -f .build-ok ]; then
  echo "ship: STOPPED. The build passed but wrote no .build-ok (a check was skipped); nothing was committed or pushed." >&2
  exit 1
fi

git add -A
if git diff --cached --quiet; then
  echo "ship: the build passed and there is nothing to commit."
  exit 4
fi
git commit -q -m "$msg" || { echo "ship: STOPPED. The commit was refused; nothing was pushed." >&2; exit 6; }
echo "ship: committed $(git rev-parse --short HEAD)"
git push -q origin main || { echo "ship: STOPPED. The push was refused; nothing was deployed. The commit is local only." >&2; exit 6; }
echo "ship: pushed; waiting for the deploy"

sha=$(git rev-parse HEAD); run=""
for _ in $(seq 1 30); do   # the run for this commit appears a few seconds after the push
  run=$(gh run list --commit "$sha" --limit 1 --json databaseId -q '.[0].databaseId' 2>/dev/null || true)
  [ -n "$run" ] && break
  sleep 2
done
if [ -z "$run" ]; then echo "ship: pushed, but no deploy run appeared for $sha; check GitHub Actions." >&2; exit 7; fi
if gh run watch "$run" --exit-status > /dev/null 2>&1; then
  echo "ship: deployed $(git rev-parse --short HEAD) (run $run)"
else
  echo "ship: the deploy of $(git rev-parse --short HEAD) FAILED (run $run); see gh run view $run" >&2
  exit 7
fi
