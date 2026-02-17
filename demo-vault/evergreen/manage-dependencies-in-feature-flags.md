---
aliases:
  - "Manage dependencies in feature flags"
"Is A":
  - Evergreen
"Created at": "2024-04-18T14:44:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to": "[[Feature Flags / Feature Management]]"
"Old Created At": "2022-07-21T16:31:00.000+02:00"
"Updated at": "2024-10-15T12:21:00.000Z"
Status: Discarded
notion_id: 0fba8b98-a552-4054-9a3a-0f09f92ba99c
---

# Manage dependencies in feature flags

When your system gets complex enough, you may find yourself with flags that depend on each other to work. There are two kinds:

1. **Nested flags** — a flag controls a feature which is a part of a larger module controlled by another flag.

1. **Coupled flags **— a feature controller by a flag that only works if something else, controlled by a different flag, is active.

Two pieces of advice here:

- **Use namespaces **— for nested flags, enforce *namespaces* to make it clear which flags are *children *of others. E.g. you may have flag “a.b.c” and flag “a.b” to make it intuitive that the former depends on the latter.

- **Avoid coupled flags** — just don’t do it. Switching a flag should always leave the system in a working state. Being loose on this rapidly turns flags into nightmare.
