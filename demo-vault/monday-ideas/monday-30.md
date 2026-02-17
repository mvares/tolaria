---
aliases:
  - "Monday #30"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-monday-idea|Publish Monday Idea]]"
Status: Published
"👓 Status": Not started
"Created time": "2024-04-18T15:09:00.000Z"
Date: 2022-12-26
"Has Notes":
  - "[[evergreen/signs-your-growth-has-stalled|Signs your growth has stalled]]"
  - "[[evergreen/its-hard-to-keep-staging-at-parity-with-prod|It’s hard to keep Staging at parity with Prod]]"
  - "[[evergreen/the-vicious-vs-virtuous-cycle-of-docs|The vicious vs virtuous cycle of docs]]"
Tags:
  - Monday
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 7712a3f4-e040-40b0-96f0-aa8d5c3e8949
---

# Monday #30

*Hey, Luca here 👋 welcome to the ****Monday 3-2-1 ****✨*

*Every Monday I will send you an email like this with ****3 short ideas**** about engineering management, technical strategy, and good hiring.*

*You will also receive the regular long-form one on Thursday, like the last one:*

- [**How to Design a Good On-call Process 🚨**](https://refactoring.fm/p/on-call)

*To receive all the full articles and support Refactoring, consider subscribing if you haven’t already!*

Become a better tech leader today ✨

*p.s. you can learn more about the *[*benefits of the paid plan here*](http://refactoring.fm/about)*.*

---

![image](../assets/d969a97f886c4d98.png)

---

### 1) 🦥 Signs your growth has stalled

The tech space moves at crazy speed, and people know it. 

Growing your skills and staying up to date isn’t only the right move for your career — it is a big source of motivation, too.

**Mastery**, defined as the desire to improve our craft, is one of the pillars of engagement at work:

[Embed](https://twitter.com/lucaronin/status/1579743622424977408)

Conversely, when your learning stalls, chances are you will also get progressively less and less engaged, in a vicious cycle that handicaps your growth.

How do you know that your learning is stalling? Here are a few signs:

#### This year looks suspiciously similar to last year 📅

Instead of thinking about your skills, which might be a bit of an abstract exercise, just think about what you have done last year, compared to this one. How did you spend your time?

Sometimes, five years of experience is [just the same year](https://cate.blog/2021/11/29/5-signs-its-time-to-quit-your-job/#:~:text=Sometimes%20five%20years%20of%20experience%20is%20just%E2%80%A6%20the%20same%20year%20of%20experience%2C%20five%20times%20over)… five times over.

#### You can predict your emotional state 🩺

This is a great tip by [Aadil](https://twitter.com/aadilmaan):

> *Has my learning stalled? How do you know this: you know precisely what time of the calendar year you will experience what kind of emotion. At Apple, by my 5th year, I knew when in the release cycle I was going to have extreme anxiety, slow work, sudden ramp up etc.*

#### You are learning coping mechanisms rather than skills 🩹

This is taken again from this [fantastic article](https://cate.blog/2021/11/29/5-signs-its-time-to-quit-your-job/) by Cate.

All companies have quirks, sacred cows, and politics you may need to work around. Which is fine to some extent.

Just ask yourself how much effort you are spending on those*. *How much of what you do (tech, processes, practices) makes you proud? How much of that would be good and reusable in another job? 

More ideas about signs you should quit your job 👇

[https://refactoring.fm/p/quitting](https://refactoring.fm/p/quitting)

### 2) 🔨 Most real-world staging environments are bad

For staging to be useful, it has to catch a special kind of issues that 1) would happen in production, but 2) wouldn’t happen on a developer laptop.

What are these? Think of problems with data migrations, database load and queries, and other infra-related problems.

To make staging catch these issues, you need to keep it at parity with production on data and infrastructure. This is hard and expensive — think about it, if it wasn’t so, you would just spin dev environments that look like prod.

The whole point of having a single, shared environment for testing instead of many individual ones is that the latter would be too expensive to maintain 👇

> *The way I see it, fundamentally, this is a resources management problem. If I wouldn't be looking at costs the dev environments could be designed and made powerful enough to satisfy all needs.

*[Alex Stoia](https://ro.linkedin.com/in/alex-stoia-6b759944), CTO at Innertrends

In my experience, however, most companies cut corners on this and end up with staging setups that look nothing like Production. For example, they may hold a small fraction of the database, or run on totally different instances.

This defeats the purpose of staging and makes it unable to do its job.

More ideas about staging and release setups 👇

### 3) 📖 The two cycles of docs

In my experience, most companies have either a good workspace for docs, reasonably updated, where everyone contributes to, or basically no docs at all, or just very outdated ones.

There is hardly ever a middle ground. 

Why is that? Because documentation naturally leads to either a virtuous or vicious cycle.

When future value is higher than writing effort, you get a 🟢 **virtuous cycle**:

1. People write more docs because they feel they are valuable

1. Knowledge grows larger, more insights are discovered, decisions are taken faster and better

1. People read more and more docs instead of having meetings

When future value is lower than writing effort, you get a 🔴 **vicious cycle**:

1. People stop writing docs because no one reads them

1. Docs become partial and outdated

1. People don't trust and read docs anymore

![image](../assets/d2aa8d006b244a55.png)

Writing docs is a bit like like writing tests — people do it if the value of future use is perceived as superior to the writing effort. Wherever you stand on this, to improve you can either (or both):

1. **Increase future use** — by embedding them in processes, turning meetings into shared notes, etc.

1. **Reduce writing effort** — with processes, templates, and clear structure.

More ideas on writing good company docs 👇

[https://refactoring.fm/p/company-docs](https://refactoring.fm/p/company-docs)

---

### 📣 Join the Refactoring Talent Club

If you’re looking for a new gig, join to get personalized opportunities from hand-selected companies. You can join publicly or anonymously, and leave anytime.

Apply now

[https://refactoring-jobs.pallet.com/talent/welcome?utm_source=substack&utm_medium=email](https://refactoring-jobs.pallet.com/talent/welcome?utm_source=substack&utm_medium=email)

If you’re hiring, join the Refactoring Talent Club to start getting bi-monthly drops of world-class hand-curated Engineering people who are open to new opportunities.

![image](../assets/ed80c34a466e4d3e.png)

---

And that’s it for today! If you are finding this newsletter valuable, consider doing any of these:

**1) ✉️ Subscribe to the newsletter** — if you aren’t already, consider becoming a paid subscriber. You can learn more about the [benefits of the paid plan here](http://refactoring.fm/about).

Get full access to Refactoring today ✨

[https://refactoring.substack.com/subscribe](https://refactoring.substack.com/subscribe)?

**2)** ❤️ **Share it** — Refactoring lives thanks to word of mouth. Share the article with your team or with someone to whom it might be useful!

I wish you a great week! ☀️

Luca
