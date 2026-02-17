---
aliases:
  - "Monday #153"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-monday-idea|Publish Monday Idea]]"
Status: Published
"👓 Status": Not started
"Created time": "2025-04-22T13:17:00.000Z"
Date: 2025-04-28
"Has Notes":
  - "[[evergreen/hire-as-last-resort|Hire as last resort]]"
  - "[[evergreen/map-context-to-improve-communication|Map context to improve communication]]"
  - "[[evergreen/threat-modeling|Threat Modeling]]"
Tags:
  - Monday
  - Free
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 1ddbdf02-815c-80ec-b5d7-da823348e402
---

# Monday #153

### 1) 🏆 What does your manager care about?

Different roles see the world—and the organization—through different lenses. 

This is obvious for roles that are very removed from our own—e.g. a CFO who sees everything through unit economics and cash flow—but it is also true for closer ones, like engineering managers vs tech leads, or EMs vs software engineers. 

In these cases, the shift of perspective is more sneaky. As an engineer, you may care about your own developer experience, while your manager cares about team productivity. You may think in terms architecture improvements, while your PM thinks in terms of product enablement. Are these related? Very closely. Are they the same thing? Absolutely not.

Quoting our coach-in-residence [Joel](https://monkeysthumb.co.uk/):

> *The better we understand the goals that our managers have, the less surprising their actions will be. […] Some of the situations where managers act in ways that most dismay or surprise us are when they are acting on their fears and worries.*

Understanding your manager’s context and priorities allows you to map your goals and concerns into their own. This boils down to asking two questions:

1. ➡️ **What makes *****you***** successful? **— What are your goals and concerns?

1. ⬅️ **What makes *****me***** successful? **— How can I help you reach your goals?

The only way for *you* to be successful is by making *your manager* successful. For many this isn’t obvious, so let that sink in!

I wrote a full article on managing up a few months ago 👇

[https://refactoring.fm/p/managing-up?utm_source=publication-search](https://refactoring.fm/p/managing-up?utm_source=publication-search)

---

### 2) 🔒 Threat modeling

One of my favorite practices around software security is *threat modeling*.

A *threat model *is the description of an application and its environment through security glasses.

Likewise, threat modeling is a family of activities you pursue to identify threats, vulnerabilities, and design countermeasures to prevent or mitigate such threats.

Historically, designing for security has often followed the ***security sandwich**** *approach: you address security during design, and you test things at the end. This *waterfall-ish *approach, though, clashes with reality: specs often change during development, so you end up testing for things that are 1) incomplete, or 2) not relevant anymore.

Good threat modeling should be applied continuously throughout the whole development lifecycle.

You can check the dedicated [OWASP page](https://owasp.org/www-community/Threat_Modeling_Process) for more details about how to perform it, complete with practical examples.

![Example of a threat three with a threat, vulnerabilities, and countermeasures ](../assets/1ddbdf02815c800b.png)

---

### 🏁 Hire as last resort

When is it the right time to expand your team? What are the signs? If you search online (or talk to people), you often find conflicting advice:

- **⬅️ You should hire *****early*** — before problems get too big.

- **➡️ You should hire *****late*** — to avoid premature scaling and burning money.

This *dilemma* is high-stakes, for two reasons:

- **Hiring is extremely expensive** — both in terms of compensation money, and time your team needs to spend on the process.

- **Reverting is hard** — firing sucks for everybody, so you want to optimize for doing that as little as possible.

Because of this, I believe in using **hiring as last resort**. Last resort with respect to what? Well, it depends on why you are hiring in the first place.

In engineering teams you hire people for one of two reasons (or both): **throughput** or **quality**.

#### Hiring for quality 🔍

You hire for **quality** when you have a skill gap on something, and it clearly limits growth. Whatever such skill is, before you hire you should ask yourself:

1. **Can you learn it?** — can your engineers acquire that skill? Smart people learn faster than we usually account for, and hiring takes a long time anyway.

1. **Can you build a first version?** — it is rare that you can *only* bring value with top-quality execution, and prototypes are useful to educate your taste and to better understand what you need.

![image](../assets/1ddbdf02815c80b7.jpg)

Often times, a combination of (1) and (2) is enough to satisfy (or delay) your need.

#### Hiring for throughput 📈

You hire for **throughput** when growth is slowed down by pure bandwidth.

In my experience this is trickier to judge than quality, because most factors that slow down your team *do not* get better with size — quite the opposite.

Bad dx, unclear priorities, confusing org structure, are all systemic diseases that you will not solve by throwing more people at them — you will arguably make them worse.

So, counterintuitively, the best time to hire is when your team is in great shape and firing from all cylinders. If that’s not the case right now, you should probably focus on fixing what doesn’t work first.

Finally, increasing headcount has diminishing returns: adding one engineer adds less than one FTE to your dev resources — and the larger your org, the larger this gap. That’s because the** cost of coordination** grows *more than linearly* with respect to your headcount.

I wrote more principles on hiring engineers in this recent piece 👇

[https://refactoring.fm/p/hiring-principles-for-engineering](https://refactoring.fm/p/hiring-principles-for-engineering)

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
