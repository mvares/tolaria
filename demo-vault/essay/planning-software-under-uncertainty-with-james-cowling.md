---
aliases:
  - "Planning Software under Uncertainty — with James Cowling"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-essays|Publish Essays →]]"
Status: Evergreened
URL: "https://refactoring.fm/p/james-cowling"
"👓 Status": Discarded
"Created time": "2024-04-18T14:53:00.000Z"
Date: 2023-07-06
"Has Notes":
  - "[[evergreen/foster-simplicity-in-your-culture|Foster simplicity in your culture]]"
  - "[[evergreen/work-backwards-from-deadlines|Work backwards from deadlines]]"
  - "[[evergreen/design-for-simplicity-defer-commitment|Design for simplicity (defer commitment)]]"
  - "[[evergreen/break-down-projects-into-stepping-stones|Break down projects into stepping stones]]"
Tags:
  - Mgmt
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 835972f9-910a-4966-8636-1d9bb07c528f
---

# Planning Software under Uncertainty — with James Cowling

Hey there! A couple of weeks ago I sat down for a chat with James Cowling, CTO at [Convex](https://www.convex.dev/) and former Senior Principal Engineer at Dropbox.

James’ work at Convex is incredible and I encourage you to check it out, while his track record at Dropbox is equally impressive. There, he led some of the company’s most daunting projects, like designing their multi-exabyte storage system, and later migrating it from AWS to 100% in-house infra.

These were enormous, multi-year projects. So, our chat *naturally* gravitated towards the challenges that arise from leading them. 

In particular, I was interested into how you *plan* and execute these right. In fact, not only are these projects massive — they also happened in a *hyper-growth *context, where assumptions shifted all the time, and the team doubled in size year over year.

As I learned, James developed his own conceptual framework for thinking at milestones, deadlines, and unknowns.

It was an incredible conversation. So, this week I took all the notes from the interview, combined them with my own ideas, and created this special edition about **planning software***** *****the right way**.

Other than the full video of James’ interview, here is what we will cover:

- ❓ **Dealing with uncertainty **— how to embrace uncertainty and unknowns.

- 🗿 **Stepping stones **— James’ framework for de-risking and executing big projects.

- ✏️ **Design for simplicity **— making progress and deferring commitment.

- ⏲️ **Management and deadlines **— building the *right thing* vs building the *thing right.*

- 🌟 **Simplicity culture **— rewarding *value* vs rewarding *building.*

Let’s dive in 👇

### ❓ Dealing with uncertainty

Link to the video chapter 🔗

I believe engineers have a natural aversion to uncertainty. We like precise things, solving problems, and getting things *right.*

After all, math is *100% right* — so let’s leave all the fuzziness to liberal arts, shall we?

When we meet uncertainty, our first instinct is to *remove* it. You can find many instances of this in everyday work:

- Data-driven decision making — “*if we just get more data then the decision will be self-evident*”

- Detailed requirements — “*we can’t build it unless you give us all the specs*”

- Long timelines — “*let’s map out everything we have to do in the next six months*”

Many of these ideas fail because reality is inherently fuzzy and *uncertainty* is impossible to avoid. Still, it is tempting to *pretend* it is not, because… you don’t see it 👇

#### Knowns and unknowns

For any given project, you can bucket *knowable* things into three categories:

1. **Known knowns** — e.g. I have to code this API

1. **Known unknowns** — e.g. What database do I choose?

1. **Unknown unknowns** — e.g. This design will collapse when load gets high.

A lot of execution success comes down to designing a plan that gradually turns the (3) into (2), and (2) into (1).

Conversely, execution failure often looks like planning for (1), accounting for (2), and pretending (3) doesn’t exist.

In James’ own words, you can’t just sit down and plan out a full, multi-year project ahead of time. There is no instruction manual for that.

So how do you move forward? Enter stepping stones 👇

### 🗿 Stepping stones

When there is no linear path from path to finish, James likes to break down work into *stepping stones*. Stepping stones are not your generic *milestones* — they need to have these qualities:

- **Incremental** — you can continue building on top of each one.

- **Valuable** — they are useful. They solve the problem, even if in an inefficient / expensive / precarious way.

- **Instructive **— they make you *learn* more about the problem space, so you can eliminate some of the *fog of war* and design better solutions in the next iterations.

Let’s make a practical example about the Dropbox storage system that James designed. The end game of this project might look like a giant, multi exabyte system deployed in data centers around the US. But, put like this, 1) it would cost a huge sum of money, and 2) it would involve daunting technical challenges, like designing a file system and its hardware architecture.

So, James scopes the problem down into deliverables that get you closer and closer, while being valuable on their own:

1. Let's build an in-memory storage system that just works on one node.

1. Make it run on one node and store data on a disk.

1. Turn it into a distributed system — still not efficient — but correct.

1. Make the distributed system efficient and scalable.

Good stepping stones are a win for all the people involved:

- **They unblock stakeholders **— because they have a partial solution they can interact with. They can give you feedback and create more alignment with engineers.

- **They motivate the team** — because they shipped something that works!

- **They might be a stopping point **— they might turn into *stopping* stones (hehe) if the company decides it’s enough.

The last point is the real litmus test: if, after a stepping stone, you can drop the project and get some value, then it’s a good stepping stone.

And this will happen. If you do your job right, you *will* drop projects before the supposed end. In fact, engineers often think that systems need to be *more* optimal than they really need to be. A surprising upside of designing good stepping stones is that they often make you do *less *work, because you discover you didn’t really need part of it.

#### Stepping stones and MVPs

So, I feel this conversation is closely related to MVPs, and how to design them. There are several examples and pictures online, but personally I dislike most of them.

Here is probably the most famous one 👇 by (the great!) Henrik Kniberg

![image](../assets/f12667b49d8e477b.jpeg)

The problem with this picture — the bottom part — is that intermediate steps *might* be valuable, but don’t get you closer to building a car. 

If your idea is to build a car, there are probably reasons for that: you might want a trunk, you might want 2-5 seats, etc. A bike is great but it doesn’t solve the same problems.

I know this is just a drawing and I am reading too much into it, but I care about getting this right. In software, stepping stones for a good car look more like… a car made of cardboard! Or a car that consumes an outrageous amount of fuel. And that’s where comparisons with reality break: you wouldn’t ship a car made of cardboard in real life — but in software you would. And you would upgrade the *chassis* in a later update.

So, while the whole stepping stones *idea* is intuitive, *how you* *design *them often it is not.

The best way to move forward on a hard problem might be to design a *disgusting* solution in 48 hours, and improve it over time. Because it is much easier to improve a system that works, than to keep everything in your head.

### ✏️ Design for simplicity

James joined Dropbox when it had less than 100 employees, and saw it grow to more than 2000. One of the biggest challenges in engineering is retaining the ability to move fast and *evolve *systems when 1) the scale grows, and 2) product assumptions change fast as well.

James’ best advice about this is to keep systems *simple*.

Simplicity is about *optionality. *The main quality of simple systems is that they are flexible — you can evolve them in many directions because you haven’t *committed* to a rigid set of abstractions.

When creating a stepping stone, you should aim to:

1. Deliver the highest possible value, and

1. Create the lowest possible commitment

So, you can think at working on a project as walking in a *cone*, where base of the cone is the design space of your final goal. Whenever you create a stepping stone, you are *moving closer* to the goal, but you are also *committing *to some ideas, thus reducing the possible *design space*. 

![image](../assets/021ada60fe5c42cf.png)

Good stepping stones are about making big steps while retaining as much design space as possible.

#### Type 1 vs Type 2

Another way of framing this is by using [Jeff Bezos’ mental model](https://thebusinessprofessor.com/en_US/management-leadership-organizational-behavior/type-1-and-type-2-decisions-bezos-explained) of *irreversible *(type 1) vs *reversible* (type 2) decisions. You want to be:

- *Slow and deliberate* — with type 1 decisions.

- *Quick and biased for action* — with type 2 decisions.

In engineering, complexity is what makes things *irreversible — *so you want avoid type 1 decisions as much as possible.

### ⏲️ Management and deadlines

Stepping stones are particularly helpful for good relationships between engineering and leadership.

Just tell me how many times have you heard engineers saying something along the lines of: “*we should do this but leadership won’t let us*”. In many teams, engineers have this feeling that managers are constantly pushing back / negotiating / fighting for deadlines.

Such fights start because, even though both managers and engineers work on the same projects, they have different sets of concerns.

Simplifying a bit:

- **Leadership** = building the *right thing*

- **Engineering** = building the *thing right*

For big projects, leadership naturally wants to *de-risk *execution,* *to make sure they are *building the right thing*. So, coming back with something that sounds like “*hey, just let me do my thing for 1 year” *just doesn’t cut it.

When managers push back on estimates, what they are really showing is their *appetite* for that project/feature.

The guys at Basecamp wrote a great piece about [working backwards from deadlines](https://basecamp.com/shapeup/1.2-chapter-03) — which I believe is the *healthy* way of using them: as design constraints.

You decide upfront you want to spend 3 months on a problem and figure out what you can get done in that time, following the stepping stones rules. Great engineering is literally *defined* by finding clever solutions against constraints, be them about cost, time, resources, or else.

### 🌟 Simplicity culture

This whole way of working, though — building simple things, working backwards from deadlines — is counterintuitive.

As engineers (or human beings, really) we want to look smart and be proud of ourselves, and it’s easy to conflate that with *building complex stuff*.

True simplicity, though, it’s hard. It requires an elegant mental model — you can’t duct-tape simplicity. 

James and I agreed that the best engineers we have known write code *like a toddler*. But writing simple code requires letting go some ego. You need experience and maturity to do the simple thing and not think that’s because you are *dumb*, or because you couldn’t figure out the complicated thing.

As a team, though, you can accelerate this. Simplicity comes natural when you reward shipping value to customers, and make people *own *the creation of such value.

In absence of this, people may build things for the sake of it. When engineers do not participate company goals, don’t know what they are truly working for, or just receive tickets from managers to complete, they *detach*. They play the game.

---

### Career

- Optimize for having fun and being around good people

- Don’t play the game

- Engineers have the luxury of being in an “upside maximisation” framework, rather than “downside minimisation”.

### Engineer to Manager

- Trap of working super hard on individual stuff

- Anything that’s going wrong is your fault

- New leaders want to prove themselves and do work themselves

- Strategic questions:

- If you answer these your team is ok 👍

### Keeping tech and business aligned in hyper-growth

- Simplicity, architectural elegance

- Hierarchy: why, what, how — in this order

### Convex

- Infrastructure engineer who spent a lot of time on large-scale infrastructure

- A lot of commonality across projects

- Write functions, run on a server, create a database

- At a high level, similar to firebase

- Designed so that people can spend their effort on building applications and not building boilerplate

- Decisions are — by definition — what you do in the face of unknown

- Design around nouns, not verbs
