---
aliases:
  - "Monday #69"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-monday-idea|Publish Monday Idea]]"
Status: Published
"👓 Status": Not started
"Created time": "2024-04-18T15:09:00.000Z"
Date: 2023-09-18
"Has Notes":
  - "[[evergreen/improve-writing-with-ai|Improve writing with AI]]"
  - "[[evergreen/as-a-manager-you-should-have-hard-conversations|As a manager you should have hard conversations]]"
  - "[[evergreen/cloud-vs-on-prem-is-about-your-application|Cloud vs on-prem is about your application]]"
Tags:
  - Monday
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: baf81b0c-a869-44f0-a36b-170009aa9108
---

# Monday #69

*Hey, *[*Luca*](https://twitter.com/lucaronin)* here! Welcome to the ****Monday Ideas ***💡

*Every Monday I will send you an email like this with ****3 short ideas**** about making great software, working with humans, and personal growth.*

*You will also receive a long-form, original article on Thursday, like the last one:*

- **XXX**

*To receive all the full articles and support Refactoring, consider subscribing if you haven’t already!*

Get full access to Refactoring ✨

[https://refactoring.substack.com/subscribe](https://refactoring.substack.com/subscribe)?

*p.s. you can learn more about the *[*benefits of the paid plan here*](http://refactoring.fm/about)*.*

---

### Coderpad

---

### 1) 💬 Hard conversations

A great litmus test to figure out if you are doing well as a manager is **hard conversations**.

Are you having enough hard conversations with your team? There are always some: about careers, about CI/CD that takes forever, or about Dave, the guy that always makes everybody else wait two days for his code reviews. Hey Dave 👋

Hard conversations lead to progress, and the fact you are having them means that people feel *safe *to address problems with you.

Many of these start with something people are not *satisfied* with. **Satisfaction** comes *before* numbers — you might think something is doing great, but if people are not happy about it, you should act.

So, to begin a *data-driven *improvement journey, you don’t need tools. My advice is to just… ask people! Here are a few things you can survey your people about:

- *Are we spending time on the right things?*

- *Do you feel overworked?*

- *How do you feel about our delivery process?*

- *How do you feel about how we do code reviews?*

- *What do you think about how we work with PMs and designers?*

You can discuss these in many ways:

- 🗳️ **Surveys **— you can run team-wide surveys on a regular basis, e.g. once a quarter or twice a year, and check progress.

- **🧑‍🤝‍🧑 1:1s** — people can share how they feel in weekly 1:1s.

- ↩️ **Retrospectives **— you can leverage retros to have collective discussions and collect opinions on team-wide processes.

More on 1:1s, retros, and engineering metrics 👇

---

### 2) 🤖 I use AI to improve my writing

So far I couldn’t make AI write fully *original* content that is good enough for my standards, so, Refactoring is still, painstakingly, written by humans!

However, I have found AI useful for improving my writing, in various ways:

- **Improve grammar** — general proof-reading, similar to what you do with Grammarly or Writer.

- **Simplify** — if I feel that a sentence is a bit convoluted, I ask AI to simplify it, and it usually works.

- **Make it shorter** — similar to *simplify*, but this especially for when something feels redundant.

I use this mostly for my newsletter writing, but I can totally see how this is helpful in a team, too. We create a lot of writing that can benefit from this — emails, product specs, design docs, etc. — especially when authors are not native speakers, or are not particularly versed in writing.

> *We use it for proofreading. I fostered this from the beginning. Being a remote team with people coming from all over the world, and a lot of them not being native English speakers, can create communication issues. Proofreading your important chats, emails, documentation, slides, etc., can help avoid misunderstandings.

— *Nicola Ballotta, Director of Cloud at Namecheap

This kind of AI is embedded in many tools already, including Google Docs and Microsoft Office

I personally use [Notion AI](https://www.notion.so/product/ai?utm_source=google&utm_campaign=19760657944&utm_medium=147709666538&utm_content=649989555747&utm_term=notion%20ai&targetid=kwd-1547008718840&gclid=CjwKCAjwkeqkBhAnEiwA5U-uMxU2dkkJ2PED6DmyEjN-HgLcISUFFzIUIqXoC17vEWOT5cq3AJoDjBoCsAgQAvD_BwE), which is one of the best implementations of AI in a product that I have seen so far.

![The Notion AI context menu. Plenty of good recipes + you can ask for anything.](../assets/df4bd80e6cc54e96.png)

---

### 3) ⚖️ Cloud vs on-prem requirements

In recent times there has been a renewed debate about cloud vs on-prem options, fueled by a few notable stories — like Basecamp, which, [quite loudly](https://basecamp.com/cloud-exit), went back to on-prem.

As with many things there is no right or wrong, and the best option depends on your application requirements. Let’s see a few 👇

#### 🏗️ Complexity

Complexity is about your system design. 

Simply put, the higher the complexity of your design, the better cloud solutions look, because you can leverage managed services — like, running your queues on SQS, or storage on S3.

Cloud services are specialized and play nicely together. In the classic tradeoff between cost and ease of use/maintenance, managed services present the most compelling arguments vs if you just rented servers on the cloud.

> *The worst error you can make is to consider the cloud environment simply as a remote datacenter, moving your product on EC2s as if they were bare metal servers. Cost comparison between the on-prem and the cloud would always be in favor of the former*.

#### 👣 Traffic

Traffic by itself may not be incredibly hard to manage. While more traffic naturally leads to more complexity, the *amount* of load is not conclusive on how much work it brings, or whether on-prem is better or worse than cloud.

This tradeoff instead depends more on how your traffic *changes *over time.

- 📈 **Growth** — how much your traffic changes in the **mid/long term**.

- 📊 **Spikiness **— how much your traffic changes in the **short term**.

The cloud tradeoff here is about elasticity. Cloud resources are naturally more elastic than on-premise ones, both in the short and long term.

- In the short term you benefit from reactivity and auto-scaling. 

- In the long term you benefit from being able to reconfigure your system more easily than if you had committed on a specific set of machines you own.

#### ⚡ Performance

Performance needs may also affect your infrastructure choices.

You can meet low response times with any infra setup, but you probably need the cloud if your audience is *also* widely distributed geographically.

Truth to be said, though, most applications don’t have this problem. Chances are your performance constraints aren’t so strict, and you can meet them with any setup, plus maybe a CDN on top.

#### 👑 Data Sovereignty

You may have legal and compliance constraints about where your data lives. Data may need to live in specific countries, and/or you may need to exhibit various degrees of ownership.

Such constraints may limit what services you are able to use, and impact your choices.

Finally, the best choice depends on many other things, too, like your team skills, product stage, and more.

I wrote more about the whole sets of tradeoffs here 👇

[https://refactoring.fm/p/cloud-vs-on-premise](https://refactoring.fm/p/cloud-vs-on-premise)

---

### 3) 🎒 Idea 3

---

And that’s it for today! If you are finding this newsletter valuable, consider doing any of these:

**1) ✉️ Subscribe to the newsletter** — if you aren’t already, consider becoming a paid subscriber. You can learn more about the [benefits of the paid plan here](http://refactoring.fm/about).

Get full access to Refactoring ✨

[https://refactoring.substack.com/subscribe](https://refactoring.substack.com/subscribe)?

**2)** 🍻 **Read with your friends** — Refactoring lives thanks to word of mouth. Share the article with your with someone who would like it, and **get a free membership** through the new [referral program](https://refactoring.fm/p/referral).

[Read with your friends 🍻](https://refactoring.substack.com/leaderboard)

I wish you a great week! ☀️

Luca
