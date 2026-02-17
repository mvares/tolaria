---
aliases:
  - "Does Scrum Make Sense in 2024?"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-essays|Publish Essays →]]"
Status: Evergreened
URL: "https://refactoring.fm/p/should-you-use-scrum-in-2024"
"👓 Status": Not started
"Date HH": 2024-12-05
"Created time": "2024-04-18T14:53:00.000Z"
Date: 2024-02-14
"Has Notes":
  - "[[evergreen/kent-becks-3x-model-for-product-maturity|Kent Beck’s 3X model for product maturity]]"
  - "[[evergreen/tuckmans-four-stages|Tuckman’s four stages]]"
Tags:
  - Updated
  - Mgmt
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 9461738f-8376-447e-b67f-c82e94a30230
---

# Does Scrum Make Sense in 2024?

### 📑 Materials

---

[https://www.youtube.com/watch?v=WazqgfsO_kY](https://www.youtube.com/watch?v=WazqgfsO_kY)

### ✍️ Post

---

Last month I started doing weekly interviews for the podcast. I have done four already, and one of the topics that come up the most frequently is **development process**.

For example, in the recent chat [with Aadil Maan](https://refactoring.fm/p/the-world-builder-framework-with), we discussed how the best teams often take *pieces* from canonical frameworks like Scrum or Kanban, and mix&match them to fit their needs.

Is this how you should think about frameworks? Or is it good, sometimes, to just trust the framework and slap it onto your team?

The answer is less trivial than it seems.

Two years ago I wrote [a full piece about Scrum](https://refactoring.fm/p/scrum-2022). I used Scrum for many years, at first almost religiously, then less and less so, until we could hardly call it Scrum anymore.

Then, since I started Refactoring, I had the chance of talking with countless managers and CTOs about their dev process and how it evolved over time. 

So, today we will try to connect the dots, and write an updated take on Scrum and, more in general, how to use frameworks for good.

Here is the agenda:

- 🔄 **The Role of Processes **— what we should expect from them.

- ⚖️ **Criticism to Scrum **— why people complain about Scrum.

- 🔨 **The *****Meta***** Dev Cycle **— a first-principles approach to what the dev cycles should do.

- 🎽 **Team Maturity **— how your team stage impacts what the best process looks like.

- 📱 **Product Maturity **— how your process should evolve alongside your product.

- 💬** Community Examples **— stories and processes from real-world companies

- 📌 **Bottom Line **— parting advice to summarize what we covered.

Let’s dive in!

---

### 🔄 The Role of Processes

A process is a repetitive series of actions you take in order to achieve a particular outcome. 

In the context of an engineering team, the *dev* process enforces a way of working on code and product that guarantees some quality.

What quality, though?

As Cate Huston [wrote](https://cate.blog/2022/02/28/low-process-culture-high-process-culture/), processes can only guarantee **adequacy**, rather than *excellence*. By definition, they are a mechanism of *standardization* — so their domain is that of **reliability**,** **rather than **greatness**.

And that’s ok. True greatness comes from people. As Will Larson points out:

> *With the right people, any process works, and with the wrong people, no process works.*

So, the best processes get two things right:

1. **Enforce the basics** — to guarantee *adequacy* and relieve people from decision fatigue.

1. **Stay out of the way** — to let people shine and create *greatness*.

How does Scrum fare on this?

### ⚖️ Criticism to Scrum

Scrum gets a lot of flak for many things these days. You can *organize* this criticism along two axes:

- **Overhead** — Teams complaining that it has too many ceremonies / it is too prescriptive.

- **Sprint duration** — Teams complaining that one or two weeks are not enough to deliver meaningful product features.

These angles are not orthogonal. For many teams, Scrum ceremonies are *correct*, but they become too much *because *they all happen on a single-week cycle — so you see all kinds of hybrids: fewer ceremonies + same short cycle, or same ceremonies + longer cycle, or anything in between.

And this is not specific to Scrum anymore: you can catalog pretty much all dev process frameworks based on 1) which ceremonies they include, and 2) how frequently you have them.

Differences can be radical. A normal Scrum process has *Sprints* that last either one or two weeks. Shape Up by Basecamp, instead, works on 6-week cycles. 

Are these even the same jobs?

To understand this better, let’s take a step back and look what you do on a cycle, at a *meta *level

### 🔨 The Meta Dev Cycle

A first question you may have is: should I work in cycles at all? After all, there exist frameworks—e.g. Kanban—which are more about continuous work.

For product development, my answer is an easy yes.

The main virtue of cycles is that they enable feedback loops — with customers, stakeholders, between developers, everyone. Feedback loops enable improvement and make sure you keep doing the right things. 

Product work is 1) inherently uncertain, and 2) involves many different stakeholders, which makes feedback crucial. 

Cycles and ceremonies are also important for managers to have reliable spots in which to take action. Without them, you would either end up 1) not working enough on problems, or 2) being on the alert all the time.

So what do you do on a cycle? At a team level, ceremonies revolve around three things:

- 🗺️** Planning **— deciding what to do next.

- 🔀** Coordination **— avoiding being stuck, removing obstacles.

- 🗳️** Feedback **— discussing how you are doing and how to get better.

This is of course, *meta *work — the actual work is writing code, creating requirements, releasing, etc — but still, it’s legit work. Every team needs to do these in one way or another, whatever framework they choose.

Here is what Scrum does about them:

- **Planning** → *Sprint Planning*, at the beginning of each Sprint.

- **Coordination** → *Daily Scrum*, everyday.

- **Feedback** → *Review* & *Retrospective*, at the end of each Sprint.

This may or may not work for you. You may want to do something *less often*, or something *more often* than that.

Let’s take a bi-weekly Sprint as an example. Here is some common criticism I hear:

- **Planning needs more time** — “*to deliver valuable product features we need longer cycles of planning*”.

- **Review should not happen at the end** — “*we review work continuously and need to release multiple times a day*”.

- **Retrospective is shallow** — “*two weeks are not enough to discover meaningful insights*”.

- **Daily Scrum is a burden** — “*most of the times coordination is easy and the ceremony feels like wasting time”*

These are not absolute pitfalls: any of these may or may not apply to you. This is where we may just throw hands up and say “*it depends*” — instead let’s go deeper and try to figure out on *what* it depends, with two ideas:

- **Team Maturity **— Tuckman’s four stages

- **Product Maturity** — Kent Beck’s EEE framework

---

### 🎽 Team Maturity

Bruce Tuckman, American psychologist and researcher, created a famous model for *group development*, describing the four main stages that teams typically go through as they work together:

1. ☁️** Forming** — team members are introduced and the team begins to establish its structure and roles.

1. ⛈️** Storming** — conflicts arise as individual agendas and working styles clash. Members may challenge the team's direction and each other's ideas.

1. 🌦️** Norming **— the team starts to resolve conflicts and develops a sense of cohesion. Team members begin to understand and respect each other's strengths and weaknesses, and they establish norms for how they should work together.

1. ☀️** Performing** — the team reaches its peak performance. Members are highly productive, motivated, and capable of working independently and interdependently.

When it comes to processes and cerimonies, the earlier the team is on the Tuckman’s scale, the  more it benefits from a prescriptive approach: you want to invest more on coordination, get feedback more frequently, and make short-term plans. This simply calls for more ceremonies and shorter cycles.

![image](../assets/36672c6c613247b2.png)

Conversely, consolidated teams, made of people who have been working together for a long time, can remove more guardrails, plan for longer, and focus on more deep work.

Standups are a perfect example of a ritual that largely depends on team maturity. Early teams might benefit from daily, sync standups in a meeting/call. Later they may switch to *async* written ones, and finally remove them altogether.

Team development is also one of the main reasons why it is tricky to look at others’ stories and apply them verbatim to your team. Even when working at a similar scale, and on a similar product, what works for others might not work for you based on their and your own maturity.

---

### 📊 Product Maturity

Last week I interviewed Kent Beck for the podcast (the full episode will come out on Friday).

Among other things, we discussed Kent’s own mental model about product maturity, which focuses on three stages (the three Xs):

1. 🔵** Explore** — you are in the search for what works. The goal is to minimize the cost of individual bets and spread small investments across a wide range of experiments. If one of these proves successful, it leads to the next phase. This is typical in startup early stages, before product-market fit.

1. 🔴** Expand** — the product experiences rapid growth and user adoption. You will encounter unanticipated issues and bottlenecks, and the primary goal is to address them to sustain growth. You may employ suboptimal solutions to keep the product alive and meet the increasing demand.

1. 🟢** Extract** — you have a clear understanding of the problem/solution space. The product has reached a stable level of high demand, and the focus shifts to efficiency, optimizing processes, and maximizing profits.

Borrowing a famous analogy by Nassim Taleb, these three stages unfold as you progressively move from a *convex* to a *concave *world:

- 📈** Convex world** — you have little to lose, while a single successful bet has the potential to turn your business around. In this context, the right way to play the game is to place as many bets as possible, keeping them cheap. You want to be able to keep playing the game until you find the successful idea.

- 📉** Concave world **— in a concave world, your business is steady and well understood, and the level of investments is already high. You have a lot to lose, and single bets have smaller potential. The right way to play the game is slow and thoughtful, maximizing the chance of getting things right.

So, different stages just call for different approaches.

We mentioned [Shape Up](https://basecamp.com/shapeup) before, which plans work in 6-week cycles. Shape Up is the framework that 37Signals uses to work on [Basecamp](https://basecamp.com/), their flagship product. 

Basecamp has been around for 20 years, makes a ton of money, and has stable growth. The company is privately owned, not VC-funded, and not in a rush for hyper-growth. 

In other words, Basecamp lives in a *concave *world, which rewards the slow and the thoughtful.

Conversely, if Basecamp was an early, pre-revenue startup, 6 weeks would be too much to push the next experiment out. You should probably make it cheaper, throw it at the wall in one week, and see if it sticks.

---

### 💬 Community Examples

Finally, here is a round-up of real-world ideas and processes from the community

**Livio Marcheschi** — *relay* approach between product and dev 👇

> *My approach with a new team is to start with (a sort of) SCRUM and then adapt.*

**Dobes Vandermeer** — two-week cycles and continuous discovery 👇

> *Currently we have a short team meetup three times a week, a 90 minute planning meeting every 2 weeks, a 60 minute retro every 4 weeks. 

We don’t use a sprint structure - discovery and delivery are basically continuous. So at the planning meeting it’s more about grooming the backlog and checking in on the big picture priorities.*

**Clemens Adolphs** — the challenge of using Scrum for research 👇

> *When I was fresh out of university and joined a startup as a “researcher/developer”, there was initially no framework (2015). Then we got a Scrum Captain who taught everyone about Scrum and Agile, and it all sounded so reasonable (compared to Waterfall).*

**Umberto Nicoletti** — a successful experience introducing Scrum 👇

> We just adopted Scrum for all the teams we could afford it, starting with the highest impact ones. The results so far are beyond my rosiest expectations (I too was skeptical at first), with lots of room for improvement still.

**Alex Buaiscia** — learnings from using Scrum for several years 👇

> *I worked with Scrum for the past 3-4 years projects. I saw the same methodology used over and over there.*

---

### 📌 Bottom Line

So, there is no universal process that works for every team. 

Different teams call for different approaches — and even the same team has evolving needs over time, as it goes through different stages.

Here are some heuristics you can follow:

1. **Optimize for smoothness **— Navy Seals say: “*slow is smooth, smooth is fast*”*. *In early teams, look for predictability before you look for speed. Remove bottlenecks, make sure nobody gets stuck, and slowly turn up the volume.

1. **Mix & Match **— don’t be adamant about frameworks. Take inspiration from different methods, take bits from here and there and create your own recipe. You can do Scrum without the dailies. You can have retrospectives only once every two Sprints. There are no sacred cows, find what works for you.

1. **Keep tweaking **— what works today might not work tomorrow, so never drop your guard. Keep talking with people, have good retros, and tweak the process whenever you see fit. So, if you have been sticking with the same process for years, chances are you can improve it.
