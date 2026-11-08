/* The design-system docs' own script (Lesson 9; the shell since 2026-11-05). Every page of design-system/docs/ loads
   it; each job runs only where its markup is. Documentation only: it never runs on a product screen.
   1. the Light / Dark switch ([data-kd-theme]): <html data-theme="light"> here and in every same-origin frame (the tab
      bar stages are srcdoc frames); kept for the tab as design-system/tokens/theme.js keeps it, and in the URL. Light is
      the stress test of the semantic roles; Onrace ships dark only (C5).
   2. the shell (scripts/docs_shell.py): the menu on a phone, the nav's filter, and the section on screen marked in
      "On this page" (the nav marks the page itself).
   3. the specimen: cropped to the component when it is a small part of its stage, and the parts legend under it; a
      legend item outlines its part while hovered, focused or pressed. A selector that finds nothing throws, so
      scripts/check_overflow.mjs fails the build. */
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
  // the filter (the navigation restructure, 2026-11-08): a page stays when its names hold the words (a component's names
  // include the entries shown on its page); a section heading or a group's sub-heading stays while one of its pages does
  var filter = document.getElementById('ds-filter'), empty = document.querySelector('.ds-empty');
  if (filter && nav) filter.addEventListener('input', function () {
    var q = filter.value.trim().toLowerCase(), shown = 0;
    nav.classList.toggle('is-filtering', !!q);
    $$('.ds-list > li:not(.ds-sub)', nav).forEach(function (li) {
      var hit = !q || li.firstChild.getAttribute('data-names').indexOf(q) > -1;
      li.hidden = !hit; if (hit) shown++;
    });
    $$('.ds-sub', nav).forEach(function (sub) {   // a group's sub-heading: shown while a page after it, before the next one, is
      var n = sub.nextElementSibling, any = false;
      while (n && !n.classList.contains('ds-sub')) { if (!n.hidden) any = true; n = n.nextElementSibling; }
      sub.hidden = !any;
    });
    $$('.ds-list', nav).forEach(function (ul) { var vis = !!ul.querySelector('li:not(.ds-sub):not([hidden])'); ul.hidden = !vis; if (ul.previousElementSibling) ul.previousElementSibling.hidden = !vis; });
    if (empty) empty.hidden = !q || shown > 0;
  });
  // the section in view: the last one whose heading has passed just under the sticky header (or the last section once the
  // page can't scroll further), marked in "On this page" and in the current family's list in the nav. Read on every
  // scroll frame: an observer that fires only when a section enters a band lags a section behind (fixed 2026-11-05).
  var sections = $$('.ds-main .dc[id], .ds-main .dc-why[id], .ds-main .dc-entry[id], .ds-main .ds-group[id]');
  if (sections.length) {
    var marks = $$('.ds-toc a');
    var shown = null;
    var mark = function () {
      var line = (document.querySelector('.ds-head') || { offsetHeight: 0 }).offsetHeight + 48, cur = sections[0];
      sections.forEach(function (s) { if (s.getBoundingClientRect().top <= line) cur = s; });
      if (innerHeight + scrollY >= document.documentElement.scrollHeight - 2) cur = sections[sections.length - 1];
      if (cur === shown) return; shown = cur;
      marks.forEach(function (a) { if (a.getAttribute('href').split('#')[1] === cur.id) a.setAttribute('aria-current', 'true'); else a.removeAttribute('aria-current'); });
    };
    var queued = false;
    window.addEventListener('scroll', function () { if (!queued) { queued = true; requestAnimationFrame(function () { queued = false; mark(); }); } }, { passive: true });
    window.addEventListener('resize', mark); window.addEventListener('load', mark); window.addEventListener('hashchange', function () { requestAnimationFrame(mark); });
    mark();
  }

  // ---------------------------------------------------------------- 3. the anatomy and the crop
  // A crop window ([data-crop] on .an-window) shows a component on its own when its parts cover a small share of their
  // stage (the Sign out button inside the whole Profile screen): the stage inside keeps its width and every style, the
  // window only hides the rest; the rules' "See it" links show it on its screen. Used for the specimen and the variants.
  // The legend under the specimen ([data-anatomy] on .dc-spec, the legend its next sibling): each part a button; hover,
  // focus or a tap (it stays pressed) outlines that exact part. A selector that finds nothing throws, so
  // scripts/check_overflow.mjs fails the build. No numbers: the legend names each part (2026-11-05).
  var PAD = 16, SHARE = 0.6;   // the room round a cropped component; above this share of the stage, it shows as it is
  function find(root, sel) {   // in the stage first, then its same-origin frames (the tab bar)
    var el = root.querySelector('.kit-frame ' + sel);
    if (el) return { el: el, frame: null };
    var frames = root.querySelectorAll('iframe');
    for (var i = 0; i < frames.length; i++) {
      var d; try { d = frames[i].contentDocument; } catch (e) { d = null; }
      var hit = d && d.querySelector(sel);
      if (hit) return { el: hit, frame: frames[i] };
    }
    return null;
  }
  function rectOf(hit) {
    var r = hit.el.getBoundingClientRect();
    if (!hit.frame) return { left: r.left, top: r.top, right: r.right, bottom: r.bottom };
    var f = hit.frame.getBoundingClientRect();
    return { left: r.left + f.left, top: r.top + f.top, right: r.right + f.left, bottom: r.bottom + f.top };
  }
  function crop(win) {
    var pan = win.firstElementChild, sels = JSON.parse(win.getAttribute('data-crop'));
    var cell = win.closest('.dc-state');   // a States cell lays its stage out at the cell's width, then shrinks to the crop
    if (cell) cell.style.width = '';
    win.classList.remove('is-cropped'); win.style.width = ''; win.style.height = ''; pan.style.transform = ''; pan.style.width = '';
    var full = win.parentNode.clientWidth;
    pan.style.width = full + 'px';   // the stage keeps the width it has uncropped
    var p = pan.getBoundingClientRect(), u = null;
    sels.forEach(function (s) {
      var hit = find(pan, s); if (!hit) return;
      var r = rectOf(hit);
      u = u ? { left: Math.min(u.left, r.left), top: Math.min(u.top, r.top), right: Math.max(u.right, r.right), bottom: Math.max(u.bottom, r.bottom) } : r;
    });
    if (!u || (!cell && (u.right - u.left) * (u.bottom - u.top) > SHARE * p.width * p.height)) return false;   // a States cell always crops to its part
    var x = Math.max(0, u.left - p.left - PAD), y = Math.max(0, u.top - p.top - PAD);
    win.style.width = Math.min(full, u.right - p.left + PAD - x) + 'px';
    win.style.height = Math.min(p.height - y, u.bottom - p.top + PAD - y) + 'px';
    pan.style.transform = 'translate(' + (-x) + 'px, ' + (-y) + 'px)';
    win.classList.add('is-cropped');
    if (cell) cell.style.width = win.style.width;
    return true;
  }
  function cropAll() { $$('.an-window[data-crop]').forEach(crop); }
  var stages = $$('[data-anatomy]');
  function outline(an) {   // the outlines of the parts whose legend item is hovered, focused or pressed
    var layer = an.querySelector('.an-layer');
    if (!layer) { layer = document.createElement('div'); layer.className = 'an-layer'; layer.setAttribute('aria-hidden', 'true'); an.appendChild(layer); }
    layer.textContent = '';
    var parts = JSON.parse(an.getAttribute('data-anatomy')), a = an.getBoundingClientRect();
    var win = an.querySelector('.an-window').getBoundingClientRect();
    $$('.an-part', an.nextElementSibling).forEach(function (b) {
      if (!(b.matches(':hover') || b === document.activeElement || b.getAttribute('aria-pressed') === 'true')) return;
      var hit = find(an, parts[+b.getAttribute('data-part')][0]); if (!hit) return;
      var r = rectOf(hit);
      var l = Math.max(r.left, win.left), t = Math.max(r.top, win.top), rr = Math.min(r.right, win.right), bb = Math.min(r.bottom, win.bottom);
      if (rr <= l || bb <= t) return;
      var box = document.createElement('span'); box.className = 'an-box';
      box.style.left = (l - a.left) + 'px'; box.style.top = (t - a.top) + 'px'; box.style.width = (rr - l) + 'px'; box.style.height = (bb - t) + 'px';
      layer.appendChild(box);
    });
  }
  function check() {   // every part finds its part on its stage
    stages.forEach(function (an) {
      JSON.parse(an.getAttribute('data-anatomy')).forEach(function (p) {
        if (!find(an, p[0])) throw new Error('anatomy: "' + p[0] + '" (' + p[1] + ') finds nothing on its stage');
      });
    });
  }
  stages.forEach(function (an) {
    var buttons = $$('.an-part', an.nextElementSibling);
    buttons.forEach(function (b) {
      ['mouseenter', 'mouseleave', 'focus', 'blur'].forEach(function (ev) { b.addEventListener(ev, function () { setTimeout(function () { outline(an); }); }); });
      b.addEventListener('click', function () {   // a tap pins it (touch has no hover); a second tap, or another part, lets go
        var on = b.getAttribute('aria-pressed') !== 'true';
        buttons.forEach(function (o) { o.setAttribute('aria-pressed', 'false'); });
        b.setAttribute('aria-pressed', String(on));
        outline(an);
      });
    });
  });
  function all() { cropAll(); stages.forEach(outline); }
  all();
  window.addEventListener('load', function () { all(); check(); });
  var t; window.addEventListener('resize', function () { clearTimeout(t); t = setTimeout(all, 100); });
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(all);
  $$('iframe').forEach(function (f) { f.addEventListener('load', all); });
})();
