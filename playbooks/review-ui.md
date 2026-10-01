# Review a rendered UI

Use before completing a UI implementation or when asked to review an existing interface. Match effort to the change: a small control edit needs a focused check; a multi-page redesign needs representative routes and states.

## Inspect and improve

1. Check composition against [page composition](../guides/page-composition.md): purpose, hierarchy, density, grouping, dominant action, and shared edges. Check component choices against [pattern selection](../guides/pattern-selection.md). Token compliance alone does not prove good design.
2. Render the actual implementation using available browser tooling. Inspect a desktop screenshot and a narrow viewport around 360px; check the product's supported themes. For a connected workflow, inspect each changed route and shared navigation. Do not substitute a mockup screenshot for implementation evidence.
3. Exercise the relevant interactions: navigation preserves context; keyboard focus is visible; dialogs close and restore focus; cancel does not save; pending states prevent duplicates; failures preserve appropriate input and offer recovery. Use isolated test data for mutations. Follow the environment's authorization and credential-entry rules.
4. Inspect representative loading, empty, error, and content states using existing fixtures or safe test mechanisms. Include long labels, large numbers, and translated text where supported. Avoid mutating real data simply to manufacture an empty state.
5. Fix high-impact issues, re-render the affected views, and repeat the failed checks. Stop when the requested task works, text is readable, the layout has no unintended overflow or overlap, and no material issues remain in the changed scope. Do not keep adding decorative polish after these checks pass.

## What to look for

- Clear selected navigation; appropriate links versus tabs versus segmented controls.
- Quiet surfaces, useful grouping, readable contrast, consistent tokens and icon sizing.
- Labels and units, meaningful empty-state action, field errors adjacent to fields.
- Designed inputs, buttons, and selects: coordinated sizes, readable text, visible focus, and polished open-popup states. Review against [controls](../guides/controls.md); reject untouched browser styling, not semantic HTML.
- Visible focus, accessible control names, touch targets, reduced-motion behavior when motion changed.
- No page-level horizontal overflow at narrow widths; wide tables scroll within their own region.
- No misleading success, fake statistics, unsupported Undo, lost drafts, or persisted secrets.
- Consistent design across the requested list/detail/edit screens, without expanding scope to unrelated routes.

## Report evidence honestly

For implementation work, briefly report what changed, which routes/viewports/interactions were checked, and any limitations. Save screenshots when the environment supports it; provide useful evidence without exposing secrets. If browser tooling or a required state is unavailable, state exactly what was not verified instead of claiming visual approval.

For a review-only request, report actionable findings ordered by impact with location, proposed correction, and reason. A table is optional; do not force a long compliance report for a small edit.
