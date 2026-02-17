---
aliases:
  - "How to do QA in 2024"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-essays|Publish Essays →]]"
Status: Evergreened
Owner:
  - Luca
URL: "https://refactoring.fm/p/how-to-do-qa-in-2024"
"👓 Status": Not started
"Date HH": 2025-09-11
"Created time": "2024-09-06T07:40:00.000Z"
Date: 2024-09-18
"Has Notes":
  - "[[evergreen/qa-vs-product-journey|QA vs product journey]]"
  - "[[evergreen/shift-quality-left|Shift quality left]]"
  - "[[evergreen/end-to-end-testing-is-expensive|End-to-end testing is expensive]]"
  - "[[evergreen/ideal-qa-journey|Ideal QA journey]]"
Tags:
  - Essay
  - Software
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 3f35bbe8-afde-40e8-a3e2-4cbb50e9ad55
---

# How to do QA in 2024

### 📑 Materials

### ✍️ Post

---

Every week I get tons of questions from readers about topics I should cover in the newsletter. Some of the most frequent ones are about QA — in fact, I believe I receive at least one or two per week.

Are these questions about specific niche optimizations or tactics? No, they are about basic things: who should do QA, what good QA looks like, or whether you need QA at all.

You might think these things get asked by fresh managers or young CTO founders — but no, they get often asked by folks who have 10+ years of experience, who are not afraid to admit they are just… confused.

There is little consensus around the role of QA in modern engineering teams, which is the reason why I am writing this piece. Recently, we held a Mastermind session about QA with our community, bringing together experienced engineering leaders to discuss their approaches, challenges, and best practices.

In this updated edition for 2024, you will find a comprehensive write-up that includes the key insights from our community discussion, along with my own thoughts and analysis. We'll also explore how emerging technologies like AI are reshaping the QA landscape, and dive into modern practices like "shifting left."

So, today we will cover a lot of ground:

- 🧠 **QA is a Mindset **— the difference between QA and testing.

- 🏆 **The Value of Testing** — a simple mental model to figure out the ROI of your tests.

- 📈 **Product Stages** — how QA changes at different growth/maturity stages.

- 🏎️ **Speed and Reliability** — why end-to-end tests are challenging.

- 🤖 **Automating tests** — the ideal journey, from zero to hero.

- 💪 **Scaling QA** — how to handle technology and your team’s duties

- 💼 **Using external services** — can you delegate QA?

Let’s dive in!

---

### 🧠 QA is a Mindset

If you can’t find a satisfying definition of QA online (I couldn’t), that’s because QA is a mindset, rather than a specific process.

QA is making sure you meet an expectation of quality for your product, and in particular that you don’t go below that quality. Some people think it’s simply “*we don’t ship bugs*”, but things are more nuanced:

1. If you ship a bug on something no one’s using — it obviously doesn’t matter.

1. If you break your most critical workflow and you have hundreds of paying customers, it matters.

1. If you break your most critical workflow but you only have a few customers, and they don’t pay or don’t pay a lot, it may not matter, too.

This *awareness* about where the value is, is the reason why we talk about *Quality Assurance*, as a broad function, as opposed to simply *Testing*.

Good QA requires sorting out what’s really valuable from what is not, and while you might argue this applies to testing in general, QA does this from a product/business standpoint, rather than a pure engineering one.

This mix of product and tech duties is also why QA is confusing to handle: should PMs do it? Or should engineers? Or should you have dedicated people for it?

We’ll get there, but for now, let’s talk about testing 👇

### ⚖️ QA vs Testing

When we talk about QA, we usually refer to a specific approach to testing—testing the product like a final user. This means actually using features and workflows to identify issues.

In our previous guide about testing, we identified three main categories: **unit**, **integration**, and **end-to-end**. 

[https://refactoring.fm/p/how-to-test-software-in-2023](https://refactoring.fm/p/how-to-test-software-in-2023)

With some degree of simplification, QA is about end-to-end testing. This is also called *black-box* testing, because it can be performed without much knowledge of tech internals — as opposed to white-box testing, like unit and integration testing, that is more coupled to the specific tech.

Honestly I am not a big fan of this definition, because, to me, this looks more like a continuum than black/white 👇

![QA primarily focuses on end-to-end testing, also known as black-box testing, because it can be performed without much knowledge of the technical internals.](../assets/85dc8d43ce984a55.png)

If you imagine tests as a pyramid with unit tests at the bottom and end-to-end tests at the top, the higher you go, the more complex the workflows you're testing, and the more you can ignore the layers below.

In fact, each layer acts as a black-box for lower ones: 

- Unit tests ignore the specific implementation of functions.

- Integration tests ignore how workflows are performed internally.

- End-to-end tests ignore pretty much everything below them.

But how is this useful? Are tests less or more valuable based on this? 👇

### 🏆 The ROI of Testing

The value of testing some part of your codebase is based on two things:

1. 💼 **Business** — how valuable is that part and how critical is it to work flawlessly?

1. 💻 **Engineering** — how likely is the test itself going to be valuable?

We should only write tests when their **future value** is higher than their **writing effort**. However, figuring this out is easier said than done.

To help with this, it is useful to think that any piece of software is the combination of a *contract* and its *implementation*. This stands true at any level of granularity, be it a small function or a large component.

- 📃** Contract** — specifies the *behaviour* in terms of what outputs are produced from what inputs.

- **🔨 Implementation** — the *internals* of how such transformations are made.

All types of tests verify that some *contract* is respected, while treating the *implementation* as a black box.

The various types of tests, such as unit, integration, or end-to-end, differ mostly in the scope and size of such contracts and black boxes.

For example, the way a UI works when you click things around is a *contract* between the software and the user. Similarly, the signature and semantics of a function represent a contract between the function and the other code that invokes it.

Tests avoid regressions by **enforcing** these contracts whenever you make changes to their underlying implementations.

So, based on how and when the contract or the implementation changes, you have three scenarios:

1. **🟡 Contract doesn’t change + implementation doesn’t change** → Test is not useful

1. 🟢 **Contract doesn’t change + implementation changes** → Test can catch a regression

1. 🔴 **Contract changes + implementation changes** → You need to change the test

The only scenario in which a test repays itself is the second one. In the first one, the test is irrelevant, while in the last one, it is a liability because you have to update it to reflect the new contract.

So, you want to invest in tests whenever there is:

1. High chance of implementation change, and

1. Low chance of contract change

How does end-to-end testing fare on this?

It’s complicated, because as your product evolves, so should your approach to QA.

In the early stages—pre-product market fit—you should invest very little in QA, especially automated QA. In fact, when a product changes rapidly, tests easily become a liability rather than an asset.

At this stage, your QA process might be minimal: identify a few key workflows, and test them manually (more on that later).

Later, finding product-market-fit makes your hypotheses more grounded, which means:

- **Business** — the stuff to test is more valuable than before.

- **Engineering** — you have some* stable* parts where you can invest in automated testing.

This journey stands true for *all *kinds of testing, but it is *particularly* true for QA, because E2E  testing is *extremely* expensive 👇

![In my experience, integration tests make for the best ROI, while for Unit and E2E… it depends.](../assets/63d8833a06ed4d20.png)

### 💸 End-to-end testing is expensive

In the table above I wrote that the effort for end-to-end testing is high — but why is that? The answer is counterintuitive.

End-to-end tests are not particularly hard to write. Popular frameworks like [Playwright](https://playwright.dev/) and [Cypress](https://www.cypress.io/) are widespread and easy to use. The testing cost comes from other reasons:

#### 1) **Speed **🏎️

End-to-end tests need browsers / device simulators, which makes them slow. Very slow. If you want to run them fast and on parallel, you need powerful infrastructure and a sophisticated pipeline.

#### 2) **Reliability **🩹

End-to-end tests generate *a lot* of false positives, also known as *flakes.*

This is a problem: to put it in context, false positives are not much of a concern for unit and integration tests — but for end-to-end tests, you may have up to 20-25% false positives per run.

Why is that? The simple answer is that the higher level the test, the more things you have *below* that can fail. With end-to-end tests, this includes anything from network latency, to external API calls, browser quirks, and infrastructure issues.

So, every time a test fails, you have to figure out whether:

1. It is just a flaky test and a re-run fixes it, or 

1. The product is fine but the test needs to be updated, or 

1. It is an actual bug.

Only in the third scenario the test is useful — in the other ones it is a liability.

All of this makes end-to-end tests *high maintenance*, which is what discourages many teams: especially early on, and if your team isn’t experienced, the time spent investigating tests is typically higher than doing manual QA.

Is this a rebuttal of end-to-end tests? Not exactly, but it’s important to understand that automated QA is 1) complex, and 2) fragile, so* *the less you need to do it, the better.

For this reason, your QA journey starts *before* you do QA. It starts by shifting quality left 👇

---

### ⬅️ Shifting quality left

The best teams I know minimize their need for end-to-end testing by guaranteeing high quality through the other stages of development.

Here is what they do:

#### 1) Great integration testing 🔍

You obviously don’t want to catch integration errors with end-to-end testing.

Integration tests are 10x easier to write and maintain than end-to-end, so you should invest in the former to minimize the need for the latter.

#### 2) Zero-defect policy 🐛

Foster a culture where bugs are fixed asap, even if low-priority. This is a no-brainer: having few-to-none known defects at any given time makes your testing more reliable and improves the morale of your team (no deadly maintenance backlog).

It also makes it easier to identify and focus on new bugs when they come up. 

#### 3) Good observability + testing in prod 📊

I am a firm believer that engineers should *own* the code they write even after it gets to prod. They should use good observability tools to verify that everything works as intended, and catch bugs early.

As we discussed [with Charity Majors](https://refactoring.fm/p/observability-and-testing-in-production?utm_source=publication-search) a few months back, modern tooling today allows for an unprecedented level of inspection, and this should be totally owned by the same engineers who write the code.

Mind you, this isn’t replaced in any capacity by end-to-end testing (which verifies different things) — but conversely, good testing in prod makes E2E less critical.

#### 4) Get engineers invested in quality 🏆

The strategies above may look easy or hard to you based on how much *quality* already belongs to your team’s culture. If the answer is “*not much*”, the good news is there are practical things you can do to steer the ship.

Here is what worked for people in the community:

- 💫 **Get buy-in about changing your culture** — get your team on board with improving. One participant of the mastermind described running a workshop with their team, getting them to describe what they were currently known for as a team (”*releasing buggy software”*) and what they wanted to be known for (”*releasing reliable software”*).

- 🧑‍💻 **Expose devs to consequences** — give engineers more exposure to the consequences of bugs. This can be done in many ways: making engineers spend some time on customer support, sharing stories about the impact of bugs on users, or involving engineers in calls with users where issues are discussed. Nobody wants to ship a shitty experience.

- 🔍 **Make testing a first-class citizen of your process** — have conversations to plan how features will be tested. Setup checklists and templates (e.g. in your design docs) to make expectations clear. These don’t have to be rigid but can help team members make conscious decisions about how they are testing and why.

- ❤️ **Show that you care **— finally, if you are a manager, show your team that quality is important to you. Reflect on how you express this, in terms of what you talk about, what you praise, and what you criticise. 

---

### 🛣️ QA & Product Journey

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

---

### 💪 QA in your team

QA, other than being a confusing task, is also a confusing *responsibility. *People have usually two doubts about this:

1. Who should do QA? Is it regular engineers? Or dedicated ones? Or PMs? Or *everyone*?

1. Is QA a shared function, or is it embedded in product teams?

If you followed me on the *shift-left* approach, you can probably guess what I think about this. For the first 3 stages, from no automation to a few automated workflows, there is no need today for dedicated QA engineers — nor, of course, dedicated QA teams.

*Quality* should be owned by the product team: by the [product engineers](https://refactoring.fm/p/how-to-become-a-product-engineer), and overseen by the product manager.

Still, I know many teams who don’t work this way, and have dedicated QA even at relatively small scale. In my experience, this happens when developers have already *maxed out* their cognitive load, for a variety of reasons: bad DX, legacy tech, a long backlog of bugs, lack of instrumentation, and more. They just can’t take on more. Conversely, in healthy and efficient teams, you don’t have to do much to make devs own quality: it happens naturally, because we all care about doing quality work.

If you find yourself in the former situation, dedicated QA engineers may be necessary to keep the bar of quality. Keep them! But invest on making the life of your developers easier.

So, we talked about the initial growth stages, but what happens when you need to *scale* automated QA through tens or hundreds of workflows? This is challenging both from a team and a tech perspective, so let’s look at both:

#### 1) Team 🎽

There is no question that engineers who work on your product should own *white-box* testing (unit and integration), for obvious ownership reasons. 

End-to-end tests, though are another story, because of two factors:

1. 📋 **Context** — they need minimal context into the rest of the tech stack, so there is little benefit in having the same product engineers creating and maintaining them.

1. 🎓 **Skills** — developing, running, and maintaining them is expensive and requires specialized knowledge.

So, to run these tests internally at scale, you may want to hire dedicated QA engineers.

Then, the question is having them *embedded* in individual teams vs in separate, shared QA function. This depends on how your product org works, because QA is essentially about product:

1. If your company runs multiple, **independent product teams**, then QA engineers belong to product teams.

1. If your team is **organized in functions** (e.g. backend, frontend, …) and runs on feature teams, then QA is likely one of these functions, and QA engineers are *summoned* to help with individual features.

In the vast majority of the experiences shared in the mastermind, QA was integrated into product teams, rather than being run as a separate one. This is true both in cases where regular engineers did QA (the same who work on the product), and in the case of dedicated QA ones, who get embedded into the same teams.

#### 2) Technology 🖥️

End-to-end tests tend to be slow and resource-hungry, so creating the right environment for them makes a huge difference in making them fast and less prone to *flakes*.

My preferred choice here is to use dedicated **preview environments**, rather than a single staging one. Preview environments are containerized instances that spin up for each PR, to be used both for automated and manual QA.

Single staging environments, on the contrary, tend to become bottlenecks and slow down the team — especially when they break.

You can find more ideas about staging vs preview envs and other configurations in this previous piece, that sparked a hot debate 👇

[https://refactoring.fm/p/do-you-need-staging](https://refactoring.fm/p/do-you-need-staging)

These configurations are obviously impacted by your infrastructure tech choices. E.g. it is harder to create containerized instances if you use a lot of cloud-specific services. 

So, when making core tech choices, think about your CI/CD pipeline.

---

### 💼 Using external platforms / services

There exist several QA services out there, which you can use to improve/delegate parts of your workflow.

You can make a separation between platforms and services:

- 🖥️ **Platforms **— tools you can use to run better tests yourself. They solve the infrastructure / pipeline part of the issue, which alone is a big deal. You may look into [Cypress](https://www.cypress.io/) or [Lambdatest](https://www.lambdatest.com/) for this.

- 🤝 **Services **— companies that use actual developers to help you write (and run) the tests, like [QA Wolf](https://qawolf.com/) or [Test.io](http://test.io/).

Between the two, platforms are quite straightforward, while services are interesting, and, if you ask me, quite underrated.

Most teams I know are skeptical about delegating core parts of the dev workflow. However, being end-to-end tests completely *black-box*, they make for a unique candidate to be owned by an external team.

External QA engineers can be efficient in *complementing* your internal (white-box) testing efforts, by creating and maintaining end-to-end tests autonomously.

Now, off-shore QA teams for hire have existed for a long time, but modern solutions like the ones above typically combine the work of an external team with a custom, hosted platform to run the tests, solving both the team and technology issues. Give them a try (no affiliation).

---

And that’s it for today!
