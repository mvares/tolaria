---
aliases:
  - "How to Write Design Docs"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-essays|Publish Essays →]]"
Status: Evergreened
URL: "https://refactoring.fm/p/design-docs"
"👓 Status": Not started
"Date HH": 2025-11-06
"URL 2": "https://twitter.com/lucaronin/status/1541338078052220934"
"Created time": "2024-04-18T14:53:00.000Z"
Date: 2022-06-23
"Has Notes":
  - "[[evergreen/share-drafts-of-docs-asap|Share drafts of docs asap]]"
  - "[[evergreen/design-docs-are-made-of-3-main-sections|Design docs are made of 3 main sections]]"
  - "[[evergreen/design-docs-are-the-most-important-tech-docs|Design docs are the most important tech docs]]"
  - "[[evergreen/i-dont-always-need-a-design-doc|I don’t always need a design doc]]"
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 68be21cf-4344-48cf-932f-2b93dff1324f
---

# How to Write Design Docs

### ❓ Six Questions

### 📑 Materials

---

[https://www.industrialempathy.com/posts/design-docs-at-google/](https://www.industrialempathy.com/posts/design-docs-at-google/)

[Untitled](https://www.notion.so/2b6399cf6bdc4a9e93dda1b6c171147b) 

<details><summary>**Zach Wolfe** — focus on the what / why / how, decision documentation, ask feedback early</summary></details>

<details><summary>**Andrew Twyman** — most design docs are **mini** (implementation + code-review is often enough). Meant to **drive a process** and reach a solution. **Different kinds**** **of docs. **Record of a decision**, not permanent description of what’s live.</summary></details>

- [Example tech spec](https://docs.google.com/document/d/1m9VGy8y3b64DBIfcp56TsMKhr8WpX47CWGyR3YQep-4/edit?mode=html)

### ✍️ Post

---

Writing docs belongs to that category of dev tasks that everybody knows they should do, but nobody wants to do anyway.

It’s an exclusive club with other illustrious members, such as writing tests, estimating tasks, or updating JIRA.

The natural restraint towards these tasks is often dismissed as *laziness. *But **laziness carries meaning**.

When devs don’t want to do something, what they are really saying is:

- **It’s a hassle** — high cost

- **It’s not worth it** — low value

People have a small ROI calculator in their head, which says the ROI is negative.

This version of laziness is useful and has driven important conversations in the past:

- Tests — write less unit tests in favour of more integration tests. From [testing pyramid](https://martinfowler.com/articles/practical-test-pyramid.html) to [testing trophy](https://kentcdodds.com/blog/the-testing-trophy-and-testing-classifications).

- Estimates — spend the minimal amount of effort on [estimates](https://refactoring.fm/p/how-to-estimate-projects) that makes them useful for prioritization. From man-days to story points to t-shirt sizes.

The goal of this article is to have the same conversation on tech docs to make them 1) *less of a hassle*, and 2) *more worthwhile.*

This is what we are going to cover:

- 📖 **Types of tech docs** — the three main ones. 

- ✏️ **What are design docs** — and why you should write them.

- 📋 **Structure of a design doc** — my own template based on three areas: *essentials*, *disclaimers*, and *reminders*.

- ❓ **FAQs **— maintaining docs, involving stakeholders, and deciding when docs are not needed.

- 📚 **Resources** **and case studies** — how design docs are managed at Google, Dropbox, Amazon, Plaid, and more.

The article also includes ideas and insights from members of the [Refactoring Community](https://refactoring.substack.com/p/community), like [Andrew Twyman](https://www.linkedin.com/in/andrewtwyman/), former Staff Engineer at Dropbox, and [Zach Wolfe](https://zdwolfe.medium.com/), Senior SDE at Amazon.

Let’s dive in 👇

### 📖 Types of tech docs

This is the first source of confusion. Many times you hear people asking “*do we have the docs?*” — but what docs? 

It is useful to separate three main types:

1. **Functional spec** — the product requirements. To communicate what should be achieved from the user perspective. It includes UI/UX specs.

1. **Design doc** — the tech design and implementation strategy. To record decisions, communicate trade-offs and converge on a solution.

1. **Tech spec** — API specs, database schema, and the overall description of what’s live.

In my experience, everybody understands the difference between the product and tech stuff — that is, between the first type and the other two. It is easy because those are usually created by different people: PMs and designers on one side, engineers on the other side.

On the contrary, the difference between *design docs* and *tech specs* is tricky. 

In my opinion, 80% of the times what you really need is a design doc rather than a tech spec. That is, **you need to record your decisions rather than describe what’s live**.

To understand this better, let’s cover what design docs are and why you should write them.

### ✏️ What are design docs

A design doc illustrates the tech design and implementation strategy for a given initiative. 

It is meant to be created *before* you start writing code, and to be shared with other stakeholders to converge on the solution.

You write it for several reasons:

1. 💭 **Help your reasoning** — writing is thinking. Going through the process of writing a formal document helps solidify your reasoning and come up with a better solution.

1. 🤝 **Create consensus **— align with stakeholders about what should be built, make sure important technical decisions are participated, and people feel invested in them. 

1. 🔨 **Find the best technical solution **— improve the original design through the contribution of others. Like a code review, but for the design.

1. 📓 **Record the decision **— for posterity and documentation. That includes the trade-offs you evaluated, alternative solutions you discarded, open questions, and more.

In that respect, a design doc is useful throughout the whole lifecycle of a project.

- *Before release* — it drives the process that makes people converge on a good solution.

- *After release* — it acts as decision record, that is often more useful than pure tech specs.

So, what goes into a design doc? 👇

![image](../assets/0e19d4f318724652.png)

### 📋 Structure of a design doc

You should have a template with all the sections you may want to include in the design doc.

You won’t need all sections all the time. Consider them as a checklist: you go through it and fill what’s needed.

In my head, sections belong to three main categories:

1. 🎯 **Essentials **— things you should always include, like goals and tech design. 

1. 📝 **Disclaimers **— things you include to create alignment and guide the conversation.

1. ⏰ **Reminders **— things that “*let’s make sure we don’t forget them*”. And boy they are many.

Let’s see them 👇

#### 🎯 Essentials

You would probably remember to write these even without the template. On the flip side, you would probably remember *only* these.

- **Header **— include the basics: project name, date, owner, other contributors. Even though design docs are a collaborative effort, it’s important that each doc has a single owner that is responsible for it.

- **Context **— links to other useful docs: product specs, UI/UX design, related design docs.

- **Goals** — what this design should achieve. It includes functional goals but also non-functional ones like performance goals, scalability, and any KPI that should be met.

- **Approach / Design **— How you are going to implement the thing. Based on the size and the scope of the initiative, it may include diagrams, database schemas, and anything that is useful to explain your approach. Focus on materials that drive the conversation, rather than *specs*. The goal of the design doc is primarily to converge on a good solution.

#### 📝 Disclaimers

People will read the *essentials* and come up with questions and ideas. That’s the whole point of the design doc.

This can be 10x more productive if you are able to drive the conversation by anticipating such points. The best way to do this is to reason through [*inversion*](https://refactoring.fm/p/the-power-of-inversion-)* *and cover not only what you want to build, but also what you *don’t*, and why.

So here is what you may include:

- **Anti-goals** — all the things you are *not *going to achieve in this iteration. Like for goals, it should include both functional elements and not functional ones. This creates alignment and prevents the classic objections “*I thought we would have this*” after release. 

- **Alternatives considered **— if you are discarding alternative options, list them and explain your thought process. Anticipate questions that will come from people who are checking your approach.

- **Open questions **— just like for alternatives, be transparent about points that are still open, and put them up front for discussion. Including open questions gives people an easy place where to contribute, and helps you drive the talk in the directions you care the most.

#### ⏰ Reminders

This is the “*let’s make sure we don’t forget about it*” space. Not all of sections will be relevant all the time, but it’s important to include them as placeholders. Again, checklist mentality.

- **Security / Privacy **— are there security or privacy concerns about this project? Write down how you plan to handle them.

- **Observability** — details about how you are going to instrument this system, with logging, alerts, and more.

- **Test plan** — how are you going to test this? Includes anything specific that needs to be carried out, like A/B testing, QA, and more.

- **Rollout** — details about the release process. It might include plans for database migrations, feature flags, and similar activities. Partial overlap with the test plan.

- **Rollback** — what will you do if things go wrong? Can you simply rollback the code? If not, write down the plan.

### ❓ FAQs

Docs are a popular topic and over time I received plenty of questions about them via email. Here are the most popular ones 👇

#### **Q: Do I always need a design doc?**

I know what you are thinking — “*man this template is so long, there is no way I am going to write all these things every time*”. 

And you are right! 

In a healthy product team, most changes are small and there is no need to record them this way. For a small change, the minimum viable design doc is the PR.

Quoting Andrew Twyman here 👇

> *I think there are two goals of a design doc: Solidify a solution in the author's mind, and get feedback to iterate and eventually align on it.

For small enough projects an implementation and code-review meet that purpose. A doc can get involved as soon as the project is big enough code to become unwieldy. 

A design docs is primarily meant to drive a process and reach a solution. It should be only as big as it has to be to describe a solution and serve the purpose.*

If you don’t need to converge with others on a solution, and decisions are small enough and not worthy of being recorded, you can avoid the design doc altogether.

Also, again, the template is a checklist and you won’t be filling all the sections all the time.

#### **Q: How do I maintain and update design docs all the time?**

Mostly, you don’t.

Design docs are not specs — they should record the decisions you made, rather than describe what’s live. When you make a new, significant change, you create a new design doc.

Quoting Zach Wolfe, design docs are like commits:

> *I view design docs as ****immutable commits**** that if you stacked on top of one another you’d mostly get the full living view.*

Conversely, design docs should be updated as long as the conversation is ongoing. Andrew on this:

> *I'd say update the doc as long as the process it's driving is active. That's generally design but not full implementation/rollout. 

So it should be updated to incorporate feedback which changes the design, but not necessarily to incorporate the final implementation. *

#### **Q: How do I work with others on a design doc?**

Design docs are collaborative pieces by nature, because they are meant to create alignment.

Here is what I learned over time about collaboration:

**1) Share it as soon as possible **— don’t wait to have a polished version. Create a full rough draft and share it. Waiting too much will make you attached to the doc and less receptive of feedback. Also, early feedback is genuinely easier to implement.

**2) Cycle the doc multiple times through stakeholders** — feedback is not a one-time, top to bottom thing, but rather a [hot potato process](https://danmall.me/articles/hot-potato-process/).

**3) Decide who needs to be involved** **and how **— people can be involved in a design doc under different roles. This is basically a [RACI Chain](https://en.wikipedia.org/wiki/Responsibility_assignment_matrix) 👇

- *Responsible* — the owner of the doc. It should be a single person.

- *Accountable* — people who can *veto *the decisions made in the doc. E.g. the tech lead for the project (if they are not the owner).

- *Consulted* — domain experts who are contributors of the doc. E.g. other devs; the PM.

- *Informed* — people who just need to be aware of the decisions been made, without actually contributing. E.g. stakeholders from other teams, customer support.

### 📚 Resources

- 📑 [**Design Docs at Google**](https://www.industrialempathy.com/posts/design-docs-at-google/)** **—

- 📑 [**How to Write a Good Software Design Doc**](https://medium.com/free-code-camp/how-to-write-a-good-software-design-document-66fcf019569c) — 

- 📑 [**Painless Functional Specifications**](https://www.joelonsoftware.com/2000/10/02/painless-functional-specifications-part-1-why-bother/) —
