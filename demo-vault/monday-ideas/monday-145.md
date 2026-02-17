---
aliases:
  - "Monday #145"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-monday-idea|Publish Monday Idea]]"
Status: Published
"👓 Status": Not started
"Created time": "2025-02-26T15:07:00.000Z"
Date: 2025-03-03
"Has Notes":
  - "[[evergreen/end-to-end-testing-is-expensive|End-to-end testing is expensive]]"
  - "[[evergreen/tech-has-uncapped-value|Tech has uncapped value]]"
  - "[[evergreen/treat-your-servers-like-cattle-not-pets|Treat your servers like cattle, not pets.]]"
Tags:
  - Monday
  - Free
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 1a6bdf02-815c-800a-96c8-e2a0366294c1
---

# Monday #145

### 1) 🔍 Why is end-to-end testing expensive?

It is common wisdom that end-to-end testing is hard — but why is that? 

End-to-end tests are not particularly hard to write. Popular frameworks like [Playwright](https://playwright.dev/) and [Cypress](https://www.cypress.io/) are widespread and easy to use. The cost of testing comes from other reasons:

#### **Speed **🏎️

End-to-end tests need browsers / device simulators, which makes them slow. Very slow. To run them fast and in parallel, you need powerful infrastructure and a sophisticated pipeline.

#### **Reliability **🩹

End-to-end tests generate *a lot* of false positives, also known as **flaky tests*****.***

To put it in context, false positives are not much of a concern for unit and integration tests — but for end-to-end ones, you may have up to 20% false positives per run.

But why is that? The simple answer is that the higher the level of the test, the more things you have *below* that can fail. With E2E, this includes anything from network latency, to external API calls, browser quirks, and infrastructure issues.

So, every time a test fails, you have to figure out whether:

1. It is just a flaky test and a re-run fixes it, or

1. The product is fine but the test needs to be updated, or

1. It is an actual bug.

Only in the third scenario the test is useful — in the other ones it is a net negative.

All of this makes end-to-end tests *high maintenance*, which is what discourages many teams: especially early on, and if your team isn’t experienced, the time spent investigating tests is typically higher than doing manual QA.

I wrote a full piece about how to do modern QA properly a few months ago 👇

[https://refactoring.fm/p/how-to-do-qa-in-2024](https://refactoring.fm/p/how-to-do-qa-in-2024)

---

### 2) 🤖 AI will probably bring *more* tech work, instead of *less*

In all tech companies I have known, there has never been shortage of work.

There has never been a time, during quarter planning, or looking at the backlog, where someone said: “*well, we don’t have much to do! This will be a light [quarter | month | week]*”

That’s because **tech and product have uncapped value**: more engineering time just means more opportunities and more business.

Which means, if we equal the use of AI to more productivity, that the most likely outcome of that productivity is: **we will just get more things done**.

You can’t say the same for everything.

Think of a cleaning service: let’s say there are 3 people who come clean your office twice a week. If all of a sudden you were able to *triple* their productivity, would you still employ three of them to do *three times* the cleaning? Probably not, because cleaning has capped value — there is only so much you can do.

Tech is not like this. I am convinced software would be even more pervasive than it is today, probably by an order of magnitude, if it wasn’t for the fact that 1) we don’t have enough engineers, and 2) code is extremely expensive to write and maintain.

![image](../assets/1a6bdf02815c80b9.png)

So, what are companies going to do with *more* productivity? Are they going to lay people off to keep getting the same amount of things done as before, or are they going to *do more* with it? To me, it is safe to say they are going for the latter.

But this won’t be true for *all* companies. There exist many companies that **see tech as a cost center with capped value**. They believe there is only so much you can get from it, and in some cases, they may even be right!

Well, these are the cases where you may see layoffs. These are the *cleaning* cases, where tech is employed as a commodity. These cases exist, but they were probably bad jobs to begin with, so I we shouldn’t focus on them.

My prediction is that good companies will use AI to do more, while bad companies will use AI to cut costs.

I wrote many more predictions in this recent piece from a couple of months ago 👇

[https://refactoring.fm/p/will-ai-replace-engineers](https://refactoring.fm/p/will-ai-replace-engineers)

---

### 3) 🐄 Treat your servers like cattle, not pets.

In a presentation around 2011, [Randy Bias](https://twitter.com/randybias) famously said: *treat your servers like cattle, not pets.*

Here is an excerpt from Randy himself:

> *In the old way of doing things, we treat our servers like pets, for example Bob the mail server. If Bob goes down, it's all hands on deck. The CEO can't get his email and it's the end of the world. In the new way, servers are numbered, like cattle in a herd. For example, www001 to www100. When one server goes down, it's taken out back, shot, and replaced on the line.*

The analogy is clear. Pets are expensive, fragile, and require bespoke work. Cattle is homogeneous, their maintenance is standard and each individual can be replaced (sorry, cows!).

Anyway, it is a beautiful picture that applies to much more than infrastructure. 

The essence of engineering is **turning pets into cattle**.

---

And that’s it for today! If you are finding this newsletter valuable, consider doing any of these:

**1) **🔒** Subscribe to the paid version** — if you aren’t already, consider becoming a paid subscriber. 1500+ engineers and managers have joined already! Learn more about the [benefits of the paid plan here](http://refactoring.fm/about).

Get full access to Refactoring ✨

[https://refactoring.substack.com/subscribe](https://refactoring.substack.com/subscribe)?

**2)** 🍻 **Read with your friends** — Refactoring lives thanks to word of mouth. Share the article with your with someone who would like it, and **get a free membership** through the new [referral program](https://refactoring.fm/p/referral).

Read with your friends 🍻

[https://refactoring.fm/leaderboard](https://refactoring.fm/leaderboard)

I wish you a great week! ☀️

Luca
