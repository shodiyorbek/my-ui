# Button

**Purpose:** the one pressable control. It's soft by default: pill-shaped, neutral, with barely-felt press feedback.

## Variants

| Class | Use |
|---|---|
| `btn--primary` | The single main action in a view (inverted neutral: black on light, white on dark) |
| `btn--subtle` | Secondary actions. Surface with a shadow ring, no border |
| `btn--ghost` | Toolbars, icon actions, tertiary. Background appears only on hover |

Sizes: `btn--sm` (32px), default (36px), `btn--lg` (40px), and `btn--icon` for a square. Icon-only buttons need `aria-label`.

## Usage

```html
<link rel="stylesheet" href="tokens/tokens.css">
<link rel="stylesheet" href="components/button/button.css">

<button class="btn btn--primary">Continue</button>
<button class="btn btn--subtle">Cancel</button>
<button class="btn btn--ghost btn--icon btn--sm" aria-label="Copy"><svg>…</svg></button>
```

React/Tailwind: keep the class names, or port the rules into `cva` variants using the same token variables.

## Do / Don't

- Do: one `primary` per view, and show a reason when disabled (tooltip or helper text).
- Do: put a label change inside the button (e.g. "Copy" → "Copied") and swap icons with the icon cross-fade from `guides/motion.md`.
- Don't: add borders, colored ghosts, or scale below `0.97`.
- Don't: use a spinner that changes the button's width. Keep the label and fade it.

## Tokens used

`color-primary`, `color-primary-fg`, `color-surface`, `color-surface-hover`, `color-text`, `color-text-muted`, `color-focus`, `shadow-ring`, `shadow-ring-hover`, `shadow-primary`, `radius-full`, `size-control*`, `space-*`, `text-*`, `weight-medium`, `duration-press`, `duration-release`, `duration-hover`, `ease-out`.
