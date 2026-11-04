/* The design-system docs' own script (Lesson 9, step 2, 2026-11-04): the overview (index.html), every component page
   (components/*.html) and why.html load it. Two jobs, each only where its markup is:
   1. the Light / Dark switch ([data-kd-theme]): <html data-theme="light"> here and in every same-origin frame (the tab
      bar stages are srcdoc frames); kept for the tab as design-system/tokens/theme.js keeps it, and in the URL. Light is
      the stress test of the semantic roles; Onrace ships dark only (C5).
   2. the anatomy ([data-anatomy] on a component page): numbers each part of the live stage, from its selector, with a
      box round it. A selector that finds nothing throws, so scripts/check_overflow.mjs fails the build.
   Documentation only: it never runs on a product screen. */
(function () {
  // ---------------------------------------------------------------- 1. the theme
  var themeBtns = Array.prototype.slice.call(document.querySelectorAll('[data-kd-theme]'));
  function docs() {
    return [document].concat(Array.prototype.slice.call(document.querySelectorAll('iframe')).map(function (f) {
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
  document.querySelectorAll('iframe').forEach(function (f) { f.addEventListener('load', function () { setTheme(current, false); }); });
  themeBtns.forEach(function (b) { b.addEventListener('click', function () { current = b.getAttribute('data-kd-theme'); setTheme(current, true); }); });

  // ---------------------------------------------------------------- 2. the anatomy
  var stages = Array.prototype.slice.call(document.querySelectorAll('[data-anatomy]'));
  if (!stages.length) return;
  function find(stage, sel) {   // the stage first, then its same-origin frames (the tab bar)
    var el = stage.querySelector('.kit-frame ' + sel) || stage.querySelector(sel);
    if (el && !el.closest('.an-layer')) return { el: el, frame: null };
    var frames = stage.querySelectorAll('iframe');
    for (var i = 0; i < frames.length; i++) {
      var d; try { d = frames[i].contentDocument; } catch (e) { d = null; }
      var hit = d && d.querySelector(sel);
      if (hit) return { el: hit, frame: frames[i] };
    }
    return null;
  }
  function place(strict) {
    stages.forEach(function (stage) {
      var parts = JSON.parse(stage.getAttribute('data-anatomy'));
      var layer = stage.querySelector('.an-layer');
      if (!layer) { layer = document.createElement('div'); layer.className = 'an-layer'; layer.setAttribute('aria-hidden', 'true'); stage.appendChild(layer); }
      layer.textContent = '';
      var box = stage.getBoundingClientRect(), W = stage.clientWidth, taken = [];
      parts.forEach(function (p, i) {
        var hit = find(stage, p[0]);
        if (!hit) { if (strict) throw new Error('anatomy: "' + p[0] + '" (' + p[1] + ') finds nothing on its stage'); return; }
        var r = hit.el.getBoundingClientRect(), dx = 0, dy = 0;
        if (hit.frame) { var fr = hit.frame.getBoundingClientRect(); dx = fr.left; dy = fr.top; }
        var left = Math.max(0, r.left + dx - box.left), top = Math.max(0, r.top + dy - box.top);
        var width = Math.min(r.width, W - left), height = r.height;
        var b = document.createElement('span'); b.className = 'an-box';
        b.style.left = left + 'px'; b.style.top = top + 'px'; b.style.width = Math.max(0, width) + 'px'; b.style.height = height + 'px';
        // the number sits on the box's top-left corner, outside it where there's room; one already there pushes it right
        var nx = Math.max(0, Math.min(left - 11, W - 22)), ny = Math.max(0, top - 11);
        function clash() { return taken.some(function (q) { return Math.abs(q[0] - nx) < 24 && Math.abs(q[1] - ny) < 24; }); }
        for (var k = 0; k < 40 && clash(); k++) {
          if (nx + 24 <= W - 22) nx += 24; else { nx = Math.max(0, Math.min(left - 11, W - 22)); ny += 24; }
        }
        taken.push([nx, ny]);
        var n = document.createElement('span'); n.className = 'an-num'; n.textContent = String(i + 1);
        n.style.left = nx + 'px'; n.style.top = ny + 'px';
        layer.appendChild(b); layer.appendChild(n);
      });
    });
  }
  place(false);
  window.addEventListener('load', function () { place(true); });
  var t; window.addEventListener('resize', function () { clearTimeout(t); t = setTimeout(function () { place(false); }, 100); });
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(function () { place(false); });
})();
