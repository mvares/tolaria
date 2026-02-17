---
aliases:
  - "Beware SPA by default"
"Is A":
  - Evergreen
"Last Tweeted": 2023-06-07
"Created at": "2024-04-18T14:44:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to":
  - "[[essay/a-tech-radar-for-2023|A Tech Radar for 2023]]"
  - "[[monday-ideas/monday-72|Monday #72]]"
"Old Created At": "2023-02-16T15:07:00.000+01:00"
"Updated at": "2024-04-19T09:37:00.000Z"
Status: Not started
notion_id: a3990a6e-cdc5-4549-8a18-247d022dd7e6
---

# Beware SPA by default

There has been a tendency in recent years to use SPAs (*single page applications*) as the **default architectural choice** for frontend applications.

While SPAs are of course not wrong *per-se*, I feel many people choose them without being aware of the **set of tradeoffs** they are getting themselves into.

SPAs are **challenging** in many departments, like SEO, initial loading times, fine-grained analytics, browser history management, and more. So, based on your requirements, they may or may not be the best architectural choice for your app.

In recent years, interesting frameworks like [Hotwire](https://hotwired.dev/) and [Remix](https://remix.run/) have come up with strategies to keep navigation and more business logic on the server, while still enabling good user experience. You should check them out!
