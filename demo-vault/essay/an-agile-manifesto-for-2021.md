---
aliases:
  - "An Agile Manifesto for 2021"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-essays|Publish Essays →]]"
Status: Everpictured
URL: "https://refactoring.fm/p/agile-manifesto"
"👓 Status": Not started
"URL 2": "https://twitter.com/lucaronin/status/1417022306648461312"
"Created time": "2024-04-18T14:53:00.000Z"
Date: 2021-07-15
"Has Notes": "[[evergreen/the-four-values-of-agile-manifesto|The Four Values of Agile Manifesto]]"
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: cd359446-d1c6-4c6b-a25d-1acd0bb68f2d
---

# An Agile Manifesto for 2021

1. **What is the most important point?**

1. **Why is that the most important point? *****(what can you achieve with it)***

1. **Why should people care? *****(what's the benefit)***

1. **What is the easiest way to understand the most important point?**

1. **How do you want the reader to feel?**

1. **What should the reader do next?**

1. **The Three Qualities (*****pick 2+*****)**

### ✍️ Post

---

When I studied CS at university, I remember being told the mythical story of how the [Agile Manifesto](https://agilemanifesto.org/) was born.

These 17 people, closed in a chalet on the mountains, who spent a few days together and came up with the [12 principles](https://agilemanifesto.org/principles.html) that defined **software engineering culture** for the next two decades.

Aside from these *founding fathers* vibes, though, there are actually many things people get wrong when remembering this moment.

### 📜 Pre-Manifesto Era

For instance, many believe the manifesto led to the creation of the various **Agile methodologies** we are all familiar with. Actually, the opposite is true: *Scrum*, *Extreme Programming,* and others mostly *predate* the manifesto.

In fact, the manifesto was born out of the necessity of **putting order** into all these similar-but-different disciplines.

Why am I telling all of this? Because it seems to me today we are in a similar **pre-manifesto***** *****era**. Many people struggle at defining what *Agile* really means, while successful subcultures like *DevOps*, *Continuous Delivery*, or *Lean*, each cover only some parts of the original Agile scope, with overlapping principles.

So a few days ago I went back to the original manifesto — kind of how you go back to the Scripture — and drew some inspiration from it.

### 🔢 The Four Values

Reading the 12 principles today, they still feel very relevant. Which is already an incredible feat in such a fast moving industry.

But we also learned a lot in these 20 years, and we can probably reframe these principles today a little bit, in the light of such learnings.

![The original agile manifesto, with my annotations](../assets/222936675a3f4b20.png)

So I started annotating the principles, with the goal of extracting a few **major themes**. I chose the ones that were both the *most* *recurrent* in the manifesto, and I believe are the *most important *today.

Here they are:

- 👥 **Work closely with stakeholders**

- 🚚 **Work in small batches & deliver incremental value**

- 🏅 **Give teams agency**

- 🎨 **Promote simplicity and good design**

Let's explore each one and let me tell you why I believe these are the key takeaways from the Agile manifesto in 2021.

### 👥 **Work closely with stakeholders**

Good communication with stakeholders is a primary factor in any project's success. Agile has long preached about keeping customers in the loop and welcoming requirements' changes, over clunky long term plans.

This feels as relevant today as ever.

Startups move at super high speed and need to work closely with users to find product-market-fit. Larger businesses need to stay lean and react fast to market changes.

How do you know if you are doing it right? Ask yourself these questions:

- 🔍 **Are customers able to *****review***** new features? **Have you set up an effective feedback loop for your work?

- 📣 **Are customers able to *****suggest***** new features? **Are you in touch with what customers really want?

- 🏆 **Do you know what *****success***** looks like? **Have you set KPIs and targets for product success?

### 🚚 Work in small batches & deliver incremental value

Splitting work in small deliverables is key to the health of your development process.

Small batches lead to **frequent releases**, which in turn make the feedback loop faster and reduce risk.

This virtuous cycle means that, counterintuitively, there is no trade-off between speed and stability in software. **Higher speed brings higher stability**, because it also brings faster recovery from failures.

[Embed](https://twitter.com/lucaronin/status/1368827812858232833)

How do you know if you are doing it right? Ask yourself these questions:

- ⚡ **How *****fast***** can you release? **High performing teams deploy in production in *10 minutes*, and do it 10+ times a day.

- 🏃 **Do you iterate on features? **After a first version is delivered, do you take room for iteration? Not doing it leads to half-assed features all over the place, and turns the process from *agile* into a series of *mini-waterfalls*.

### 🏅 Give teams agency

A simple way to sort high-performing from low-performing teams is based on their *agency*:

- **Bad** teams are given **solutions** to implement.

- **Good** teams are given **problems** to solve.

- **Great** teams are given the **agency** **to find problems** and provide solutions.

The best results I have witnessed in software have always been delivered by diverse, cross-functional teams who had the skills and trust to independently iterate over a product.

The manifesto got this exactly right, also highlighting the key elements to make it happen:

- 🤝 **Trust **(point 5) — teams should have the agency to find both problems and solutions on their own.

- 🔄 **Self-organization **(point 11)** **— teams should be able to work independently and include all the skills needed to evolve the product.

- 🧘‍♂️ **Reflection **(point 12) — improvement is obtained through regular retrospective *within* the team.

### 🎨 Promote simplicity and good design

Out of 12 principles, it may seem weird that only two (9 and 10) talk explicitly about software design.

Good design means **minimizing the work to be done**, both right now and in the future, and this mostly comes from **good communication**. 

Technical excellence comes from **good understanding**, as much as [technical debt comes from the lack of it](https://refactoring.fm/p/the-true-meaning-of-technical-debt).

A few directions to get this right:

- ✍️ **Invest in design **— this means, of course, more engineering analysis, but also more talking with stakeholders. You should discuss both the here and now, and the future evolution of the project.

- 🙅🏻‍♀️ **Avoid premature abstractions** — when you have limited understanding and/or limited context into the future, stick with simple solutions that are easy to refactor once requirements become clear. Wrong abstractions are hard to remove and are the #1 source of tech debt. Even duplicating code is often better than a bad abstraction.

- 🧩 **Buy instead of make **— as platforms consolidate, there are less and less use cases where it makes sense to write custom code for your company. Building something with code should be your last resort, instead of your default solution. Take advantage of frameworks, no-code and low-code tools to reduce the tech footprint of your product.

### 📚 Resources

As you may know, I have written several articles in the past about this! Here are a few, organized by theme:

#### 👥 **Work closely with stakeholders**

- [**The Pyramid of Stakeholders**](https://refactoring.fm/p/stakeholders) — this article explores the relationship we have with the different types of stakeholders and provides advice on how we can communicate well with them.

- [**How to Design a Communication Architecture**](https://refactoring.fm/p/how-to-design-a-communication-architecture)** **— in 2012, Ben Horowitz wrote that a CEO’s most important duty is "to design a communication architecture for their company". This article provides a step-by-step approach based on responsibilities.

#### 🚚 Work in small batches & deliver incremental value

- [**The Four Measures of Software Delivery Performance**](https://refactoring.fm/p/the-four-measures-of-software-delivery)** **— this article explores how delivery metrics reliably predict wider business performance and benefit your company goals.

- [**How Shipping Fast Changes Your Life**](https://refactoring.fm/p/how-shipping-fast-changes-your-life)** **— shipping fast is truly one of the major areas that separate elite engineering teams from average and poor ones. Here is what happens to your team when you ship fast (or slow).

#### 🏅 Give teams agency

- [**Feature Teams vs Durable Teams**](https://refactoring.fm/p/feature-teams-vs-durable-teams-)** **— a reflection on various teams configurations through the lens of ownership, resource allocation and decision making.

- [**The Pyramid of Engagement**](https://refactoring.fm/p/the-pyramid-of-engagement-)** **— in over 80 years, Gallup defined a model for workers' engagement which is based on twelve needs across four categories. In the article I discuss them and provide a small framework to support them as leaders.

#### 🎨 Promote simplicity and good design

- [**The True Meaning of Technical Debt**](https://refactoring.fm/p/the-true-meaning-of-technical-debt)** **—  this article dives into the origins of this widely used metaphor, why it is often misunderstood, together with some battle-tested advice about how to deal with it in real world situations.

- [**The Best No-Code Tools You Should Use**](https://refactoring.fm/p/the-best-no-code-tools-you-should)** **— No-code tools have grown from being a cute option for non-technical folks, to an indispensable weapon for any startup and engineering team. This article includes a list of my favorite ones, organized by purpose and category.

### ⭐ Weekly Featured Jobs

Here are the jobs featured this week!

1. **Tidelift**: [Senior Software Engineer](https://pallet.xyz/list/refactoring-jobs/job/64a4118e-813b-489a-93b1-5ad7ee0efd28) (Remote)

1. **Candor**: [Software Engineer, Infra/Backend/Full-stack](https://pallet.xyz/list/refactoring-jobs/job/c9229417-e697-414a-b156-525195bd7765) (Remote)

1. **Catawiki**: [Senior Back-end Developer](https://pallet.xyz/list/refactoring-jobs/job/55afd81b-db9f-4aea-a57a-d049b75173f2) (Remote)

1. **Pallet**: [Full-Stack Software Engineer](https://pallet.xyz/list/refactoring-jobs/job/fabc980d-b4b7-479c-b9c0-c9785fe8cd6f) (Remote)

1. **Secureframe**: [Full-Stack Software Engineer](https://pallet.xyz/list/refactoring-jobs/job/f36f69fd-d2de-4ce0-aa05-2bdc638a534d) (Remote)  

1. **Solv: **[Full-stack Technical Lead (React)](https://pallet.xyz/list/refactoring-jobs/job/2ae5022d-3299-408a-9bfb-2b30308b1c10?n=Refactoring%20Jobs%20&r=%2Flist%2Frefactoring-jobs%2Fjobs) (Remote)

1. **Hatch: **[VP, Mobile Engineering](https://pallet.xyz/list/refactoring-jobs/job/ffcda8e6-c0cc-4c12-b7e6-a7c20ab4c47d?n=List%20Review%20&r=%2Flist%2Frefactoring-jobs%2Freview) (Remote)

1. **Gearflow: **[Full-stack Software Engineer, Marketplace](https://pallet.xyz/list/refactoring-jobs/job/ab9860a4-2c7e-4ada-8321-d767b61b50f2?n=Refactoring%20Jobs%20&r=%2Flist%2Frefactoring-jobs%2Fjobs) (Remote)

1. **Foster: **[Founding Lead Engineer](https://pallet.xyz/list/refactoring-jobs/job/b4af6b2d-65e8-4994-acfb-0cce55af0ff2?n=Refactoring%20Jobs%20&r=%2Flist%2Frefactoring-jobs%2Fjobs) (Remote)

*Browse many more open roles (or add your own) on the full board *👇
