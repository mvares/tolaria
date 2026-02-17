---
aliases:
  - "Ideal QA journey"
"Is A":
  - Evergreen
Tags:
  - Not for Monday
"Created at": "2024-04-18T14:44:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to":
  - "[[essay/how-to-do-qa|How to do QA]]"
  - "[[essay/how-to-do-qa-in-2024|How to do QA in 2024]]"
"Old Created At": "2023-12-07T10:47:00.000+01:00"
"Updated at": "2024-12-24T13:07:00.000Z"
Status: Not started
notion_id: 05e210b6-1228-47c8-bdfd-fba06e561802
---

# Ideal QA journey

Jon has worked with hundreds of companies at QA Wolf, picking them up at any stage, from those with zero pre-existing tests, to those who had already plenty of automation in place.

Here are the four stages most companies go through:

#### 1) No Testing ❌

You are looking for PMF, talking with customers and shipping all the time. Very little QA should be in place at this time. End-to-end testing would drag you down because the product changes too fast.

Even manually, don’t bother documenting workflows, just go through the most important parts of your product at any given time to make sure you didn’t break anything.

#### 2) Manual Testing 🧤

Customers start to rely on some core workflows, and you have a few consolidated features.

Start documenting critical workflows and doing manual QA on them. The ideal process looks like having a list of workflows you go through for each release.

#### 3) Automated testing 🤖

You have many of such workflows now, and manual testing has become a burden. It slows down releases, and people (likely PMs) despise it.

Automate 10-20 workflows yourself, by creating some Playwright / Cypress tests as part of your CI/CD, on an environment that is as close to prod as possible.

Especially at the beginning, these tests will slow down your release — there is no way around it — both because of raw execution time, and because of the time you spend investigating failures.

Aim at releasing every day. Multiple times a day is awesome, but even once a day is ok (<10% of teams do that), especially if you are new to end-to-end testing.

#### 4) Testing at scale 📈

Up to this stage, you may have QA responsibilities distributed across your team:

1. Product managers document workflows to be tested — and possibly test them when doing things manually.

1. Product engineers write and maintain tests.

But how does this scale when your product consolidates and your headcount grows, e.g. spinning multiple product teams? Let’s look at the two main options: keeping this in-house, or using external platforms/services 👇
