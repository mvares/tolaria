---
aliases:
  - "How AI is Changing of Engineering Docs"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-essays|Publish Essays →]]"
Status: Evergreened
URL: "https://refactoring.fm/p/how-engineering-docs-change-with"
"👓 Status": Not started
"Created time": "2025-04-18T17:10:00.000Z"
Date: 2025-06-25
"Has Notes":
  - "[[evergreen/the-30m-docs-search-problem|The 30m docs search problem]]"
  - "[[evergreen/a-new-docs-workflow-with-ai|A new docs workflow with AI]]"
  - "[[evergreen/the-ai-docs-paradox|The AI docs paradox]]"
Tags:
  - Guest
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 1d9bdf02-815c-803f-838a-f8ebc423acd1
---

# How AI is Changing of Engineering Docs

### 📑 Materials

---

[https://getunblocked.com/blog/documentation/?utm_source=refactoring&utm_medium=email&utm_campaign=ref_documentation](https://getunblocked.com/blog/documentation/?utm_source=refactoring&utm_medium=email&utm_campaign=ref_documentation)

- Picture

### ✍️ Post

---

Here's a thought experiment: tomorrow morning, an AI wakes up with perfect knowledge of every programming language, framework, and design pattern ever created. It can read any codebase, understand any system, and generate any documentation you ask for.

What happens to all the docs we've been writing?

This isn't science fiction — we're already halfway there. AI can parse most codebases in seconds, explain complex algorithms better than most humans, and generate API docs that would take days to write manually. 

Which brings us to an uncomfortable question: if AI can understand code without docs, and can write better docs than most humans... **what's the point of documentation anymore?**

The answer, it turns out, is more complex than you'd think.

We're witnessing a fundamental rewiring of how engineering knowledge works. What we write, how we write it, who writes it, and even *why* we write it at all.

Now, if you ask me, it was *about time*. The [stats about the effectiveness developer docs](https://www.statista.com/statistics/1401435/daily-time-spent-searching-solutions-developers-globally/) have always been grim:

- 64% of developers spend over 30 minutes daily searching for information

- 26% waste more than an hour

That's *weeks* lost every year, and it has always been hard to figure out *why*:

- Some teams get there because of little to no docs, and overly relying on *tribal knowledge.*

- Others literally *drown *in docs — Confluence pages, READMEs, Slack threads — and devs can't reliably find what they need.

So the issue isn't strictly *quantity *— it’s about the whole lifecycle: from *recording* the right things, to *retrieving* them at the right time, to keeping them up to date.

This is where AI has the potential to change everything, even if we are still figuring out *how*.

Today we’ll dive deep into this transformation. We'll explore why AI makes some documentation obsolete while making other types more crucial than ever. We'll examine how teams are already adapting their workflows, and what the future of engineering knowledge looks like when AI can understand your codebase better than you do.

To help me with this, I am bringing in [Dennis Pilarinos](https://www.linkedin.com/in/dennispi/), founder of [Unblocked](https://getunblocked.com/), who I interviewed just recently [on the podcast](https://refactoring.fm/p/the-future-of-dev-tools-with-dennis). Dennis has worked on dev tools his whole career, from holding Director roles at Microsoft and Amazon, to founding Buddybuild (and selling it to Apple), to now building Unblocked. 

We touched on some of these topics during our chat, and it was so enlightening that I thought we should absolutely write a full piece together! 

So here's what we'll cover:

- 🔍 **The 30min search problem** — why traditional docs fail despite our best efforts

- 🤖 **The AI docs paradox** — how AI both needs docs and makes them obsolete

- 🔄 **A new docs workflow** — reimagining writing, reading, and maintaining docs

- 🔮 **The future of docs** — what engineering knowledge looks like in 2026 and beyond

Let's dive in!

---

*Disclaimer: I partnered with the team at Unblocked for this piece, as they're building fascinating solutions in this space. However, this article reflects my unbiased views on documentation practices and the broader transformation happening in engineering knowledge management.*

---

### 🔍 The 30min search problem

Let's start with a familiar scene:

Sarah, a senior engineer, needs to understand how the payment processing service handles refunds. Twenty minutes later, she's opened various pages on Confluence (”*is this up to date?” *she wonders), searched on Slack, checked Github READMEs, and scanned PR comments (just joking — who has the time to do that?!)

Finally, she DMs Tom: "Hey, quick question about refunds..."

Tom is a good guy: he answers within a few mins, points her to the *one* good page in the docs (”this is up to date, scrap the rest”) and gives her additional context that was not written anywhere.

Versions of this happen everyday in *all* the teams I know. Sometimes it’s better, sometimes it’s worse, but I have never found a team that *solved* documentation.

But why? In my experience, docs have three main failure modes:

1. **They don't exist** — writing docs is nobody's job and everybody's job. The people who know the most have the least time, and writing stuff is *hard*. Trust me I am a writer.

1. **They can't be trusted** — once developers get burned by outdated instructions, they develop a simple heuristic: when in doubt, ask someone.

1. **They can't be found** — there is an overwhelming variety of knowledge that potentially deserves to be *recorded* (ADRs, runbooks, design docs, meeting notes). Good luck finding a universal way to organize it.

Now, even when you somewhat do well on these, the final nail in the coffin is *the* *colleague test*: **is finding and reading docs faster *****and***** easier than asking a colleague?**

Quick math: 

- **Reading docs** — 20 minutes of focused effort for finding the right stuff + extracting the exact bits that you need.

- **Slack to Tom** — 3 minutes, direct answer to your question, zero cognitive load.

Tom is just too good.

This creates a devastating feedback loop: asking co-workers is easier than using docs → docs get ignored → docs become outdated → trust erodes even more → people stop writing docs.

In the long run, this creates obvious problems:

- Tom spends a lot of time answering the same questions over and over, taking it away from productive work. And the paradox is: the better an engineer you are, the more you’ll get questions from others. So it’s your top performers who suffer the most.

- Tom eventually leaves the company. During his notice, he hastily writes some notes about the systems he knows best, which nobody will truly understand.

- Complex systems for which tribal knowledge has left the company eventually turn into technical debt: they will either swamp productivity or need to be rewritten.

In theory, we have all the pieces of the puzzle to do things better. Over the years we figured out many [smart formats](https://adr.github.io/), created [good templates](https://refactoring.fm/p/design-docs?utm_source=publication-search), and [frameworks for better organization](https://fortelabs.com/blog/para/).

Still, getting docs right is an uphill battle: it takes time, effort, and as soon as you lose your grip a bit, things go downhill incredibly fast. It’s a war many teams are losing every day, and not because they are not trying.

So it is fair to say we need rescue, and the bet is that AI is coming for it 👇

---

### 🤖 The AI docs paradox

Two weeks ago we discussed [how to design AI-first APIs](https://refactoring.fm/p/how-to-design-apis-for-an-ai-world), and we argued that documentation is going to become *more important than ever*. Shamelessly quoting myself:

> *Your documentation is no longer just developer guidance — it's part of your operational system. Unlike humans who read docs once and internalize patterns, AI processes documentation with nearly every decision.*

So is AI going to make docs *less* or *more *important*? *To me, it depends on *what* docs.

Let’s bucket docs in three macro categories:

- **The “Why” docs** — they record *why* we built things the way we did. What are the goals, the constraints, the assumptions, and the principles we build on top of.

- **The “What” docs **— they record *what *has been built. What features, what system design, what workflows.

- **The “How” docs **— they record *how* stuff has been built, and how it works. It’s the implementation details, the runbooks, the code comments, and so on.

AI is especially useful on* *the *how*. We can argue on the *quality* of AI-generated code, but it is obvious to anyone who has used Cursor for a while that AI documents code better than humans (if asked to do so!).

The *Why* is and will stay a domain of humans for a long time. It’s where you translate business context into technical decisions, and it’s *vital* to write this down. It’s also the part that, above all, no intelligent being (artificial or not) can figure out by simply looking at a codebase: it’s additional context that is not part of the software itself.

The *What *is trickier and I guess it’s the real frontier where humans and AI are going to collaborate. Starting from good *whys*, AI can draft good *whats* in terms of design docs, system architectures, and even roadmaps.

![image](../assets/218bdf02815c80a1.png)

This pyramid structure reveals why AI is both making docs less and more important simultaneously:

- **Less important** — the massive bottom layer of "how" documentation — implementation details, code comments, API references — can increasingly be generated on-demand.

- **More important** — the slim top layer of "why" documentation — business context, decisions, constraints — becomes *critical* because it's what AI needs to generate everything else.

This is somewhat counterintuitive because many teams have this exactly backwards. We spend 80% of our effort on the *how*, which is more extensive, more volatile, but also easier to generate for AI, and 20% on the *why*, which only *we *can provide instead.

Time to flip that ratio 👇

---

### 🔄 A New Docs Workflow

If we accept that AI changes what's worth documenting, we need to completely rethink *how* we create, maintain, and consume documentation.

Here’s what a new workflow may look like:

#### 1) Provide business context upfront

There are a lot of tasks where, as humans, we *still* perform better than AI only because we have *more context* into some specific business nuances. These would be tedious and repetitive to include in the prompt of individual tasks, so we should provide them *upfront*.

Hayden Miyamoto is pioneering this with the [Master Prompt](https://www.youtube.com/watch?v=_K_F_icxtrI) method, through which he maintains a loooong one-pager where AI can learn *everything* they need about the company, team, goals, and all the kind of shared knowledge that goes beyond specific tasks.

#### **2) Focus on capturing decisions**

The most valuable human docs are not descriptions anymore — are *decisions*. 

[ADRs](https://adr.github.io/) (Architecture Decision Records) and design docs work like append-only logs:

- You don't "update" an ADR when things change — you write a *new* decision that supersedes the old one.

- At any time, AI can trace this evolution and understand both current state and history.

Example: Instead of maintaining an "Authentication System" doc that goes stale, you have:

- ADR-001: "Why we chose JWT tokens" (2021)

- ADR-017: "Moving to session-based auth for shared devices" (2023)

- ADR-024: "Adding biometric auth for mobile" (2024)

#### 3) Keep docs simple and close to the action

For AI to be the most effective it can be, docs need to be simple and co-located.

Andrej Karpathy has been hammering on this for a long time now:

[Embed](https://x.com/karpathy/status/1899876370492383450)

This means Markdown wins over complex formats, and docs in repos are even more valuable than before: they get the double benefit of 1) being in the same context space, and 2) being easy to update together with code.

#### **4) Automate the How**

Trust the AI to own the implementation layer: code comments, API docs built from code + context, runbooks created from actual system behavior.

Make AI update these at every code commit, and you’ll get an awesome, disciplined doc history like very few human teams are able to maintain.

#### **5) Connect AI to all the tools**

No matter how well you capture it, knowledge will *always* be scattered across multiple tools:

- Tickets live in project management tool, like Linear or Jira.

- Ephemeral chats live on Slack or Teams.

- Code and system docs live in repos.

- Goals and principles may live in separate wikis, like Notion or Confluence.

Each tool has its own strengths, and we are always going to use many at the same time, but this doesn’t mean we can’t use AI as a horizontal layer that helps navigate through it all.

Small plug: this is where Unblocked shines. It connects to all of your tools so it answers your questions by fetching info from everywhere — Notion, Github, GDocs, Linear, Slack, you name it.

It’s one of the tools I recommend the most these days: 100% plug and play, doesn’t need you to change anything in your workflows, and it’s immediately valuable. You can learn more below 👇

[Learn more about unblocked](https://getunblocked.com/)

---

### 🔮 The Future of Docs

So, I am a believer in designing things starting from an ideal goal, or a *final state* if you will.

For documentation, or better, engineering knowledge, my ideal state is the following: 

Let’s say we are debugging a production issue. Instead of frantically searching everywhere, we ask our AI assistant: "Why are refunds failing for European customers?"

Within seconds, the system fetches and goes through:

- The original PRD about SEPA compliance (from Notion)

- The ADR about payment processing for EU customers (from GitHub)

- A Slack thread where the team discussed timeout issues (from 6 months ago)

- Recent PR comments about a webhook format change (from last week)

- The latest docs of our payment library (e.g. fetched via the [Context7](https://context7.com/) MCP)

- Current error patterns from our monitoring system

Then, it replies:

> *The issue started when the payment provider deprecated their v2 webhook format yesterday. This breaks our SEPA flow because of this and that. Here's a fix that maintains compliance while handling v3's longer processing times...*

This might feel like science fiction, but it is not. My feeling is that we largely don’t need *smarter models* to enable this kind of analysis: we just need to provide better context, and we can work on that *right now*.

We need to become more intentional about what we record and how, shifting from the idea that docs are something we *read*, to the idea that they are something that will be analyzed by software, like logs.

Traditional documentation is like a library — you need to know what book to look for, where to find it, and how to extract what you need. Future documentation is like having a super *Tom*, a senior engineer who's read everything, remembers everything, and can explain exactly what you need to know right now.

It’s an exciting future, and personally I can’t wait to build it.

---

### 📌 Bottom line

And that's it for today! Here are the key insights:

- 📚 **Traditional documentation is a losing battle** — the complexity of modern software has outpaced our ability to manually maintain comprehensive docs

- 🤖 **AI changes the game, but not how you'd expect** — it's phenomenal at explaining "what" but needs human context for "why"

- 📐 **The Why/What/How pyramid** — focus human effort on the valuable top layers (decisions, context) and let AI handle the volatile bottom layer

- 💬 **Documentation becomes conversation** — we're moving from static wikis to dynamic AI assistants that understand your entire engineering context

- 🏃 **The future is already here** — teams using AI-native knowledge systems will dramatically outpace those stuck in traditional documentation

See you next week!

Sincerely
Luca
