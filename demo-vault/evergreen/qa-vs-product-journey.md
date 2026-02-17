---
aliases:
  - "QA vs product journey"
Rating: Good
"Is A":
  - Evergreen
Tags:
  - Long
"Created at": "2024-09-25T09:01:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to":
  - "[[essay/how-to-do-qa-in-2024|How to do QA in 2024]]"
  - "[[monday-ideas/monday-136|Monday #136]]"
"Updated at": "2024-12-24T13:15:00.000Z"
Status: Not started
notion_id: 10cbdf02-815c-80fd-8618-e1cae82db248
---

# QA vs product journey

So, let’s say you have done your homework: team cares about quality; unit and integration tests are in place, code is instrumented, and devs test things in production. You want to level things up by adding some E2E testing. What should you do? How much should you invest in it?

This journey should move together with your product one. The more consolidated your product, the more value you unlock through QA.

Based on this, most companies go through various steps:

#### 1) 🌱 Zero-to-one → No Testing

You are looking for PMF, talking with customers and shipping all the time. Very little QA should be in place at this time. E2E would drag you down because the product changes too fast. 

Even manually, don’t bother documenting workflows, just go through the most important parts of your product at any given time to make sure you didn’t break anything.

#### 2) 🪴 Product-market-fit → Manual Testing

Customers start to rely on some workflows, and you have some consolidated features.

Start documenting critical ones and doing manual QA on them. The ideal process looks like having a list of workflows you go through for each release.

You may be asking yourself: what? still no automated E2E? YMMV, but remember you always have the other pieces of the puzzle in place: zero-defects, good unit + integration tests, good observability + testing in prod. You will be surprised by how far you can go by getting the basics right.

#### 3) 🌳 Scale → Automated testing

You have many of such workflows now, and manual testing has become a burden. It slows down releases, and people (engineers and PMs) despise it. 

The time has come! Automate ~10 workflows yourself, create some playwright / cypress tests as part of your CI/CD, on an environment that is as close to prod as possible.

Especially at the beginning, these tests will slow down your release — there is no way around it — both because of raw execution time, and because of time you spend investigating failures.

Aim at releasing every day. Multiple times a day is awesome, but even once a day is ok (<10% of teams do that), especially if you are new to it.

#### 4) Testing at scale 📈

As you grow, when you start having 50-100 automated workflows, you enter an entirely different ball game, both from a tech and a team point of view. Who should do QA at this point? How to minimize flakes? This stuff is slow, should I roll my own infra?

To understand how to scale QA, let’s go back to how you should organize responsibilities 👇 
