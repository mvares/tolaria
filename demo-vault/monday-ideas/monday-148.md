---
aliases:
  - "Monday #148"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-monday-idea|Publish Monday Idea]]"
Status: Published
"👓 Status": Not started
"Created time": "2025-03-18T15:10:00.000Z"
Date: 2025-03-24
"Has Notes":
  - "[[evergreen/make-pr-take-minutes|Make PR take minutes]]"
  - "[[evergreen/prospect-theory|Prospect Theory]]"
  - "[[evergreen/task-relevant-maturity|Task-relevant maturity]]"
Tags:
  - Monday
  - Free
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 1babdf02-815c-8019-81fe-ee39b07e58b0
---

# Monday #148

### 1) 🔀 Avoid context switch on code reviews

Last month we published the results of our big survey on good engineering *practices*, and some interesting insights came from the time it takes to close a PR.

It looks like there are no decisive differences when the time ranges between 1 hour and 1 day, but team performance is 1) significantly better when PRs take *minutes* to get approved, and 2) significantly worse when they take *days*.

![image](../assets/197bdf02815c8059.png)

* *

Why is that? Our interpretation is the following:

- 🥇 **When a PR takes minutes** — be it because PRs are small, people pair on reviews, or everyone stops on their tracks to review code — there is little to no context switch for the submitter, which leads to less work in progress, tasks getting closed faster, and all kinds of benefits down the line.

- 🥈 **When a PR takes between 1 hour and one day** — the submitter needs to switch to other tasks. At that point whether the review takes 1 hour or, say, 4, there isn’t a lot of difference in terms of workflow.

- 🥉 **When a PR takes days** — the workflow degrades considerably as multiple changes need to get batched together, which creates more risk, more outages, rework, and a worse feedback loop.

You can find more insights in the full report 👇

[https://refactoring.fm/p/the-path-to-engineering-maturity](https://refactoring.fm/p/the-path-to-engineering-maturity)

---

### 2) 🎲 Prospect Theory

Last year we reviewed Daniel Kahneman’s masterpiece [**Thinking, Fast and Slow**](https://refactoring.fm/p/thinking-fast-and-slow?utm_source=publication-search), for the community book club.

One of the parts that stuck the most with me is **Prospect Theory**, which is regarded as one of the century’s most significant contributions to behavioral economics. This theory challenges the traditional view that people make *rational decisions* based on the final outcome of their choices.

Instead, it shows three main things:

1. ⚖️ **Relativeness** — people evaluate outcomes of gains and losses relative to a reference point, not absolute values.

1. **💸 Loss aversion** — losses hurt more than equivalent gains feel good.

1. 🧮 **Probability distortions **— we are not good at weighing probability.

By combining all three we get plenty of irrational, *asymmetric* behavior, in which people tend to be **risk-averse for gains **but** risk-seeking for losses**.

While a lot of this is conventional wisdom now, what surprised me the most is how *precise the *model is. Kahneman doesn’t only show we are biased — he shows exactly *how* biased we are.

For example, there is a stunningly precise reference table for how (badly) probabilities turns into decision weights:

<!-- Table -->

And a mathematical function to display our loss aversion:

![image](../assets/1babdf02815c80fc.png)

The absolute values and parameters of these functions stay reliably constant throughout the study, making our irrational behavior predictable.

This is all summarized into a final 2x2 grid:

<!-- Table -->

Prospect Theory is also the part of the book that offers the most business examples.

Risk assessment and decision-making are managers’ bread and butter, and the model shows we are doing it just wrong: we are overly cautious with successful projects, but willing to take excessive risks to save failing ones. It also shows why it is hard to kill projects that are clearly failing: the pain of accepting the loss often outweighs the rational choice to cut our losses.

Knowing these biases is the first step to counter them, but Kahneman also showed that people leaned into irrational behavior despite *knowing* it was irrational! 

Just like with other biases, Kahneman believes **process and rules** can save us from bad intuitive decisions. Still, it may be hard to make the right calls *even* when we know they are so.

You can find my full summary & review of the book below 👇

[https://refactoring.fm/p/thinking-fast-and-slow?utm_source=publication-search](https://refactoring.fm/p/thinking-fast-and-slow?utm_source=publication-search)

---

### 3) ✅ Task-relevant maturity

In his seminal book *High Output Management*, Andy Grove coined the fantastic term *task-relevant maturity* to express an employee’s overall *readiness* to take on some responsibility.

Grove breaks TRM down into many factors, but I will simplify and consider two main ones:

1. **Skill / Familiarity **— the employee’s *chops* that enable her to take on the task.

1. **Quality of the Context **— how mature and well documented your *definition of good *is.

Both items are crucial. 

Say you need to create a design doc around a new product feature. You may have the best engineer in the world, who has done hundreds of them in their career, but they still need context from you:

- **Task-specific**: what set of tradeoffs should they consider? What about speed? Or scale?

- **Principles**: what do design docs look like on our team? How do you plan rollouts? What about rollbacks? How does the code get instrumented?

So, the right amount of management depends on the level of TRM:

- **🔴 Low TRM** — your teammate (or group) hasn’t done this before and/or there is no existing procedure for it. In this case, give detailed instructions, possibly pair regularly, and establish a close feedback loop. Don’t let them do too much work without hearing from you, correct often and update the procedure with your feedback continuously.

- 🟡 **Medium TRM** — your teammate has completed similar tasks before and has an idea of what good looks like, coming from experience and/or good docs. In this case, give the best possible context about the goals to be achieved, and leave them free to execute. Keep communication lines open to give support whenever needed.

- 🟢 **High TRM** — your teammate has completed plenty of similar tasks in the past, with good results. In this case, other than giving full autonomy, you can challenge them to *improve *the definition of good. What can we do better? 

![TRM improves through manager’s feedback, and allows people to go after more and more ambitious tasks](../assets/1babdf02815c80a7.jpeg)

I published a full article last year about finding just the *right* amount of management 👇

[https://refactoring.fm/p/the-right-amount-of-management](https://refactoring.fm/p/the-right-amount-of-management)

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
