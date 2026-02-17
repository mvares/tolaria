---
aliases:
  - "How to Write Documentation"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-essays|Publish Essays →]]"
Status: Evergreened
URL: "https://refactoring.fm/p/how-to-write-documentation"
"👓 Status": Not started
"Date HH": 2024-10-10
"Created time": "2024-04-18T14:53:00.000Z"
Date: 2023-06-08
"Has Notes":
  - "[[evergreen/cheatsheet-for-writing-engineering-docs|Cheatsheet for writing engineering docs]]"
  - "[[evergreen/organize-docs-by-projects-and-areas|Organize docs by projects and areas]]"
  - "[[evergreen/keep-tech-docs-close-to-code|Keep tech docs close to code]]"
  - "[[evergreen/write-docs-during-the-whole-lifecycle|Write docs during the whole lifecycle]]"
Tags:
  - Guide
  - Software
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 777b009e-19a7-4eb6-9678-f9d7c6aa4a44
---

# How to Write Documentation

### 📑 Materials

---

- *how do you write docs in your company?*

- [Untitled](https://www.notion.so/c573948e94f649b0a5b4b4a8aab08144)

- [Untitled](https://www.notion.so/869230e430da486083207bb885043cf5)

- [Untitled](https://www.notion.so/809549ecc10443a3bcde2c0e7c0303d4)

- [Untitled](https://www.notion.so/726ec617b3ce4bda959ecd6abafd5bc2)

- [Untitled](https://www.notion.so/fea67272f0b244a58e3d7fe90af9ec54)

### 💡 Ideas

---

Hey! Welcome to a new 📖 **Refactoring Guide**!

Guides are **super articles** that act as *primers* about one topic: they are longer, they draw from previous pieces, add new content, references, and ideas from the community.** **

You can expect ~1 new guide per month.

The first of such primers has been about [engineering metrics](https://refactoring.fm/p/how-to-get-started-with-engineering), and has instantly become the most popular article of the year.

---

Organizing knowledge is one of my obsessions.

Today, this is a core part of my work as a *writer*, but even in my previous life, as a CTO, I invested a lot of energy into processes that enabled good, sustainable docs.

I have written many articles about docs — but they mostly cover specific kinds (e.g. [design docs](https://refactoring.fm/p/design-docs), or [meeting docs](https://refactoring.fm/p/how-to-remove-meetings)), so I thought this was a perfect topic for the second of our *guides.*

In the past weeks I talked with a ton of tech leaders, read plenty of case studies, and reflected on my own experience about tech documentation. So here is what we will cover:

- 🌟 **Benefits of docs** — the three main reasons. This is non-trivial and crucial to understand.

- ❌ **Why docs fail **— why *all* teams struggle with docs and what to do about it.

- 🏆 **How to write *****successful *****docs **— tips to write useful docs and make people stick with them. 

- 🏷️ **Types of docs **— let’s cover the main kinds and how to write them.

- 📌 **Docs cheatsheet **— let’s summarize everything into a few easy steps.

- 🔨 **Tools** — what to use to write modern docs.

- 📚 **Resources **— more readings, books, and case studies.

Let’s dive in!

### 🌟 Benefits of docs 

To every person I surveyed about how they write docs, I always asked at the end: *are you happy about your docs?* 100% of them said *no*. Literally 100%!

I believe this is not (only) because people struggle at writing docs — it’s that they are generally confused about what those are useful for and how to use them. 

Writing docs — of whatever kind — provides four main benefits:

1. 💭 **Help your reasoning** — writing is thinking. Going through the process of writing a formal document helps solidify your reasoning and come up with a better solution.

1. ⚡ **Improve output **— you can support your writing with previously created templates, checklists, and examples. These make the work easier and lead to better results 

1. 💬 **Improve communication **— it is easier to have good conversations about complex topics when these are backed by writing. You get more thorough reasoning and easier convergence. 

1. 📔 **Future reference **— docs naturally record decisions and can be used for posterity.

These benefits happen throughout the whole life of a project, from inception to release to future maintenance.

Now, I have found that most teams ***over-index***** on the future reference*** *use case, while neglecting the first two. But writing docs only *after* the fact is like retrofitting unit tests to production code: not completely useless, but you miss out on a lot of value.

Also, writing docs at the end is genuinely *harder* than doing it gradually while the work is in progress. Artifacts like meeting notes and design docs are not only useful *per se — *they naturally* *turn into long-term docs, later, with very little effort.

Minimizing such effort is crucial to make people keep up with docs. In fact, people are only going to write docs is the **value from their use is perceived as *****superior***** to the writing effort**.

Based on how this equation turns out, you end up either in a vicious or a virtuous cycle 👇

![image](../assets/375c01a8283642ee.png)

#### ❌ V**icious docs cycle**

1. People write less docs because no one reads them

1. Docs become partial and outdated

1. People don't trust and read docs anymore

1. People write less and less docs

#### ✅ V**irtuous docs cycle**

1. People write more docs because they feel they are valuable

1. Knowledge grows larger, more insights are discovered, decisions are taken faster and better

1. People read more docs instead of having meetings

1. People write more and more docs

---

### 🏆 How to write *successful *docs

So, if we trust the equation, we have two ways of avoiding the *vicious cycle* and encouraging the *virtuous* one: 1) maximize the use** **of docs, and 2) minimize effort of writing them.

Over time, I have found (and written) a lot of advice about this. Here are the four best ideas you should try:

#### 1) 🔄 Attach docs to processes

I have found that the easiest way to be consistent at writing documents is to attach them to existing processes. This eventually turns writing into a habit so that people do it naturally — like brushing their teeth.

E.g. you can enforce agendas for meetings, or design docs for new initiatives. For larger projects, you can use checklists that detail everything that needs to be done, including writing down stuff.

You can also use the onboarding process as an opportunity to update old docs 👇

> A good practice we established, especially for higher-level technical documentation, is to assign every new hire the task of updating and filling in any gaps as part of the onboarding process.

[Nicola Ballotta](https://hybridhacker.email/) — Director of Cloud at Namecheap

Also, create templates for any type of document that needs to be written. This is a low hanging fruit that 1) reduces the friction of writing, and 2) improves the overall quality.

#### 2) 💻 Keep docs close to code

For technical docs, I have found that the closer they are to the code, the higher the chance that they will stay relevant and up to date.

Ideally, you want tech docs to be updated in PRs — just like code.

I am a fan of commenting code (more on that later) because comments are extremely easy to update. Everything happens in the same PR, so it is also easy for others to verify that you actually did it. Also, code comments can turn automatically into docs with various tools.

These benefits also apply to READMEs and repo docs. Everything that lives in your repo is generally easy to update.

> *Tech docs, i.e. docs related to a specific project live in the github repo and undergo the same PR/CR process that code does. Format is markdown.*

— Umberto Nicoletti, Head of R&D at Proemion

#### 3) 🍱 Organize by projects and areas

I am a fan of the [PARA method](https://fortelabs.co/blog/para/) by Tiago Forte for organizing information, and I have brought this to how I organize docs in my teams as well.

I believe, at a high level, you can separate between two major types of notes:

- ↕️ **Project notes **— stuff you need to deliver a project. They may span multiple areas for cross-functional teams. E.g. product requirements, design docs, roll-out plan. A project is an initiative that needs to be delivered and has a beginning and an end.

- ↔️ **Area notes **— long-lived documentation about a specific *area*. E.g. engineering onboarding, database schemas, company org chart. An area is anything for which you need to maintain a *standard*, and that stays relevant for indefinite time (as opposed to projects that have an end).

Most action happens in project notes, while area notes are more useful for future reference. This separation, though, is not static: after a project is delivered, you may archive most of its material, and move some of it into the respective *areas*, where it will stay useful for longer. 

For example, you may move the database migration specs into the general database docs, or the PRD into the *product* area.

If your system supports it, you may *tag *content rather than actually moving it. E.g. I am a fan of using Notion for company docs because it allows you to be flexible with this and define areas and projects through *relations* and *tags*, rather than *folders*. But you can implement this in any system, like Confluence, or Google Docs.

You can find more ideas about organizing company docs in this previous Refactoring article 👇

[https://refactoring.fm/p/company-docs](https://refactoring.fm/p/company-docs)

#### 4) 📦 Archive old stuff

One of the main reasons why people don’t read docs (and, eventually, stop writing them) is that, in your workspace, good docs are mixed with old, outdated ones.

In some cases, **outdated docs** should simply be updated, but in many others, those are simply not useful anymore.

For these cases, you should have a safe place where you can put all this stuff, like an *archive* folder. Do not delete anything — just move it away to declutter your space and keep signal-to-noise high.

### 🏷️ Types of docs

We discussed how to organize docs and where to put them — but *what* docs should you actually write? Let’s see the main categories:

#### 📱 Product requirement docs (PRDs)

PRDs are the main product docs for new features/products. They outline the *why* and *what *should be built, while letting designers and engineers explore the *how*.

About what goes into a PRD, I like to think about three main areas:

1. 🎯 **Goals **— what should be achieved from a business perspectives. KPIs and targets should go here.

1. 🤹 **Features **— high level view of what users should be able to do. Might include some guidance about UX.

1. 📏 **Scope** — assumptions, anti-goals, constraints, and anything non trivial that is useful to clarify to create alignment.

Each of these items can be more or less detailed based on whether we are talking of a small feature or a large product area.

Also, PRDs usually start high-level based on the PM input, and get richer and more detailed with the input of designers and engineers.

You can find various specific formats of PRDs. A notable one is PRFAQs, which mimics a future press release. It was popularized by Amazon and you can find a template [here](https://www.linkedin.com/pulse/working-backwards-press-release-template-example-ian-mcallister/).

Lenny Rachitsky also published a great list of PRD templates [here](https://www.lennysnewsletter.com/p/my-favorite-templates-issue-37?s=r).

#### 📐 Design Docs

A design doc illustrates the tech design and implementation strategy for a given initiative. It is meant to be created *before* you start writing code, and to be shared with other stakeholders to converge on the solution.

Design docs are useful throughout the whole lifecycle of a project:

- *Before release* — they drive the process that makes people converge on a good solution.

- *After release* — they act as a decision record, which is often more useful than pure tech specs.

In my experience, design docs are the MVP of all tech docs, where in this case "MV" stands *both* for Minimum Viable, and Most Valuable.

![image](../assets/7ee8709e96564510.webp)

I have written a full article about design docs, which includes my personal template, and answers to many FAQs. You can find it below 👇

[https://refactoring.fm/p/design-docs](https://refactoring.fm/p/design-docs)

An alternative to design docs — or a particular implementation of them — is Architecture Decision Records (ADR), which, as the name suggests, are meant to capture important architecture decisions together with context, consequences, and more.

You can find more ADR info and templates in this [useful repo](https://github.com/joelparkerhenderson/architecture-decision-record).

#### 📋 Tech specs

Tech specs are different from design docs as they act as a description of what’s live. They may include database schemas, API specs, or system diagrams.

Even if they are separate from design docs, they mostly *stem *from these. In fact, after a project has been delivered, you may move parts of the design doc from the *project* space to *areas *where these are more useful, turning them into specs.

A good workflow may look like this:

1. A change is described in a design doc

1. Design doc is finalized

1. Project is delivered

1. Design doc stays immutable, as a snapshot, but parts that describe specs are moved (copied) to the respective areas.

#### 💬 Code comments

Commenting code is a somewhat controversial practice, as many developers believe that *good code documents itself*.

I have found, instead, that top performing teams are consistently good at commenting code, by focusing on the right amount of comments that provide the most value to the codebase.

Here is my take about the most common types of comments:

- ✅ **Comments at the top of the file/class** — a few lines to describe the file’s primary goal can go a long way to help maintainers. It also helps to avoid scope creep over time and to keep the file true to its original goal.

- ✅ **Comments on complex functions** — most functions should be simple enough to be understandable *as-it-is*, but there are algorithms and processes that cannot be so, no matter how well you write them. In these cases, it helps to include a description of the inputs, the logic, and the outputs of the function.

- ❌ **In-line comments** — while there is value in explaining the workings of a complex function, the need to comment single lines of code is most often a code smell. If people understand what the function does but not some of its lines, there is probably something you can rework, rather than commenting the lines themselves.

Code comments are also easier to keep up to date with respect to docs that live elsewhere, as you may update them in place whenever you are making changes to the code itself.

Likewise, it is easy to spot in PRs whenever somebody is changing the code without updating the comments, and report it.

#### 🌟 Principles, conventions, best practices

If design docs are about *recording* decisions, principles provide a blueprint for *how* such decisions should be made.

Without principles, you might meet goals in a way that doesn't reflect your culture. Engineers might deliver features without peer review, managers might meet deadlines by making people overwork, or teams might cut corners on security and accessibility.

So, principles are a set of **shared beliefs** that create alignment over how you do things in your company. They are, simultaneously:

- 👌 A definition of what **good** looks like.

- 🗣️ A **shared language** to be used in daily work.

Healthy *trust* inside your team comes from the alignment around *how* things should be done, plus giving people the *autonomy *to go for them.

![image](../assets/1fa495645e754571.webp)

I have written a full article about how to create good engineering principles. You can check it out below 👇

[https://refactoring.fm/p/principles](https://refactoring.fm/p/principles)

### 📌 Docs cheatsheet

So, here is a recap of what we covered:

#### What docs you should write

Focusing on tech docs, here is what you need, from the highest to lowest level 👇

1. 🌟 **Principles **— to describe how decisions should be made

1. 📐 **Design Docs **— to describe *how *things are built, and record tech decisions

1. 📋 **Specs **— to describe what’s live, taking it from PRDs and DDs

1. 💬 **Code comments **— to help maintainers and keep track of small debt. In most languages you also have ways to *auto-generate* specs from comments. 

![image](../assets/28d9adc890b648a2.png)

#### How you should write them

- **Attach to processes **— review principles on every performance review, create a design doc for every project, write comments whenever you write code. Turn writing docs into a recurring habit, and support those habits with templates and checklists to make them easier.

- **Organize into projects and areas **— separate working docs for deliverables from long-term materials. Eventually turn the former into the latter.

- **Archive old stuff **— keep your workspace decluttered by hiding what is not useful anymore.

### 🔨 Tools

Here are the 5 best tools that I know for creating modern documentation:

1. [**Notion**](https://notion.so/) — the most popular modern tool to create knowledge bases, workflows, and organize work and life in general. It is hard to even define what Notion does, as it replaces so many tools. It is my favourite and has a great ecosystem around it.

1. [**Coda**](https://coda.io/) — close to Notion but slightly more *techy.* It also boasts integrations with popular tools like Github, Gmail, Intercom, and more options to build workflows and internal tools. A fantastic all-round tool.

1. [**Slite**](https://slite.com/) — while Notion and Coda are as much about knowledge as they are about workflows, Slite is more focused on knowledge. It provides a beautiful canvas to create and organize written content, and plenty of collaboration features.

1. [**Slab**](https://slab.com/) — closer to Slite than to Notion or Coda, it also includes deep integrations with Dropbox, Google Drive, Slack, to surface content from all of your sources. It is an interesting take and a good option for companies who have already invested in other doc tools.

1. [**Confluence**](https://www.atlassian.com/software/confluence) — this list wouldn't be complete without the flagship Atlassian product. If you are into JIRA and the Atlassian ecosystem, Confluence is a solid choice that ties in with the rest of your workflow.

### 📚 Resources

- 📑 [**The PARA Method**](https://fortelabs.co/blog/para/) — by [Tiago Forte](https://twitter.com/fortelabs). It is the best framework I know for organizing digital information. I use it both for life and work.

- 📑 [**How Notion Uses Notion**](https://www.notion.so/blog/how-notion-uses-notion) — even if you are not into Notion, this is a great read into how a 100+ people company organizes their knowledge. It is rare to find such in-depth case studies, and this one is really good. Also, most advice is general and applicable to any tool.

- 📑 [**GitLab Handbook**](https://about.gitlab.com/handbook/) — this handbook is the central repository for how GitLab is run. GitLab is 100% remote and global, and people literally work and coordinate through the handbook. It is more than 2000+ pages and includes vast documentation about [how the handbook itself is managed](https://about.gitlab.com/handbook/about/). 

- 📑 [**Slab Library**](https://slab.com/library/) — tons of examples of internal documentation from successful companies like Coinbase, Basecamp, Netflix and more. Check out Trello's remote policy, how Netflix runs code reviews, or Salesforce's meeting agenda template. It's a great resource.

- 📑 [**Painless Functional Specifications**](https://www.joelonsoftware.com/2000/10/02/painless-functional-specifications-part-1-why-bother/) — legendary blog post (first of two parts) by Joel Spolsky about specs: why and how you should write them. Funny and very insightful.

- 📑 [**How to Write a Good Software Design Doc**](https://medium.com/free-code-camp/how-to-write-a-good-software-design-document-66fcf019569c) — Angela Zhang, EM at Plaid, wrote this comprehensive piece that covers the why, the what, and the how around design docs.
