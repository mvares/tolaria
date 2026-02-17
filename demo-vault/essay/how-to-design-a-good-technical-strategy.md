---
aliases:
  - "How to Design a Good Technical Strategy 👁️"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-essays|Publish Essays →]]"
Status: Evergreened
URL: "https://refactoring.fm/p/how-to-design-a-good-tech-strategy"
"👓 Status": Not started
"Created time": "2024-04-18T14:53:00.000Z"
Date: 2021-09-02
"Has Notes":
  - "[[evergreen/tech-strategy-is-based-on-three-elements|Tech strategy is based on three elements]]"
  - "[[evergreen/there-are-two-levels-of-strategies|There are two levels of strategies]]"
  - "[[evergreen/good-tech-strategy-is-a-superpower|Good tech strategy is a superpower]]"
  - "[[evergreen/tech-strategy-is-a-plan-and-a-conversation|Tech strategy is a plan and a conversation]]"
  - "[[evergreen/tech-leads-need-strategy-skills-other-than-execution|Tech Leads need strategy skills other than execution]]"
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: ac6f9cc1-0b98-4faa-9319-390c58496f2d
---

# How to Design a Good Technical Strategy 👁️

1. **What is the most important point?**

1. **Why is that the most important point? *****(what can you achieve with it)***

1. **Why should people care? *****(what's the benefit)***

1. **What is the easiest way to understand the most important point?**

1. **How do you want the reader to feel?**

1. **What should the reader do next?**

1. **The Three Qualities (*****pick 2+*****)**

### 📑 Materials

---

[Untitled](https://www.notion.so/7b85f991b31f4470a623152c572a9be8) 

### ✍️ Post

---

A few months ago I wrote an article about the different [role of tech leads and engineering managers](https://refactoring.fm/p/the-role-of-tech-leads-and-engineering). After that, several people wrote me to tell their experience, and asked for advice about their responsibilities and career path.

I find it very hard to give good advice about leadership roles in tech. The same role can be very different in different companies — and also in different teams within the same company. 

In software, I feel we are still figuring out what the various **skills** and** responsibilities** really are, and we keep adjusting roles and tracks accordingly.

For instance, there is now a healthy conversation about separating **management** from **individual contribution **career paths. However, even within the IC track, you eventually grow into technical leadership roles, which mostly require a different set of skills.

So much that [Pat Kua](https://twitter.com/patkua) argues that the dual model for engineering careers should actually be a [*trident*](https://www.thekua.com/atwork/2019/02/the-trident-model-of-career-development/)[ model](https://www.thekua.com/atwork/2019/02/the-trident-model-of-career-development/), where you have three routes:

As all careers start with pure IC, you can either transition into an Engineering Manager, or a Tech Lead (or Lead Developer, Principal Engineer, etc.).

While the move to management is now relatively well-documented, what is it that really separates pure ICs from Technical Leaders? 👇

### Your job as a technical leader

As a Tech Leader of various kinds, your duties can be divided in two big categories:

1. Working with your **engineering team**

1. Working with **non-technical stakeholders**

The first is more of an evolution of your execution skills — you get to make design decisions, guide development and review other engineers' work. 

The second is a different beast — you will discuss and negotiate technical requirements, risks, and the overall **technical direction** of your team/product, with stakeholders coming from other functions. 

In this context, your focus shifts from **how** things should be built* *to **what** should be built and **why***. *That is, you move from technical** **execution to technical** **strategy.

But what is a **technical strategy** and how can you design one?

### What is a technical strategy

The technical strategy of your company is the plan of how engineering enables the product and company strategy, and drives them forward.

In the best companies, this doesn't happen strictly top-down, but more as a **conversation**. 

Product and engineering are **mutually influenced** — many of the most successful products of all times where in fact enabled by engineering breakthroughs.

- 📱 Famously, Steve Jobs was shown a prototype of a multi-touch screen and *then* decided they could build a phone with it. 

- 🎧 Spotify decided to go all-in on mobile because it was the right choice business-wise *and* it was finally technically viable (encoding + buffering tech + mobile networks performance).

### A good technical strategy is a superpower

Think at **engineering as a mini-company** within you company. As your mini-company, it requires a vision, a mission, and a plan to make it happen. 

A good technical strategy can do wonders to all aspects of your work:

- 🔋 **Empower product and business **— it enables new opportunities and creates competitive advantage over time.

- 💬 **Establish clear communication** — planning and negotiation become easier when they start from an agreed, high-level direction.   

- 📣 **Engage Engineers **— it provides a clear purpose that rallies people and motivates them.

### How to design a technical strategy?

The [Reforge](https://reforge.com/) guys wrote [a fantastic article](https://www.reforge.com/blog/overcome-the-tech-strategy-spiral) about the same topic, arguing there are two levels of strategy:

- **Company Strategy **— the logical plan you design to bring your company’s mission into being.

- **Functional Strategy **— the logical plan for how a specific function (product, engineering, marketing, etc.) will drive its part of the company strategy.

Functional strategies are influenced by one another about what can be done, they all contribute to the overall company strategy, and eventually to the roadmap.

![image](../assets/1e0f9129a32e41c7.png)

When it comes to Engineering, you can design your strategy by reflecting on three elements:

1. 🏢 **Your Company**

1. 📱 **Your Product**

1. 👕 **Your Team**

#### 🏢 Your Company

What can engineering do to support your **company mission**? What should you invest in to create a **core asset **for your company, generating a hard-to-copy, **competitive advantage**?

Examples:

- **Zoom** invested early in custom, state-of-the art [streaming technology](http://highscalability.com/blog/2020/5/14/a-short-on-how-zoom-works.html), which turned into a moat for their business.

- **Airbnb** invested early in [machine learning](https://news.airbnb.com/sharing-more-about-the-technology-that-powers-airbnb/) to support both guests' (*search & discovery*) and hosts' (*smart pricing*) experience.

#### 📱 Your Product

How can engineering support your **product strategy** to deliver a superior experience that drives the company mission forward? 

What kind of products can be **enabled** by a strong technical strategy?

Example:

- **Uber** invested in a general purpose fulfillment platform, which down the line enabled the creation of [multiple product lines](https://www.uber.com/newsroom/go-get/), like Uber Eats and Uber Freight.

#### 🎽 Your Team

Finally, the best strategy doesn't exist in isolation, it depends on your team and evolves with it.

How can you leverage your engineering **team's strengths** to create something that benefits your company long term?

**Airbnb** famously took a big bet on [React Native](https://reactnative.dev/) in 2016, but ended up sunsetting it in 2018. In a long and articulate [retrospective](https://reactnative.dev/) they acknowledged their issues where mostly operational — like already having a large team of native mobile developers.

Native developers were reluctant to 1) learn a new framework that changed the way they work, and 2) having to maintain a complex, hybrid approach between the old and the new.

React Native might have been a good choice in isolation, or to start with, but it failed because of Airbnb's team configuration and pre-existing assets.

### 📚 Resources

- 📑 [**How to Overcome the Technical Strategy Spiral**](https://www.reforge.com/blog/overcome-the-tech-strategy-spiral)** **— this great article by Reforge explains how to shift your skills from execution to strategy, and how to create a technical strategy from scratch.

- 📑 [**The Trident Model of Career Development**](https://www.thekua.com/atwork/2019/02/the-trident-model-of-career-development/)** **— [Pat Kua](https://twitter.com/patkua) argues the best model for Engineering career development is not the classic dual track, but a *trident* that separates Technical Leadership from pure Individual Contribution. Thoughtful and recommended.

- 📑** **[**React Native at Airbnb**](https://medium.com/airbnb-engineering/react-native-at-airbnb-f95aa460be1c)** **— long post-mortem of the failed attempt, lasted 2 years, to introduce React Native into the mobile stack of Airbnb. This is the best piece you can read about what does it mean to deploy a strategic tech initiative into a large, modern company, with its challenges and opportunities. 

### ⭐ Weekly Featured Jobs

Here are the **remote engineering** jobs featured this week! They are all from great companies and I personally review them one by one.

1. **Pager** — [Senior Software Engineer](https://pallet.xyz/list/refactoring-jobs/job/a37dac23-ac6a-4e53-9243-2567aa97f993) — *the best way to capture and share your digital life.*

1. **Journey** — [Founding Frontend Engineer](https://pallet.xyz/list/refactoring-jobs/job/31bc6537-7db9-4517-bd50-3b27ea8984cc) — *a storytelling tool designed for the internet age.*

1. **Zapier** — [VP Platforms & Labs](https://pallet.xyz/list/refactoring-jobs/job/518b0188-6975-4877-bf47-819146599b71) — *the easiest way to automate your work*

1. **Hubspot** — [Director of Engineering, Fintech](https://pallet.xyz/list/refactoring-jobs/job/8a28c8f2-efd3-462e-ba58-d2748d5e2210) — *inbound marketing, sales and service software*

1. **Stripe** — [Staff Engineer, Product Experience](https://pallet.xyz/list/refactoring-jobs/job/8885d449-0fbf-49e2-a262-aa96c0e4999e) — *online payment processing for internet businesses*

*Browse many more open roles (or add your own) on the full board* 👇
