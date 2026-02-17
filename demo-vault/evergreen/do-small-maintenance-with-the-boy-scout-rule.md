---
aliases:
  - "Do small maintenance with the Boy Scout rule"
"Is A":
  - Evergreen
"Last Tweeted": 2023-09-09
"Created at": "2024-04-18T14:44:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to":
  - "[[essay/how-to-plan-for-maintenance|How to Plan for Maintenance]]"
  - "[[monday-ideas/monday-71|Monday #71]]"
"Old Created At": "2023-04-27T15:16:00.000+02:00"
"Updated at": "2024-04-19T09:37:00.000Z"
Status: Not started
notion_id: 5d900dfb-4849-43c1-a3cc-de71370ec240
---

# Do small maintenance with the Boy Scout rule

### 🏅 Boy Scout Rule

> ***Always leave the code better than you found it.***
— Robert Martin (Uncle Bob)

The boy scout rule, coined by Robert Martin, is about taking the chance to improve the code whenever you are already making changes to that code, for any other reasons. Think of adding a test that wasn’t there, or updating a small dependency. 

This approach works well, but not for everything. A few upsides and downsides:

- 🟢 **It avoids context-switch** — it makes the change cheaper than scheduling a separate task

- 🟢 **It doesn’t require negotiation** — it is just agreed that estimates keep some *slack *for this type of tasks.

- 🔴 **Timeline is best-effort **— doing such improvements depends on other tasks, so it’s only suitable for issues that can afford to wait kind of indefinitely.

- 🔴 **Only suitable for very small tasks **— Adding a few hours to improve existing tests is ok, but you can’t slip e.g. two days of maintenance on top of two days of feature work with the *boy scout rule*. I have seen it happen and it breaks trust. Don’t do it.  

A corollary of the rule is to *do immediately* whatever is too small to be otherwise tracked and planned.

> ***"Will it take less than two minutes?" Yes, then do it.
****— *David Allen, Getting Things Done

This is lifted straight from the [GTD](https://en.wikipedia.org/wiki/Getting_Things_Done) methodology, where David Allen advocates to do on the spot any task that requires less than two minutes to complete, like sending a short email or making up the bed.

In software, you might want to put the threshold to 5-10 mins, and there are plenty of stuff that falls into this:

- Small cosmetic updates to the UI

- Very small bugs

- Changing a piece of copy

In these cases, you will spend more time creating a ticket and pondering (multiple times in the long run) when to do it, than just by doing it on the spot. So do it, or ignore it forever (which is equally ok).
