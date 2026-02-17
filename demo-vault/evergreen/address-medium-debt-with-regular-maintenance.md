---
aliases:
  - "Address medium debt with regular maintenance"
"Is A":
  - Evergreen
"Created at": "2024-04-18T14:44:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to": "[[essay/how-to-manage-technical-debt|How to Manage Technical Debt]]"
"Old Created At": "2022-02-04T11:11:00.000+01:00"
"Updated at": "2024-04-19T09:37:00.000Z"
Status: Not started
notion_id: 67708def-0264-45cb-8ccc-45bc88fbd0f5
---

# Address medium debt with regular maintenance

Medium Debt is about issues you need to prioritize and schedule, because they are somewhat impactful, but you can still fix them in between a few hours and a couple of days.

Examples are:

- Automate a tedious manual process

- Adjust performance of a small service that’s been degrading over time

- Remove a bottleneck in the CI/CD pipeline to shave a few minutes off the deploy time

How should you address these?

In my experience, the best approach is to allocate a **fixed time** every sprint to spend on such maintenance. The right share largely depends on your team and product, but it might be anything between 10% to 40%. If you need to spend more than 40%, you should probably address debt at a more strategic level (see *large debt*).

You can also decide to assign fixed days to this (e.g. Fridays) to build the habit.

This is not the only possible approach. There are teams who put these tasks in a backlog together with new product features, prioritize the ones against the others and plan what to do sprint by sprint. While this is not wrong by itself, it has a few drawbacks:

- **Expensive** — negotiating tech debt against product work every sprint can bring serious overhead, especially for minor tasks.

- **Apples vs oranges** — sometimes it’s hard to identify the ROI of small maintenance tasks (e.g. refactoring a small module).

- **Unreliable** — if you have to negotiate it every time, it is more likely that maintenance will be left behind when you are under pressure, and more generally it will be harder to keep a consistent pace.
