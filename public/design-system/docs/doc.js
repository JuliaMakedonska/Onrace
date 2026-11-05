/* The design-system docs' own script (Lesson 9; the shell since 2026-11-05). Every page of design-system/docs/ loads
   it; each job runs only where its markup is. Documentation only: it never runs on a product screen.
   1. the Light / Dark switch ([data-kd-theme]): <html data-theme="light"> here and in every same-origin frame (the tab
      bar stages are srcdoc frames); kept for the tab as design-system/tokens/theme.js keeps it, and in the URL. Light is
      the stress test of the semantic roles; Onrace ships dark only (C5).
   2. the shell (scripts/docs_shell.py): the menu on a phone, the nav's filter, and the section on screen marked in the
      nav and in "On this page".
   3. the anatomy ([data-anatomy]): each part's number in the gutter beside the stage, at the part's height, never over
      it; a legend item outlines its part while hovered or focused. A selector that finds nothing
      throws, so scripts/check_overflow.mjs fails the build. */
(function () {
  var $$ = function (sel, root) { return Array.prototype.slice.call((root || document).querySelectorAll(sel)); };

  // ---------------------------------------------------------------- 1. the theme
  var themeBtns = $$('[data-kd-theme]');
  function docs() {
    return [document].concat($$('iframe').map(function (f) {
      try { return f.contentDocument; } catch (e) { return null; }
    }).filter(function (d) { return d && d.documentElement; }));   // a frame still loading has no root yet; its load event applies the theme
  }
  function setTheme(t, save) {
    docs().forEach(function (d) { if (t === 'light') d.documentElement.setAttribute('data-theme', 'light'); else d.documentElement.removeAttribute('data-theme'); });
    themeBtns.forEach(function (b) { b.setAttribute('aria-pressed', String(b.getAttribute('data-kd-theme') === t)); });
    if (!save) return;
    try { sessionStorage.setItem('onrace-theme', t); } catch (e) {}
    try { var u = new URL(location.href); if (t === 'light') u.searchParams.set('theme', 'light'); else u.searchParams.delete('theme'); history.replaceState(null, '', u); } catch (e) {}
  }
  var current = document.documentElement.getAttribute('data-theme') === 'light' ? 'light' : 'dark';
  setTheme(current, false);
  $$('iframe').forEach(function (f) { f.addEventListener('load', function () { setTheme(current, false); }); });
  themeBtns.forEach(function (b) { b.addEventListener('click', function () { current = b.getAttribute('data-kd-theme'); setTheme(current, true); }); });

  // ---------------------------------------------------------------- 2. the shell
  var nav = document.getElementById('ds-nav'), menu = document.querySelector('.ds-menu');
  if (nav && menu) {
    menu.addEventListener('click', function () {
      var open = menu.getAttribute('aria-expanded') !== 'true';
      menu.setAttribute('aria-expanded', String(open)); nav.classList.toggle('is-open', open);
    });
    nav.addEventListener('click', function (e) {
      if (e.target.closest('a') && menu.getAttribute('aria-expanded') === 'true') { menu.setAttribute('aria-expanded', 'false'); nav.classList.remove('is-open'); }
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && menu.getAttribute('aria-expanded') === 'true') { menu.setAttribute('aria-expanded', 'false'); nav.classList.remove('is-open'); menu.focus(); }
    });
  }
  var filter = document.getElementById('ds-filter'), empty = document.querySelector('.ds-empty');
  if (filter && nav) filter.addEventListener('input', function () {
    var q = filter.value.trim().toLowerCase(), shown = 0;
    nav.classList.toggle('is-filtering', !!q);
    $$('.ds-fam', nav).forEach(function (fam) {
      var famHit = !q || fam.querySelector('.ds-fam-a').getAttribute('data-names').indexOf(q) > -1, any = false;
      $$('.ds-comps li', fam).forEach(function (li) {
        var hit = famHit || li.firstChild.getAttribute('data-names').indexOf(q) > -1;
        li.hidden = !hit; if (hit) { any = true; shown++; }
      });
      fam.hidden = !(famHit || any);
    });
    $$('.ds-fams', nav).forEach(function (ul) { var role = ul.previousElementSibling; var vis = !!ul.querySelector('.ds-fam:not([hidden])'); ul.hidden = !vis; if (role) role.hidden = !vis; });
    $$('.ds-top', nav).forEach(function (ul) { ul.hidden = !!q; });
    if (empty) empty.hidden = !q || shown > 0;
  });
  var sections = $$('.ds-main .dc[id], .ds-main .dc-why[id]');
  if (sections.length && 'IntersectionObserver' in window) {
    var links = $$('.ds-toc a, .ds-comps a, .ds-fam-a').filter(function (a) { return a.getAttribute('href').indexOf('#') > -1 || a.closest('.ds-toc'); });
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        links.forEach(function (a) {
          var on = a.getAttribute('href').split('#')[1] === e.target.id && (a.closest('.ds-toc') || a.closest('.ds-fam.is-current'));
          if (on) a.setAttribute('aria-current', 'true'); else if (a.getAttribute('aria-current') === 'true') a.removeAttribute('aria-current');
        });
      });
    }, { rootMargin: '-15% 0px -75% 0px' });
    sections.forEach(function (s) { io.observe(s); });
  }

  // ---------------------------------------------------------------- 3. the anatomy
  var stages = $$('[data-anatomy]');
  if (!stages.length) return;
  function find(stage, sel) {   // the stage first, then its same-origin frames (the tab bar)
    var el = stage.querySelector('.kit-frame ' + sel);
    if (el) return { el: el, frame: null };
    var frames = stage.querySelectorAll('iframe');
    for (var i = 0; i < frames.length; i++) {
      var d; try { d = frames[i].contentDocument; } catch (e) { d = null; }
      var hit = d && d.querySelector(sel);
      if (hit) return { el: hit, frame: frames[i] };
    }
    return null;
  }
  function legendOf(stage) { return stage.parentNode.querySelector('.an-legend'); }
  function show(stage, n, on) {
    var box = stage.querySelector('.an-box[data-part="' + n + '"]'), li = legendOf(stage).querySelector('li[data-part="' + n + '"]');
    if (box) box.classList.toggle('is-on', on);
    if (li) li.classList.toggle('is-on', on);
  }
  function place(strict) {
    stages.forEach(function (stage) {
      var parts = JSON.parse(stage.getAttribute('data-anatomy'));
      var layer = stage.querySelector('.an-layer');
      if (!layer) { layer = document.createElement('div'); layer.className = 'an-layer'; layer.setAttribute('aria-hidden', 'true'); stage.appendChild(layer); }
      layer.textContent = '';
      var frame = stage.querySelector('.kit-state'), sb = stage.getBoundingClientRect(), fb = frame.getBoundingClientRect();
      var gutter = fb.right - sb.left + 6, last = -Infinity;
      var spots = parts.map(function (p, i) {
        var hit = find(stage, p[0]);
        if (!hit) { if (strict) throw new Error('anatomy: "' + p[0] + '" (' + p[1] + ') finds nothing on its stage'); return null; }
        var r = hit.el.getBoundingClientRect(), dx = 0, dy = 0;
        if (hit.frame) { var fr = hit.frame.getBoundingClientRect(); dx = fr.left; dy = fr.top; }
        return { i: i, left: r.left + dx - sb.left, top: r.top + dy - sb.top, right: r.right + dx - sb.left, h: r.height, w: r.width };
      }).filter(Boolean);
      // parts on one line (within 16px of each other's middle) keep their own order, 1 above 2: the gutter has room for one
      // number per line, so the rest step down below it; hovering a legend item outlines the exact part
      var row = function (x) { return Math.round((x.top + x.h / 2) / 16); };
      spots.slice().sort(function (a, b) { return row(a) - row(b) || a.i - b.i; }).forEach(function (s) {
        var y = Math.max(s.top + s.h / 2 - 11, last + 24);   // at the part's middle, a step below the number above
        last = y;
        var n = document.createElement('span'); n.className = 'an-num'; n.textContent = String(s.i + 1);
        n.style.left = gutter + 'px'; n.style.top = y + 'px';
        var box = document.createElement('span'); box.className = 'an-box'; box.setAttribute('data-part', s.i);
        box.style.left = Math.max(0, s.left) + 'px'; box.style.top = s.top + 'px'; box.style.width = Math.max(0, Math.min(s.w, fb.right - sb.left - Math.max(0, s.left))) + 'px'; box.style.height = s.h + 'px';
        layer.appendChild(box); layer.appendChild(n);
      });
    });
  }
  stages.forEach(function (stage) {   // a legend item outlines its part while hovered or focused
    $$('li[data-part]', legendOf(stage)).forEach(function (li) {
      var n = li.getAttribute('data-part');
      ['mouseenter', 'focus'].forEach(function (ev) { li.addEventListener(ev, function () { show(stage, n, true); }); });
      ['mouseleave', 'blur'].forEach(function (ev) { li.addEventListener(ev, function () { show(stage, n, false); }); });
    });
  });
  place(false);
  window.addEventListener('load', function () { place(true); });
  var t; window.addEventListener('resize', function () { clearTimeout(t); t = setTimeout(function () { place(false); }, 100); });
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(function () { place(false); });
})();
