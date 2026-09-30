// Headless test of lib/spring.js: run with `node scripts/test-spring.mjs`. Fake rAF clock; compares to the closed-form spring.
import fs from 'node:fs';
let now = 0, queue = [];
globalThis.performance = { now: () => now };
globalThis.requestAnimationFrame = (cb) => { queue.push(cb); return queue.length; };
globalThis.cancelAnimationFrame = () => { queue = []; };
globalThis.matchMedia = () => ({ matches: false });
eval(fs.readFileSync(new URL('../lib/spring.js', import.meta.url), 'utf8'));
const { createSpring, project, rubberband } = globalThis.mySpring;
const tick = (ms = 1000 / 60) => { now += ms; const q = queue; queue = []; q.forEach((cb) => cb(now)); };
const exact = (t, z = 1, R = 0.4) => { const w = 2 * Math.PI / R; return 1 - Math.exp(-w * t) * (1 + w * t); };

// 1. matches closed form (0 -> 1, smooth)
let out = 0; const s = createSpring({ value: 0, onUpdate: (v) => (out = v) });
s.to(1); let maxErr = 0, t0 = now;
for (let i = 0; i < 30; i++) { tick(); maxErr = Math.max(maxErr, Math.abs(out - exact((now - t0) / 1000))); }
console.log('max error vs closed form:', maxErr.toFixed(4)); if (maxErr > 1e-3) process.exitCode = 1;

// 2. rests exactly on target
for (let i = 0; i < 120 && s.isAnimating; i++) tick();
console.log('rested:', !s.isAnimating, 'value:', s.value); if (s.isAnimating || s.value !== 1) process.exitCode = 1;

// 3. retarget mid-flight: no jump, velocity preserved
const s2 = createSpring({ value: 0 }); s2.to(100);
for (let i = 0; i < 8; i++) tick();
const before = { x: s2.value, v: s2.velocity }; s2.to(0);
console.log('retarget keeps position:', s2.value === before.x, 'keeps velocity:', s2.velocity === before.v, `(v=${before.v.toFixed(0)}px/s)`);
tick(); console.log('first frame after retarget still moving forward:', s2.value > before.x); if (!(s2.value > before.x)) process.exitCode = 1;

// 4. velocity handoff: flick continues in the flick direction first
const s3 = createSpring({ value: 0 }); s3.to(0, { velocity: 2000 }); tick();
console.log('flick carries momentum:', s3.value > 0); if (!(s3.value > 0)) process.exitCode = 1;

// 5. helpers
console.log('project(1000px/s):', project(1000).toFixed(0) + 'px', '| rubberband(200, 400):', rubberband(200, 400).toFixed(1) + 'px');
