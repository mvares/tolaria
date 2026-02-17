---
aliases:
  - "Using time to size work is bad"
"Is A":
  - Evergreen
"Last Tweeted": 2022-10-16
"Created at": "2024-04-18T14:44:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to":
  - "[[essay/how-to-estimate-software-projects|How to Estimate Software Projects]]"
  - "[[monday-ideas/monday-19|Monday #19]]"
"Old Created At": "2021-10-15T16:12:00.000+02:00"
"Updated at": "2024-04-19T09:37:00.000Z"
Status: Not started
notion_id: 2f36a22f-109d-46e8-a1b2-4183e27cb142
---

# Using time to size work is bad

I have quite a strong opinion that using man-days, or time in general, as the main measure of engineering work is not ideal.

Time is bad for three reasons:

- 👥 **It depends on the developer** — the estimate is bound to the person that is assigned to the task. Junior vs Senior devs might take very different times to complete the same task.

- ⚒️ **It depends on** **other activities** — even though you can strive to measure an absolute effort, devs naturally take into account the time they expect to lose on concurrent activities, like maintenance, meetings, and interruptions.

- 🗓️** It turns estimates into** **deadlines **— it comes natural to set deadlines based on the sum of days that come up from estimates. This creates a **commitment **that is fragile — see (2) — and imprecise, because estimates are rough. It also puts more stress on developers, which may lead to the vicious cycle of inflated estimates.

![image](../assets/d45007542ef7436c.png)

Instead of time, you can use story points. [Untitled](https://www.notion.so/db2d92a28c074f6da9537323f03be78d).
