---
aliases:
  - "Benefits of microservices are organizational"
"Is A":
  - Evergreen
"Last Tweeted": 2023-03-14
Tags:
  - Has Pic
"Created at": "2024-04-18T14:44:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to":
  - "[[essay/monolith-vs-microservices|Monolith vs Microservices]]"
  - "[[monday-ideas/monday-46|Monday #46]]"
"Old Created At": "2022-11-24T11:10:00.000+01:00"
"Updated at": "2024-09-18T08:44:00.000Z"
Status: Not started
Tweet: "The benefits of microservices are largely organizational, not just technical. If you want to leverage independent teams, a service-based architecture is essential. But remember, if your team is still one large unit, the overhead may outweigh the gains. Focus on modularity and spin off services when it makes sense for independent workflows. Let’s discuss! #Microservices #SoftwareArchitecture"
notion_id: ec9a35b3-890b-4232-b070-f65cd67c40d5
---

# Benefits of microservices are organizational

Overall, the benefits of isolated services vs a modular monolith seem to be mostly organizational, rather than technical. This doesn’t make them less important, though.

As by [Conway’s Law](https://refactoring.fm/i/71307178/conways-law), your software design structure gets eventually shaped around your team’s communication structure. So, if your team is large and you want to organize it around **small independent teams**, you may need to gravitate towards a service-based architecture.

![image](../assets/8122285be3ab4fa3.png)

The opposite is also true: you won’t probably get the full benefits of microservices as long as your team stays a **single large unit**. The overhead will not be worth it if it is not matched by the communication benefits brought by autonomous teams.

It seems to me that a solid recipe for any team might be to focus on modularity, and spin off independent services whenever you want to enable equally independent workflows, rather than (supposed) stronger technical qualities.

---

I have come to believe that the benefits of microservices vs a monolith are mostly organizational, rather than technical

This doesn’t make them less important, though.

As by Conway’s Law, your software design structure gets eventually shaped around your team’s communication structure.

So, if your team is large and you want to organize it around small independent teams, you may need to gravitate towards a service-based architecture.

The opposite is also true: you won’t probably get the full benefits of microservices as long as your team stays a single large unit.

The overhead will not be worth it if it is not matched by the communication benefits brought by autonomous teams.

It seems to me that a solid recipe for any team might be to focus on modularity, and spin off independent services whenever you want to enable independent workflows, rather than (supposed) stronger technical qualities.
