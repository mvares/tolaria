---
aliases:
  - "Collaboration vs coordination"
"Is A":
  - Evergreen
Tags:
  - Has Pic
"Created at": "2025-12-29T11:02:00.000Z"
Reviewed: false
Reading: "[[readings/collaboration-sucks|Collaboration Sucks]]"
Archived: false
Pinned: false
"Belongs to": "[[essay/the-ai-productivity-paradox|The AI Productivity Paradox]]"
"Updated at": "2025-12-29T11:03:00.000Z"
Status: Not started
Tweet: "Collaboration is about many people contributing to an output, while coordination involves considering others' work to complete tasks. There are three levels of coordination:\n1. ↩️ Sync coordination (e.g., meetings for decisions)\n2. 🔀 Async coordination (e.g., decisions needing approval)\n3. ➡️ No coordination (e.g., decisions made independently)\n\nEfficiency increases as coordination decreases. Reducing coordination safely depends on the probability of wrong decisions and their impact. If the process believes individuals will often make mistakes or that errors have severe consequences, coordination will be prioritized. Improving this involves finding ways to minimize unnecessary coordination."
notion_id: 2d8bdf02-815c-804d-b1d1-ccc3dd10cf87
---

# Collaboration vs coordination

The last angle I want to explore is about collaboration, inspired by this great article by PostHog from last week: [collaboration sucks](https://newsletter.posthog.com/p/collaboration-sucks)

And I want to nitpick here: it’s not *collaboration* that sucks — it’s *coordination*. What’s the difference?

- **🤝 Collaboration** — is about many people contributing to an output.

- **🚥 Coordination** — is when, in order to do what I do, I need to take into account what other people do.

There can be collaboration *without* (or with minimal) coordination. To be precise, it is useful to think about coordination in three levels:

1. **↩️ Sync coordination** — e.g. we hold a meeting to make a decision.

1. **🔀 Async coordination** — e.g. I make a decision, but that needs to be approved before it is confirmed. In the meantime, I do something else.

1. **➡️ No coordination** — e.g. I make a decision and it doesn’t need approval from others. Might get reverted if it’s wrong.

When you account strictly for throughput, these three are in **ascending order of efficiency**.

In reality, though, how you decide the right mode is about:

- **Probability** — how likely it is that a wrong decision is made, and

- **Impact** — what happens if a wrong decision is made.

You always want to *trend* towards less coordination, given that these two factors are in check.

![image](../assets/2d8bdf02815c808a.png)

So, when you see coordination happening, it’s because *the process* believes that individual people, left to themselves, 1) would make wrong calls too often, and/or 2) wrong calls would be too bad for the product/business.

Assuming that’s true, how do you improve? How do you safely reduce coordination?
