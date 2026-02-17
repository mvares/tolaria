---
aliases:
  - "End-to-end testing is expensive"
"Is A":
  - Evergreen
"Created at": "2024-04-18T14:44:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to":
  - "[[essay/how-to-do-qa|How to do QA]]"
  - "[[essay/how-to-do-qa-in-2024|How to do QA in 2024]]"
  - "[[monday-ideas/monday-145|Monday #145]]"
"Old Created At": "2023-12-07T10:46:00.000+01:00"
"Updated at": "2025-02-26T15:14:00.000Z"
Status: Not started
notion_id: 552008b4-be0f-43af-8e89-afcbebeca495
---

# End-to-end testing is expensive

In the table a little above I wrote that the effort for end-to-end testing is *high* — but why is that? The answer is somewhat counterintuitive.

End-to-end tests are not particularly hard to write. Popular frameworks like [Playwright](https://playwright.dev/) and [Cypress](https://www.cypress.io/) are widespread and easy to use. The cost of testing comes from other reasons:

#### 1) 🏎️ **Speed**

End-to-end tests need browsers / device simulators, which makes them slow. Very slow. To run them fast and in parallel, you need powerful infrastructure and a sophisticated pipeline.

#### 2) 🩹 **Reliability**

End-to-end tests generate *a lot* of false positives, also known as **flaky tests*****.***

To put it in context, false positives are not much of a concern for unit and integration tests — but for end-to-end ones, you may have up to 20% false positives per run.

But why is that? The simple answer is that the higher the level of the test, the more things you have *below* that can fail. With end-to-end tests, this includes anything from network latency, to external API calls, browser quirks, and infrastructure issues.

So, every time a test fails, you have to figure out whether:

1. It is just a flaky test and a re-run fixes it, or

1. The product is fine but the test needs to be updated, or

1. It is an actual bug.

Only in the third scenario the test is useful — in the other ones it is a net negative.

All of this makes end-to-end tests *high maintenance*, which is what discourages many teams: especially early on, and if your team isn’t experienced, the time spent investigating tests is typically higher than doing manual QA.
