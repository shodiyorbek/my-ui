// Interruptible, velocity-aware springs with no dependencies. Use for gestures (drag, flick, sheets)
// when the project has no animation library. With Motion, use its spring with stiffness/damping instead.
// Plain script: exposes only window.mySpring (wrapped, so it never collides with page globals). In a bundled app, copy the functions and `export` them.

(() => {
/** Presets match tokens.json `spring` (damping ratio + response in seconds). */
const SPRINGS = {
  snappy: { dampingRatio: 1, response: 0.3 },
  smooth: { dampingRatio: 1, response: 0.4 },
  gentle: { dampingRatio: 1, response: 0.55 },
  flick: { dampingRatio: 0.85, response: 0.4 },
};

/**
 * Animate a number with a spring. Retargeting keeps position AND velocity, so a moving element can be
 * grabbed or redirected mid-flight with no jump.
 *   const s = createSpring({ value: 0, onUpdate: (v) => (el.style.transform = `translateY(${v}px)`) });
 *   s.to(300);                       // animate
 *   s.to(0, { velocity: -1200 });    // hand off release velocity (px/s)
 *   s.set(120);                      // jump (e.g. while dragging), stops motion
 */
function createSpring({ value = 0, preset = 'smooth', onUpdate, onRest } = {}) {
  let x = value, v = 0, target = value, frame = 0, last = 0, range = 1;
  let { dampingRatio, response } = SPRINGS[preset] ?? preset;

  // Exact solution of the damped oscillator from the current state, so retargets and any frame rate
  // (60/120Hz, dropped frames) land precisely on the true spring curve.
  const advance = (dt) => {
    const w0 = 2 * Math.PI / response, z = dampingRatio;
    const x0 = x - target, v0 = v;
    let xt, vt;
    if (z < 1) {
      const wd = w0 * Math.sqrt(1 - z * z), e = Math.exp(-z * w0 * dt), cos = Math.cos(wd * dt), sin = Math.sin(wd * dt);
      const b = (v0 + z * w0 * x0) / wd;
      xt = e * (x0 * cos + b * sin);
      vt = e * ((-z * w0) * (x0 * cos + b * sin) + (-x0 * wd * sin + b * wd * cos));
    } else if (z === 1) {
      const e = Math.exp(-w0 * dt), b = v0 + w0 * x0;
      xt = e * (x0 + b * dt);
      vt = e * (b - w0 * (x0 + b * dt));
    } else {
      const wd = w0 * Math.sqrt(z * z - 1), r1 = -z * w0 + wd, r2 = -z * w0 - wd;
      const c2 = (v0 - r1 * x0) / (r2 - r1), c1 = x0 - c2;
      xt = c1 * Math.exp(r1 * dt) + c2 * Math.exp(r2 * dt);
      vt = c1 * r1 * Math.exp(r1 * dt) + c2 * r2 * Math.exp(r2 * dt);
    }
    x = target + xt;
    v = vt;
  };

  const step = (now) => {
    advance(Math.min((now - last) / 1000, 0.064));
    last = now;
    // Rest thresholds scale with the distance travelled: 0.1% of it (px, opacity, scale all work)
    const resting = Math.abs(target - x) < range * 0.001 && Math.abs(v) < range * 0.01;
    if (resting) { x = target; v = 0; }
    onUpdate?.(x);
    if (resting) { frame = 0; onRest?.(x); } else frame = requestAnimationFrame(step);
  };

  const start = () => { if (!frame) { last = performance.now(); frame = requestAnimationFrame(step); } };

  return {
    to(next, { velocity, preset: p } = {}) {
      target = next;
      range = Math.max(Math.abs(next - x), Math.abs(velocity ?? v) * 0.1, 1e-3);
      if (velocity !== undefined) v = velocity;
      if (p) ({ dampingRatio, response } = SPRINGS[p] ?? p);
      if (matchMedia('(prefers-reduced-motion: reduce)').matches) { this.set(next); onRest?.(next); return; }
      start();
    },
    set(next) { cancelAnimationFrame(frame); frame = 0; x = target = next; v = 0; onUpdate?.(x); },
    get value() { return x; },
    get velocity() { return v; },
    get isAnimating() { return frame !== 0; },
  };
}

/** Where a flick would come to rest (Apple's scroll-deceleration projection). velocity in px/s. */
function project(velocity, decelerationRate = 0.998) {
  return (velocity / 1000) * decelerationRate / (1 - decelerationRate);
}

/** Resistance past a boundary: the further you pull, the less it follows. */
function rubberband(overshoot, dimension, constant = 0.55) {
  return (overshoot * dimension * constant) / (dimension + constant * Math.abs(overshoot));
}

/** Tracks pointer samples and returns release velocity in px/s (last ~100ms). */
function velocityTracker() {
  let samples = [];
  return {
    add(position, time = performance.now()) {
      samples.push({ position, time });
      samples = samples.filter((s) => time - s.time <= 100);
    },
    velocity() {
      if (samples.length < 2) return 0;
      const a = samples[0], b = samples[samples.length - 1];
      return b.time === a.time ? 0 : ((b.position - a.position) / (b.time - a.time)) * 1000;
    },
    reset() { samples = []; },
  };
}

globalThis.mySpring = { SPRINGS, createSpring, project, rubberband, velocityTracker };
})();
