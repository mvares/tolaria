---
aliases:
  - "Design docs are made of 3 main sections"
"Is A":
  - Evergreen
"Created at": "2024-04-18T14:44:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to":
  - "[[essay/how-to-write-design-docs|How to Write Design Docs]]"
  - "[[monday-ideas/monday-33|Monday #33]]"
"Old Created At": "2022-06-23T17:33:00.000+02:00"
"Updated at": "2024-04-19T09:37:00.000Z"
Status: Not started
notion_id: 7abdee4c-9c4d-4913-b1e0-7caa80184667
---

# Design docs are made of 3 main sections

A good design doc can be organized in three main sections:

1. 🎯 **Essentials **— things you should always include, like goals and tech design. 

1. 📝 **Disclaimers **— things you include to create alignment and guide the conversation.

1. ⏰ **Reminders **— things that “*let’s make sure we don’t forget them*”. And boy they are many.

Let’s see them 👇

#### 🎯 Essentials

You would probably remember to write these even without the template. On the flip side, you would probably remember *only* these.

- **Header **— the basics: project name, date, owner, other contributors.

- **Context **— links to other useful docs: product specs, UI/UX design, related design docs.

- **Goals** — what this design should achieve.

- **Approach / Design **— How you are going to implement the thing. Focus on materials that drive the conversation, rather than *specs*.

#### 📝 Disclaimers

People will read the *essentials* and come up with questions and ideas. That’s the whole point of the design doc.

This can be 10x more productive if you are able to anticipate such points. The best way to do this is to reason through [*inversion*](https://refactoring.fm/p/the-power-of-inversion-)* *and cover not only what you want to build, but also what you *don’t*, and why.

So here is what you may include:

- **Anti-goals** — all the things you are *not *going to achieve in this iteration. This prevents the classic objections “*I thought we would have this*” after release. 

- **Alternatives considered **— if you are discarding alternative options, list them and explain your thought process. Anticipate questions that will come from people who are checking your approach.

- **Open questions **— just like for alternatives, be transparent about points that are still open, and put them up front for discussion.

#### ⏰ Reminders

This is the “*let’s make sure we don’t forget about it*” space. Not all of sections will be relevant all the time, but it’s important to include them as placeholders. Again, checklist mentality.

- **Security / Privacy **— are there security or privacy concerns about this project?

- **Observability** — details about how you are going to instrument this system, with logging, alerts, and more.

- **Test plan** — how are you going to test this?

- **Rollout** — details about the release process. It might include plans for database migrations, feature flags, and similar activities.

- **Rollback** — what will you do if things go wrong? Can you simply rollback the code?
