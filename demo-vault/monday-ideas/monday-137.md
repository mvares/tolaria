---
aliases:
  - "Monday #137"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-monday-idea|Publish Monday Idea]]"
Status: Published
"👓 Status": Not started
"Created time": "2024-12-31T08:55:00.000Z"
Date: 2025-01-06
"Has Notes":
  - "[[evergreen/how-to-collect-web-data|How to collect web data?]]"
  - "[[evergreen/should-on-call-be-mandatory|Should on-call be mandatory?]]"
  - "[[evergreen/pes-manage-the-whole-feature-management-workflow|PEs manage the whole feature management workflow]]"
Tags:
  - Monday
  - Free
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 16dbdf02-815c-8014-8d8c-fde5c9c61dee
---

# Monday #137

### 1) ⏰ Should on-call be mandatory? 

This is a question I get surprisingly often via email.

In my opinion, being on-call can be considered part of the duties of any engineer, so there is no wrong in making it mandatory.

Especially if you are introducing this from scratch, mandatory on-call for all engineers is healthy to build ownership and to make sure no critical areas of the code are left uncovered by docs and playbooks.

Eventually, however, consider making it *voluntary*. People may be more or less okay with being on-call depending on things like their family responsibilities. If the team is big enough and the process has been battle-tested for a while already, then it's probably best to let people choose if they want to do on-call.

I wrote a full piece on creating good on-call processes 👇

[https://refactoring.fm/p/on-call](https://refactoring.fm/p/on-call)

---

### 2) 🕷️ How do you extract web data? 

There are various ways to extract web data, on an ideal line that goes from *buy* to *build*. Most people are familiar with direct *scraping*, while for many use cases there are simpler and faster ways.

Here are the four main ones I know of:

![image](../assets/16dbdf02815c806f.jpg)

 

#### Ready-made datasets 🗃️

Several companies (e.g. [**Bright Data**](https://brightdata.com/cp/datasets/browse?id=hl_588e08b6), [**Oxylabs**](https://oxylabs.io/products/datasets), or [**Webz**](https://webz.io/datasets/premium-datasets)) offer pre-collected datasets on various topics. These datasets are pricey but also incredibly rich, and they get refreshed on a regular basis. For example, for ~$50K, you can buy:

- 💼 **500M Linkedin profile records **— to power a massive outreach campaign.

- 🛒 **270M Amazon product records** — to perform market analysis for your e-commerce, inform pricing and predict trends.

- 🏠 **130M Zillow listings** — to spot real estate trends and investment opportunities.

#### Third-party APIs that wrap websites 🕷️

Just like you can buy datasets, you can buy access to APIs that *wrap* popular websites like Amazon or Google. But why should I use a wrapper instead of the APIs of the same service?

Answers depend on the service, so let’s make the example of search engine (SERP) APIs:

- **📊 Higher limits** — higher thresholds for data access, and more data retrieved in a single query.

- 👔 **Tailored fit** — tailored to accomodate specific use cases, so they are 1) simpler to use, and 2) more feature-rich. E.g. [Tavily](https://tavily.com/) is a stripped down API that is optimized for LLMs.

- 💪 **Resilience** — they have mitigations against IP bans and CAPTCHA challenges.

- 🌐 **Multiple suppliers** — they provide results from multiple search engines at the same time.

#### Hosted web scraping APIs / tools 🖥️

If you need more flexibility but don't want to reinvent the wheel, there exist plenty of **hosted web scraping tools** and APIs.

These services provide the endpoints and the infrastructure to scrape data from any website. Popular examples include: [**ScrapingBee**](https://www.scrapingbee.com/), [**Scrapfly**](https://scrapfly.io/), and [**Bright Data**](https://brightdata.com/)** **itself.

#### Implement from scratch 🔧

When developers look at hosted scraping services, they are always surprised by how much they cost. The problem is that scraping is one of those tasks that seem simple until it’s not. In my experience, there are three main challenges:

1. 🎭 **Dynamic Content** — modern, JavaScript-heavy websites are tricky to scrape

1. 🧩 **CAPTCHAs **— many websites don't like being scraped

1. 🚫 **IP Blocking** — if a website catches on to your scraping, they might ban your IP.

There are many ways to address these problems one by one, but they are not always trivial. 

So, unless 1) web scraping is 100% core to your business, 2) there is relevant IP you want to build around it, and/or 3) volume is very high so that cost is an issue, I actually discourage people from implementing everything from scratch.

Still, if you want to go that route, here are my recommendations:

- For complex, interactive, JS-heavy sites where user interaction is required, I'd recommend using [**Playwright**](https://playwright.dev/).

- If you're dealing with simpler, static pages where you don't need to execute JS, libraries like **Scrapy** or **BeautifulSoup** work just as well.

I wrote a full primer on scraping use cases and technologies a few months ago 👇

[https://refactoring.fm/p/fundamentals-of-web-scraping-use](https://refactoring.fm/p/fundamentals-of-web-scraping-use)

---

### 3) 🔄 Feature Management Workflows

One of the biggest trends of 2024, which we often discussed, is [**the rise of product engineers**](https://refactoring.fm/p/how-to-become-a-product-engineer)** **(PEs).

This led, among other things, to more engineered workflows for managing features. Modern feature management has usually three components: 1) controlled rollouts, 2) experiments, and 3) monitoring. Let’s look at all of them:

#### **Controlled rollouts 🚦**

PEs use feature flags to release new features only to a subset of users, to get early feedback and measure impact.

This helps in monitoring leading indicators (e.g., initial user engagement) before affecting lagging ones (e.g., overall user retention). E.g. releasing a new UI to 10% of users and comparing their engagement rates to the control group.

Feature flags are useful for many other things, which wee discussed this in a previous article 👇

[https://refactoring.fm/p/feature-flags](https://refactoring.fm/p/feature-flags)

#### **Conducting experiments 🔬**

Having reliable leading indicators + a good feature flag infra allows you to run A/B tests.

You can compare different versions of a feature, roll them out to different groups of users, and make data-driven decisions. E.g. you can test two different onboarding flows and measure their impact on new user activation rates (leading) before seeing effects on user lifetime value (lagging).

A/B tests are not the only way to run experiments. In fact, to be statistically significant, they need a good volume of data, which is not always available. Think of a B2B SaaS setting, where you have a few customers, or the checkout page of an e-commerce, where only (e.g.) 5% of your users ever get to.

In these cases, you want to measure feature adoption and retention, as well as gather qualitative feedback from relevant users, like those who tried the feature but churned.

#### **Measuring outcomes 📈**

Post-launch, product engineers closely track both leading and lagging indicators to assess feature performance.

They set up dashboards and alerts for key metrics, so they can iterate based on real-time data.

Example: Tracking daily active users of a new feature (leading) while monitoring its impact on overall product usage and revenue (lagging).

You can find our full piece on modern product engineering below!

[https://refactoring.fm/p/how-to-become-a-product-engineer](https://refactoring.fm/p/how-to-become-a-product-engineer) 

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
