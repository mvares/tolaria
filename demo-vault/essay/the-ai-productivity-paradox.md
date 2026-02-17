---
aliases:
  - "The AI Productivity Paradox"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-essays|Publish Essays →]]"
Status: Evergreened
URL: "https://refactoring.fm/p/the-ai-productivity-paradox"
"👓 Status": Not started
"Created time": "2025-10-31T08:09:00.000Z"
Date: 2025-11-26
"Has Notes":
  - "[[evergreen/make-things-simple|Make things simple]]"
  - "[[evergreen/collaboration-vs-coordination|Collaboration vs coordination]]"
  - "[[evergreen/higher-ai-usage-higher-context-switch|Higher AI usage == higher context switch]]"
  - "[[evergreen/sometimes-ai-is-productivity-placebo|Sometimes AI is productivity placebo]]"
Tags:
  - Guest
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 29dbdf02-815c-80bd-a601-eda6ba7826e6
---

# The AI Productivity Paradox

### ✍️ Post

---

Last week I finally caught up with the latest [DORA Research about AI](https://dora.dev/research/ai/). It is a massive, 140 pages doc, exploring the state of AI assisted development — and it gave me a lot to think about.

By now, there are a lot of reports out there (including [our own](https://refactoring.fm/p/the-state-of-ai-adoption-in-engineering)) that try to figure out how engineering teams are doing with respect to AI. Broadly speaking, there are three main areas that are important to measure:

1. 🔴 **Adoption** — how much engineers are using AI tools.

1. 🟡 **Productivity** — how much AI is making individuals and teams work faster.

1. 🟢 **Impact** — how much all of this turns into business outcomes.

These work as increasing levels of maturity, and increasingly better proxies for true value: adoption by itself is not very useful, productivity is somewhat better, and impact is what we truly care about.

The problem is: these topics are also in ascending order of *how hard* they are to measure. A lot of the available data is either fuzzy, or self-reported, or both, which makes it hard to trust.

So today I want to cover some of the ideas that keep surfacing in these types of research, common pitfalls to avoid, and mental models I have seen the best teams use to trend in the right direction — the one that goes from “adoption is high”, to “impact is high”.

Here is the agenda:

- **💊 Productivity placebo** — are you more productive, for real?

- ⛔ **Bottlenecks** — is the whole pipeline more productive?

- 🔍 **Quality traps** — are you more productive at the expense of something else?

- ⚔️ **Collaboration sucks** — an unpleasant but useful mental model.

- 🪄 **Making things simpler** — how do you trend in the right direction?

Let’s dive in!

---

*I discussed a lot of this with Doug from *[*Atono*](https://atono.io/)*, with whom I already wrote *[*this guide on creating a product engineering culture*](https://refactoring.fm/p/how-to-build-a-product-engineering?utm_source=publication-search)* a few months ago.*

*I am both a fan of Atono as a tool, and of how the team is *[*openly sharing everything*](https://atono.substack.com/)* about how they work, which includes many of the topics we’ll discuss today.*

[*Learn more about what Atono is doing*](https://atono.io/)* *

*Disclaimer: even though Atono is a partner for this piece, I will only provide my transparent opinion on practices and tools we covered, Atono included.*

---

### 💊 Productivity placebo

One of the first findings from the DORA report is that **90% of engineers regularly use** AI for coding at work.

This is unsurprising, but also doesn’t say much. As [Laura Tacho noted](https://www.linkedin.com/posts/lauratacho_most-news-headlines-about-some-company-writing-activity-7397243855068200962-zT-W?utm_source=share&utm_medium=member_desktop&rcm=ACoAAAVyY90BgAYglfc9McmePzN_c4b10ZpQ7OI) a few days ago, with the current state of telemetry tooling, we can’t even reliably measure how much code is truly written by AI. An engineer may accept an AI autocomplete, then change every single character, and that would still count as AI usage.

Which leads us to the second problem, closely related to the first: **productivity data is largely self-reported**. In fact, the only way we can investigate AI productivity impact on a scale that goes beyond small experiments, is by asking developers how they feel about it — which DORA did, finding that they are happy about it. However, we also know that [the only time](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) we tried to measure productivity *without* trusting developers, by using proper control groups, we found that they *thought* they were more productive, while they were not.

Why does this even happen? Why people’s instinct gets misguided? I love this take from a recent [Cerbos article](https://www.cerbos.dev/blog/productivity-paradox-of-ai-coding-assistants) 👇

> *AI coding assistants feel productive because they give instant feedback. You type a prompt and code drops in right away. That loop feels like progress, the same reward you get from closing a ticket or fixing a failing test. The problem is that dopamine rewards activity in the editor, not working code in production. […]*

In other words, it’s** productivity placebo**.

Has it ever happened to you to get into a multi-hour bug-fixing rabbit hole, try everything and nothing works, you give up for the day, and then the morning after you get back and are able to fix it in 5 minutes?

This happens because the relentless bug fixing is like a **fake state of flow**. You get into a workflow that has a quick feedback loop (you change a small thing and immediately see if it works), and is cognitively easy to sustain, so you can go on for hours. But the reason why it feels easy is because you are not truly engaged. You are working on autopilot, and so, unsurprisingly, not making a lot of progress.

There is a way to work with semi-autonomous AI agents that feels exactly like this. You feel productive, but you are not.

So how do you escape it? To me it’s first and foremost about good work hygiene:

- **Stay engaged** — try to understand what the AI is doing, review the actual code, and possibly write a few bits yourself.

- **Do not multi-task** — waiting is painful, but don’t let yourself detach from the task and wander to your email, browser, or Slack. Context switch makes you stupid and less capable of intercepting AI mistakes.

- **Make frequent pauses** — e.g. get up for 5 mins every 30 (pomodoro-style), have a quick walk, and get back to work. Avoid your own *brain rot*, like in the bug fixing analogy, by forcing yourself to *reset* frequently.

If you only read the *titles* of these items, these would be good pieces of advice for any coding session: they just happen to be even more true when AI is in the loop. 

So, in this case too, like in many others, AI works as an amplifier:

> *The research reveals a critical truth: AI’s primary role in software development is that of an amplifier. It magnifies the strengths of high-performing organizations and the dysfunctions of struggling one.

— *DORA Report 2025* *

Now, even if you escape these traps and get *truly* more productive thanks to AI, there is a more **advanced trap** you need to take care of, which is that individual productivity doesn’t necessarily translate to team productivity 👇 

---

### ⛔ **Bottlenecks**

As it’s well known, software development is a pipeline, and coding is just one part of it.

If a developer can implement a complete feature in 2 hours, but the PM needs 2 days to verify requirements, you are cooked. Or maybe it took two days to *write* the requirements beforehand, and you are cooked anyway.

This velocity mismatch can happen at any step, and, because of how queues work, the step with the lowest throughput becomes a bottleneck for the whole system.

![image](../assets/2aabdf02815c8034.png)

Bottlenecks have nasty second-order effects even on the *fast* steps: recent [research by Faros](https://www.faros.ai/blog/ai-software-engineering) shows that high AI usage in coding is strongly associated with higher context switch and bigger PRs.

![image](../assets/2aabdf02815c800a.png)

Why higher context switch? Because when developers are quick at writing code but constantly need to wait for review / QA / deploy, they switch to other tasks to keep themselves busy, which increases WIP, which in turn impacts quality, which in turn comes back to bite productivity 👇

### 🔍 **Quality traps**

When a step of the dev process is perceived as a bottleneck, the simplest and most tempting way to elevate its throughput is by relaxing its constraints:

- **Code reviews are slow?** → Make them lighter

- **QA can’t keep up with more features?** → Let’s just ship

It’s important to note that this is not necessarily bad. 

In fact, these are arguably good directions to *trend* towards, as long as they are enabled by your platform. We don’t want faster code reviews if it means engineers are sloppier about them, but we *do* want faster code reviews as the result of a lot of checks being automatically performed by the pipeline.

A sneaky way to relax constraints is to make AI do the thing. Does it take more time to write the PRDs than to build the feature? Let’s make ChatGPT write the PRD.

Again, this is good to trend towards if it’s done in the spirit of building platform—you document a task, improve the team’s understanding of it, delegate first drafts to AI, polish them (correct the output), and implement feedback (improve the input)—but it’s sloppy as a cheap way to do things faster.

Quoting an awesome [Reddit thread](https://www.reddit.com/r/ProductManagement/comments/1ml2a41/faang_pms_how_are_you_guys_improving_your_skills/) about how PRDs quality declined in the post-AI world:

> *Many critics note that as a result, quality declined. PRDs post-ChatGPT got worse, becoming overly long documents that said nothing. Readership dropped off a cliff when teams noticed AI-generated bloat. […]

How much time did you spend? User stories shouldn’t be taking you that long that you need AI help, and if they do, it’s a terrible trade off, don’t hand off to an LLM!*

---

### ⚔️ Coordination vs Collaboration

The last angle I want to explore is about collaboration, inspired by this great article by PostHog from last week: [collaboration sucks](https://newsletter.posthog.com/p/collaboration-sucks)

And I want to nitpick here: it’s not *collaboration* that sucks — it’s *coordination*. What’s the difference?

- **Collaboration** — is about many people contributing to an output.

- **Coordination** — is when, in order to do what I do, I need to take into account what other people do.

There can be collaboration *without* (or with minimal) coordination. To be precise, it is useful to think about coordination in three levels:

- **Sync coordination** — e.g. we hold a meeting to make a decision.

- **Async coordination** — e.g. I make a decision, but that needs to be approved before it is confirmed. In the meantime, I do something else.

- **No coordination** — e.g. I make a decision and it doesn’t need approval from others. Might get reverted if it’s wrong.

When you account strictly for throughput, these three are in **ascending order of efficiency**.

In reality, though, how you decide the right mode is about:

- **Probability** — how likely it is that a wrong decision is made, and 

- **Impact** — what happens if a wrong decision is made.

You always want to *trend* towards less coordination, given that these two factors are in check.

So, when you see coordination happening, it’s because *the process* believes that individual people, left to themselves, 1) would make wrong calls too often, and/or 2) wrong calls would be too bad for the product/business.

Assuming that’s true, how do you improve? How do you safely reduce coordination?

---

### 🪄 Making things simpler

Coordination exists because of cognitive load: stuff is hard and people can’t fit everything into their heads. This leads to layering & specialization, which in turn make coordination *required* to do things.

Some of this is necessary, but it’s important to understand that layering makes everything more complex. All of a sudden:

- Productivity is stiffer, because gains in one layer create bottlenecks elsewhere.

- Context about what to do gets *fractured* instead of being centralized, and more decisions are made based on local optima instead of global optima.

- Each layer uses its own tools and processes, making context more obscure and harder to recompose.

All of this is a mess for people, and is especially a mess for AI. Engineers use Claude Code and store some specs in the repo, PMs use ChatPRD or what else, some stuff is on Notion, some on Linear, and so on.

So, call it product engineering or however you like, if you read Refactoring you probably know I am bullish on merging some layers and going back to when people just did *more*.

That’s my bullish case for AI — to enable a *third era* of software engineering:

- **Yesterday: Web is simple** → each engineer does everything, but the tech doesn’t scale. Basically the PHP / JQuery era.

- **Today: Web is complex** → the tech now scales, but is (too) complex and engineers need to be layered into frontend, backend, infra, and more.

- **Tomorrow: Web is complex but we have AI** → same tech as today, but engineers can delegate a good chunk of cognitive load to AI, and do everything again.

---

*A little aside and a shout-out to Atono: having people do more makes me bullish, in turn, on tools that cover more ground.*

*The borders of tools largely exist because of the different people who use them — so what if we get less different people? What if engineers are closer to product, and PMs are closer to coding? *

*All of a sudden you can reshape what tools do, and try the unexpected. Like, feature flags support inside user stories, or a chrome extension for bug reporting from the same tool that you use to make your Q4 roadmap.*

*If you are in the mood for something new, give Atono a try!*
