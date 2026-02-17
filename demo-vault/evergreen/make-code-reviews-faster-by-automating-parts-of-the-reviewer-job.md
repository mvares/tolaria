---
aliases:
  - "Make code reviews faster by automating parts of the reviewer job"
"Is A":
  - Evergreen
"Last Tweeted": 2022-06-16
"Created at": "2024-04-18T14:44:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to": "[[essay/code-reviews|Code Reviews]]"
"Old Created At": "2021-12-31T16:04:00.000+01:00"
"Updated at": "2024-04-19T09:37:00.000Z"
Status: Not started
notion_id: e267c918-b5d0-4dd5-b0d7-f58f7f98e870
---

# Make code reviews faster by automating parts of the reviewer job

Easiest way to make faster code reviews is to automate part of the review job. Second best way is [Untitled](https://www.notion.so/00d1f9304bbb47e9bb957df8af670c66) 

Make the reviewer do less work by automating part of their job. A few ways:

- **Include Tests **— comprehensive tests make the code more easy to understand, replicable, and vastly reduce reviewer’s work.

- **Apply Linting **— perform static analysis automatically in your CI pipeline, so reviewers can spare themselves stylistic errors, suspicious constructs, etc.

- **Have a list common mistakes **— create a space in your docs to write down common comments made during reviews, so the reviewer can point to them instead of giving detailed explanations every time. Here is one such document created by the Golang team: [Code Review Comments](https://github.com/golang/go/wiki/CodeReviewComments).
