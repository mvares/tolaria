---
aliases:
  - "Monday #161"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-monday-idea|Publish Monday Idea]]"
Status: Published
"👓 Status": Not started
"Created time": "2025-06-19T13:13:00.000Z"
Date: 2025-06-23
"Has Notes":
  - "[[evergreen/accelerate-is-more-than-metrics|Accelerate is more than metrics]]"
  - "[[evergreen/good-vs-bad-meetings-by-kathryn-koehler|Good vs bad meetings – by Kathryn Koehler]]"
  - "[[evergreen/as-a-platform-team-dont-lose-sight-of-customers|As a Platform Team, don’t lose sight of customers]]"
Tags:
  - Monday
  - Free
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 217bdf02-815c-806d-8a82-f03a8bce7a6a
---

# Monday #161

### 1) 🙅‍♂️ No Agenda No Attenda

When [I interviewed Kathryn Koehler](https://refactoring.fm/p/how-to-improve-developer-productivity?utm_source=publication-search), Director of Engineering Productivity at Netflix on the podcast, we spent a lot of time talking about *meetings*

In fact, Kathryn says she spends a lot of time doing two things:

- **Removing unnecessary meetings **— to allow developers carve out focus time.

- **De-demonizing good meetings** — to allow the *good* conversations happen.

The risk that we face, in fact, after all this preaching about async & written comms, is that we don’t let even *good* meetings happen — when there is really no substitute to them.

Kathryn argues that a lot of the 10x work happens in great meetings where people can figure out something hard together and align quickly.

So what do good meetings look like?

- ⚽ **They kick the ball forward **— they are about *doing *things, instead of just *syncing. *Most of the syncing may actually happen… *async.*

- 🏗️ **They are structured **— Kathryn is fond of saying “*no agenda no attenda*”. If it isn’t clear what a meeting is about, just don’t go. To meeting owners: always do your own homework and create an agenda that puts everybody on the same page about what needs to be done.

- 🍻 **They are personal **— they create bonding. Use the first minutes to do some small talk, and always use meetings when personal issues are at stake. Think of 1:1s, or retrospectives.

I published more lessons we learned from our podcast guests in this *collective* article last year 👇

[https://refactoring.fm/p/the-top-10-lessons-from-our-podcast](https://refactoring.fm/p/the-top-10-lessons-from-our-podcast) 

---

### 2) 🧱 Platform teams should never lose sight of their *customers*

Earlier this year Camille Fournier published a full article on Refactoring on [how to create good platform engineering teams](https://refactoring.fm/p/creating-a-platform-engineering-team).

She wrote at length about how platform teams are fundamentally different from the classic *central teams*, and one of the core differences is that central teams often **lose sight of their customers**.

Instead of thinking about the people who use their systems as their customers, they view them as those clueless application engineers who just don’t get it. They don’t read the docs, they don’t know how to use systems in the right way, they don’t want to try the new stuff and give feedback on it.

Treating your customers as an inconvenience to be managed is one of the main contributors to the bad reputation of central teams.

We need to view our **platforms as products** not just because we want them to be thoughtful abstractions that are easy to use but also because we want to make sure that we are building things that the customer actually wants and needs.

Your team will have lots of good ideas for products you could be building, but in order for those products to be successful they need to be evaluated for product market fit: *will the application engineers at your company actually use this thing once you build it?*

You can make something that seems great on paper, with easy onboarding, great documentation, and widespread customer awareness, but still get no adoption because it just doesn’t meet a pressing need for the application teams.

![A simplified model of the Platform Engineering lifecycle](../assets/217bdf02815c8099.png)

This is more than just hiring some product managers, making a product roadmap, setting some adoption metrics, and calling it a day. Your whole platform team needs to **develop customer empathy** and connections with customer teams who can give you feedback on what is important to them and where their pain points lie.

Your best products may even come from application teams who have built something useful for themselves that turns out to be something you could expand for the rest of the company.

You can find the full article by Camille below 👇

[https://refactoring.fm/p/creating-a-platform-engineering-team](https://refactoring.fm/p/creating-a-platform-engineering-team)

---

### 3) 📊 Accelerate is more than DORA

Ask anyone about *Accelerate*, and chances are they will mention the DORA metrics. 

These four KPIs define how teams can measure their software delivery performance, and became instantly famous:

1. 🚀 **Deployment Frequency** — how often you release to production.

1. ⏱️ **Lead Time for Changes** — the amount of time it takes a commit to get to production.

1. 📉 **Change Failure Rate** — the percentage of deployments causing a failure.

1. 🛠️ **Time to Restore Service (MTTR)** — how long it takes to recover from a failure.

One of the reasons why the metrics caught on is because they provided, for the first time, a research-backed way to evaluate software delivery across two dimensions:

- **Throughput** → via Deployment Frequency + Lead Time for Changes.

- **Stability** → via Change Failure Rate + MTTR.

But here’s the thing: if you think *Accelerate* is *only* about metrics, you're missing 90% of the picture. The core of Accelerate is not the metrics: it's the *engine *that enables them.

The book meticulously identifies and validates **24 key capabilities** that are statistically shown to improve software delivery performance. The metrics are the *outcome*, while the capabilities are the *drivers*. And the research proves this connection with extreme rigor. It moves the conversation from "*what good looks like*" to "*what specific actions demonstrably lead to good*.

With some degree of simplification, we can organize these capabilities into three buckets: **cultural**, **process**, and **technical**.

![Some of the 24 capabilities identified by Accelerate, in an ideal journey that goes from culture, to process, to tech.](../assets/217bdf02815c8068.png)

These buckets work as levels of a pyramid, each one supporting the health of the ones above:

1. Good culture is what makes people work well together and feel good about their work environment. It keeps retention high, stress low, and enables the creation of good process 👇

1. Process exists to make work flow well through the system. Good process is about tight feedback loops and minimizing waste.

1. Good culture and good process naturally lead to the technical practices that enable elite software delivery, like continuous deployment and empowered teams.

We reviewed Accelerate in our book club two months ago, and we reviewed *all* the 24 capabilities in our full book review 👇

[https://refactoring.fm/p/accelerate](https://refactoring.fm/p/accelerate)

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
