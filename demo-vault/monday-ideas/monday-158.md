---
aliases:
  - "Monday #158"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-monday-idea|Publish Monday Idea]]"
Status: Published
"👓 Status": Not started
"Created time": "2025-05-27T13:43:00.000Z"
Date: 2025-06-02
"Has Notes":
  - "[[evergreen/from-ic-to-em-is-like-from-player-to-coach|From IC to EM is like from player to coach]]"
  - "[[evergreen/monorepos-are-better-in-2025|Monorepos are better in 2025]]"
  - "[[evergreen/career-frameworks-with-just-1-track|Career frameworks with just 1 track]]"
Tags:
  - Monday
  - Free
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 200bdf02-815c-8036-adc5-d22dac2826f0
---

# Monday #158

### 1) From player to coach 🏀

I am a sports fan, and I like to think at the transition from IC to manager, like the one from being a player to being a coach. In fact, things that make you effective as a coach are often quite different from those that make you effective as a player.

Let’s dissect this a bit, using basketball as an example:

- **🏀 As a player** — you’re on the court. You’re responsible for executing plays and defending effectively. You may be the captain, in which case you’ll also make decisions in real-time on which plays to execute throughout the game.

- 👔 **As a coach** — you’re off the court. You set the strategy for the game, and build the plays that the team executes. You’re responsible for ensuring your team is healthy and strong – physically and mentally. And, when the game is not going your way, you’re responsible for picking the right play and/or changing strategy accordingly.

![image](../assets/200bdf02815c80f2.png)

The best coaches differentiate themselves by coordinating their team‘s efforts and plays. Similarly, as an EM, the most effective levers you have to influence your team’s output are your **systems and** **processes**.

We talked about this several times, for example:

- **👔 **[**Changing Roles: from Engineer to Manager**](https://refactoring.fm/p/engineer-to-manager)** **— awesome guest post from my friend Louis Bennett.

- 📗 [**An Elegant Puzzle**](https://refactoring.fm/p/an-elegant-puzzle)** **— our review + summary of the masterpiece by Will Larson about Engineering Management. 

---

### 2) 🗿 Monorepos are just better 

I believe that today, in 2025, monorepos are the best way to organize codebases. More specifically, I believe they *a lot* better (not just a little) than polyrepos, for the vast majority of orgs.

The TL;DR is that 1) there have been historically very real pros and cons about monorepos vs polyrepos, but while today the cons of monorepos have been largely solved with tooling, the cons of polyrepos are all still out and about.

Here is a sample of the latter, paraphrased from a real-world team exploration done by [Danilo Spinelli](https://www.linkedin.com/in/danilospinelli/):

1. **Refactoring complexity** — in a poly-repo environment, tasks like library updates or major refactoring become highly complex. Each repository must be individually updated, requiring significant coordination and increasing the risk of inconsistencies and integration issues.

1. **Hard-to-propagate updates** — changes made to common packages are less visible in a polyrepo structure. This necessitates the additional steps of publishing the packages and then updating each respository with a separate pull request (PR), making the process cumbersome.

1. **Service misalignment** — due to the above, there is a high risk of software components becoming misaligned, depending on the update status of common packages.

1. **Distributed code reviews** — pull requests can be spread across multiple repos, making the review process more complex, hard to monitor and time-consuming.

1. **Duplication of settings** — essential settings like security measures, identity, and pipeline boilerplates need to be replicated in each repo. Updates to any of these common elements require refactoring across multiple repos, increasing the workload and potential for errors.

1. **Documentation challenges** — when common docs pertain to multiple components, it becomes unclear where to place them in a poly-repo setup, leading to potential accessibility and update issues.

Here is also a [detailed post-mortem](https://segment.com/blog/goodbye-microservices/) by Segment about how they moved from 100+ repositories back to a monolith+monorepo.

Monorepos have different challenges, that mostly revolve around building and continuous integration. You don’t want to re-run the whole pipeline when a small change is made. Also, each workspace has its own test suite, its own linting, and its own build process. So a single monorepo might have **thousands of tasks to execute**.

These problems, however, are largely solved by modern build tools, that *cache* the results of individual build tasks so that no work is ever done twice. For Javascript stacks, you can check out [Turborepo](https://turbo.build/).

I wrote a more in-depth analysis of the monolith vs microservices debate (which is not the same — but related) in this [past article](https://refactoring.fm/p/monoliths-vs-microservices).

While you can find other techniques we recommend for 2025 in our yearly tech radar below!

[https://refactoring.fm/p/the-refactoring-tech-radar-for-2025](https://refactoring.fm/p/the-refactoring-tech-radar-for-2025) 

---

### 3) 🪜 Single-track career frameworks

There is wide consensus today that companies should separate management and IC career tracks, because it’s different skills, different aspirations, etc.

Even though this is right *in principle*, there exist situations where a single track makes sense.

If you are a small team, say under 30 people, you may not need *full-time* managers and you may compress the management + tech leadership duties onto the same people.

![image](../assets/c6f9a28c41254e9b.png)

So, in such a scenario, senior engineers can only be promoted into managers.

I know, outrageous!

But in small companies there might be no way for an IC to progress further, because you simply don’t have the kind of work for which you need Staff+ Engineers.

- Will all the people want to turn into managers? No!

- Are you providing equal growth opportunities to people who want to stay ICs? Also no!

And that’s fine — **not all opportunities exist everywhere at a given time**. Just be transparent about what exists in your company and what not.

I wrote more about designing career frameworks in this two part-series 👇

[https://refactoring.fm/p/career-frameworks-2](https://refactoring.fm/p/career-frameworks-2)

---

And that’s it for today! If you are finding this newsletter valuable, consider doing any of these:

**1) **🔒** Subscribe to the paid version** — if you aren’t already, consider becoming a paid subscriber. 1500+ engineers and managers have joined already! Learn more about the [benefits of the paid plan here](http://refactoring.fm/about).

Get full access to Refactoring ✨

[https://refactoring.substack.com/subscribe](https://refactoring.substack.com/subscribe)?

**2)** 🍻 **Read with your friends** — Refactoring lives thanks to word of mouth. Share the article with your with someone who would like it, and **get a free membership** through the new [referral program](https://refactoring.fm/p/referral).

Read with your friends 🍻

[https://refactoring.fm/leaderboard](https://refactoring.fm/leaderboard)

I wish you a great week! ☀️

Luca
