---
aliases:
  - "Design for simplicity (defer commitment)"
"Is A":
  - Evergreen
"Last Tweeted": 2023-07-19
Tags:
  - Has Pic
"Created at": "2024-04-18T14:44:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to":
  - "[[essay/planning-software-under-uncertainty-with-james-cowling|Planning Software under Uncertainty — with James Cowling]]"
  - "[[monday-ideas/monday-60|Monday #60]]"
"Old Created At": "2023-07-06T12:22:00.000+02:00"
"Updated at": "2024-09-18T08:44:00.000Z"
Status: Not started
Tweet: "Keeping systems simple is key for tech leaders. As you scale, remember: simplicity equals flexibility. Aim for high value with low commitment in your designs. Avoid irreversible decisions—focus on reversible ones to maintain your design space. Let’s discuss how we can implement this in our projects! #CTO #Engineering"
notion_id: 0afaeaaa-1431-48e5-a8e6-dbf2a0ce81c4
---

# Design for simplicity (defer commitment)

James joined Dropbox when it had less than 100 employees, and saw it grow to more than 2000. One of the biggest challenges in engineering is retaining the ability to move fast and *evolve *systems when 1) the scale grows, and 2) product assumptions change fast as well.

James’ best advice about this is to keep systems *simple*.

Simplicity is about *optionality. *The main quality of simple systems is that they are flexible — you can evolve them in many directions because you haven’t *committed* to a rigid set of abstractions.

When creating a stepping stone, you should aim to:

1. Deliver the highest possible value, and

1. Create the lowest possible commitment

So, you can think at working on a project as walking in a *cone*, where base of the cone is the design space of your final goal. Whenever you create a stepping stone, you are *moving closer* to the goal, but you are also *committing *to some ideas, thus reducing the possible *design space*. 

![image](../assets/d3da94ad19ca4c5f.png)

Good stepping stones are about making big steps while retaining as much design space as possible.

#### Type 1 vs Type 2

Another way of framing this is by using [Jeff Bezos’ mental model](https://thebusinessprofessor.com/en_US/management-leadership-organizational-behavior/type-1-and-type-2-decisions-bezos-explained) of *irreversible *(type 1) vs *reversible* (type 2) decisions. You want to be:

- *Slow and deliberate* — with type 1 decisions.

- *Quick and biased for action* — with type 2 decisions.

In engineering, complexity is what makes things *irreversible — *so you want avoid type 1 decisions as much as possible.

---

Two weeks ago I sat down with James Cowling, former Senior Principal Engineer at Dropbox, and we had a great chat about various topics.

James joined Dropbox when it had less than 100 employees, and saw it grow to more than 2000.

A thread 👇

One of the biggest challenges in engineering is retaining the ability to move fast and evolve systems when 1) the scale grows, and 2) product assumptions change fast as well.

James’ best advice about this is to keep systems simple.

Simplicity is about optionality.

The main quality of simple systems is that they are flexible — you can evolve them in many directions because you haven’t committed to a rigid set of abstractions.

So, whenever you are designing a feature or a system, you should aim to:

1. Deliver the highest possible value, and

1. Create the lowest possible commitment

You can think of working on a project as walking in a cone, where the base of the cone is the design space of your final goal.

Whenever you create a milestone (James calls them stepping stones), you are moving closer to the goal, but you are also reducing the design space.

Good stepping stones are about making big steps while retaining as much design space as possible.

Another way of framing this is by using Jeff Bezos’ mental model of irreversible (type 1) vs reversible (type 2) decisions 👇

You want to be:
• Slow and deliberate — with type 1 decisions.
• Quick and biased for action — with type 2 decisions.

In engineering, complexity is what makes things irreversible — so you want avoid type 1 decisions as much as possible.

You can catch up with our whole chat (video + article) below 👇
[https://refactoring.fm/p/james-cowling](https://refactoring.fm/p/james-cowling)
