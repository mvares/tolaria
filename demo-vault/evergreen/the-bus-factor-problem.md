---
aliases:
  - "The bus factor problem"
"Is A":
  - Evergreen
"Created at": "2025-11-05T14:22:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to":
  - "[[essay/interview-with-adam-tornhill|Interview with Adam Tornhill]]"
  - "[[monday-ideas/monday-186|Monday #186]]"
"Updated at": "2025-12-11T18:14:00.000Z"
Status: Not started
notion_id: 2a2bdf02-815c-80a2-a548-edff01d15d8c
---

# The bus factor problem

Perhaps one of the most alarming findings from Adam's analysis is the widespread exposure to "bus factor" risk — how many people can leave an organization before code becomes unmaintainable.

The numbers are sobering: in a typical codebase with 50 developers working on millions of lines of code, the bus factor might be as low as just 2-3 people.

> ***"It turns out that almost all codebases, no matter how large the development team is, are quite exposed to a risk known as the bus factor... your bus factor might be as low as just two, three people, which is really, really scary."***

This concentration happens due to several factors:

- 🏗️ **Early contributor advantage** — developers who join projects early create more code when there are fewer constraints

- 🧠 **Historical knowledge** — long-term contributors accumulate deep understanding of decisions and context

- ⚡ **Productivity differences** — individual capability variations compound over time

Adam's approach to mitigating bus factor risk involves combining three analyses:

- Identifying which areas would be impacted if key people left

- Determining whether those areas are hotspots (frequently changed) or stable

- Assessing the code health of at-risk areas

When code checks all three risk boxes, Adam recommends pairing knowledge-holders with other team members for collaborative refactoring — simultaneously distributing knowledge and improving code quality.
