---
aliases:
  - "The Lifecycle of Code Quality"
"Is A":
  - Evergreen
Tags:
  - Has Pic
"Created at": "2024-12-24T09:38:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to":
  - "[[essay/code-quality-in-the-age-of-ai-packmind|Code Quality in the Age of AI (Packmind)]]"
  - "[[monday-ideas/monday-141|Monday #141]]"
"Updated at": "2025-01-28T14:39:00.000Z"
Status: Not started
Tweet: "Great code quality isn't about individual talent; it's about robust systems that deliver consistent results. Invest in clear practices, effective coaching, and automated testing to create a cycle of improvement. Let's discuss the real drivers of quality in development! #CodeQuality #TechLeadership"
notion_id: 166bdf02-815c-804a-99c6-f3c2d5b4e0cf
---

# The Lifecycle of Code Quality

### 🔄 The Lifecycle of Quality

Code quality is not about individual performance or heroic efforts. It's about having systems and processes that consistently produce good outcomes.

I believe a team of average developers working within a well-designed system will outperform a group of exceptional developers working within a suboptimal system.

So let's explore the six steps that make up your quality system, and how they reinforce each other 👇

![image](../assets/166bdf02815c8033.png)

#### 1) Encoded coding practices 📝

Everything starts with having clear, documented practices that define what good code looks like for your team. These may include: system design principles and patterns, code organization and naming conventions, security and performance guidelines, docs requirements, and more.

Good encoded practices are the foundation of your quality system because they *inform* everything else: they make coaching and pairing easier; they enable laser-focused static analysis, and provide clear guidelines for code reviews.

They create a shared language that makes all subsequent steps more effective.

#### 2) Coaching & pairing 👥

Knowledge doesn't spread by osmosis. The best teams actively share it and discuss it through good collaboration.

In my experience, the two most effective forms of collaboration in engineering teams are:

1. 👯 **Pairing** — it’s no secret that I am a big fan of pair programming. I [wrote about it](https://refactoring.fm/p/pair-programming-in-2024) plenty of times, and will continue to do so!

1. ✏️ **Design discussions** — a good design process, possibly supported by good [design docs](https://refactoring.fm/p/design-docs?utm_source=publication-search), does wonders for your team’s growth. It helps you get to better solutions, coaches younger co-workers, and intercepts issues before it’s too late. When the design is good, pure coding mistakes can’t be *too* bad.

#### 3) Static analysis 🤖

One of my [predictions about AI](https://refactoring.fm/p/predictions-about-ai) is that static analysis is going to be huge.

What started as simple linting for stylistic errors, is gradually evolving to intercept code smells, security vulnerabilities, optimization opportunities, and more.

This is healthy because the more you can catch with automation, the more code reviews get easy. To the point where I believe good testing + good static analysis will remove a lot of the need for *blocking* reviews, and many teams will be able to switch to a merge first + review later workflow for most changes.

A limitation of most static analysis tools today — which makes me bullish about the work of the guys at [Packmind](https://www.packmind.com/packmind-tech-coach?utm_source=refactoring&utm_medium=newsletter) — is that the set of rules and criteria are fixed. The next step, to me, is AI taking *your own* coding standards and enforcing them in static analysis, like a human reviewer would.

That’s exactly what Packmind is up to, so [check it out](https://www.packmind.com/packmind-tech-coach?utm_source=refactoring&utm_medium=newsletter) if you want.

#### 4) Automated testing ✅

We covered this already — a solid test suite makes you *faster* by creating the confidence to change code without the fear of breaking things.

I am very opinionated about testing and I don’t believe all tests are good. You should be intentional in what kind of tests to invest in, and for what parts of your codebase, to make sure the ROI is positive. I wrote more about this [here](https://refactoring.fm/p/how-to-test-software-in-2023).

#### 5) Code review 🔍

Finally, code reviews are your last line of defense.

When everything else works, reviews should rarely spot crucial issues. Conversely, if they often do, you should ask yourself what other parts of the process are failing: should you discuss design more? do you have enough encoded practices? Is static analysis powerful enough?

Code reviews are literally the *worst* moment (before shipping) in which to spot problems, because they are the last. By *shifting left* and investing in what comes before, you can shrink what goes into reviews considerably, and address many items arguably in better ways.

One of the goals of code reviews should be to **continuously reduce their own scope**, by making engineers uncover rules that can be enforced by previous parts of the dev process.

So, when done right, reviews are less about catching basic issues (handled by good design + static analysis) or verifying correctness (covered by tests), and more about sharing knowledge, identifying new patterns, and creating new coding practices.

This way, reviews feed back into the rest of the process, creating a virtuous cycle of continuous improvement.

More thoughts (and hot takes!) about reviews in this [previous article](https://refactoring.fm/p/thoughts-on-code-reviews).
