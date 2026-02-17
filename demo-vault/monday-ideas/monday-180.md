---
aliases:
  - "Monday #180"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-monday-idea|Publish Monday Idea]]"
Status: Published
"👓 Status": Not started
"Created time": "2025-10-28T09:41:00.000Z"
Date: 2025-11-03
"Has Notes":
  - "[[evergreen/theory-of-constraints|Theory of Constraints]]"
  - "[[evergreen/in-engineering-metrics-move-from-lagging-to-leading-indicators|In engineering metrics, move from lagging to leading indicators]]"
  - "[[evergreen/the-rise-of-local-first-software-adam-wiggins|The rise of local-first software (Adam Wiggins)]]"
Tags:
  - Monday
  - Free
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 29abdf02-815c-8011-aa2d-ef61bddba8d1
---

# Monday #180

### 1) 🔗 Theory of Constraints

One of the most frequent themes I hear about AI is that it’s hard to use it *a lot* on something, without creating bottlenecks elsewhere. 

Use it to write more code? More stress on code reviews. PMs create more prototypes? Engineers get more work to do. And so on. 

This made me think about the **Theory of Constraints** (TOC) — a model that views any system as being limited by a very small number of constraints, and, more immediately, by its weakest link. The corollary of TOC is that, to improve the performance of a system, you should focus on bottlenecks, one at a time.

For example, you may measure the various steps of your release process and discover that the biggest bottleneck is the time the code spends idle waiting for review. Or you may trace your API calls and figure out that the largest chunk of response times come from the database.

TOC was introduced by Eliyahu M. Goldratt in his 1984 book titled [The Goal](https://en.wikipedia.org/wiki/The_Goal_(novel))*.* The author suggests a five-step process to improve a system’s performance:

1. **🔍 Identify** — the system's constraints.

1. **🎲 Decide** — how to *exploit* the system's constraints.

1. **🔀 Subordinate** — everything else to the above decision.

1. **⬆️ Elevate** — the system's constraints.

1. **🔄 Repeat** — once a constraint is addressed, you should move to the next, in a continuous improvement cycle.

I wrote a full list of my favorite mental models in this article last year 👇

[https://refactoring.fm/p/mental-models-for-engineers-and-managers](https://refactoring.fm/p/mental-models-for-engineers-and-managers)

---

### 2) 📊 Leading vs lagging software metrics

This whole bottlenecking stuff also made me think about a chat I had with Abi Noda, CEO of DX, where we discussed the infamous "*# of commits / day*" metric. We agreed it's somewhat useful to measure, but that obviously becomes toxic when set as a target.

But… why? How can data give useful directional information, but become *bad* if we try to optimize for it?

The answer is in the difference between **leading and lagging indicators**:

- ➡️ **Lagging indicators** — show results of past actions (outcomes)

- ⬅️ **Leading indicators** — predict future outcomes (inputs)

![image](../assets/29abdf02815c804a.png)

Lagging indicators change slowly, are easy to measure, but hard to influence directly. They validate long-term success, but you can't use them to change direction.

A product example: *revenues* vs *feature adoption*. Revenue validates success, but you can't just set a higher revenue target and wait. To improve revenue, you need something actionable like feature adoption speed—a leading metric.

The *number of commits per day* is lagging, as are DORA metrics and most quantitative engineering metrics. You can't optimize for them directly because they're *downstream* of the dev process. When you treat them as *upstream* metrics, you reverse causation.

So, what's *leading* in developer productivity? As of today, the most convincing answer is **developer experience**. Good satisfaction across the usual suspects ([**focus time, no waiting, ease of release**](https://refactoring.fm/i/154749198/what-does-a-successful-team-look-like), …) *predicts* good speed and quality.

You can find more ideas about measuring dev productivity in this piece 👇

[https://refactoring.fm/p/whats-next-in-measuring-dev-productivity](https://refactoring.fm/p/whats-next-in-measuring-dev-productivity)

---

### 3) 🎙️ The Rise of Local-first Software

Earlier this year [I interviewed Adam Wiggins](https://refactoring.fm/p/user-experience-local-first-apps?utm_source=publication-search), co-founder of Heroku. Adam also introduced the concept of “local-first software” in a 2018 essay, which has since grown into a movement.

He defines it as combining the best of both worlds:

> ***"Local-first is kind of having your cake and eating it too. It's getting the collaborative shareability that we associate with web and cloud apps like Google Docs... but also getting back data ownership and user agency."***

Here are the key aspects of local-first software:

- **🔐 Data ownership** — users retain control and ownership of their data.

- **🌐 Offline-first** — applications work seamlessly offline, enhancing user agency.

- **🤝 Collaboration** — enables real-time collaboration similar to cloud-based apps.

- **🔀 Interoperability **— data can be more easily ported between different services.

Adam draws inspiration from tools like Dropbox and Git, which offer elements of local-first philosophy. He believes this approach is increasingly relevant in an era where data ownership and AI capabilities are becoming more critical.

Here is the full interview with Adam:

[https://www.youtube.com/watch?v=3vzXDT4ZniQ&t=20s](https://www.youtube.com/watch?v=3vzXDT4ZniQ&t=20s)

You can also find it on 🎧 [**Spotify**](https://open.spotify.com/episode/3Eo3r08g0Vb4F6ojnLihEz?si=a4f9b114f29e44da) and 📬 [**Substack**](https://refactoring.fm/p/user-experience-local-first-apps?utm_source=publication-search)
