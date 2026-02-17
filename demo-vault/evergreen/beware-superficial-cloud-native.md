---
aliases:
  - "Beware superficial cloud native"
"Is A":
  - Evergreen
Tags:
  - Not for Monday
"Created at": "2024-04-18T14:44:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to": "[[essay/a-tech-radar-for-2023|A Tech Radar for 2023]]"
"Old Created At": "2023-02-16T15:07:00.000+01:00"
"Updated at": "2025-02-19T10:12:00.000Z"
Status: Not started
notion_id: e566940c-1bbf-4d1d-9fab-e66fd8567208
---

# Beware superficial cloud native

Cloud providers today have a strong influence on how applications are designed.

That’s because, over time, they gradually expanded from simply **renting servers** to people, to running **managed services** that you can use like building blocks for composing your software.

Since these services are **well-designed in isolation**, you may be fooled into thinking that by taking many of them and combining them you will *naturally *end up with a good design.

This is wrong, of course, and lies at the core of many mistakes people make with trendy patterns like **microservices**, **serverless**, and more.

Cloud services provide real, tangible benefits, but they should *support* your system design — which is largely independent from them — rather than the other way around.

You can find more ideas about cloud, monoliths and microservices, in these recent articles:

- 🗿 [**Monoliths vs Microservices**](https://refactoring.fm/p/monoliths-vs-microservices)

- ☁️ [**Cloud vs On-premise Infrastructure**](https://refactoring.fm/p/cloud-vs-on-premise)
