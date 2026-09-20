/* MIT © Jakub Antalik — inspired by the searching/globe algorithm in thinking-orbs. */
(function () {
  "use strict";
  var canvas = document.getElementById("thinking-orb-canvas");
  if (!canvas || !canvas.getContext) return;
  var intro = document.getElementById("a-propos");
  if (intro && canvas.parentElement) intro.insertBefore(canvas.parentElement, intro.querySelector(".profile-aside"));
  var ctx = canvas.getContext("2d");
  var reduced = window.matchMedia("(prefers-reduced-motion: reduce)");
  var visible = true, hidden = document.hidden, raf = 0, start = performance.now();
  var resizeObserver = "ResizeObserver" in window ? new ResizeObserver(resize) : null;
  function delta(a, b) { return Math.atan2(Math.sin(a - b), Math.cos(a - b)); }
  function resize() {
    var box = canvas.getBoundingClientRect(), size = Math.max(1, Math.min(box.width, box.height));
    var dpr = Math.min(window.devicePixelRatio || 1, 2);
    canvas.width = Math.round(size * dpr); canvas.height = Math.round(size * dpr);
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    draw(reduced.matches ? 0 : (performance.now() - start) / 1000);
  }
  function draw(time) {
    var size = Math.min(canvas.clientWidth, canvas.clientHeight); if (!size) return;
    var center = size / 2, radius = size * 0.41, yaw = time * 0.5;
    var tilt = 0.4 + Math.sin(time * 0.35) * 0.06, scan = time * 1.7;
    var st = Math.sin(tilt), ct = Math.cos(tilt), sy = Math.sin(yaw), cy = Math.cos(yaw), dots = [];
    ctx.clearRect(0, 0, size, size);
    for (var li = 0; li <= 17; li += 1) {
      var lat = -Math.PI / 2 + li / 17 * Math.PI, cl = Math.cos(lat), sl = Math.sin(lat);
      var lonCount = Math.max(1, Math.round(Math.abs(cl) * 44));
      for (var lj = 0; lj < lonCount; lj += 1) {
        var lon = lj / lonCount * Math.PI * 2, x = cl * Math.cos(lon), y = sl, z = cl * Math.sin(lon);
        var px = x * cy + z * sy, rz = -x * sy + z * cy, py = y * ct - rz * st, depthZ = y * st + rz * ct;
        var depth = (depthZ + 1) / 2, boost = Math.exp(-(delta(lon + time * 0.5, scan) ** 2) / 0.18) * Math.max(0, depthZ);
        dots.push({ x: center + px * radius, y: center - py * radius, z: depthZ, r: 0.45 + 1.25 * depth + 0.75 * boost, a: 0.22 + 0.55 * Math.min(1, depth + boost) });
      }
    }
    dots.sort(function (a, b) { return a.z - b.z; });
    dots.forEach(function (dot) {
      var shade = Math.round(55 + (1 - dot.z) * 46);
      ctx.fillStyle = "rgba(" + shade + "," + (shade + 16) + "," + (shade + 10) + "," + dot.a * 0.58 + ")";
      ctx.beginPath(); ctx.arc(dot.x, dot.y, dot.r, 0, Math.PI * 2); ctx.fill();
    });
  }
  function resume() { if (!raf && !reduced.matches && visible && !hidden) raf = requestAnimationFrame(tick); }
  function tick(now) { raf = 0; if (!reduced.matches && visible && !hidden) { draw((now - start) / 1000); resume(); } }
  function visibilityChange() { hidden = document.hidden; if (raf) cancelAnimationFrame(raf); raf = 0; resume(); }
  function motionChange() { if (raf) cancelAnimationFrame(raf); raf = 0; draw(reduced.matches ? 0 : (performance.now() - start) / 1000); resume(); }
  function intersection(entries) { visible = entries[0].isIntersecting; if (raf) cancelAnimationFrame(raf); raf = 0; resume(); }
  function cleanup() {
    if (raf) cancelAnimationFrame(raf);
    if (resizeObserver) resizeObserver.disconnect();
    if (observer) observer.disconnect();
    window.removeEventListener("resize", resize);
    document.removeEventListener("visibilitychange", visibilityChange);
    reduced.removeEventListener ? reduced.removeEventListener("change", motionChange) : reduced.removeListener(motionChange);
  }
  resizeObserver && resizeObserver.observe(canvas);
  window.addEventListener("resize", resize, { passive: true });
  document.addEventListener("visibilitychange", visibilityChange);
  reduced.addEventListener ? reduced.addEventListener("change", motionChange) : reduced.addListener(motionChange);
  var observer = "IntersectionObserver" in window ? new IntersectionObserver(intersection, { threshold: 0 }) : null;
  if (observer) observer.observe(canvas);
  window.addEventListener("pagehide", cleanup, { once: true });
  resize(); resume();
}());
