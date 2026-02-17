---
aliases:
  - "How to Create an Engineering OS for your Organization"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-essays|Publish Essays →]]"
Status: Evergreened
URL: "https://refactoring.fm/p/how-to-create-an-engineering-os-for"
"👓 Status": Discarded
"Created time": "2024-05-16T07:43:00.000Z"
Date: 2024-05-22
"Has Notes":
  - "[[evergreen/the-four-dimensions-of-calibration|The four dimensions of calibration]]"
  - "[[evergreen/on-decision-making|On Decision Making]]"
Tags:
  - Guest
  - Mgmt
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 7f3ca44e-c0f0-400c-9972-bd70b4f2b8b1
---

# How to Create an Engineering OS for your Organization

Refactoring was born to help engineers write good software and work well together.

This is a broad goal that is shared by other products and communities as well. I got in touch with many of them during these years, often doing some work together, partnerring on articles, and more.

One of them is, of course, **Plato** — they run an awesome engineering leadership mentoring platform and community. They recently **got acquired by Coda** 🎉 which gave me the chance to reconnect with Quang and Jean-Baptiste — Plato’s founders — and catch up.

This turned into an extremely interesting chat, where they explained to me how they are building a comprehensive framework about how engineering teams operate, which they called **EngOS**.

EngOS has a lot of overlap with my own way of thinking at how teams work, so we decided to write this piece together and explore this topic.

---

### 📖 What is an OS?

One of the first memories I have of my time as a startup founder is me printing a giant version of the [Business Model Canvas](https://en.wikipedia.org/wiki/Business_Model_Canvas), and hanging it to the wall.

![image](../assets/3dc3a78afcb740dc.png)

I remember being confused by it: I didn’t know what to put in the various boxes, and even when I did, I was not sure it was the right stuff.

In hindsight, such *confusion* was the whole point of the exercise. The *Canvas* is not a framework in the sense of it being *prescriptive* about what you should or shouldn’t do. It is a template — a set of building blocks that you can use to create *your own *framework.

Back to engineering, whenever we ask how teams should do this and that, we often get “*it depends”* as a response. But what if we take a step back? Can we define a standard set of *areas* — the equivalent of the Canvas’ boxes — which you can fill with your own processes, and which define how your engineering org operates?

That’s what EngOS does 👇

---

### 🧩 EngOS

Plato is, at its core, a mentorship platform for engineering leaders. Quang started it in 2017, and, in 7+ years, they worked with hundreds of companies, thousands of mentors, and hosted tens of thousands of sessions.

At some point, you naturally start to see patterns. Quang tells me that every engineering team has an *operative system*. They may not call it that way, but they have one. 

Like a computer OS, an engineering OS is made of various pieces, each having a specific function. The pieces of EngOS answer questions like:

- *How do we make decisions?*

- *How do we plan work?*

- *How do we grow the team?*

Depending on the scale and stage of the company, some categories may be informal or undefined, while others more crisp or inherited from the overarching organization. Also, as an engineering leader, chances are you can only influence some of them at your level.

So, EngOS defines four major areas:

- 🟡 **Execution **— how things get done.

- 🔵 **Team **— how teams are run.

- 🟢 **Engineering **— how engineering work is performed, from design to operations.

- 🟣** Personal productivity **— how individuals operate.

Each area is further split into multiple items, so you have ten of them in the end 👇

![image](../assets/bfe1662233d04345.png)

Once they identified these items, Plato started collecting notes about how the most successful companies run them. For example:

- [How Coda does ](https://coda.io/@oliverheckmann/the-ultimate-coda-handbook-for-planning-and-okrs)[**Planning**](https://coda.io/@oliverheckmann/the-ultimate-coda-handbook-for-planning-and-okrs) 🟡

- [How Yelp drives ](https://platocommunity.substack.com/p/how-we-drive-developer-productivity)[**Engineering Productivity**](https://platocommunity.substack.com/p/how-we-drive-developer-productivity) 🟢

- [How Webflow does ](https://platocommunity.substack.com/p/webflows-playbook-for-hiring-engineers)[**Hiring**](https://platocommunity.substack.com/p/webflows-playbook-for-hiring-engineers) 🔵

So, the driving principle of the EngOS is ”*do not reinvent the wheel*”. Whatever challenges you are facing at work, chances are other engineering teams have faced them before, and they may have found a solution you can be inspired by.

By identifying the main pieces of your OS you can more easily find common ground with those teams, speak the same language, and find common solutions.

So, let’s look at each individual item from EngOS, with examples from Refactoring and Plato about how these are run in successful companies:

---

### 🟡 Execution

Execution is *how things get done* at your company. 

This is a fractal topic: while at a high-level there should exist principles and processes that are shared across the whole org, the more you go into details the more teams should have the autonomy to run their own show.

Let’s look at the three main *dimensions* of execution:

#### 1) Planning

Planning is an ever-controversial topic in engineering. The best planning processes strike a delicate balance between long-term goals with short-term agility. They create *alignment* across the organization, while empowering teams to find their own solutions. 

Here are a few powerful ideas about this:

- ✏️ [**Coda Handbook for Planning & OKRs**](https://coda.io/@oliverheckmann/the-ultimate-coda-handbook-for-planning-and-okrs) — Oliver Heckmann wrote a detailed handbook which draws from his experience as Head of Engineering at Coda, plus that of 14 years as VP of Engineering at Google. I love his breakdown into the three blocks: **Big Rocks**, **OKRs**, and **Resource Planning**, and how precisely he addresses process and execution.

- 🍀 [**The Four Types of Work**](https://refactoring.fm/p/the-four-types-of-work-2023?utm_source=publication-search)** **— in one of the most popular Refactoring articles ever, I address how to plan for the various types of work you encounter in an engineering org.

- 🎙️ [**Netflix’s combination of Goals + Freedom**](https://www.youtube.com/watch?v=_ed80YBOtZk)** **— in our interview to Kathryn Koehler, Director of Productivity Engineering at Netflix, she explains how Netflix sets annual and quarter goals, and leaves teams the freedom + responsibility to go after them however they like.

#### 2) Team Collaboration

Team collaboration is the set of processes that make people work *together *effectively: the way you run meetings, the way people get status update, the set of project mgmt tools, and so on.

Here are a few questions you can ask yourself to start assessing the state of your team collaboration:

- *What recurring meetings do you hold?*

- *What is a recurring meeting you have added over the last 6 months? Why?*

- *What is a recurring meeting you have removed over the last 6 months? Why?*

- *What is an example of a collaborative process that is run regularly and doesn’t involve meetings?*

- *How can people learn about the status of a project / task without asking anyone?*

Does any of these questions make you uneasy? Why? Start from there!

Here are notable examples that we covered in the past:

- 🔨 [**How to Build a Company around Crafters**](https://refactoring.fm/p/kaz-nejatian)** **— in this interview with Kaz Nejatian, COO of Shopify, we walked through how they abruptly removed *all* recurring meetings from the company, and they strive to empower crafters at all costs, even accepting some chaos while doing so :)

- 🪚 [**How to Reduce Meetings**](https://refactoring.fm/p/how-to-remove-meetings)** **— a framework + a detailed case study on making meetings reduce until they eventually… disappear ✨

- 🧰 [**How to Create a Great Remote Team**](https://refactoring.fm/p/how-to-create-a-great-remote-team)** **—

#### 3) Decision Making

How teams make decisions is an often overlooked part of how they work. It doesn’t feel like something that should be *designed*, yet you can easily measure how well you are doing it by asking two questions:

1. **Efficiency** — how long does it take to make a decision? Think of feature prioritization, design dilemmas, or build vs buy situations: how fast do you converge?

1. **Quality** — how *sticky* are your decisions? How often do you have to backtrack on them?

In my experience, here is what enables good decision making:

1. **⭐ Shared principles** — you want people to make choices that are in line with your team’s culture. Different people tasked with the same decisions should mostly come to the same conclusions, and that is only possible if they share the same set of values.

1. **🔍 Good context **— people can only make good decisions when they have full visibility into the elements that go into it. As a manager, you should *lead with context*: provide all the necessary data to get to a decision, and empower your teammates to go for it.

1. 📋 **Templates and procedures** — for specific and recurring situations you may write down procedures about how to perform them. You may create a template for design docs, a set of criteria for buy vs build, a checklist for code reviews, and so on. Procedures easily turn into mini frameworks that speed up work and improve its quality.

Here are some resources to learn more about this:

- **⚖️ **[**The 7C Framework for Buy vs Build**](https://platocommunity.substack.com/p/10-the-7cs-framework-for-the-build) — a thoughtful, and detailed framework from Sue Nallapeta, CTO, about choosing technology. It considers 7 factors: *core capability, cost, complexity, competence, cohesion, competitive advantage, *and *culture*.

- ⭐ [**Engineering principles**](https://refactoring.fm/p/principles?utm_source=publication-search) — my own take on how to create good engineering principles for your team, with plenty of examples from successful companies.

- 🎲 [**Mental models for engineers and managers**](https://refactoring.fm/p/mental-models-for-engineers-and-managers) — the collection of my favorite mental motels that helped me at work.

---

### 🔵 Team

#### 1) Formation

Structuring teams is a complex process that includes hiring, allocating headcount, creating reporting structures, and more.

Here are examples and resources that help with it

About hiring, we wrote a [**full guide**](https://platocommunity.substack.com/p/webflows-playbook-for-hiring-engineers) about it last year

- [**Webflow’s Playbook for Hiring Engineers**](https://platocommunity.substack.com/p/webflows-playbook-for-hiring-engineers) — the story of how Webflow ditched LeetCode, created a simpler hiring pipeline and measured how many engineering hours it saved in the process (spoiler: many!)

- [**How to Structure Engineering Teams**](https://refactoring.fm/p/how-to-structure-engineering-teams)** **— our own full guide on how to create efficient team structures, based on scope, growth stages, roles, and more.

- [Good Hiring Process](https://refactoring.fm/p/good-hiring-process-1?s=w)

#### 2) Management

Management is a very broad term. In the scope of EngOS, it is about coaching and mentoring your teammates. Think of onboarding, 1:1 meetings, training, health and growth.

This feels like an ever-elusive topic, as it depends on so many factors. Recently on the newsletter we discussed what [The Right Amount of Management](https://refactoring.fm/p/the-right-amount-of-management) looks like, and the [evolving role of Engineering Managers](https://refactoring.fm/p/how-engineering-management-is-changing).

From Plato, I also loved [Anant Gupta’s talk](https://www.youtube.com/watch?v=J_0wDkFlEM4) about lessons learned from his experiences at Uber, Linkedin, and Included Health.

[How to Run Great 1:1s](https://refactoring.fm/p/how-to-run-great-11s-in-2023)

[How to Give Feedback](https://refactoring.fm/p/how-to-give-feedback-)

#### 3) Calibration

Calibration is all-things performance management. 

This topic can get more or less nuanced based on the growth stage of your company, and include things like performance reviews, career frameworks, compensation, and succession plans for critical roles.

About engineering performance, I liked [**Gusto’s simple approach**](https://platocommunity.substack.com/p/9-how-we-evaluate-engineering-performance)** **which takes care of four axes:

1. 🗃️ **Project** — the direct impact you or your team (if a manager) have on deliverables. It's best described in terms of customer behavior changes (e.g., increased product usage, higher NPS) or learnings that influence product direction.

1. 🔨 **Better Engineering** — improvements in systems or platform that boost engineer effectiveness. It includes reducing test time, error rates, or new hire ramp time. Its importance grows with seniority due to the broader impact on the overall engineering system.

1. 🪴 **People** — enhancing team efficiency and health through things like hiring, mentoring, providing feedback, and code reviews. Metrics for People impact include team engagement, effective hiring, team health, and qualitative feedback from team members and peers.

1. 🏢 **Better Organization** — improving the overall health of the organization. Examples include enhancing the hiring process through new interview questions or rubrics, driving diversity programs, and representing the company at external events.

I wrote more about calibration in two previous pieces:

- 🏅 [**Performance Reviews**](https://refactoring.fm/p/performance-reviews)

- 🪜 [**Career Frameworks**](https://refactoring.fm/p/career-frameworks-1)

---

### 🟢 Engineering

The last area is about engineering-specific activities. EngOS buckets them into three categories:

#### 1) Operations

How you manage maintenance, on-calls, incidents, and all the operational train of work.

My favorite litmus test of how you are doing on this is how much proactive vs reactive work you do.

- Great teams are able to do operations mostly *proactively*, through prevention and scheduled work. On-calls are peaceful, and incidents are rare.

- Struggling teams are rather than stuck in *reactive*, *fire-fighting* mode. They routinely spend 50%+ of their time on operations, and feature work gets constantly derailed by failures and P0 bugs.

We collected many community stories and ideas about this in these previous pieces:

- **🛠️ **[**How to Plan for Maintenance**](https://refactoring.fm/p/how-to-plan-for-maintenance?utm_source=publication-search)** **— our thorough guide, full of stories from the community, about creating an effective process for maintenance.

- ⬆️ [**Achieving 99.99% Uptime at DigiCert**](https://platocommunity.substack.com/p/11-transforming-digicerts-organization)** **— if you are up for something more technical, here is a loong and detailed case study by Wade Choules, SVP of Eng at DigiCert, about how they completely turned around their dev process to achieve high availability.

- 🎙️ [**Observability & Testing in Production**](https://refactoring.fm/p/observability-and-testing-in-production?initial_medium=video)** **— our recent interview with Charity Majors where we discuss, among other things, how teams should think about operations, testing, and continuous delivery.

#### 2) Productivity

Engineering productivity is a divisive topic: most teams agree you should do something about it, but most disagree about *what*. Should you use metrics? Should you set goals? What about developer experience? How should you work on it?

Fortunately, this is also one of the topics we cover the most often on Refactoring. Here are some recommendations:

- 📊 [**How to Use Engineering Metrics**](https://refactoring.fm/p/how-to-get-started-with-engineering)** **— this is my most popular article ever. It’s a full guide on how to get started, what metrics to pick, and what you should use them for.

- 💫 [**How we Drive Developer Productivity at Yelp**](https://refactoring.fm/p/how-to-get-started-with-engineering)** **— this is a piece I really enjoyed from the Plato community by Kent Willis, Director of Engineering at Yelp. It would be reductive to say it’s just about productivity. It’s a summary of the 10-year engineering journey of Yelp, from 2013 to today, and how they went through the monolith, microservices, metrics, platform teams, and more.

- 🎙️** **[**Engineering Productivity & Developer Experience**](https://refactoring.fm/p/engineering-productivity-and-developer?initial_medium=video)** **— we recently interviewed Laura Tacho, CTO at DX about these very themes. Laura is a veteran: she is an accomplished, engineering coach, and her work at DX focuses exactly on developer experience (you can pretty much tell by the name) and productivity.

#### 3) Design

Finally, you should reflect on the state of your design process and documentation. In addition to what we already covered, here are two articles that should help you with that:

- ✏️ [**Design Docs**](https://refactoring.fm/p/design-docs)** **— design docs are the MVP of all docs. I wrote a popular article (which includes my own template) about them a while back.

- 📑 [**How to Write Documentation**](https://refactoring.fm/p/how-to-write-documentation)** **— if you are up for something more thorough, here my full guide about creating good docs and making the team stick with them. It’s a 3000-word piece full of additional references, links, and tools.

---

### 🟣 Personal Productivity

Finally, there is your personal productivity setup. I love how in the EngOS picture this is at the base: in fact, while much of your productivity depends on how your team works, there are some important foundations you should take care of by yourself.

Everyone has their own preferences on this, but here are a few recipes that I have seen working broadly and I can recommend: 

- ⏱️ [**How to Manage Your Time**](https://refactoring.fm/p/how-to-manage-your-time?utm_source=publication-search) — my personal setup, which includes pomodoros, timeboxing, a good calendar, and setting focus time aside.

- **🧘 **[**How to Relieve Stress**](https://refactoring.fm/p/stress?utm_source=publication-search)** **— understanding the sources of stress, monitoring your state effectively, and strategies to defuse burnout. This has become even more important for me since I work by myself.

- 📙 [**Atomic Habits**](https://refactoring.fm/p/atomic-habits)** **— our community review of the best-seller book by James Clear. It’s one of my favorite books: it has changed the way I think at my identity, progress, and many other things.

---

### 🏃‍♂️ How to get started?

Once you understand the framework, you can use it to reflect on what you can do better with your team. Quang suggests to do so by holding an **audit meeting***.*

Here is a template you can use to run it 👇

As you can see in the template, the audit works in three steps:

1. 🔍 **Scope** — You look at the 10 categories and choose 3-4 to include in the audit. These should be the ones with the strongest potential for improvement.

1. 🗳️ **Survey** — Before the meeting, you survey participants about *pain points* in the various categories.

1. 💬 **Discuss** — You get together as a group and discuss the results of the survey. You may sort pain points by severity, and design actions to address them.

### 📌 Bottom line

Engineering leaders are tasked with making their teams operate efficiently. Efficiency, however, is an *holistic *goal that doesn’t come from good technology alone: it comes from good process, good culture, and taking care of the team as a whole.

Not being able to make good decisions promptly is just as problematic as not having a good CI/CD process, yet it may be easily overlooked.

In fact, while this framework is called *EngOS*, I have found most categories to be relevant to any team, even non-technical ones.

Plato is building a library of community-sourced articles and templates to help solve the various friction points of your OS, and they will have many released by early June for their annual conference Elevate.

Elevate will be held at San Francisco on June 5th and 6th — as a Refactoring reader, if you want to join you can get **60% off the full ticket price** by using the link below 👇 

 https://platohq.com/events/elevate?code=ELEVATE2024-REFACTORING
