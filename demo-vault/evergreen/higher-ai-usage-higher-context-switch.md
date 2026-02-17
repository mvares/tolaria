---
aliases:
  - "Higher AI usage == higher context switch"
"Is A":
  - Evergreen
Tags:
  - Has Pic
"Created at": "2025-12-29T11:00:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to": "[[essay/the-ai-productivity-paradox|The AI Productivity Paradox]]"
"Updated at": "2025-12-29T11:03:00.000Z"
Status: Not started
Tweet: If a developer can implement a complete feature in 2 hours, but the PM needs 2 days to verify requirements, the workflow is compromised. This velocity mismatch can create bottlenecks in the system. Research by Faros indicates that higher AI usage in coding correlates with increased context switching and larger pull requests (PRs). Higher context switching occurs because fast coding leads developers to shift to other tasks while awaiting reviews, QA, or deployment, thereby increasing work in progress (WIP) and negatively impacting quality, which ultimately affects productivity.
notion_id: 2d8bdf02-815c-80ac-8a2f-ef2f52b51e04
---

# Higher AI usage == higher context switch

As it’s well known, software development is a pipeline, and coding is just one part of it.

If a developer can implement a complete feature in 2 hours, but the PM needs 2 days to verify requirements, you are cooked. Or maybe it took two days to *write* the requirements beforehand, and you are cooked anyway.

This velocity mismatch can happen at any step, and, because of how queues work, the step with the lowest throughput becomes a bottleneck for the whole system.

Bottlenecks have nasty second-order effects even on the *fast* steps: recent [research by Faros](https://www.faros.ai/blog/ai-software-engineering) shows that high AI usage in coding is strongly associated with higher context switch and bigger PRs 👇

![image](../assets/2d8bdf02815c8066.png)

Why higher context switch? Because when developers are quick at writing code but constantly need to wait for review / QA / deploy, they switch to other tasks to keep themselves busy, which increases WIP, which in turn impacts quality, which in turn comes back to bite productivity 👇
