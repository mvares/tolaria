---
aliases:
  - "Thoughts on Code Reviews"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-essays|Publish Essays →]]"
Status: Evergreened
Owner:
  - Luca
URL: "https://refactoring.fm/p/thoughts-on-code-reviews"
"👓 Status": Not started
"Date HH": 2024-06-20
"Created time": "2024-06-10T07:14:00.000Z"
Date: 2024-06-19
"Has Notes":
  - "[[Automate / Defer / Pair]]"
  - "[[evergreen/code-reviews-should-ever-shrink-their-scope|Code reviews should ever-shrink their scope]]"
  - "[[evergreen/why-code-reviews-matter-two-extremes|Why code reviews matter: two extremes]]"
Tags:
  - Updated
  - Software
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: ac5b83ad-7a32-4967-be23-7598afce7444
---

# Thoughts on Code Reviews

### 📑 Materials

---

[Code Reviews](https://www.notion.so/3150ff499b9c46379824bacbb92e63f5) 

### ✍️ Post

---

One of the major concerns I have about running Refactoring full-time is to lose some **hands-on experience**.

I try to compensate by doing research and talking with as many people as I can, but there is no deny that I have now some *detachment* from things that, up until to a couple of years ago, I used to do every day.

While this is mostly a source of concern, over time I have also found an unexpected flip side.

As long as I was deep in the weeds, **I used not to question many engineering practices** that seemed standard* *to me. After all, a startup has its good share of risks already, so why spend a precious [innovation token](https://mcfunley.com/choose-boring-technology) on *process*? Do not reinvent the wheel, Luca.

The problem with this (perfectly good) advice is that, from time to time, the proverbial wheel *needs* to be reinvented. Conditions change, tooling gets better, and we eventually find better ways to work.

So, I have found that by being *removed* from the daily engineering struggle, I feel less attached to the way I used to work, and it feels easier* *now to *question* things here and there, and prompt some good conversations.

Lately, one of my small obsessions is the way we do **code reviews**.

Code reviews look, to me, like an imperfect solution to two *supremely important* problems:

1. 🏆 **Keeping code quality high **— which leads to ease of change, fewer defects, and less maintenance.

1. 📚 **Sharing knowledge across the team **— which creates alignment, growth, resilience, flexibility, and more.

These are also *self-reinforcing* goals: shared knowledge helps keep the quality high, and, in turn, high quality code is generally crisper and easier to understand for others.

Code reviews address these goals by making code changes inspected by multiple engineers — at least two: the author, and one+ reviewers. This, to me, not only looks fine: it looks like the only possible way.

Still, even if we agree on everything above, there is plenty left to figure out, like:

- *When should reviews be made?*

- *Should all the code be reviewed?*

- *What goes into a review? *

- *Who should do reviews?*

Today, the most common workflow for code reviews is async + blocking + mandatory, that is:

- 🔀 **Async** — a PR is opened, one reviewer (or more) is assigned, and they will perform their review asap.

- ⛔ **Blocking** — code isn’t merged and deployed until it passes the review.

- 🔒 **Mandatory** — you do the same workflow for all changes.

I believe this is far from ideal, and I spent the last couple of weeks writing down 1) why, and 2) how I think we can do better.

So, this article is a honest conversation on the upsides and downsides of code reviews, starting from first principles, and discussing both familiar and unconventional workflows.

It is not a *prescriptive recipe* that tells you exactly what to do, but it rather gives you a set of ingredients and mental models to let you create the recipe that works best for you.

Here is the agenda:

- 🏆 **Why code reviews matter** — and why your *innovation token* is probably well spent here.

- 🔍 **The scope of code reviews** — what is really the *scope* of a code review?

- 💠 **Automate / Defer / Pair** — my modest proposal for a healthy review process.

- 🎽 **Choosing for your team **— how your team maturity and seniority affects reviews.

Let’s dive in!

---

### 🏆 Why code reviews matter

This question looks banal. 

However, while the *main* goals (quality, knowledge sharing) may be obvious, I have found that reviews have second and third-order effects that are trickier to figure out, and worth discussing

Code reviews are your main (and possibly only) **feedback loop **on how your team writes code. 

This feedback loop not only intercepts defects: it aligns people on practices and culture. From high level engineering principles, down to naming conventions, chances these many of these are not only enforced by—they are literally born out of—code reviews.

So let’s start with what happens when this feedback loop is not in place.

#### A no-reviews story ❌

I have worked once as an EM on a team that didn’t review code. When I joined, it was made of 4 senior engineers: they were all extremely fast and experienced, and they just pushed code to prod all the time.

Things apparently worked, and code quality was good. But there where other, invisible problems:

- **Gatekeeping** — over time, each engineer had developed their personal areas of ownership, which had become impenetrable to everyone else.

- **Inconsistency** — different parts of the code had completely inconsistent choices about naming, libraries used, folder structure, and more.

- **No docs **— since the general expectation was that everyone worked on their own, there was little incentive to write good docs and keep them updated.

Down the line, these problems led to more problems:

- **Collaboration **— any conversation about design, tradeoffs, or estimates, was extremely hard, because everyone’s ownership was completely siloed.

- **Hiring **— onboarding new engineers, either junior or senior, was a nightmare.

- **Resource allocation** — if we wanted to invest more on a specific product area, it was hard because we couldn’t put more people on it at will.

- **Key man risk** — individual engineers got an outsized importance for the business and, even if—to their credit—no one ever tried took advantage of it, it was concerning to me as a manager.

I will stop here and won’t bother you with how we tried to put things back on track. This story was to show that the impact of not doing reviews goes way beyond the “*more bugs in prod*”. In the long run it is detrimental to almost everything you do.

#### The other extreme: slow reviews 🐌

Now, there is another end of this spectrum which is equally bad. Bad code reviews are usually *bad* in two ways, often at the same time:

- **They are slow **— they delay release for several hours (or days!)

- **They are superficial **— they don’t really improve the code, nor let knowledge be shared.

The problems with superficial reviews are the same of the *no-reviews* scenario, so no need to elaborate on that. 

Conversely, slow reviews are worth discussing, because I have known many people who apparently have no issue with them, when instead they should.

The problem with slow reviews is that they mess up with engineers’ work. Big time.

Once a developer fires up a PR, their work is far from over: they may need to implement improvements based on the review, and, when the feature is released, check that everything works fine in production through logs and instrumentation.

This is all legit, valuable work.

But including several hours of delay at some point in this process (which you should also multiply by the number of review iterations) makes engineers switch to other tasks, which increases WIP, increases cognitive load, reduces productivity, leads to batched releases, and a whole self-reinforcing cycle of *badness.*

![Slower time to production reduces productivity and literally increases the number of devs you need to do the same things.](../assets/d6a2bb9c304f4fcd.webp)

So, waiting just leads to more waiting. 

In fact, when people are used to wait a lot for reviews, they begin to create fewer & bigger PRs, which increases the burden on the reviewer and makes reviews even slower and shallower.

So, how do you do code reviews well? To answer this, let’s first figure out what *should go* in a code review.

---

### 🔍 The scope of code reviews

If we go back to the idea of code reviews as **feedback loop** for the whole dev process, what should they give feedback on?

In most teams, there are various other devices that impact how you write code, but let’s simplify and look at two particularly relevant ones for this conversation:

1. **📋 Design docs** — that’s where you discuss your design and implementation plan. You may follow a template that enforces good practices.

1. 🤖 **Static analysis** — that’s where you catch coding standards violations, security vulnerabilities, missing tests, and various kinds of smells.

Design docs are about things you discuss *before* you write code, while static analysis happens *after* you have written it.

These steps can intercept many items that would otherwise be firmly in the scope of code reviews. So, ideally, you want most of the action to happen in these two stages, as opposed to reviews, with the latter acting as a *fallback.*

In fact, 1) you don’t want reviews to deal with *design *issues, as they are expensive do rectify *after* you have already written the code, and 2) you obviously don’t want human reviewers to look for issues that can be found automatically.

> *Static analysis tools can do 2 things really well IMO:*

Design docs and static analysis don’t cover it all, nor they are ever perfect, but by investing on them you can shrink what goes into code reviews considerably, and address many items arguably  in better ways — by either automating them, or shifting them left.

So, one of the goals of code reviews should be to **continuously reduce their own scope**, by allowing engineers to uncover items and rules that can be later enforced by other parts of the dev process.

---

### 🚢 Ship / Show / Ask

So, the TL;DR of this article so far is three things:

1. Reviews are about 1) improving quality, and 2) sharing knowledge.

1. Reviews are a crucial practice but they are also easy to mess up.

1. The scope of reviews is continuously *squeezed* left and right by good design and good static analysis (among others).

How do we use this to create a solid review process?

[Two years ago](https://refactoring.fm/p/code-reviews?utm_source=publication-search) I wrote about the **Ship / Show / Ask** framework by [Rouan Wilsenach](https://www.rouanw.com/), which, for new code, considers three cases:

- 🚢 **Ship** — You make the change directly on your mainline, without asking for a code review. This works when you fix unremarkable bugs, add features using established patterns, or do collateral changes like improving docs.

- 🔍 **Show** — You create a PR, run all the CI pipeline, merge it without anyone’s approval, and *then* ask for feedback. This way you release quickly but still create space for discussion. It works in situations where you want to share knowledge but don’t necessarily need feedback, or the feedback is valuable but shouldn’t be blocking.

- ❓ **Ask** — You make changes on a branch, open a PR, and wait for the review before merging. This is the standard process most companies adopt today.

The main intuition behind Ship / Show / Ask is that the optimal process should use different strategies based on the type of change, rather than imposing the same workflow on everything.  

![image](../assets/7a181555bbe44d12.jpg)

It also encourages engineers to make their own call on the strategy to use, which is empowering*.*

---

### 💠 Automate / Defer / Pair

So, today I propose an evolution of the Ship / Show / Ask, which is based on the same three options, but is more opinionated about how to perform them.

I tried to come up with some memorable name, but I just ended up with **Automate / Defer / Pair**:

#### 1) Automate 🤖

When 1) there is no remarkable knowledge to be shared, and 2) potential for improvements is low, you should probably skip the review and just rely on static analysis and your test pipeline.

In my experience, tasks that meet these criteria are never the majority, but there are still plenty of them in any team: fixing small bugs, adding tests, updating dependencies, small cosmetic changes, and more.

#### 2) Defer ↪️

This is probably the most controversial part of this article: I believe the majority of code changes *should* be reviewed, but the review shouldn’t be blocking. 

In fact, when you think at 1) improving quality, and 2) sharing knowledge, both can be accomplished *after *the code has been merged. 

This works beautifully well especially in continuous delivery workflows, where you often push changes in *disabled *state, gated behind a flag. You merge, get an async review, and possibly push improvements later.

![In a mature engineering team, you should be able to do non-blocking reviews for most tasks, automate the simple ones, and pair on the remaining.](../assets/84f90a6a757e4867.jpg)

#### 3) Pair 👯 

There are two scenarios in which async, deferred reviews are not ideal:

1. **Correctness is very important **— the change is hard to revert and/or has the potential do to big damage: think of db migrations, or payment workflows.

1. **Complexity is high **— the PR has thousands of LOCs, or is an inherently complex algorithm, and the reviewer has little context on the task.

I have found that, in both cases, async reviews are not ideal.

First, it’s extremely hard for a reviewer to truly check for correctness on their own. To do that, they shouldn’t only *understand *the code: they should check it out on their machine, review tests, and run everything on their own. But how many reviewers do this? Few that I know of, because 1) is a whole lot of work, and 2) it’s still not going to be perfect, because of the missing context.

The latter point, about context, is also what makes complex PRs basically unreviewable.  Whenever the PR is big, or the code is legitimately elaborate, how can you expect a reviewer to figure out everything on their own and come up with meaningful suggestions?

So, in all these cases, my preferred solution is **pairing**. 

Pairing on complex / critical reviews solves all these issues. Face time is *high-bandwidth* so you get a 1) deeper, and 2) faster review, plus plenty of collateral benefits that Vic summarized very well recently: 👇

![image](../assets/27800be00eb04511.png)

You can also try *mob* versions of this, as Alfredo told us in the community 👇

> *We perform periodic Concerns Reviews. Whenever someone finds something concerning in the codebase or in the development experience, instead of stopping the work, we write it down on the Concerns board. We then review these concerns together periodically and prioritize tech debt repayment accordingly.*

Still, pairing should arguably be reserved for a *small* portion of your work. 

If you feel the majority of changes need to get this treatment, you should probably focus on working in small batches, short-lived branches, and all the usual advice on PR that *still* applies.

---

### 📌 Bottom line — doing the best for your team

This framework isn’t necessarily a good fit any team. It is *aspirational*.

It’s like when we say that not deploying on Fridays is bad advice: not deploying on Fridays is *great* when your dev process and your systems are not sufficiently robust to prevent nightmarish weekends to your devs. Still, it is helpful to know that elite teams indeed deploy on Fridays, and you can probably get there, too.

Likewise, I have known—and worked for a long time in— teams where 1) there was no agreement even on basic design topics, and/or 2) testing and static analysis were shallow at best.

In these cases, human + blocking + async reviews have indeed a ton of value, and you should 100% do them. But you should also continuously invest in taking their *findings* and moving them *out* of reviews: can you add that to the linter? can you add a todo item in the design doc?

Counterintuitively, having consistently helpful and valuable reviews is a *smell* that you can do better in other parts of the process.

Finally, these are not *team *choices only, but individual ones, too. You can be more cautious with fresh hires and junior engineers — which also equals to faster growth for them — and *empower *more folks who have been working with you longer. This doesn’t mean senior engineers == push without review, it means *trusting* them with picking the right review strategy based on what the situation demands.
