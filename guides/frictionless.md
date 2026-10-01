# Frictionless interaction

Friction is anything between the user's intent and the result: waiting, re-typing, extra clicks, confirmations, lost state, layout jumps, and having to guess what's clickable. A soft UI removes it and never draws attention to the fact.

## Response

- **Feedback on pointer-down**, not on release. Pressed state is instant.
- **Optimistic updates when reversible.** Show local feedback immediately; optimistically update only when failure can safely roll back. Preserve a retry path. Password changes, payments, and inventory posting show pending feedback and wait for server confirmation before announcing success.
- **Stream, don't block.** Long results appear progressively. The user can scroll, copy or stop while the result is still streaming in.
- **No layout shift.** Reserve space for images, async content and buttons that change label. Use `tabular-nums` for changing numbers. Skeletons match the final layout's shape.
- **Deep links render immediately.** Opening a URL to a detail view shows that view, not a see-through placeholder for seconds (measured on bencho.dev: 3–5s).
- **Loading only when it's > ~300ms.** Below that, show nothing. A flash of spinner feels slower than a short wait.

## Input

- **Move focus intentionally.** Focus the relevant control when opening a dialog. On initial page load, avoid stealing focus or unexpectedly opening the mobile keyboard.
- **Enter submits, Shift+Enter makes a newline** in chat-style inputs. `Esc` closes whatever is on top. `⌘K` opens search/commands.
- **Inputs grow with content** (auto-resizing textarea up to a max, then scroll).
- **Persist appropriate drafts** and scroll positions across navigation and reloads. Never persist passwords, payment credentials, or other sensitive fields as drafts; follow the product's retention requirements.
- **Forgiving parsing:** normalize fields whose semantics allow it, accept pasted formats, and preserve meaningful characters. Never trim passwords.
- **Validate on blur or submit**, never while the user is typing their first attempt. Put the error next to the field, in plain words, with the fix.

## Actions

- **Undo over confirm.** Delete immediately, show a toast with Undo (≈5s). Confirmations are only for irreversible and destructive actions, and those name the thing being destroyed.
- **Primary action is easy to reach** at the natural completion point of the task. Use sticky placement only when it does not obscure content or focused fields. Explain disabled actions.
- **Contextual controls appear on hover or focus** (copy, edit, retry on a message) but stay keyboard-reachable, and on touch they're always visible or behind a visible action menu.
- **Smart defaults** so most users never need settings.
- **Hit areas:** ≥ 32px on desktop, 44px on touch, even when the visible icon is 16px. When there's no room (a chip's ×), extend the target with an invisible `::after` 8px past the visible edge instead of enlarging the icon.
- **No dead zones:** items in menus and lists touch each other. Their breathing room comes from padding inside each item, not margin between them, so the hover highlight never flickers and clicks never land on nothing.
- **Tooltips:** the first one waits 400–700ms so passing through doesn't trigger it. Once one is open, neighbours open instantly.

## States (every component needs all of these)

default · hover · pressed · focus-visible · disabled (with reason) · loading · empty (with a next step) · error (with recovery) · success (quiet, often just the updated state).

## Copy

Short, calm, human. Sentence case. Say what happened and what to do next. No exclamation marks, no blame ("Couldn't save. Retry" not "Error: invalid request!").
