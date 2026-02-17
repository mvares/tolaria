---
aliases:
  - "Monday #90"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-monday-idea|Publish Monday Idea]]"
Status: Published
"👓 Status": Not started
"Created time": "2024-04-18T15:09:00.000Z"
Date: 2024-02-12
"Has Notes":
  - "[[evergreen/prune-your-dependencies|Prune your dependencies]]"
  - "[[evergreen/the-prt-system|The PRT System]]"
  - "[[evergreen/have-11s-with-everyone-in-your-first-30-days|Have 1:1s with everyone in your first 30 days]]"
Tags:
  - Monday
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 6b184b69-3ef3-4bef-9976-d909db84c9c3
---

# Monday #90

### 1) 💬 When you are new, just talk with everyone

One of the most underrated tactics to onboard yourself well in a new company is to have 1:1s with literally *everyone* who is even remotely related to your job.

Do that in the first 30 days, and don't wait for your manager to take care of this.

How to?

Create a list of all the people in your team and key stakeholders in the company. Don't be afraid to reach out even to the manager of your manager, and others that feel "too high". Nobody ever gets pissed off for this.

Prepare some questions to make this both a moment of bonding and learning. Here are a few:

- **What should I know about the product / company / people?**

- **What is the biggest challenge that you face?**

- **What can I do to make your life easier?**

- **Who else should I talk to?**

You will be surprised by how much you can learn from people with casual chats, where there are no expectations whatsoever.

This was one of the best pieces of advice I received from Aadil during our chat last week 👇

[https://refactoring.fm/p/the-world-builder-framework-with](https://refactoring.fm/p/the-world-builder-framework-with)

---

### 2) ✂️ Prune your dependencies

Most applications today have just too many dependencies. Dependencies spread out for many reasons:

- Templates and boilerplates bring in stuff that you don’t use.

- Different teams use different libraries for the same purpose (e.g. HTTP calls).

- Dependencies from dead or pruned code are never removed (”*maybe this is used elsewhere?*”)

Keeping few dependencies is crucial, because dependencies, in turn, brings various problems:

- 🔒 **Security** — they increase your application’s attack surface.

- 🚚 **Release** — they increase build and deploy times.

- 🔧 **Maintenance** — they require constant work to be kept up to date.

The best way to keep your footprint small is prevention:

1. Create a developer portal to keep consistency across teams (e.g. with [Backstage](https://backstage.spotify.com/)).

1. Explicitly favor using libraries you already use, instead of new ones (e.g. you can write this down in your design doc template).

1. Whenever you remove some code, check if you can remove some dependency.

On top of this, you can also do periodic clean-ups — e.g. once a quarter — where the whole team spends a few days squashing unused / redundant dependencies. Or, if you do [bug duty](https://refactoring.fm/i/139963364/bug-duty), you can make dependency pruning part of the duties.

I list more techniques (and *resolutions*) you can adopt for the new year in this recent piece 👇

[https://refactoring.fm/p/new-tools-and-techniques-for-2024](https://refactoring.fm/p/new-tools-and-techniques-for-2024)

---

### 3) 🌱 The PRT System

In November last year I wrote a piece about [Personal Knowledge Management](https://refactoring.fm/p/how-i-take-notes-part-1), where I detail the workflows I use to run Refactoring — and my life.

In my workspace, I have three main buckets: 🔨 **Projects**, 🔄 **Responsibilities**, and 🏷️ **Topics **(PRT).

#### 1) 🔨 **Projects**

Projects are things I want to achieve on a defined timeframe. They have a beginning and an end, and are bigger than a single task (I can’t complete them in one sitting).

![My projects for the quarter. It’s a blend of personal + Refactoring ones](../assets/43901ffe7979465e.png)

I create 5-6 projects every quarter, and that includes both Refactoring projects and life projects, e.g. the recent relocation we did, or our honeymoon.

#### 2) 🔄 **Responsibilities**

Responsibilities are activities that I do on a regular basis, for which I need to maintain a standard. E.g. writing on social media, or running interviews with guests.

![The list of my main responsibilities for Refactoring. Sending email sequences is a good example — I do it weekly and I saved the procedure for it (with various links to substack)](../assets/a30a3b775184427b.jpg)

The defining feature of a responsibility is that it is recurring: it doesn’t have an end. So, while projects require **plans** or roadmaps, responsibilities require **procedures** about how to perform them.

I usually have a recurring task on Todoist for each responsibility, linking back to the procedure on Notion.

![Todoist task for the weekly responsibility, linked to the procedure on Notion](../assets/568d7a6c61f44bc4.jpg)

#### 3) 🏷️ **Topics**

Are areas of interest. A topic is anything that can be useful in the future. Examples are “frontend”, “no code”, or “sim racing”.

![A small sample of the No Code items. There are waaay more items than that.](../assets/443cbd6aa9b34f09.png)

Topics are the least *actionable* category. It’s stuff that I believe it is worth saving, but I have no expectation of doing anything with it in the near future.

The Projects → Responsibilities → Topics organization kind of goes from the most actionable to the least.

![image](../assets/51d293e2113f419c.jpg)

New activities always start as projects, to kick them off. Projects may eventually turn into responsibilities: e.g. I start doing paid ads (project), and eventually I need to manage them weekly (responsibility).

So, when I organize my note (check the [full article](https://refactoring.fm/p/how-i-take-notes-part-1) for more) I take those that are *unassigned — *no project, responsibility, or topic is attached — and I assign them to at least one of these buckets. Each note may belong to *either* a project or a responsibility, rarely both, and can have further topics attached.

For doing this, I use Notion. Notion can model this organization through database relationships, which is flexible and powerful in many ways. Its ability to use views, formulas, and rollups, to me, is simply unmatched.

The main drawback of Notion, if you ask me, is that it is *slow*, and a bit *cumbersome* on mobile. This would be an issue if I used it for capturing stuff, but I mostly don’t, so all good!

To me, for *organizing*, flexibility > speed.

[https://refactoring.fm/p/how-i-take-notes-part-1](https://refactoring.fm/p/how-i-take-notes-part-1)

---

And that’s it for today! If you are finding this newsletter valuable, consider doing any of these:

**1) ✉️ Subscribe to the newsletter** — if you aren’t already, consider becoming a paid subscriber. 1500+ engineers and managers have joined already! Learn more about the [benefits of the paid plan here](http://refactoring.fm/about).

Get full access to Refactoring ✨

[https://refactoring.substack.com/subscribe](https://refactoring.substack.com/subscribe)?

**2)** 🍻 **Read with your friends** — Refactoring lives thanks to word of mouth. Share the article with your with someone who would like it, and **get a free membership** through the new [referral program](https://refactoring.fm/p/referral).

Read with your friends 🍻

[https://refactoring.fm/leaderboard](https://refactoring.fm/leaderboard)

I wish you a great week! ☀️

Luca
