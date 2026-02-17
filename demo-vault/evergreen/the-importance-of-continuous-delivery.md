---
aliases:
  - "The importance of continuous delivery"
Rating: Good
"Is A":
  - Evergreen
"Created at": "2024-06-07T07:42:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to":
  - "[[essay/charity-majors-observability-testing-in-production|Charity Majors – Observability & Testing in Production]]"
  - "[[monday-ideas/monday-114|Monday #114]]"
"Updated at": "2024-08-29T09:17:00.000Z"
Status: Not started
notion_id: c0b0ad77-b95d-4b66-8290-6bcb5d424315
---

# The importance of continuous delivery

In our recent interview with Charity Majors we talked about continuous delivery and how this is *enabled* by good observability. In fact:

1. Good observability == being able to get **closer conversations with code**, plus drawing correlation with business value.

1. Closer conversations with code allow to tell at a glance **when something is not working**.

1. Spotting problems fast grows the confidence to **ship many times a day**.

This virtuous cycle, however, can only happen when you get the code out in real environments in a small enough amount of time that engineers still have all that context in their head, so they go and check production against the instrumentation.

Charity goes even further and says that, as an engineer, your job isn’t over until you have looked at production to see that everything works.

This is the natural evolution of *integrated teams*, which went through various stages:

1. **Testing** — it used to be that QA ran all the tests → until we figured out it’s better if engineers do so.

1. **DevOps** — it used to be that ops people were separate from devs → until we figured out they should not.

1. **Observability** — it used to be that engineers job was over when they pushed their code → until we figured out it’s better if they look at how it works in prod.

#### Death Spiral 💀

Conversely, when you don’t get code out fast, and you don’t get it out automatically, you enter the **software engineering death spiral**, where everything starts taking a longer time. 

Code reviews take longer. Disks get larger. So people back up more. So they end up switching projects more. So they are waiting on each other more. Then you need a release engineering team and SRE team. Then you start batching releases, which further increases risk.
