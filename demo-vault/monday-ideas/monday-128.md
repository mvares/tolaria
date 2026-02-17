---
aliases:
  - "Monday #128"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-monday-idea|Publish Monday Idea]]"
Status: Published
"👓 Status": Not started
"Created time": "2024-10-29T13:53:00.000Z"
Date: 2024-10-29
"Has Notes":
  - "[[evergreen/shift-quality-left|Shift quality left]]"
  - "[[evergreen/principles-create-alignment-and-enable-autonomy|Principles create alignment and enable autonomy]]"
  - "[[evergreen/merchants-of-complexity|Merchants of complexity]]"
Tags:
  - Monday
  - Free
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 12ebdf02-815c-8006-ab28-e1ad23567dc0
---

# Monday #128

### 1) 🏯 Beware of *merchants of complexity*

In our recent [interview with David Heinemeier Hansson](https://refactoring.fm/p/merchants-of-complexity-with-dhh), we discussed the concept of "merchants of complexity" in the software industry, which David wrote about in a [recent blog post](https://world.hey.com/dhh/merchants-of-complexity-4851301b).

David argues that companies that **profit from complicated layering** have an incentive to maintain it. This creates a conflict between simplifying software and sustaining a business model based on such complexity.

This is why—David explains—he never commercialized his work on Rails:

> *I knew that I could have all these noble ideals about how we should build software and we should keep it simple and we should compress complexity instead of layering it away. And I'd go like, all that would eventually disappear because the incentives of needing to sustain and grow a business would overwhelm that.*

By keeping Rails as an open-source project, separate from his commercial ventures, David can maintain his focus on simplicity and complexity *compression*, without the pressure to monetize the framework directly.

The interview is chock-full of stories and insights — you can find it below 👇

[https://refactoring.fm/p/merchants-of-complexity-with-dhh](https://refactoring.fm/p/merchants-of-complexity-with-dhh)

---

### 2) 🔨 Good principles are about the *how*

Many companies do not invest in creating a set of engineering principles, because they are confused as to why they should be useful.

My simple answer for that is that principles describe *how* decisions should be made.

Why does that matter?

Without principles, you might meet goals in a way that doesn't reflect your culture:

- Engineers might deliver features... without peer review

- Managers might meet deadlines... by making people overwork

- Teams might go fast... cutting corners on security and accessibility

Principles are a set of shared beliefs that create alignment over *how* you do things in your company.

They are, simultaneously:

1. 👌 A definition of what good looks like

1. 🗣️ A shared language to be used in daily work

In other words, they create alignment and enable autonomy.

![image](../assets/12ebdf02815c807e.png)

You can find our full article about engineering principles below 👇

[https://refactoring.fm/p/principles](https://refactoring.fm/p/principles)

---

### 3) ⬅️ Shift code-quality left

Code (and product) quality is a holistic virtue that comes from taking care of things at all stages. If you think you can take care of quality simply through good QA or code reviews, you are mistaken.  

The best teams I know guarantee high quality throughout all the development stages, not just at the end. Here is what they do:

#### Great integration testing 🔍

You obviously don’t want to catch integration errors with end-to-end testing.

Integration tests are 10x easier to write and maintain than end-to-end, so you should invest in the former to minimize the need for the latter.

#### Zero-defect policy 🐛

Foster a culture where bugs are fixed asap, even if low-priority. This is a no-brainer: having few-to-none known defects at any given time makes your testing more reliable and improves the morale of your team (no deadly maintenance backlog).

It also makes it easier to identify and focus on new bugs when they come up. 

#### Good observability + testing in prod 📊

I am a firm believer that engineers should *own* the code they write even after it gets to prod. They should use good observability tools to verify that everything works as intended, and catch bugs early.

As we discussed [with Charity Majors](https://refactoring.fm/p/observability-and-testing-in-production?utm_source=publication-search) a few months back, modern tooling today allows for an unprecedented level of inspection, and this should be totally owned by the same engineers who write the code.

#### Get engineers invested in quality 🏆

The strategies above may look easy or hard to you based on how much *quality* already belongs to your team’s culture. If the answer is “*not much*”, the good news is there are practical things you can do to steer the ship.

Here is what worked for people in the community:

- 💫 **Get buy-in about changing your culture** — get your team on board with improving. One participant of the mastermind described running a workshop with their team, getting them to describe what they were currently known for as a team (”*releasing buggy software”*) and what they wanted to be known for (”*releasing reliable software”*).

- 🧑‍💻 **Expose devs to consequences** — give engineers more exposure to the consequences of bugs. This can be done in many ways: making engineers spend some time on customer support, sharing stories about the impact of bugs on users, or involving engineers in calls with users where issues are discussed. Nobody wants to ship a shitty experience.

- 🔍 **Make testing a first-class citizen of your process** — have conversations to plan how features will be tested. Setup checklists and templates (e.g. in your design docs) to make expectations clear.

- ❤️ **Show that you care **— finally, if you are a manager, show your team that quality is important to you. Reflect on how you express this, in terms of what you talk about, what you praise, and what you criticise. 

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
