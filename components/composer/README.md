# Composer

**Purpose:** the main text input for chat and AI-style UIs, modeled on the ChatGPT desktop composer. It's a large soft container that grows with the text.

## Structure

```html
<form class="composer">
  <textarea class="composer__input" rows="1" placeholder="Ask anything" autofocus></textarea>
  <div class="composer__bar">
    <button type="button" class="btn btn--ghost btn--icon btn--sm" aria-label="Attach"><svg>…</svg></button>
    <button type="submit" class="btn btn--primary btn--icon btn--sm composer__send" aria-label="Send" disabled><svg>…</svg></button>
  </div>
</form>
```

## Behaviour (see `guides/frictionless.md`)

- Autofocus on load and after sending.
- `Enter` sends, `Shift+Enter` adds a newline. Don't send while an IME composition is active (`event.isComposing`).
- The send button is disabled while the input is empty and enabled as soon as there's text. It never moves or changes size.
- Sending is optimistic: clear the input and show the message immediately. While a reply streams, the send button becomes a stop button (use the icon cross-fade).
- Persist the draft per conversation.
- Grows up to 200px, then scrolls inside.

## Do / Don't

- Do: raise it with `shadow-float` on focus instead of a colored focus border.
- Don't: add a visible border, a label above it, or a character counter unless there's a real limit.

## Tokens used

`color-surface`, `color-text`, `color-text-muted`, `shadow-ring`, `shadow-float`, `radius-xl`, `space-*`, `text-md`, `leading-normal`, `duration-hover`.
