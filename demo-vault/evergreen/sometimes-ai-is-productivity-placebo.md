---
aliases:
  - "Sometimes AI is productivity placebo"
"Is A":
  - Evergreen
"Created at": "2025-12-29T10:58:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to": "[[essay/the-ai-productivity-paradox|The AI Productivity Paradox]]"
"Updated at": "2025-12-29T11:03:00.000Z"
Status: Not started
Tweet: "💊 Productivity placebo\n\n90% of engineers use AI for coding. However, productivity data is often self-reported, leading to misconceptions about actual productivity. AI coding assistants create a false sense of productivity due to instant feedback, resembling a \"fake state of flow.\" To avoid this trap, follow good work hygiene:\n↳ Stay engaged: Understand and review AI-generated code.\n↳ Do not multi-task: Focus on one task or allow full autonomy to AI for longer periods.\n↳ Make frequent pauses: Reset your focus regularly to avoid brain fatigue.\nAI amplifies both strengths and dysfunctions in development teams."
notion_id: 2d8bdf02-815c-803a-87b6-f0d18ba28e16
---

# Sometimes AI is productivity placebo

### 💊 Productivity placebo

One of the first findings from the DORA report is that **90% of engineers regularly use** AI for coding at work.

This is unsurprising, but also doesn’t say much. As Laura Tacho noted a few days ago, with the current state of telemetry tooling, we can’t even reliably measure how much code is truly written by AI.

![image](../assets/2d8bdf02815c801b.png)

Which leads us to the second problem, closely related to the first: **productivity data is largely self-reported**. In fact, the only way we can investigate AI productivity impact on a scale that goes beyond small experiments, is by asking developers how they feel about it — which DORA did, finding that they are happy about it. However, we also know that [the only time](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) we tried to measure productivity *without* trusting developers, by using proper control groups, we found that they *thought* they were more productive, while they were not.

Why does this even happen? Why do people’s instincts get misguided? I love this take from a recent [Cerbos article](https://www.cerbos.dev/blog/productivity-paradox-of-ai-coding-assistants) 👇

> AI coding assistants feel productive because they give instant feedback. You type a prompt and code drops in right away. That loop feels like progress, the same reward you get from closing a ticket or fixing a failing test. The problem is that dopamine rewards activity in the editor, not working code in production. […]

In other words, it’s **productivity placebo**.

Has it ever happened to you to get into a multi-hour bug-fixing rabbit hole, try everything and nothing works, you give up for the day, and then the morning after you get back and are able to fix it in 5 minutes?

This happens because the relentless bug fixing is like a **fake state of flow**. You get into a workflow that has a quick feedback loop (you change a small thing and immediately see if it works), and is cognitively easy to sustain, so you can go on for hours. But the reason why it feels easy is because you are not truly engaged. You are working on autopilot, and so, unsurprisingly, not making a lot of progress.

There is a way to work with semi-autonomous AI agents that feels exactly like this. You feel productive, but you are not.

So how do you escape it? To me it’s first and foremost about good work hygiene:

- **Stay engaged** — try to understand what the AI is doing, review the actual code, and possibly write a few bits yourself.

- **Do not multi-task** — I believe you should pick one of two extremes here. You either set things up in a way that the agent is autonomous for a *long *time, so that you can meaningfully do something else (e.g. a meeting), *or* you move in short enough iterations that allow you to follow the task and not wander to your email, browser, or Slack. Frequent context switch makes us stupid and less capable of intercepting AI mistakes.

- **Make frequent pauses** — e.g. get up for 5 mins every 30 (pomodoro-style), have a quick walk, and get back to work. Avoid your own *brain rot*, like in the bug fixing analogy, by forcing yourself to *reset* frequently.

If you only read the *titles* of these items, these would be good pieces of advice for any coding session: they just happen to be even more true when AI is in the loop.

So, in this case too, like in many others, AI works as an amplifier:

> The research reveals a critical truth: AI’s primary role in software development is that of an amplifier. It magnifies the strengths of high-performing organizations and the dysfunctions of struggling ones.

Now, even if you escape these traps and get *truly* more productive thanks to AI, there is a **more** **advanced trap** you need to take care of, which is that individual productivity doesn’t necessarily translate to team productivity 👇
