---
aliases:
  - "Monday #147"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-monday-idea|Publish Monday Idea]]"
Status: Published
"👓 Status": Not started
"Created time": "2025-03-11T09:30:00.000Z"
Date: 2025-03-17
"Has Notes":
  - "[[evergreen/what-to-use-web-data-for|What to use web data for]]"
  - "[[evergreen/just-keep-building-because-building-is-a-muscle|Just keep building – because building is a muscle]]"
  - "[[evergreen/divergence-convergence|Divergence & Convergence]]"
  - "[[evergreen/large-codebases-is-the-1-problem-for-ai-coding|Large codebases is the #1 problem for AI coding]]"
Tags:
  - Monday
  - Free
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 1b3bdf02-815c-8032-a839-c6ad9d7f5c37
---

# Monday #147

### 1) 🗺️ Ship projects through divergence + convergence

How do you ship stuff on time? The #1 advice from Agile is 1) break down work in small pieces, and 2) get frequent feedback.

In my experience, though, this isn’t enough.

For any non-trivial project, there is additional work that spawns over the course of it. Most comes from feedback: other features you find out you need, tweaks, bugs, etc.

This is healthy — in fact, you should get suspicious when it *doesn’t* happen: chances are you are not getting enough feedback.

However, scope creep can easily derail deadlines and create friction on prioritization. To avoid this, you can break down the project timeline into timeboxed stages. For example:

1. 🥇 **50%** → Core features

1. 🥈 **30%** → Learnings + secondary features

1. 🥉 **20%** → More testing + bug fixing + final tweaks

So, let’s say you have a 6-month project for which you are working on scope and requirements. Start by identifying a subset of core features, on which to spend the first three months. After three months, look at the project status: are you on track? Are you late? How much new stuff has emerged?

![image](../assets/1b3bdf02815c805d.png)

You have now a backlog with:

- 🧀 **Leftovers** — a few core items still to complete.

- 🥈 **Secondaries** — all the minor features.

- 🔍 **Learnings** — tweaks and additional features that came from the learning and feedback over these first months.

Together with stakeholders, re-prioritize these and figure out what to fit in the next two months. Finally, in the last month, focus on *convergence*:* *do the final tweaks, more QA, and bug fixing.

Some FAQs:

- 🌊 **Isn’t this waterfall-ish?** — Nope, you are still demoing stuff every week, testing, getting feedback, etc. It’s just that you do the most important items first, and timebox the various stages.

- ⚖️ **What if my core features take more than 50%?** — go for it, but be aware of what you are leaving on the table. In my experience you can’t really avoid the final tweaks, so, if you want to stay in time, you are likely penalizing tasks that come from learning. Which is usually not a good deal.

I wrote a massive *guide *on how to plan and execute software projects last year, which is one of the most popular Refactoring articles ever 👇

[https://refactoring.fm/p/how-to-plan-and-execute-projects](https://refactoring.fm/p/how-to-plan-and-execute-projects)

---

### 2) 🔨 Building is a muscle

These days we see more and more people throwing themselves at improbable side projects thanks to AI — like Pieter Levels and his flight sim (which makes $70K/mo 🫠).

If you are thinking to do the same but don’t know where to start, the best advice is probably to… just start. With whatever.

Because **building is a muscle: **the more you build, the better you get at building, in many ways:

- 🔨 **Skills** — you get more *skilled.* You learn more tools, languages, and you get faster overall.

- 🧠 **Mindset** — You get used to spending time building ideas on the side. You develop *discipline*, and it just becomes a habit. Like going to the gym.

- 👓 **Sensitivity** — You start looking at things with new *lenses*, through which every problem is an opportunity to build something. The more you build, the more you find things to build.

So, if you are just getting started, here is my bottom line advice:

- 🩹 **Scratch your own itch** — find a problem *you* personally have and you think you can solve with tech. You may eventually find others who have the same problems, but even if you don’t, hey, it’s one less problem anyway!

- 🌶️ **Use the tech you know + some interesting new bits** — use 80% of stuff you are familiar with, but spice things a bit by adding some pieces you want to learn. This will work as an extra motivation, while not putting the whole project at risk.

- ☀️ **Enjoy the journey** — find ways to work on your project that don’t disrupt your life, and always pay attention to how you feel. It should feel good. Optimize for enjoying the process, rather than getting to a specific destination (e.g. I’ll make a ton of money!).

I wrote more about side projects in a previous article which takes from my chat with [Vic Vijayakumar](https://x.com/VicVijayakumar) — principal engineer at Twilio and… side-project *master 👇*

[https://refactoring.fm/p/how-to-build-side-projects](https://refactoring.fm/p/how-to-build-side-projects)

---

### 3) 🕷️ Should you collect web data? 

Because of AI, scraping and web data extraction are having an incredible reinassance.

AI lets companies *make sense *of a lot of data that was already available but not easy to take advantage from — and much of this data comes from the web.

Can such data be useful for you as well? Let’s see.

In my experience, use cases for web data can be split into two categories:

- ➡️ **Direct **— specific usage that is directly connected to the value prop of your product.

- ⬅️ **Indirect **— second-order benefits, more generic and widely applicable.

Direct uses cases are about products that create value by aggregating, summarizing, reviewing, and generally *transforming* web data. There is plenty of them — think of:

- Search engines in the travel space, like Skyscanner or Kayak.

- E-commerce aggregators, similar to Google Shopping

- SEO tools, like Ahrefs or Semrush

These are all ad-hoc use cases. You can find similar strategies by reflecting on your product and whether it can deliver more value by using web data directly.

There are also other, more general use cases, that work well for many companies:

#### **1) Security 🔒**

You can intercept emerging security risks by tapping into **threat intelligence feeds** (e.g. here is a [great list](https://github.com/hslatman/awesome-threat-intelligence?tab=readme-ov-file)), government alerts, and industry news on the web.

Based on your business, there is a lot you can anticipate, prevent, or mitigate this way: tech vulnerabilities, phishing attempts, data breaches, stolen information, and more.

For example, financial institutions monitor dark web forums for mentions of stolen credit card numbers, allowing them to proactively alert customers and prevent fraud.

#### 2) Market & competition insights 📈

Web data is a treasure trove of information about your market and competitors. For some businesses, this doesn’t really move the needle, while for others it’s crucial. 

Think of e-commerce stores:

- 🏷️ **Dynamic pricing **— you can harness data from competitors' websites, product pages, and deal sites to inform your pricing decisions.

- 🚀 **Track product launches **— keep tabs on new product announcements that are relevant to you (e.g. new products you can sell).

- 😊 **Analyze customer sentiment **— gather and analyze customer reviews and ratings across various platforms to understand market trends.

#### 3) Brand health & customer support 🩺

You can monitor your brand’s health through social media analysis, online reviews and ratings, gaining insights into brand perception.

The same approach can be adopted to intercept issues and provide proactive customer support. For example, that’s what many telcos do to spot issues in their network.

#### 4) Building AI models 🤖

Finally, AI stands out as a *meta* use case. You can use web data to fine-tune base models or create RAG systems for a variety of use cases, including the ones above. We also discussed it in this [previous article](https://refactoring.fm/p/how-to-integrate-llms?utm_source=publication-search).

We wrote a full piece about web scraping fundamentals last year 👇

[https://refactoring.fm/p/fundamentals-of-web-scraping-use](https://refactoring.fm/p/fundamentals-of-web-scraping-use)

---

And that’s it for today! If you are finding this newsletter valuable, consider doing any of these:

**1) **🔒** Subscribe to the paid version** — if you aren’t already, consider becoming a paid subscriber. 1500+ engineers and managers have joined already! Learn more about the [benefits of the paid plan here](http://refactoring.fm/about).

Get full access to Refactoring ✨

[https://refactoring.substack.com/subscribe](https://refactoring.substack.com/subscribe)?

**2)** 🍻 **Read with your friends** — Refactoring lives thanks to word of mouth. Share the article with your with someone who would like it, and **get a free membership** through the new [referral program](https://refactoring.fm/p/referral).

Read with your friends 🍻

[https://refactoring.fm/leaderboard](https://refactoring.fm/leaderboard)

I wish you a great week! ☀️

Luca
