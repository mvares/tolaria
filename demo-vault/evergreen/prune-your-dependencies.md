---
aliases:
  - "Prune your dependencies"
"Is A":
  - Evergreen
"Created at": "2024-04-18T14:44:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to":
  - "[[essay/new-tools-and-techniques-for-2024|New Tools and Techniques for 2024]]"
  - "[[monday-ideas/monday-90|Monday #90]]"
"Old Created At": "2024-01-24T09:25:00.000+01:00"
"Updated at": "2024-04-19T09:37:00.000Z"
Status: Not started
notion_id: e39dece9-6d6e-4e73-84f7-aa2e539fe352
---

# Prune your dependencies

Most applications today have just too many dependencies. Dependencies spread out for many reasons:

- Templates and boilerplates bring in stuff that you don’t use.

- Different teams use different libraries for the same purpose (e.g. HTTP calls).

- Dependencies from dead or pruned code are never removed (”*maybe this is used elsewhere?*”)

The proliferation of dependencies, in turn, brings various problems:

- 🔒 **Security** — they increase your application’s attack surface.

- 🚚 **Release** — they increase build and deploy times.

- 🔧 **Maintenance** — they require constant work to be kept up to date.

So, the best way to keep your footprint small is prevention:

- Create a developer portal to keep consistency across teams (e.g. with [Backstage](https://backstage.spotify.com/)).

- Explicitly favor using libraries you already use, instead of new ones (e.g. you can write this down in your design doc template).

- Whenever you remove some code, check if you can remove some dependency.

On top of this, you can also do periodic clean-ups — e.g. once a quarter — where the whole team spends a few days squashing unused / redundant dependencies. Or, if you do [bug duty](https://refactoring.fm/i/139963364/bug-duty), you can make dependency pruning part of the duties.
