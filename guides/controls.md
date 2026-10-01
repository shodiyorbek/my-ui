# Inputs, buttons, and selects

Use for forms, filters, search, toolbars, and any actionable control. The house preference is deliberately designed controls, not untouched browser styling or unmodified library defaults. These are visual defaults, not permission to replace semantic HTML with clickable divs.

## One control family

Reuse existing project primitives first. Match adjacent controls in height, baseline, radius, type weight, and icon scale. Use the project tokens or the house defaults: 36px compact desktop, 40px regular, 44px touch; 8–12px corner radius; 14–16px text; 12–16px horizontal padding; 16px icons. Prefer 16px input text on narrow touch screens to avoid unwanted mobile zoom. Use consistent SVG icons from the project's icon set; do not substitute Unicode arrows or emoji whose alignment varies by platform.

Quiet surfaces still need discoverable boundaries. Use a subtle ring or border, with stronger contrast on hover and a clearly visible focus outline. Keep text readable. Avoid decorative gradients, deep shadows, permanent glow, excessive pill shapes, and focus effects that move the layout.

## Inputs

- Use real input/textarea elements inside a styled field or input-group primitive. Keep labels visible above fields; placeholders demonstrate a format and never replace labels.
- Use a clear surface, quiet boundary, deliberate padding, and room for text. Match search fields to adjacent filters instead of shrinking their text.
- Put leading icons, unit suffixes, and trailing actions in dedicated slots. Reserve space so text never runs underneath. Mark decorative icons hidden from assistive technology; label action buttons.
- Search may have a leading search icon and a clear action when nonempty. Passwords may have an accessible show/hide action. Do not add icons solely to decorate every field.
- Keep help and errors below the field, associated with aria-describedby. Use aria-invalid for errors and explain the correction in words, not red alone.
- Preserve input type, name, autocomplete, inputmode, selection, paste, autofill, and password-manager support. Do not trim passwords or suppress autofill to make the field look cleaner.
- Provide default, hover, focus, filled, invalid, disabled, and readonly states. Readonly remains selectable and readable; disabled is not a loading state.

## Buttons

Default to a rounded rectangle for forms and toolbars; use pills when the product context calls for them, not universally. Primary is high-contrast neutral; secondary has a quiet surface/ring; ghost is for lower-priority tools. Keep a dominant action per task, without forcing unrelated forms to share a submit button.

Use verb-led labels, consistent icon placement, and balanced padding. Give icon-only actions an accessible name and an adequate target. Use real buttons for actions and links for navigation. Specify type="button" for controls that must not submit a form.

Pending buttons keep their footprint and communicate progress. Prevent repeated submission in the handler as well as the UI. Do not fade the entire button until its pending label becomes unreadable. Press feedback is subtle; reduced-motion users do not need scale animations. Keep a visible focus ring in every variant.

## Select versus combobox versus menu

| Need | Pattern |
|---|---|
| Choose one value from a short known list | Designed Select trigger + accessible listbox popup |
| Find a product, customer, or other large dataset | Searchable Combobox; expose loading, no matches, and retry states |
| Run commands such as edit, export, archive | Menu button with menu actions, not a Select |
| Lightweight no-framework form or deliberate mobile picker | Styled native select may be appropriate; retain its native picker behavior |

The preferred app Select has an aligned trigger, trailing chevron, selected value, and quiet focus treatment. Its popup uses a matching surface, subtle elevation, rounded corners, padded option rows, highlighted keyboard focus, and a selected checkmark. Match trigger width unless content needs more space; cap height, scroll inside, and reposition near viewport edges. Selection must not change merely because an option is hovered.

Use the accessible Select/Combobox already present in the project. If one is missing, choose a maintained primitive such as Base UI, Radix Select, or React Aria appropriate to the stack. Do not install several competing libraries. Verify the installed version's API before implementing.

Do not create a bespoke dropdown from a div and click handlers. A custom control must support its primitive's keyboard model, Escape dismissal, focus return, typeahead where applicable, accessible naming, selected/disabled states, form value/reset, and touch interaction. A searchable combobox must preserve text editing and IME composition. Test inside dialogs and near screen edges.

A styled native select is an intentional fallback, not a fully custom menu: appearance:none changes the closed trigger, not necessarily the operating-system popup. Do not promise complete popup styling from CSS alone. If a task specifically requires custom menus, use a supported accessible primitive rather than that fallback.

## Review before delivery

Inspect a row containing an input, a select, and a button together. Check alignment, text size, padding, and focus at desktop and touch widths. Open the select; inspect the popup as well as the trigger. Exercise keyboard navigation, Escape, selection, and form submission. Test long values, invalid input, disabled controls, loading, supported themes, and zoom. Report unavailable browser checks honestly.

## Research basis

These house choices synthesize [the primary-source research](../references/modern-controls.md); they are not a claim that one vendor's styling is universally best.
