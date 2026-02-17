---
aliases:
  - "Monday #45"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-monday-idea|Publish Monday Idea]]"
Status: Published
"👓 Status": Not started
"Created time": "2024-04-18T15:09:00.000Z"
Date: 2023-04-10
"Has Notes":
  - "[[evergreen/choose-tech-based-on-importance-lock-in|Choose tech based on importance + lock-in]]"
  - "[[evergreen/the-delegation-path|The delegation path]]"
  - "[[evergreen/design-docs-are-the-most-important-tech-docs|Design docs are the most important tech docs]]"
Tags:
  - Monday
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 57da24b7-bc57-4d2a-9c9d-59b98967e0cb
---

# Monday #45

*Hey, *[*Luca*](https://twitter.com/lucaronin)* here! welcome to the ****Monday 3-2-1 ****✨*

*Every Monday I will send you an email like this with ****3 short ideas**** about engineering management, technical strategy, and good hiring.*

*You will also receive the regular long-form one on Thursday, like the last one:*

- [**How to Help Underperformers 📉**](https://refactoring.fm/p/how-to-help-underperformers)

*To receive all the full articles and support Refactoring, consider subscribing if you haven’t already!*

Become a better tech leader today ✨

[https://refactoring.substack.com/subscribe](https://refactoring.substack.com/subscribe)?

*p.s. you can learn more about the *[*benefits of the paid plan here*](http://refactoring.fm/about)*.*

---

![image](../assets/1cd0fddcc00f433a.png)

---

### 1) 🔀 The Delegation Path

One of the most popular approaches to delegation is the **Eisenhower Matrix**, which buckets your tasks in four quadrants, based on **urgency** and **importance**.

The matrix advices to address tasks based on the quadrant they are in, and, in particular, to delegate those that are **urgent + not important**. 

![The original Eisenhower matrix — you should aim to delegate everything, not just the bottom left](../assets/03d8b2e7b6034029.png)

Now, I have found this advice hard to follow in real life, for two reasons:

1. **Urgent tasks** — are often hard to delegate. Delegation is a long-term play that in the short-term may require more time/effort than doing the thing yourself.

1. **Non-important tasks** — are ok, but they are often trivial, so if you only delegate those, you are limiting people’s growth.

So, I feel like Eisenhower Matrix is just tactical advice — incomplete at best.

Instead, to look at things from a more strategic perspective, there are three angles you can use. Ask yourself these questions:

1. 🌟 **Unique value** — *Where is your time spent best? What is the unique value you bring to the table?*

1. 🎓 **Skills** — *Are there people better equipped than you at handling some of your tasks?*

1. 🌱 **Growth** — *Are there people who are eager to learn how to do some of the things you do?*

My rule of thumb is: if at least two out of three drive me away from a task, I should probably delegate it.

So, I have found that you can draw a *path* on the eisenhower matrix, that goes from the easiest + least valuable to delegate, to the hardest + most valuable **👇**

![The delegation “path of enlightenment”  ](../assets/91540855b56d4f9f.png)

1. 🥉 **Not urgent + not important** — despite what the matrix says, you can’t always *delete* these. Conversely, they are the safest and easiest to delegate.

1. 🥈 **Not important + urgent **— you need some structure already in place to delegate these in *timely* fashion, but you can still do so with little expectations on quality.

1. 🥇 **Important + not urgent **— the heart of good delegation. You need to establish what success looks like, how communication happens and who needs to be involved.

1. 🏆 **Important + urgent **— the apex of delegation. When you are able to delegate these safely, you know you made it.

More ideas on good delegation in this recent Refactoring article 👇

[https://refactoring.fm/p/how-to-delegate](https://refactoring.fm/p/how-to-delegate)

---

### 2) ✏️ Design docs are the MVP of docs

If you feel you don't write enough docs and don't know where to start, the best way is by enforcing design docs.

Design docs are the MVP of docs, where in this case MV stands for *both* **Minimum Viable** and **Most Valuable**.

A design doc illustrates the tech design and implementation strategy for a feature or component. It is meant to be created *before* you start writing code, and to be shared with other stakeholders to converge on the solution.

![image](../assets/73721fb460c34cc7.png)

You write it for several reasons:

1. 💭 **Help your reasoning** — writing is thinking. Going through the process of writing a formal document helps solidify your reasoning and come up with a better solution.

1. 🤝 **Create consensus **— align with stakeholders about what should be built, make sure important technical decisions are participated, and people feel invested in them. 

1. 🔨 **Find the best technical solution **— improve the original design through the contribution of others. Like a code review, but for the design.

1. 📓 **Record the decision **— for posterity and documentation. That includes the trade-offs you evaluated, alternative solutions you discarded, open questions, and more.

In that respect, a design doc is useful throughout the whole lifecycle of a project.

- *Before release* — it drives the process that makes people converge on a good solution.

- *After release* — it acts as decision record, that is often more useful than pure tech specs.

More ideas on how to write good design docs 👇

[https://refactoring.fm/p/design-docs](https://refactoring.fm/p/design-docs)

---

### 3) ⚔️ Boring vs exciting technology

When choosing some technology, we face the *risk *of things going wrong in some expected or unexpected ways. How should we evaluate such risk?

Any risk, including tech risk, it's about **probability * impact**. In this case, *impact* depends on two factors: 

- 💼 **How important the feature is for business **— can we afford to get this wrong, or is this mission critical?

- ⛑️ **How hard it is to recover **— how reversible is this decision? how much lock-in do we develop if we go this route?

To minimize risk, the higher the **impact**, the lower you want **probability **to be.

So, for *critical* areas where the *lock-in* is also high (e.g. database, infrastructure, payments, etc.), it is better go the safe route and choose something good but *boring*.

For *less important* areas, where your decision is also *reversible*, you can maybe afford to take a bet and choose something new and *exciting*.

![image](../assets/3d8352390f804771.png)

More ideas on how to choose technology 👇

[https://refactoring.fm/p/how-to-choose-between-boring-and](https://refactoring.fm/p/how-to-choose-between-boring-and)

---

And that’s it for today! If you are finding this newsletter valuable, consider doing any of these:

**1) ✉️ Subscribe to the newsletter** — if you aren’t already, consider becoming a paid subscriber. You can learn more about the [benefits of the paid plan here](http://refactoring.fm/about).

Get full access to Refactoring today ✨

[https://refactoring.substack.com/subscribe](https://refactoring.substack.com/subscribe)?

**2)** ❤️ **Share it** — Refactoring lives thanks to word of mouth. Share the article with your team or with someone to whom it might be useful!

I wish you a great week! ☀️

Luca
