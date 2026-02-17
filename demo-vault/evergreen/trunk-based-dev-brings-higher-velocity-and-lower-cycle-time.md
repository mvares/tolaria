---
aliases:
  - "Trunk-based dev brings higher velocity and lower cycle time"
"Is A":
  - Evergreen
"Last Tweeted": 2022-08-22
Tags:
  - Has Pic
"Created at": "2024-04-18T14:44:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to":
  - "[[Feature Flags / Feature Management]]"
  - "[[monday-ideas/monday-41|Monday #41]]"
"Old Created At": "2022-07-21T16:28:00.000+02:00"
"Updated at": "2024-09-18T08:44:00.000Z"
Status: Not started
Tweet: "Trunk-based development boosts team velocity and reduces cycle times by merging small batches of code daily. But what if your project can't be broken into daily tasks? Enter feature flags—merge incomplete features without breaking your trunk. Let's discuss: how do you manage code quality while adopting this approach? #DevOps #TechLeadership"
notion_id: 15eafa30-5b86-41c0-a321-38c60c5157fb
---

# Trunk-based dev brings higher velocity and lower cycle time

Trunk-based development is a version control workflow where developers work in small batches and merge their work into the main trunk as often as possible — usually at least once a day.

That is opposed to the common workflow of *feature branches*, where developers create a separate branch for each new feature, and then work in isolation on that branch until the feature is complete.

- [Untitled](https://www.notion.so/4d19e7443df34ee9ae017d0bd6e06a1f) 

There is convincing evidence that teams who adopt trunk-based workflows achieve higher velocity and shorter cycle time.

However, not all projects can be broken down in small, working parts that get completed within a day. How should you work in those cases? 

Enter feature flags.

![image](../assets/bf7c8e9cd1a24bb8.png)

With feature flags, you can keep code in a *disabled *state, and merge it to the trunk even if the feature is not complete.

Small and frequent merges have some major benefits:

- Easier code reviews

- Less chance of conflicts

- Reduced risk for releases
