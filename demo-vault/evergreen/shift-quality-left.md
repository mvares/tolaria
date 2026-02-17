---
aliases:
  - "Shift quality left"
Rating: Top
"Is A":
  - Evergreen
Tags:
  - Long
"Created at": "2024-09-25T09:00:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to":
  - "[[essay/how-to-do-qa-in-2024|How to do QA in 2024]]"
  - "[[monday-ideas/monday-128|Monday #128]]"
"Updated at": "2024-10-29T13:58:00.000Z"
Status: Not started
notion_id: 10cbdf02-815c-80ec-a873-dd2dc79492aa
---

# Shift quality left

Code (and product) quality is a holistic virtue that comes from taking care of things at all stages. If you think you can take care of quality simply through good QA or code reviews, you are mistaken.  

The best teams I know guarantee high quality throughout all the development stages, not just at the end. Here is what they do:

#### 1) Great integration testing 🔍

You obviously don’t want to catch integration errors with end-to-end testing.

Integration tests are 10x easier to write and maintain than end-to-end, so you should invest in the former to minimize the need for the latter.

#### 2) Zero-defect policy 🐛

Foster a culture where bugs are fixed asap, even if low-priority. This is a no-brainer: having few-to-none known defects at any given time makes your testing more reliable and improves the morale of your team (no deadly maintenance backlog).

It also makes it easier to identify and focus on new bugs when they come up. 

#### 3) Good observability + testing in prod 📊

I am a firm believer that engineers should *own* the code they write even after it gets to prod. They should use good observability tools to verify that everything works as intended, and catch bugs early.

As we discussed [with Charity Majors](https://refactoring.fm/p/observability-and-testing-in-production?utm_source=publication-search) a few months back, modern tooling today allows for an unprecedented level of inspection, and this should be totally owned by the same engineers who write the code.

#### 4) Get engineers invested in quality 🏆

The strategies above may look easy or hard to you based on how much *quality* already belongs to your team’s culture. If the answer is “*not much*”, the good news is there are practical things you can do to steer the ship.

Here is what worked for people in the community:

- 💫 **Get buy-in about changing your culture** — get your team on board with improving. One participant of the mastermind described running a workshop with their team, getting them to describe what they were currently known for as a team (”*releasing buggy software”*) and what they wanted to be known for (”*releasing reliable software”*).

- 🧑‍💻 **Expose devs to consequences** — give engineers more exposure to the consequences of bugs. This can be done in many ways: making engineers spend some time on customer support, sharing stories about the impact of bugs on users, or involving engineers in calls with users where issues are discussed. Nobody wants to ship a shitty experience.

- 🔍 **Make testing a first-class citizen of your process** — have conversations to plan how features will be tested. Setup checklists and templates (e.g. in your design docs) to make expectations clear.

- ❤️ **Show that you care **— finally, if you are a manager, show your team that quality is important to you. Reflect on how you express this, in terms of what you talk about, what you praise, and what you criticise. 
