---
aliases:
  - "Monday #94"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-monday-idea|Publish Monday Idea]]"
Status: Published
"👓 Status": Not started
"Created time": "2024-04-18T15:09:00.000Z"
Date: 2024-03-11
"Has Notes":
  - "[[evergreen/evaluate-tech-with-this-checklist|Evaluate tech with this checklist]]"
  - "[[evergreen/velocity-is-not-very-useful|Velocity is not very useful]]"
  - "[[evergreen/optimize-cycle-time-up-to-a-limit|Optimize Cycle time — up to a limit]]"
  - "[[evergreen/if-you-are-thinking-of-quitting-you-probably-should|If you are thinking of quitting, you probably should]]"
Tags:
  - Monday
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 4eeb0cca-1a8d-44a9-8836-18f3eb248161
---

# Monday #94

*Hey, Luca here! Welcome to a new edition of the* ***Monday Ideas*** 💡

*Every Monday I send you an email like this with three short ideas about making good software, working with humans, and personal growth.You will also receive a long-form* ***original essay*** **🧵** *every Wednesday, and a* ***podcast episode*** **🎙️** *every Friday.*

*Here are the latest editions you may have missed:*

### 1) 🚪 If you are thinking of quitting, you probably should

Now that I work *solo*, I try to stay in touch intentionally with some friends and past co-workers by having monthly or bi-weekly 1:1s with them.

Last week I spoke with a friend who is not happy at work and is thinking of quitting, but he is not sure.

He asked for advice, which I don’t feel qualified to give because these situations are very personal — they depend on work just as much as they depend on the rest of your life.

There is something I can say, though: **quitting is hard**.

Everything is stressful: looking for a new job, interviewing, negotiating, joining a new team of strangers — this is all way out of our comfort zone.

So, if you find yourself pondering to go through all this, chances are you already know it’s the right thing to do.

Most often, gut feeling knows it best — if you are thinking of quitting, you probably should.

I wrote a full piece about potential reasons to move on, and signs you should pay attention to. It explores three angles: **growth**, **money**, and **wellbeing**. You can find it below:

[https://refactoring.fm/p/quitting](https://refactoring.fm/p/quitting)

---

### 2) 🏆 Cycle Time vs Velocity

I am wrapping up the report from a wide survey around engineering productivity which I have been promoting on the newsletter for a while (if you participated, thank you so much 🙏).

I can anticipate that, when it comes to engineering metrics, there are two KPIs that are clear winners: **Cycle Time** and **Velocity**.

I believe, however, that they represent two different generations of metrics: Cycle Time is practical and useful in plenty of situations, while Velocity is kinda overrated.

Let’s see why.

#### Cycle Time

Cycle Time is a subset of the overall *Lead Time. *

Lead Time covers the whole cycle from ideation to release, including *analysis* and *design* phases, whose duration can vary a lot based on the breadth of the initiative. 

However, once the initiative itself has been broken down in deliverables, the delivery process itself should move in short and predictable *cycles*, which are more useful to measure. These are measured by Cycle time.

![image](../assets/5d290b6331164a79.png)

Cycle Time possesses all the hallmarks of great KPIs:

- **It is objective**: it doesn't need context to be interpreted, you know exactly what it means.

- **It is easy to understand**: it can be easily discussed and explained to management, as it works like the engineering equivalent of sales cycle and product funnel metrics.

- **It stays relevant as you scale**: it doesn't depend on the size of the team.

- **It is actionable**: it shouldn't fluctuate much. Significant increases usually point to specific problems that can be identified and resolved.

A healthy Cycle Time in real-world scenarios is anything within a few days. Further improvements are fine, but striving for less than one day brings diminishing returns.

So, breaking down work in small batches is important, but there is kind of an *optimal* batch size — under which you are only pedaling faster without delivering more value.

#### Velocity

Conversely, in my experience, velocity has limited utility. You can use it for rough sizing when planning work, but nothing more. For anything else, it is just misleading.

In fact:

1. **It is not a measure of productivity **— you can’t *optimize* velocity, at least not reliably. Since story points (or t-shirt sizes) are arbitrary, people will eventually just inflate the points. And it’s not because people are evil, it’s a natural, even unconscious, reaction to a bad way of defining productivity.

1. **It is not useful across teams **— velocity is only meaningful *locally* to the team, because of the arbitrary nature of estimates.

1. **It is too high level **— if you get bad velocity in a sprint, you can’t *drill down *into it to figure out what went wrong, as you can do instead with e.g. cycle time.

You can find more about engineering metrics in the full (free!) guide I wrote last year:

[https://refactoring.fm/p/how-to-get-started-with-engineering](https://refactoring.fm/p/how-to-get-started-with-engineering)

---

### 3) 🔍 Checklist for choosing tech

Choosing the right tech is a daunting task that depends on a large number of factors. At the end of last year I surveyed people in the community about their favorite criteria to make the right picks, and here they are, organized in a checklist:

**1) **☑️ **Success stories** — the #1 thing I look at is whether I can find examples of other products using that tech. Bonus points if such products are related to mine, in terms of scale or industry.

**2) **☑️ **Good Github repo** — for open source tech, the repo contains an awful lot of information you should consider. Look at the number of stars, frequency of commits, number of contributors, and open vs resolved issues. Is this a healthy project? Is this actively maintained?

**3) **☑️ **Governance** — on top of the above, is the project roadmap public? are issues visible? Is the *decision making* itself visible?

**4) **☑️ **Skin in the game** — who maintains this? Is this a company’s pet project? Or is it core to their business? Does the company have a track record of good support to projects like this?

**5) **☑️ **Good docs** — are docs comprehensive and clear? Do they refer to the latest version? Do they include my use case?

**6)** ☑️ **Community** — is there good enough community support? If I have any issues, is there anyone to ask?

I wrote a full guide about choosing technology that covers a lot more, like creating a good decision process with your team, and how to make buy vs build decisions 👇

[https://refactoring.fm/p/how-to-choose-technology](https://refactoring.fm/p/how-to-choose-technology)

---

### 📬 [Product for Engineers](https://newsletter.posthog.com/?utm_source=refactoring&utm_campaign=refactoring)

One of the clearer trends in tech careers in recent years is having engineers get more ownership and make meaningful product decisions. I wrote about [Product Engineers](https://refactoring.fm/p/product-engineers) in the past, and this is only growing stronger with time.

So today I am happy to promote [Product for Engineers](https://newsletter.posthog.com/?utm_source=refactoring&utm_campaign=refactoring), a newsletter from PostHog dedicated to helping engineers improve their product skills.

![image](../assets/ab80a062e7a248a8.webp)

You can subscribe for free to get curated advice on building great products, lessons (and mistakes) from PostHog, and deep dives into the strategies of top startups.

[https://newsletter.posthog.com/?utm_source=refactoring&utm_campaign=refactoring](https://newsletter.posthog.com/?utm_source=refactoring&utm_campaign=refactoring)

---

And that’s it for today! If you are finding this newsletter valuable, consider doing any of these:

**1) ✉️ Subscribe to the newsletter** — if you aren’t already, consider becoming a paid subscriber. 1500+ engineers and managers have joined already! Learn more about the [benefits of the paid plan here](http://refactoring.fm/about).

Get full access to Refactoring ✨

[https://refactoring.substack.com/subscribe](https://refactoring.substack.com/subscribe)?

**2)** 🍻 **Read with your friends** — Refactoring lives thanks to word of mouth. Share the article with your with someone who would like it, and **get a free membership** through the new [referral program](https://refactoring.fm/p/referral).

Read with your friends 🍻

[https://refactoring.fm/leaderboard](https://refactoring.fm/leaderboard)

I wish you a great week! ☀️

Luca
