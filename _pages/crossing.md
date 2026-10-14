---
title: "Would you cross?"
description: "Try a two-minute version of a crowdsourced experiment on how automated cars should communicate with pedestrians, and compare yourself with 1,434 participants."
layout: gridlay
permalink: /crossing/
---

# Would you cross?

An automated car approaches while you stand at a zebra crossing. Some cars stop for you, some do not, and some show a message on an external human-machine interface (eHMI). **Hold the space bar (or press and hold on the scene) whenever you feel safe to cross**, and let go when you do not. There are 8 short trials, about a minute in all. This is a shortened version of a [crowdsourced study](/p/bazilinskyy2021should) with 1,434 participants. Your answers stay in your browser: nothing is sent or stored.

<div markdown="0" id="xing">
<canvas id="xing-cv" aria-label="Street scene with an approaching car" role="img"></canvas>
<div id="xing-bar"><span id="xing-status">Press Start when you are ready.</span><button id="xing-start" class="btn-doi" type="button">Start</button></div>
<div id="xing-results"></div>
</div>

<style>
#xing { max-width: 800px; }
#xing-cv { display: block; width: 100%; aspect-ratio: 16 / 9; border-radius: 5px; touch-action: none; user-select: none; -webkit-user-select: none; cursor: pointer; }
#xing-bar { display: flex; justify-content: space-between; align-items: center; gap: 10px; margin: 6px 0; font-size: 90%; }
#xing-results table { width: 100%; font-size: 90%; margin: 8px 0; }
#xing-results td { padding: 3px 6px; vertical-align: middle; }
#xing-results .bar { height: 12px; border-radius: 2px; background: var(--chart-bar-hover); }
#xing-results .num { width: 3.5em; text-align: right; font-variant-numeric: tabular-nums; }
</style>

<script>
(function () {
  // Kinematics as in the study: 50 km/h; a yielding car brakes from 35 m and stops in front of the crossing.
  const V = 50 / 3.6, BRAKE_AT = 35, STOP_AT = 2, EHMI_AT = 50, START = 60;
  const DECEL = V * V / (2 * (BRAKE_AT - STOP_AT));
  const TRIALS = [  // yielding, message, colour, position
    {y: true, msg: '', label: 'Stops, no eHMI'},
    {y: true, msg: 'WALK', col: '#22c55e', pos: 'bumper', label: 'Stops, green WALK on the bumper'},
    {y: true, msg: 'WILL STOP', col: '#06b6d4', pos: 'bumper', label: 'Stops, cyan WILL STOP on the bumper'},
    {y: true, msg: 'bar', col: '#22c55e', pos: 'bumper', label: 'Stops, green light bar on the bumper'},
    {y: true, msg: 'WALK', col: '#22c55e', pos: 'windshield', label: 'Stops, green WALK on the windshield'},
    {y: false, msg: '', label: 'Does not stop, no eHMI'},
    {y: false, msg: "DON'T WALK", col: '#ef4444', pos: 'bumper', label: "Does not stop, red DON'T WALK on the bumper"},
    {y: false, msg: "WON'T STOP", col: '#ef4444', pos: 'bumper', label: "Does not stop, red WON'T STOP on the bumper"},
  ];
  const cv = document.getElementById('xing-cv'), ctx = cv.getContext('2d');
  const status = document.getElementById('xing-status'), startBtn = document.getElementById('xing-start'), out = document.getElementById('xing-results');
  let W, H, F, HY, order = [], idx = -1, t0 = 0, held = false, heldMs = 0, lastT = 0, running = false, results = [];

  function size() {
    const dpr = devicePixelRatio || 1, w = cv.clientWidth;
    cv.width = Math.round(w * dpr); cv.height = Math.round(w * 9 / 16 * dpr);
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    W = w; H = w * 9 / 16; F = W * 0.75; HY = H * 0.42;
  }
  // camera 1.6 m high on the kerb at x = 0, looking down the road; the lane is to the left
  const px = (x, z) => W * 0.62 + F * x / z, py = (y, z) => HY + F * (1.6 - y) / z;

  function distance(tr, t) {  // distance of the car's front to the crossing at time t (s)
    const d = START - V * t;
    if (!tr.y || d > BRAKE_AT) return d;
    const tb = (START - BRAKE_AT) / V, s = t - tb, tStop = V / DECEL;
    return s >= tStop ? STOP_AT : BRAKE_AT - (V * s - DECEL * s * s / 2);
  }
  const duration = tr => tr.y ? (START - BRAKE_AT) / V + V / DECEL + 1.5 : (START + 8) / V;

  function quad(pts, fill) {
    ctx.beginPath(); pts.forEach(([x, y], i) => i ? ctx.lineTo(x, y) : ctx.moveTo(x, y)); ctx.closePath();
    ctx.fillStyle = fill; ctx.fill();
  }
  function scene() {
    const sky = ctx.createLinearGradient(0, 0, 0, HY);
    sky.addColorStop(0, '#8ec5ea'); sky.addColorStop(1, '#dcecf7');
    ctx.fillStyle = sky; ctx.fillRect(0, 0, W, HY);
    ctx.fillStyle = '#9aa5ad'; ctx.fillRect(0, HY, W, H - HY);  // pavement
    const far = 400, near = 0.8;
    quad([[px(-7, near), py(0, near)], [px(-7, far), py(0, far)], [px(0, far), py(0, far)], [px(0, near), py(0, near)]], '#454b52');  // road
    for (let z = 6; z < far; z += 9)  // centre line
      quad([[px(-3.6, z), py(0, z)], [px(-3.6, z + 4), py(0, z + 4)], [px(-3.4, z + 4), py(0, z + 4)], [px(-3.4, z), py(0, z)]], '#e9e3c9');
    for (let x = -6.6; x < -0.2; x += 1)  // zebra crossing from z = 1 to 4
      quad([[px(x, 1), py(0, 1)], [px(x, 4), py(0, 4)], [px(x + 0.5, 4), py(0, 4)], [px(x + 0.5, 1), py(0, 1)]], '#f4f4f0');
  }
  function car(tr, d, active) {
    const z = 4 + d;
    if (z < 0.4) return;  // passed the camera
    const X = -1.75, w = 1.8, x0 = px(X - w / 2, z), x1 = px(X + w / 2, z), s = F / z;
    const y = h => py(h, z);
    ctx.fillStyle = 'rgba(0,0,0,.25)'; ctx.beginPath(); ctx.ellipse((x0 + x1) / 2, y(0), (x1 - x0) * 0.6, s * 0.12, 0, 0, 2 * Math.PI); ctx.fill();
    ctx.fillStyle = '#e8edf2'; ctx.beginPath(); ctx.roundRect(x0, y(0.95), x1 - x0, y(0.18) - y(0.95), s * 0.12); ctx.fill();  // body
    quad([[px(X - 0.72, z), y(0.95)], [px(X - 0.55, z), y(1.45)], [px(X + 0.55, z), y(1.45)], [px(X + 0.72, z), y(0.95)]], '#d5dce3');  // cabin
    quad([[px(X - 0.66, z), y(1.0)], [px(X - 0.53, z), y(1.38)], [px(X + 0.53, z), y(1.38)], [px(X + 0.66, z), y(1.0)]], '#2b3640');  // windshield
    ctx.fillStyle = '#1d2329';
    ctx.fillRect(px(X - 0.78, z), y(0.18), s * 0.3, s * 0.18); ctx.fillRect(px(X + 0.48, z), y(0.18), s * 0.3, s * 0.18);  // wheels
    ctx.fillStyle = '#fff8d6';
    ctx.fillRect(px(X - 0.82, z), y(0.78), s * 0.32, s * 0.1); ctx.fillRect(px(X + 0.5, z), y(0.78), s * 0.32, s * 0.1);  // lights
    if (!active || !tr.msg) return;
    const wind = tr.pos === 'windshield', top = wind ? 1.3 : 0.6, h = tr.msg === 'bar' ? 0.07 : 0.2;
    const ex = px(X - 0.5, z), ey = y(top), ew = s * 1.0, eh = s * h;
    ctx.fillStyle = wind ? 'rgba(0,0,0,0)' : '#111'; ctx.fillRect(ex, ey, ew, eh);
    if (tr.msg === 'bar') { ctx.fillStyle = tr.col; ctx.fillRect(ex + ew * 0.05, ey, ew * 0.9, eh); return; }
    ctx.fillStyle = tr.col; ctx.font = `bold ${eh * 0.82}px system-ui, sans-serif`; ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
    ctx.fillText(tr.msg, ex + ew / 2, ey + eh / 2, ew * 0.95);
  }
  function overlay(text) {
    ctx.fillStyle = 'rgba(0,0,0,.45)'; ctx.fillRect(0, 0, W, H);
    ctx.fillStyle = '#fff'; ctx.font = `600 ${H * 0.07}px system-ui, sans-serif`; ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
    ctx.fillText(text, W / 2, H / 2);
  }
  function badge() {  // the pedestrian's answer, so the key press shows
    ctx.fillStyle = held ? '#16a34a' : 'rgba(0,0,0,.5)';
    ctx.beginPath(); ctx.roundRect(W - W * 0.3, H * 0.04, W * 0.27, H * 0.09, H * 0.02); ctx.fill();
    ctx.fillStyle = '#fff'; ctx.font = `600 ${H * 0.045}px system-ui, sans-serif`; ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
    ctx.fillText(held ? 'Safe to cross' : 'Not safe', W - W * 0.165, H * 0.085);
  }

  function frame(now) {
    if (!running) return;
    requestAnimationFrame(frame);
    const tr = TRIALS[order[idx]], t = (now - t0) / 1000;
    if (t < 0) { scene(); overlay(`Trial ${idx + 1} of ${order.length}`); lastT = now; return; }
    if (held) heldMs += now - Math.max(lastT, t0);
    lastT = now;
    const d = distance(tr, t);
    scene(); car(tr, d, d <= EHMI_AT); badge();
    if (t >= duration(tr)) { results.push({tr, share: heldMs / (duration(tr) * 1000)}); next(); }
  }
  function next() {
    idx++; heldMs = 0;
    if (idx >= order.length) return finish();
    status.textContent = `Trial ${idx + 1} of ${order.length}: hold space or press the scene when you feel safe to cross.`;
    t0 = performance.now() + 1200;  // a short pause with the trial number
  }
  function start() {
    order = TRIALS.map((_, i) => i).sort(() => Math.random() - 0.5);
    idx = -1; results = []; out.replaceChildren(); startBtn.disabled = true; running = true;
    next(); requestAnimationFrame(frame);
  }
  function finish() {
    running = false; held = false; startBtn.disabled = false; startBtn.textContent = 'Again';
    scene(); overlay('Done, see your results below');
    status.textContent = 'Done. Share of each trial you felt safe to cross:';
    const rows = results.slice().sort((a, b) => TRIALS.indexOf(a.tr) - TRIALS.indexOf(b.tr));
    const table = document.createElement('table');
    for (const r of rows) {
      const tr = table.insertRow(), pct = Math.round(100 * r.share);
      tr.insertCell().textContent = r.tr.label;
      const bar = tr.insertCell(); bar.style.width = '35%';
      Object.assign(bar.appendChild(document.createElement('div')), {className: 'bar'}).style.width = pct + '%';
      Object.assign(tr.insertCell(), {className: 'num', textContent: pct + '%'});
    }
    const note = document.createElement('p');
    note.innerHTML = 'What 1,434 participants did in the <a href="/p/bazilinskyy2021should">full study</a>: for cars that stopped, ' +
      'they felt safer with <b>WALK</b> than with <b>WILL STOP</b>, followed by the light bar; eHMIs on the <b>bumper</b> and roof ' +
      'worked better than on the <b>windshield</b>; and green and cyan felt safer than red. Do your bars agree? ' +
      'More in the <a href="https://github.com/bazilinskyy/crossing-crowdsourcing" target="_blank">code of such experiments</a>.';
    out.append(table, note);
  }

  const press = v => e => { if (running) { held = v; e.preventDefault(); } };
  addEventListener('keydown', e => { if (e.code === 'Space') press(true)(e); });
  addEventListener('keyup', e => { if (e.code === 'Space') press(false)(e); });
  cv.addEventListener('pointerdown', press(true));
  for (const ev of ['pointerup', 'pointercancel', 'pointerleave']) cv.addEventListener(ev, press(false));
  startBtn.addEventListener('click', e => { startBtn.blur(); start(); });
  document.addEventListener('visibilitychange', () => { if (document.hidden) held = false; });  // a key let go in another tab never arrives
  addEventListener('resize', () => { size(); if (!running) { scene(); car(TRIALS[1], 20, true); } });
  size(); scene(); car(TRIALS[1], 20, true);
})();
</script>
