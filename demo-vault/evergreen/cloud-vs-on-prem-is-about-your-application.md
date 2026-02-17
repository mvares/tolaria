---
aliases:
  - "Cloud vs on-prem is about your application"
"Is A":
  - Evergreen
Tags:
  - Long
"Created at": "2024-04-18T14:44:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to":
  - "[[essay/cloud-vs-on-premise-infrastructure|Cloud vs on-premise infrastructure]]"
  - "[[monday-ideas/monday-69|Monday #69]]"
"Old Created At": "2022-12-23T16:19:00.000+01:00"
"Updated at": "2024-04-19T09:37:00.000Z"
Status: Not started
notion_id: 0ae67698-0e9d-475b-9764-ae6bed24039d
---

# Cloud vs on-prem is about your application

Qualities and requirements of your application make for a big chunk of what you should take into account for choosing the right infrastructure approach. Let’s see a few elements.

#### 🏗️ Complexity

Complexity is about your system design. 

Simply put, the higher the complexity of your design, the better cloud solutions look, because you can leverage managed services — like, running your queues on SQS, or storage on S3.

Cloud services are specialized and play nicely together. In the classic tradeoff between cost and ease of use/maintenance, managed services present the most compelling arguments vs if you just rented servers on the cloud.

> *The worst error you can make is to consider the cloud environment simply as a remote datacenter, moving your product on EC2s as if they were bare metal servers. Cost comparison between the on-prem and the cloud would always be in favor of the former*.

####  Traffic

Traffic by itself may not be incredibly hard to manage. While more traffic naturally leads to more complexity, the *amount* of load is not conclusive on how much work it brings, or whether on-prem is better or worse than cloud.

This tradeoff instead depends more on how your traffic *changes *over time.

- 📈 **Growth** — how much your traffic changes in the **mid/long term**.

- 📊 **Spikiness **— how much your traffic changes in the **short term**.

The cloud tradeoff here is about elasticity. Cloud resources are naturally more elastic than on-premise ones, both in the short and long term.

- In the short term you benefit from reactivity and auto-scaling. 

- In the long term you benefit from being able to reconfigure your system more easily than if you had committed on a specific set of machines you own.

#### ⚡ Performance

Performance needs may also affect your infrastructure choices.

You can meet low response times with any infra setup, but you probably need the cloud if your audience is *also* widely distributed geographically.

Truth to be said, though, most applications don’t have this problem. Chances are your performance constraints aren’t so strict, and you can meet them with any setup, plus maybe a CDN on top.

#### 👑 Data Sovereignty

Finally, you may have legal and compliance constraints about where your data lives. Data may need to live in specific countries, and/or you may need to exhibit various degrees of ownership.

Such constraints may limit what services you are able to use, and impact your choices.
