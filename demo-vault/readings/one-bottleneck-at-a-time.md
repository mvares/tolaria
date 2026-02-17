---
aliases:
  - "One Bottleneck at a Time"
"Related to": "[[readings-digest/weekly-digest-9|Weekly Digest #9]]"
"Reading time": 10 min
Summary: Focus all your effort on fixing the biggest bottleneck in your team or organization. Improving other areas first only creates delays and piles up work. Fix one constraint at a time, then find the next and repeat to increase overall output.
"Discarded for digest?": false
Notes: "[[evergreen/there-is-only-one-bottleneck|There is only one bottleneck]]"
"Note Status": Evergreened
URL: "https://theengineeringmanager.substack.com/p/one-bottleneck-at-a-time"
Author: James Stanier
Category: Articles
"Full Title": One Bottleneck at a Time
Highlights: 8
"Last Synced": 2026-01-19
"Last Highlighted": 2026-01-19
notion_id: 2ecbdf02-815c-81f5-bb9b-e87783191581
---

# One Bottleneck at a Time

there’s always one constraint that matters most, and focusing elsewhere is, at best, wasted effort. ([View Highlight](https://read.readwise.io/read/01kf8dzcx0fb5j0hqhew0mhbt3))

systems have a particular property: at any given time, there is only one *bottleneck* that is limiting the throughput of the whole thing. ([View Highlight](https://read.readwise.io/read/01kf8e0nh975nv7p8pqk3byfph))

Improving anything other than that constraint doesn’t improve the system. It just creates inventory, and inventory is bad because it creates blockages. ([View Highlight](https://read.readwise.io/read/01kf8e2csw00v7qv5hznwgs99h))

Goldratt outlines five focusing steps:
1. Identify the constraint.
2. Make sure it’s not being wasted on unnecessary work.
3. Subordinate everything else to it.
4. Elevate it if needed (invest to increase its capacity).
5. Repeat. ([View Highlight](https://read.readwise.io/read/01kf8e2wfhtxb3b9sregr8z81d))


In software teams, this pattern shows up everywhere: pull requests pile up waiting for review, features sit in staging for weeks waiting for QA, decisions stall because they’re waiting for leadership sign-off, and engineers are blocked because specs aren’t ready. ([View Highlight](https://read.readwise.io/read/01kf8e3nsgtg7tm3j6xahe730a))

Let’s work through an example. Imagine that in your organisation, deployments are slow, painful, and risky. Because of past incidents, you’ve increased the number of manual checks and gates for every deploy, and now you’re only deploying once every two weeks. Engineers see it as a platform problem, while the platform team sees it as an engineering problem, since they need to up their quality and stop breaking things. Therefore, it sits unfixed: it’s not glamorous work, it’s not anyone’s specific responsibility, and the company is afraid of change in case things break even more. ([View Highlight](https://read.readwise.io/read/01kf8e657xyggqjys30k77vyqb))

spend five minutes thinking about your team, your department, and your company. At each level, write down what you think the biggest bottleneck is to going faster right now. Then write down what you could do actionably to fix it. ([View Highlight](https://read.readwise.io/read/01kf8e81y47g33tw48ep318x2a))

At the *team* level, perhaps your test suite is slow and flaky, and all of the onus is being put on the QA engineer to fix it while the other engineers don’t think it’s their problem. The action here is to have all of the engineers pivot their time to speeding up the test suite together, rather than leaving it to one person. ([View Highlight](https://read.readwise.io/read/01kf8e8rqzgcxa2fgm2nj9wdsd))
