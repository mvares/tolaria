---
aliases:
  - "Monday #60"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-monday-idea|Publish Monday Idea]]"
Status: Published
"👓 Status": Not started
"Created time": "2024-04-18T15:09:00.000Z"
Date: 2023-07-17
"Has Notes":
  - "[[evergreen/design-for-simplicity-defer-commitment|Design for simplicity (defer commitment)]]"
  - "[[evergreen/organize-docs-by-projects-and-areas|Organize docs by projects and areas]]"
  - "[[evergreen/80-of-building-features-is-non-functional-work|80% of building features is non-functional work]]"
Tags:
  - Monday
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 4df5f431-fe4d-40bf-b80a-9904e2aaf8d0
---

# Monday #60

*Hey, *[*Luca*](https://twitter.com/lucaronin)* here! Welcome to the ****Monday Ideas ***💡

*Every Monday I will send you an email like this with ****3 short ideas**** about making great software, working with humans, and personal growth.*

*You will also receive a long-form, original article on Thursday, like the last one:*

- [**How to Automate Work with Low-code**](https://refactoring.fm/p/how-to-automate-work-with-low-code)** 🔌**

*To receive all the full articles and support Refactoring, consider subscribing if you haven’t already!*

Get full access to Refactoring ✨

[https://refactoring.substack.com/subscribe](https://refactoring.substack.com/subscribe)?

*p.s. you can learn more about the *[*benefits of the paid plan here*](http://refactoring.fm/about)*.*

---

### 🐺 QA Wolf

Now back to this week’s ideas! 👇

---

### 1) 🔮 Defer commitment

Two weeks ago [I sat down with James Cowling](https://refactoring.fm/p/james-cowling), former Senior Principal Engineer at Dropbox, and we had a great chat about various topics.

James joined Dropbox when it had less than 100 employees, and saw it grow to more than 2000. One of the biggest challenges in engineering is retaining the ability to move fast and *evolve *systems when 1) the scale grows, and 2) product assumptions change fast as well.

James’ best advice about this is to **keep systems *****simple***.

Simplicity is about **optionality***. *The main quality of simple systems is that they are flexible — you can evolve them in many directions because you haven’t *committed* to a rigid set of abstractions.

So, whenever you are designing a feature or a system, you should aim to:

1. Deliver the highest possible value, and

1. Create the lowest possible commitment

You can think at working on a project as walking in a *cone*, where base of the cone is the design space of your final goal. Whenever you create a milestone (James calls them **stepping stones**), you are *moving closer* to the goal, but you are also *committing *to some ideas, thus reducing the possible *design space*. 

![image](../assets/f6d4e0174f394ead.png)

Good stepping stones are about making big steps while retaining as much design space as possible.

#### Type 1 vs Type 2

Another way of framing this is by using [Jeff Bezos’ mental model](https://thebusinessprofessor.com/en_US/management-leadership-organizational-behavior/type-1-and-type-2-decisions-bezos-explained) of *irreversible *(type 1) vs *reversible* (type 2) decisions. You want to be:

- *Slow and deliberate* — with type 1 decisions.

- *Quick and biased for action* — with type 2 decisions.

In engineering, complexity is what makes things *irreversible — *so you want avoid type 1 decisions as much as possible.

You can catch up with the whole chat (video + article) here 👇

[https://refactoring.fm/p/james-cowling](https://refactoring.fm/p/james-cowling)

---

### 2) ⏲️ “It should take one day!”

How many times have you heard a PM say that? Maybe replying to your estimate for some work, that looked more like “one week”.

Sometimes it is hard to communicate *why* it takes so long to build a feature. And the typical reason is that 80% of the work is *non-functional*.

For any new feature, in fact, you have to:

- Design for security and accessibility.

- Add automated tests.

- Figure out potential bottlenecks at scale.

- Add monitoring, logging, and general observability.

Then, to favor adoption, there is even more to do:

- Figuring out how to get the feature to users.

- Writing documentation (internal and external).

- Communicating that the new feature exists.

- Instrumenting the feature with adoption tracking to measure its use.

Even after releasing in production, the work doesn't stop and shifts into **maintenance** — like fixing bugs and making improvements customers are asking for.

This work only really stops if the feature/product is killed, or the company goes bankrupt!

While it may not seem plausible at first, the **total lifetime cost** of a feature might really be weeks or months of work, even for a simple one.

![image](../assets/f717ca79138f4d0c.png)

I wrote a full article about how to balance your engineering investment, and keep your sanity 👇

[https://refactoring.fm/p/engineering-investments](https://refactoring.fm/p/engineering-investments)

---

### 3) 📑 Organize docs in Projects and Areas

I am a fan of the [PARA method](https://fortelabs.co/blog/para/) by Tiago Forte for organizing information, and I have brought this to how I organize docs in my teams as well.

I believe, at a high level, you can separate between two major types of notes:

- ↕️ **Project notes** — stuff you need to deliver a project. A project is an initiative that has a beginning and an end, and potentially involves multiple areas (cross-functional). Likewise, projects may need a *diverse* set of docs, including e.g. product requirements, design docs, rollout plans, and more.

- ↔️ **Area notes** — long-lived documentation about a specific *area*. An area is anything for which you need to maintain a *standard*, and that stays relevant for indefinite time (as opposed to projects, that have an end). Engineering onboarding, database schemas, company org charts are all examples of docs that may not belong to a specific project, but rather to a long-lived area.

Most action happens in project notes, while area notes are more useful for future reference. This separation, though, is not static: after a project is delivered, you may archive most of its material, and move some of it into the respective *areas*, where it will stay useful for longer.

For example, you may move the database migration specs into the general database docs, or the PRD into the *product* area.

If your system supports it, you may *tag* content rather than actually moving it. E.g. I am a fan of using Notion for company docs because it allows you to be flexible with this and define areas and projects through *relations* and *tags*, rather than *folders*. But you can implement this in any system, like Confluence, or Google Docs.

I wrote a full guide on how to write documentation and it’s one of the most popular Refactoring articles ever 👇

[https://refactoring.fm/p/how-to-write-documentation](https://refactoring.fm/p/how-to-write-documentation)

---

### One Schema

---

And that’s it for today! If you are finding this newsletter valuable, consider doing any of these:

**1) ✉️ Subscribe to the newsletter** — if you aren’t already, consider becoming a paid subscriber. You can learn more about the [benefits of the paid plan here](http://refactoring.fm/about).

Get full access to Refactoring ✨

[https://refactoring.substack.com/subscribe](https://refactoring.substack.com/subscribe)?

**2)** ❤️ **Share it** — Refactoring lives thanks to word of mouth. Share the article with your team or with someone to whom it might be useful!

I wish you a great week! ☀️

Luca
