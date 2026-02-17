---
aliases:
  - "Monday #136"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-monday-idea|Publish Monday Idea]]"
Status: Published
"👓 Status": Not started
"Created time": "2024-12-24T13:06:00.000Z"
Date: 2024-12-30
"Has Notes":
  - "[[evergreen/qa-vs-product-journey|QA vs product journey]]"
  - "[[evergreen/reactive-vs-proactive-work|Reactive vs Proactive work]]"
  - "[[evergreen/startups-vs-big-tech-for-your-career|Startups vs big tech for your career]]"
Tags:
  - Monday
  - Free
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 166bdf02-815c-80ea-85ff-e4e9cf1d1e5c
---

# Monday #136

### 1) 🏢 Should you work at a Startup or a Big Tech?

There is common advice that says:

- **Go with startups** — if you want to have more responsibility and a generalist experience.

- **Go with big tech** — if you want to specialize into something and earn more.

There is some truth in this but it is hard to generalize — especially because neither startups nor big tech are cohesive categories that always behave the same way.

So, when people ask me for advice about choosing jobs, I tell them to stay open and judge more based on the conversations they have during interviews, with people from their future team, rather than the overall company *reputation*.

Things vary a lot, also within the same company. There are lean teams inside big orgs that own high-growth products from top to bottom, operating like a startup, and then there are convoluted, bureaucratic experiences with long chains of commands to release any small change.

Also, not all startups make for good experiences. Some are messy; excellence is nowhere to be found, and the only thing you will learn is how to burn out.

So, my advice is to spend considerable time *talking* with your prospective employers, and asking a ton of questions:

- *How does the team work? Tell me about more the product dev process*

- *What are some ambitious projects you are working on?*

- *Are you raising money? What are the plans for the company?*

- *Is the company growing? Are you hiring for other roles?*

Think like an investor in the company, because you kind of are. You are investing your time in it and you are betting that it will be good for your growth and career.

More advice on how to navigate your career in our full guide from last month 👇

[https://refactoring.fm/p/how-to-navigate-your-career](https://refactoring.fm/p/how-to-navigate-your-career)

---

### 2) 🔀 Reactive vs Proactive work

Paul Graham’s essay about [Maker’s schedule vs Manager’s schedule](https://paulgraham.com/makersschedule.html) has long been a favorite of mine. TL;DR Paul argues that managers and makers (e.g. engineers, designers, etc.) run on different schedules:

- 🔨 **As a Maker **— you benefit from long, uninterrupted streaks of time where you do your focus work. 

- 🎽 **As a Manager **— your schedule is run by meetings where you make decisions that move the ball forward.

These schedules are not only very different, they are **incompatible**. 

As a Maker, you shouldn't be bothered with too many meetings, because those come at the expense of your productivity — but managers will drag you into them because that’s how they do their work.

![image](../assets/166bdf02815c801e.png)

Now, while this makes for a great mental model, **I also find it a bit simplistic**, especially when applied to technical management. For two reasons:

1. **☯️ Black / White** — in engineering, it is rare to find managers who run on a *pure* manager’s schedule like PG suggests. Everyone is a *blend *of some maker’s and manager’s work, with the magic being on finding the blend that works best for your team.

1. ⛑️ **Support to makers** — counterintuitively, one of the major reasons why managers don’t have a lot of *guaranteed* focus time, is to support makers. Hang on with me on this 👇

I believe a better way to think about your schedule, is in *proactive* vs *reactive* terms:

- ➡️ **Proactive work **— that’s your scheduled, planned work. This is often done in *anticipation* of your team’s needs: *hiring*, *planning*, *1:1s*,* *are all examples of proactive stuff that runs on a schedule.

- ⬅️ **Reactive work **— that’s *unexpected *work that *reacts* to your team’s needs. That’s whenever you need to clarify some specs, jump in on a technical dilemma, handle a resignation, or defuse some conflict.

And here is the thing: managers are naturally subject to way more reactive work than makers, which is what effectively messes up with their calendars.

Reactive work is sneaky. It looks like you can lock those two hours of coding on Wednesday, until you get a DM on Slack and figure out that 3 people are stuck and need your intervention.

This divide between reactive vs proactive work is incredibly important — in fact, improving management’s health can often be framed as some version of turning reactive work into proactive:

- *Improve career framework → make career conversations more predictable*

- *Improve design process → reduce reactive changes to specs*

- *Improve hiring process → make resource allocation more proactive*

I explore this mindset and the divide between technical and management work in this article from earlier this year:

[https://refactoring.fm/p/how-to-stay-technical-as-an-engineering](https://refactoring.fm/p/how-to-stay-technical-as-an-engineering)

---

### 3) QA vs Product Journey ⚖️

Let’s say you want to secure the core product workflows by adding some E2E testing — which you have never done before. What should you do? How much should you invest in it?

This journey should move together with that of your product. Most companies go through four steps:

1. 🌱 **Zero-to-one → No testing **— You are looking for product-market-fit, talking with customers and shipping all the time. Very little QA should be in place at this time. E2E would only drag you down because the product changes too fast.

1. 🪴 **Product-market-fit → Manual testing **— customers start to rely on some workflows, and you have some consolidated features. Start documenting critical ones and doing manual QA on them. The ideal process looks like having a list of workflows you go through for each release. What? Still no automation? YMMV, but you will be surprised by how far you can go by getting the basics right, that is: zero-defects policy, good unit + integration tests, good observability + good testing in prod.

1. 🌳 **Scale →** **Automated testing **— you have many of such workflows now, and manual testing has become a burden. It slows down releases, and people despise it.  The time has come! Automate ~10 workflows, create some playwright tests as part of your CI/CD, on an environment that is as close to prod as possible. Especially at the beginning, these tests will slow down your release, both because of raw execution time, and because of time you spend investigating failures. Aim at releasing every day. Multiple times a day is awesome, but even once a day is ok (<10% of teams do that).

1. 📈 **Testing at scale **— as you grow, when you have 50-100 automated workflows, you get to an entirely different ball game, both from a tech and a team point of view. Who should do QA at this point? How to minimize flakes? This stuff is slow, should I roll my own infra?

To understand how to scale QA, how to organize responsibilities, and shift quality left, you can check out our recent piece about it 👇

[https://refactoring.fm/p/how-to-do-qa-in-2024](https://refactoring.fm/p/how-to-do-qa-in-2024) 

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
