---
aliases:
  - "It’s hard to keep Staging at parity with Prod"
"Is A":
  - Evergreen
"Last Tweeted": 2023-01-05
"Created at": "2024-04-18T14:44:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to":
  - "[[essay/do-you-really-need-a-staging-environment|Do you really need a Staging environment?]]"
  - "[[monday-ideas/monday-30|Monday #30]]"
"Old Created At": "2022-05-21T14:33:00.000+02:00"
"Updated at": "2024-04-19T09:37:00.000Z"
Status: Not started
notion_id: d62746cb-a743-4d6c-96d3-a4d10d33e14b
---

# It’s hard to keep Staging at parity with Prod

For Staging to be useful, it has to catch a special kind of issues that 1) would happen in production, but 2) wouldn’t happen on a developer laptop.

What are these? Think of problems with data migrations, database load and queries, and other infra-related problems.

To make Staging catch these issues, you need to keep it at parity with Production on data and infrastructure. This is hard and expensive — think about it, if it wasn’t so, you would just spin dev environments that look like prod.

The whole point of having a single, shared environment for testing instead of many individual ones is that the latter would be too expensive to maintain 👇

> *The way I see it, fundamentally, this is a resources management problem. If I wouldn't be looking at costs the dev environments could be designed and made powerful enough to satisfy all needs.

*[Alex Stoia](https://ro.linkedin.com/in/alex-stoia-6b759944), CTO at Innertrends

In my experience, however, most companies cut corners on this and end up with Staging setups that look nothing like Production. For example, they may hold a small fraction of the database, or run on totally different instances.

This defeats the purpose of Staging and makes it unable to do its job.

- [Untitled](https://www.notion.so/8316c17e21644d9b8458c8d91229f583) 
