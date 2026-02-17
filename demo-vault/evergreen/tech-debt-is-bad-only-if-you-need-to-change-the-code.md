---
aliases:
  - "Tech debt is bad only if you need to change the code"
"Is A":
  - Evergreen
"Last Tweeted": 2025-12-19
"Created at": "2025-09-25T16:04:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to":
  - "[[essay/how-to-prioritize-tech-debt|How to Prioritize Tech Debt]]"
  - "[[monday-ideas/monday-187|Monday #187]]"
"Updated at": "2025-12-19T09:31:00.000Z"
Status: Not started
Tweet: Bad code is only problematic if changes are needed. Focus quality efforts on hotspots, the areas frequently subject to change. Many tech debt efforts misidentify targets, focusing on stable code instead of active areas. In most codebases, ~5% of the code sees 90% of the activity. This was evident during a failed M&A when a consulting firm highlighted poor quality code, failing to consider frequency of change. Despite our emphasis on strategic parts, marginal code was weighted equally, contributing to the deal's collapse. Remember, prioritize areas that impact your product's evolution.
notion_id: 279bdf02-815c-8062-88f9-c43bd6829345
---

# Tech debt is bad only if you need to change the code

Bad code is bad only if you need to change it. If it looks bad, but is stable, it doesn’t pose any concerns.

This might seems trivial to say, but it has deep implications. The main one is that you should focus your quality work on *hotspots *(cit. Adam Tornhill): the parts of your codebase that are frequently subject to change.

As humans we are bad at judging this intuitively, so a lot of work on tech debt is simply misguided: it either happens either on bad—but stable—code, or on areas that are active but already in relatively good shape.

This is also hard to evaluate because *activity distribution* is extremely skewed: in most codebases, **~5% of the code gets 90% of the activity**.

This reminds me of something from my startup days.

During an M&A conversation, the buyer’s consulting firm ran a technical due diligence. They found several areas of poor quality code—as we expected. In fact, over time we had doubled down on specific parts of the product we cared about, while phasing out others. The latter stayed experimental: less testing, more duplication, etc.

What I didn’t expect was how hard this proved to be to argue. We pointed to the strategic parts we were proud of, but they weighted sketchy marginal code as an equal part of the whole.

In other words, the **frequency of change** wasn’t considered.

Eventually the M&A failed for a variety of reasons. This was not explicitly mentioned as a blocker, but I always suspected it contributed.

You can find the full article from my chat with Adam below 👇

During my time as a co-founder of my startup, we once had a promising M&A conversation with a partner. Talks were in advanced stage, and the buyer brought in a consulting firm to perform a technical due diligence on our product.

They ran static analysis tools and they found—as we expected—several areas of poor quality code. We knew that because over time, as it is often the case for startups, we doubled down on some specific parts of the product—the ones we cared about keeping healthy and clean—while gradually phasing out others. On the latter, code had often stayed in an experimental stage: less testing, more duplication, etc.

What I didn’t expect, though, is that this proved hard to argue. As much as we pointed to the core, strategic parts we were proud of, the firm also pointed to a bunch of sketchy stuff which for us was marginal, but for them was equally part of the whole.

In other words, the *frequency of change* was not taken into account.

Eventually the M&A failed for a variety of reasons, and while this was not explicitly mentioned as a blocked, I always suspected it contributed to the outcome.
