# Segmented control

**Purpose:** pick one of 2–5 mutually exclusive views or modes (Chat / Code, Day / Week / Month). It uses Craft's clip-path thumb: a second copy of the labels in the selected style is clipped to the active segment, so the label color changes in exact sync with the moving thumb, with no mismatched cross-fade.

## Usage

```html
<link rel="stylesheet" href="components/segmented/segmented.css">

<div class="segmented" role="radiogroup" aria-label="Mode">
  <button class="segmented__option" role="radio" aria-checked="true">Chat</button>
  <button class="segmented__option" role="radio" aria-checked="false">Code</button>
</div>

<script src="components/segmented/segmented.js"></script>
<script>
  initSegmented(document.querySelector('.segmented'), { onChange: (i) => console.log(i) });
</script>
```

React: render the options and the overlay yourself, then set `--clip-left` / `--clip-right` from the selected option's `offsetLeft` / `offsetWidth` in a layout effect.

## Behaviour

- Arrow keys move the selection (radiogroup pattern). Only the selected option is in the tab order.
- No animation on first paint. Re-measures on resize.
- 250ms `--ease-out` on `clip-path`. Instant under `prefers-reduced-motion`.
- Track is a `--color-wash` pill with a 2px inset. The thumb is `--color-surface` with `--shadow-ring`, a pill inside a pill, so the radii are concentric by construction.

## Do / Don't

- Do: keep labels short and similar in length.
- Don't: use it for more than 5 options (use a select), or for actions (use buttons).

## Tokens used

`color-wash`, `color-surface`, `color-text`, `color-text-muted`, `color-focus`, `shadow-ring`, `radius-full`, `size-control-sm`, `space-3`, `text-sm`, `weight-medium`, `ease-out`.
