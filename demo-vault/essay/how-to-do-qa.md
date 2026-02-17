---
aliases:
  - "How to do QA"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-essays|Publish Essays →]]"
Status: Evergreened
"👓 Status": Not started
"Created time": "2024-04-18T14:53:00.000Z"
Date: 2023-11-30
"Has Notes":
  - "[[evergreen/ideal-qa-journey|Ideal QA journey]]"
  - "[[evergreen/end-to-end-testing-is-expensive|End-to-end testing is expensive]]"
  - "[[evergreen/qa-is-about-end-to-end-testing|QA is about end-to-end testing]]"
  - "[[evergreen/qa-is-a-mindset|QA is a mindset]]"
Tags:
  - Event
  - Software
  - Not for HH
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: ca76ea6e-6054-4769-8a1c-35f625754bb8
---

# How to do QA

### ✍️ Post

---

Every week I get tons of questions from readers about topics I should cover in the newsletter. Some of the most frequent ones are about QA — in fact, I believe I receive at least one or two per week.

Are these questions about specific niche optimizations or tactics? No, they are about basic things: who should do QA, what good QA looks like, or whether you need QA at all.

You might think these things get asked by fresh managers or young CTO founders — but no, they get often asked by folks who have 10+ years of experience, who are not afraid to admit they are just… confused.

There is little consensus around the role of QA in modern engineering teams, which is the reason why I am writing this piece. I am not doing this alone: last week I interviewed Jon Perl, founder and CEO of QA Wolf, and we chatted for one hour about all-things-QA.

In this edition you will find the full video recording of the interview and my full write-up. The latter includes everything we covered in the chat, plus my own take and thoughts about it.

A small disclaimer: Jon runs one of the most popular QA services in the world — which is the whole point about having him as a guest — so his ideas are naturally biased towards how he does things at QA Wolf. I personally like their approach and I have known the QA Wolf guys for a long time, but this piece/interview is not sponsored by QA Wolf — I only wrote my unbiased opinion.

So, today we will cover a lot of ground:

- 🧠 **QA is a Mindset**

- 🔍 **QA vs Testing** — a subtle difference

- 🏆 **The Value of Testing **— a simple mental model to figure out the ROI of your tests 

- 📈 **Product Stages **— how QA changes at different growth/maturity stages.

- 🏎️ **Speed and Reliability **— why end-to-end tests are challenging.

- 🤖 **Automating tests **— the ideal journey, from zero to hero.

- 💪 **Scaling QA **— how to handle technology and your team’s duties

- 💼 **Using external services **— can you delegate QA?

Let’s dive in!

---

### 🧠 QA is a Mindset

If you can’t find a satisfying definition of QA online (I couldn’t), that’s because QA is a mindset, rather than a specific process.

QA is making sure you meet an expectation of quality for your product, and in particular that you don’t go below that quality. Some people think it’s simply “*we don’t have to ship bugs*”, but things are more nuanced than that:

1. If you ship a bug on something no one’s using — obviously it doesn’t matter.

1. If you break your most critical workflow and you have hundreds of paying customers, it matters.

1. If you break your most critical workflow but you only have a few customers, and they don’t pay or don’t pay a lot, it may not matter, too.

This *awareness* about where the value is, is the reason why we talk about *Quality Assurance*, as a broad function, as opposed to simply *Testing*.

Good QA requires sorting out what’s really valuable from what is not, and while you might argue this applies to testing in general, QA does this from a product / business standpoint, rather than a pure engineering one.

This mix of product and tech duties is also why QA is confusing to handle: should PMs do it? Or should engineers? Or should you have dedicated people for it? 

We’ll get there, but for now, let’s talk about testing 👇

---

### 📖 QA vs Testing

When we talk about QA, we usually refer to a specific approach to testing — that is, testing the product like a final user. This means actually *using* features and workflows, and figure out if something is broken.

A few months back I wrote a full piece about testing, where I identified three main categories of tests: unit, integration, and end-to-end. 

[https://refactoring.fm/p/how-to-test-software-in-2023](https://refactoring.fm/p/how-to-test-software-in-2023)

With some degree of simplification, QA is about end-to-end testing. 

End-to-end testing is, again, testing your product from the user perspective. This is also called *black-box* testing, because it can be performed without much knowledge of tech internals — as opposed to white-box testing, like unit and integration testing, that is more coupled to the specific tech.

Honestly I am not a big fan of this definition, because, to me, this looks more like a continuum than black/white.

![image](../assets/5795927df1a34ad6.png)

Indeed, if you imagine tests as a pyramid with unit tests at the bottom and end-to-end tests at the top, the higher you go, the more complex workflows you're testing. As you move upwards, you can ignore more layers below, making the box become **darker.**

However, each layer acts as a black-box for lower ones: 

- Unit tests ignore the specific implementation of functions.

- Integration tests ignore how workflows are performed internally.

- End-to-end tests ignore pretty much everything below them.

But how is this useful? Are tests less or more valuable based on this?

---

### 🏆 What’s the value of testing?

The value of testing some part of your codebase is based on two things:

1. 💼 **Business**: how valuable that part is and how badly you want it to work and stay bug-free.

1. 💻 **Engineering**: how likely is the test itself going to be valuable.

So we should only write tests when their **future value** is higher than their **writing effort**. However, figuring this out is easier said than done.

To help with this, it is useful to think that any piece of software is the combination of a *contract* and its *implementation*. This stands true at any level of granularity, be it a small function or a large component.

- 📃** Contract** — specifies the *behaviour* in terms of what outputs are produced from what inputs.

- **🔨 Implementation** — the *internals* of how such transformations are made.

All types of tests verify that some *contract* is respected, while treating the *implementation* as a black box.

The various types of tests, such as unit, integration, or end-to-end, differ mostly in the scope and size of such contracts and black boxes.

For example, the way a UI works when you click things around is a *contract* between the software and the user. Similarly, the signature and semantics of a function represent a contract between the function and the other code that invokes it.

Tests avoid regressions by **enforcing** these contracts whenever you make changes to their underlying implementations.

So, based on how and when the contract or the implementation changes, we have three scenarios:

1. **Contract doesn’t change + implementation doesn’t change** → Test is not useful

1. **Contract doesn’t change + implementation changes** → Test can catch a regression

1. **Contract changes + implementation changes** → You need to change the test

The only scenario in which a test repays itself is the second one. In the first one, the test is irrelevant, while in the last one, it is even a liability because you have to update it to reflect the new contract.

So, you want to invest in tests whenever there is:

1. High chance of implementation change, and

1. Low chance of contract change

How does end-to-end testing fare on this? It depends on your product stage 👇

---

### 📈 Product stages

During our chat, Jon stresses a lot that, in early product stages — pre-product market fit — you should invest very little in QA, especially automated QA. In fact, whenever a product changes fast, tests are easily a liability rather than an asset, for the reasons listed above.

So, at that stage, your QA process might be minimal: identify a few key workflows and test them manually.

Later, finding product-market-fit means you get two things:

- A core set of customers relying on your product, and maybe paying for it

- A core set of features / workflows that are less likely to change.

These things, combined, impact both the business and engineering angle of testing:

- **Business**: the stuff to test is more valuable than before

- **Engineering**: you have some* stable* parts where you can invest in automated testing.

It is worth noting that this is true for *all *kinds of testing, not only QA. But it is *particularly* true for QA, because end-to-end testing is *extremely* expensive 👇

![image](../assets/764885e2ff8a4410.webp)

---

### 💸 End-to-end testing is expensive

In the table above I wrote that the effort for end-to-end testing is high — but why is that? The answer is counterintuitive.

End-to-end tests are not particularly hard to write. Popular frameworks like [Playwright](https://playwright.dev/) and [Cypress](https://www.cypress.io/) are widespread and easy to use. The testing cost comes from other reasons:

#### 1) 🏎️ **Speed**

End-to-end tests need browsers / device simulators, which makes them slow. Very slow. If you want to run them fast and on parallel, you need powerful infrastructure and a sophisticated pipeline.

#### 2) 🩹 **Reliability **

End-to-end tests generate *a lot* of false positives, also known as *flaky tests.*

This is a problem: to put it in context, false positives are not much of a concern for unit and integration tests — but for end-to-end tests, you may have up to 20-25% false positives per run.

But why is that? The simple answer is that the higher level the test, the more things you have *below* that can fail. With end-to-end tests, this includes anything from network latency, to external API calls, browser quirks, and infrastructure issues.

So, every time a test fails, you have to figure out whether:

1. It is just a flaky test and a re-run fixes it, or 

1. The product is fine but the test needs to be updated, or 

1. It is an actual bug.

Only in the third scenario the test is useful — in the other ones it is a liability.

All of this makes end-to-end tests *high maintenance*, which is what discourages many teams: especially early on, and if your team isn’t experienced, the time spent investigating tests is typically higher than doing manual QA.

So is this a rebuttal of end-to-end tests? What does an ideal QA journey look like, from zero to hero?

---

### 🛣️ Journey of automating tests

Jon has worked with hundreds of companies at QA Wolf, picking them up at any stage, from those with zero pre-existing tests, to those who had already plenty of automation in place.

Here are the four stages most companies go through:

#### 1) ❌ No Testing

You are looking for PMF, talking with customers and shipping all the time. Very little QA should be in place at this time. End-to-end testing would drag you down because the product changes too fast. 

Even manually, don’t bother documenting workflows, just go through the most important parts of your product at any given time to make sure you didn’t break anything.

#### 2) 🧤 Manual Testing

Customers start to rely on some workflows, and you have some consolidated features.

Start documenting critical workflows and doing manual QA on them. The ideal process looks like having a list of workflows you go through for each release.

#### 3) 🤖 Automated testing

You have many of such workflows now, and manual testing has become a burden. It slows down releases, and people (likely PMs) despise it.

Automate 10-20 workflows yourself, create some playwright / cypress tests as part of your CI/CD, on an environment that is as close to prod as possible.

Especially at the beginning, these tests will slow down your release — there is no way around it — both because of raw execution time, and because of time you spend investigating failures.

Aim at releasing every day. Multiple times a day is awesome, but even once a day is ok (<10% of teams do that), especially if you are new to end-to-end testing.

#### 4) 📈 Testing at scale

Up to this stage, you may have QA responsibilities distributed across your team:

1. Product managers document workflows to be tested — and possibly test them when doing things *manually*.

1. Product engineers write and maintain tests.

But how does this scale when your product consolidates and your headcount grows, e.g. spinning multiple product teams? Let’s look at the two main options: keeping this in-house, or using external platforms/services

---

### 💪 Scaling QA internally

Scaling QA is challenging both from a team and a technology perspective, so let’s look at both.

#### 1) 🎽 Team

Engineers who work on your product (let’s call them Product Engineers) should totally own white-box testing (unit and integration tests) for obvious ownership reasons. 

End-to-end tests, though are another story:

- **Context** — they need minimal context into the rest of the tech stack, so there is little benefit in having the same product engineers creating and maintaining them.

- **Maintenance** — maintaining them is expensive and requires specialized knowledge.

So, to run these tests internally at scale, you may want to hire dedicated QA engineers.

Then, the question of having them *embedded* in individual teams vs in separate, shared QA function, depends on how your wider team works, because QA is essentially about product.

1. If your company runs multiple, **independent product teams**, then QA engineers belong to product teams.

1. If your team is **organized in functions** and runs on feature teams, then QA is likely one of these functions, and QA engineers are *summoned* to help with individual features.

I wrote more about structuring engineering teams in this in-depth guide a few weeks ago 👇

[https://refactoring.fm/p/how-to-structure-engineering-teams](https://refactoring.fm/p/how-to-structure-engineering-teams)

#### 2) 🖥️ Technology

End-to-end tests tend to be slow and resource-hungry, so creating the right environment for them makes a huge difference in making them fast and less prone to *flakes*.

When asked for advice, Jon says that his ideal choice is using dedicated **preview environments**, instead of a single staging one. Preview environments look like containerized instances that spin up for each PR, to be used both for automated and manual QA.

Single staging environments, on the contrary, tend to become bottlenecks and slow down the team — especially when they break.

You can find more ideas about staging vs preview envs and other configurations in this previous article, that sparked a hot debate:

[https://refactoring.fm/p/do-you-need-staging](https://refactoring.fm/p/do-you-need-staging)

Some of these configuration are impacted by your infrastructure tech choices. E.g. it is harder to create containerized instances, if you use a lot of cloud-specific services. 

So, when making core tech choices, think about your CI/CD pipeline.

---

### 💼 Using external platforms / services

There exist several QA services out there, which you can use to improve/delegate parts of your workflow.

You can make a separation between platforms and services:

- 🖥️ **Platforms **— tools you can use to run better tests yourself. They solve the infrastructure / pipeline part of the issue, which alone is a big deal. You may look into [Cypress](https://www.cypress.io/) or [Lambdatest](https://www.lambdatest.com/) for this.

- 🤝 **Services **— companies that use actual developers to help you write (and run) the tests, like [Test.io](http://test.io/), or, of course, [QA Wolf](https://qawolf.com/) itself.

Between the two, platforms are quite straightforward, while services are interesting, and, if you ask me, extremely underrated.

Most teams I know are skeptical about delegating core parts of the dev workflow. However, being end-to-end tests completely *black-box*, they make for a unique candidate to be owned by an external team.

External QA engineers can be efficient in *complementing* your internal (white-box) testing efforts, by creating and maintaining end-to-end tests autonomously.

Now, off-shore QA teams for hire have existed for a long time, but modern solutions typically combine the work of an external team with a custom, hosted platform to run the tests, solving both the team and technology issues.

During the community Q&A, Jon got asked about the QA Wolf workflow, which he was happy to explain:

When QA Wolf starts working with a company, it typically needs to catch up on coverage first. So there are three stages:

#### 1) 🗺️ Lay of the land

An assessment + initial work done together with the company 

- **Product **— what testing do you have in place today? Is there a manual test plan? Let’s establish this plan first, and later automate it.

- **Roadmap** — let’s plan what coverage you need and a timeline for building it.

- **Build + Feedback** — QA Wolf creates the coverage as autonomously as possible, and gets feedback from the team.

#### 2) 🔌 Start running automated tests

Automated tests are run initially just once a day, to figure out value and not to disrupt the release pipeline.

As soon as the team gets confident about them, they become a part of CI/CD, and QA Wolf creates infrastructure to run them on parallel (spinning up a separate container for each test).

When a test fails it gets investigated by QA Wolf:

1. False positive — gets ignored

1. Test needs update — gets updated by QA Wolf

1. Actual bug — gets reported by QA Wolf

#### 3) 📈 Run tests at scale

Coverage is continuously improved by a collaboration between the company’s team, which communicates product updates, and the QA Wolf team, which writes and maintains the actual tests.

Tests developed this way stay an asset of the company — they can be downloaded anytime and there is no lock-in.

Communication between the teams happens on dedicated Slack/Teams channels, and through integrations with issue trackers (Linear, Jira, Asana, …).

---
