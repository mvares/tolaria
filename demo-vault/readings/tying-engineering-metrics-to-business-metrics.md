---
aliases:
  - "Tying Engineering Metrics to Business Metrics"
"Related to": "[[readings-digest/weekly-digest-3|Weekly Digest #3]]"
Summary: This article explains how engineering metrics connect to important business metrics like revenue and customer retention. It highlights that tracking engineering performance can help identify issues early and improve customer satisfaction. By understanding these connections, engineering leaders can better support business goals.
"Discarded for digest?": false
"Note Status": Saved
URL: "https://icchasethi.medium.com/tying-engineering-metrics-to-business-metrics-f4df7651e026"
Author: Iccha Sethi
Category: Articles
"Full Title": Tying Engineering Metrics to Business Metrics
Highlights: 12
"Last Synced": 2025-12-10
"Last Highlighted": 2025-11-13
notion_id: 2c5bdf02-815c-818b-baa0-fde251554b2d
---

# Tying Engineering Metrics to Business Metrics

this isn’t an exhaustive list of engineering metrics, the goal is to provide a practical framework that you can adapt to your context. ([View Highlight](https://read.readwise.io/read/01k9z2npfqvnrxqjbysfxwz0qt))

Key Business Metrics ([View Highlight](https://read.readwise.io/read/01k9z2p0wper3xdp28rxn80j79))

Below are some key business metrics that most business use:
**ARR (Annual Recurring Revenue):** The total recurring revenue a company expects to receive annually from its customers. ([Wall Street Prep](https://www.wallstreetprep.com/knowledge/net-revenue-retention-nrr/))
**NRR (Net Revenue Retention):** A metric that measures the percentage of recurring revenue retained from existing customers over a specific period, accounting for expansions, contractions, and churn. ([Planhat](https://www.planhat.com/thought-leadership/gross-revenue-retention-vs-net-revenue-retention))
**GRR (Gross Revenue Retention):** The percentage of recurring revenue retained from existing customers over a specific period, excluding any revenue gained from expansions or upsells. ([ChurnZero](https://churnzero.com/blog/net-revenue-retention-vs-gross-revenue-retention-explained/))
**CAC (Customer Acquisition Cost):** The total cost incurred by a company to acquire a new customer, including marketing and sales expenses. ([Cast](https://cast.app/net-dollar-retention))
These metrics are lagging indicators, sometimes as lagging as 12 months, where a customer churns at the end of their yearly contract impacting the GRR. ([View Highlight](https://read.readwise.io/read/01k9z2pf4zzf88yjse6cyq3ajr))

High GRR and NRR reflect loyal, satisfied customers who find the product valuable, easy to use (**user experience**), and reliable (**system reliability**). These customers are more likely to expand their usage, purchase additional features, and remain long-term advocates for your platform. ([View Highlight](https://read.readwise.io/read/01k9z2ppm3t3svrq11x0gdvjyr))

To grow the business via ARR and reduce CAC simultaneously, we must prioritize shipping product features quickly (**feature velocity**) without compromising the factors that sustain GRR and NRR. ([View Highlight](https://read.readwise.io/read/01k9z2q1d0wfk5sszpscbchcpm))

Engineering Metrics (Lagging) ([View Highlight](https://read.readwise.io/read/01k9z2q6rph29cn1243njag4jm))

There are a number of engineering metrics which are lagging, but in much lesser magnitude of time than GRR/NRR/CAC/ARR. **Metrics like uptime, time to detect and recover incidents, performance, support tickets, bugs, and team velocity** can be measured over shorter timeframes. ([View Highlight](https://read.readwise.io/read/01k9z2rj3hmm8pcnw0p112wfz0))

As an engineering leader I have found that they’re most insightful when reviewed monthly and analyzed for trends over 3–6 months ([View Highlight](https://read.readwise.io/read/01k9z2rppk3dzjvw638znv1j0j))

Engineering Metrics (Leading) ([View Highlight](https://read.readwise.io/read/01k9z2rzqq2p9kv3nnyvb4ef34))

Sometimes even months might be too late to come back and fix something. ([View Highlight](https://read.readwise.io/read/01k9z2s2g5gje9wg1nxtjp9a09))

Summary ([View Highlight](https://read.readwise.io/read/01k9z2t0kgc09n7qyk22y3e0mz))

Tying these all together — short **lead time for change**, means PRs get quickly into production. This is not only amazing for **team and product velocity** because we are shipping changes quickly and get to validate them quicker in production, but also allow us to decrease our **Time to recover during incidents** by applying a fix quickly. With lower impacting incidents, means less unhappy customers which help us maintain our **GRR**. Similarly with quicker time for features to get in production, means our product has higher value quicker, thereby making it easier to gain new customers and increase our **ARR**. ([View Highlight](https://read.readwise.io/read/01k9z2t2m88v7zmnrcf4kn9vgp))
