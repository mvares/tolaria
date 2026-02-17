---
aliases:
  - "Monday #116"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-monday-idea|Publish Monday Idea]]"
Status: Published
"👓 Status": Not started
"Created time": "2024-08-07T07:10:00.000Z"
Date: 2024-08-12
"Has Notes":
  - "[[Automate / Defer / Pair]]"
  - "[[evergreen/the-map-is-not-the-territory|The Map is not the Territory]]"
  - "[[evergreen/make-staging-optional|Make Staging optional]]"
Tags:
  - Monday
  - Free
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 2ffde15b-cde2-4dbe-b71e-2e8aa343c243
---

# Monday #116

Most AI developer tools focus on code generation. 

In my experience, the most time-consuming part is not writing code but finding the right context, especially during onboarding or refactoring legacy code. Decisions are scattered, and the right person isn't always available, wasting time on questions.

Unblocked saves time by providing accurate answers, reducing the need to search. Making the right decisions upfront equals to less rework.

### 1) 🔍 Are you happy with your code review workflow?

Code reviews are a double-edged sword. They're crucial for quality, but can easily turn into big bottlenecks.

Last month I proposed a simple approach, called **Automate / Defer / Pair** that chooses behavior based on different types of code changes:

#### **Automate simple tasks **🔧

For changes with low knowledge sharing and improvement potential, skip human review. Rely on static analysis and test pipelines instead. 

Examples are: fixing small bugs, adding tests, or minor cosmetic changes

#### **Defer reviews for most routine changes **↪️

Review the majority of code changes, but at a later time — without blocking merging. Why? Because quality improvements and knowledge sharing can happen post-merge.

It works especially well in continuous delivery workflows where you use [feature flags](https://refactoring.fm/p/feature-flags?utm_source=publication-search) to push changes frequently in a disabled state.

#### Pair for critical and complex changes 👯

When should you opt for real-time collaboration? It’s two scenarios:

1. 🔒 **High-stakes changes** — when correctness is crucial (e.g., database migrations, payment workflows)

1. 🧩 **Complex code** — large PRs or intricate algorithms where async reviewers lack context

Pairing works better in these cases because face time provides high-bandwidth communication, and allows for deeper and faster reviews, without all the async back-and-forth.

![In a mature engineering team, you should be able to do non-blocking reviews for most tasks, automate the simple ones, and pair on the remaining.](../assets/13ff9089eda64855.jpg)

You can find the full article with more ideas and the longer explanation below 👇

---

### 2) 🗺️ The Map is not the Territory

*The Map is Not the Territory* is a mental model that emphasizes the difference between our perceptions / models (the map) and the actual reality (the territory).

It reminds us that models are useful, but they are not the reality: their goal is to represent a *slice* of reality, in a way that is useful for a specific goal.

In other words, they are just *tools —* if you overstep their boundaries / goal, they may turn useless or even harmful.

This is true for all kinds of models, not just the big, high level frameworks we are covering today. We create models all the time:

#### **Software **💻

When designing software, we model how the system works in the form of diagrams, docs, and even tests. 

However, these are not a perfect representation of the actual code. 

A diagram could help understand the structure of your codebase, but it may not be exhaustive about dependencies, which makes it insufficient to decide e.g. how to partition the system.

#### **Project management **⏱️

We create plans, roadmaps, and resource estimates, to help us organize and deliver projects. 

However, these are not *the* projects themselves, and we must be prepared to adapt our plans if new information becomes available or unforeseen challenges arise.

Whenever you encounter a hard problem, focus on what you need to accomplish, and figure out what models / frameworks can be helpful.

I covered a wide range of mental models for engineers in this previous article 👇

[https://refactoring.fm/p/mental-models-for-engineers-and-managers](https://refactoring.fm/p/mental-models-for-engineers-and-managers)

---

### 3) 💣 Don’t remove Staging — make it optional

I know I have some radical views about simplifying release pipelines. For example, I try as much as possible to remove Staging environments and make devs push straight to prod.

Of course this assumes a lot of things: good tests, good instrumentation, breaking down work in small parts, etc.

![image](../assets/aefb9b6766834aa8.jpg)

It’s a journey, but especially when it comes to using Staging, you don’t need to do all or nothing.

Let’s say you analysed your workflow and figured out that:

1. A large chunk of changes could go straight to prod, but

1. there is a 20% of cases where you still need staging

What do you do?

The easiest improvement you can make is to **turn staging into an *****optional***** step** of your release process.

You separate the staging workflow from your main branching strategy, and give developers the agency to choose to either deploy to production or test on staging first, based on risk and complexity.

For many teams, this is 1) easy to do, 2) it builds ownership, and 3) it gets 80% of results with 20% of the effort

Win-win-win! Sometimes, when we design processes, we limit ourselves by thinking that things can only be **either always or never**.

There are often good solutions in between.

I wrote more ideas about staging environments here 👇

[https://refactoring.fm/p/do-you-need-staging](https://refactoring.fm/p/do-you-need-staging)

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
