---
aliases:
  - "Use stacked-diffs and trunk-based dev to improve velocity"
"Is A":
  - Evergreen
"Last Tweeted": 2022-12-14
"Created at": "2024-04-18T14:44:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to":
  - "[[essay/code-reviews|Code Reviews]]"
  - "[[monday-ideas/monday-28|Monday #28]]"
"Old Created At": "2021-12-31T16:05:00.000+01:00"
"Updated at": "2024-04-19T09:37:00.000Z"
Status: Not started
notion_id: 103ba64a-9633-4c60-8c3a-f518f0347eca
---

# Use stacked-diffs and trunk-based dev to improve velocity

Many big companies like Facebook and Google have a code review workflow that is not based on PRs, but rather on **stacked diffs**.

[Embed](https://twitter.com/dan_abramov/status/1407803004183531527?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1407803004183531527%7Ctwgr%5E%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fgraphite.dev%2Fblog%2Fpost%2FDThX8ffP1gmxWJChEv0y)

Stacked diffs are a way to have your code reviewed *without* firing up a PR. You take a portion of your local changes and make it available for review. You can *stack* these changes into multiple requests for review, so you never get stuck waiting for reviews.

[Embed](https://twitter.com/alexandracoding/status/1278001790907285508?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1278001790907285508%7Ctwgr%5E%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fgraphite.dev%2Fblog%2Fpost%2FDThX8ffP1gmxWJChEv0y)

This workflow, other than being faster, allows to (mostly) get rid of branches and work in [trunk-based development](https://cloud.google.com/architecture/devops/devops-tech-trunk-based-development) mode instead. In turn, there is convincing evidence that teams who adopt trunk-based workflows achieve higher velocity and faster turnaround.

[Embed](https://twitter.com/jezhumble/status/1415908836439773185)

If this seems crazy to you, you may reflect on the fact that engineers working in some of the best companies in the world commit directly to master all the time (and often on a monorepo), unless they have a reason not to.
