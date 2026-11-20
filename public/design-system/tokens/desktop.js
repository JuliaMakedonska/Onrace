/* The desktop, for what a media query can't do (Lesson 10 step 7, 2026-11-20). It reads the one breakpoint from
   design-system/tokens/tokens.css (--bp-desktop), so no page writes a width of its own:
   - <body data-desktop-home="race-browse.html" data-desktop-param="race">: a detail page that has a home on a desktop
     (Race detail in Race browse's race card, Result detail in Results list's result card) opens there, with the
     page's own query (its key, and add=, try=, … where the home reads them). Below the breakpoint nothing changes. The
     split view takes its detail from this page by fetch(), which runs no script, so the pane is never sent away.
   - <iframe class="sheet-presenter" data-src="results-list.html">: the screen under a form sheet that is a page of its
     own (Log result, Race picker), loaded from the breakpoint only (an iframe that isn't drawn still loads), inert and
     out of the focus order (modal-sheet.css draws it dimmed).
   - [data-popover-modal]: a sheet that is a popover card on a desktop (Filters) is modal below it only: aria-modal
     follows the width, since on a desktop the screen stays live around it.
   Loaded with defer by the pages that need it. */
(function () {
  var bp = getComputedStyle(document.documentElement).getPropertyValue('--bp-desktop').trim();
  if (!bp) return;
  var mq = matchMedia('(min-width: ' + bp + ')');
  var body = document.body;
  var home = body && body.getAttribute('data-desktop-home');
  if (home && mq.matches) {
    var q = new URLSearchParams(location.search), key = body.getAttribute('data-desktop-param');
    if (key && !q.get(key) && body.getAttribute('data-desktop-key')) q.set(key, body.getAttribute('data-desktop-key'));
    location.replace(new URL(home, location.href).pathname + (q.toString() ? '?' + q.toString() : '') + location.hash);
    return;
  }
  function apply() {
    document.querySelectorAll('iframe.sheet-presenter[data-src]').forEach(function (f) {
      if (mq.matches && !f.getAttribute('src')) f.setAttribute('src', f.getAttribute('data-src'));
    });
    document.querySelectorAll('[data-popover-modal]').forEach(function (d) { d.setAttribute('aria-modal', mq.matches ? 'false' : 'true'); });
  }
  apply();
  if (mq.addEventListener) mq.addEventListener('change', apply);
})();
