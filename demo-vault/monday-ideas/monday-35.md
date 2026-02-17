---
aliases:
  - "Monday #35"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-monday-idea|Publish Monday Idea]]"
Status: Published
"👓 Status": Not started
"Created time": "2024-04-18T15:09:00.000Z"
Date: 2023-01-30
"Has Notes":
  - "[[evergreen/figure-out-what-makes-good-things-good|Figure out what makes good things good]]"
  - "[[evergreen/feature-flags-build-vs-buy|Feature flags build vs buy]]"
  - "[[evergreen/reduce-concurrent-work-to-improve-productivity|Reduce concurrent work to improve productivity]]"
Tags:
  - Monday
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 39627b36-6452-442f-b7f5-70502a37ea81
---

# Monday #35

*Hey, Luca here 👋 welcome to the ****Monday 3-2-1 ****✨*

*Every Monday I will send you an email like this with ****3 short ideas**** about engineering management, technical strategy, and good hiring.*

*You will also receive the regular long-form one on Thursday, like the last one:*

- [**LinearB – The Quest for Engineering Productivity**](https://refactoring.fm/p/linearb)

*To receive all the full articles and support Refactoring, consider subscribing if you haven’t already!*

Become a better tech leader today ✨

[https://refactoring.substack.com/subscribe](https://refactoring.substack.com/subscribe)?

*p.s. you can learn more about the *[*benefits of the paid plan here*](http://refactoring.fm/about)*.*

---

![image](../assets/71b0ab1eb4c544ad.png)

---

### 1) 🎽 What makes good things good

If great taste is knowing what’s good, and great skill is knowing how to build things, there is a third element that I consistently found in the most experienced people I have known.

They do not only know what is good — they also know exactly *why*. 

They know ***what *****makes good things good**. 

Which is less trivial than it seems.

I may watch hundreds of TV shows and develop a good, intuitive taste for good ones, but I may not be able to explain how my judgement works. And that may be fine, unless I ever want to *create* a TV show. At that point, closing that gap becomes crucial, because knowing what makes good things good is what ultimately allows my taste to *turn* into skills.

![image](../assets/1859520745854571.png)

In my experience, there are two main ways that help you with that:

- **Just build stuff** — being dissatisfied with your output constantly triggers your reasoning and makes you ask “why do I think this is crap?”.

- **Discuss with others** — when you discuss some subject, you need to elaborate on your judgment. If you disagree with somebody about something being good, chances are you want to figure out why.

I wrote more about taste and skills in this previous article 👇

[https://refactoring.fm/p/taste-vs-skills](https://refactoring.fm/p/taste-vs-skills)

### 2) 🚩 Feature Flags — build vs buy

Feature flags look like a simple system. Indeed, many teams I know have built **in-house solutions** to support them. 

However, since flags are useful for so many purposes, the scope of these systems tends to **creep** over time. 

People will ask support for A/B testing; for A/B testing you will need metrics and granular targeting; at that point you will likely need auditing, to track who changed what. 

Before you realize it, the flag service becomes the one with the highest load in your system, and keeping it fast and reliable becomes non-trivial.

Putting my CTO hat, my take is that **feature flags are a commodity**, with a cost of total ownership that can be very high. 

They also have strong lock-in, which is an argument often used *against* external services, but it is equally scary when you are locked into a nightmar-ish custom tool that you need to maintain forever.

So, you are probably better off either 1) using a managed service, or 2) hosting one of the many open source tools out there.

Which tools? Here they are 👇

- [LaunchDarkly](https://launchdarkly.com/) — arguably the most widely used tool for feature management, it is hosted and allows for granular user targeting.

- [Optimizely](https://www.optimizely.com/) — started as an A/B testing tool, it is now a full suite that includes feature flags, a CMS, marketing and e-commerce tools.

- [Unleash](https://www.getunleash.io/) — the most popular open source solution. Features are comparable to LaunchDarkly, and provides a [native integration](https://docs.gitlab.com/ee/operations/feature_flags.html) with GitLab.

- [GrowthBook](https://www.growthbook.io/?r=prd-ffs) — open source platform that you can either host or choose to use as a managed service. Simpler than many others, it still provides the basics: flags, A/B tests, segmentation.

- [Env vars + Doppler](https://www.doppler.com/) — some companies implement basic feature flagging via environment variables (we did that too, in the past). While this has clear limitations (e.g. changing a variable needs a reboot), it is also simple to setup and performance is very fast. In this case, you can use a service like Doppler to sync variables across the instances and manage them from a single place.

Feature flags are the unsung heroes of continuous delivery. You can find more ideas on why they are useful and how to use them here 👇

[https://refactoring.fm/p/feature-flags](https://refactoring.fm/p/feature-flags)

### 3) 🤹 Reduce concurrent work

One of the most effective ways to increase your team’s productivity is, *counterintuitively*, to reduce the amount of concurrent work.

The more things people have to juggle with, the more they lose effectiveness. Your whole team just gets worse:

- **More meetings** — with more projects, it gets harder to keep everyone on the same page. So you need more meetings, which further reduces the bandwidth for dev work.

- **More rework** — when people are spread too thin, they get things wrong more easily, which leads to rework and frustration.

- **Context switch** — the cost of switching from one task to another is real. With highly technical tasks, you need to load a giant context in your head before you are able to make any progress. This cost is pure overhead and you want to pay it as seldom as possible.

The nasty effects of concurrent work have been well understood since forever. [Kanban](https://email.mg1.substack.com/c/eJxNUMGOhCAM_ZrhaBAF9MBhL3vZjzAFqkNGwWDZiX-_OF42bdoU2r6-54BwSfk0ezqIXWGic0cT8X2sSISZlQPzFLxRQyfHoWfecC2ctiwc05wRNwirYXuxa3BAIcVPc8_HkT2NVX4QfgYNavaDni0oDjAq4OhmUHhDQvEBo0ODv5jPFJG5tG0Y6VrFVvMk2o9H9_UQ39UxNu_wCjv6AE3KS3266pp-IFqILBjBheCKCy67ak3XSDuMXHsxu1ZKq_Sj59vSNkexB4F7NRWPZbMWB_Un4wyOUg5xadxa7EVuui4qMdA5YQS7ojeUCzK6lfuoMC0YMVdF_QRkWiX7th_aXkilb56VjdStFiNvWYX2qU5F8w_uD940h8U), that got popular as early as in the 80s, explicitly tracks work in progress (WIP) as a KPI, and recommends setting hard limits for it. Low WIP positively correlates with lead time and little rework.

I wrote more ideas about engineering productivity in this previous article 👇

[https://refactoring.fm/p/engineering-productivity](https://refactoring.fm/p/engineering-productivity)

---

And that’s it for today! If you are finding this newsletter valuable, consider doing any of these:

**1) ✉️ Subscribe to the newsletter** — if you aren’t already, consider becoming a paid subscriber. You can learn more about the [benefits of the paid plan here](http://refactoring.fm/about).

Get full access to Refactoring today ✨

[https://refactoring.substack.com/subscribe](https://refactoring.substack.com/subscribe)?

**2)** ❤️ **Share it** — Refactoring lives thanks to word of mouth. Share the article with your team or with someone to whom it might be useful!

I wish you a great week! ☀️

Luca
