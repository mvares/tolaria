---
aliases:
  - "Monday #106"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-monday-idea|Publish Monday Idea]]"
Status: Published
"👓 Status": Not started
"Created time": "2024-05-31T07:15:00.000Z"
Date: 2024-06-03
"Has Notes":
  - "[[evergreen/good-microservices-start-with-good-monoliths|Good microservices start with good monoliths]]"
  - "[[evergreen/dora-space-devex-frameworks|DORA, Space & DevEX frameworks]]"
  - "[[evergreen/unbundle-delegation-with-sops|Unbundle delegation with SOPs]]"
Tags:
  - Monday
  - Free
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 7941f9df-4631-4e67-81c4-a996f16eb919
---

# Monday #106

### 1) 🍝 Distributed spaghetti

Consider the [Gall's Law](https://en.wikipedia.org/wiki/John_Gall_(author)):

> *A complex system that works is invariably found to have evolved from a simple system that worked. A complex system designed from scratch never works and cannot be patched up to make it work. You have to start over with a working simple system.*

Paraphrasing it, good microservices designs are invariably found to have evolved from good monolithic designs.

Likewise, if your monolith looks like spaghetti, moving to microservices will not magically fix it. Rather, it will turn it into **distributed spaghetti**, making problems worse.

![image](../assets/d90e162718d145ac.png)

More ideas on monoliths and microservices 👇

[https://refactoring.fm/p/monoliths-vs-microservices](https://refactoring.fm/p/monoliths-vs-microservices)

---

### 2) 📊 DORA vs SPACE vs DevEx

If you are new to engineering metrics and you try to educate yourself, the first thing you will probably meet is *frameworks, *the most popular of which are: DORA, SPACE, and DevEX.

They are all born out of *research* into how engineering teams work, but they are about very different things.

1. 🚚 **DORA** — is about DevOps metrics. It’s four KPIs you should take into account to measure your delivery process.

1. 💫 **SPACE** — draws a holistic picture of how engineering teams work, along five axes: Satisfaction & Wellbeing, Performance, Activity, Communication & Collaboration, Efficiency & Flow. Each item is evaluated on individual, team, and system levels, and features a number of recommended metrics.

1. 🔧 **DevEx** — organizes developer experience into three key dimensions: *feedback loops*, *cognitive load*, and *flow state*.

These three frameworks are useful for different things. 

DORA is specific for DevOps, not dev productivity in general. This makes it useful in those cases where your bottleneck is around delivery, which may or may not be the case.

SPACE is sophisticated and non-prescriptive: it gives you all the ingredients but you have to put them together yourself in a recipe that works for your team.

DevEx is the most actionable for most teams. Here is more about its three dimensions:

- 🔄 **Feedback loops** — how quickly developers receive feedback on their actions, including the quality of that feedback.

- 🧠 **Cognitive load** — the mental effort and processing capacity required by developers to code effectively. It emphasizes the need to minimize interruptions and streamline processes.

- 🌊 **Flow state** — the optimal mental state where developers experience high motivation, creativity, and productivity.

A lot of this data is designed to be gathered through *conversations*

In fact, a problem with engineering metrics is that we may be tempted to treat our *teams* like software, and fix their problems by only looking at *telemetry* data. No opinions involved.

The difference is: **systems can’t talk to us, but our teams can**, and should.

So, to evaluate developer experience, the first thing you should do is to have good conversations with your teammates:

- 💬 **1:1s** — ask what is the one thing that makes it harder to do their job.

- 📮 **Surveys** — collect opinions and ideas about making things better.

- 🍻 **Retrospectives **— discuss ideas and improvements with the team.

You can find more ideas about engineering metrics in our recent chat with Laura Tacho, CTO at DX 👇

[https://refactoring.fm/p/engineering-productivity-and-developer](https://refactoring.fm/p/engineering-productivity-and-developer)

---

### 3) 🪚 Unbundle delegation with SOPs

If you *feel* like you could delegate something, but you are not sure where to start, it is useful to reflect on the fact that delegation is two things together:

When you unbundle these two steps, things become a lot less scary — and here is the good news: doing (1) is easy, and it is pretty helpful even without (2).

Basically, **you delegate things to yourself**.

Write down instructions for your tasks assuming you totally forgot how to do them. For many of those, this may not be not far from the truth. Think of reports you create on a monthly basis, or recurring hiring routines.

Such instructions are often called SOPs — [Standard Operating Procedures](https://en.wikipedia.org/wiki/Standard_operating_procedure) — and there is a large body of literature on how to create them well.

You can write them down, or, even more easily, record the process with [Loom](https://loom.com/) or [Scribe](https://scribehow.com/).

I have many for Refactoring as well 👇

![Some of my SOPs for Refactoring](../assets/80b56cbb861442e5.png)

Having a SOP written down makes delegation 10x easier. You should not simply *assign *them to someone else, as they are too prescriptive, but you can use them as a starting point to discuss the task at hand, collect suggestions, and eventually let the new assignee come up with their own process.

I wrote a full guide about delegating work, you can find it here 👇

[https://refactoring.fm/p/how-to-delegate](https://refactoring.fm/p/how-to-delegate)

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
