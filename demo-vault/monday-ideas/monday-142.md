---
aliases:
  - "Monday #142"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-monday-idea|Publish Monday Idea]]"
Status: Published
"👓 Status": Not started
"Created time": "2025-02-04T14:01:00.000Z"
Date: 2025-02-10
"Has Notes":
  - "[[evergreen/use-design-systems|Use Design Systems]]"
  - "[[evergreen/with-ai-niche-stacks-will-thrive|With AI, niche stacks will thrive]]"
  - "[[evergreen/why-code-reviews-matter-two-extremes|Why code reviews matter: two extremes]]"
Tags:
  - Monday
  - Free
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 190bdf02-815c-80a7-9679-eda06ec95e49
---

# Monday #142

### 1) 🔨 AI will make niche stacks thrive

An underrated benefit of using AI coding tools is that you get *Universal Basic Proficiency* in pretty much everything. This especially helps niche languages and frameworks, making them easier to pick up.

Why is this important? Because I feel like we spent the last decade *consolidating* most of web dev around very few choices, making suboptimal calls to prioritize reusing the same skills, vs choosing the right tool for the job.

Nobody ever thought Electron apps feel or work better than native ones, but Electron still dominates because 1) you can write once and run everywhere, and 2) people prefer to write (e.g.) React than Swift.

Or, Rust is widely admired for its performance, memory safety, and concurrency. But even when these features matter, how many teams are actually learning Rust vs lazily creating yet another Node service?

AI drastically reduces the barrier to entry for any language and tech. This, I believe, will do wonders to the *diversity* of our stacks, which, in turn, will improve the quality of our apps.

I wrote more predictions about AI (at my own risk) in this recent piece 👇

[https://refactoring.fm/p/predictions-about-ai](https://refactoring.fm/p/predictions-about-ai)

---

### 2) 🎨 Use design systems

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

### 3) Code review horror stories 🔍

Code reviews are the main (and possibly only) **feedback loop** on how your team writes code.

This feedback loop not only catches defects but also aligns practices and culture. From high-level principles to naming conventions, many of these are enforced and even born out of code reviews.

This is sometimes hard to understand, so let me tell you two stories:

#### A no-reviews story ❌

I worked as an EM on a team that didn’t review code. The team of 4 senior engineers pushed code to prod all the time.

Things seemed fine, and code quality was good, but there were invisible problems:

- **Gatekeeping** — Each engineer had personal areas of ownership, impenetrable to others.

- **Inconsistency** — Different parts of the code had inconsistent naming, libraries, folder structures, etc.

- **No docs** — Little incentive to write and update docs.

These problems eventually led to more issues:

- **Collaboration** — Design, tradeoff, or estimate discussions were hard due to silos.

- **Hiring** — Onboarding new engineers was a nightmare.

- **Resource allocation** — Hard to invest in specific product areas.

- **Key man risk** — Individual engineers became too important, which was concerning.

This story shows the impact of not doing reviews goes beyond “*more bugs in prod*”. It affects almost everything you do in the long run.

#### A slow-reviews story 🐌

The other end of the spectrum is equally bad. Bad code reviews are usually *bad* in two ways, often simultaneously:

- **They are slow** — delaying release for hours or days.

- **They are superficial** — not improving the code or sharing knowledge.

Superficial reviews have the same problems as *no-reviews*, so no need to elaborate.

Slow reviews mess up engineers’ work. Once a developer submits a PR, their work isn’t over: they may need to implement improvements based on the review and ensure everything works in production.

![image](../assets/190bdf02815c804c.webp)

Including several hours of delay (multiplied by review iterations) makes engineers switch tasks, increasing WIP, cognitive load, reducing productivity, leading to batched releases, and a cycle of *badness.*

More thoughts on code reviews:

[https://refactoring.fm/p/thoughts-on-code-reviews](https://refactoring.fm/p/thoughts-on-code-reviews)

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
