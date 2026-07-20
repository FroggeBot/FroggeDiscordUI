# DiscordUI

Shared discord.py/py-cord rendering primitives for the Frogge ecosystem's Bot and Worker
processes. Both depend on the same py-cord library but never share code directly (see the
`FroggeBot`/`FroggeWorker` repos' own `ffxivvenues.py` client, deliberately duplicated rather
than shared) — this package exists specifically for the pieces where that duplication would be
dangerous rather than merely repetitive: a live posted message's interactive buttons are routed
by custom_id back to the Bot's own dispatch table, so whichever process builds that message must
reproduce the exact same rendering and custom_id format, or clicks fail silently in production
with no compile-time or test-time signal.

Contains only pure functions of `Schemas`-typed data and `discord.ui` objects — no Bot-only
`Interaction`-driven navigation/modal/picker scaffolding (that stays in `Bot/src/bot/ui/`, since
Worker has no interactions to respond to). `Bot` re-exports every name this package defines from
its own historical locations (`bot/colors.py`, `bot/ui/components/_core.py`,
`bot/cogs/reaction_roles/posts.py`) so no other file in the Bot codebase needed to change.
