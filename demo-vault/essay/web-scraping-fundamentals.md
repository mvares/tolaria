---
aliases:
  - "Web Scraping Fundamentals"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-essays|Publish Essays →]]"
Status: Evergreened
Owner:
  - Luca
URL: "https://refactoring.fm/p/fundamentals-of-web-scraping-use"
"👓 Status": Not started
"Created time": "2024-07-19T06:26:00.000Z"
Date: 2024-08-21
"Has Notes":
  - "[[evergreen/how-to-collect-web-data|How to collect web data?]]"
  - "[[evergreen/what-to-use-web-data-for|What to use web data for]]"
  - "[[evergreen/is-scraping-responsible|Is scraping responsible?]]"
Tags:
  - Guest
  - Mgmt
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 24d7fa4f-97ba-4c4a-be6f-e911c7bbf2a6
---

# Web Scraping Fundamentals

### 📑 Materials

### Misc

### ✍️ Post

---

In [last week’s article](https://refactoring.fm/p/how-to-craft-your-vision-and-mission) I talked in some detail about my previous startup, Wanderio.

I explained some of our biggest challenges, including the need of integrating transport suppliers that didn’t have an API. To overcome this, we often resorted to scraping, and we did a lot of it.

Over time, our scraping *skill* proved useful in other, unexpected circumstances:

- Some supplier’s API was not exactly 99.99% available, so we used scraping as a fallback for when it went down (because yes, the websites often kept working).

- Some supplier’s API was incomplete, so some operations where only available via scraping.

- Some data was only available on the public web (e.g. airports geo data), and we extracted it from there.

So, I might be biased from this experience, but I believe **extracting web data** properly is an important tool for your tech strategy.

Still, I feel this domain is largely misunderstood. When I speak with other tech leaders about scraping, I typically find three areas of concerns:

1. 🎯 **Use cases** — people don’t know what to use it for.

1. 🔌 **Implementation** — extracting web data is perceived as overly complex and fragile.

1. ❤️ **Legal & ethical concerns** — scraping has a somewhat shady reputation.

These are long-standing arguments, but today they all have solid answers: use cases are copious; responsible scraping exists, and implementation is 10x easier than it was even just a few years ago.

This whole evolution happened [gradually, and then suddenly](https://www.goodreads.com/quotes/102579-how-did-you-go-bankrupt-two-ways-gradually-then-suddenly), thanks to the help of a singular trend: AI.

LLMs reignited the scraping conversation because they heavily rely on web data, for two tasks:

- **Training** — models are extensively trained on web data.

- **Agent behavior** — models increasingly need to perform real-time navigation to answer user queries and (possibly) make actions.

So, today’s article demystifies scraping and web data collection, from the perspective of an engineering leader who wants to explore how to use it for their team, and whether they should.

We will address the three concerns above by bringing in stories, real-world data from the industry, and my own experience. 

Here is the agenda:

1. 🎯 **What to use web data for **— a round-up of the most popular (and often surprising) use cases.

1. 🔌 **How to collect web data **— the four main ways, and the best options to implement them.

1. ❤️** How to do responsible scraping **— a recap of the regulatory framework + my personal moral compass about it.

Let’s dive in!

---

*For this article, I am partnering with Bright Data, which kindly provided industry reports, data, and insights to make the piece more grounded and useful.*

*I trust Bright Data because, at Wanderio, we worked with them for many years. They know the industry better than anybody else, and also pioneered the concept of *[*ethical data collection*](https://brightdata.com/trustcenter)*, so they were a natural partner for this piece.*

*Still, I will only provide my unbiased opinion on any service / tool that is mentioned, Bright Data included.*

---

### 🎯 What to use web data for

In my experience, use cases for web data can be split into two categories:

- ➡️ **Direct **— specific usage that is directly connected to the value prop of your product.

- ⬅️ **Indirect **— second-order benefits, more generic and widely applicable.

Direct uses cases are about products that create value by aggregating, summarizing, reviewing, and generally *transforming* web data.

There is plenty of them — think of:

- Search engines in the travel space, like Skyscanner or Kayak.

- E-commerce aggregators, similar to Google Shopping

- SEO tools, like Ahrefs or Semrush

- Brand monitoring tools, like Mention or Brandwatch

These are all ad-hoc use cases. You can find similar strategies by reflecting on your product and whether it can deliver more value by using web data directly.

There are also other, more general use cases, that work well for many companies. Here are some of my favorites:

#### **1) Security 🔒**

You can intercept emerging security risks by tapping into **threat intelligence feeds** (e.g. here is a [great list](https://github.com/hslatman/awesome-threat-intelligence?tab=readme-ov-file)), government alerts, and industry news on the web.

Based on your business, there is a lot you can anticipate, prevent, or mitigate this way: tech vulnerabilities, phishing attempts, data breaches, stolen information, and more.

For example, financial institutions monitor dark web forums for mentions of stolen credit card numbers, allowing them to proactively alert customers and prevent fraud.

#### 2) Market & competition insights 📈

Web data is, of course, a treasure trove of information about your market and competitors. For some businesses, this doesn’t really move the needle, while for others it’s crucial. 

Think of e-commerce stores:

- 🏷️ **Dynamic pricing **— you can harness data from competitors' websites, product pages, and deal sites to inform your pricing decisions.

- 🚀 **Track product launches **— keep tabs on new product announcements that are relevant to you (e.g. new products you can sell).

- 😊 **Analyze customer sentiment **— gather and analyze customer reviews and ratings across various platforms to understand market trends.

#### 3) Brand health & customer support 🩺

You can monitor your brand’s health through social media analysis, online reviews and ratings, gaining insights into brand perception.

The same approach can be adopted to intercept issues and provide proactive customer support. For example, that’s what many telcos do to spot issues in their network.

#### 4) Building AI models 🤖

Finally, AI stands out as a *meta* use case. You can use web data to fine-tune base models or create RAG systems for a variety of use cases, including the ones above.

We also discussed it in this previous article:

[https://refactoring.fm/p/how-to-integrate-llms?utm_source=publication-search](https://refactoring.fm/p/how-to-integrate-llms?utm_source=publication-search)

---

### 🔌 How to collect web data

There are various ways to extract web data, on an ideal line that goes from *buy* to *build*.

Let’s explore the four main ones, commenting on pros and cons, and ideal use cases:

![image](../assets/5af136f0ae8a4d00.jpg)

#### 1) Ready-made datasets 🗃️

Several companies offer pre-collected datasets on various topics. Examples are [**Bright Data**](https://brightdata.com/cp/datasets/browse?id=hl_588e08b6), [**Oxylabs**](https://oxylabs.io/products/datasets), or [**Webz**](https://webz.io/datasets/premium-datasets).

These datasets are pricey but also incredibly rich, and they get refreshed on a regular basis. For example, for ~$50K, you can buy:

- 💼 **500M Linkedin profile records **— to power a massive outreach campaign.

- 🛒 **270M Amazon product records** — to perform market analysis for your e-commerce, inform pricing and predict trends.

- 🏠 **130M Zillow listings** — to spot real estate trends and investment opportunities.

The main advantage of this approach, of course, is that it’s quick and easy: you get clean, structured data without the hassle of collecting it yourself. 

Downsides are 1) cost, 2) not real-time data, and 3) only available for popular websites.

![image](../assets/278f83d7393c4008.png)

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

---

### ❤️ How to do responsible scraping

Scraping has a somewhat shady reputation, but can you do it responsibly? The short answer is yes, but it's not straightforward.

This is still largely uncharted territory, so let's dive into both the current regulatory framework and my personal moral compass.

#### 1) Regulatory framework **📜**

The legal side is still murky and subject to interpretation, but here are some guidelines you can keep in mind:

- 😇 **Fair and transformative use **— in some jurisdictions, like the US, scraping may be protected under the *fair use doctrine* if 1) the use of the scraped data is sufficiently transformative (e.g., for research, commentary, or criticism) and 2) it doesn’t harm the original content owner’s market.

- 📝 **Contractual Obligations** — many websites have Terms of Service that explicitly prohibit scraping. Violating these terms can lead to legal action for breach of contract. The problem is: it’s not always clear when websites can *enforce* these contracts, in fact… 👇 

- 🌐 **Public Webpages** — [some courts have ruled](https://techcrunch.com/2024/02/26/meta-drops-lawsuit-against-web-scraping-firm-bright-data-that-sold-millions-of-instagram-records/?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAAEmf_QyxfiT8vumWNKGBVsHOaKzVu43bbhyR_FfFV1gBO_4vyiA4iMqUJdWTpiDuZrkYa0s1MVB8rHfQ9b42RoxTTx8xC1fheV7E8klmHDcfxkJXDlQ3ZhM-E4t5-EsHLDbjREHVjvSqgTmWMvHT4rrGhMrHysmyrBnFSx8rxkV2) that scraping publicly accessible data (e.g., data not behind a login wall) does not constitute unauthorized access, and TOS can’t be enforced in that case because the user didn’t explicitly accept it (as they would if they had logged in).

It is also worth noting that bypassing CAPTCHAs and IP bans generally does not qualify as unauthorized access:

> *The court additionally disagreed […] that using automated tools to bypass access restrictions, like CAPTCHAs, was the same as accessing a “password-protected website.”*

So where does this leave us?

#### 2) Moral compass 🧭

My first observation is that, whenever the legal framework is uncertain or contradictory, you can’t blindly rely on it and distance yourself from ethical considerations. Actually, to me this is *always* true, not just when regulation is unclear, but we can argue it is *especially* true here.

Of course, this is a personal stance. I have no pretense to say this should be universally valid, nor I will judge others (most of the times 🙃) for doing things differently.

We play the game by the rules, but we still get to decide what the boundaries of these rules are. For some people it’s the law; for some it’s personal ethics, which might be narrower, while for others it’s even *beyond* the law — it’s “*what am I risking if I break the law here?*”

Eric Schmidt, former Google CEO, a few days ago, during a roundtable at Stanford, advocated for [startups to steal IP and make lawyers clean up the mess](https://www.theverge.com/2024/8/14/24220658/google-eric-schmidt-stanford-talk-ai-startups-openai).

Full quote:

> *I was not arguing that you should illegally steal everybody's music. What you would do if you're a Silicon Valley entrepreneur, which hopefully all of you will be, is if it took off, then you'd hire a whole bunch of lawyers to go clean the mess up, right?

But if nobody uses your product, it doesn't matter that you stole all the content.

And do not quote me.*

Just quoted you Eric — sorry!

Silicon Valley villains aside, for scraping, I ask myself two questions:

1. 🏆 **Does it bring any upside to the data owner?**

1. 🤝 **Is it coherent with the intended usage of the data?**

To move forward you need at least one strong yes.

The simple version is: if you are using data in a way that is wildly different from what was intended, it should cause no harm to the owner.

I also have a few (opinionated) examples:

- 🟢** Wanderio** — Wanderio is a good example of responsible scraping (*insert meme of Obama awarding himself)*,* *because it brought business to the suppliers it scraped, just like Skyscanner or Kayak.

- 🟡 **Perplexity **— there is a lot of debate on whether AI search engines should be allowed to operate the way they do. Perplexity cites sources but removes a lot of the need to visit the original websites. Still, information is used coherently and links are provided, so, if you ask me, that’s still ok.

- 🔴 **Midjourney **— (and DALL-E, Stable Diffusion, and the likes) can mimic the style of individual artists, obviously damaging their personal businesses. It uses their IP, commoditizes their work, and profits on top of it. Hard to be a fan.

---

*Finally, I want to thank again Bright Data for being a partner on this. If you want to learn more, you can explore their *[*State of Public Web Data*](https://brightdata.com/static/state_of_public_web_data_report_2024.pdf?md5=2589325-c03ec92c)*, which was extremely helpful to shape this piece.*

---

As always, if you have any questions or want to share your own experiences, I'd love to hear from you. Until next time, happy (and ethical) scraping! 👋

---

Did you know that web scraping is experiencing a renaissance, largely thanks to AI? 🤖

I worked for 8 years as CTO of a travel startup, and we used used web scraping extensively. Scraping has a shady reputation and is often misunderstood, so this week I wrote a free article to demystify it and explore its potential for your tech strategy.

You can find the full article at the end, here is the TL;DR:

🎯 𝗨𝗦𝗘 𝗖𝗔𝗦𝗘𝗦
Web scraping isn't just for price comparison sites. It has a wide range of applications that might surprise you:

↳ Security intelligence — 𝘮𝘰𝘯𝘪𝘵𝘰𝘳 𝘵𝘩𝘳𝘦𝘢𝘵 𝘧𝘦𝘦𝘥𝘴 𝘵𝘰 𝘱𝘳𝘦𝘷𝘦𝘯𝘵 𝘤𝘺𝘣𝘦𝘳 𝘢𝘵𝘵𝘢𝘤𝘬𝘴 (𝘭𝘪𝘯𝘬𝘴 𝘪𝘯 𝘵𝘩𝘦 𝘢𝘳𝘵𝘪𝘤𝘭𝘦)
↳ Market insights — 𝘵𝘳𝘢𝘤𝘬 𝘤𝘰𝘮𝘱𝘦𝘵𝘪𝘵𝘰𝘳𝘴' 𝘱𝘳𝘪𝘤𝘪𝘯𝘨 𝘢𝘯𝘥 𝘱𝘳𝘰𝘥𝘶𝘤𝘵 𝘭𝘢𝘶𝘯𝘤𝘩𝘦𝘴
↳ Brand health — 𝘢𝘯𝘢𝘭𝘺𝘻𝘦 𝘰𝘯𝘭𝘪𝘯𝘦 𝘳𝘦𝘷𝘪𝘦𝘸𝘴 𝘢𝘯𝘥 𝘴𝘰𝘤𝘪𝘢𝘭 𝘮𝘦𝘥𝘪𝘢 𝘴𝘦𝘯𝘵𝘪𝘮𝘦𝘯𝘵
↳ AI model training — 𝘨𝘢𝘵𝘩𝘦𝘳 𝘥𝘢𝘵𝘢 𝘧𝘰𝘳 𝘧𝘪𝘯𝘦-𝘵𝘶𝘯𝘪𝘯𝘨 𝘰𝘳 𝘤𝘳𝘦𝘢𝘵𝘪𝘯𝘨 𝘙𝘈𝘎 𝘴𝘺𝘴𝘵𝘦𝘮𝘴

🔌 𝗜𝗠𝗣𝗟𝗘𝗠𝗘𝗡𝗧𝗔𝗧𝗜𝗢𝗡 𝗢𝗣𝗧𝗜𝗢𝗡𝗦
Contrary to popular belief, implementing web scraping doesn't have to be complex. There's a whole spectrum of options that go from buy to build:

↳ Ready-made datasets — 𝘱𝘳𝘦-𝘤𝘰𝘭𝘭𝘦𝘤𝘵𝘦𝘥 𝘥𝘢𝘵𝘢 𝘧𝘰𝘳 𝘱𝘰𝘱𝘶𝘭𝘢𝘳 𝘸𝘦𝘣𝘴𝘪𝘵𝘦𝘴, 𝘵𝘩𝘢𝘵 𝘺𝘰𝘶 𝘤𝘢𝘯 𝘣𝘶𝘺
↳ Wrapper APIs — 𝘸𝘳𝘢𝘱𝘱𝘦𝘳𝘴 𝘧𝘰𝘳 𝘤𝘰𝘮𝘮𝘰𝘯 𝘴𝘦𝘳𝘷𝘪𝘤𝘦𝘴 𝘭𝘪𝘬𝘦 𝘴𝘦𝘢𝘳𝘤𝘩 𝘦𝘯𝘨𝘪𝘯𝘦𝘴
↳ Hosted scraping tools — 𝘧𝘭𝘦𝘹𝘪𝘣𝘭𝘦 𝘴𝘦𝘳𝘷𝘪𝘤𝘦𝘴 𝘧𝘰𝘳 𝘤𝘶𝘴𝘵𝘰𝘮 𝘴𝘤𝘳𝘢𝘱𝘪𝘯𝘨 𝘯𝘦𝘦𝘥𝘴
↳ In-house implementation — 𝘧𝘰𝘳 𝘤𝘰𝘳𝘦 𝘣𝘶𝘴𝘪𝘯𝘦𝘴𝘴 𝘯𝘦𝘦𝘥𝘴 𝘰𝘳 𝘩𝘪𝘨𝘩-𝘷𝘰𝘭𝘶𝘮𝘦 𝘴𝘤𝘦𝘯𝘢𝘳𝘪𝘰𝘴

❤️ 𝗥𝗘𝗦𝗣𝗢𝗡𝗦𝗜𝗕𝗟𝗘 𝗦𝗖𝗥𝗔𝗣𝗜𝗡𝗚
The regulatory framework around scraping is still murky. Public data can be usually scraped under fair use doctrine, but I don’t think that’s enough. Here's my personal moral compass:

↳ Bring value to data owners — 𝘦𝘯𝘴𝘶𝘳𝘦 𝘺𝘰𝘶𝘳 𝘶𝘴𝘦 𝘰𝘧 𝘥𝘢𝘵𝘢 𝘣𝘦𝘯𝘦𝘧𝘪𝘵𝘴 𝘰𝘳 𝘢𝘵 𝘭𝘦𝘢𝘴𝘵 𝘥𝘰𝘦𝘴𝘯’𝘵 𝘩𝘢𝘳𝘮 𝘵𝘩𝘦 𝘰𝘳𝘪𝘨𝘪𝘯𝘢𝘭 𝘴𝘰𝘶𝘳𝘤𝘦
↳ Align with intended usage — 𝘶𝘴𝘦 𝘥𝘢𝘵𝘢 𝘪𝘯 𝘢 𝘸𝘢𝘺 𝘵𝘩𝘢𝘵'𝘴 𝘤𝘰𝘩𝘦𝘳𝘦𝘯𝘵 𝘸𝘪𝘵𝘩 𝘪𝘵𝘴 𝘰𝘳𝘪𝘨𝘪𝘯𝘢𝘭 𝘱𝘶𝘳𝘱𝘰𝘴𝘦
↳ Respect legal boundaries — 𝘣𝘦 𝘢𝘸𝘢𝘳𝘦 𝘰𝘧 𝘛𝘦𝘳𝘮𝘴 𝘰𝘧 𝘚𝘦𝘳𝘷𝘪𝘤𝘦𝘴 𝘢𝘯𝘥 𝘳𝘦𝘨𝘶𝘭𝘢𝘵𝘪𝘰𝘯 𝘪𝘯 𝘺𝘰𝘶𝘳 𝘤𝘰𝘶𝘯𝘵𝘳𝘺

Web scraping, when done responsibly, is a powerful tool, because the vast majority of web data isn’t available through APIs.

Here is my full article about web scraping fundamentals: [https://refactoring.fm/p/fundamentals-of-web-scraping-use](https://refactoring.fm/p/fundamentals-of-web-scraping-use)

♻️ If you found value in these insights, please consider reposting it! It means a lot to me and helps spread these ideas to other tech leaders who might benefit.
