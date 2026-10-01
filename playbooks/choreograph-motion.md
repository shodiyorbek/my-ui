# Choreograph motion

Use for a multi-step flow, shared-surface transition, gesture or animated illustration. For a simple button or popover, use the existing [motion recipes](../guides/motion.md) directly.

## 1. Describe the behavior

Write a short implementation brief: what change motion explains, how often it occurs, start/end states, origin, animated properties, exit behavior, interruption behavior and reduced-motion alternative. Resolve routine choices from house defaults; do not turn this into a questionnaire for the user.

Define what must remain true: focus, entered data, selected item, scroll position, accessible names and the actual operation result. Motion must never invent progress or delay an available action.

## 2. Choose the smallest mechanism

- Use the project's accessible primitive for focus, keyboard navigation and dismissal. An animation library alone is not a dialog, menu or tabs implementation.
- CSS transitions suit simple reversible values. They can retarget an in-flight transition; a physics spring additionally carries velocity. A sampled CSS `linear()` spring curve is not a velocity-aware spring.
- During dragging, track the pointer directly. Apply the release spring and velocity after the user lets go; see [springs](../guides/springs.md).
- Reuse the installed library and check its current official API before borrowing a historical recipe. Add a dependency only when the interaction requires it.

## 3. Preserve continuity

- For next/back flows, choose direction from navigation intent and reading context. Give exiting content the latest direction as well as entering content. Keep stable state identities and preserve entered values.
- For shared surfaces, inspect both container geometry and content. Check parent transforms, clipping, text scaling and corner distortion with long content and narrow widths.
- If a visual crossfade needs duplicate layers, keep the duplicate inert and hidden from assistive technology. Maintain one live semantic control and avoid duplicate IDs or focus targets.
- Give each moving property one owner. Prefer one entrance for a group; avoid stacking parent movement with child stagger unless their separate purposes are clear.

## 4. Make sequences cancellable

Model illustration sequences with explicit phases such as idle, hover, pressed and exit. Cancel superseded timers and animations, and guard asynchronous completions so an old sequence cannot restart after a new action or unmount.

For SVG work, isolate transforms in groups and check coordinate space, `transform-box` and origin. Verify stroke caps at zero-length reveals; normalize path lengths when useful. Morphing paths require compatible geometry or suitable tooling, not arbitrary interpolation between unrelated path strings.

## 5. Tune and verify

When direction is genuinely uncertain, compare a few live variants with the same content and triggers. A small development-only timing control can help; do not build a tuning panel for every task.

Test rapid reversal, repeated clicks, exit during entry, long translations, changing content, narrow viewports and reduced motion. Check real focus and dismissal behavior separately from visual polish. Verify teardown leaves no running loop or stale update. Use [review-ui](review-ui.md) for the rest of the delivery checks.

Judge at normal speed first; slowed playback helps locate a defect. Keep the version that clarifies the user's task with less distraction. Record observed behavior and remaining gaps, rather than treating a pretty recording as proof of correctness.

Source context and review limitations: [Animations.dev study](../references/sites/animations-dev.md). This playbook is an original synthesis; it does not reproduce course examples.
