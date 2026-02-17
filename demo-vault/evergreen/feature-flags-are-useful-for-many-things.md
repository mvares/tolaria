---
aliases:
  - "Feature flags are useful for many things"
"Is A":
  - Evergreen
"Created at": "2024-04-18T14:44:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to": "[[Feature Flags / Feature Management]]"
"Old Created At": "2022-07-21T16:28:00.000+02:00"
"Updated at": "2024-04-19T09:37:00.000Z"
Status: Not started
notion_id: a0b171df-948d-4a93-a079-6467a606cdbc
---

# Feature flags are useful for many things

#### 1) Trunk-based dev

[Untitled](https://www.notion.so/872af996e38547858e82338840078b75) 

#### 2) Gradual rollouts

You can make a newly released feature available only to a small subset of users, to reduce risk.

This can be implemented with most feature flag systems, which can be also configured to gradually expand the subset, up to a 100% rollout.

#### 3) Kill switch

You can instantly disable features that are behaving unexpectedly, without rolling back the code. 

This further decreases the risk of each release, to the point where it’s not uncommon for teams that make heavy use of feature flags to skip the staging environment and deploy directly in production 👇

[https://refactoring.fm/p/do-you-need-staging](https://refactoring.fm/p/do-you-need-staging) 

#### 4) A/B tests

Similarly to gradual rollouts, you can A/B test new changes to check their impact on business KPIs.

#### 5) Access control

If you have different customer tiers which should access different sets of features, you can use feature flags to implement access control.

**Alex Stoia**, CTO at Innertrends, told me how they do it 👇

> *We use feature flagging quite often, it's integral to our development and deployment process. But in our case it's directly tied to our internal permissions system which handles 'who can access what'. For us a feature is something that eventually would be included in the permissions system so why not included from the start?

This way, if something is in working or not ready yet, no one has permission to access it (or see it), in alpha testing only a few clients have access to it, and so on. And this is easily controlled from an administration page.*

#### 6) Feature management

Gradual rollouts, kill switches and access control allow for a granular control of a feature life cycle. This whole practice is sometimes called *feature management.*

For companies who run features this way, it becomes a central part of their workflow. 

**Chiamaka Nwolisa**, Software Engineer at HelloFresh, explains their vast usage of feature flags

> *At my current company (>1000 engineers), we basically **hide 99% of features** behind feature flags.*
