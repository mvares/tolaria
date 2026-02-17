---
aliases:
  - "Address small tech debt with the boyscout rule"
"Is A":
  - Evergreen
"Last Tweeted": 2022-06-03
"Created at": "2024-04-18T14:44:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to":
  - "[[essay/how-to-manage-technical-debt|How to Manage Technical Debt]]"
  - "[[monday-ideas/monday-2|Monday #2]]"
"Old Created At": "2022-02-04T11:10:00.000+01:00"
"Updated at": "2024-04-19T09:37:00.000Z"
Status: Not started
notion_id: 8e8633ff-f125-497a-ba8a-bbb8cc9f3ee9
---

# Address small tech debt with the boyscout rule

Small debt is about minor improvements you can make in a few hours of time. A few examples:

- Add missing tests

- Deduplicate some code by creating a simple abstraction

- Adjust a piece of code to make it adhere to your codebase conventions

The best way to address small debt is to make these changes whenever you are working on that code for any other reason. You basically follow [Robert C. Martin’s boy scout rule](https://www.oreilly.com/library/view/97-things-every/9780596809515/ch08.html):

> Always leave the code better than you found it.

This is effective, as opposed to scheduling an independent task, because it avoids context-switch and makes the change cheaper. However, it also means the timeline for such improvements is *best-effort* (it depends on other tasks), so it is only suitable for issues that are not too harmful.
