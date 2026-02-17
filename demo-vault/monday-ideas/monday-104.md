---
aliases:
  - "Monday #104"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-monday-idea|Publish Monday Idea]]"
Status: Published
"👓 Status": Not started
"Created time": "2024-05-17T07:38:00.000Z"
Date: 2024-05-20
"Has Notes":
  - "[[evergreen/manager-vs-engineer-feedback-loop|Manager vs Engineer feedback loop]]"
  - "[[evergreen/qa-is-about-end-to-end-testing|QA is about end-to-end testing]]"
  - "[[evergreen/invest-in-abstractions-that-are-core-short-term-payoff|Invest in abstractions that are core + short-term payoff]]"
Tags:
  - Monday
  - Free
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 9ba0425c-6e82-4745-b7fe-06a9a40df50b
---

# Monday #104

### 1) 🔄 Manager vs Engineer feedback loop

There are countless ways in which your job changes when you go from being an IC to a manager, but one of the most peculiar is your **feedback loop**.

The feedback loop for your work is the way you *learn* whether what you are doing is good, is working, and how you can do better.

- **🔨 As an engineer** — your feedback loop is *short*. You develop a feature, release it, see how it works and move on to the next thing. You work in *small batches*, and you have a direct understanding of how you are doing.

- 🎽 **As a manager **— your feedback loop is *murky*. You work on systems and processes, and measuring these 1) is hard, and 2) takes a long time. E.g. we have removed standups: are we doing better? How do we even know? 

These challenges for a manager exist, in a way, by design — because the manager’s role is *naturally* more about the *future* than that of an IC. 

Nevertheless, you should strive to create good feedback loops even when it’s harder to do so. In a manager’s work, this is often about *qualitative *data, rather than quantitative. 

E.g. is the *developer experience* hard to measure? Run a survey. Talk with people. 

In other words, while feedback for engineers is more explicit and continuous, for managers it most often requires *asking* for it.

This is one of the things we discussed with my friend [Thiago Ghisi](https://twitter.com/thiagoghisi) during our chat on the podcast:

[https://www.youtube.com/watch?v=vO-EX0HHaB8&](https://www.youtube.com/watch?v=vO-EX0HHaB8)

More lessons from the first season of the podcast here 👇

[https://refactoring.fm/p/the-top-10-lessons-from-our-podcast](https://refactoring.fm/p/the-top-10-lessons-from-our-podcast)

---

### 2) 🔍 QA vs end-to-end testing

When we talk about QA, we usually refer to a specific approach to testing — that is, testing the product like a final user. This means actually *using* features and workflows to figure out if something is broken.

A few months back I wrote a full piece about testing, which identified three main categories of tests: **unit**, **integration**, and **end-to-end**.

With some degree of simplification, QA is about end-to-end testing.

End-to-end testing is, again, testing your product from the user perspective. This is also often called **black-box testing**, because it can be performed without much knowledge of tech internals — as opposed to white-box testing, like unit and integration testing, that is more coupled to the specific tech.

Honestly I am not a big fan of this definition, because, to me, this looks like a continuum, more  than black/white 👇

![image](../assets/b91bfb638eba47e5.png)

If you imagine tests as a pyramid with unit tests at the bottom and end-to-end tests at the top, then the higher you go, the more complex the workflows you're testing. And the more you move upwards, the more layers you have below, which is what makes the box *darker.*

In fact, each layer acts as a black box for the ones below:

- Unit tests ignore the specific implementation of functions.

- Integration tests ignore how workflows are performed internally.

- End-to-end tests ignore pretty much everything below them.

You can find my full article about testing below 👇

[https://refactoring.fm/p/how-to-test-software-in-2023](https://refactoring.fm/p/how-to-test-software-in-2023)

---

### 3) ⚖️ Abstractions vs payoff

Most of the times, when talking about fast-moving startups, we warn against creating premature abstractions because these may be invalidated by the product evolution.

Something that is true today might not be true tomorrow, so we should only invest, engineering-wise, on what feels *core*.

In my experience, however, that’s not enough to guarantee that an abstraction is successful. The other angle you should consider is the **timeline** **for its payoff**.

You may invest in the *right* abstraction, but whose payoff is too far in the future, and that still leads to failure. You may be accounting for 10x the traffic, or 10x the engineers, and don't live enough to see it.

With time and gray hair I have become more and more conservative about tech investments. 

As a startup you should focus on stuff that is truly core to your value prop, and whose payoff is reasonably short-term.

![image](../assets/17357e33eb854ddb.png)

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
