# review-ui

Use when checking UI before it ships. Report findings as a list ordered by severity, each with file/line and a concrete fix.

1. **Raw values** — any hex, px, font or shadow not coming from `tokens/tokens.json`.
2. **Reinvented components** — markup that duplicates something in `components/index.md`.
3. **States** — missing hover / focus-visible / disabled / loading / empty / error states.
4. **Dark mode** — every color has a dark counterpart and nothing is unreadable.
5. **Spacing & alignment** — values on the spacing scale, consistent rhythm, aligned edges.
6. **Accessibility** — semantics, keyboard, focus, labels, contrast.
7. **Responsive** — works at 360px wide with no horizontal scroll.
