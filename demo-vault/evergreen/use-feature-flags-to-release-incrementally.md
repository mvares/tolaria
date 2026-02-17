---
aliases:
  - "Use feature flags to release incrementally"
"Is A":
  - Evergreen
"Created at": "2024-04-18T14:44:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to": "[[essay/do-you-really-need-a-staging-environment|Do you really need a Staging environment?]]"
"Old Created At": "2022-05-21T14:38:00.000+02:00"
"Updated at": "2024-04-19T09:37:00.000Z"
Status: Discarded
notion_id: 5c5cbf31-f70f-496b-a187-b0dc226fab88
---

# Use feature flags to release incrementally

Feature flags are a way to enable / disable features without making a new release. 

With feature flags, you can deploy some code and verify its behaviour before tuning it on to all users, or turn off a feature that performs unexpectedly without rolling back the code.

By gating features that are not ready for public viewing, you can merge code earlier and make incremental releases, reducing the risk of each release even without a Staging environment.

[LaunchDarkly](https://launchdarkly.com/) is the most popular tool I know of for managing feature flags. You can also check out [their guide](https://launchdarkly.com/blog/what-are-feature-flags/) to learn more about feature flags in general.
