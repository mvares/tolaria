---
aliases:
  - "Self-hosting LLMs vs APIs"
"Is A":
  - Evergreen
"Created at": "2024-04-18T14:44:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to":
  - "[[essay/how-to-embed-llms-into-your-tech-stack|How to embed LLMs into your tech stack]]"
  - "[[monday-ideas/monday-96|Monday #96]]"
"Old Created At": "2024-01-18T11:00:00.000+01:00"
"Updated at": "2024-04-19T09:37:00.000Z"
Status: Not started
notion_id: 62d59f7d-4b39-4fbe-a034-e2e500f8f827
---

# Self-hosting LLMs vs APIs

### 🖥️ Self-hosting vs APIs

One of the most frequent questions I hear about integrating LLMs is whether to go the OpenAI route (or the likes), using their APIs, or hosting an open-source system yourself (e.g. Llama).

APIs of course win the *ease of use* and *time to market* arguments, but what about other factors?

#### 1) Cost & Skills

Counterintuitively, **self-hosting LLMs doesn’t typically save money** over using APIs. OpenAI’s pricing is extremely aggressive, and their team is world-class at optimizing the use of hardware.

For example, hosting a Llama node on a suitable AWS instance would likely cost you around **$8-10 / hour**, which means it would lose money on anything but high-load workflows.

And even in high-load cases, the cost upside is unclear when you factor in maintenance, which requires strong technical expertise. If you don’t have such expertise in-house, self-hosting is out of the question.

#### 2) Privacy & Security

Solid arguments for self-hosting are, instead, **privacy and security** concerns.

While you can opt out of letting OpenAI use your conversations’ data for future training, I completely understand companies who are uneasy at *firehosing* vast amounts of private information (possibly including their customers’) to an aggressive startup.

So, if privacy matters to you, self-hosting an LLM may be worth the hassle.
