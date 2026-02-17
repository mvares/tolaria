---
aliases:
  - "How to Test Software in 2023"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-essays|Publish Essays →]]"
Status: Evergreened
URL: "https://refactoring.fm/how-to-test-software-in-2023"
"👓 Status": Not started
"Date HH": 2025-04-10
"Created time": "2024-04-18T14:53:00.000Z"
Date: 2023-03-23
"Has Notes":
  - "[[evergreen/minimum-viable-testing-process|Minimum Viable Testing Process]]"
  - "[[evergreen/testing-pyramid-vs-testing-trophy|Testing Pyramid vs Testing Trophy]]"
  - "[[evergreen/qa-is-about-end-to-end-testing|QA is about end-to-end testing]]"
Tags:
  - Software
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 3b1c6939-d629-4eca-9a03-22e8a277d514
---

# How to Test Software in 2023

### 📑 Materials

---

- [https://kentcdodds.com/blog/the-testing-trophy-and-testing-classifications](https://kentcdodds.com/blog/the-testing-trophy-and-testing-classifications)

- [https://martinfowler.com/testing/](https://martinfowler.com/testing/)

- [https://www.crispy-engineering.com/p/why-test-diamond-model-makes-sense](https://www.crispy-engineering.com/p/why-test-diamond-model-makes-sense)

### 💡 Ideas

---

### ✍️ Post

---

Testing is an ever-controversial topic in software.

You would be hard-pressed to find any engineer who doesn't believe that **testing is crucial** to their workflow. Despite this, many teams struggle and are not happy with it.

Additionally, the general **consensus** around what good testing looks like seems shift all the time. Testing is so ingrained into all parts of the dev workflow that any change to such workflow leads to changes to testing. 

For example, introducing [*feature flags*](https://refactoring.fm/p/feature-flags), switching to [*trunk-based dev*](https://refactoring.fm/i/71307178/trunk-based-dev-in-the-wild), adding or removing a [*Staging environment*](https://refactoring.fm/p/do-you-need-staging), or [*using AI*](https://refactoring.fm/p/ai-future-of-coding) to write code may all bring changes to your testing strategy.

In this article, I will write my take on what good testing looks like, and suggest a **practical workflow** that works today, in 2023.

Here is our agenda for today:

- ⚖️ **Contracts vs Implementations **— an important model model to reflect on testing.

- 🔨 **Regressions **— pondering the true ROI of tests.

- 🗂️ **Types of tests **— a basic classification with the main types you should know.

- ⛰️ **Testing Pyramid **— a *classic* testing model made popular by Martin Fowler.

- 🏆 **Testing Trophy **— a *modern* testing model which I personally prefer.

- 🔄 **My Testing Process **— we put all of this together to design a practical process.

- ✨ **Other types of tests **— we go beyond the basics with chaos engineering, load, security, and data testing.

- 💬 **Community examples **— how Product Hunt and Swarmia do testing.

- 📚 **Resources **— as always, further articles and resources to learn more

Let’s dive in!

### ⚖️ Contracts vs Implementations

Our relationship with tests is similar to that with docs, security, and all those investments where we sacrifice something today for some benefit in the future.

Therefore, we should write tests only when their future value is higher than their writing effort. However, figuring out this value is easier said than done.

To help with this, it is useful to think at any piece of software as the combination of a *contract* and its *implementation*. This stands true at any level of granularity, be it a small function or a large component.

- **Contract** — specifies the behavior in terms of what outputs are produced from what inputs.

- **Implementation **— the *internals* of how such transformations are made.

All types of tests verify that some *contract* is respected, while treating the *implementation* as a black box.

The various types of tests, such as unit, integration, or end-to-end, differ mostly in the scope and size of such contracts and black boxes.

For example, the way a UI works when you click things around is a *contract *between the software and the user. Similarly, the signature and semantics of a function represent a contract between the function and the other code that invokes it.

### 🔨 Regressions

Tests avoid regressions by *enforcing *these* *contracts whenever you make changes to their underlying implementations.

Tests are also useful for other things, too, such as documenting what these contracts are about or helping create better designs (e.g., with TDD). This is sometimes controversial, but even if we agree to all, we are still talking about secondary benefits.

Writing and maintaining tests is expensive. If they didn’t catch regressions, we wouldn’t write them, period.

So, based on how and when the contract or the implementation changes, we have three scenarios:

1. **Contract doesn’t change & implementation doesn’t change** → Test is not useful

1. **Contract doesn’t change & implementation changes** → Test can catch a regression

1. **Contract changes & implementation changes** → Need to change the test

The only scenario in which a test repays itself is the second one. In the first one, the test is irrelevant, while in the last one, it is even a liability because you have to update it to reflect the new contract.

So, you want invest in tests where there is:

1. High chance of implementation change, and 

1. Low chance of contract change

Based on that, just how effective are the various types of tests? Let’s list them first 👇

### 🗂️ Types of tests

You can find various classifications of tests. I like this simple one:

- **Static Testing** — if you use a language with static types, a lot of prevention is done in real-time in your IDE.

- **Unit Testing** — it tests the behaviour of a single function / small component.

- **Integration Testing** — it tests a larger workflow that involves multiple components.

- **End-to-end Testing** — it tests some behaviour from top to bottom from the user perspective. E.g. for a web application, it involves starting the app and clicking around in the browser.

- **Manual Tests** — you go clicking and trying stuff by yourself. Let’s not pretend this doesn’t exist: it does, and it’s healthy, when combined with automated tests. 

Exception made for static testing, which is coupled with your language choice, your investment on the other types of tests is 100% discretionary. 

### ⛰️ Testing pyramid

One of the most popular testing *models* out there is the testing pyramid, made popular by Martin Fowler.

The larger the layer, the more tests and effort on that layer.

The pyramid is based on the assumption that the earlier you catch a bug the better, which is largely right, and also that the more you move up the more tests get slower to write/run and costlier to maintain.

Andrew Twyman, former Staff Engineer at Dropbox: 

> *The earlier a developer finds out about a bug, the easier it is to fix, and the less time it wastes. That means prefer to catch bugs in static analysis (ideally in the IDE), then in the build, then in unit tests, then in integration tests, then in code review, then in QA, then in deployment, then in user reports.*

What I feel is missing though, is that as you move up you also get more stable *contracts*, and higher chance of *changing implementation* under the hood. This makes integration tests *very* valuable, while unit tests… a bit less so.

![image](../assets/79966e2caea244eb.png)

To Martin’s (and others’) credit, things haven’t always been like this. In the past we would write most code from scratch. There were lot of custom functions, a lot of algorithms, so unit tests verified complex stuff whose implementation might also change in the future.

Today, especially at unit level, we mostly write software by *composing* stuff. 

Logic in itself is trivial, and when it changes, most often it does because the contract itself changes as well — which puts unit tests into the liability bucket.

So, I don’t feel the pyramid is still the right mental model for most teams.

### 🏆 Testing trophy

When you look at the table above, you see that the ideal testing strategy might not look like a pyramid after all, but more like a diamond.

Or, [as Kent said](https://kentcdodds.com/blog/write-tests), like a trophy.

![The testing trophy proposed by Kent C. Dodds](../assets/4824cbd843b04792.jpeg)

The ideas behind the trophy are simple:

1. Static testing is a no-brainer.

1. Integration tests consistently deliver the best ROI, so most of your effort should be spent on those.

1. End to end and Unit tests are good when used for the right things.

### 🔄 My Testing Process

So, when we put all these things together, this is my preferred workflow for testing:

#### 1) Use a statically typed language

Most languages today have statically typed versions you can adopt, e.g. Typescript for Javascript, or Sorbet for Ruby.

My opinion is that this is a no-brainer for 99% of teams. 

Static typing not only catches *a ton* of bugs early, it also documents the code thanks to types and annotations, making it easier for others to understand what’s going on.

#### 2) Write unit tests when relevant

Unit tests are still an important part of your testing investment. However, I am not adamant about their coverage — you should write them for whatever is non-trivial or subject to implementation changes in the future.

#### 3) Write plenty of integration tests

Integration tests are about testing execution *paths* that involve multiple functions / components. Figure out the most important ones for each area of your product, and test them in depth. To identify them, you can often think about *business* paths, based on how your product is used.

API endpoints are also good candidates for integration tests.

Sometimes, the difference between unit and integration tests is a bit *murky*,* *but it doesn’t matter that you are able to separate those precisely. Just focus on what feels worthwhile to be tested.

#### 4) Write a few, critical end-to-end tests

End-to-end tests are expensive to develop and maintain. My rule of thumb is to invest on testing those parts that you would check manually otherwise.

The main goal of end-to-end tests is to **remove manual checks**, so you can release faster.

If you are an e-commerce, you may start by testing the main purchase funnel, checkout included. If you are a SaaS, you may test that new customers are able to subscribe, and the core features used by your existing ones. 

Good tools that you can use for end-to-end testing are [**Cypress**](https://www.cypress.io/) and [**RainforestQA**](https://rainforestqa.com/). You may also consider using an agency that runs manual QA, like [**Lodestone**](lodestoneco.com), which is used by Product Hunt.

#### 5) Avoid staging if you can

I wrote a full article about this. TL;DR is you can probably avoid a staging environment by implementing a combination of:

- Gradual rollouts with [feature flags](https://refactoring.fm/p/feature-flags)

- Live previews for PRs

- Video walkthroughs for PRs (fantastic idea by [Rado](https://www.linkedin.com/in/radoslavstankov/?originalSubdomain=bg))

The idea is: the less steps to production, the faster you release, the better feedback loop you have, which also helps stability because you recover faster from mistakes.

Check out the full article for more ideas 👇

[https://refactoring.fm/p/do-you-need-staging](https://refactoring.fm/p/do-you-need-staging)

### ✨ Other kinds of tests

On top of this, there is plenty of other testing that falls into the “*your mileage may vary*” category. You may consider implementing it based on your product, size, and more.

#### 1) Chaos engineering 🔥

Chaos engineering is about testing the resilience of your systems by randomly causing some damage in production. It was made popular by Netflix, through their own [Chaos Monkey](https://netflix.github.io/chaosmonkey/).

> *Chaos Monkey is responsible for randomly terminating instances in production to ensure that engineers implement their services to be resilient to instance failures.*

[Devansh](https://www.linkedin.com/in/devansh-devansh-516004168/), Senior ML Engineer, also reported on this in the community:

> *The testing procedure we have at Clientell has been inspired by Chaos Engineering. We do a lot of testing for the systems running at scale (important given that we deal with lot of data). Most of it tends to focus on simulating user journeys and throwing a variety of errors at them. Here are two guides I have on them: *[*A Guide to Chaos Engineering*](https://codinginterviewsmadesimple.substack.com/p/a-guide-to-chaos-engineering-technique?r=4tnbw&utm_campaign=post&utm_medium=web)*, *[*How to Stress Test Your Systems*](https://open.substack.com/pub/codinginterviewsmadesimple/p/how-to-stress-test-your-systems-technique?r=4tnbw&utm_campaign=post&utm_medium=web)

#### 2) Load testing 🏋️

Load testing is important in many cases. You may have a spiky load profile and want to test for resilience, or you may have SLAs / SLOs to guarantee.

Historically, load testing has been a severe pain for developers because of its inherent complexity and lack of modern tools.

Recently, I have been recommended [**K6**](https://k6.io/) a lot for this. It is open-source, it allows you to write simple tests in Javascript, and run them in CI/CD pipelines. Results can be displayed easily on external visualization tools like Grafana and New Relic.

#### 3) Security testing 🔒

Teams of any size should figure out the level of security investment—and testing—to put in place. I wrote a full article about how to embed security in your dev process. You can check it out below:

[https://refactoring.fm/p/how-to-write-secure-code](https://refactoring.fm/p/how-to-write-secure-code)

#### 4) Data testing 💾

When you work heavily with data, enforcing the **quality **and** correctness** of such data is just as important as doing it for code. This is getting crucial as AI becomes widespread — data turns into a cornerstone of your tech stack.

Under-investing in data testing leads to a lot of manual work and to discovering problems in production, either reported by somebody on the team, or, worse, customers.

In my circles, many teams are using [**Great Expectations**](https://greatexpectations.io/) for this. You write *expectation* statements to enforce constraints, run automatic pipelines on your data, and generate reports.

### 💬 Community examples

Here are two practical workflow examples from elite engineering teams.

#### Product Hunt

[Radoslav Stankov](https://www.linkedin.com/in/radoslavstankov/?originalSubdomain=bg), Head of Engineering at Product Hunt, often [writes about testing](https://blog.rstankov.com/tag/testing/) and implemented this workflow:

> I use the following hierarchy of tests. Similar to the Testing pyramid. They go from easy and cheap to expensive, slow, and more valuable.

#### Swarmia

[Ari Koponen](https://www.linkedin.com/in/apkoponen/?originalSubdomain=fi), Head of Platform at Swarmia, told me about their workflow:

> *All of our test suites run for every PR on CI/CD pipeline (GitHub Actions). We use feature flags to rollout features for limited testing.*

### 📚 Resources

- 📑 [**Write tests. Not Too many. Mostly Integration**](https://kentcdodds.com/blog/write-tests) — this article by Kent C. Dodds, inspired in turn by Guillermo Rauch, is a modern take on the classic *testing pyramid* and introduces the famous *testing trophy*.

- 📑 [**Software Testing Guide**](https://martinfowler.com/testing/) — the most comprehensive collection of articles and guides about testing, written by none other than Martin Fowler.

#### ⚒️ Tools

- [K6](https://k6.io/)

- [Great Expectations](https://greatexpectations.io/)

- [Cypress](https://www.cypress.io/)

- [RainforestQA](https://www.rainforestqa.com/)

- [Lodestone](https://www.lodestoneco.com/)
