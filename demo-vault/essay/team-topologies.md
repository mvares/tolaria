---
aliases:
  - "Team Topologies"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-essays|Publish Essays →]]"
Status: Evergreened
URL: "https://refactoring.fm/p/team-topologies"
"👓 Status": Not started
"Date HH": 2025-03-14
"Created time": "2024-04-18T14:53:00.000Z"
Date: 2023-05-11
"Has Notes":
  - "[[evergreen/the-four-types-of-teams|The Four Types of Teams]]"
  - "[[evergreen/the-three-types-of-cognitive-load|The Three Types of Cognitive Load]]"
Tags:
  - Mgmt
  - Book
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: fd7af2ea-14c5-4262-94c7-8762ee5e2f45
---

# Team Topologies

### 📑 Materials

---

[Untitled](https://www.notion.so/3be96fcda3b24f6596e5576bbc5423de) 

### 💡 Ideas

---

- 

### ✍️ Post

---

Team organization — that is, how people communicate and work together — can make or break companies. Yet, when it comes to organizing engineering teams, it is hard to find good, comprehensive advice. 

Most ideas out there feel either too abstract — e.g. “*create two-pizza teams*” — or too specific — e.g. “*the ideal ratio between engineers and managers is 5*”.

There are few works that manage to stay high-level, so to be relevant to many situations, while also being practical, so that you can apply lessons to your team.

[**Team Topologies**](https://www.goodreads.com/book/show/44135420-team-topologies) is one of them.

Written in 2019 by Matthew Skelton and Manuel Pais, both experienced DevOps consultants, it has rapidly become a seminal book about team organization.

It has achieved this by providing an original, brilliant *mental model *about collaboration, coupled with case studies that let people understand how to use it in practice.

So, today I will review the core ideas in the book and give you my own take on them. I will also link related articles and further resources to learn more.

We will cover:

- 🔄 **Conway’s *****reverse maneuvre ****— *using Conway’s Law for good.

- 🏋️‍♀️ **Cognitive Load **— an original way to think at teams’ scope.

- 🍀 **The Four Types of Teams **— the *core* of the book.

- 💬 **The Three Interaction Modes **— how the types of teams work together. 

- 📌 **Luca’s takeaways **— what I personally took from the book and how to use this in practice.

Let’s dive in 👇

### 🏰 Conway’s *reverse maneuvre*

In Karate Kid — one of my favourite movies when I was a kid myself — an old Karate *sensei *teaches martial arts to a boy, by using weird, seemingly unrelated exercises.

![Wax on, wax off!](../assets/f3af3073808249d0.webp)

Team Topologies pulls off a similar trick with software. It teaches you how to write good code, but almost never talks about it.

In fact, the authors are strong believers of the **Conway’s Law**, which states that your software architecture will eventually resemble your team organization. So much, that they believe that if you create a good team organization, software architecture will largely take care of itself.

![image](../assets/2f95305e582b4fe9.png)

What makes a team organization *good*? The book gives you a brilliant answer, which is about *cognitive load* 👇

### 🏋️‍♀️ Cognitive Load

There is wide consensus in our industry around splitting engineering orgs into small teams. There is less consensus on *how *to do so.

In Team Topologies, a good team should own an amount of software that can *fit in your head* (or *their* head, as a team). Engineers and teams are able to bring the most value when they sustain the right amount of *cognitive load* for their work: not too much, not too little.

Cognitive load here is the amount of *mental effort* that is required in your working memory to perform your job. Basically, how much stuff you have to load in your brain.

However, not all cognitive load is created equal. There are three kinds:

- 🔨 **Intrinsic** — your tech skills, which are intrinsic to your work. E.g. how classes are defined in Java.

- 🐌 **Extraneous** — stuff you have to remember that doesn’t bring value, so it is mostly a distraction. E.g. *how do I deploy this app, again?*

- 🌟 **Germane** — knowledge about your business domain and the problems you need to solve. E.g. what are good abstractions for financial data, or best practices for an e-commerce checkout.

Germane load is the only knowledge that creates actual *value*. So, you want to create teams where such load is maximized, while *intrinsic* and *extraneous* ones are minimized.

What does this mean? 👇

#### 🔨 Reducing Intrinsic Load

Intrinsic load is about technology. 

You can reduce it via good tech choices that make stuff easy to build. E.g. building your prototype with a low-code tool can reduce the *intrinsic* load required to operate it, as opposed to going for a custom full-stack app.

Also, you can reduce intrinsic load by working on your team capabilities, instead of your tech:

- **Training **— upskilling your people makes it easier for them to build new things.

- **Pair programming **— making people work together lets them share the tech load.

- **Hiring **— by hiring for skills you are missing, you reduce the load on individuals by *spreading *it on more people.

#### 🐌 Reducing Extrinsic Load

Extrinsic load is about *bureaucracy* — meant as the unnecessary tasks and steps you need to perform in your dev process.

Extrinsic load is minimized by creating good DX. I have found that optimizing for fast and frequent releases, good tooling, and, in general, a culture of continuous delivery, is the best cure for this.

#### 🌟 Optimizing Germane Load

When you put all things together, you should organize teams so that they are able to apply their *domain knowledge* to solve problems of the *right size*, minimizing the amount of *plumbing* and non-business-related effort.

The germane load should also be optimized so that teams are not overwhelmed by the problems they need to solve. Splitting teams to make them own specific parts of the product lets them laser focus their domain knowledge and improve the quality.

So, how do you organize teams?

### 🎽 The Four Types of Teams

Based on this, authors identify four main types of teams:

#### 1) Stream-aligned Teams 🏆

These are teams who own and **work independently** on a *slice* of the business domain.

In other contexts they are commonly named *product teams*, but authors prefer a more *neutral *naming because the identifying nature of such teams is *how* they work — independently, with end-to-end responsibility — rather than on *what* (i.e. a product).

In fact, stream-aligned teams can arise in operations, support, and any other area when they are given the chance of owning a full stream of work. *Cross-functional* would also be misleading, because 1) it doesn’t guarantee independence, and 2) it isn’t necessarily true.

One of the key lessons of Team Topologies is that **stream-aligned teams are most important teams.** Other teams are basically there to reduce the cognitive load of stream-aligned teams.

The whole *stream* concept is about *flow — *a piece of software should move through the dev process to the final users with as few interruptions as possible, like a flowing river, minimizing the number of handoffs.

#### 2) Enabling Teams 🧑‍🏫

Enabling teams are about **developing skills**. 

They research new best practices, or new tech, and are *consulted* to improve the output of other teams. The final goal is to *transfer* such knowledge to stream-aligned teams, not to retain it themselves.

I have found this take interesting because I feel we most often focus on *collaboration* — i.e. splitting tasks across people/teams based on their skills — while there is lower attention on *training*, to take teams that today are *not* independent and make them actually so.

Collaboration brings overhead in terms of coordination, resource allocation, and more. There are times where this is desirable, and others where pushing for more independence is the right call.

To be honest, having dedicated* *teams for *enablement* isn’t necessarily viable for startups or mid-size companies, but I like the idea behind it and it was a good takeaway for me.

#### 3) Complicated-subsystem Teams 🧶

These are teams that **work on niche problems** that require specific skills, that would otherwise *bottleneck* the work of other teams.

The difference between *enabling *and* complicated-subsystem* teams is that the latter *retain *their skills, because there isn’t much benefit in teaching other teams, or it isn’t really viable — e.g. because of your headcount.

Typical examples are areas where you need specialized skills but only **occasional involvement**. Think of specific algorithmic work, audio-processing, or infrastructure tuning.

In these cases, you may settle with *horizontal *teams that occasionally collaborate with others, rather than full-time specialists, individually embedded in *vertical* teams.

#### 4) Platform Teams 🏗️

These are teams that build *infrastructure* that is used by other teams and enables their work. Infrastructure here is meant broadly: think of CI/CD, tooling and any product/framework born for internal use.

Platform teams are *similar* to stream-aligned teams in that they *own* their work — with the difference that their *customers* are other teams, so they are inward-facing.

They are also similar to *complicated-subsystem* teams* *in that they support the work of other teams — with the difference that platform teams create solutions that are used by multiple teams, while *complicated-subsystem* teams collaborate with other teams for bespoke work.

The difference between such various interaction modes is the core of Team Topologies 👇

---

### 💬 The Three Modes of Interaction

*Curling* is a (kind of weird) sport in which players slide *rocks* on a sheet of ice towards a target area. After the rock is thrown, players can *sweep* the ice in front of the stone with brooms and brushes, to decrease the friction and make the rock travel a longer distance.

In Team Topologies, the goal is to **support stream-aligned teams** to do their best work. Stream-aligned teams are the rock, while all other teams are like the *sweepers* whose goal is reduce friction.

![Stream-aligned teams are the *stones* that need support from all other teams.](../assets/988b781ea8e54f86.png)

To understand how to do so effectively, it is not enough to reflect on *what* teams do. You have to figure out how such teams *interact* with each other, so that their respective work is *multiplied*, rather than *obstructed*.

So, Team Topologies identifies three main modes of interaction 👇

#### 1) Collaboration 🤝

It occurs when two teams come together on a **shared project**.

It is the typical way *stream-aligned* teams and *complicated-subsystem* teams interact. Multiple stream-aligned teams may also collaborate in case of large projects and programs.

Teams who collaborate *split* their responsibility and need coordination, so you should design workflows to **limit***** *****collaboration** as much as possible.

If this looks counterintuitive to you, what we are just saying is that people who often work together should probably be on the same team, rather than coordinating from different teams. The latter should be your last resort, rather than the norm.

![image](../assets/f35aa7a55bc04590.png)

By the Conway’s Law, too much collaboration is also how you get to highly-coupled monoliths that are hard to disentangle. Blurred team boundaries lead to blurred software boundaries. 

#### 2) X-as-a-service 🔌

This is when one team **uses software** provided to them by another team

As opposed to cooperation, X-as-a-service works more like a **consumer-provider **model: one team may provide their product to multiple other teams.

This style of communication is *healthy* because it is low effort and it keeps responsibilities separated. It is the typical mode in which *platform teams* operate.

#### 3) Facilitating 🧑‍🏫

Facilitating occurs when one team **needs assistance** or knowledge from another team.

It is the default mode in which *enabling teams* operate. They share expertise, but the receiving teams retains the end-to-end responsibility of their product.

This is healthy, too, because it leads to team growth and boundaries are clear. 

### 📌 Luca’s takeaways

---

So, you may wonder how you can apply this framework to improve your teams.

In the book there are plenty of case studies about real companies that where *transformed *by these ideas, so, if you want to learn more, I encourage you to pick them up.

Personally, here are the main lessons I took from the book, the ones that I could apply directly to my teams:

#### 1) Relentlessly cut down cognitive load ✂️

Cognitive load is the lens through which the whole framework has been developed.

The first step to act on it should be to **assess** **it**. You can do so by having good conversations with your team: how hard does it feel to write software? What are the biggest bottlenecks and time wasters? What would make your job easier?

At scale, you can also run a survey to get quantitative feedback. This doesn’t replace conversations, but I am a fan of collecting both *qualitative* and *quantitative* feedback. Surveys are also useful because you can run them periodically and spot trends. 

Overall, this is similar to what we discussed about **wellbeing metrics** a couple of weeks ago 👇

[https://refactoring.fm/i/117405036/wellbeing-metrics](https://refactoring.fm/i/117405036/wellbeing-metrics)

Once you have a clear picture of where you stand, go for the improvements suggested at the beginning of the article: improve DX, split teams, make good tech choices, etc.

#### 2) Seek strong ownership 🏅

In Team Topologies, good teams are about ownership and clear boundaries. When boundaries *blur *and responsibilities are shared, that’s where the problems begin.

Authors strongly suggest to limit collaboration, by turning it into the two other interaction modes:

- 🔌 **Turn *****collaboration***** into *****x-as-a-service*** — *productize *otherwise bespoke dev work, so to 1) get clear ownership boundaries and 2) empower multiple teams.

- 🧑‍🏫 **Turn *****collaboration***** into *****facilitation***** **— rather than making teams permanently collaborate, *train* folks in stream-aligned teams so that they can be eventually independent. When training around some skills comes up often, create *facilitating teams* for them.
