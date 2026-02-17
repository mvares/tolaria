---
aliases:
  - "What is mobile fragmentation"
"Is A":
  - Evergreen
"Created at": "2025-06-10T06:44:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to":
  - "[[essay/how-to-do-mobile-testing-right|How to Do Mobile Testing Right]]"
  - "[[monday-ideas/monday-166|Monday #166]]"
"Updated at": "2025-07-07T09:17:00.000Z"
Status: Not started
notion_id: 20ebdf02-815c-80ea-939b-c2951639c95a
---

# What is mobile fragmentation

We've thrown the term "*mobile fragmentation*" around, but what do we mean by that? Spoiler: it’s not something that happens to your phone screen after a drop.

At its core, mobile fragmentation is the sheer diversity of hardware and software across the millions of devices your application might encounter in the wild.

Such diversity is also *multi-dimensional*:

- 📱**Device manufacturers (the *****who*****) **—** **from the big players like Apple and Samsung, to the long tail of Xiaomi, Oppo, OnePlus, and the countless regional champions. Each comes with its own hardware quirks, custom Android *skins*, and unique interpretations of how Android *should* behave.

- 📋 **Operating systems & versions (the *****what***** & *****when*****)** —** **you need to account for multiple major versions active concurrently. Update rollouts lead to notorious lags, and some devices *never *get updated beyond a certain point. This is true for both iOS and Android, with Android being typically much worse.

- 📏 **Screen sizes & resolutions (the *****where*****)** — today’s smartphones range from compact screens, to *phablets*, foldables, and tablets: the range is vast. Other than physical size, you may also need to account for pixel density, aspect ratios, and newer features like dynamic refresh rates or screen cutouts (notches, punch-holes), that can all wreak havoc on your UI if not handled gracefully.

- ⚙️ **Hardware differences (the *****how*****) **—** **beneath the glass, there's even more: processors, memory constraints, GPUs, and sensors, which may or may not make a difference in how your app behaves.

Trying to account for every permutation is impossible. Understanding these dimensions, however, is the first step to building a *smarter* strategy.
