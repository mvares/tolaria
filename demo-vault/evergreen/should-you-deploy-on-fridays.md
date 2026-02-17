---
aliases:
  - "Should you deploy on Fridays?"
"Is A":
  - Evergreen
"Created at": "2024-04-18T14:44:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to":
  - "[[Feature Flags / Feature Management]]"
  - "[[monday-ideas/monday-73|Monday #73]]"
"Old Created At": "2023-03-20T10:39:00.000+01:00"
"Updated at": "2024-04-19T09:37:00.000Z"
Status: Not started
notion_id: 3ed97669-b37e-4516-ab32-83fc5b074e1b
---

# Should you deploy on Fridays?

### 🔥 Should you release on Fridays?

This is a complicated question that has no singular answer. 

My take is that wellbeing of your team should be your #1 concern, so if your folks don’t feel confident, you shouldn’t release. Full stop.

If you find yourself in this situation, though, you should investigate *why* it is so. You can and should work to build that confidence, knowing that the best engineering teams make no difference between Fridays, Mondays, or Thursdays.

To get you closer, here are a few things you may consider:

- 🌅 **Release in the morning **— with good observability in place, you can catch 95% of issues within a few hours.

- 🚩 **Release behind a feature flag **— push the code but keep it disabled.

- 🔒 **Release to a beta group **—make the update available only to a subset of users, which dramatically reduces the risk.

- 🐛 **Do quality Fridays **— you can use Fridays to squash bugs and do some maintenance, which is low-risk stuff to release.

So, your mileage may vary, but just know that *never* deploying on Fridays has hidden costs:

1. You will batch more stuff together and have a riskier deploy on Monday, and 

1. People will have lost some context and debugging will be harder.

More on maintenance and feature flags 👇

[https://refactoring.fm/p/feature-flags](https://refactoring.fm/p/feature-flags)

[https://refactoring.fm/p/how-to-plan-for-maintenance](https://refactoring.fm/p/how-to-plan-for-maintenance)
