#!/usr/bin/env python3
"""Spring math shared by build_tokens.py and the springs guide.

A spring is described the Apple way: damping ratio (1 = no overshoot) and response (seconds for one
undamped period). Conversions to other APIs, verified against motion@13.4.6 source:
  stiffness = (2*pi / response)**2      (mass = 1)
  damping   = 2 * damping_ratio * sqrt(stiffness)
  Motion    { visualDuration: response / 1.2, bounce: 1 - damping_ratio }

CLI:  python scripts/spring.py 1 0.4     -> prints every API's parameters and a CSS linear() easing
"""
import math
import sys


def physics(damping_ratio: float, response: float) -> tuple[float, float]:
    stiffness = (2 * math.pi / response) ** 2
    return stiffness, 2 * damping_ratio * math.sqrt(stiffness)


def position(t: float, damping_ratio: float, response: float) -> float:
    """Progress 0→1 of a unit spring starting at rest."""
    w0 = 2 * math.pi / response
    z = damping_ratio
    if z < 1:
        wd = w0 * math.sqrt(1 - z * z)
        return 1 - math.exp(-z * w0 * t) * (math.cos(wd * t) + (z * w0 / wd) * math.sin(wd * t))
    if z == 1:
        return 1 - math.exp(-w0 * t) * (1 + w0 * t)
    wd = w0 * math.sqrt(z * z - 1)
    r1, r2 = -z * w0 + wd, -z * w0 - wd
    return 1 - (r2 * math.exp(r1 * t) - r1 * math.exp(r2 * t)) / (r2 - r1)


def settle_time(damping_ratio: float, response: float, tolerance: float = 0.001) -> float:
    """First time after which the spring stays within `tolerance` of the target."""
    step, t, last_outside = 0.001, 0.0, 0.0
    while t < 5:
        if abs(1 - position(t, damping_ratio, response)) > tolerance:
            last_outside = t
        t += step
    return round(last_outside + step, 3)


def css_linear(damping_ratio: float, response: float, samples: int = 40) -> tuple[str, int]:
    """CSS linear() easing plus the duration (ms) it must be paired with."""
    duration = settle_time(damping_ratio, response)
    points = []
    for i in range(samples + 1):
        p = i / samples
        points.append(f"{position(p * duration, damping_ratio, response):.4f}".rstrip("0").rstrip(".") or "0")
    points[0], points[-1] = "0", "1"
    return f"linear({', '.join(points)})", round(duration * 1000)


def describe(damping_ratio: float, response: float) -> str:
    k, c = physics(damping_ratio, response)
    easing, ms = css_linear(damping_ratio, response)
    overshoot = max(position(i / 1000 * ms / 1000, damping_ratio, response) for i in range(1001)) - 1
    return "\n".join([
        f"damping ratio {damping_ratio}, response {response}s",
        f"  settles in        {ms}ms, overshoot {max(overshoot, 0) * 100:.1f}%",
        f"  Motion (time)     {{ type: 'spring', visualDuration: {response / 1.2:.3f}, bounce: {1 - damping_ratio:.2f} }}",
        f"  Motion (physics)  {{ type: 'spring', stiffness: {k:.0f}, damping: {c:.1f}, mass: 1 }}",
        f"  SwiftUI           .spring(response: {response}, dampingFraction: {damping_ratio})",
        f"  Reanimated        withSpring(v, {{ stiffness: {k:.0f}, damping: {c:.1f}, mass: 1 }})",
        f"  CSS               {ms}ms {easing}",
    ])


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("usage: spring.py <damping_ratio> <response_seconds>")
    print(describe(float(sys.argv[1]), float(sys.argv[2])))
