---
aliases:
  - "What’s Next in Measuring Dev Productivity — DX"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-essays|Publish Essays →]]"
Status: Evergreened
Owner:
  - Luca
URL: "https://refactoring.fm/p/whats-next-in-measuring-dev-productivity"
"👓 Status": Not started
"Created time": "2024-07-19T06:26:00.000Z"
Date: 2025-02-05
"Has Notes":
  - "[[evergreen/what-is-dx-core-4|What is DX Core 4]]"
  - "[[evergreen/in-engineering-metrics-move-from-lagging-to-leading-indicators|In engineering metrics, move from lagging to leading indicators]]"
Tags:
  - Guest
  - Mgmt
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 669d4e3d-07f1-4d8e-98f2-720d3c0ea4f8
---

# What’s Next in Measuring Dev Productivity — DX

### 📑 Materials

---

### ✍️ Post

---

Last week I had a long chat with Abi Noda.

Abi is the CEO of [DX](https://getdx.com/), which does some of the world’s most interesting research about developer experience and productivity. He also writes a fantastic [Substack](https://newsletter.getdx.com/), which you should check out if you are interested in these topics.

The idea behind the chat was to learn more about [**DX Core 4**](https://getdx.com/research/measuring-developer-productivity-with-the-dx-core-4/) — DX’s latest framework for measuring developer productivity, which already received high praise from some of my favorite authors, like [Will](https://lethain.com/measuring-developer-experience-benchmarks-theory-of-improvement/) and [Gergely](https://newsletter.pragmaticengineer.com/p/measuring-developer-productivity-bae).

But we got side-tracked! I love this topic, so we ended up talking big picture and discussing all the progress that happened over the last few years, and how the goal post is constantly moving as we learn new things.

The first time I wrote anything about engineering metrics was *checks notes* in [September 2020](https://refactoring.fm/p/creating-a-measurable-process-for?utm_source=publication-search), in the third article ever on Refactoring. I did so to cover a big win for my team at that time: improving our code review process. In just a few months we had been able to decrease the % of PRs approved without review from 20% to almost zero, and increase the % of those reviewed within 24 hours from ~50% to 96%.

We had done so with the help of a couple of tools, including *Pull Panda*, a handy app that collected analytics about your PRs, which at that time had just been acquired by Github.

The founder of Pull Panda was… Abi.

Fast forward a couple of years, Abi founded DX and I went full time on Refactoring. 

So, this chat is not only delightfully fitting our respective journeys — it also comes at the right time, as I believe we are going through **four major shifts** in this space.

![image](../assets/185bdf02815c8066.png)

So here is the agenda for today:

- 📖 **What is DX Core 4** — and how it builds on top of a decade of research

- 📊 **From *****telemetry***** to *****holistic***** metrics**

- ⬅️ **From *****lagging***** to *****leading***** indicators**

- 🤏 **From *****surveys***** to *****experience sampling***

- 🔧 **From “*****what to measure*****” to “*****how to use metrics*****”**

Let’s dive in!

---

*Disclaimer: I am a fan of DX and what Abi is building, and they are also long-time partners of Refactoring. However, you will only get my unbiased opinion about all the practices and tools mentioned here, DX included.*

*You can learn more about DX below* 👇

---

### 📖 What is DX Core 4

The two most popular engineering metrics frameworks out there are DORA and SPACE, which shaped how we think about developer productivity over the last decade.

However, they both face recurring criticism:

- 🎯 **DORA is precise but narrow** — it gives you exact metrics to track, but only covers a small part of what makes engineering teams effective. I.e. your delivery.

- 🌊 **SPACE is comprehensive but vague** — it gives you a complete picture of what matters, but teams often don't know what to do with it. What should you measure exactly? How do you implement it in practice?

DX Core 4—which comes from some of the same authors of DORA and SPACE—tries to hit a sweet spot by being, at once, 1) more comprehensive than DORA, and 2) more prescriptive than SPACE.

It breaks down developer productivity into **four dimensions**, and for each of them it recommends a key metric you should track, and a few secondary ones to really deep dive.

![image](../assets/185bdf02815c80f6.png)

These dimensions pack both *quantitative* data a-la DORA (e.g. speed and quality), and newer *qualitative* measures, custom-designed by the DX team (e.g. effectiveness)

And that’s where things get interesting to me 👇

---

### 📊 From *telemetry* to *holistic* metrics

When we first started measuring engineering productivity we naturally gravitated towards what was easy to measure: **telemetry data from our systems**.

This wasn’t only the *easiest* way to get started — as engineers, it felt like the *right way*, because it mimics how we instrument software: objective data, automatic collection, no human input! 

However, telemetry data can only capture so much of the dev process — mostly *delivery: *PRs, commits, builds, and tickets — but of course there is much more to productivity. Things like cognitive load, documentation, quality of tooling, and collaboration, are hard to grasp from systems.

Enter surveys!

Surveys have become a widespread way to poll developers around devex, and we discussed it several times last year, for example in interviews with [Charity](https://refactoring.fm/p/observability-and-testing-in-production), [Laura](https://refactoring.fm/p/engineering-productivity-and-developer), and [Rebecca](https://refactoring.fm/p/elements-of-an-effective-software).

The problem has always been that surveys are *qualitative* and imperfect, and there was no standard way to run them.

DX Core 4, under the *effectiveness *dimension, tries to standardize this by defining DXI — the **Developer Experience Index**, which you can calculate by using a 14-question survey, battle-tested on several companies big and small.

DXI to me is probably the most interesting part of the framework as it does two things:

- **Standardization** — convincingly provides a standard template for devex surveys

- **Benchmarking** — turns a *qualitative* measure into a *quantitative *one by creating an *index*, paired with benchmarks that correlate scores to business value,

> *"A one point increase in developer experience index score translates to about 15 minutes per developer per week of time saved." — *Abi Noda

To me, this looks like the devex version of the [Gallup engagement survey](https://refactoring.fm/p/the-pyramid-of-engagement-?utm_source=publication-search), which has been run successfully for decades, with great success.

But why does it *matter* to measure developer experience?

Most answers you can find are about getting a more *holistic *picture of your team, which is true, but doesn’t say much. I want to go a step further and say that such data matters because, in most cases, it is the *most actionable data*.

Let me explain 👇

---

### ⬅️ From *lagging* to *leading* indicators

While talking with Abi, at some point we discussed the (in)famous “*# of commits / day*” metric. We both agreed that this is *useful *to measure, but ineffective (and even toxic) when set as a target.

But what does that mean? How can some data give useful directional information, but suddenly become *bad *if we try to optimize for it?

The answer is in the difference between **leading and lagging indicators**. 

- ➡️ **Lagging indicators** — are *outcome* metrics that show results of past actions. 

- ⬅️ **Leading indicators** — are *input* metrics that predict future outcomes.

This difference is mostly [discussed in product management](https://refactoring.fm/p/how-to-become-a-product-engineer), but is exceptionally relevant in engineering, too.

![image](../assets/185bdf02815c80b4.png)

Lagging indicators usually change slowly, are easier to measure, but harder to influence directly. They are *perfect* to give you long-term validation, but you can’t use them to change direction* *directly.

A product example is *revenues* vs *feature adoption*. Revenue is what ultimately validates success, but you can’t just set a higher revenue target and wait for it to happen. Revenue is lagging — to improve it you need something more actionable that you can influence directly, like the speed of feature adoption, which is a leading metric.

So, back to our engineering case, the *number of commits per day* is a lagging indicator, and so are (mostly) the DORA metrics, and the majority of quantitative engineering metrics. You can’t optimize for them directly, because they are *downstream *of everything that happens in the dev process.

When you treat them as *upstream* (leading) metrics, you fail because you are reversing the correlation/causation direction.

So, what is *leading* in developer productivity? As of today, the most convincing answer is **developer experience**. Good satisfaction across the various *usual suspects* ([enough focus time, no waiting, ease of release,](https://refactoring.fm/i/154749198/what-does-a-successful-team-look-like) …) *predicts* good speed and quality.

Now, the classic problem of surveys is that they are *delayed* and *infrequent*, which makes them unreliable because of memory decay, recency bias, and all kinds of problems. Which is why I was especially pleased to learn that DX has found a way to avoid these problems by collecting data in real-time 👇 

---

### 🤏 From *surveys* to *experience sampling*

Abi introduced me to **experience sampling **— a new approach to collect feedback in real-time, right when developers are doing their work. It uses custom tools integrated into the dev environment to capture insights at the key moments.

So, if a traditional survey is like a periodic medical check-up, experience sampling is like the fitness tracker checking your vitals throughout the day.

Experience sampling tools can prompt feedback during specific events, like after merging a pull request, after deploying to prod, or while using various dev tools.

Questions are brief and contextual, like: “*How smooth was this PR review process?”, or “How confident do you feel about this deployment?”*

This approach brings two strong benefits:

- 📊 **Accurate data **— every response has clear context attached to it and there are is no memory bias. 

- 🔍 **Granular analysis **— feedback provided is not *aggregated*, but related to individual units of work. This makes it possible later to break it down by dimensions like type of work, team, or project.

Quoting Abi:

> *"If developers report friction in the PR process, you can actually go and look at those specific PRs. You get that linkage between objective events and subjective experience — it's almost the marriage of qualitative and quantitative data."*

### 🔧 From *what to measure* to *how to use metrics*

In mid 2023 I wrote a long guide on [how to get started with engineering metrics](https://refactoring.fm/p/how-to-get-started-with-engineering). There I argued that metrics adoption was graduating from *innovators*, to *early adopters*.

![My picture from mid 2023](../assets/185bdf02815c8049.png)

A couple of months ago, in our recent [community survey](https://refactoring.fm/p/the-path-to-engineering-maturity), **44.7% of teams reported using engineering metrics **— which further moves them to the *early majority* camp.

This growth was enabled by the work of a handful of thoughtful people, like Abi, who are pushing tools and practices forward.

So where does this leave us?

In the early days, most questions I received about this space where variations of: “*what should I measure?*” These days, I more get asked often “*how should I use this?” — *that is people have a decent idea of what to track, but are still unsure of how to turn data into value.

The next frontier, to me, looks like **operationalizing metrics **— creating playbooks that explain how to embed data into processes, how to use it in conversation, and what’s the role of the various stakeholders in owning and improving metrics.

---

### 📌 Bottom line

And that’s it for today! Here are the main takeaways from this piece:

1. 📈 **Engineering metrics are evolving** — from simple telemetry to holistic measures that capture the full developer experience.

1. 🎯 **DX Core 4 hits a sweet spot** — more comprehensive than DORA, more prescriptive than SPACE.

1. 🔄 **Focus on leading indicators** — developer experience predicts and influences outcomes like speed and quality

1. ⚡ **Experience sampling is the future** — real-time feedback collection provides more accurate and actionable data than traditional survey

1. 🛠️ **The next frontier is operationalization** — turning good metrics into effective processes and improvement loops
