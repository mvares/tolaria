---
aliases:
  - "Make things simple"
"Is A":
  - Evergreen
Tags:
  - Has Pic
"Created at": "2025-12-29T11:02:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to": "[[essay/the-ai-productivity-paradox|The AI Productivity Paradox]]"
"Updated at": "2025-12-29T11:03:00.000Z"
Status: Not started
Tweet: "Coordination exists due to cognitive load, leading to complexity in productivity. Layering causes bottlenecks and fractures context, making decision-making local rather than global. Different tools used by engineers and PMs create further obscurity. Advocating for a merger of layers, the vision for AI-enabled software engineering suggests three eras:\n\n↳ 𝗬𝗲𝘀𝘁𝗲𝗿𝗱𝗮𝘆: Web is simple, where one engineer does everything (PHP/JQuery era).\n↳ 𝗧𝗼𝗱𝗮𝘆: Web is complex, requiring specialized roles.\n↳ 𝗧𝗼𝗺𝗼𝗿𝗿𝗼𝘄: Web is complex but AI assists in reducing cognitive load, allowing engineers to manage multiple roles again."
notion_id: 2d8bdf02-815c-801d-b702-c0564c087183
---

# Make things simple

Coordination exists because of cognitive load: stuff is hard and people can’t fit everything into their heads. This leads to layering & specialization, which in turn makes coordination *required* to do things.

Some of this is necessary, but it’s important to understand that layering makes everything more complex. All of a sudden:

- Productivity is stiffer, because gains in one layer create bottlenecks elsewhere.

- Context about what to do gets *fractured* instead of being centralized, and more decisions are made based on local optima instead of global optima.

- Each layer uses its own tools and processes, making context more obscure and harder to recompose.

All of this is a mess for people, and it is especially a mess for AI. Engineers use Claude Code and store some specs in the repo, PMs use ChatPRD or what else, some stuff is on Notion, some on Jira, and so on.

So, call it product engineering or however you like, if you read Refactoring you probably know I am bullish on merging some layers and going back to when people just did *more*.

That’s my bullish case for AI — to enable a *third era* of software engineering:

- **Yesterday: Web is simple** → each engineer does everything, but the tech doesn’t scale. Basically the PHP / JQuery era.

- **Today: Web is complex** → the tech now scales, but is (too) complex and engineers need to be layered into frontend, backend, infra, and more.

- **Tomorrow: Web is complex but we have AI** → same tech as today, but engineers can delegate a good chunk of cognitive load to AI, and do everything again.

![image](../assets/2d8bdf02815c804a.png)

---
