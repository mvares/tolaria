---
aliases:
  - "Monday #114"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-monday-idea|Publish Monday Idea]]"
Status: Published
"👓 Status": Not started
"Created time": "2024-07-24T06:51:00.000Z"
Date: 2024-07-29
"Has Notes":
  - "[[evergreen/pairing-on-tasks-is-effective-to-onboard-new-engineers|Pairing on tasks is effective to onboard new engineers]]"
  - "[[evergreen/how-to-technical-lead-without-tech-skills|How to technical lead without tech skills]]"
  - "[[evergreen/the-importance-of-continuous-delivery|The importance of continuous delivery]]"
Tags:
  - Monday
  - Free
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 8c52d335-c726-428f-970b-1c6a4f7edb83
---

# Monday #114

### 1) 👯 Onboard engineers by pairing

Companies often focus on speeding up the hiring process, but forget that onboarding is a key part of bringing new talent on board. 

You may celebrate quick hires, only to find out that new employees aren't fully productive until a year after joining. 

I feel that many teams underestimate the importance of effective onboarding, and they do so because onboarding is generally viewed as a documentation-heavy, hard-to-maintain process.

However, it doesn't have to be this way. 

One powerful yet overlooked method to onboard people efficiently is to do *pairing*.

![What a good onboarding for an engineer may look like, from signing to month one.](../assets/a359402527414ee8.jpg)

Pair programming, and pairing on tasks in general, is an effective way to share knowledge without the need to have thorough docs ready in advance. You may pair new hires with an *onboarding buddy*, or with various people from their future team, based on the task at hand.

In the context of onboarding, pairing is helpful for many reasons:

- 🍻 **It builds rapport** — it is a great way to kickstart relationships between co-workers, especially in a remote team.

- 📑 **It highlights missing docs** — you realize what information is available in written form, and what can only be transferred in person instead.

- 🪴 **It is a growth opportunity** — pairing emphasises communication, giving and receiving constructive feedback, and working together towards a goal. These skills are useful in many situations: from managing people, to mentoring, to negotiating with stakeholders.

I wrote a full article about onboarding engineers, which you can find below 👇

[https://refactoring.fm/p/onboarding-engineers](https://refactoring.fm/p/onboarding-engineers)

---

### 2) 👑 Leading engineers more skilled than you

In a recent [Mastermind session](https://refactoring.fm/p/introducing-the-refactoring-mastermind?utm_source=publication-search) on the community, a CTO of a growing startup asked how he should lead his frontend team, being more of a backend guy himself.

The answer depends, primarily, on what kind of contribution you believe you should provide:

- *How hands-on do you believe you need to be? Why?*

- *Why are you pulled into technical conversations in the first place? *

- *How do you envision your ideal role in the dev process? *

You won’t find these answers in books or articles (including this one!), but rather by figuring out what your team truly needs from you. 

At my startup, after we raised our Series A, we went to hire a few senior engineers to level up some strategic parts of our stack. Among them, we hired a lead frontend engineer who was 5-6 years older than me, and had been in the industry for even longer.

At the beginning, I didn’t know how to handle that relationship. I felt that I had to prove myself, and that being the CTO meant I had to *lead* my tech team on pretty much everything.

So the first months were a bit rocky because — guess what — I had no idea what I was doing.

![image](../assets/33a5da2d1c0a4eb1.jpg)

It took a long time to *embrace *what now looks obvious to me: **you can’t be a *****super set***** of all of your team’s technical skills**.

That doesn’t mean though, that you go hands off and take a back seat. Even if you are not doing the bulk of the coding, as a CTO, you have unique strengths to lean into:

- Provide the right context for your team to make decisions

- Provide guidance about the business and the wider strategy

- Ask the right questions, challenge the tradeoffs, and make people bounce ideas off of you.

Of course, your mileage may vary. 

In small teams you may want to be more hands-on, so you may upgrade your skills to stay so. And, in any part of the stack, you should probably be proficient enough to being able to know what’s good.

But it’s important to understand that strong technical leadership is only *one *of the ways you can contribute as a CTO, and not necessarily the one your team needs the most.

So, to figure out your role, always start with your team’s needs, and go backwards from there.

You can find more lessons from the masterminds in this recent newsletter edition 👇

[https://refactoring.fm/p/lessons-from-the-mastermind-sessions](https://refactoring.fm/p/lessons-from-the-mastermind-sessions)

---

### 3) 🔍 Good observability leads to continuous delivery

In our recent [interview with Charity Majors](https://refactoring.fm/p/observability-and-testing-in-production?utm_source=publication-search) we talked about continuous delivery and how this is *enabled* by good observability. In fact:

1. Good observability == being able to get **closer conversations with code**, plus drawing correlation with business value.

1. Closer conversations with code allow to tell at a glance **when something is not working**.

1. Spotting problems fast grows the confidence to **ship many times a day**.

This virtuous cycle, however, can only happen when you get the code out in real environments in a small enough amount of time that engineers still have all that context in their head, so they go and check production against the instrumentation.

Charity goes even further and says that, as an engineer, your job isn’t over until you have looked at production to see that everything works.

This is the natural evolution of *integrated teams*, which went through various stages:

1. **Testing** — it used to be that QA ran all the tests → until we figured out it’s better if engineers do so.

1. **DevOps** — it used to be that ops people were separate from devs → until we figured out they should not.

1. **Observability** — it used to be that engineers job was over when they pushed their code → until we figured out it’s better if they look at how it works in prod.

#### Death Spiral 💀

Conversely, when you don’t get code out fast, and you don’t get it out automatically, you enter the **software engineering death spiral**, where everything starts taking a longer time. 

Code reviews take longer. Disks get larger. So people back up more. So they end up switching projects more. So they are waiting on each other more. Then you need a release engineering team and SRE team. Then you start batching releases, which further increases risk.

You can find the full interview below 👇

[https://refactoring.fm/p/observability-and-testing-in-production?utm_source=publication-search](https://refactoring.fm/p/observability-and-testing-in-production?utm_source=publication-search)

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
