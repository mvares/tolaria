---
aliases:
  - "You should test in production"
"Is A":
  - Evergreen
"Created at": "2024-06-07T07:43:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to":
  - "[[essay/charity-majors-observability-testing-in-production|Charity Majors – Observability & Testing in Production]]"
  - "[[monday-ideas/monday-138|Monday #138]]"
"Updated at": "2025-01-07T16:27:00.000Z"
Status: Not started
notion_id: 162927b7-cf97-4f8c-b52f-c136bbb91176
---

# You should test in production

Testing in production matters because, no matter how good your staging environment is, it is never going to be exactly like prod. 

It is not possible to have the same concurrency, the same chaos, the same variability, because every moment in production is unique.

Charity says you may or may not have a staging environment — that’s up to various factors — but you can’t *not* invest in good production tooling.

Counterintuitively, the right mindset, most of the times, is to invest resources in *fixing* *problems faster*, rather than *preventing problems*.

The former leads to speed, flow, and CD. The former leads to gating, batching, and pain.
