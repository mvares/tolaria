---
aliases:
  - "The Operating Cost of New Features"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-essays|Publish Essays →]]"
Status: Everpictured
URL: "https://refactoring.fm/p/the-operating-cost-of-new-features"
"👓 Status": Not started
"URL 2": "https://twitter.com/lucaronin/status/1368955895649034255"
"Created time": "2024-04-18T14:53:00.000Z"
Date: 2021-03-05
"Has Notes": "[[evergreen/minimize-features-operating-cost|Minimize features’ operating cost]]"
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 4e8424a3-ebda-4fa5-ba52-40340e84ff85
---

# The Operating Cost of New Features

1. **What is the most important point?**

1. **Why is that the most important point? *****(what can you achieve with it)***

1. **Why should people care? *****(what's the benefit)***

1. **What is the easiest way to understand the most important point?**

1. **How do you want the reader to feel?**

1. **What should the reader do next?**

1. **The Three Qualities (*****pick 2+*****)**

### 📚 Relevant Research

---

- [https://www.eferro.net/2021/02/basal-cost-of-software.html?utm_campaign=tmw-ctocraft&utm_medium=email&utm_source=Revue newsletter](https://www.eferro.net/2021/02/basal-cost-of-software.html?utm_campaign=tmw-ctocraft&utm_medium=email&utm_source=Revue%20newsletter)

- [https://medium.com/@johnpcutler/how-much-does-a-new-feature-cost-f93c82bf638f](https://medium.com/@johnpcutler/how-much-does-a-new-feature-cost-f93c82bf638f)

- [https://www.reforge.com/blog/growth-metric-acquisition-monetization-virality](https://www.reforge.com/blog/growth-metric-acquisition-monetization-virality)

### 📋 Outline

---

If you work on a digital product, chances are you are familiar with *Retention*.

Retention stands for the continued use of a product (or feature) by your customers. Good retention improves monetization, lowers acquisition costs, and gives you an edge over competition.

One of the most popular ways of studying Retention is by **cohort analysis**.

Such method groups users by batches of time (typically days, weeks, or months) based on their first interaction with the product, and shows how these *cohorts* stay engaged, displaying the share of users that continue using the product over time.

![image](../assets/706a830bc0bf4f25.png)

But you may ask — why are we talking of retention and cohorts?

### 📈 Feature Costs and Retention 

In many ways, the retention distribution is similar to the way development costs behave. 

For each feature, you can roughly divide such costs in two steps:

- **Delivery Costs** — costs you sustain to develop the feature until the first deliverable.

- **Operating Costs** — costs you sustain to maintain and evolve the feature, until...forever! 

If you work in small batches and iterate fast ([which you should](https://refactoring.fm/p/the-four-measures-of-software-delivery)), the line between these two steps is blurred, but the costs follow a predictable distribution nevertheless. They go from being higher before delivery, to being lower over time when your team moves on to new initiatives.

![If you don't plan properly, operating costs are going to kill your team's capacity over time  ](../assets/57b9a94fcf844f69.png)

Here comes the obvious difference with retention: over time, good products want to keep retention high. **Good engineering wants to keep such costs low**.

In particular, good design should minimize *both* delivery and operating costs. And I would argue that, out of the two, it's vastly more important to minimize operating costs, as they — in contrast with delivery costs — compound over time with those of other features.

Just like good retention makes companies thrive by making customers come back, bad operating costs may sink it, by taking up most of your team capacity.

### 🏃 **Operating** Costs

In my experience, the bulk of operating costs, for any feature or product area, is spawned by three elements:

1. 💼 **Business changes**

1. 🐛 **Bug fixing**

1. 🔨 **Tech Maintenance**

Let's see them more in detail, together with strategies to minimize them.

#### 💼 Business Changes

**Feature updates and changes prompted by business needs**. 

The frequency and magnitude of these depends on the market and the environment you are in — whether you are in a fast growing startup, a consolidated business, or anything in between

Frequent changes lead to misalignment between what business needs and what the code represents, that is the [true nature of technical debt](https://refactoring.fm/p/the-true-meaning-of-technical-debt).

🎯 **Strategy**

- **Invest more time on design **— To reduce the impact of such changes on your development costs, invest time in understanding *both *the current requirements, and potential evolutions. Spend time with stakeholders to map the possible scenarios, and create your design accordingly.

####  🐛 Bug Fixing

**Time spent on regressions and mistakes made by developers.**

Mistakes are inevitable. The best strategy to minimize their impact is to catch them *early* and *frequently*.

🎯 **Strategy**

- **Make your code safer **— To catch bugs *early*, you should invest in a proper testing pipeline. Based on your team and your codebase, you may also evaluate static typing over dynamic typing options (e.g. Typescript over Javascript). 

- **Invest in Continuous Delivery **— To catch bugs *frequently*, you should release frequently. Companies that work in small batches are also faster at recovering from regressions ([it's been proven](https://refactoring.fm/p/the-four-measures-of-software-delivery)).

#### 🔨 Tech Maintenance Costs

**Under the hood work related to the specific design or technologies.** Like scaling issues, framework and dependencies updates.

🎯 **Strategy**

- **Invest more time on design **— Just like for business changes, many issues can be solved upfront by better understanding what the business needed in the first place. Many scaling issues happen because developers *don't expect* something to need to scale, at all.

- **Minimize technology risk **—** **This often means:** **[choose boring technology](https://mcfunley.com/choose-boring-technology). For critical product parts, choose tech that is proven, well supported, and works (and fails) in a way that is well understood by your team. 

- **Buy instead of Make **—** **"Don't reinvent the wheel" it's a common advice to follow, but the reality is you should follow it *aggressively*. If you don't believe something should be a core asset for your company, then you should look out for a way to buying it, instead of making it.

### 📚 Resources

- [**The Basal Cost of Software**](https://www.eferro.net/2021/02/basal-cost-of-software.html?utm_campaign=tmw-ctocraft&utm_medium=email&utm_source=Revue)** **— this recent article by [Eduardo Ferro](https://twitter.com/eferro) greatly inspired my post, drawing a comparison between operating feature costs and the basal metabolic rate of human body. Recommended.

- [**How Much Does a New Feature Cost?**](https://medium.com/@johnpcutler/how-much-does-a-new-feature-cost-f93c82bf638f) — spoiler: more than you think. Great short post by [John Cutler](https://twitter.com/johncutlefish) that enumerates all the hidden costs caused by new features. It's one of those that should be printed and hung on the wall.

- [**The One Growth Metric that Moves Acquisition, Monetization, and Virality**](https://www.reforge.com/blog/growth-metric-acquisition-monetization-virality)** **— if the retention metaphor sparked your curiosity and want to learn more about retention itself, this is an amazing post by [Brian Balfour](https://twitter.com/bbalfour), one of the absolute OGs of product growth.

**And that's it for this week! What's your experience with maintaining features over time? Let me know in the comments or via email **📮** **
