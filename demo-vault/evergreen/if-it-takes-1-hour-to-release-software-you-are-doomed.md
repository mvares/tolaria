---
aliases:
  - "If it takes 1 hour to release software you are doomed"
"Is A":
  - Evergreen
"Last Tweeted": 2023-04-13
Tags:
  - Has Pic
  - Not for Monday
"Created at": "2024-04-18T14:44:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to":
  - "[[essay/do-you-really-need-a-staging-environment|Do you really need a Staging environment?]]"
  - "[[monday-ideas/monday-8|Monday #8]]"
"Old Created At": "2022-05-21T14:36:00.000+02:00"
"Updated at": "2024-04-19T09:37:00.000Z"
Status: Not started
Tweet: When software releases take an hour or more due to staging bottlenecks, it creates a vicious cycle. Developers context switch, testing suffers, and features get batched, increasing risk and complicating debugging. CTOs, let's discuss how to streamline releases for better control and efficiency. What strategies have you found effective?
notion_id: 2d4b272d-fefb-4b4c-b3d0-3f535c3a132d
---

# If it takes 1 hour to release software you are doomed

When releases take **one hour** or more, because they get bottlenecked on Staging, a vicious cycle happens:

- Devs start to **context switch** to other tasks while the release is in progress.

- **Less testing** and monitoring in production get done because devs lose control of when code is released.

- “**Only in the morning**” releases (or worse, “only beginning of the week”), instead of multiple times a day.

- Multiple **features are batched** and released together for convenience, which makes releases riskier, harder to debug, and it further muddies single devs’ ownership of the release. 
