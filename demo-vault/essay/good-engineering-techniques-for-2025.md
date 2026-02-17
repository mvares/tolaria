---
aliases:
  - "Good Engineering Techniques for 2025 📡"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-essays|Publish Essays →]]"
Status: Evergreened
URL: "https://refactoring.fm/p/the-refactoring-tech-radar-for-2025"
"👓 Status": Not started
"Created time": "2025-02-11T10:21:00.000Z"
Date: 2025-03-26
"Has Notes":
  - "[[evergreen/iac-is-a-no-brainer|IaC is a no brainer]]"
  - "[[evergreen/monorepos-are-better-in-2025|Monorepos are better in 2025]]"
  - "[[evergreen/ddd-is-having-a-reinassance|DDD is having a reinassance]]"
  - "[[Continuous Integration / Delivery / Deployment]]"
Tags:
  - Essay
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 197bdf02-815c-80b6-bc37-c09231ca34cd
---

# Good Engineering Techniques for 2025 📡

### 📑 Materials

---

### ✍️ Post

---

## Intro

Hey there! Early every year we publish a list of **techniques and tools** you should consider in your new year resolutions.

It’s a list of recommended items, each with my own commentary about why you should add it to your arsenal. This year we are kinda late, but hopefully in time for your Q2 planning!

![image](../assets/1bfbdf02815c80c6.png)

So how do we pick these items?

Most of them come from good conversations with smart tech leaders I know. These happen in the community, over the podcast, and in my network of friends. I also have a small set of publications I trust, from which I snipe material — most notably the [Thoughtworks Radar](https://www.thoughtworks.com/radar/), which inspires this work.

With respect to previous years, this time we will focus on *techniques *— that is, practices that almost any engineering team can apply. For each of them we will explain why they matter, why they matter *now*, and recommended tools / ways to implement them.

Also, some of these are novel, while others are definitely not, but I believe it’s their time to shine, and I’ll explain why.

So here is the full list:

1. 🚚 **Continuous Deployment** — and, once for all, the difference with continuous integration and continuous delivery.

1. 🐥 **1% Canary** — doing good QA in production.

1. 🗺️ **Domain-Driven Design** — a 20-years-old good practice turned *super powerful* thanks to AI.

1. 🗿 **Monorepos** —

1. 🏗️ **Infrastructure as Code **—

1. 🙋 **Async Standups **—

1. 🔬 **AI Code Analysis **—

1. 🔍 **Non-blocking Code Reviews **—

1. 📊 **Engineering Metrics —**

Let’s dive in!

---

### 1) 🚚 Continuous Deployment

There is a lot of confusion about the differences between continuous integration, continuous delivery, and continuous deployment, so here is a recap:

- 🥉 **Continuous Integration** — means that pushing new code into a shared repository triggers an automated build & testing process. Example: dev opens up a PR; automated tests run in CI pipeline; if tests pass, the code can be merged into the main branch.

- 🥈 **Continuous Delivery **— means that code on the main branch *can *be deployed at any time — i.e. it is always in a deployable state. Example: code passes CI tests; it is automatically deployed to a staging environment; a human manually approves the release to production.

- 🥇 **Continuous Deployment **— means that every change that passes automated tests gets *automatically* deployed to production. 

So, continuous deployment *extends* continuous delivery by removing manual approvals. This enables faster feedback loops and ensures code changes don’t get stale or batched in pre-prod stages like staging.

Small + frequent changes vastly reduce risk and improve developer productivity because there fewer handoff steps.

Also, deploying code doesn’t necessarily mean to *release* it! In fact, you should *decouple* the two things with the next technique 👇

---

### 2) 🐥 1% Canary

I love the name *1% canary* — which I stole from [Thoughtworks](https://www.thoughtworks.com/radar). This is the practice of rolling out new software to a *super small sample* of users, to reduce risk and do more additional QA.

This sample can be arbitrarily small: it can be beta users, a selected group of testers, or even just people on your team.

The point is to move the final QA stage to production, so that you skip an intermediate step, plus you make sure you are testing the real thing, instead of a replica.

You can implement this by using feature flags and *feature management workflow* tools. We covered this in various previous articles:

- 🚢 [**Do you Really Need a Staging Environment?**](https://refactoring.fm/p/do-you-need-staging?utm_source=publication-search)

- 🚩 [**Feature Flags**](https://refactoring.fm/p/feature-flags?utm_source=publication-search)

---

### 3) 🗺️ Domain-Driven Design

Ok this is not exactly new! DDD has been around for more than 20 years, and has only grown in importance year after year.

Most recently, I believe we got to an inflection point that turned DDD from simply *excellent* to *inevitable* for most engineering teams — because of AI.

Why is that? Let’s take a step back and define what DDD is about.

At its code, DDD is about organizing software around the business domain, rather than technical concerns. It does so through various devices, like:

- 🗣️ **Ubiquitous Language** — teams create a shared vocabulary that both developers and business people use to avoid misunderstandings.

- 📐 **Bounded Contexts** — identifying different parts of the systems so that they have clear, well-defined responsibilities and relationships

- 🔀 **Context Mapping** — describe the types of relationships between bounded concepts and teams.

Giving an exhaustive description of DDD is out of the scope of this piece (and we would need an entire book) but you get the idea.

The key part here is that DD focuses on creating *clarity* about the business domain and its moving parts, before we recreate them with software. This is exactly the type of work that I expect engineers to spend more and more time on, in the age of AI, as opposed to pure coding.

We need humans to map the nuances of business and product into structured *concepts* and *relationships*, only* later *to be turned into code by AI. When you do a good job on the former, you will find that the latter becomes trivial, and it feels just right to delegate it to a machine.

Conversely, when we feel that coding is hard, it is often because we try to do the two things together — at the same time. We try to figure out concepts *while* we are coding, and that’s where no amount of AI will be able to save us.

To learn more about DDD you can check out:

- 📘 [**Domain-Driven Design**](https://www.goodreads.com/book/show/179133.Domain_Driven_Design) — the original *blue* book by Eric Evans (2003) that introduced DDD. This is a deep, theoretical exploration. Perfect for strong foundations.

- 📕 [**Implementing Domain-Driven Design**](https://www.goodreads.com/book/show/15756865-implementing-domain-driven-design) — by Vaughn Vernon (2016). this is more of a practical guide to applying DDD in real-world projects. Recommended and easier to digest than Evan’s book.

---

### 4) 🗿 Monorepos

This is another controversial one: I believe that today, in 2025, monorepos are the the best way to organize codebases. More specifically, I believe they *a lot* better (not just a little) than polyrepos, for the vast majority of orgs.

The TL;DR is that 1) there have been historically very real pros and cons about monorepos vs polyrepos, but while today the cons of monorepos have been largely solved with tooling, the cons of polyrepos are all still out and about.

Here is a sample of the latter, paraphrased from a real-world team exploration done by Danilo Spinelli: 

1. **Repository obsolescence and neglect **— multiple repositories often lead to some becoming obsolete or unused, and these are not always marked accordingly.

1. **Refactoring complexity** — in a poly-repo environment, tasks like library updates or major refactoring become highly complex. Each repository must be individually updated, requiring significant coordination and increasing the risk of inconsistencies and integration issues.

1. **Hard-to-propagate updates** — changes made to common packages are less visible in a poly-repo structure. This necessitates the additional steps of publishing the packages and then updating each respository with a separate pull request (PR), making the process cumbersome.

1. **Service misalignment** — due to the above, there is a high risk of software components becoming misaligned, depending on the update status of common packages.

1. **Distributed code reviews** — pull requests can be spread across multiple repos, making the review process more complex, hard to monitor and time-consuming.

1. **Duplication of settings** — essential settings like security measures, identity, and pipeline boilerplates need to be replicated in each repo. Updates to any of these common elements require refactoring across multiple repos, increasing the workload and potential for errors.

1. **Documentation challenges**: — when common docs pertains to multiple components, it becomes unclear where to place it in a poly-repo setup, leading to potential accessibility and update issues.

Here is also a [detailed post-mortem](https://segment.com/blog/goodbye-microservices/) by Segment about how they moved from 100+ repositories back to a monolith+monorepo.

Monorepos have different challenges, that mostly revolve around building and continuous integration. You don’t want to run the whole pipeline when a small change is made:

> *Monorepos have many advantages - but ****they struggle to scale****. Each workspace has its own test suite, its own linting, and its own build process. A single monorepo might have ****thousands of tasks to execute****.*

These problems, however, are largely solved by modern build tools, that *cache* the results of build tasks so that no work is ever done twice.

For Javascript stacks, you can check out [Turborepo](https://turbo.build/).

I also wrote a more in-depth analysis of the monolith vs microservices debate (which is not the same — but is related) in this [past article](https://refactoring.fm/p/monoliths-vs-microservices).

---

### 5) 🏗️ Infrastructure as Code

Infrastructure as Code (IaC) is the practice of provisioning infrastructure through code instead of manual processes (i.e. clicking around in cloud consoles). 

IaC has an overwhelming number of benefits:

- 🪄 **Reproducibility** — infra can be created, destroyed, and recreated consistently across envs.

- ↩️ **Version control** — infra changes get tracked just like application code.

- 🤖 **Automation** — reduces human error and speeds up deployment.

- 📑 **Self-documentation** — the code itself documents what infra exists and how it's configured.

These benefits have existed for a long time, at the expense of some additional config work upfront. The factor that heavily tips the scale today is, again, AI.

AI is really good at understanding and generating infrastructure code. This means you can describe what you want in plain English, and AI can help generate the corresponding infrastructure code.

The most used tools for this are **Terraform** and **Ansible**:

1. [**Terraform**](https://www.terraform.io/) — is the gold standard for cloud-agnostic infrastructure provisioning. It allows you to define what should exist (VMs, networks, databases) in declarative fashion, and it maintains state to track and manage these resources over time.

1. [**Ansible**](https://www.redhat.com/en/ansible-collaborative?intcmp=7015Y000003t7aWQAQ) — configures systems and deploys applications using procedural, stateless automation. It is YAML-based and allows you to install software, manage configurations, and run tasks on infrastructure that already exists. 

So, Terraform and Ansible are complementary: the former builds the environment, and the latter sets it up.

> *Getting deeper into Infrastructure as Code techniques on my IT estate. (To be specific: containerised workloads; Ansible). I know I’m late to that party, but as a software guy and a one-man shop I tend to operate infrastructure on a “set it up once and hopefully never need to touch it again” basis. Well, this month I have been forced into a hardware upgrade, and suddenly it looks like the time I invested last year is paying off!
— *[Ross Younger](https://nz.linkedin.com/in/rossyounger)

---

### 6) 🙋 Async standups

There is a lot of *variance* on engineering ceremonies and it’s hard to give advice that works for everybody. When I speak with startups, I restrain myself to saying things like “do 1-week sprints” or “do monthly retros”, because all of this depends on a lot of stuff.

However, there is one thing that I believe that today, in 2025, you should definitely work to get rid of: daily *synchronous *standups, that happen either in person or in a call.

Don’t get me wrong, standups solve a very real problem: coordination and feedback loop on a daily basis. That is, making sure that people 1) are working on the right things, 2) are making progress, and 3) have everything they need to continue to do so.

The problem is that using a sync standup is an incredibly expensive way to achieve these,  because 80% of the times things should be running just fine, so the meeting becomes a waste of time.

The better way to get the same outcome is to run an *async* version of the same standup, where people write a note every day that says:

1. What they worked on yesterday

1. What they will work on today

1. If they need any help

You can do so on a simple Slack / Teams channel, or use a dedicated tool like [Steady](https://steady.com/) or [Geekbot](https://geekbot.com/).

High-performing teams that work on short cycles (e.g. weekly) may also get rid of standups altogether, but that depends on your team. So consider Tuckman’s four stages: where does your team fall? 👇

![image](../assets/1bfbdf02815c8078.png)

The earlier your team is on the scale, the more it benefits from a **prescriptive approach**: more investment on coordination, tigher feedback loops, shorter plans. Conversely, late-stage teams benefit from more focus time and from making people free to do their thing.

---

### 7) 🔬 AI Code Analysis

One of my [predictions about AI](https://refactoring.fm/p/predictions-about-ai) last year was that static analysis would be completely transformed by AI and become pervasive.

Six months in, this is actually happening: what started as simple linting for stylistic errors, is evolving to intercept code smells, security vulnerabilities, optimization opportunities, and more.

Also, AI code analysis is proving itself helpful in multiple steps of the dev process:

1. **Coding **— developers get real-time feedback inside the IDE about opportunities for improvement. See [Packmind](https://packmind.com/).

1. **CI/CD **— more thorough analysis is run asynchronously when a PR is submitted. See [Codacy](https://www.codacy.com/).

1. **Planning / Retrospective **— aggregated analysis about the health of your codebase can be discussed in recurring ceremonies. See [Codescene](https://codescene.com/).

This is healthy because the more you can catch with automation, the more code reviews get easy. To the point where I believe good testing + good static analysis will remove a lot of the need for *blocking* reviews, and many teams will be able to switch to a merge first + review later workflow for most changes.

A limitation of most static analysis tools today — which makes me bullish about the work of the guys at [Packmind](https://www.packmind.com/packmind-tech-coach?utm_source=refactoring&utm_medium=newsletter) — is that the set of rules and criteria are fixed. The next step, to me, is AI taking *your own* coding standards and enforcing them in static analysis, like a human reviewer would.

That’s exactly what Packmind is up to, so [check it out](https://www.packmind.com/packmind-tech-coach?utm_source=refactoring&utm_medium=newsletter) if you want.

---

### 8) 🔍 Non-blocking Code Reviews

As I have written in the past, code reviews are your last line of defense.

When everything else works, they should rarely spot crucial issues. Conversely, if they often do, you should ask yourself what other parts of the process are failing: should you discuss design more? Do you have enough encoded practices? Is static analysis (see above) powerful enough?

Code reviews are literally the *worst* moment (before shipping) in which to spot problems, because they are the last. By *shifting left* and investing in what comes before, you can shrink what goes into reviews considerably, and address many items arguably in better ways.

One of the goals of code reviews should be to **continuously reduce their own scope**, by making engineers uncover rules that can be enforced by previous parts of the dev process.

When done right, reviews become less about catching basic issues (handled by good design + static analysis) or verifying correctness (covered by tests), and more about sharing knowledge, identifying new patterns, and creating new coding practices.

When this happens, it means that you can make most code reviews **non-blocking**: that is, you do them *after* the code is merged.

I know, outrageous! But think about that: most changes we make are boring and uneventful. When correctness and common issues are reasonably taken care of, there is no reason to make developers *wait* and do this painful back and forth: merge optimistically and update after the fact if anything needs to be improved.

![In a mature engineering team, you should be able to 1) do non-blocking reviews for most tasks, 2) automate the simple ones, and 3) pair on the remaining.](../assets/1bfbdf02815c8050.png)

I proposed my own review framework **Automate / Defer / Pair** a while ago, you can find it [here](https://refactoring.fm/p/thoughts-on-code-reviews).

---

### 9) 🧩 Product Engineering

The biggest cultural shift that we have covered recently is *product engineering*, which is only growing stronger in 2025.

Unlike traditional developers who mainly focus on technical implementation, product engineers own entire features from analysis to post-launch iteration, bridging the gap between PMs and pure developers.

In high-performing teams, PMs provide direction and support but leave engineers in charge of creating tickets and managing actual tasks. Requirements focus on outcomes rather than implementation details.

![image](../assets/1bfbdf02815c800c.png)

Here are the key traits that make product engineers different from traditional developers:

1. 📊 **Data-driven development** — engineers own leading product metrics and make decisions based on them. On top of this, they collaborate with PMs, who stay in charge of higher-level (lagging) strategic metrics tied to business outcomes.

1. 🎯 **Feature ownership** — they manage the entire feature lifecycle, from requirements gathering to post-launch monitoring, using feature flags and A/B testing for controlled rollouts.

1. 👥 **Customer focus** — they participate in customer calls, analyze user feedback, and iterate based on real usage data rather than just specifications.

As AI keeps reducing the cognitive load of pure coding, this trend will only accelerate. What started as a bold approach only applied in forward-thinking startups is rapidly becoming the standard expectation for elite engineers across the industry.

> *One concept that really changed my perspective in 2024 was the Product Engineer role. It reshaped how I view the impact engineers can have within an organization.*

We covered this in full here:

- 🎨 [**How to Become a Product Engineer**](https://refactoring.fm/p/how-to-become-a-product-engineer?utm_source=publication-search)

---

### 10) 📊 Engineering Metrics

This should take no one by surprise — as it is one of the topics we talk about the most on Refactoring. Still, in our [recent survey](https://refactoring.fm/p/the-path-to-engineering-maturity?utm_source=publication-search) on engineering maturity, only ~45% of the teams actively use engineering metrics.

I truly believe it is time for everyone to at least dip their toes in the water, and figure out what kind of—even minimal—approach can be helpful for them.

Our own survey show that teams who track and use engineering metrics report all kinds of positive correlations:

- +17% time spent as planned (55% vs 47%)

- +30% of projects delivered on time (64% vs 49%)

- +9.2% happiness about dev practices (3.55 vs 3.25)

And if you think that your engineers would be skeptic, think again: for teams that *do not* track metrics, 69.7% engineers are in favor of trying.

![image](../assets/1b9bdf02815c8001.png)

In recent years metrics frameworks have grown significantly from pure delivery data (a-la DORA) to 360° tools that help monitor the quality of your developer experience, and it’s a no brainer to explore them in a way or another. 

There is also a lot of literature about how to use metrics for good, while avoiding anti-patterns that scare developers off. We try to do our part from our small corner of the world, with articles like the following:

- 📊 [**How to Use Engineering Metrics**](https://refactoring.fm/p/how-to-get-started-with-engineering)** **— our *big *guide on getting started with metrics

- 🖥️ [**Your Dashboards are Probably Doomed**](https://refactoring.fm/p/your-dashboards-are-probably-doomed?utm_source=publication-search)** **— a popular article written with Dylan Etkin about making data actionable… probably not through dashboards.

- **📈 **[**What's Next in Measuring Dev Productivity?**](https://refactoring.fm/p/whats-next-in-measuring-dev-productivity?utm_source=publication-search)** **— our most recent piece about the latest research on productivity metrics, and where the whole space is going. Based on a great chat with Abi Noda.

---
