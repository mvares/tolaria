---
aliases:
  - "In engineering metrics, move from lagging to leading indicators"
"Is A":
  - Evergreen
Tags:
  - Has Pic
"Created at": "2025-02-26T14:12:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to":
  - "[[essay/whats-next-in-measuring-dev-productivity-dx|What’s Next in Measuring Dev Productivity — DX]]"
  - "[[monday-ideas/monday-180|Monday #180]]"
"Updated at": "2025-12-16T08:29:00.000Z"
Status: Not started
Tweet: The discussion highlights the importance of differentiating between lagging and leading indicators in engineering metrics. Lagging indicators, such as the number of commits per day, reflect past performance but are hard to influence directly. In contrast, leading indicators, like developer experience, can predict future outcomes and are actionable. While lagging metrics provide long-term validation, focusing on upstream metrics such as developer satisfaction can enhance productivity and quality. The challenge with traditional surveys is their infrequency and reliability, but real-time data collection can mitigate these issues, providing a more accurate assessment of developer experience.
notion_id: 1a6bdf02-815c-800e-88e7-d127c08a5ba2
---

# In engineering metrics, move from lagging to leading indicators

### ⬅️ From *lagging* to *leading* indicators

While talking with Abi, at some point we discussed the (in)famous “*# of commits / day*” metric. We both agreed that this is *useful *to measure, but ineffective (and even toxic) when set as a target.

But what does that mean? How can some data give useful directional information, but suddenly become *bad *if we try to optimize for it?

The answer is in the difference between **leading and lagging indicators**. 

- ➡️ **Lagging indicators** — are *outcome* metrics that show results of past actions. 

- ⬅️ **Leading indicators** — are *input* metrics that predict future outcomes.

This difference is mostly [discussed in product management](https://refactoring.fm/p/how-to-become-a-product-engineer), but is exceptionally relevant in engineering, too.

![image](../assets/29abdf02815c8096.png)

Lagging indicators usually change slowly, are easier to measure, but harder to influence directly. They are *perfect* to give you long-term validation, but you can’t use them to change direction* *directly.

A product example is *revenues* vs *feature adoption*. Revenue is what ultimately validates success, but you can’t just set a higher revenue target and wait for it to happen. Revenue is lagging — to improve it you need something more actionable that you can influence directly, like the speed of feature adoption, which is a leading metric.

So, back to engineering, the *number of commits per day* is a lagging indicator, and so are (mostly) the DORA metrics, and the majority of quantitative engineering metrics. You can’t optimize for them directly, because they are *downstream *of everything that happens in the dev process.

When you treat them as *upstream* (leading) metrics, you fail because you are reversing the correlation/causation direction.

So, what is *leading* in developer productivity? As of today, the most convincing answer is **developer experience**. Good satisfaction across the various *usual suspects* ([enough focus time, no waiting, ease of release,](https://refactoring.fm/i/154749198/what-does-a-successful-team-look-like) …) *predicts* good speed and quality.

Now, the classic problem of surveys is that they are *delayed* and *infrequent*, which makes them unreliable because of memory decay, recency bias, and all kinds of problems. Which is why I was especially pleased to learn that DX has found a way to avoid these problems by collecting data in real-time 👇 
