---
aliases:
  - "Monorepos are better in 2025"
"Is A":
  - Evergreen
"Created at": "2025-04-22T13:14:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to":
  - "[[essay/good-engineering-techniques-for-2025|Good Engineering Techniques for 2025 📡]]"
  - "[[monday-ideas/monday-158|Monday #158]]"
"Updated at": "2025-05-27T14:07:00.000Z"
Status: Not started
notion_id: 1ddbdf02-815c-80eb-ae86-d06f0b8bef21
---

# Monorepos are better in 2025

I believe that today, in 2025, monorepos are the best way to organize codebases. More specifically, I believe they *a lot* better (not just a little) than polyrepos, for the vast majority of orgs.

The TL;DR is that 1) there have been historically very real pros and cons about monorepos vs polyrepos, but while today the cons of monorepos have been largely solved with tooling, the cons of polyrepos are all still out and about.

Here is a sample of the latter, paraphrased from a real-world team exploration done by [Danilo Spinelli](https://www.linkedin.com/in/danilospinelli/):

1. **Repository obsolescence and neglect** — multiple repositories often lead to some becoming obsolete or unused, and these are not always marked accordingly.

1. **Refactoring complexity** — in a poly-repo environment, tasks like library updates or major refactoring become highly complex. Each repository must be individually updated, requiring significant coordination and increasing the risk of inconsistencies and integration issues.

1. **Hard-to-propagate updates** — changes made to common packages are less visible in a poly-repo structure. This necessitates the additional steps of publishing the packages and then updating each respository with a separate pull request (PR), making the process cumbersome.

1. **Service misalignment** — due to the above, there is a high risk of software components becoming misaligned, depending on the update status of common packages.

1. **Distributed code reviews** — pull requests can be spread across multiple repos, making the review process more complex, hard to monitor and time-consuming.

1. **Duplication of settings** — essential settings like security measures, identity, and pipeline boilerplates need to be replicated in each repo. Updates to any of these common elements require refactoring across multiple repos, increasing the workload and potential for errors.

1. **Documentation challenges** — when common docs pertain to multiple components, it becomes unclear where to place them in a poly-repo setup, leading to potential accessibility and update issues.

Here is also a [detailed post-mortem](https://segment.com/blog/goodbye-microservices/) by Segment about how they moved from 100+ repositories back to a monolith+monorepo.

Monorepos have different challenges, that mostly revolve around building and continuous integration. You don’t want to re-run the whole pipeline when a small change is made. Also, each workspace has its own test suite, its own linting, and its own build process. So a single monorepo might have **thousands of tasks to execute**.

These problems, however, are largely solved by modern build tools, that *cache* the results of individual build tasks so that no work is ever done twice. For Javascript stacks, you can check out [Turborepo](https://turbo.build/).

I also wrote a more in-depth analysis of the monolith vs microservices debate (which is not the same — but is related) in this [past article](https://refactoring.fm/p/monoliths-vs-microservices).

---
