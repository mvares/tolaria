---
aliases:
  - "Engineering Handbook (Mastermind)"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-essays|Publish Essays →]]"
Status: Evergreened
URL: "https://refactoring.fm/p/how-to-create-an-engineering-handbook"
"👓 Status": Not started
"Date HH": 2025-09-04
"Created time": "2024-09-18T08:07:00.000Z"
Date: 2024-10-30
"Has Notes":
  - "[[evergreen/sections-of-an-engineering-handbook|Sections of an Engineering Handbook]]"
  - "[[evergreen/how-to-create-maintain-handbooks|How to create & maintain handbooks]]"
  - "[[evergreen/handbook-first-journey|Handbook-first journey]]"
Tags:
  - Essay
  - Mgmt
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: b74ab2b5-3803-4b02-8566-de7f0b8cff0d
---

# Engineering Handbook (Mastermind)

### 📑 Materials

---

- [https://resend.com/handbook](https://resend.com/handbook)

- [https://handbook.gitlab.com/](https://handbook.gitlab.com/)

- [Hyperactive Hive Mind Workflow](https://www.perplexity.ai/search/hyperactive-hive-mind-cal-newp-P9P2AVLqRZazW2Yz5UAuig)

- [https://dora.dev/capabilities/generative-organizational-culture/](https://dora.dev/capabilities/generative-organizational-culture/)

### Joel’s notes

### Materials from the call

### ✍️ Post

---

I am, admittedly, a note-taking nerd.

I have written about this many times [[1](https://refactoring.fm/p/how-i-take-notes-part-1?utm_source=publication-search), [2](https://refactoring.fm/p/brian?utm_source=publication-search), [3](https://refactoring.fm/p/how-i-write-refactoring-?utm_source=publication-search)] and I guess I will keep doing that, because 1) good writing, in both work and life, seems to be constantly underrated, and 2) my workflows change over time, and I can’t help but writing about them.

Also, my work as a full-time writer is a note-taker dream. My output is very directly connected to the quality of my note-taking: the better I am at [managing my knowledge](https://refactoring.fm/p/how-i-take-notes-part-1?utm_source=publication-search), the faster and better I am able to turn it into articles.

Even in my past lives, as CTO first and Head of Engineering later, I have always been the docs guy. I introduced Notion at my startup in 2018, and tweaked it endlessly to create the perfect workspace for us.

All this passion didn’t save me from making mistakes. Actually, a lot of them.

Many (most?) of our docs grew stale and irrelevant. Our structures so complex that people couldn’t find even basic information. We declared *doc bankrupcy* and started over more than once.

This is what I was thinking when I joined our latest mastermind a few weeks ago, about **Engineering Handbooks**.

![image](../assets/128bdf02815c801b.png)

In our private community, we run a mastermind session every month: we vote on a topic, we join a 75 mins session facilitated by [Joel](https://monkeysthumb.co.uk/) (a professional CTO coach), and discuss our respective experiences.

After the session, Joel publishes the learnings on our forum, the conversation continues async, and I eventually turn the insights into the article you are reading right now.

![image](../assets/128bdf02815c8098.png)

So, this piece is the result of the **collective knowledge of ~20 CTOs, engineering managers, and software engineers**, who debated on engineering handbooks for *weeks*. And I have the steep task of turning it into a full article!

So, here is what we will explore today:

- 📘 **What is an Engineering Handbook** — and why it is a crucial investment for your team.

- 🏗️ **Structuring your Handbook** — to ensure it is comprehensive yet easy to navigate.

- 📝 **Creating and Maintaining** **Handbooks **— strategies to keep them relevant and up-to-date.

- 🌐 **The Handbook-first approach** — and how it transforms team communication and culture.

Let’s dive in!

---

### **📘 What is an Engineering Handbook?**

An Engineering Handbook is the guide for how your engineering team works.

It serves both as a **cultural repository**, capturing your team’s collective wisdom, and as an **operational guide**, explaining how the team should function day-to-day.

Handbooks come in many forms, the most popular of which are digital docs (wikis, Notion, Confluence, …), and code repositories — i.e. markdown files that live together with code, like [GitLab's public handbook](https://gitlab.com/gitlab-com/content-sites/handbook).

In some companies handbooks get also printed as physical books, and given to new employees. This is less common but still pretty much in use, like [at Valve](https://cdn.steamstatic.com/apps/valve/Valve_NewEmployeeHandbook.pdf).

Handbooks for engineering teams typically cover three key areas.

1. 🛠️ **Technical practices** — coding standards, development processes, and tech stack details.

1. 🤝 **Team dynamics** — communication, collaboration guidelines, and decision-making processes.

1. 🌱 **Growth and onboarding** — how new members join and how existing members develop their skills.

In short, it's a living document that reflects and shapes how your team collaborates to build great software.

The *living* part is crucial. As [Umberto Nicoletti](https://www.linkedin.com/in/umberto-nicoletti/), Head of R&D, put it in the community thread:

> *"Rules are made to serve us, not for us to serve the rules."*

The handbook is a tool to *empower* your team, not constrain it. To achieve this, teams need to keep it relevant and up to date, which is tricky, but well worth it. A good handbook, in fact, enables:

1. 🚀 **Speed **— it makes onboarding and decision-making faster by providing clear, accessible guidance.

1. 🔄 **Consistency** — it ensures uniform practices across projects and team members.

1. 🌐 **Scalability** — it enables teams to grow and work asynchronously by codifying knowledge and processes.

So, let’s see how to structure your handbook 👇

---

### 🏗️ Structuring your Handbook

Handbooks should be easy to understand and navigate, because engineers have to actually *want* to use it.

This is the #1 quality you should aim to achieve — before it being comprehensive, detailed, or whatever you might think of.

When something is easy to understand, it is easy to update. When it is easy to navigate, things are easy to find. Remove these qualities, and over time handbooks become forgotten dusty tomes sitting in a (digital) corner.

![image](../assets/128bdf02815c8068.jpg)

To reflect on how to build your handbook, let’s cover three things: **organization principles**, **sections**, and **modularity**.

#### **1) 🗂️ Organization Principles**

Documentation is a game where players are, in turn, either readers or writers.

As a reader, I want to easily find and read valuable information about what I need. As a writer, I want to easily write about what I am working on and contribute to the company knowledge.

In both cases, we want to **minimize** **effort** and **maximize** **value**. So, without getting into any particular structure or tool, these are the qualities we should optimize docs for:

- 🔄 **Reusable **— Design your notes to be easily reused and connected. The more information is reused, the more value it provides and the easier it repays the cost of writing it. For reusability, the best strategy is to have notes/pages that are **small** and **cohesive**. Create a note around a **single concept**, and link it to all the other notes where this concept is mentioned or useful.

- 🔍 **Discoverable **— Make content easy to be found. Whatever tool you use, create a simple structure and avoid excessive nesting. Prefer tags (if you can) to deep subfolders, and make navigation as easy as possible. E.g. for their internal docs, Notion has ditched folders in favour of a [global database](https://www.notion.so/blog/how-notion-uses-notion#how-we-categorize-every-document) organized with labels.

- **🍱 Contextual **— Organize notes around how you will use them. Think at what they are useful for, in which situations you will need them, and put them there.

#### **2) 📚 Core Sections**

There is no one-size-fits-all structure for a handbook, but these are sections you might consider:

1. **Company vision & mission** — This sets the tone for everything else. We discussed it in [this recent piece](https://refactoring.fm/p/how-to-craft-your-vision-and-mission?utm_source=publication-search).

1. **Domain knowledge **— if your business operates in a space that requires specific domain knowledge (e.g. finance), you may have a section that teaches the basics.

1. **Engineering principles **— they answer the "why" behind your engineering practices. It’s the set of your shared engineering beliefs, that guide how decisions should be made. More about them [here](https://refactoring.fm/p/principles).

1. **Dev process** — How do you build and ship software? This covers your SDLC, from planning to deployment.

1. **Tech guidelines** — Your coding standards, design principles, and best practices. Aren’t these the same thing as the engineering principles? Not exactly: principles are cultural stances, e.g. “[fix problems even when they are not yours](https://asana.com/inside-asana/asana-engineering-values#:~:text=decades%20to%20come.-,6.%20Fix%20problems%2C%20even%20when%20they%E2%80%99re%20not%20yours,-By%20Rachel%20Miller)”, guidelines are tactical rules, e.g. linting and naming conventions.

1. **Team collaboration** — How do engineers work together? This includes meeting structures, stakeholders, pairing, and everything around ceremonies.

1. **Onboarding **— how new engineers [get up to speed](https://refactoring.fm/p/onboarding-engineers?utm_source=publication-search). There might be specific docs about your first week, how to setup your dev environment, etc.

1. **Career Growth** — how team members can grow their careers. This includes [career frameworks](https://refactoring.fm/p/career-frameworks-1?utm_source=publication-search), reviews, promotion cycles, and HR stuff.

Again, you shouldn’t probably create *all *of this: for some companies, domain knowledge is irrelevant. For small teams, career growth is just a few lines. And so on. Consider this as a checklist that you can go through and take inspiration from.

For example, [**Mirco Franzek**](https://www.linkedin.com/in/mirco-franzek/), Senior Backend Developer, shared in the community discussion how his team structures their handbook:

> "*Our handbook is roughly divided into four parts: onboarding, daily work, development information, and business logic. The 'daily work' section is read and updated most often.*"

This approach is totally fine: it balances the needs of new hires with the day-to-day requirements of the existing team.

All in all, it is more important for the handbook to be clear and useful than to be comprehensive. So, as [**Ross Younger**](https://www.linkedin.com/in/rossyounger/) said, start small:

> *"When it comes to getting the first version out, my advice would be to start small. Start with what matters most to your team and let it evolve. Be prepared to insert placeholders for sections you think you ought to write later, but also be prepared to change your mind."*

Your handbook's structure should serve your team's needs. Don't be afraid to experiment and iterate. The best structure is the one that your team actually uses and finds valuable.

---

### 📝 **Creating and maintaining handbooks**

A well-structured handbook is great, but the real challenge lies in creating and maintaining it. Let's explore how to make this process smooth and sustainable:

#### 1) 🚀 Kicking off

If you don’t have a lot in place, or what you have is old / unreliable / not much used, you should probably restart from scratch.

Starting fresh creates positive momentum and allows everyone to contribute without biases/attachments to what exists. If you are doing that, consider a three-step process:

1. **Document what you have** — start by writing down your current practices. Don't aim for perfection, just capture what you're actually doing.

1. **Identify gaps** — as you document, you'll naturally spot areas where guidance is missing or unclear. There are the practices where people disagree on how to perform them: might be code reviews, design docs, or else. Just make note of these and move on. Don’t aim to fix everything on the spot.

1. **Prioritize and fill** — schedule the work to fill the gaps, starting with the most critical ones. Get to a first version that is acceptable, and move on to the next phase 👇

#### 2) 🌱 The Gardener

Maintaining docs is often compared to gardening: good gardeners do a few small things everyday, instead of big batches of isolated work. Once your handbook is in a good state, you should nail the basics of contribution:

1. **Assign a *****gardener***** **— I am a big believer in having a direct responsible individual for your handbook. While contribution should come from everyone (more on that below), it’s important to have someone who has the meta-job of keeping the whole work relevant. Is the structure good? Is the handbook being used? What can we do better? When contribution is 100% bottom up, without a single owner, the risk is nobody asks these questions.

1. **Encourage contribution **— the gardener should prod team members to contribute to the handbook, and make it easy for them to do so. Is the structure clear? Are there good templates in place? Aim to remove all kinds of *thinking* people should do before contributing. 

1. **Establish the boy scout rule **— just like they [should do with code](https://refactoring.fm/i/136586866/boy-scout-maintenance), people should always leave the handbook in a better state than they found it. When anyone finds a small gap, it is best to fill it on the spot. This is infinitely easier than letting problems pile up, like with tech debt.

1. **Prune outdated content** — the limit of the boy scout rule is that it only works for stuff that actually gets updated. But a lot of content simply becomes irrelevant over time, and it’s important to prune it to keep the space decluttered. While this can be done by anyone, in my experience it is mostly up to the gardener.

Shout-out to** **[Ezequiel Actis Grosso](https://www.linkedin.com/in/fractionaltech/), fractional CTO, who introduced the gardener topic in our discussion:

> *"Another aspect I think is important is the role of the 'Gardener' — or what Notion refers to as a Librarian. It helps to keep the content curated, up-to-date, and valuable — more 'gardening' than 'policing,' similar to the mindset around code ownership."*

#### 3) 🔗 Integrate into existing workflows

Finally, for the handbook to stay relevant, maintaining it should feel natural, not like an extra chore. To do that, the best way I know is to *integrate *it into existing processes. In my experience, these are the easiest ones:

1. **Onboarding** — make new hires update relevant handbook sections as a part of the onboarding process. This is such a win-win-win: new hires can easily spot gaps exactly because they are new, they bring fresh perspectives, and for them it’s a good task that delivers real impact.

1. **Retrospectives **/** Postmortems** — After significant projects, incidents, or simply in periodic retrospectives, update the handbook with lessons learned. To make sure you do so, create an agenda for these meetings and include handbook update as a bullet point.

1. **Tech decisions** — Whenever you make important technical decisions, ask yourself if you should reflect these in your handbook. Structured formats like ADRs ([Architecture Decision Records](https://refactoring.fm/i/140313356/adrs)) can be linked or integrated directly.

So my TL;DR is: 1) start with a solid (if small) first version, 2) assign an owner, 3) distribute the responsibilities, and 4) link to processes.

---

### 🌐 H**andbook-first**

As we close this guide, I want to reflect on how teams actually use their handbooks, and what makes the difference between success and failure.

In my experience, there are three levels of handbook adoption that teams go through: **handbook-free**, **handbook-supported**, and **handbook-first**.

Let's explore each of them.

#### **1) **🙅‍♂️ **Handbook-free — people are the documentation**

Most teams start here. Knowledge lives in people's heads and is transmitted through conversations. This works fine when teams are small and everyone talks to each other frequently.

However, when teams grow or become distributed, this approach breaks down. Knowledge gets lost, inconsistencies arise, and onboarding new people becomes super long.

![image](../assets/12dbdf02815c8088.jpeg)

This leads to the infamous *hyperactive hive mind*, as [Clemens Adolphs](https://www.linkedin.com/in/clemens-adolphs-7473a392/) points out: 

> *"An engineering handbook is one of many important tools to employ combating what Cal Newport calls the 'hyperactive hive mind' way of working. You've all seen that way, where work unfolds in a series of asynchronous, unstructured, ad-hoc messages. A handbook approach is calmer but takes time and effort."*

To leave this stage you need to start documenting things 👇

#### **2) **🥈 **Handbook-supported — the unstable middle**

This is where many teams land in their first attempt at documentation. The typical pattern is:

- Conversations mostly happen in meetings and chat

- Decisions are taken and later (often begrudgingly/hastily) reported in docs

- Documentation is seen as a chore, something you do after the real work

But here's the key insight: this is not a stable state. One of two things typically happens:

1. ❌ If documentation always comes *after* decisions, there is little benefit in having docs at all. Over time, they become outdated and forgotten, effectively reverting to "no handbook".

1. ✅ If teams start seeing the benefits of documentation, they naturally move towards a handbook-first approach. The virtuous cycle begins when docs start preventing sync conversations from happening, thus saving time.

#### **3) **🥇** Handbook-first — documentation drives decisions**

In a handbook-first culture, the dynamic changes completely:

- Fewer conversations happen, and they often start *from* documentation.

- Decisions are made *because* of documentation, not the other way around.

- The handbook becomes a tool for *thinking*, not just recording.

Teams that successfully adopt a handbook-first approach are more resilient and do clearer thinking. In fact, writing things down just makes your thinking better (trust me on this, I am a writer) and often reveals gaps in logic or process that weren't apparent in conversation.

It also makes knowledge a *team* quality, rather than a personal one, so that it doesn't walk out the door when people leave. And new team members can quickly get up to speed by reading documented processes and decisions.

#### 🏢 **Real-world examples**

Some companies have mastered the handbook-first approach:

- [**GitLab**](https://handbook.gitlab.com/) — leads by example with their public handbook, which has become the gold standard for transparent documentation. They use it for everything from engineering practices to company values.

- [**Resend**](https://resend.com/handbook) — shows how smaller companies can adopt this approach effectively. They maintain a manageable but comprehensive handbook that grows with their team.

- [**Linear**](https://linear.app/method) — demonstrates how documentation can be seamlessly integrated into product development. Their [**"Linear Method"**](https://linear.app/method) publicly documents not just processes, but the principles behind how they build software, influencing both their team's work and their product design.

Remember what [**Ross Younger**](https://www.linkedin.com/in/ross-younger-429b311/) emphasized:

> "The handbook is part of how you live. If it's not serving you, then why does it exist?"

This gets to the heart of the matter. A handbook isn't just a document — it's a fundamental shift in how your team thinks, communicates, and makes decisions. When done right, it becomes an integral part of your engineering culture, driving both efficiency and quality in your organization.

---

### 📌** Bottom Line**

So, here is the final cheatsheet about Engineering Handbooks:

- 📘 **Purpose** — a handbook serves as both a cultural repository and an operational guide for your engineering team.

- 🏗️ **Structure** — focus on three core areas:

- 📈 **Evolution** — teams typically go through three stages:

- 🎯 **Success factors **— focus on these:

- ⚠️ **Common pitfalls **— watch out for these:

Remember: the goal isn't perfection, but usefulness. A slightly messy but actively used handbook is far better than a pristine one that nobody reads.

---

### 💬 [Join the Community](https://refactoring.circle.so/join?invitation_token=a106a5e1beec6c1dffdb5c7c3cec92cd5a94351b-674026ab-40f6-4847-86a0-3aa71f173705)

And that’s it for today! As always, this article couldn’t be possible without the great ideas shared in our private community of **800+ members**. It is seriously the best part of Refactoring, and you should join it if you haven’t already.

[Join the Community today 💬](https://refactoring.circle.so/join?invitation_token=a106a5e1beec6c1dffdb5c7c3cec92cd5a94351b-674026ab-40f6-4847-86a0-3aa71f173705)

---

### 🏛️ [Learn more in the Library](https://library.refactoring.club/)

You can also find this and the attached resources in the Refactoring Library 👇

[Go to the Library 🏛️](https://library.refactoring.club/)

---

And that’s it for today! See you next week 👋

Luca
