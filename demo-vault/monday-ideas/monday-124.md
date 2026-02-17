---
aliases:
  - "Monday #124"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-monday-idea|Publish Monday Idea]]"
Status: Published
"👓 Status": Not started
"Created time": "2024-10-04T06:53:00.000Z"
Date: 2024-10-04
"Has Notes":
  - "[[evergreen/impostor-syndrome-is-not-dunning-kruger|Impostor syndrome is not Dunning Kruger]]"
  - "[[evergreen/how-to-advocate-for-tech-debt|How to advocate for tech debt]]"
  - "[[evergreen/pair-programming-is-productive|Pair Programming is productive]]"
Tags:
  - Monday
  - Free
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 115bdf02-815c-80da-98e1-e00601f6128e
---

# Monday #124

### Work OS

### 1) 🎽 Impostor Syndrome ≠ Dunning Kruger

Impostor syndrome is often conflated with the Dunning-Kruger effect. However, these are two very different things.

The **Dunning-Kruger **shows that individuals with low actual competence tend to overestimate their abilities (*overconfidence*). This confidence starts going down when they gain competence—which indeed can lead to feeling like an impostor—but it ramps up again when competence grows.

Individuals experiencing impostor syndrome, instead, tend to **continuously underestimate their abilities** (*underconfidence*), even as their competence increases, with the lowest perceived competence occurring at higher levels of actual competence.

![image](../assets/115bdf02815c80f7.png)

So, the TL;DR is: the Dunning-Kruger is nothing to worry about. While impostor syndrome involves *persistent *self-doubt and often leads to anxiety, Dunning-Kruger is 1) temporary, and 2) doesn’t necessarily cause emotional distress.

I wrote more about impostors, insecurity, and all these nasty things in this recent article last month 👇

[https://refactoring.fm/p/how-to-deal-with-insecurity-and-impostor](https://refactoring.fm/p/how-to-deal-with-insecurity-and-impostor)

---

### 2) 👯 Pair programming is actually productive 

If you have been reading Refactoring for a while, you know that every now and then I just *need* to promote pair programming. It is just so underrated.

Today I address the common criticism about *productivity* — that is, that two developers who pair produce less code that working separately.

First of all, we should all know that the metric for successful programming is not the number of lines of code, but the ability to solve a problem in a maintainable, and understandable way for the long term.

> “*If you have two engineers on one computer, won’t they type half as much code?*“

BUT STILL, let’s talk about output. Research found [[1](https://collaboration.csc.ncsu.edu/laurie/Papers/XPSardinia.PDF), [2](https://www.cs.utexas.edu/users/mckinley/305j/pair-hcs-2006.pdf)] that the *raw output *of a programming pair, in terms of tasks they accomplish, is **only 15% smaller** than that of two independent developers.

Why is that? For two main reasons:

- 📱 **Less distractions** — two people are less likely to get distracted than one. That short trip to Twitter doesn't look all that appealing when there is someone by your side. Also, if one of you loses focus or is interrupted, the other can remain in a flow state, and quickly bring you back in. 

- 👁️ **More awareness** — when working for hours on a problem, you might lose perspective of the main task. Remember that time you spent all afternoon on a bug and then fixed it in 10 minutes the morning after? That’s when the “*state of flow*” gets toxic and turns into tunnel vision. This doesn’t happen in a team of two.

That said, this 15% gap is *easily *repaid down the line by three factors:

- **No code reviews** — all the code is automatically reviewed. No further PRs to stop you from shipping. Also, chances are this kind of review is way better than your usual PR.

- **Less WIP **— assigning more people to tasks means there are automatically less tasks in progress at any given time. Less tasks in progress equals less context switch, less batching, more focus, and better output.

- **More quality **—  Pair programming consistently leads to higher code quality. Two people bring in better problem solving, which leads to better design. This in turn brings in less bugs, less bad abstractions, and less time spent on maintenance over time.

Here is my full piece on the secret power of pair programming 👇

[https://refactoring.fm/p/pair-programming-in-2024](https://refactoring.fm/p/pair-programming-in-2024)

---

### 3) 🤝 How to advocate for tech debt

On a recent [mastermind session](https://refactoring.fm/p/introducing-the-refactoring-mastermind?utm_source=publication-search), a CTO confessed they feel unable to advocate for big tech debt work. How can they convince other executives that some technical work is worth doing?

Here is the advice that was shared in the session:

#### 1) Bring data 🔍

When it comes to refactoring, migrations, and other work under the hood, I have found that there are three types of data you can use to advocate for it:

1. 🏅 **Customer KPIs** — the impact of bad code can easily leak to customers through outages, latency, or reported bugs. This is the easiest angle for business stakeholders to understand, and the first you should look into.

1. 🚚 **Productivity** — chances are your dev experience is impacted by the debt. You can measure this in terms of time spent on maintenance, code churn, or other metrics about specific parts of the dev process (e.g. your CI/CD got slower and slower and it now takes 2 hours to deploy). Being able to say “if we get this done we can ship 10% more features”, backed by convincing numbers, is powerful.

1. 🔭 **Enablement** — finally, consider product evolution. Does this work *enable *product features we couldn’t do before? In my experience, the enablement angle is the best way to *partner *with* *PMs on debt, which in turn is one of the most effective ways to get things done.

Now, sometimes data is not enough. Sometimes you don’t have enough of it, or you believe you have, but it’s not enough for your *interlocutors*.

This is where trust comes into play 👇

#### 2) Create trust ❤️

Data matters, but sometimes it is tough to obtain. Thankfully, there is *a ton* of work that gets done purely because of trust. And that’s ok. Trust makes* *work faster and riskier — which, in many cases, is a good tradeoff.

Also, this is not black or white. A successful argument might be based on 80% data and 20% trust, or 50:50, or you name it.

More trust can *compensate* for less data, so, for tech debt work, if you can’t get your point across, you can either bring more data, or more trust.

To do the latter, here is my advice 👇

#### 3) Create a track record 🥇

Advocating for tech work is easier when you have a successful history of tackling other tech work. 

You can bring this up explicitly in conversation, showing success stories from the past where similar actions led to similar benefits.

If you don’t have such track record, start building it, and start small: solve small pieces of debt, document it, and celebrate it. Build momentum and confidence that you can take larger actions.

#### 4) Involve others in the decision process 🔄

Another strong factor in building trust is involving others *early* in the process. Partner *early* with peers, PMs, and people whose opinion is legitimately important for your cause.

Partner with them when you are still *unsure* that the work is worth doing, and get to a conclusion together.

Conversely, do not autonomously decide for a course of action and *then* make the case to justify it to others. This can come across as disingenuous, and people may feel you are pushing some personal agenda.

#### 5) Don’t make it all-or-nothing ⚖️

Finally, whenever possible, present different levels of investment.

Maybe the leadership isn’t ready to commit to a 6-month rework, but they would test the waters with a 1-month proof of concept. You may 1) do the most important piece first, in a fraction of the time, 2) show success, and 3) get green light for the rest of the work.

I published more lessons from our masterminds in this newsletter edition 👇

[https://refactoring.fm/p/lessons-from-the-mastermind-sessions](https://refactoring.fm/p/lessons-from-the-mastermind-sessions)

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
