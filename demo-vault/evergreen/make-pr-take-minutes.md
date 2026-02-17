---
aliases:
  - "Make PR take minutes"
"Is A":
  - Evergreen
Tags:
  - Has Pic
"Created at": "2025-02-11T10:19:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to":
  - "[[essay/the-path-to-engineering-maturity|The Path to Engineering Maturity]]"
  - "[[monday-ideas/monday-148|Monday #148]]"
"Updated at": "2025-03-18T15:15:00.000Z"
Status: Not started
Tweet: "CTOs, here's a critical insight: PRs that take minutes to approve lead to significantly better performance. When reviews drag into hours or days, context switches increase, workflows degrade, and risks multiply. Let’s prioritize quick reviews to keep teams agile and productive. Thoughts? #DevOps #TechLeadership"
notion_id: 197bdf02-815c-8096-aac9-ca695d1d2d4f
---

# Make PR take minutes

Data about how long it takes to get a PR approved is also interesting: there are no decisive differences when the time ranges between 1 hour and 1 day, but performance is 1) significantly better when PRs take *minutes* to get approved, and 2) significantly worse when they take *days*.

![image](../assets/197bdf02815c8059.png)

Why is that? Our interpretation is the following:

- 🥇 **When a PR takes minutes** — be it because PRs are small, people pair on reviews, or everyone stops on their tracks to review code — there is little to no context switch for the submitter, which leads to less work in progress, tasks getting closed faster, and all kinds of benefits down the line.

- 🥈 **When a PR takes between 1 hour and one day** — the submitter needs to switch to other tasks. At that point whether the review takes 1 hour or, say, 4, there isn’t a lot of difference in terms of workflow.

- 🥉 **When a PR takes days** — the workflow degrades considerably as multiple changes need to get batched together, which creates more risk, more outages, rework, and a worse feedback loop.
