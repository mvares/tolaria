---
aliases:
  - "Monday #86"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-monday-idea|Publish Monday Idea]]"
Status: Published
"👓 Status": Not started
"Created time": "2024-04-18T15:09:00.000Z"
Date: 2024-01-15
"Has Notes":
  - "[[evergreen/maslows-hierarchy-of-culture|Maslow’s Hierarchy of Culture]]"
  - "[[evergreen/repaying-tech-debt-impacts-business-via-second-order-effects|Repaying tech debt impacts business via second-order effects]]"
  - "[[evergreen/web3-applications-run-on-five-layers|Web3 applications run on five layers]]"
Tags:
  - Monday
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 18a577f0-df35-4f8b-a5c5-7141ef3734da
---

# Monday #86

*Hey, *[*Luca*](https://twitter.com/lucaronin)* here! Welcome to the ****Monday Ideas ***💡

*Every Monday I send you an email like this with ****3 short ideas**** about making great software, working with humans, and personal growth.*

*Paid members also receive a long-form, original essay on Thursday, like the last one:*

[https://refactoring.fm/p/how-to-plan-and-execute-projects](https://refactoring.fm/p/how-to-plan-and-execute-projects)

*To receive all the full articles and support Refactoring, consider joining 1400+ engineers and get the paid membership!*

Get full access to Refactoring ✨

[https://refactoring.substack.com/subscribe](https://refactoring.substack.com/subscribe)?

*p.s. learn more about the *[*benefits of the paid plan here*](http://refactoring.fm/about)*.*

---

### 📈 The State of Engineering Productivity in 2024

Before we dive into this week’s ideas, I have some news! I am conducting a survey about what makes engineering teams productive: practices, usage of metrics, tools, etc.

The goal is to collect a few hundreds responses, gather insights, and write a thorough newsletter edition about this!

If you want to help me out on this, you can fill out the survey below 👇 it should take no more than 5 mins

Thank you! 🙏

### 1) ✨ Good engineering culture is about impact

In his bestseller book *Drive*, Daniel Pink argues our motivation is driven by three factors:

- 🟣 **Autonomy** — the desire to be self-directed. We get motivation and joy by having control over our lives.

- 🔴 **Mastery** — the desire to improve our craft. We get satisfaction by getting better at what we do.

- 🟢 **Impact** — the desire to have a positive impact on the world. We are empowered by work that serves a higher purpose.

I love this framework and I quote it all the time. In my experience, however, the three elements have **different weights** for different people.

I have met engineers who were extremely driven by *impact*, and others who cared more about *mastering their craft*. Engineers who wanted maximum agency, and others who were happy to fit in a tight process.

These are not rigid categories. It is a spectrum, and everyone falls somewhere on it.

Since teams are, basically, just groups of people, this is true for teams as well. And for companies: companies inherit their founders’ traits, because founders hire people who are similar to themselves.

Now, I have found that **the best engineering cultures are driven by impact**. Impact is about what the business needs to achieve: if people are aligned and motivated to go after it, everything else follows.

On the contrary, a strong culture of *technical* *mastery* that is *not* also hungry for impact, may end up in bureaucracy and overly complicated tech.

That is not to say technical prowess doesn’t matter: it does, but the three elements work like a **Maslow’s Hierarchy of Culture**: without alignment on impact you can’t have *safe* autonomy, and, without autonomy, you can’t get healthy mastery.

I have written a full guide about creating good engineering culture a month ago👇

[https://refactoring.fm/p/culture](https://refactoring.fm/p/culture)

---

### 2) 🦠 Tech debt & second-order effects

The biggest reason why it is hard to sell leadership on repaying tech debt is that such initiatives mostly impact the business via **second-order effects**, like *velocity*, *happiness*, or *reduced turnover*.

Second-order effects have **longer feedback loops** and can be hard to assess.

If you strictly pit these against e.g. a feature that increases the conversion rate at checkout, it's not a level playing field.

So, most times, the #1 element that enables repaying debt is **savvy leadership** that understands this and isn't pedantic with requiring precise ROI and KPIs.

They understand their team and how bottlenecks work — and go for it.

Still, a good strategy for managing technical debt can be measurable and produce quantitative results. I wrote a full guide about this, which is one of the most popular Refactoring pieces ever 👇

[https://refactoring.fm/p/technical-debt](https://refactoring.fm/p/technical-debt)

---

### 3) 👾 Web3’s five layers

Interest in web3 has been on the rise in the past few months, and the recent [approval of a Bitcoin ETF](https://www.ft.com/content/443b2589-0a4a-48ef-872e-3cd52b1b297d) marks an historical moment for this space.

However, the architecture of a web3 application remains a mystery for most engineers — as it is wildly different from a regular web2 one.

Web3 applications can be organized in **five layers**. Most layers leverage existing technology and build on top of them. Let’s see such layers one by one and draw a comparison with web2 👇

![image](../assets/63877c752ee44a31.png)

#### 1) Protocol Layer 🔀

When we talk of protocols for web applications, we usually refer to the ones defined in the [OSI model](https://en.wikipedia.org/wiki/OSI_model) — like IP, TCP, SSL, HTTP. 

Web3 adds blockchain protocols *on top* of those. These new protocols regulate how data is stored and updated across the blockchain, and thus, across applications.

#### 2) Infrastructure Layer 🏗️

Smart contracts are run by **Nodes**. Nodes are the basic infrastructure piece of the blockchain.

From an infrastructure perspective, the main difference between a node and a computer running regular software is that each node runs *all* the blockchain. 

This poses obvious scalability concerns, which are being addressed in various ways. For example, Eth2 introduces [sharding](https://ethereum.org/en/eth2/shard-chains/), while Solana has [proof-of-history](https://solana.com/news/proof-of-history).

#### 3) Platform Layer 🧱

When it comes to running software, just like people don’t want to run their own servers, they don’t want to run their own nodes.

To solve this pain there are companies that provide “*Nodes as a service*”, the main ones being [Alchemy](https://www.alchemy.com/) and [Infura](https://infura.io/). They provide convenient APIs to access the blockchain (read and write) and allow you to scale while keeping the node layer below completely transparent.

They are the **AWS of web3**.

#### 4) Contract Layer 📃

Nodes run virtual machines (EVM in case of Ethereum) on top of which smart contracts run. This layer is about the business logic that affects the *state* of the application, which is stored on the blockchain.

#### 5) Application Layer 📱

Applications who rely on smart contracts are still built with traditional backend / frontend stacks. In fact, most apps today are *mixed* — they manage part of the logic and state on the blockchain, and part on regular centralized databases.

This is to be expected because, as we will see, smart contracts impose rigid workflows that have a serious impact on your development velocity. Whenever you have non-critical logic and data (e.g. analytics, caching) you are better off developing it in a traditional fashion.

E.g. to access Ethereum nodes, you can find plenty of libraries that act as a bridge between the web3 and web3 world. Just check on [Ethereum docs](https://ethereum.org/en/developers/docs/apis/backend/).

I wrote a two-part series on web3 engineering. You can check it out below 👇

[https://refactoring.fm/p/web3-tech](https://refactoring.fm/p/web3-tech)

---

And that’s it for today! If you are finding this newsletter valuable, consider doing any of these:

**1) ✉️ Subscribe to the newsletter** — if you aren’t already, consider becoming a paid subscriber. 1400+ engineers and managers have joined already! Learn more about the [benefits of the paid plan here](http://refactoring.fm/about).

Get full access to Refactoring ✨

[https://refactoring.substack.com/subscribe](https://refactoring.substack.com/subscribe)?

**2)** 🍻 **Read with your friends** — Refactoring lives thanks to word of mouth. Share the article with your with someone who would like it, and **get a free membership** through the new [referral program](https://refactoring.fm/p/referral).

Read with your friends 🍻

[https://refactoring.fm/leaderboard](https://refactoring.fm/leaderboard)

I wish you a great week! ☀️

Luca
