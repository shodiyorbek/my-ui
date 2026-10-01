# Choose patterns by behavior

Read the relevant rows before selecting a component. A component's presence in this library is not a reason to use it.

| User intent | Prefer | Decision boundary |
|---|---|---|
| Navigate related destinations, such as stock / movements / drafts | Text navigation links with a quiet active indicator | Use real links and preserve URL context. Do not add ARIA tab roles to ordinary route navigation. |
| Switch a small local mode, such as list / grid | Segmented control | Short, mutually exclusive options that change the same workspace; avoid long labels and unrelated destinations. |
| Switch local content panels | Accessible tabs | Implement the tab/tabpanel relationship and arrow-key behavior, preferably with the project's existing primitive. |
| Narrow a dataset | Search, filter, and sort controls | Display active filters and a clear reset. Distinguish no records from no matching results. |
| Compare many records across attributes | Table | Align numbers, label units, expose sort state; contain horizontal scroll if necessary. |
| Browse visually distinct objects | List or cards | Images and object identity should justify cards; do not cardify dense comparison data. |
| Edit a few fields in context | Dialog or small inline editor | Label the task, handle errors in place, manage focus, restore focus on close. |
| Complete a long or multi-step edit | Dedicated page; sometimes a side panel | Support navigation and recovery; avoid cramped scrolling dialogs or nested dialogs. |
| Perform occasional secondary actions | Context menu | Keep frequent or essential actions visible; do not hide everything behind an ellipsis. |
| Explain a failure or invalid input | Persistent inline error | Say what happened and how to recover. A transient toast must not be the only error. |
| Acknowledge a completed ordinary action | Updated content or quiet status | Use a toast when useful; do not show both a banner and toast for every success. |
| Perform a reversible low-risk deletion | Undo if supported by the backend | Do not promise recovery the system cannot provide. Confirm irreversible or consequential actions with specific wording. |

## Interaction contracts

Navigation retains relevant filters and context. Cancel preserves the original data. Escape closes the topmost dismissible surface without saving. Dialogs trap focus while open and restore it afterward; inline editors do not trap focus. Successful saves update the affected content. Failures retain non-sensitive input and offer a retry without duplicate submission.

Passwords are not trimmed, persisted as drafts, echoed from server actions, or placed in URLs. Payments, password changes, and inventory posting wait for confirmed success. Optimistic UI requires a defined rollback path.

## Examples of context-sensitive taste

- Stock / movements / drafts: quiet route links work better than a large pill switch when these are separate destinations.
- List / grid: a compact segmented switch can be appropriate because it changes representation, not location.
- A chat composer can be strongly rounded while its messages remain unboxed.
- A table may need subtle row separators even when a reading page does not.
- A marketing headline may be large and expressive while application settings headings stay restrained.

These are decision examples, not universal bans on pills, borders, cards, or color.
