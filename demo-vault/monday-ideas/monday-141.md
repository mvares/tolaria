---
aliases:
  - "Monday #141"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-monday-idea|Publish Monday Idea]]"
Status: Published
"👓 Status": Not started
"Created time": "2025-01-28T14:32:00.000Z"
Date: 2025-02-03
"Has Notes":
  - "[[evergreen/the-lifecycle-of-code-quality|The Lifecycle of Code Quality]]"
  - "[[evergreen/the-delegation-path|The delegation path]]"
Tags:
  - Monday
  - Free
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 189bdf02-815c-802e-8c6a-dce8a725586e
---

# Monday #141

### 1) 🎨 Use design systems

Early last year I listed [a set of practices](https://refactoring.fm/p/new-tools-and-techniques-for-2024) that I believed you needed to consider in 2024.

Have you done it?! I don’t want to know 😄

Out of them, one of my favorite is using a design system. Design systems are not a novel idea — but they are an idea that has only been growing and improving with time. They address two issues:

1. Delivering *consistent* products at scale, and 

1. Making design work *more efficient*

So, what started as simple, static style guides, usually for corporates, has evolved today into full component libraries and best practices that can dramatically improve any team’s workflow. 

Modern design systems also bridge the gap between design and development: they are typically coded, version-controlled, and supported by dedicated tools, like [Storybook](https://storybook.js.org/).

So, just like there is consensus today about investing in platform and DX, I believe design systems are going to follow the same route and becoming commonplace, especially in the age of AI and [product engineers](https://refactoring.fm/p/how-to-become-a-product-engineer).

Here are a couple of recommended resources:

- [**Design Systems**](https://www.designsystems.com/) — a publication by Figma entirely dedicated to… well, you guessed it.

- [**Design ADRs**](https://zeroheight.com/blog/capturing-your-design-system-decisions/) — we covered the benefits of ADRs above, and you can make the same arguments for design work. Checkout this great article to learn more.

And you can find our full *technology radar *below* *👇

[https://refactoring.fm/p/new-tools-and-techniques-for-2024](https://refactoring.fm/p/new-tools-and-techniques-for-2024)

---

### 2) 🔄 Code quality is about systems

Code quality is not about individual performance or heroic efforts. It's about having systems and processes that consistently produce good outcomes.

I believe a team of average developers working within a well-designed system will outperform a group of exceptional developers working within a suboptimal system.

![image](../assets/189bdf02815c8058.png)

So here are the six steps that make up your quality system, and how they reinforce each other:

#### Encoded coding practices 📝

Everything starts with clear, documented practices that define what good code looks like for your team. These may include: system design principles and patterns, code organization and naming conventions, security and performance guidelines, docs requirements, and more.

Good encoded practices *inform* everything else: they make coaching and pairing easier; they enable laser-focused static analysis, and provide clear guidelines for code reviews.

#### Coaching & pairing 👥

The best teams actively share and discuss knowledge through good collaboration.

In my experience, the best ways are:

1. 👯 **Pairing** — I am a big fan of pair programming. I [wrote about it](https://refactoring.fm/p/pair-programming-in-2024) plenty of times, and will continue to do so!

1. ✏️ **Design discussions** — a good design process, possibly supported by good [design docs](https://refactoring.fm/p/design-docs?utm_source=publication-search), does wonders for your team’s growth. It helps you get to better solutions, coaches younger co-workers, and intercepts issues before it’s too late.

#### Static analysis 🤖

One of my [predictions about AI](https://refactoring.fm/p/predictions-about-ai) is that static analysis is going to be huge. What started as simple linting for stylistic errors, is gradually evolving to intercept code smells, security vulnerabilities, optimization opportunities, and more.

This is healthy because the more you can catch with automation, the easier code reviews get for humans.

#### Automated testing ✅

A solid test suite makes you *faster* by creating the confidence to change code without the fear of breaking things. I am very opinionated about testing and I don’t believe all tests are good. You should be intentional in what kind of tests to invest in, and for what parts of your codebase, to make sure the ROI is positive. I wrote more about this [here](https://refactoring.fm/p/how-to-test-software-in-2023).

#### Code review 🔍

Code reviews are your last line of defense. When everything else works, reviews should rarely spot crucial issues. Conversely, if they often do, you should ask yourself what other parts of the process are failing: should you discuss design more? do you have enough encoded practices? Is static analysis powerful enough?

Code reviews are the *worst* moment (before shipping) in which to spot problems, because they are the last. So, one of the goals of code reviews should be to **continuously reduce their own scope**, by making engineers uncover rules that can be enforced by previous parts of the dev process.

More thoughts (and hot takes!) about reviews in this [previous article](https://refactoring.fm/p/thoughts-on-code-reviews).

Also, here is our full piece about code quality in the age of AI 👇

[https://refactoring.fm/p/code-quality-in-the-age-of-ai?utm_source=publication-search](https://refactoring.fm/p/code-quality-in-the-age-of-ai?utm_source=publication-search)

---

### 3) 🔀 The Delegation Path

One of the most popular approaches to delegation is the **Eisenhower Matrix**, which buckets your tasks in four quadrants, based on **urgency** and **importance**.

The matrix advices to address tasks based on the quadrant they are in, and, in particular, to delegate those that are **urgent + not important**. 

![The original Eisenhower matrix — but you should aim to delegate everything, not just the bottom left](../assets/189bdf02815c80e0.png)

Now, I have found this advice hard to follow in real life, for two reasons:

1. **Urgent tasks** — are often hard to delegate. Delegation is a long-term play that in the short-term may require more time/effort than doing the thing yourself.

1. **Non-important tasks** — are ok, but they are often trivial, so if you only delegate those, you are limiting people’s growth.

So, I feel like Eisenhower Matrix is just tactical advice — incomplete at best.

Instead, to look at things from a more strategic perspective, there are three angles you can use. Ask yourself these questions:

1. 🌟 **Unique value** — *Where is your time spent best? What is the unique value you bring to the table?*

1. 🎓 **Skills** — *Are there people better equipped than you at handling some of your tasks?*

1. 🌱 **Growth** — *Are there people who are eager to learn how to do some of the things you do?*

My rule of thumb is: if at least two out of three drive me away from a task, I should probably delegate it.

So, I have found that you can draw a *path* on the eisenhower matrix, that goes from the easiest + least valuable to delegate, to the hardest + most valuable **👇**

![The delegation “path of enlightenment”  ](../assets/189bdf02815c807f.png)

1. 🥉 **Not urgent + not important** — despite what the matrix says, you can’t always *delete* these. Conversely, they are the safest and easiest to delegate.

1. 🥈 **Not important + urgent **— you need some structure already in place to delegate these in *timely* fashion, but you can still do so with little expectations on quality.

1. 🥇 **Important + not urgent **— the heart of good delegation. You need to establish what success looks like, how communication happens and who needs to be involved.

1. 🏆 **Important + urgent **— the apex of delegation. When you are able to delegate these safely, you know you made it.

More ideas on good delegation in this previous Refactoring article 👇

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
