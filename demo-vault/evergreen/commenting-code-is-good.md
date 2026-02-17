---
aliases:
  - "Commenting code is good"
"Is A":
  - Evergreen
"Last Tweeted": 2023-05-24
"Created at": "2024-04-18T14:44:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to":
  - "[[essay/what-is-code-quality|What is Code Quality?]]"
  - "[[monday-ideas/monday-52|Monday #52]]"
"Old Created At": "2022-11-25T17:24:00.000+01:00"
"Updated at": "2024-04-19T09:37:00.000Z"
Status: Not started
notion_id: c2d4cef3-87a0-42f0-a986-5594b908a227
---

# Commenting code is good

Commenting code is a somewhat controversial practice, as many developers believe that *good code documents itself*.

I found, instead, that top performing teams are consistently good at commenting code, by focusing on the right amount of comments that provide the most value to the codebase.

Here is more about common types of comments:

- ✅ **Comments at the top of the file/class** — a few lines to describe the file’s primary goal can go a long way to help maintainers. It also helps to avoid scope creep over time and to keep the file true to its original goal.

- ✅ **Comments on complex functions** — most functions should be simple enough to be understandable *as-it-is*, but there are algorithms and processes that cannot be so, no matter how well you write them. In these cases, it helps to include a description of the inputs, the logic, and the outputs of the function.

- ❌ **In-line comments** — while there is value in explaining the workings of a complex function, the need to comment single lines of code is most often a code smell. If people understand what the function does but not some of its lines, there is probably something you can rework, rather than commenting the lines themselves.

Code comments are also easier to keep up to date with respect to docs that live elsewhere, as you may update them in place whenever you are making changes to the code itself.

Likewise, it is easy to spot in PRs whenever somebody is changing the code without updating the comments, and report it.

---

Commenting code ✏️ has become a somewhat controversial practice, as many developers believe that good code documents itself.

A small thread 👇

Personally I found, instead, that top performing teams are consistently good at commenting code, by focusing on the right amount of comments that provide the most value to the codebase.

Here is more about common types of comments:

1. ✅ Comments at the top of the file/class

A few lines to describe the file’s primary goal can go a long way to help maintainers. It also helps to avoid scope creep over time and to keep the file true to its original goal.

1. ✅ Comments on complex functions

Most code should be understandable as-is, but there are algorithms and processes that cannot be so, no matter how well you write them.

In these cases, you can include a description of the inputs, the logic, and the outputs of the function.

1. ❌ In-line comments

While there is value in explaining the workings of a complex function, the need to comment single lines of code is most often a code smell.

If people understand what the function does but not some of its lines, there is probably something you can rework.

Code comments are also easier to keep up to date with respect to docs that live elsewhere, as you may update them in place whenever you are making changes to the code itself.

Likewise, it is easy to spot in PRs whenever somebody is changing the code without updating the comments, and report it.
