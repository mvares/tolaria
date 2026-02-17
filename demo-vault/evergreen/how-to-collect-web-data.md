---
aliases:
  - "How to collect web data?"
Rating: Good
"Is A":
  - Evergreen
Tags:
  - Has Pic
  - Long
"Created at": "2024-09-18T07:46:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to":
  - "[[essay/web-scraping-fundamentals|Web Scraping Fundamentals]]"
  - "[[monday-ideas/monday-137|Monday #137]]"
"Updated at": "2024-12-31T09:52:00.000Z"
Status: Not started
Tweet: "💡 CTOs, are you leveraging web data effectively? From pre-collected datasets to hosted scraping tools, there’s a spectrum of options. Consider your use case: quick insights or custom solutions? Building from scratch can be tempting, but weigh the costs and complexities first. Let’s discuss the best strategies for your tech stack! #WebScraping #DataStrategy"
notion_id: b4af9511-f4aa-4f05-8db6-0971dd8feb26
---

# How to collect web data?

There are various ways to extract web data, on an ideal line that goes from *buy* to *build*.

Let’s explore the four main ones, commenting on pros and cons, and ideal use cases:

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/631d83ff-20ce-4401-a614-56e2c0f97767/b03baf80-506e-492c-8059-c50c9ea22c31/CleanShot_2024-12-31_at_10.52.052x.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667MTQN4H6%2F20260131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260131T190646Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCeUbopUyqK51V%2FIaTJpUcC5PcwOkINx0Xc9MkaJ9Q8BQIhAJRsRbxcEAs4bb0HdGrx94DMvZ9CI9E6IeE4dMYJ4EMJKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz57ZjrAzbuk8EloHUq3AP0g9hHBZdGfHrOpWwhtqM8FN9MfCbfbXt1BD4tQaBoSkeg7XNuKc9zd%2Bkj9BnkDaqw4amSj%2BZ9R9ldEUJrRdqo5OFyFR8zG8pFm98dcZVjo059G5olo99nUCElUpSCKc%2BxDGKicbR9VvrT%2F%2BjH4kTnwAA60M7GuUTHzRamfxcOnB77HgTVtKmHQ8IOA%2BZm4MZHvIjjAx78%2FANdiB7anEo2j6FJDbZLIZKx8IQ88yZZC9r86g9CXzbqjgDNmugeCagOHubXUVceJWSr27fR35bIqy5rMvgJ7lYakhzoszD55tL04V2I2iJBDBFlDGTyFVoCK4vG7UB6Pu1Am64uOPY8x%2BMpyVinxuHXVoykkU8Q1mX82egcwPx15uQRJ8Q1RmN%2ByH%2FWUge5nEYagOKkqfq5%2FKq0%2BIIobVerwyQxZusmlFa9rJbJZ%2FGzBSU4uDAFs3fE9iI0wp%2F7zKN5igpLin5X5gA%2FZ37S9071m8Wz7BIsDHlvOTo5VhEIWuryaal9HpY2Hu8j4CTiqkfvu2GtfsXPDSTjKDw6dn1JfioftA79GQM4991jRawCz3uYD0WBO9SG8w%2BZEobUh2J32n7l9IZR5qOFKo8TIIjNwhvTzqzMugwG1E6AL8Pchkvx%2FzDZjPnLBjqkATlfORJxmvPMN1WaRWD7XTV7qzO4WVappKsAy2KdAqwY5Aq0J2Jg1nQVqvULVRnqgfHGgSp4UJ5wgTfqU5iPEk%2BnkVEmRht6WFZGRP5vDRPncmO7%2BlE%2B%2BP5cP5mTNiOxZRMMt6WjsrV2wJDcMgMgaPLRgWoJ5XN69S7gc84mHF9%2FIvhp7%2FGBPibboTjv2VhKX3tvvQGIJOQcqxlOAFIzy8MRfvQt&X-Amz-Signature=413c6308790f396aa5496473a052edd4bcd00c61421b061123d5a8b2a74d58de&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### 1) Ready-made datasets 🗃️

Several companies offer pre-collected datasets on various topics. Examples are [**Bright Data**](https://brightdata.com/cp/datasets/browse?id=hl_588e08b6), [**Oxylabs**](https://oxylabs.io/products/datasets), or [**Webz**](https://webz.io/datasets/premium-datasets).

These datasets are pricey but also incredibly rich, and they get refreshed on a regular basis. For example, for ~$50K, you can buy:

- 💼 **500M Linkedin profile records **— to power a massive outreach campaign.

- 🛒 **270M Amazon product records** — to perform market analysis for your e-commerce, inform pricing and predict trends.

- 🏠 **130M Zillow listings** — to spot real estate trends and investment opportunities.

The main advantage of this approach, of course, is that it’s quick and easy: you get clean, structured data without the hassle of collecting it yourself. 

Downsides are 1) cost, 2) not real-time data, and 3) only available for popular websites.

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/631d83ff-20ce-4401-a614-56e2c0f97767/adc67c44-0ba7-46ae-b990-e7885a86f1cf/CleanShot_2024-08-15_at_15.43.382x.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667MTQN4H6%2F20260131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260131T190646Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCeUbopUyqK51V%2FIaTJpUcC5PcwOkINx0Xc9MkaJ9Q8BQIhAJRsRbxcEAs4bb0HdGrx94DMvZ9CI9E6IeE4dMYJ4EMJKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz57ZjrAzbuk8EloHUq3AP0g9hHBZdGfHrOpWwhtqM8FN9MfCbfbXt1BD4tQaBoSkeg7XNuKc9zd%2Bkj9BnkDaqw4amSj%2BZ9R9ldEUJrRdqo5OFyFR8zG8pFm98dcZVjo059G5olo99nUCElUpSCKc%2BxDGKicbR9VvrT%2F%2BjH4kTnwAA60M7GuUTHzRamfxcOnB77HgTVtKmHQ8IOA%2BZm4MZHvIjjAx78%2FANdiB7anEo2j6FJDbZLIZKx8IQ88yZZC9r86g9CXzbqjgDNmugeCagOHubXUVceJWSr27fR35bIqy5rMvgJ7lYakhzoszD55tL04V2I2iJBDBFlDGTyFVoCK4vG7UB6Pu1Am64uOPY8x%2BMpyVinxuHXVoykkU8Q1mX82egcwPx15uQRJ8Q1RmN%2ByH%2FWUge5nEYagOKkqfq5%2FKq0%2BIIobVerwyQxZusmlFa9rJbJZ%2FGzBSU4uDAFs3fE9iI0wp%2F7zKN5igpLin5X5gA%2FZ37S9071m8Wz7BIsDHlvOTo5VhEIWuryaal9HpY2Hu8j4CTiqkfvu2GtfsXPDSTjKDw6dn1JfioftA79GQM4991jRawCz3uYD0WBO9SG8w%2BZEobUh2J32n7l9IZR5qOFKo8TIIjNwhvTzqzMugwG1E6AL8Pchkvx%2FzDZjPnLBjqkATlfORJxmvPMN1WaRWD7XTV7qzO4WVappKsAy2KdAqwY5Aq0J2Jg1nQVqvULVRnqgfHGgSp4UJ5wgTfqU5iPEk%2BnkVEmRht6WFZGRP5vDRPncmO7%2BlE%2B%2BP5cP5mTNiOxZRMMt6WjsrV2wJDcMgMgaPLRgWoJ5XN69S7gc84mHF9%2FIvhp7%2FGBPibboTjv2VhKX3tvvQGIJOQcqxlOAFIzy8MRfvQt&X-Amz-Signature=cb1d396f3cfd9e40917bcf5cd240b7f0001f3ef3e1b0a11993d3d1855ac2c06c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### 2) Third-party APIs that wrap websites 🕷️

Just like you can buy datasets, you can buy access to APIs that *wrap* popular websites like Amazon or Google.

This is often a confusing proposition, because at a first glance you may wonder: why should I use a wrapper instead of the APIs of the same service?

Answers depend on the service, so let’s make the example of search engine (SERP) APIs, which are probably the *most wrapped* in tech:

- **📊 Higher limits** — wrapped SERP APIs generally offer higher thresholds for data access compared to direct API limits. You can retrieve more data in a single query, which is crucial for extensive research.

- 👔 **Tailored fit** — SERP APIs are usually tailored to accomodate specific use cases, so they are 1) simpler to use, and 2) more feature-rich. E.g. [Tavily](https://tavily.com/) provides an extremely stripped down API that is optimized for LLMs; SERP APIs for SEO add historical ranking, search volume, and domain insights.

- 💪 **Resilience** — they usually have mitigations against IP bans and CAPTCHA challenges.

- 🌐 **Multiple suppliers** — finally, they may provide results from multiple search engines, to give a more well-rounded perspective.

#### 3) Hosted web scraping APIs / tools 🖥️

If you need more flexibility but don't want to reinvent the wheel, there exist plenty of **hosted web scraping tools** and APIs.

These services provide the endpoints and the infrastructure to scrape data from any website. Popular examples include: [**ScrapingBee**](https://www.scrapingbee.com/), [**Scrapfly**](https://scrapfly.io/), and [**Bright Data**](https://brightdata.com/)** **itself.

Honorable mention to [**ParseHub**](https://www.parsehub.com/), which is a desktop app for doing **no-code scraping**. It also allows to store results in the cloud and it provides REST endpoints to access the extracted data programmatically. It’s a weird workflow, but it’s nice!

These services handle infrastructure for you and provide easy-to-use APIs, so they are a good intermediate step vs a full in-house implementation.

#### 4) Implement from scratch 🔧

When developers look at hosted scraping services, they are always surprised by how much they cost.

For the price of a basic tier on any of the services above, you can rent a server that would easily do 100x of the requests.

The problem is that scraping is one of those tasks that seem simple until it’s not. In my experience, there are three main challenges:

1. 🎭 **Dynamic Content** — modern, JavaScript-heavy websites can be tricky to scrape. You'll need to render the pages properly to access all the data.

1. 🧩 **CAPTCHAs **— many websites don't like being scraped, and they'll throw CAPTCHAs at you to prove you're human.

1. 🚫 **IP Blocking** — if a website catches on to your scraping, they might ban your IP address.

There are many ways to address these problems one by one, but they are not always trivial. 

So, unless 1) web scraping is 100% core to your business, 2) there is relevant IP you want to build around it, and/or 3) volume is very high so that cost is an issue, I actually discourage people from implementing everything from scratch.

Still, if you want to go that route, here are my recommendations. To me, tech choices largely depend on the type of website you need to scrape:

For complex, interactive, JS-heavy sites where user interaction is required, I'd recommend using [**Playwright**](https://playwright.dev/). Playwright is mostly known for testing, but the truth is it is extremely flexible and can automate browser actions, making it great for scraping tasks.

On the other hand, if you're dealing with simpler, static pages where you don't need to execute JS, libraries like **Scrapy** or **BeautifulSoup** in Python are simpler choices that work just as well.
