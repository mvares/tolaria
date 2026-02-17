---
aliases:
  - "Evaluate Cost + Impact + Contagion to assess technical debt"
"Is A":
  - Evergreen
"Created at": "2024-04-18T14:44:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to":
  - "[[essay/how-to-manage-technical-debt|How to Manage Technical Debt]]"
  - "[[monday-ideas/monday-5|Monday #5]]"
"Old Created At": "2022-02-04T11:15:00.000+01:00"
"Updated at": "2024-04-19T09:37:00.000Z"
Status: Not started
notion_id: 560fb08e-ac38-4f42-a068-b957596b8861
---

# Evaluate Cost + Impact + Contagion to assess technical debt

When it comes to assessing tech debt initiatives, I am a fan of the [system used by Riot](https://technology.riotgames.com/news/taxonomy-tech-debt).

They use three main metrics:

- 💣 **Impact** — business metrics impacted by the debt, or the value you unlock by repaying it. Crucial for the ROI equation.

- 💸 **Fix Cost** — a rough estimate based on some feasible solution. For the sake of prioritization, there is no need for it to be accurate. Simple t-shirt sizing (e.g. S, M, L, XL) is fine.

- 🦠 **Contagion** — this answers the question: “*if this debt is allowed to continue to exist, how much will it spread?*”. It’s a great angle because, in this regard, not all debt is created equal.

The contagion metric is particularly powerful because it informs on how impact and cost change over time. [Bill Clark](https://www.ltrandolphgames.com/), former EM for League of Legends, explains this well:

> If a piece of tech debt is well-contained, the cost to fix it later compared to now is basically identical. You can weigh how much impact it has today when determining when a fix makes sense.
