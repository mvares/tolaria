---
aliases:
  - "Make Staging optional"
Rating: Top
"Is A":
  - Evergreen
"Last Tweeted": 2022-07-08
"Created at": "2024-04-18T14:44:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to":
  - "[[essay/do-you-really-need-a-staging-environment|Do you really need a Staging environment?]]"
  - "[[monday-ideas/monday-116|Monday #116]]"
"Old Created At": "2022-05-21T14:39:00.000+02:00"
"Updated at": "2024-08-29T09:15:00.000Z"
Status: Not started
notion_id: fee9f802-8d89-4fa0-b48e-476ac2137f1a
---

# Make Staging optional

I know I have quite radical views about simplifying release pipelines.

For example, I try as much as possible to remove Staging environments and make devs push straight to production.

However, this doesn't need to be a black / white decision — you can go step by step 👇

Let’s say you analysed your workflow and figured out that:

1. a large chunk of changes could go straight to prod

but

1. there is a 20% of cases where you still need staging

What do you do?

The easiest improvement you can make is to turn staging into an *optional* step of your release process.

You separate the staging workflow from your main branching strategy, and give developers the agency to choose to either deploy to production or test on staging first, based on risk and complexity.

For many teams, this is:

1. easy to do

1. it builds ownership, and

1. it gets 80% of results with 20% of the effort

Super win!

Sometimes, when we design processes, we limit ourselves by thinking that things can only be either always or never.

There are often good solutions in between.

I wrote more ideas about staging environments here 👇

[https://refactoring.fm/p/do-you-need-staging](https://refactoring.fm/p/do-you-need-staging)
