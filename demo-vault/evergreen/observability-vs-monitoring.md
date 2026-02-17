---
aliases:
  - "Observability vs monitoring"
"Is A":
  - Evergreen
"Created at": "2024-06-07T07:41:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to":
  - "[[essay/charity-majors-observability-testing-in-production|Charity Majors – Observability & Testing in Production]]"
  - "[[monday-ideas/monday-131|Monday #131]]"
"Updated at": "2024-11-19T14:16:00.000Z"
Status: Not started
notion_id: 77e806b7-16d2-4d36-91b7-dc112eeaea82
---

# Observability vs monitoring

In the first part of our chat, Charity and I talked about the difference between Observability and other related concepts like *monitoring*, *APM*, and more.

Charity, who also wrote [a book](https://www.amazon.com/Observability-Engineering-Charity-Majors-ebook/dp/B09ZQ6FHTT) about it — explained how observability is a **property of complex systems**, just like scalability, or performance. Even more so, it is about *socio-technical *systems, not just your tech:

- If you **add more metrics**, you are improving observability.

- If you **educate your team** on how to ask questions about the system, you are improving observability as well.

Observability helps understand the intersection of software and users, and is like **the business intelligence of tooling**: it’s the single source of truth where you can break down, zoom in, zoom out information about your systems, together with information about your customers.

More specifically, good observability is based on three pillars:

- 📊 **Metrics **— offer insight into the health and performance of a system

- **🔀 Traces** —** **map the journey of a request or action as it moves through all the nodes of a system.

- ✏️ **Logs **— provide detailed records of events and activities within the system.

Together, these form the backbone of any observable system, enabling teams to monitor and address system issues in real-time.
