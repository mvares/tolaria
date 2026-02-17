---
aliases:
  - "The Three Stages of Engineering Teams"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-essays|Publish Essays →]]"
Status: Evergreened
URL: "https://refactoring.fm/p/the-three-stages-of-engineering-teams"
"👓 Status": Not started
"Created time": "2024-04-18T14:53:00.000Z"
Date: 2021-08-05
"Has Notes":
  - "[[evergreen/from-the-platforms-to-products-stage|From the “platforms” to “products” stage]]"
  - "[[evergreen/the-platforms-intermediate-stage|The “platforms” intermediate stage]]"
  - "[[evergreen/when-you-are-starting-up-just-hire-generalists|When you are starting up, just hire generalists]]"
  - "[[evergreen/generalists-platforms-products-teams|Generalists → Platforms → Products Teams]]"
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: f11787e0-7d2f-46e9-aad7-151f72132b23
---

# The Three Stages of Engineering Teams

1. **What is the most important point?**

1. **Why is that the most important point? *****(what can you achieve with it)***

1. **Why should people care? *****(what's the benefit)***

1. **What is the easiest way to understand the most important point?**

1. **How do you want the reader to feel?**

1. **What should the reader do next?**

1. **The Three Qualities (*****pick 2+*****)**

###  📑 Materials

---

[Untitled](https://www.notion.so/0b8151df8fe74c6589bbd1e6fd1f79ba) 

[Untitled](https://www.notion.so/badf980abe4c4a3185fa7a82d9b62d76) 

- Disagree with Sahil

### ✍️ Post

---

[Mike Krieger](https://twitter.com/mikeyk), co-founder & CTO of Instagram, believes there are three major growth stages an engineering team goes through.

These are crucial moments in the wider company evolution, and largely match my own experience at a [fast-growing startup](https://www.crunchbase.com/organization/wanderio) first, and a [larger company](https://translated.com/) later.

He called them:

1. 🃏 **Generalists**

1. 🧱 **Platforms**

1. 🧩 **Products**

Each of them represents a different way to organize teams and engineering work within your company.

Let's see them one by one 👇

### 🃏 Generalists Stage

This happens when you are just starting up and your team is roughly **under 10 people**. 

At this stage you are still **figuring out what to build** and how to build it. You can't really anticipate what you will be doing, both in terms of actual tasks, and tech you will be using.

#### Team

For this reason, it is wise to surround you of **generalists** who are happy to do pretty much anything.

These are curious people** **— they don't bother about **switching technologies**, mixing them with no-code tools, and do whatever it takes to deliver the product. 

Even more so, they *thrive* doing it.

On the other side of the spectrum, you probably don't want someone who is **heavily invested** in some specific technology, as they will try to use it no matter what, because they feel their career depends on that.

Finally, generalists are more likely to make for good managers down the line, as they develop systems thinking by working on a wide array of activities.

#### Technology

As a rule of thumb, you should expect everything you build at this stage to be **scrapped** at some point in the future. This is almost inevitable as you 1) try many different things to see what sticks, and 2) you move really fast.

So my advice is:

- Don't create [**premature abstractions**](https://refactoring.fm/p/the-true-meaning-of-technical-debt/comments#comment-2365661)

- Make full use of [**no-code / low-code**](https://refactoring.fm/p/the-best-no-code-tools-you-should)[ ](https://refactoring.fm/p/the-best-no-code-tools-you-should)[**tools**](https://refactoring.fm/p/the-best-no-code-tools-you-should)

### 🧱 Platforms Stage

As your team grows, you get to a point where the *generalists* stage breaks, usually for two reasons:

- 📣 **Communication** — in a larger group of people, “everyone does everything” makes it hard to organize work properly.

- 📚 **Skills **—** **technology becomes more complex and it requires specific skills to move forward.

The most natural choice at this stage is to organize your engineering team into layers/platforms based on your tech stack — e.g. Frontend + Backend.

Separating layers helps to build engineering culture and practices, and slowly makes your team shift from generalists to specialists.

[Embed](https://twitter.com/lucaronin/status/1350025856354308096?s=21)

It also allows for an easy chain of reporting where you identify a *lead* for each layer and make them implement the first management behaviors (e.g. 1:1s).

#### Feature Teams

In a team organized by platforms, complex features are delivered by **Feature Teams**. 

These are cross-functional teams assembled with the purpose of delivering a specific feature, and dismantled later.

![image](../assets/3bb9193135ca4bbb.png)

My feeling about Feature Teams is they are a **necessary evil **in between the *generalists* and the *product* stage.

Feature Teams have two major pitfalls:

- **Product ownership **— being temporary, teams retain little ownership of what they build. This in turn makes it harder to 1) properly iterate on features and 2) develop product expertise over time.  

- **Resource allocation **— while it is a flexible way to work, it also requires continuous negotiation between stakeholders to define what is the best way to allocate engineers. 

![image](../assets/b9ce50d9b84b4d36.png)

### 🧩 Products Stage

At some point, the overhead brought by *feature teams* becomes unnecessary and it gets more convenient to create stable teams working around different **product areas**.

This change is enabled by two trends:

- 👥 **Your headcount is larger** — so you are physically able to split people into more groups than just *layers*.

- ⛰️ **Your product gets more stable **— so you can identify areas that require continuous work, and you are comfortable in allocating fixed resources to them.

With respect to *platforms*, this organization brings mostly upsides, with a few downsides:

- ➕ **It builds ownership **— teams retain strong ownership of their domain and improve their knowledge over time. You are also able to define KPIs and make teams work towards goals, which is great.

- ➕ **Easy work planning** — each team is responsible of the evolution of its product area, so there is no more continuous negotiation over who works on what.

- ➖ **Harder to ship cross-team initiatives **— since teams are built to be independent, it may become harder to collaborate on a larger initiative that spans multiple teams.

- ➖ **Reporting is trickier **— chain of reporting becomes less obvious, as you have multiple ways to organize [responsibilities of PMs, tech leads and engineering managers](https://refactoring.fm/p/the-role-of-tech-leads-and-engineering).

This stage is usually perceived like the *endgame* of engineering teams, and many people I know are anxious about doing it right, and doing it at the right time. 

However, my experience is that when the time comes it just feels like a natural step. You will already have people who have been working on an area for some time, who are recognized as experts on that. So product teams mostly **formalize what is already implicit**.

If it doesn’t feel natural, maybe the time isn’t right and you can stay with platforms a little longer.

### 📚 Resources

- 🌀 [**Feature Teams vs Durable Teams**](https://refactoring.fm/p/feature-teams-vs-durable-teams-)** **— if you want to learn more about the differences between feature teams and durable product teams, I wrote a full article about them a few months ago.

- 📑 [**How Instagram Co-founder Mike Krieger Took Its Engineering Org from 0 to 300 People**](https://review.firstround.com/how-instagram-co-founder-mike-krieger-took-its-engineering-org-from-0-to-300-people)** **—** **this interview inspired me to write this article. I took many ideas from it and I recommend you to read it for more great insights.

- 📹 [**Life of a Startup CTO**](https://docs.google.com/presentation/d/1q6SoSGrTo-dCMCrsrk0P1LrT-G22s9fys1aOoIJ6Ssg/edit#slide=id.gda14be6869_0_25)** **— this is a presentation I gave to an entrepreneurship class a few months ago. It builds on the same topics, also discussing your responsibilities as a CTO and the stages of your business.

### ⭐ Weekly Featured Jobs

Here are the **remote engineering** jobs featured this week! They are all from great companies and I personally review them one by one.

1. 🆕 **A Team** — [Independent Software Developer ($130-190/hr)](https://pallet.xyz/list/refactoring-jobs/job/ba420447-46c3-45d1-aaed-8b96fb4b0728) — professional network for A-Talent to connect and form full-stack teams.

1. **Sermo** — [Senior Backend Engineer](https://pallet.xyz/list/refactoring-jobs/job/2fd8d07f-dc55-47d4-8e47-f5d1cfa9762d) / [Senior Frontend Engineer](https://pallet.xyz/list/refactoring-jobs/job/5f91ff17-484e-4c87-a740-217731d6995b)— *the social network for doctors.*

1. **Companion** — [Senior Backend Generalist](https://pallet.xyz/list/refactoring-jobs/job/d0384959-1b47-46f5-99f8-c1d15e9174e2) — *transformative learning experiences for your dog.*

1. **Tidelift** — [Senior Software Engineer](https://pallet.xyz/list/refactoring-jobs/job/64a4118e-813b-489a-93b1-5ad7ee0efd28) — *a managed open source subscription, backed by creators and maintainers.*

1. **Everli** — [Backend Engineer (PHP, Laravel)](https://pallet.xyz/list/refactoring-jobs/job/0ad43a07-b34c-40bc-b58f-98dc645d67f5) — *get groceries delivered to your home, from all supermarkets.*

1. **River** — [iOS Engineer](https://pallet.xyz/list/refactoring-jobs/job/4257a985-1c2c-49cd-92da-e9544a9c0e7f) — a *primary and behavioral health plan to deliver real peace of mind.*

1. **Candor** — [Software Engineer, Infra / Backend / Fullstack](https://pallet.xyz/list/refactoring-jobs/job/c9229417-e697-414a-b156-525195bd7765) — *the way top tech employees manage their RSUs.*

1. **Catawiki** — [Senior Back-end Developer](https://pallet.xyz/list/refactoring-jobs/job/55afd81b-db9f-4aea-a57a-d049b75173f2) — *the online marketplace with weekly auctions.*

1. **Pallet** — [Full-Stack Software Engineer](https://pallet.xyz/list/refactoring-jobs/job/fabc980d-b4b7-479c-b9c0-c9785fe8cd6f) — *infrastructure for modern hiring.*

1. **Secureframe** — [Full-Stack Software Engineer](https://pallet.xyz/list/refactoring-jobs/job/f36f69fd-d2de-4ce0-aa05-2bdc638a534d) — *it helps companies to streamline their security compliance.*
