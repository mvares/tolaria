---
aliases:
  - "Charity Majors – Observability & Testing in Production"
"✏️ Status": Not started
"Belongs to":
  - "[[responsibility/publish-podcast|Publish Podcast]]"
  - "[[person/charity-majors|Charity Majors]]"
Status: Evergreened
URL: "https://refactoring.fm/p/observability-and-testing-in-production?utm_source=publication-search"
"👓 Status": Not started
"Created time": "2024-04-19T10:14:00.000Z"
Date: 2024-05-10
"Has Notes":
  - "[[evergreen/you-should-test-in-production|You should test in production]]"
  - "[[evergreen/the-importance-of-continuous-delivery|The importance of continuous delivery]]"
  - "[[evergreen/observability-vs-monitoring|Observability vs monitoring]]"
  - "[[evergreen/how-intercom-dodged-a-painful-migration|How Intercom dodged a painful migration]]"
Tags:
  - Podcast
  - Free
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 8cb5ebaf-994a-4d87-84a4-3facafbe5e8a
---

# Charity Majors – Observability & Testing in Production

### ⚖️ Observability vs Monitoring ([video](https://www.youtube.com/watch?v=97YRxrKNLP0&t=117s))

In the first part of our chat, Charity and I talked about the difference between Observability and other related concepts like *monitoring*, *APM*, and more.

Charity, who also wrote [a book](https://www.amazon.com/Observability-Engineering-Charity-Majors-ebook/dp/B09ZQ6FHTT) about it — explained how observability is a **property of complex systems**, just like scalability, or performance. Even more so, it is about *socio-technical *systems, not just your tech:

- If you **add more metrics**, you are improving observability.

- If you **educate your team** on how to ask questions about the system, you are improving observability as well.

Observability helps understand the intersection of software and users, and is like **the business intelligence of tooling**: it’s the single source of truth where you can break down, zoom in, zoom out information about your systems, together with information about your customers.

More specifically, good observability is based on three pillars:

- 📊 **Metrics **— offer insight into the health and performance of a system

- **🔀 Traces** —** **map the journey of a request or action as it moves through all the nodes of a system.

- ✏️ **Logs **— provide detailed records of events and activities within the system.

Together, these form the backbone of any observable system, enabling teams to monitor and address system issues in real-time.

#### 💬 Intercom migration story ([video](https://www.youtube.com/watch?v=97YRxrKNLP0&t=476s))

Charity makes a real-world example of how good observability enables teams to make the right technical decisions, taking the business context into account.

A few years ago, Intercom had to do a **giant database migration** because they had outgrown the largest EC2 instance size.

They thought it **was going to take a year** or so. Big deal. So they integrated Honeycomb and started instrumenting their code with app and user IDs.

At some point, one of the engineers was just poking around, breaking down and grouping events and figured out that something like 75 to 80% of the execution time for that database **was being taken up by one user ID** who was paying ~$20 a month.

So, instead of the full sharding migration they could just throttle that guy, and figure out things later.

This story seems extreme but it shows how technical decisions are inseparable from business decisions.

#### 🚚 Continuous Delivery ([video](https://www.youtube.com/watch?v=97YRxrKNLP0&t=2049s))

Later we talked about continuous delivery and how this is *enabled* by good observability. In fact:

1. Good observability == being able to get **closer conversations with code**, plus drawing correlation with business value.

1. Closer conversations with code allow to tell at a glance **when something is not working**.

1. Spotting problems fast grows the confidence to **ship many times a day**.

This virtuous cycle, however, can only happen when you get the code out in real environments in a small enough amount of time that engineers still have all that context in their head, so they go and check production against the instrumentation.

Charity goes even further and says that, as an engineer, your job isn’t over until you have looked at production to see that everything works.

This is the natural evolution of *integrated teams*, which went through various stages:

1. **Testing** — it used to be that QA ran all the tests → until we figured out it’s better if engineers do so.

1. **DevOps** — it used to be that ops people were separate from devs → until we figured out they should not.

1. **Observability** — it used to be that engineers job was over when they pushed their code → until we figured out it’s better if they look at how it works in prod.

#### Death Spiral 💀

Conversely, when you don’t get code out fast, and you don’t get it out automatically, you enter the **software engineering death spiral**, where everything starts taking a longer time. 

Code reviews take longer. Disks get larger. So people back up more. So they end up switching projects more. So they are waiting on each other more. Then you need a release engineering team and SRE team. Then you start batching releases, which further increases risk.

#### 🪂 Testing in production ([video](https://www.youtube.com/watch?v=97YRxrKNLP0&t=1680s))

Testing in production matters because, no matter how good your staging environment is, it is never going to be exactly like prod. 

It is not possible to have the same concurrency, the same chaos, the same variability, because every moment in production is unique.

Charity says you may or may not have a staging environment — that’s up to various factors — but you can’t *not* invest in good production tooling.

Counterintuitively, the right mindset, most of the times, is to invest resources in *fixing* *problems faster*, rather than *preventing problems*.

The former leads to speed, flow, and CD. The former leads to gating, batching, and pain.

#### 🤖 AI Engineering ([video](https://www.youtube.com/watch?v=97YRxrKNLP0&t=2814s))

At the end of our chat we also briefly talked about how AI is changing engineering.

Charity worries that generative AI is focused on generating a lot of lines of code from scratch, when most complexity in real life is in maintaining and evolving existing code.

So, there is a bad scenario in which we figure out that genAI code is 10x faster to write, but 10x slower to debug and maintain.

Also, junior engineers seem to be disproportionately impacted by this, with the job market becoming harder for them than it is for seniors.

I always believe people under-index on the benefits that junior folks bring to the team. It’s not just about tech chops — they keep things healthy by holding seniors to a higher standard. In my experience, teams with junior engineers have generally better docs, better tests, and lower turnover.

### 🐦 Linkedin / Twitter
