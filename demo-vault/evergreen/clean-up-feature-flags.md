---
aliases:
  - "Clean up feature flags"
"Is A":
  - Evergreen
"Created at": "2024-04-18T14:44:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to": "[[Feature Flags / Feature Management]]"
"Old Created At": "2022-07-21T16:30:00.000+02:00"
"Updated at": "2024-09-04T09:05:00.000Z"
Status: Not started
notion_id: c1578780-992e-456a-9500-9e485419ce75
---

# Clean up feature flags

When feature flags become a first class citizen of your dev workflow, it may be hard to fight against their proliferation.

In my experience, most feature flags end up being temporary and should be deleted at some point. This is hard to perform reliably at scale, as widely reported.

To prevent *flag hell*, here are three effective strategies:

1. **Clean up branches** — whenever you create a new flag, to also create a *cleanup* branch with the code that removes the flag. You immediately submit the cleanup PR and keep it open until you are ready to remove the flag. You can reject the PR that adds the new flag if the author didn't also submit the cleanup PR.

1. **Cap to temporary flags** — you can put a cap to the number of temporary flags that can be active at any given time. When you reach the cap, whenever you would create a new one you should also remove an old one. You can easily check for this at PR time. 

1. **Clean up sprints** — if things get really bad, consider allocating dev cycles to clean up the mess. I always prefer gradual solutions that are embedded in the process, but if nothing else work, this should do the trick!
