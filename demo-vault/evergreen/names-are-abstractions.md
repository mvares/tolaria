---
aliases:
  - "Names are abstractions"
"Is A":
  - Evergreen
"Created at": "2024-04-18T14:44:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to":
  - "[[essay/how-to-name-things|How to Name Things]]"
  - "[[monday-ideas/monday-80|Monday #80]]"
"Old Created At": "2023-10-06T15:21:00.000+02:00"
"Updated at": "2024-04-19T09:37:00.000Z"
Status: Not started
notion_id: 7fb1922b-e46d-4f73-bcb4-a3d96b7122d1
---

# Names are abstractions

A lot of the advice above is a variation of one of the golden rules in software: *do not create premature abstractions*.

Names and naming conventions are particularly *sneaky* because they may not feel like abstractions, but they are.

Conventions should encode something repetitive, so that when I see one I immediately understand what it does. Instead, codebases are often full of -*Managers*, *-Providers*, -*Services* that have pretty much nothing in common. When I see an *EmailManager*, I will ask myself: *what does a Manager do?* If there isn’t a good answer for that, then 1) it’s confusing, and 2) you are *polluting* the “Manager” keyword for anybody who wants to use it for good in the future.

Of course, it goes both ways: when there is a convention in place, you should use it whenever it is fitting.
