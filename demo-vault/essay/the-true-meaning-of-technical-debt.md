---
aliases:
  - "The True Meaning of Technical Debt"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-essays|Publish Essays →]]"
Status: Everpictured
URL: "https://refactoring.fm/p/the-true-meaning-of-technical-debt"
"👓 Status": Not started
"URL 2": "https://twitter.com/lucaronin/status/1337359758345576450"
"Created time": "2024-04-18T14:53:00.000Z"
Date: 2020-12-11
"Has Notes": "[[evergreen/design-sweet-spot-for-tech-debt|Design sweet spot for tech debt]]"
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 46a7b9ff-cf46-40c9-941a-7d5d1112b60d
---

# The True Meaning of Technical Debt

Last week I came across this old [article](https://randsinrepose.com/archives/managementese/) by Rands about *managementese. *It is also included in [*Managing Humans*](https://www.goodreads.com/ru/book/show/1317946.Managing_Humans)*:* a beautiful, humorous book about engineering management, that I believe everyone in the field should read.

The article is a great essay on communication — and how, in the workplace, communication naturally optimizes for clarity and speed. 

Weird phrases that we often mock, such as "*action item"*, or "*circling back", *are actually highly efficient vectors of meaning. They fit non trivial concepts in very few words, and are understood by everybody.

One of such great metaphors is **Technical Debt. **

Technical Debt is a very popular concept among developers, I think for a couple of reasons:

- It's very intuitive — something that piles up and makes you slower and slower, just like interest on existing debt.

- Management understands it, yet it stays under control of Engineering.

These elements make it a perfect leverage during negotiation about priorities, deadlines and resources.

However, is it really as clear as it sounds? 

It is a fact that, over time, all development teams get slowed down by the existing codebase. But why? Is it because maintenance is inevitable? Or because we could do something better in the first place? Or both?

### ❓ Why Technical Debt Happens?

If you search for "Technical Debt" on Google and look at excerpts from the first page, you will find some kind of consensus.

![image](../assets/49150d36b8894658.png)

It looks like it is something that accumulates because of some nasty, quick and dirty practices. If true, it should follow that by writing clean code from the start (and documentation, and tests, etc.), debt never piles up, or it does in a negligible quantity.

Of course, if you have any experience working in an engineering team, you know this is false.

Technical debt creeps in even when you work with the best intentions, and follow the very best practices.

But why?

### 🔍 Technical Debt as *disagreement*

Enter this short [video](https://www.youtube.com/watch?v=pqeJFYwnkjE) by Ward Cunnigham.

Ward is the original inventor of the "Technical Debt" term, and it's revealing to hear the sentence in which this metaphor was used the first time (emphases are mine):

> If we fail to make the program aligned with what we **understand** to be the proper way to **think about** our [...] objects, then we are going to continuously stumble into **disagreement**, and that would slow us down like paying interest on a loan.

Ward describes debt as** the natural result of writing code about something we don't have a proper understanding of. **

He doesn't talk of poor code — which he says accounts for a very minor share of debt.

He talks of *disagreement* between business needs and how the software has been written.

But how do we land to such disagreement? In my experience, there are two offenders:

- 🎨 **Wrong Design** — what we built was wrong from the start!

- 🏃 **Rapid Evolution** — we built the right thing, but the landscape changed quickly and made it obsolete.

Let's see these more in detail 👇

### 🎨 Wrong Design

It may happen that the team designs a solution that doesn't properly fit business requirements, in a non-obvious way. 

Requirements may still be met on the surface, but something is wrong under the hood — an abstraction that doesn't fit, some duplication, scalability issues, and so forth. 

Of course, such things may happen because of poor development skills. But in my experience, most of the times it's because developers didn't fully understand what had to be done.

#### How to improve? 💡

If this happens regularly, a natural response is to invest more in the Design phase. This means, of course, more Engineering analysis, but also more talking with stakeholders to discuss both the here and now, and the future evolution of the project.

![image](../assets/3753b7b3c31146a8.png)

Increasing Design effort brings diminishing results after a while, so it's up to you to find the sweet spot, based on how solid is your company planning vs how much change you can expect in the future.

### 🏃 Rapid Evolution

The second scenario is when things change so rapidly, that today's requirements cannot really be  trusted. 

That is: even if we build the right thing, it risks becoming obsolete fast, because of the ever-changing business landscape.

#### How to improve? 💡

A thorough Design phase provides limited protection against future changes, so a leaner cycle might work better: 

1. 🏃 **Rush** — the code out of the door

1. 🔍 **Learn** — more things about your business reality

1. 🔨 **Refactor** — put that learning back into the software

Basically, we take a piece of the Design effort and move it forward, in a Refactoring phase that happens every time a few pieces have consolidated and are ready to be *secured*.

In this scenario, we are accepting the creation of debt, trusting our ability to repay it in the short term. 

![image](../assets/8a6540caf01e4872.png)

This ability comes down to three elements:

- **Writing code that is clean to refactor** — which is very different from *clean*. Such code is similar to those sailor knots who should be strong enough to hold for a while, but easy to dismantle when not needed anymore.

- **Actually learning along the way** — analyze, with the help of stakeholders, what still fits and what is going to become debt.  

- **Spending regular time on refactoring** — reorganize the code periodically to reflect your updated understanding.

### 📌 Takeaways

As always, I try to summarize the main points of the article in this final section. This should be useful for the reader, but it also serves as a reality check for me to understand if what I have written makes sense from top to bottom 😅

So, if you are in a hurry, that's what you should remember:

1. **Technical debt is caused by a lack of understanding **— it stems from *disagreement* between business needs and how the software has been written.

1. **You can limit such disagreement...** — by spending more effort on the design phase, and by properly discussing requirements with stakeholders.

1. **...or you can embrace it **— by explicitly planning for lean releases and following rework. This is a better choice when the future is uncertain and might bring radical changes.

### 📚 Resources

A few resources have helped me writing this article, and can be useful to dig deeper into this topic:

- 📺 [**Debt Metaphor**](https://www.youtube.com/watch?v=pqeJFYwnkjE) — a short video by Ward Cunningham that explains the relationship between debt and understanding.

- 📃 [**Technical Debt as a Lack of Understanding**](https://daverupert.com/2020/11/technical-debt-as-a-lack-of-understanding/)** **— a recent article by Dave Rupert that reflects on Ward's definition and adds up some real world experience.

- 📃 [**Technical Debt Quadrant**](https://martinfowler.com/bliki/TechnicalDebtQuadrant.html) — a thoughtful essay by Martin Fowler about what Technical Debt really is, and its different types.

**And that's it for this week! What's your experience with technical debt? Let me know in the comments **👇 **or via email!**

---

### Description

If you forgive the pretentious title, this article dives into the origins of this widely used metaphor, and why it is often misunderstood.

I also provide some battle-tested advice about how to deal with debt in real world situations, and list some great, related resources that have inspired me about this over the years.
