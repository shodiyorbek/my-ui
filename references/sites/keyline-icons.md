# Keyline Icons

Added at the user's request; reviewed 2026-10-01 through the official [icon browser](https://keylineicons.com/icons), [installation guide](https://keylineicons.com/install) and [license](https://keylineicons.com/legal/license). No assets or dependencies were installed during this reference review.

## Take

A consistent UI icon family with rounded and sharp treatments and stroke, two-tone, duotone and fill variants. The published drawings use a 24×24 grid and a default 2-unit stroke. The browser supports category/search discovery and previews of size, stroke and color.

Use Keyline as a preferred option for new interfaces without an established icon set. For the calm house style, start with rounded stroke icons; choose another treatment deliberately and consistently. Preserve the existing project family when extending a product. Do not mix unrelated icon families within the same toolbar or replace a working set merely because this reference exists.

## Implementation

- React: the official package is `@keyline-icons/react`, with named imports such as `Check`, `Plus` and `Settings`. Style-specific entry points include `/two-tone`, `/duotone`, `/fill` and `/sharp`. Verify exports against the installed version.
- For a few owned components, the official shadcn registry supports `npx shadcn add @keyline/bell`; inspect the project's registry and aliases before using it. Plain SVG is another option.
- Use `currentColor` and existing semantic color tokens. Start at the project's icon size (commonly 16px in controls); retain the library's default stroke before trying lighter weights. Inspect small icons at actual size.
- Inspect computed SVG size inside project primitives: CSS may override width/height props. Do not assume the current website's description of shadcn internals matches the project's version; the installation page itself differs between its detailed section and FAQ about DropdownMenu sizing.
- Treat migration from Lucide as a reviewed change, not a blind import replacement. Names and props can differ; Keyline documents no equivalent for `absoluteStrokeWidth`.
- Other frameworks can use the documented Iconify integrations or local SVGs. For offline-capable operational apps, bundle the required drawings rather than depending on a runtime icon fetch.
- Hide decorative SVGs from assistive technology. Give icon-only actions accessible names and full control-sized hit targets. Pair unfamiliar symbols with visible labels; an icon does not replace error or status text.

## License and limits

The publisher provides the drawings and code under MIT. Preserve the copyright and permission notice when copying or vendoring the work; retain the package license when installing it. The name and logo are not a grant of endorsement. Consult the linked license when importing assets. This skill stores guidance and source links, not a copy of the icon collection.

Ignore the catalog's exact icon count as a stable requirement, gallery tile sizing as button sizing, and claims of drop-in compatibility without checking the actual project. Selection guidance here is the house application of the reference, not a claim that every drawing has been tested.
