/* Split view (Lesson 10 step 5, 2026-11-17): the behaviour of design-system/patterns/split-view.html, used by Race browse
   and Results list. The layout is design-system/components/split-view.css; this script only fills the detail pane.
   - Whether the screen is split is the CSS's answer (--split on .split-detail: 0 on a phone, 1 from --bp-tablet), so
     the breakpoints live in one place and a phone keeps its flow: a card opens its own screen, as before.
   - Split, choosing a card (or a map pin) puts its key in the URL (?race=… or ?result=…, pushState, so a choice can be
     linked and Back goes back), marks its card Selected (aria-current="page") and shows the detail in the pane.
   - The detail comes from the detail screen's own page (data-split-source: race-detail.html, result-detail.html): its
     article and action bar for that key, so the pane and the phone's screen are one source. While it loads the pane
     is aria-busy with the loading page's skeleton (data-split-loading); if it fails (or ?fail=1, the reviewer switch),
     the error page's detail error (data-split-error) shows inside the pane, its Try again retries in place.
   - With nothing chosen the pane shows its .split-empty ("No race selected", "No result selected").
   - [data-split-close] (Race browse, tablet: "‹ Map") clears the choice. */
(function () {
  var root = document.querySelector('.split-view');
  var pane = root && root.querySelector('.split-detail');
  if (!pane) return;
  var param = pane.getAttribute('data-split-param');
  var src = { detail: pane.getAttribute('data-split-source'), loading: pane.getAttribute('data-split-loading'), error: pane.getAttribute('data-split-error') };
  var empty = pane.querySelector('.split-empty'), content = pane.querySelector('.split-content');
  var docs = {}, current = null;

  function split() { return getComputedStyle(pane).getPropertyValue('--split').trim() === '1'; }
  function keyOf(a) { try { return new URL(a.getAttribute('href'), location.href).searchParams.get(param); } catch (e) { return null; } }
  function chosen() { return new URLSearchParams(location.search).get(param); }
  function page(url) {
    if (!docs[url]) docs[url] = fetch(url).then(function (r) { if (!r.ok) throw new Error(url + ' ' + r.status); return r.text(); })
      .then(function (t) { return new DOMParser().parseFromString(t, 'text/html'); });
    return docs[url];
  }
  function wake(n) {   // an imported part shows, and its photo loads (the detail page keeps its sources in data-* until shown)
    n.hidden = false;
    n.querySelectorAll('[data-srcset]').forEach(function (el) { el.srcset = el.getAttribute('data-srcset'); el.removeAttribute('data-srcset'); });
    n.querySelectorAll('img[data-src]').forEach(function (img) { img.src = img.getAttribute('data-src'); img.removeAttribute('data-src'); });
    return n;
  }
  function put(nodes) {
    content.textContent = '';
    nodes.forEach(function (n) { if (n) content.appendChild(wake(document.importNode(n, true))); });
  }
  function mark(key) {
    root.querySelectorAll('.card-link, .map-pin').forEach(function (a) {
      if (key && keyOf(a) === key) a.setAttribute('aria-current', 'page');
      else if (a.getAttribute('aria-current') === 'page') a.removeAttribute('aria-current');
    });
  }
  function show() {
    var key = split() ? chosen() : null;
    mark(key);
    empty.hidden = !!key; content.hidden = !key;
    var token = current = {};
    if (!key) { content.textContent = ''; pane.removeAttribute('aria-busy'); pane.setAttribute('data-split-state', 'empty'); return; }
    pane.setAttribute('aria-busy', 'true'); pane.setAttribute('data-split-state', 'loading');   // data-split-state: what the pane shows, for the docs' stage check to wait on
    if (src.loading) page(src.loading).then(function (d) {
      if (current !== token || !pane.hasAttribute('aria-busy')) return;
      put([d.querySelector('main > *'), d.querySelector('.phone-screen > .action-bar')]);
    }).catch(function () {});
    var attr = '[data-' + param + '="' + key.replace(/["\\]/g, '') + '"]';
    var job = new URLSearchParams(location.search).get('fail') === '1' ? Promise.reject(new Error('fail=1')) : page(src.detail).then(function (d) {
      var item = d.querySelector('main ' + attr);
      if (!item) throw new Error('no ' + key);
      return [item, d.querySelector('.phone-screen > .action-bar' + attr)];
    });
    job.then(function (parts) {
      if (current !== token) return;
      pane.removeAttribute('aria-busy'); put(parts); pane.scrollTop = 0; pane.setAttribute('data-split-state', 'shown');
    }).catch(function () {
      return page(src.error).then(function (d) {
        if (current !== token) return;
        pane.removeAttribute('aria-busy'); put([d.querySelector('.state-message[data-cause="detail"]')]); pane.setAttribute('data-split-state', 'error');
        content.querySelectorAll('[data-retry]').forEach(function (a) {
          a.addEventListener('click', function (e) {
            e.preventDefault();
            var u = new URLSearchParams(location.search); u.delete('fail');
            history.replaceState(null, '', location.pathname + '?' + u.toString());
            show();
          });
        });
      });
    });
  }
  function go(key) {
    var u = new URLSearchParams(location.search);
    if (key) u.set(param, key); else u.delete(param);
    u.delete('fail');
    history.pushState(null, '', location.pathname + (u.toString() ? '?' + u.toString() : ''));
    show();
  }
  root.addEventListener('click', function (e) {
    if (e.defaultPrevented || e.button || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey || !split()) return;
    var close = e.target.closest('[data-split-close]');
    if (close) { e.preventDefault(); go(null); return; }
    var a = e.target.closest('.card-link, .map-pin');
    var key = a && keyOf(a);
    if (!key) return;
    e.preventDefault();
    go(key);
  });
  // Copy link inside a result's pane: the same as on Result detail (its button says "Link copied" for a moment)
  content.addEventListener('click', function (e) {
    var btn = e.target.closest('[data-copy]');
    if (!btn) return;
    var url = btn.closest('.proof').querySelector('.proof-url').textContent.trim();
    var done = function () { btn.textContent = 'Link copied'; setTimeout(function () { btn.textContent = 'Copy link'; }, 2000); };
    if (navigator.clipboard) navigator.clipboard.writeText(url).then(done, done); else done();
  });
  window.addEventListener('popstate', show);
  var was = split();
  window.addEventListener('resize', function () { var now = split(); if (now !== was) { was = now; show(); } });
  if (split()) {   // both views show side by side: the List / Map switch is off, so the list view is the one in force
    var list = root.querySelector('.view-btn[data-view="list"][aria-pressed="false"]');
    if (list) list.click();
  }
  show();
})();
