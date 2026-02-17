---
aliases:
  - "Monday #131"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-monday-idea|Publish Monday Idea]]"
Status: Published
"👓 Status": Not started
"Created time": "2024-11-19T13:59:00.000Z"
Date: 2024-11-25
"Has Notes":
  - "[[evergreen/how-to-prepare-for-a-salary-review|How to prepare for a salary review]]"
  - "[[evergreen/single-tool-vs-multiple-tools|Single tool vs multiple tools]]"
  - "[[evergreen/observability-vs-monitoring|Observability vs monitoring]]"
  - "[[evergreen/my-favorite-ai-tools-for-coding|My favorite AI tools for coding]]"
  - "[[evergreen/your-manager-feels-more-productive-than-you|Your manager feels more productive than you]]"
Tags:
  - Monday
  - Free
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 143bdf02-815c-8041-bd27-c2e1e07a8d01
---

# Monday #131

### Budibase

---

### 1) 🎽 How to prep for salary reviews

Earlier this year we wrote a full piece about how to do good [salary reviews](https://refactoring.fm/p/how-to-do-salary-reviews). Many companies do this at the end of the year — if that’s the case for you, you should prepare in three steps:

#### 1.1) Market Research 🔍

Regularly benchmark salaries to ensure competitiveness and retain talent. This can be done by HR or engineering managers, depending on company structure.

Useful salary data sources: [Payscale](https://www.payscale.com/research/), [Levels.fyi](https://www.levels.fyi/), [Glassdoor](https://www.glassdoor.com/Salary/)

#### 1.2) Performance Data Collection 📊

While opinions vary on linking performance to salary, it's crucial to have a clear, fair process. I usually rely on the following principles:

- 💰 **Consistent raises** — if the budget allows, I aim to give a minimum yearly raise to every team member, including those with average performance. Of course, there may be years when this minimum raise cannot be met.

- 🌟 **Rewarding excellence** — for exceptional performers, I aim to provide a bonus in addition to the minimum yearly raise.

- 🗣️ **Seeking feedback** — I never rely solely on my judgment. I seek feedback from colleagues who have worked closely with the person being reviewed.

Related to performance, we wrote a full piece about [performance reviews](https://refactoring.fm/p/performance-reviews?utm_source=publication-search) last year.

#### 1.3) Budget Planning 🧮

Once you have a clear understanding of fair compensation for your team, it’s time to plan your budget. Develop a comprehensive plan for raises, considering:

- 💰 **Financial constraints** — understand the overall budget limitations and financial health of the company.

- 🔄 **Competition **—** ** keep up with industry salary trends to ensure competitiveness.

- 💡 **Strategic priorities** — consider the company’s strategic goals and how salary adjustments can support these objectives.

- 🌟 **Employee retention** — factor in the importance of retaining top talent and how competitive salaries can aid in this effort.

Include specific reasons for planned raises to aid in negotiations with upper management. You can find the full piece below!

[https://refactoring.fm/p/how-to-do-salary-reviews](https://refactoring.fm/p/how-to-do-salary-reviews)

---

### 2) ⚖️ Single tool vs multiple tools

For status updates, async exchanges through docs and tools are the main alternative to meetings. While tools seem easier, most are specific to certain use cases and users.

So what do you do? Two options work:

1. 📁 **Single tool** — stick with one source of truth, prioritizing consistency over UX, e.g., use Notion for everything.

1. 🗃️ **Multiple tools** — use specialized solutions for different use cases, prioritizing UX over consistency, e.g., use Notion for OKRs and Jira for tasks.

The choice depends on team skills, product, and scale.

![image](../assets/143bdf02815c80ba.png)

#### Using a Single Tool 📁

A single tool reduces inconsistencies and delays. The main challenge is ensuring good UX for all stakeholders.

Teams can enhance the tool with custom visualizations, automated workflows, and chatOps. Examples: Visor + Jira, Glide + Google Sheets, Softr + Airtable.

Select a tool with a strong ecosystem and granular data handling capabilities.

#### Using Multiple Tools 🗃️

Using different tools for different jobs can work but poses two main risks: 1) confusion about what goes into each tool, and 2) inconsistency — info may need replication, risking stale data.

To counter these:

1. **Clarify boundaries** — make the scope and responsibilities of each tool clear. For instance, use Notion for OKRs, Linear for tasks, and store projects on both with links.

1. **Clarify ownership** — ensure it's clear who owns and updates each tool. For example, PMs own Notion project pages, while TLs or EMs maintain Linear ones.

1. **Use automation** — set good boundaries to minimize overlap and use tools like Zapier for automation if needed.

#### How to Choose 🎲

Both styles can work. Consider how much action happens on the tools by stakeholders. If deep UX differences exist, you may need to split tools.

This should be a collaborative choice:

- **Talk with people** — ask stakeholders what they need.

- **Use tools in meetings** — prototype tool usage in meetings to ensure clarity and comfort with the workflow.

- **Take baby steps** — test one use case at a time and proceed when everyone is satisfied.

You can find our full piece about keeping stakeholders aligned below! 👇

[https://refactoring.fm/p/how-to-keep-stakeholders-aligned](https://refactoring.fm/p/how-to-keep-stakeholders-aligned)

---

### 3) 📊 Observability vs Monitoring

Earlier this year [I interviewed Charity Majors](https://refactoring.fm/p/observability-and-testing-in-production?utm_source=publication-search), and at the beginning of our chat we discussed the difference between Observability and other related concepts like *monitoring*, *APM*, and more.

Charity, who also wrote [a book](https://www.amazon.com/Observability-Engineering-Charity-Majors-ebook/dp/B09ZQ6FHTT) about it — explained how observability is a **property of complex systems**, just like scalability, or performance. Even more so, it is about *socio-technical *systems, not just your tech:

- If you **add more metrics**, you are improving observability.

- If you **educate your team** on how to ask questions about the system, you are improving observability as well.

Observability helps understand the intersection of software and users, and is like **the business intelligence of tooling**: it’s the single source of truth where you can break down, zoom in, zoom out information about your systems, together with information about your customers.

More specifically, good observability is based on three pillars:

- 📊 **Metrics **— offer insight into the health and performance of a system

- **🔀 Traces** —** **map the journey of a request or action as it moves through all the nodes of a system.

- ✏️ **Logs **— provide detailed records of events and activities within the system.

Together, these form the backbone of any observable system, enabling teams to monitor and address system issues in real-time.

You can find the full interview here:

[https://refactoring.fm/p/observability-and-testing-in-production?utm_source=publication-search](https://refactoring.fm/p/observability-and-testing-in-production?utm_source=publication-search)

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
