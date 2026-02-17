---
aliases:
  - "# Writing a Good CLAUDE.md"
"Related to": "[[readings-digest/weekly-digest-3|Weekly Digest #3]]"
Summary: CLAUDE.md should concisely onboard Claude to your codebase by explaining the project’s WHAT, WHY, and HOW. Keep instructions minimal and universally applicable, and use progressive disclosure with separate docs for task-specific details. Rely on linters and hooks for formatting and avoid auto-generating the file.
"Discarded for digest?": false
"Note Status": Saved
URL: "https://www.humanlayer.dev/blog/writing-a-good-claude-md"
Author: Kyle Mistele
Category: Articles
"Full Title": "# Writing a Good CLAUDE.md"
Highlights: 17
"Last Synced": 2025-12-10
"Last Highlighted": 2025-12-03
notion_id: 2c5bdf02-815c-81e0-b4a1-f131abf40262
---

# # Writing a Good CLAUDE.md

LLMs are stateless functions. Their weights are frozen by the time they're used for inference, so they don't learn over time. ([View Highlight](https://read.readwise.io/read/01kbhrgqc13ajj8a4xm2vt73vw))

Since Claude doesn't know anything about your codebase at the beginning of each session, you should use `CLAUDE.md` to onboard Claude into your codebase. ([View Highlight](https://read.readwise.io/read/01kbhrhzdgqzsfhgznd64jeyzh))

**WHAT**: tell Claude about the tech, your stack, the project structure. Give Claude a map of the codebase. This is especially important in monorepos! Tell Claude what the apps are, what the shared packages are, and what everything is for so that it knows where to look for things ([View Highlight](https://read.readwise.io/read/01kbhrj0yaa5yvy2143fy3kbw5))

**WHY**: tell Claude the *purpose* of the project and what everything is doing in the repository. What are the purpose and function of the different parts of the project? ([View Highlight](https://read.readwise.io/read/01kbhrj2x42hhxa14jjf11c83e))

**HOW**: tell Claude how it should work on the project. For example, do you use `bun` instead of `node`? You want to include all the information it needs to actually do meaningful work on the project. How can Claude verify Claude's changes? How can it run tests, typechecks, and compilation steps? ([View Highlight](https://read.readwise.io/read/01kbhrj77xbdyd84th5gte7snb))

Frontier thinking LLMs can follow ~ 150-200 instructions with reasonable consistency. ([View Highlight](https://read.readwise.io/read/01kbhrkzp4k8bxxhsptp0m7n78))

LLMs bias towards instructions that are on the peripheries of the prompt ([View Highlight](https://read.readwise.io/read/01kbhrm7nskcs84xdx84wbc10a))

As instruction count increases, instruction-following quality decreases uniformly ([View Highlight](https://read.readwise.io/read/01kbhrmjwpgqjjay9b7vwe2ejm))

Our analysis of the Claude Code harness indicates that **Claude Code's system prompt contains ~50 individual instructions**. ([View Highlight](https://read.readwise.io/read/01kbhrmwt2h3eqyjrqt2ack2nc))

All else being equal, **an LLM will perform better on a task when its' context window is full of focused, relevant context** including examples, related files, tool calls, and tool results compared to when its context window has a lot of irrelevant context. ([View Highlight](https://read.readwise.io/read/01kbhrnk51t23b6zsxjb98x78y))

leverage the principle of **Progressive Disclosure** to ensure that claude only sees task- or project-specific instructions when it needs them. ([View Highlight](https://read.readwise.io/read/01kbhrp151ght6smrcx62xt6zv))

we recommend keeping task-specific instructions in *separate markdown files* with self-descriptive names somewhere in your project.
For example:
`agent_docs/ |- building_the_project.md |- running_tests.md |- code_conventions.md |- service_architecture.md |- database_schema.md |- service_communication_patterns.md` ([View Highlight](https://read.readwise.io/read/01kbhrpe3jheqh3pp2g377mwjf))

**Prefer pointers to copies**. Don't include code snippets in these files if possible - they will become out-of-date quickly. Instead, include `file:line` references to point Claude to the authoritative context. ([View Highlight](https://read.readwise.io/read/01kbhrpydpfw5pq6mp0jm9qcq0))

Never send an LLM to do a linter's job ([View Highlight](https://read.readwise.io/read/01kbhrqbt1ewm0yvs49syez2ep))

*always use deterministic tools whenever you can*. ([View Highlight](https://read.readwise.io/read/01kbhrqfhsx5qhv7x4x4sg274z))


1. `CLAUDE.md` is for onboarding Claude into your codebase. It should define your project's **WHY**, **WHAT**, and **HOW**.
2. **Less (instructions) is more**. While you shouldn't omit necessary instructions, you should include as few instructions as reasonably possible in the file.
3. Keep the contents of your `CLAUDE.md` **concise and universally applicable**.
4. Use **Progressive Disclosure** - don't tell Claude all the information you could possibly want it to know. Rather, tell it *how to find* important information so that it can find and use it, but only when it needs to to avoid bloating your context window or instruction count.
5. Claude is not a linter. Use linters and code formatters, and use other features like [Hooks](https://code.claude.com/docs/en/hooks) and [Slash Commands](https://code.claude.com/docs/en/slash-commands) as necessary.
6. `CLAUDE.md is the highest leverage point of the harness`

