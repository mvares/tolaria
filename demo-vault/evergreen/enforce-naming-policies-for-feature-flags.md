---
aliases:
  - "Enforce naming policies for feature flags"
"Is A":
  - Evergreen
"Created at": "2024-04-18T14:44:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to": "[[Feature Flags / Feature Management]]"
"Old Created At": "2022-07-21T16:30:00.000+02:00"
"Updated at": "2024-04-19T09:37:00.000Z"
Status: Not started
notion_id: 08b4301a-998f-4dc4-b2c4-1d0aa71568b2
---

# Enforce naming policies for feature flags

You should enforce a clear policy about naming flags, to avoid *naming hell *later. Here are two tips:

- **Create buckets **— create bucketing rules that adapt to your workflow. You can use names of modules, parts of products, or totally made up categories. The ideal criterion should be 1)  easy to apply at all times, and 2) should stand the test of time. 

- **Separate permanent and temporary flags **— most teams have temporary flags for testing purposes and permanent ones for general feature mgmt. These have totally different goals, and you should separate them. You may explicitly *flag *temporary flags (hehe) to 1) remember to delete them, and 2) keep them separated from the rest.
