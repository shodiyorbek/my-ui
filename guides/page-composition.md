# Page composition

Read when creating or redesigning a page or connected workflow. Start with the user's task, then choose the visual structure. See [annotated studies](../references/composition-studies.md) for examples.

## Ground the design

Inspect existing navigation, shared components, design tokens, real content, and relevant states. Identify the main user task and the action that completes it. State any consequential assumption briefly; ask only when missing intent changes the design materially.

For a redesign, map the requested routes and their connected states: list → detail → create/edit → result. Identify shared headers, tabs, filters, and action patterns. Update the requested scope consistently; flag adjacent gaps without silently expanding the assignment. Preserve query parameters, store/tenant context, permissions, and deep links.

## Choose the right composition

| Product | Content and density | Navigation and action |
|---|---|---|
| Conversational / writing app | Comfortable reading measure, plain flowing content, generous separation between turns | Quiet history sidebar; composer close to the content; visible stop/retry/error states |
| Operational dashboard | Wide work surface, compact readable rows, aligned numeric columns, filters near results | Stable section navigation, explicit active state, one dominant workflow action; local row actions stay secondary |
| Marketing website | Strong headline, deliberate section rhythm, meaningful product imagery or demonstration | Clear value proposition and next step; allow expressive type and brand color when appropriate |
| Settings / forms | Constrained field width, labels above fields, related options grouped | Separate independent forms and their submit actions; explain consequences next to the action |

Do not impose a chat-width column on tables or a dashboard's dense controls on a landing page. Desktop and mobile may use different compositions while preserving the same task.

## Compose before decorating

- Establish three levels: page purpose, task controls, working content. The content gets most of the space.
- Align headings, controls, and content to shared edges. Use more space between groups than within them.
- Use a card only when it represents a distinct object, grouped task, or useful surface boundary. Plain text and lists can sit directly on the page. Avoid card-inside-card structures with no semantic benefit.
- Give each task or independent form a dominant action. Supporting navigation and utility actions should be quieter. Never make a global Save button appear to save an unrelated form.
- Add summary metrics only when they inform a decision, with real values and meaningful units. Do not invent KPI cards to fill space.
- Choose density for frequency of use and information volume. Empty space should aid scanning, not force daily operators to scroll through oversized controls.
- Use real or representative long names, translated labels, missing images, large values, and zero/one/many rows when evaluating the layout. Mark demonstration data as such; never substitute it for live failures.

## Adapt without hiding the task

At narrow widths, wrap controls in priority order; collapse secondary navigation; preserve labels and the main action. A genuinely wide table may scroll in a contained, discoverable region, but the page itself should not overflow. Use sticky controls only when they do not cover content, focused fields, or the software keyboard.

Support browser zoom and text growth. Do not truncate the only explanation of an error or action. Icon-only controls require accessible names and discoverability on touch.

## Final composition check

Can a new user identify the page purpose, current location, main action, and next step without guessing? Can a returning user finish the frequent task with little navigation? If not, fix hierarchy or workflow before adding shadows or animation.
