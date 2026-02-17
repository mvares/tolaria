---
aliases:
  - "Monday #166"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-monday-idea|Publish Monday Idea]]"
Status: Published
"👓 Status": Not started
"Created time": "2025-07-07T07:43:00.000Z"
Date: 2025-07-28
"Has Notes":
  - "[[evergreen/what-is-mobile-fragmentation|What is mobile fragmentation]]"
  - "[[evergreen/system-1-vs-system-2|System 1 vs System 2]]"
  - "[[evergreen/technical-debt-vs-product-maturity|Technical debt vs product maturity]]"
Tags:
  - Monday
  - Free
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 229bdf02-815c-800d-ae9f-eece6ddb8282
---

# Monday #166

### 2) 📱 What is mobile fragmentation?!

I always feel that non-mobile developers do not fully appreciate that sheer complexity involved in creating mobile apps.

A good chunk of such complexity is brought in by what we call *mobile* *fragmentation* — the sheer diversity of hardware and software across the millions of devices your application might encounter in the wild.

Mobile diversity is particularly awful for developers because it is *multi-dimensional*:

- 📱**Device manufacturers (the *****who*****) **—** **from the big players like Apple and Samsung, to the long tail of Xiaomi, Oppo, OnePlus, and the countless regional champions. Each comes with its own hardware quirks, custom Android *skins*, and unique interpretations of how Android *should* behave.

- 📋 **Operating systems & versions (the *****what***** & *****when*****)** —** **you need to account for multiple major versions active concurrently. Update rollouts lead to notorious lags, and some devices *never *get updated beyond a certain point. This is true for both iOS and Android, with Android being typically much worse.

- 📏 **Screen sizes & resolutions (the *****where*****)** — today’s smartphones range from compact screens, to *phablets*, foldables, and tablets: the range is vast. Other than physical size, you may also need to account for pixel density, aspect ratios, and newer features like dynamic refresh rates or screen cutouts (notches, punch-holes), that can all wreak havoc on your UI if not handled gracefully.

- ⚙️ **Hardware differences (the *****how*****) **—** **beneath the glass, there's even more: processors, memory constraints, GPUs, and sensors, which may or may not make a difference in how your app behaves.

Accounting for every permutation is impossible, so teams develop *strategies *based on user distribution, business goals, product stage, and more.

We tried to navigate all of this in the guide we wrote with the guys at BrowserStack back in May👇

[https://refactoring.fm/p/how-to-do-mobile-testing-right](https://refactoring.fm/p/how-to-do-mobile-testing-right)

---

### 3) 🧠 System 1 vs System 2

One of the latest books we read in our [book club](https://refactoring.fm/book-club) is [Thinking, Fast & Slow](https://refactoring.fm/p/thinking-fast-and-slow?utm_source=publication-search), by Daniel Kahneman.

The book is a masterclass in understanding how our mind work, and especially our hidden biases.  

Kahneman's central thesis revolves around two modes of thought: *System 1* and *System 2*.

- 1️⃣ **System 1** — is fast, intuitive, and emotional. It operates automatically and quickly, with little or no effort and no sense of voluntary control.

- 2️⃣ **System 2** — on the other hand, is slower, more deliberative, and more logical. It allocates attention to effortful mental activities that demand it, including complex computations.

What's surprising — and somewhat unsettling — is how much we rely on System 1, even when we think we're being logical and methodical. We often pride ourselves on our analytical abilities (especially in engineering 🫠), but Kahneman shows that we're far more inclined to do quick, intuitive judgments.

The main problem is that we don’t have a reliable way to figure out *when* to engage System 2 — the analytical side — vs accept the quick answer provided by System 1.

This perfectly displayed in the famous bat and ball problem:

> *"A bat and ball cost $1.10. The bat costs one dollar more than the ball. How much does the ball cost?”*

Most people answer 10 cents, which is System 1 stuff. The correct answer (5 cents) would require engaging System 2, but we usually accept the quick answer because it looks good.

This reminded me of chess. During lunch I often watch [Hikaru](https://www.youtube.com/@GMHikaru) videos, where he often talks about the problem of knowing *when to spend your time*. Modern chess has shifted more and more towards shorter time controls (e.g. 10-minute games), which means players spend little time, on average, on every move. What’s interesting, especially in grandmaster games, is that players do not spend a similar amount of time on every move — they *blitz* most of them (i.e. few seconds) and spend long chunks of several minutes on a few crucial ones.

Blitz moves are System 1—quick judgment and pattern-matching—while the long ones are when players engage their analytical brain.

Knowing *when* it is worth to spend more time on a move—i.e. when to engage System 2 vs when to trust intuition—is a crucial quality that separates outstanding players from the good ones.

Similarly, in real life, we need to *blitz* most decisions because System 2 is 1) **slow**, and 2) **extremely costly**, while System 1 is basically free. But we can still create good strategies to fight our biases and give System 1 less leeway.

You can find our full summary + review of the book below 👇

[https://refactoring.fm/p/thinking-fast-and-slow?utm_source=publication-search](https://refactoring.fm/p/thinking-fast-and-slow?utm_source=publication-search)

---

### 4) 🎒 Does *intentional* tech debt really exist?

When it comes to startups and fast growing products, you may hear about taking on debt **intentionally**, as the result of prioritizing speed and growth over engineering quality.

Regardless of whether this would make for a good strategy, in my experience, debt is most often **inevitable** rather than intentional. Fast growth, in fact, *naturally* leads to technical debt, because when the product changes at a fast rate, your engineering abstractions get invalidated equally fast.

Such volatility, though, changes with the maturity of your product. For the sake of simplicity, let’s consider three stages:

- 🐣 **0 to 1** — you start building a product from scratch, with a set of initial assumptions.

- 📏 **Product Market Fit** — you figure out what works, double down on it, and scrap the rest.

- 📈 **Scale** — you grow your business predictably and harden your tech.

The earlier you are on this scale, the more your product needs to move fast, and the more *leverage* you get by accruing debt.

The later you are on the scale, the more debt becomes a drag that *prevents* your product from growing. Your scale is such that you get the most leverage by *repaying* debt.

![image](../assets/229bdf02815c80e7.png)

For early stage startups it might be inevitable (and even healthy) to accumulate debt early on. At the same time, though, you should create processes to help repay debt from the very beginning.

You can find our full (and long!) guide on managing technical debt below 👇

[https://refactoring.fm/p/technical-debt](https://refactoring.fm/p/technical-debt)

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
