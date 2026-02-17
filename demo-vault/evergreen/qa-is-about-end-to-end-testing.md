---
aliases:
  - "QA is about end-to-end testing"
"Is A":
  - Evergreen
Tags:
  - Has Pic
"Created at": "2024-04-18T14:44:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to":
  - "[[essay/how-to-do-qa|How to do QA]]"
  - "[[essay/how-to-test-software-in-2023|How to Test Software in 2023]]"
  - "[[monday-ideas/monday-104|Monday #104]]"
"Old Created At": "2023-12-07T10:45:00.000+01:00"
"Updated at": "2024-09-18T08:44:00.000Z"
Status: Not started
Tweet: "QA isn't just about checking boxes—it's about end-to-end testing from the user's perspective. Think of it as a pyramid: unit tests at the base, leading to complex workflows at the top. Each layer obscures the details below, making higher-level tests crucial for real-world usability. Let's discuss how we can refine our testing strategies to ensure a seamless user experience. #TechLeadership #QualityAssurance"
notion_id: a3e27a59-1a0e-4c99-92c9-b87423570ff6
---

# QA is about end-to-end testing

When we talk about QA, we usually refer to a specific approach to testing — that is, testing the product like a final user. This means actually *using* features and workflows to figure out if something is broken.

A few months back I wrote a full piece about testing, where I identified three main categories of tests: unit, integration, and end-to-end.

With some degree of simplification, QA is about end-to-end testing.

End-to-end testing is, again, testing your product from the user perspective. This is also often called *black-box* testing, because it can be performed without much knowledge of tech internals — as opposed to white-box testing, like unit and integration testing, that is more coupled to the specific tech.

Honestly I am not a big fan of this definition, because, to me, this looks more like a continuum than black/white.

![image](../assets/b91bfb638eba47e5.png)

If you imagine tests as a pyramid with unit tests at the bottom and end-to-end tests at the top, then the higher you go, the more complex the workflows you're testing. And as you move upwards, the more layers you have below, which is what makes the box *darker.*

In fact, each layer acts as a black box for the ones below:

- Unit tests ignore the specific implementation of functions.

- Integration tests ignore how workflows are performed internally.

- End-to-end tests ignore pretty much everything below them.
