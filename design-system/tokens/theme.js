/* tokens/theme.js: the theme switch for the light-theme stress test (Lesson 8 step 5, 2026-10-29).
   Onrace is dark-only (C5). ?theme=light puts data-theme="light" on <html>, which switches tokens/tokens.css's semantic
   roles to the light block; nothing else changes. Loaded in each page's <head>, before first paint, not deferred.
   - The URL decides: ?theme=light or ?theme=dark. The choice is kept for the tab in sessionStorage, so a state change made
     by a page script (location.href = '…-loading.html?run=1') keeps the theme even when the script drops the parameter.
   - A tap on a link to another page adds theme=light to its URL, so the theme stays visible in the address.
   - Dark is the default and sets nothing: a dark page is the page as it was before this file existed. */
(function () {
  var KEY = 'onrace-theme', t = null, q = null;
  try { q = new URLSearchParams(location.search).get('theme'); } catch (e) {}
  if (q === 'light' || q === 'dark') {
    t = q;
    try { sessionStorage.setItem(KEY, q); } catch (e) {}
  } else {
    try { t = sessionStorage.getItem(KEY); } catch (e) {}
  }
  if (t !== 'light') return;
  document.documentElement.setAttribute('data-theme', 'light');
  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a[href]');
    if (!a || a.target === '_blank' || a.origin !== location.origin || !/\.html$/.test(a.pathname)) return;
    var u = new URL(a.href);
    if (!u.searchParams.has('theme')) { u.searchParams.set('theme', 'light'); a.href = u.toString(); }
  }, true);
})();
