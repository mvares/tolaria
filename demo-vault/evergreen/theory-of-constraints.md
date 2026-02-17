---
aliases:
  - "Theory of Constraints"
"Is A":
  - Evergreen
"Created at": "2024-04-18T14:44:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to":
  - "[[essay/mental-models-for-engineers-and-managers|Mental Models for Engineers and Managers]]"
  - "[[monday-ideas/monday-180|Monday #180]]"
"Old Created At": "2024-03-01T10:23:00.000+01:00"
"Updated at": "2025-10-28T09:49:00.000Z"
Status: Not started
notion_id: 869e4a4b-f8b5-494d-bd60-f1cd08519f7b
---

# Theory of Constraints

### 🔗 Theory of Constraints

The Theory of Constraints (TOC) is a model that views any system as being limited by a very small number of constraints — and, more immediately, by its weakest link.

The corollary of TOC is that, to improve the performance of a system, you should focus on bottlenecks, one at a time.

For example, you may measure the various steps of your release process and discover that the biggest bottleneck is the time the code spends idle waiting for review. Or you may trace your API calls and figure out that the largest chunk of response times come from the database.

TOC was introduced by Eliyahu M. Goldratt in his 1984 book titled [*The Goal*](https://en.wikipedia.org/wiki/The_Goal_(novel))*.* The author suggests a five-step process to improve a system’s performance:

1. **🔍 Identify** — the system's constraints.

1. **🎲 Decide** — how to *exploit* the system's constraints.

1. **🔀 Subordinate** — everything else to the above decision.

1. **⬆️ Elevate** — the system's constraints.

1. **🔄 Repeat** — this is a continuous improvement cycle. Once a constraint is addressed, you should move to the next.

If you want to learn more, here is the most thorough description of TOC I have found, which includes detailed guidance on each of the steps:

- 📑 [**Theory of Constraints — by Lean Production**](https://www.leanproduction.com/theory-of-constraints/)
