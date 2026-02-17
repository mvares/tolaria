---
aliases:
  - How to Use Engineering Metrics
✏️ Status: Not started
Belongs to: "[[responsibility/publish-essays|Publish Essays →]]"
Status: Evergreened
URL: https://refactoring.fm/p/how-to-get-started-with-engineering
👓 Status: Not started
Date HH: 2024-06-12
Created time: 2024-04-18T14:53:00.000Z
Date: 2023-04-27
Has Notes:
  - "[[evergreen/how-to-get-started-with-engineering-metrics|How to get started with engineering metrics]]"
  - "[[evergreen/velocity-is-not-very-useful|Velocity is not very useful]]"
  - "[[evergreen/optimize-cycle-time-up-to-a-limit|Optimize Cycle time — up to a limit]]"
  - "[[evergreen/investment-metrics-are-extremely-useful|Investment Metrics are extremely useful]]"
  - "[[evergreen/as-a-manager-you-should-have-hard-conversations|As a manager you should have hard conversations]]"
  - "[[metrics-are-helpful-for-3-things|Metrics are helpful for 3 things]]"
Tags:
  - Guide
  - Software
🎙️ Status: Not started
Is A:
  - Newsletter Edition
notion_id: 99fd89bc-3d8c-47df-8ff4-47d767f1d120
---

# How to Use Engineering Metrics

### 📑 Materials

---

[Untitled](https://www.notion.so/1ee03cbc0bb64d61a1ff34efbf4cdb4e) 

<details><summary>Discarded #1</summary></details>

<details><summary>Discarded #2</summary></details>

### 💡 Ideas

---

There is a lot of talk around engineering metrics today.

This isn’t entirely new — simple metrics for productivity have been around for decades: think of *velocity*, or *WIP limits* in Kanban. 

When people talk of engineering metrics* today*, though, they usually refer to a relatively new wave of KPIs, like DORA, PR cycle metrics, or investment frameworks. These are specific to the development workflow and are backed by solid research.

However, even if the first analytics tools of this kind are almost 10 years old now, this whole space still feels like a **work in progress**.

I believe this is a reflection of the **state of software engineering** in general.

In fact, KPIs are meant to measure processes, and the software industry doesn’t have much consensus around these in the first place. It’s genuinely hard to point at *many* things that all software teams do, which in turn makes it hard to build a product to improve them.

That said, I believe we are at a tipping point now, where we start to see more consolidation, and many workflows have been figured out. It feels to me we have moved from the *innovators* to *early adopters *stage, where most modern teams would benefit from incorporating metrics in their work.

![Adoption curve of engineering metrics — I believe we are in the *early adopters* stage.](../assets/05ccd17cd63c4180.png)

It’s still a lot to digest, but for teams and managers who make the leap, benefits are impossible to ignore.

So, this article wants to be your primer about engineering metrics and how you can use them with your team. Especially if you have never touched them, this is meant to give you a *minimum viable* take on how to get started. And you should, because benefits are impossible to ignore.

Here is what we will cover:

- 🎯 **Goal of metrics** — what they are and aren’t useful for. Let’s set expectations right.

- 🚦 **Types of metrics** — introducing the simple *WIP* classification.

- 🏁 **How to get started **— a practical workflow to leverage engineering metrics on your team

- 👑 **Advice from the best **— I reached out to the CEOs and founders of the major tools in this space. They shared with me their advice to leaders who want to start using metrics 👇

![image](../assets/871515cf9375426b.png)

Let’s dive in!

### 🎯 Goal of metrics

Let’s start with a simple disclaimer: *nothing* will *authoritatively *tell you how well your team is working, as a whole. If you are looking for a *holistic *picture of your team’s performance, that still comes from your experience.

That’s especially true when you consider that *engineering* is not a silo that creates some abstract tech by itself, but a group of people who work, together with PMs, designers and others, on a product for some users.

Engineering metrics do not capture the big picture, because they are not meant to.

> *Metrics don’t show how much the team cares about the product and users. The care is visible in small adjustments that were not planned to improve the user experience, unusual scenarios, etc.

The care is also visible when the team takes initiative for the work they are doing over following the requirements and designs. I'm wondering if that's all somehow measurable.
*
— Hovhannes Guylan, Senior Engineering Manager

So, metrics are *clues*. They empower your processes and, to quote my friend [Naqui](https://www.linkedin.com/in/naquiuddin/), give you a sense of where the wind is blowing.

> *There is no one set of metrics that accurately gives performance information. However multiple metrics combined together in multiple ways gives a good sense of where the wind is blowing.

— *Naquiuddin Khaja, Engineering Manager

Personally, I have used engineering metrics for many years, and here is what they have been the most useful for:

#### 1) 📈 **Spot trends**

Sometimes it’s hard to pinpoint a good target for a KPI, but you can spot whether things are improving or not.

For example, the number of commits per day doesn’t look all that actionable in isolation, but what if there has been a steady decline in the last three months? Are we getting slower at PRs, too? Maybe that’s because we are having too many meetings? Or there is too much work in progress? 

#### 2) 💬 **Start conversations**

Once you have spotted a trend, numbers make it easy to start a conversation with your team.

> *Metrics are always a means to an end. For me, the goal is to get visibility into what's happening in the development process/developer experience and insights on the things that I should pay attention to. 

— Ari Koponen, Head of Platform at Swarmia*

Such conversations can range from celebrations, for when things have improved, to figuring out the root cause of a problem, starting from some evidence. Which leads to the last point 👇

#### 3) 📣 **Back initiatives**

Numbers can provide *evidence* that backs initiatives with stakeholders.

E.g. showing that your team routinely spends 40% of their time on maintenance is a great starting point to advocate for some debt-reducing project.

So, what types of metrics you should track?

### 📋 Types of metrics

There exist various classifications for engineering metrics. The [SPACE Framework](https://queue.acm.org/detail.cfm?id=3454124) is probably the best out there, but it is also quite extensive and I haven’t found a company that implements it in full.

So, for my own utility, I have come up with a simpler mental model, conveniently called *WIP*, based on three categories: 

- ❤️ **Wellbeing** — perceptual data about people’s satisfaction. You can take this in surveys, track it in 1:1s, retrospectives, and more.  

- ⚖️ **Investment** — data about where your team allocates their time. This is mostly discretionary and there is no right or wrong.

- 📈 **Productivity** — numbers that point at some objective performance, like the DORA metrics.

The goal of this is to be *useful*, rather than *exhaustive*. In fact, I believe the *minimum viable* metrics you should track include some data points from each of these categories. I do not recommend totally ignoring any of them.  

So, let’s list everything that goes into each bucket 👇

### ❤️ Wellbeing metrics

A great litmus test to figure out if you are doing well as a manager is **hard conversations**. 

Are you having enough hard conversations with your team? There are always some: about careers, about CI/CD that takes forever, or about Dave, the guy that always makes others wait two days for his code reviews. Hey Dave 👋

Hard conversations lead to progress, and having them means that people feel *safe *to address problems with you.

Many of these start with something people are not *satisfied* with. **Satisfaction** comes *before* numbers — you might think something is doing great, but if people are not happy about it, you should act.

So, to begin your *data-driven *improvement journey, you don’t need tools. My advice is that you can just… ask people! Here are a few things you can survey your people about:

- *Are we spending time on the right things?*

- *Do you feel overworked?*

- *How do you feel about our delivery process?*

- *How do you feel about how we do code reviews?*

- *What do you think about how we work with PMs and designers?*

You can discuss these in many ways:

- 🗳️ **Surveys **— you can run team-wide surveys on a regular basis, e.g. once a quarter or twice a year, and check progress.

- **🧑‍🤝‍🧑 1:1s** — people can share how they feel in weekly 1:1s. We used a “[*weather report*](https://refactoring.fm/i/35216383/weather-report)*” *for this*.*

- ↩️ **Retrospectives **— you can leverage retros to have collective discussions and collect opinions on team-wide processes.

I want to stress that there is no substitute to this. Out of all the categories of *metrics*, if you have to act on one only, it should be this.

> *My suggestion is to prioritize getting to know your team, fully trust the people you lead, and ensure they are passionate about and accountable for their work. There will always be time to examine metrics once you've accomplished that.

*— Nicola Ballotta, Director of Cloud at Namecheap

That said, there are also tools that help you with this. There are three main categories you can try:

- **General HR **— products like [Lattice](https://lattice.com/engagement) or [Mesh](https://www.mesh.ai/) help you with company-wide engagement, making you run surveys, track e-NPS, and more. If you are a small company these may feel a bit like an overkill

- **Communication-based **— tools like [StatusHero](https://statushero.com/check-ins) or [Range](https://range.co/) focus on creating rituals (e.g. check-ins) where people can report blockers, note how they feel, and more. They are very useful and I used them a lot in the past.

- **Engineering-focused **— some tools also explicitly focus on *developers’ wellbeing*, like [Typo](/dd940f77b9724dc29979c3c81aec1e1a). This is promising even though I never had the chance to try it myself.

![Developer wellbeing on Typo](../assets/8894873867dd4b0c.png)

---

### ⚖️ Investment metrics

Investment metrics are for figuring out how you spend your time as a team. 

For example, how much time goes into maintenance vs new features? How much on new features vs small improvements? 

In my experience, tracking your engineering investment has incredible ROI. It creates *alignment* with the business, builds trust, and counters natural biases your team may have towards specific types of work. 

In fact, based on their culture, most teams naturally skew towards some modes of work. For example: 

- 🏭 **Feature factories** — always pumping out new stuff. 

- 📊 **Optimizers*** — *focus on short-term and small improvements, rather than big initiatives.

- 🏗️ **Perfectionists** — engineering-heavy teams who overly focus on refactoring.

The best way to counter this is to start *visualizing* where your time goes, and adjust.

About this, I am a fan of the *balance framework*, which divides work into four main areas:

1. 🩺 **KTLO** — mandatory maintenance to *Keeps The Lights On*.

1. 🔨 **New things** — work towards business goals, like new products or features.

1. 🔧 **Improvements** — work to improve existing features, including performance, reliability, and security.

1. ⚙️ **Productivity** — improvements to the developer experience. This may also affect operations and other departments’ productivity.

This helps you have conversations based on grounded evidence, and build a sustainable work balance. E.g. are you spending more than 30% on KTLO? You can bring up the data, discuss if there is some debt that slows the team down, and plan actions to improve.

![Tracking investment balance on Swarmia.](../assets/649bdb5c8b504aa0.png)

Most engineering metrics tools today provide ways to track your investment (will provide a list at the end of the post).

I wrote more about balancing your engineering work in this previous Refactoring article 👇

[https://refactoring.fm/p/engineering-investments](https://refactoring.fm/p/engineering-investments)

### 📈 **Productivity** metrics

*Productivity* metrics are what most people think about when we talk of *engineering metrics*. 

These are the numbers that people strive to improve, for which you set targets, check industry benchmarks, and more.

There is almost no limit to the amount of KPIs you can track this way. Delivery metrics (e.g. DORA), coding metrics (e.g. # of commits, commit size, churn, …), collaboration metrics (e.g. PRs metrics), and more.

Any of these can be useful at specific times and in specific situations, but I believe only a few are useful on a regular basis. I will cover them:

#### 🌟 DORA Metrics

Nicole Forsgren, Jez Humble and Gene Kim surveyed more than 2000 tech companies between 2013 and 2017.

They focused on *software delivery*, to understand which practices accelerate development, and in turn bring the most value to companies.

Their work had to validate two major theses:

1. Software **delivery performance** can be measured in a meaningful way.

1. Good software delivery performance predicts wider **organizational performance** — that is, it actually brings value to companies.

They succeeded in both and wrote their findings in a book, called [Accelerate](https://www.amazon.com/Accelerate-Software-Performing-Technology-Organizations/dp/1942788339/ref=sr_1_1?dchild=1&keywords=accelerate&qid=1612333280&sr=8-1).

![image](../assets/9ec9882ce1a14bb7.png)

*Accelerate* has since become a cornerstone work for software engineering, as it backs decades of theories with real, indisputable data. It defines four major metrics for measuring software delivery performance, which today are widely called [DORA](https://dora.dev/) metrics:

1. ⏱️ **Lead Time for Changes **— the amount of time that goes from the first commit of a feature to its release in production.

1. 🚀 **Release Frequency **— how often the organization deploys code for their primary service.

1. 🔨 **Mean Time To Restore **— how much time is needed to recover from downtime / issues introduced with the latest release.

1. 🔥 **Change Failure Rate **— the percentage of releases that result in downtime / severe issues.

*Accelerate* contains performance benchmarks for each metric, defining the categories of *elite, high, medium, *and* low* performers.

![Dora Metrics on Codacy](../assets/b8cb856050444bf6.png)

Here are the three main takeaways:  

1. **Software delivery performance matters** — high performers in software delivery are twice as likely to exceed organizational goals as low performers. They also have 50% higher market cap growth, over three years, compared to low performers.

1. **There is no trade-off between speed and stability** — high performers do better at all measures. Actually, delivery speed *brings* stability, by means of faster recovery from failures.

1. **The gap between high and low performers is incredible** — often being 100x on a single measure. You have companies that deploy once every few months, and others of similar size, with comparable tech assets, who do it multiple times a day.

*Accelerate* has been followed by more research and surveys by the same team in the following years, which you can find on the [DORA website](https://dora.dev/).

#### 🔄 Cycle Time

Out of the four DORA metrics, if you had to choose only one to optimize, that would be the *Lead Time for Changes* — which today is more often called **Cycle Time**. 

It is a subset of the overall *Lead Time,* which instead covers the whole cycle from ideation to release.

**Why measuring one instead of the other?**

Lead Time includes *analysis* and *design* phases, whose duration can vary a lot based on the breadth of the initiative. However, once the initiative itself has been broken down in multiple deliverables, the delivery process should move in short and predictable *cycles*, which are more useful to measure.

![image](../assets/6c73f7e918f4490d.png)

So, Cycle Time is the most popular engineering metric today — and for good reason. In fact, it possesses all the hallmarks of great KPIs:

- **It's objective**: it doesn't need context to be interpreted, you know exactly what it means.

- **It's easy to understand**: it can be easily discussed and explained to management, as it works like the engineering equivalent of sales cycle and product funnel metrics.

- **It stays relevant as you scale**: it doesn't depend on the size of the team.

- **It's actionable**: it shouldn't fluctuate much. Significant increases usually point to specific problems that can be identified and resolved.

A healthy Cycle Time in real-world scenarios is anything within a couple of days. Further improvements are fine, but I have noticed that striving for < one day brings diminishing returns.

Breaking down work in small batches is important, but there is kind of an *optimal* batch size — under which you are only pedaling faster without delivering more value.

So it’s ok to optimize Cycle Time, but I wouldn’t obsess on getting it down to *hours*.

#### 🔍 PR Cycle Time

Cycle Time is an aggregated metric that combines several steps of your workflow. 

When you zoom in, a critical measure for most teams is **PR Cycle time** — the average time that goes from when a PR is opened to when it is merged.

You might think this is very specific compared to the previous stuff we discussed. I am including it here because, in my experience, code reviews are often the single biggest bottlenecks of software teams.

![Tracking cycle time on LinearB: in the example, 5 days of 6 go into review. This is not uncommon.](../assets/d9fc72eb442349cd.png)

It always boggles my mind how many teams do *heroic* efforts to shave 10 mins off their CI/CD pipeline, and then are totally fine with the code sitting idle for *days *waiting for review.

> *I recommend starting with one leading metric (i.e., PR Cycle Time) and looking at that metric consistently throughout the entire engineering organization. This will lead to valuable discussions and, ultimately, the desired changes around that metric.

— *Eiso Kant, CEO at Athenian

> *We track PR cycle times closely. 

We are interested in keeping the batch size low and making sure our review times stay in order. I almost always have a tab open for our "pull requests" view.

It includes cycle time metrics, but, maybe even more importantly, allows you to easily see when the "Merge" or "Review" sections get long. It is usually a symptom of too much WIP / lack of focus.

*— Ari Koponen, Head of Platform at Swarmia

You can find ideas about having a good *and* fast code review process in this previous article 👇 which is one of the most popular ever on Refactoring!

[https://refactoring.fm/p/code-reviews](https://refactoring.fm/p/code-reviews) 

#### 🤷‍♂️ Velocity

Velocity gets a honorable mention because it is still the most well-known engineering metric so I felt compelled to spend a few words about it.

And these few words are: *velocity is not very useful*.

In my experience, velocity has some limited utility in planning work — you can use it for rough sizing, but not more — and is just misleading for anything else.

In fact:

- **It is not a measure of productivity **— you can’t *optimize* velocity, at least not reliably. Since story points (or t-shirt sizes) are arbitrary, people will eventually just inflate the points. And it’s not because people are evil, it’s a natural, even unconscious, reaction to a bad way of defining productivity.

- **It is not useful across teams **— velocity is only meaningful *locally* to the team, because of the arbitrary nature of estimates.

- **It is too high level **— if you get bad velocity in a sprint, you can’t *drill down *into it to figure out what went wrong, as you can do instead with e.g. cycle time.

### 🏁 How to get started

I want to be absolutely clear on this: using metrics is **a lot of work**. 

That is true for any metrics, not just engineering one. In fact, for each single KPI you decide to track, you have to:

- **Monitor it on a regular basis **— these are the basics, of course. You will look at a dashboard, reflect on the *meaning *of those numbers, and correlate them with the work that is going on.

- **Discuss performance with your team **— engineering metrics are best used in conversations with your team. The team has the most *context* about how work happens and can comment on things that went right or wrong. Failing to do this not only handicaps your understanding, it also creates skepticism within your team. Do not turn metrics in to a “*manager’s thing*”.

- **Create initiatives to improve **— conversations are pointless if you don’t carve out space for improving things. When issues are surfaced, you should design initiatives to address them.

This is a continuous cycle: you look at numbers, discuss them with people, figure out how to improve, measure things again, discuss, over and over again. 

So, if you are just getting started, here is the *minimum viable metrics* program I would recommend:

#### 1) Start with *wellbeing* conversations ❤️

Talk to people: engineers, managers, but also PMs and other non-technical stakeholders who are particularly involved. Figure out what are the most *frustrating* problems, to them, in the development process. 

You can do it individually, but I also recommend to do it in team-wide retrospectives. You can have a retrospective focused on the developer experience, and separate one that focuses on the business angle. Write down the 2-3 top issues that people agree on.

#### 2) Pick *one* metric 🤏

Start with *one* of the issues you found, and figure out how to measure it. You can probably find some* *KPI related to it. Here is a quick cheatsheet:

- **Things moving too slow** → Lead time or Cycle time

- **Struggling with how to allocate your time** → Investment balance

- **Slow/unreliable release process** → DORA metrics

- **Building the wrong things** → Feature adoption metrics

Make it an *official* initiative and create a dedicated retrospective about it, with some generous cadence (e.g. once every two weeks).

At the beginning, focus on *improvement* rather than setting a target. It is more important to build momentum rather than reaching specific goals.

#### 3) Rotate 🔄

On a longer timeframe (e.g. quarterly) decide whether to continue your investment on that KPI or move your focus to another of the top issues. Keep having conversations to keep issues *up to date* and surface new ones.

In the long run, at any given time you will find yourself with some specific part of the dev process that requires more of your attention, and a long tail of KPIs you track with a minimum level of investment, to avoid regressions.

### 👑 Roundtable of advice from founders of metrics tools

---

I am lucky to know personally CEOs and founding members of most of the products in the engineering metrics space. 

So I reached out to them and asked what advice they would give to leaders that wants to start using metrics but don’t know exactly how.

![image](../assets/7f5f0894f52b4b67.png)

Here are their answers 👇

#### Eiso Kant, CEO at Athenian

*Many recommend beginning with DORA metrics, but DORA metrics are not enough to guide an engineering organization - they’re only part of the equation.*

*We can’t talk about metrics without talking about change management. Most leaders struggle to create the right culture around metrics. The right culture requires consistency, so I recommend starting with one leading metric (i.e., PR Cycle Time) and looking at that metric consistently throughout the entire engineering organization. This will lead to valuable discussions and, ultimately, the desired changes around that metric.*

*Yes, DORA metrics can show us the typical characteristics of high-performing teams, but not how they made their journey to get there, or a map to get your organization where it needs to get.*

#### **Ori Kenen, CEO at LinearB**

*An engineering metrics program is essential to solve engineering leaders’ dual mandate of operational excellence and aligning R&D investments to business impact. However, metrics like DORA only go so far. They’re often lagging indicators - and are challenging to use without context. You need to use engineering metrics benchmarks to gauge success. Then to create sustained improvement, you must reduce dev toil with workflow automation.*

We’ve built free resources to help engineering leaders start their metrics program and improve software delivery:

- *Our *[*engineering metrics benchmarks*](https://linearb.io/engineering-benchmarks/)* report*

- *Our upcoming *[*3 part workshop*](https://linearb.io/events/2023-summer-series/)* on how to start benchmarking, improve dev efficiency, and resource allocation*

- *A *[*free LinearB account*](https://linearb.io/get-started/)* to get your engineering metrics*

#### Kovid Batra, Founding Member at Typo

*Effective dev teams rely heavily on engineering metrics, but their usefulness is limited unless they are aligned with desired outcomes. 

EMs must first gain a comprehensive understanding of the system as a whole, including how features are conceptualized and brought to production, before focusing on more targeted metrics for optimization.

Although process-specific metrics such as PR Cycle time, MTTR, and Code Review Time are valuable, they should be employed in a manner that enhances the overall workflow, rather than being used in isolation.*

#### Kendrick Curtis, Lead EM at Codacy

*As you'd expect, we actively use *[***Pulse***](https://www.pulse.codacy.com/)*** ****(self-plug) in team sprint retros because it works on a team level, so there's no finger-pointing at devs who are "underperforming" but the team as a whole can look at outlier tickets and say, "OK, why was the cycle time on this one ticket so long? Can we learn anything from it?" -- the DORA metrics are not perfect or complete but being able to ask "why did this take so long?" or "why did we have so many production incidents this month?" has significant value IMO.*

*Pulse or similar cycle-time explorer tool would have been super-helpful at my previous employer to graph phases of cycle. If your team is taking a long time to process code reviews, for instance, this will be glaringly obvious in the cycle time chart (a*[*nd maybe you can find some help on this here...*](https://www.youtube.com/watch?v=ln468WtFr9w)*). If there's a bottleneck in QA or Product review, these things can be visualized in a way that you can then tackle.*

*But, as others here say, I think there is a huge thing to be said for "just listen to your engineers and make sure they are happy, excited about their work and making progress" because over-examination of metrics can lead to unwanted gaming of the system. Metrics do best IMO when they are streamlining your processes rather than studying individuals' performance.*

#### Ari Koponen, Head of Platform at Swarmia

*Metrics are always a means to an end. For me, the goal is to get visibility into what's happening in the development process/developer experience and insights on the things that I should pay attention to.

When talking about metrics, people often think of "a single number," but my experience is that visualizing the data in an easy-to-understand way provides better insights.

The metrics we most commonly refer to in our team are:*

- ***Investment distribution ****— this gives us a top-level view of where our time is going and if we should spend time e.g., improving our architecture or paying more attention to quality/documentation/admin tools.*

- ***Weekly work log ****— we look at this every Friday when having internal demos. It allows us to quickly get a feel of what kind of a week it was. What was our focus, did we have a lot of bug-fixing, etc.*

- ***High-level work log ****— it visualizes epics/stories/issues for a longer period of time and allows us to see if we've been able to focus on our objectives/roadmap work over the past few weeks/months.*

- ***WIP metrics ****— we track WIP for Epics, stories, bugs, and pull requests.*

- ***Lead time / Cycle time metrics ****— we track our story and PR cycle times closely. We have a cycle time goal of 14 days for stories (to help us scope things reliably) and also track scope creep and flow efficiency (active days / total days in progress) to see if we were able to focus on the work. For pull requests, we are interested in keeping the batch size low and making sure our review times stay in order. I almost always have a tab open for our "pull requests" view.*

#### Alex Circei, CEO at Waydev

*For executives new to engineering metrics, it's essential to align KPIs with the company's strategic goals and objectives. *

*Start by measuring Waydev's recommended metrics, including ****Lead Time for Changes****, ****Deployment Frequency****, and ****Change Failure Rate****, as they provide insights into efficiency, velocity, and stability, allowing to identify bottlenecks and areas for improvement. *

*Use these metrics to drive positive change, motivate your team, review progress, and adapt the approach as needed. *

*Implementing a data-driven culture is vital to fostering collaboration and continuous improvement, enabling informed decision-making, and driving long-term success. *

*By leveraging engineering metrics, executives can better understand their team's performance, optimize resource allocation, and improve overall engineering efficiency.*
