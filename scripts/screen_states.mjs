/* The screen states (2026-11-08, shared): every wireframe page and the states its URL switches open, Race browse with
   0, 1, 2, 3 and 5 active filters in List view, Map view and with the Filters sheet open, the two alerts opened by a
   click, and every pattern page. Read by scripts/check_overflow.mjs (the overflow and one-line checks) and
   scripts/check_focus.mjs (the focus halo and the sheet bar), so both walk the same states. Until 2026-11-08 the list
   lived in check_overflow.mjs. */
import { readdirSync } from 'node:fs';
import { join } from 'node:path';

// Filter sets for Race browse: 0, 1, 2, 3 and 5 active filters, the longest chip texts (microcopy.md: regions,
// sport types, a date range across two years), plus a search chip.
export const FILTERS = {
  0: '',
  1: 'sport=deka',
  2: 'region=North%20America&sport=deka',
  3: 'region=North%20America&sport=deka&from=2026-12-28&to=2027-01-03',
  5: 'region=North%20America&sport=deka&sport=half-marathon&sport=triathlon&from=2026-12-28&to=2027-01-03&q=Killington',
};
export const CAUSES = {   // the URL switches each state page reads (as the screenshot runs use them)
  'race-detail': ['', 'race=utmb'], 'race-detail-error': ['', 'cause=registration&race=utmb'],
  'results-list': ['', 'saved=Spartan%20Race%20Beast%20%E2%80%94%20Killington', 'add=spartan-beast-killington-2025', 'add=spartan-beast-killington-2025&try=athlinks', 'saved=Spartan%20Race%20Beast%20%E2%80%94%20Killington&linked=spartan-beast-killington-2025&url=https%3A%2F%2Fwww.athlinks.com%2Fevent%2Fspartan-race-beast-killington-2025%2Fresults'],   // 2026-11-06: the add sheet, its error, a link just saved
  'log-result': ['', 'catalog=spartan-beast-killington-2025'], 'log-result-error': ['cause=fields', 'cause=link', 'cause=submit'],
  'race-picker': ['', 'q=hyrox', 'catalog=utmb-2026'], 'race-picker-empty': ['q=a%20very%20long%20race%20name%20nobody%20has%20heard%20of'],
  'result-detail': ['', 'result=valencia-half-2025', 'result=spartan-beast-killington-2025', 'result=spartan-beast-killington-2025&add=spartan-beast-killington-2025', 'result=spartan-beast-killington-2025&add=spartan-beast-killington-2025&try=athlinks', 'result=spartan-beast-killington-2025&linked=spartan-beast-killington-2025&url=https%3A%2F%2Fwww.athlinks.com%2Fevent%2Fspartan-race-beast-killington-2025%2Fresults'], 'result-detail-error': ['', 'cause=link&result=valencia-half-2025'],
  'sign-in-sign-up': ['', 'mode=signup', 'reset=done'], 'sign-in-sign-up-check-inbox': ['', 'reason=unconfirmed'],
  'sign-in-sign-up-error': ['cause=signin', 'cause=signup&mode=signup', 'cause=confirm'], 'sign-in-sign-up-loading': ['', 'mode=signup'],
  'reset-password-error': ['', 'cause=rate'],
  'new-password-error': ['cause=submit', 'cause=short', 'cause=same', 'cause=mismatch', 'cause=expired'],
  'profile-error': ['', 'cause=save&field=country&value=France&prev=Italy'],
};
export function screenStates(ROOT) {
  const W = join(ROOT, 'wireframes'), states = [];
for (const f of readdirSync(W).filter(f => f.endsWith('.html') && f !== 'index.html').sort()) {
  const name = f.replace('.html', '');
  if (name.startsWith('race-browse')) {
    for (const [n, q] of Object.entries(FILTERS)) {
      if (name === 'race-browse-error' && n !== '0') continue;   // the error page keeps its filters out of view
      for (const act of ['', 'map', 'sheet']) states.push({ name, q, act, label: `${name} · ${n} filters${act ? ' · ' + act : ''}` });
    }
  } else {
    for (const q of CAUSES[name] || ['']) states.push({ name, q, act: '', label: name + (q ? '?' + q : '') });
  }
}
states.push({ name: 'profile', q: '', act: 'click:#sign-out', label: 'profile · sign-out alert' });
states.push({ name: 'log-result', q: 'race_name=Spartan%20Race%20Beast%20%E2%80%94%20Killington', act: 'click:[data-cancel]', label: 'log-result · discard confirm' });
// the patterns (Lesson 9 step 4, 2026-11-06): each a phone page of existing components, measured like a screen
for (const f of readdirSync(join(ROOT, 'design-system/patterns')).filter(f => f.endsWith('.html')).sort())
  states.push({ name: '../design-system/patterns/' + f.replace('.html', ''), q: '', act: '', label: 'patterns/' + f.replace('.html', '') });
// the examples (Lesson 9 step 6, 2026-11-10): screens built only from the system, measured like a screen
for (const f of readdirSync(join(ROOT, 'design-system/examples')).filter(f => f.endsWith('.html')).sort())
  states.push({ name: '../design-system/examples/' + f.replace('.html', ''), q: '', act: '', label: 'examples/' + f.replace('.html', '') });
return states;
}
