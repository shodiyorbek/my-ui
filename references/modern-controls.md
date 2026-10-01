# Modern control references

Reviewed 2026-10-01 from official documentation. These are reference patterns, not copied source or a requirement to install every library.

| Source | Take | Adapt / avoid |
|---|---|---|
| [Radix Text Field](https://www.radix-ui.com/themes/docs/components/text-field) | Input groups with dedicated icon/action slots; coordinated sizes and surface variants | Choose product tokens rather than adopting every theme default |
| [Radix Button](https://www.radix-ui.com/themes/docs/components/button) | Consistent sizes, variants, and radius choices | Rounded rectangles or pills according to context; avoid making all controls primary |
| [Radix Select](https://www.radix-ui.com/themes/docs/components/select) | Separate trigger, value, and popup composition | Style the popup too; do not confuse value selection with command menus |
| [Base UI Select](https://base-ui.com/react/components/select) | Composable value-selection control for a custom design system | Reuse the installed primitive and verify its version rather than inventing props |
| [Base UI Combobox](https://base-ui.com/react/components/combobox) | Searchable selection for larger option sets | Do not add a search field to every tiny option list |
| [React Aria quality](https://react-aria.adobe.com/quality) | Visible labeling and accessibility, internationalization, and interaction behavior | Custom visuals must preserve these behaviors |
| [WAI-ARIA combobox pattern](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/) | Keyboard and focus expectations; preservation of native editing behavior | ARIA attributes alone do not implement the interaction |

House decisions: [controls guide](../guides/controls.md). The goal is custom visual treatment with dependable behavior, not a ban on native HTML controls.
