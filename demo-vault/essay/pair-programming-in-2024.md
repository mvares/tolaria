---
aliases:
  - "Pair Programming in 2024"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-essays|Publish Essays →]]"
Status: Evergreened
URL: "https://refactoring.fm/p/pair-programming-in-2024"
"👓 Status": Not started
"Date HH": 2024-11-28
"Created time": "2024-04-18T14:53:00.000Z"
Date: 2024-02-28
"Has Notes": "[[evergreen/pair-programming-is-productive|Pair Programming is productive]]"
Tags:
  - Updated
  - Software
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 5e585f16-a532-4666-91b3-e48f1f5a425e
---

# Pair Programming in 2024

### ✍️ Post

---

### [Talking Pair Programming](https://www.youtube.com/watch?v=q9UsW-uKu1M)

### [The Power of Pair Programming](https://www.youtube.com/watch?v=fUKheBx8YQo&t=1s)

### Intro

Over the last two podcast episodes, respectively with Farhan and Kent, we talked a lot about pair programming. 

In fact, pairing is one of the core practices advocated by Kent in extreme programming, and is widely adopted in Shopify, too.

This shouldn’t be surprising — all studies about pairing (which go back to the [early 2000s](https://www.researchgate.net/publication/2333697_The_Costs_and_Benefits_of_Pair_Programming)) report overwhelming benefits, including happiness, growth, code quality, and even overall productivity. 

Yet, it is still *kinda *surprising to hear about teams and people pairing regularly. 

Why is that?

Farhan argues that pair programming is the *underhanded free throw* of engineering. Underhanded free throws have been proven to be better than normal free throws at everything except one thing: **they look stupid**.

And pair programming *does *look stupid, to everybody:

- 💼 **To managers, it feels like a waste** — it's two devs working on the same code, when they could be doing two separate things.

- 🔨 **To developers, it feels uncomfortable** — social interaction is draining. And what about the sacred *state of flow*?

Nevertheless, there exist extremely successful companies who pair *regularly*, or *most of the time*, or even *all the time*. In some cases, they have been doing so for *decades*, and they loudly advocate the case for it.

I wrote my first (and only) piece on pair programming in 2021, so it is time for a beefy update, which includes everything I learned over the past three years by talking with tens of tech leaders, trying new tools, and even consulting to companies who were into pairing.

So, this article is my best attempt to demystify pair programming and tell you everything you should know about it:

- **If you pair already**, this is the piece you will send to your skeptical friends.

- **If you don’t pair**, this is the piece that will make you a convert, or will at least make you try.

Here is the agenda:

- 🏆 **Why you should pair program **— let’s talk about productivity, knowledge, happiness, and soft skills.

- 📖** How to pair program **— the most popular techniques and when to use them.

- ⏱️** How to plan for pair programming **— what goes into a session and how to make it successful.

- 🔨 **Tools for pair programming **— you don’t pair on Zoom. A short list of the best tools to elevate the pairing experience.

- **❓ FAQs** — a greatest hits of the most frequent questions I get about this, including how to allocate resources, should managers pair, should you pair remotely, and more.

- 📚 **Resources** — further guides, articles, and papers to learn more.

Let’s dive in!

---

### 🏆 Why you should pair program

Pair programming is consistently adopted by some of the most well-known engineering teams in the world. The degree of adoption varies — here are some examples:

- Pair **regularly** → [GitLab](https://about.gitlab.com/blog/2021/02/04/remote-pair-programming-tips/#how-to-get-the-most-out-of-remote-pairing), [GitHub](https://deepcollaboration.simplecast.com/episodes/jason-warner-cto-github), [Atlassian](https://www.atlassian.com/blog/technology/remote-pair-programming-tools-process)

- Pair **most of the time** → [Thoughtworks](https://martinfowler.com/articles/on-pair-programming.html)

- Pair **all the time** → [Pivotal](https://review.firstround.com/Why-Every-Startup-Should-Pair-Program)

Such companies report strong benefits that can be organized in four main categories:

1. 🏃‍♂️ **Productivity**

1. 📖 **Knowledge Sharing**

1. ❤️ **Happiness**

1. 🎽 **Soft skills**

Some of these are to be expected, while others are wildly counterintuitive. Let's see them one by one 👇

#### 1) Productivity 🏃‍♂️

The metric for successful programming is not the number of lines of code, but the ability to solve a problem in a maintainable, and understandable way for the long term.

> “*If you have two engineers on one computer, won’t they type half as much code?*“

BUT STILL, let’s talk about output. Various studies [1, 2] suggest that the *raw output *of a programming pair, in terms of tasks they accomplish, is only 15% smaller than that of two independent developers.

Why is that? For two main reasons:

- **Less distractions** — two people are less likely to get distracted than one. That short trip to Twitter doesn't look all that appealing when there is someone by your side. Also, if one of you loses focus or is interrupted, the other can remain in a flow state, and quickly bring you back in. 

- **More awareness** — when working for hours on a problem, you might lose perspective of the main task. Remember that time you spent all afternoon on a bug and then fixed it in 10 minutes the morning after? That’s when the “*state of flow*” gets toxic and turns into tunnel vision. This doesn’t happen in a team of two.

That said, this 15% gap is *easily *repaid down the line by three main factors:

- **No code reviews** — all the code is automatically reviewed. No further PRs to stop you from shipping. Also, chances are this kind of review is way better than your usual PR.

- **Less WIP **— assigning more people to tasks means there are automatically less tasks in progress at any given time. Less tasks in progress equals less context switch, less batching, more focus, and better output.

- **More quality **—  Pair programming consistently leads to higher code quality. Two people bring in better problem solving, which leads to better design. This in turn brings in less bugs, less bad abstractions, and less time spent on maintenance over time.

#### 2) Knowledge Sharing 📖

Pair programming is a phenomenal knowledge sharing device. There are at least three use cases for which such sharing is valuable:

- **Double ownership** — code written this way has two owners out of the box. This makes your team more cohesive, resilient to turnover, and flexible in work allocation. It is also hard to replicate in any other way.

- **Onboarding** — pair programming makes onboarding faster. It makes new hires get in touch with your practices, your culture, and it also helps them develop early relationships with peers.

- **Learning** — you may pair people with different skill levels to accelerate the learning process of younger members. This is awesome for *teachers*, too, who develop coaching behaviour and increase their impact.

#### 3) Happiness ❤️

One of the most common objections to pair programming is that it is draining due to the continuous social interaction. It is also believed that, being many developers **introverted**, they would come to despise this interaction.

Pair programming *is *tiring indeed, especially at the beginning, but people get used to it, and grow to love it. Cockburn and Williams notice in their study:

> *In statistically significant results, pair programming teams who had earlier programmed alone reported that they enjoyed pair programming more and that they were more confident in their programs than when they programmed alone.*

But *how* *much* more? In a survey among the same participants, a stunning 80%+ of developers reported they enjoy working *more* because of pair programming.

![Share of developers who enjoy their work *more* because of pair programming. It’s over 80% for all cohorts.](../assets/9a36151e139f466e.png)

Participants report a new sense of confidence and shared ownership, that ultimately makes them happier. Quotes from actual developers 👇

> *I find it reassuring to know that my partner is constantly reviewing my code while I drive.*

> *It’s nice to celebrate with somebody when something works.*

So, I am introvert myself, and I can relate to all the concerns. However, while it is true that introverts don't like much interaction, we *do* crave **deep interactions** with those who are close to their interests.

Pair programming allows to develop deep relationships without being socially overwhelming, which is the best possible scenario for an introvert.

#### 4) Soft skills 🎽

Finally, pair programming emphasises **communication**, giving and receiving constructive **feedback**, and working together towards a **goal**.

These skills are crucial in all other kinds of situations, from managing people, to mentoring, to negotiating with stakeholders. Engineers who pair regularly experience a professional growth that goes well beyond coding.

---

### 📖 How to pair program

There exist two main *styles *of pair programming:

- 🚗 **Driver / Navigator**

- 🏓 **Collaborative / Adversarial** (aka Ping Pong)

Let’s look at both:

#### 1) Driver / Navigator 🚗

At any given time there is one person who writes code, and one that observes. These are respectively called **Driver** and **Navigator**.

The Driver is focused on the here and now — the **current step**. As a Driver, you should think out loud, talk about what you are doing, what you are going to do and how.

Navigators are trickier, and that’s how many people get confused. Navigators help with three main things:

- **🧠 Brainstorm **— they discuss design choices and suggest the way forward.

- 👁️** Focus **— they keep the focus on the final goal and make sure the task relates to it.

- **🔍 Review **— they spot errors and propose improvements. Just like a regular code review, but in real time.

#### 2) Collaborative / Adversarial (aka Ping Pong) 🏓

Ping pong pairing is when you work in parallel with your buddy on separate things. A popular choice is to have one developer taking care of tests, and the other of the implementation. 

This is called *adversarial *because while one of you works on making tests *fail*, the other works making them *pass*. It is also a great way to practice TDD, especially on tricky designs.

[Jono Stiansen](https://twitter.com/jonocodes), Engineering Manager, on this 👇

> *We used to do full XP, meaning we’d always pair and do TDD and we generally didn’t have PRs because the idea was we already had been reviewed by at least two eyes.*

#### When should you use one style vs the other?

Pair programming depends a lot on the *chemistry *between developers, so personal preference is always the first deciding factor.

If you are unsure, the driver / navigator style is the most popular, so that’s what I would suggest to get started, but feel free to experiment different styles for different tasks.

You can also do all kinds of hybrids, like starting adversarial to get the first tests out, and then continue in driver / navigator style.

---

### 🗺️ How to plan for pair programming

Pairing sessions require more planning that going solo. If when you are alone you can just open the editor and wing it, that’s not true when there’s two of you (and that’s a good thing).

So here what you should nail about your pairing session:

1. **Duration of the session **— how much will you work together? Decide in advance and sync the respective calendars.

1. **Agree on the high-level goal **— what you want to accomplish, not necessarily how.

1. **Break the work **— down into smaller tasks, and prioritize them. 

1. **Decide your pairing strategy **— whatever style you choose (e.g. driver / navigator) always work in short batches. For example: code for 25 minutes; take a 5 minute break; swap roles.

1. **Configure Git to share credit **— here is a [handy guide](https://docs.github.com/en/pull-requests/committing-changes-to-your-project/creating-and-editing-commits/creating-a-commit-with-multiple-authors) for Github. There are also plenty of tools that help you with it, my preferred one being [git-together](https://github.com/kejadlen/git-together).

1. **Configure your pairing tool of choice** — more on that later.

1. **Work **— do the thing!

1. **Analyze the session** — with a mini retro at the end. How did that feel? What went right? What can you do better next time? This is a crucial conversation to have, especially at the beginning.

---

### 🔨 Tools for Pair Programming

This is an area that has seen *huge* improvements in the last few years.

In fact, while nothing beats two folks sitting side by side IRL, remote pairing today is a delightful, highly effective experience. So much so that pairing setups are being used for more than pure programming. People pair on incidents, on design docs, diagramming, and more.

Here are my tools of choice for it:

- [**Tuple**](https://tuple.app/)

- [**CoScreen**](https://www.coscreen.co/)

- [**Pop**](https://pop.com/)

These are all good. If I have to pick one, it would be Tuple — unobtrusive, lots of nice touches, and it just works, especially for programming. But again, these are all good, choice comes down to personal preference.

---

### ❓ FAQs

So let’s wrap this up with the top questions I receive about pairing, from readers of the newsletter and people in the community.

#### 1) When should you pair program vs when is it not worth it?

Pair programming is best when it allows you to produce high quality software and share knowledge in the process. Kent Beck says:

> *Pairing works when there is sufficient uncertainty in the problem be solved and the approach to solving it.*

Viceversa, pairing might not bring much value for mechanical or trivial tasks that both members could accomplish by themselves. If the work doesn't require taking any decisions, and there is no learning involved, you might as well avoid pairing.

#### 2) Is pair programming effective remotely?

Absolutely! Pairing is one of the best ways two remote engineers can spend their time. Other than being *effective* per se, it is a fantastic way to build strong relationships, which is especially important in remote teams.

#### 3) Should managers pair program?

For engineering managers who want to stay technical and hands-on, pairing with engineers is one of the best ways to do so. Way better than doing code reviews *pretending* that you know what you are doing!

#### 4) How do you allocate resources for pairing?

This is a popular one, that the answer is simple: you just assign two people to the task. That’s it.

#### 5) How often should you pair? 

This depends on many factors: familiarity with pairing, complexity of tasks, engineers preferences, and more.

If you want to build the habit, you may start by intentionally pairing ~20% of the time, on the most challenging tasks. So, for each dev cycle, you may create the habit of picking the top, most complex item, and assign it to two engineers.

#### 6) Can you pair in more than two people?

Yes, and it’s usually deemed *mob programming*. [Shreyas Patil](https://www.linkedin.com/in/shreyaspatil), Senior Software Engineer, told his experience in the community:

> *We have a high density version of pair programming often referred as “mob programming”. So, we have set aside a Friday every two weeks where we gather to work on a problem or tech-debt.*

---

### 📚 Resources

Finally, here are the best additional readings I have found about this:

- **📑 **[**On Pair Programming**](https://martinfowler.com/articles/on-pair-programming.html) — this article from Thoughtworks is a comprehensive guide on pair programming that covers the benefits, challenges, and everything you need to know.

- 📑 [**Pair Programming Guide**](https://tuple.app/pair-programming-guide/) — the Tuple’s guide to Pair Programming. Also extremely good.

- **📑 **[**The Costs and Benefits of Pair Programming**](https://collaboration.csc.ncsu.edu/laurie/Papers/XPSardinia.PDF) — a peer-reviewed paper by Cockburn and Williams about the outstanding impact of pair programming on engineering teams.

- **📑 **[**Pair programming productivity: Novice–novice vs expert–expert**](https://www.cs.utexas.edu/users/mckinley/305j/pair-hcs-2006.pdf) — another interesting paper that shows how pairing is particularly helpful to novice engineers. 

---
