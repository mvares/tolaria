---
aliases:
  - "What an Elite Team Looks Like"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-essays|Publish Essays →]]"
Status: Evergreened
URL: "https://refactoring.fm/p/what-does-an-elite-team-look-like"
"👓 Status": Not started
"Created time": "2025-10-02T12:59:00.000Z"
Date: 2025-10-22
"Has Notes":
  - "[[evergreen/focus-on-single-teams|Focus on single teams]]"
  - "[[evergreen/what-makes-a-team-good-is-speed-engagement|What makes a team good is speed & engagement]]"
  - "[[evergreen/use-specialists-platform-for-quality|Use specialists & platform for quality]]"
  - "[[evergreen/scale-quality-by-turning-taste-into-constraints|Scale quality by turning taste into constraints]]"
Tags:
  - Essay
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 280bdf02-815c-8048-9668-f449c96c31e3
---

# What an Elite Team Looks Like

### 📑 Materials

---

### ✍️ Post

---

Over the past few weeks I have been interviewing several Refactoring community members. It’s mostly people who are responsible for engineering teams — EMs, tech leads, but also VPs of small to mid-size orgs.

I want to understand what’s top of their minds and what their biggest challenges are, so that I can help them better with Refactoring.

A question I always ask is: if you had a magic wand and could fix all the problems in your team, and make people work however you like, what would you do? Which is another way to ask: what does the perfect software engineering team look like to you?

How do people work together? What makes it *amazing*?

Most of the time, this question stops people on their tracks. They don’t know.

They might point at small improvements, like, would like to be a bit faster, have more tests, etc, but what’s the final goal? What does the *best *team look like? And yes, let’s accept there is no one-size-fits-all, but it doesn’t matter, you can still ask yourself: what does an elite team look like? And how close are you to that?

Without a vision, it’s hard to assess where you stand. Are you doing okay? How much untapped potential do you have? Can you do +10% (on what?!) with the same people, or—gosh—you might do 2x? 3x?

The truth is: nobody knows. 

And if you think about it, this is infuriating.

As an industry, software development has no consensus on pretty much anything. Everything feels controversial: tests are controversial, docs are controversial, agile, tech stacks, team organization, and so on.

So we often look at stories from successful companies, draw our own lessons, but that too never feels 100% convincing. Google does this thing, but should we copy Google? “*You are not Google, stupid!*” Look what Anthropic does — yeah but that’s too weird. Basecamp? Man, those are like hippies, right?!

I don’t think we need a *framework* to fix this, but I think we can work our way from first principles and settle on a few mental models that can be helpful. Let’s try to figure out what good should look like — not to create a model to copy, but a direction to trend towards.

So here is the agenda for today:

- 🎽 **Focusing on single teams** — why nailing this is the most important problem in software today.

- 🏆 **What makes teams good** — the two qualities that are foundational for great teams.

- 🧱 **Product vs platform** — the two types of work that require different skills and workflows.

- 🪴 **How to scale quality** — turning expert judgment into process and constraints that empower everyone.

Let’s dive in!

---

### 🎽 Focusing on single teams

To avoid boiling the ocean here, I want to focus on a specific (not really) problem: how a single team works. How a small group of 5-10 people, working on a software product, can be effective at working together.

To me, this feels like the most important problem in software to solve.

In fact, on a scale that goes from individuals to entire orgs, the team seats in the middle and has an outsized influence on everything else: many of the choices you seemingly make at org level on one side, and individual work on the other, are actually downstream from how you want small groups of engineers to work together.

![image](../assets/293bdf02815c8009.png)

I’ll make a couple of examples.

[Team Topologies](https://refactoring.fm/p/team-topologies), one of the most influential works on how tech orgs should be structured, banks everything on the notion of *stream-aligned teams*. The big idea is how a single team should work, and the organization design follows.

On the individual side, how engineers work largely depends on how the rest of their teammates work. What skills they need (are they full-stack? or specialists?), what duties they have (do you need tech leads? or EMs? or both?), how their career progresses, it’s all a consequence of the workflows of a core group of people. The atomic unit of your org.

We always have big tech in our mind, but 90% of companies have less than 20 employees. For those companies, solving problems for a single team means solving them for the whole org. And we may also argue that all big companies start as small companies, so they have to *graduate* from there anyway.

I may throw also AI to the mix and preach on how it makes all of this even more relevant but I will spare you that — this is not an AI article (finally!).

So what makes single teams *good*?

### 🏆 What makes teams good?

There is a famous quote from Jeff Bezos about focusing on the things that are not going to change over time:

> *I very frequently get the question: 'What's going to change in the next 10 years?' And that is a very interesting question; it's a very common one. I almost never get the question: 'What's not going to change in the next 10 years?' And I submit to you that that second question is actually the more important of the two -- because you can build a business strategy around the things that are stable in time.

[I]n our retail business, we know that customers want low prices, and I know that's going to be true 10 years from now. They want fast delivery; they want vast selection. It's impossible to imagine a future 10 years from now where a customer comes up and says, 'Jeff I love Amazon; I just wish the prices were a little higher,' [or] 'I love Amazon; I just wish you'd deliver a little more slowly

— Jeff Bezos*

A lot of things are changing in software right now, and are probably going to change over the next few years. What are those that are *not* going to change?

To me, there are at least two:

- ⚡ **Speed **— we’ll always want to be fast

- ❤️ **Engagement **— we’ll always want people to do engaging work

Let’s unpack these and why I think they are the crucial ones.

#### 1) On speed ⚡

I believe speed is the ultimate engineering quality. If you optimize for speed, almost everything else falls into place.

When I say this I always get bad looks, because everyone knows that when you try to be fast for its own sake, bad things happen: you cut corners, ship the wrong stuff, and ultimately trip on yourself.

But when I say speed, I don’t mean 100 meters speed. I mean marathon speed. Long distance speed. You are still optimizing for the stopwatch time, but you need everything to work like clockwork to get there.

When looked through this lens, speed is not at odds with anything else. 

- **Speed is not at odds with stability** — shipping faster leads to *higher* stability, through faster recovery from mistakes. 

- **Speed is not at odds with quality **— either. Pretty much the opposite: quality enables speed. Not everyone is convinced of this, but it is obvious when you think at what quality is *not. *

*Not* quality is:

- *Spending most of your time fixing tech debt*

- *Putting out fires in prod*

- *Maintaining a long backlog of bugs*

- *Taking forever to make any change*

Whatever definition of quality you can find, it always manifests as something you do to keep going fast. You keep quality high so you can spend your time on what matters, without getting slowed down. 

Quality is in service of speed.

There is one thing, though, that is *not* necessarily in service of speed: **enjoyment of our work**.

#### 2) On engagement ❤️

As humans we want to do enjoyable work that challenges us, that allows us to grow and learn. We want our work to have purpose. We want to be enriched by it.

For this to happen, we need to design for it, because it doesn’t just naturally happen.

As a senior engineer, are you happy to create yet another form? Are you happy to fix AI bugs? Are you happy to sit in countless meetings?

Some *yak shaving* is inevitable at work, but you don’t want people to be spending *most *of their time doing things that are trivial or unpleasant. You want to build **human capital** together with **tech capital**, so you should ask yourself:

- *Is everyone growing (and teaching!)?*

- *Is everyone challenged by their work?*

- *Is everyone’s talents used to the best of their ability?*

So if we agree on the speed + enjoyment factors, how do we work fast and enjoy what we do?

To answer this question I believe we need to go back to *what* engineers build.

### 🧱 Building product vs building platform

With some degree of simplification, there are two main things engineers can build in a team:

- **Product **— features that get used by customers.

- **Platform **— tooling that helps other people in the company work better.

Why is this separation important? Because I believe the value brought in by these two types of work is complementary, and it requires different skills and different workflows.

Let’s unpack this.

#### 1) Product engineering for *throughput*

Speed is always good, but it is *especially* important when you build product. Being faster at product means getting a better feedback loop with customers, who in turn inform you of what needs to be built.

Teams who are fast at building product in 2025 trend towards *product engineering* — that is, empowering single engineers to ship and own entire features.

These folks are [generalists](https://refactoring.fm/p/generalists-in-2025) — they might not be the best *engineers* from a tech perspective, but know how to navigate the whole stack, and are motivated by solving customers’ problems, as opposed to building tech.

Product engineering banks on a simple idea: if we increase the *scope* of what an individual can own, we are reducing the number of people who are needed to ship a batch of work, in turn reducing the meetings and overall cost of coordination.

![image](../assets/292bdf02815c809e.png)

It’s a self-reinforcing cycle that leads to productive teams and, very importantly, **happy people**, who can spend most of their time building as opposed to coordinating / managing status.

The main concern about product engineering is about **quality** — how can you ship quality stuff if single engineers own things from top to bottom? Nobody has the skills to do that.

This is true, and that’s were platform comes into play.

#### 2) Platform engineering for *quality*

I believe the right way to look at quality is not (just) as a matter of skills, but as a system. So the question becomes: how does your platform help product engineers ship quality software (and go faster)?

That’s where specialists come into play. You don’t want to use senior specialist engineering time to build yet another trivial feature, but to build tools that empower others. That’s 1) a better use of their time, and 2) more engaging and rewarding work at the same time.

In other words, I believe the correct mental model is to **scale throughput with generalists, and quality with specialists**. 

![image](../assets/293bdf02815c80fc.png)

That’s how you go *fast*, at *scale*, without compromising *quality*, and with everybody doing challenging work.

And by the way, as Camille pointed out, good platform engineering *suspiciously *looks like product engineering, but where your customers are other engineers 👇

[https://refactoring.fm/p/creating-a-platform-engineering-team?utm_source=publication-search](https://refactoring.fm/p/creating-a-platform-engineering-team?utm_source=publication-search)

In fact, platform engineers do the equivalent of what the very best product engineers do: they have design products (tools), build things that customers want, dogfood them, and ship things from top to bottom.

So, if this is an aspirational destination, how do you trend towards it?

### 🪴 How to scale quality (and product)

To build products you need multiple specialities, or layers: product mgmt, UI/UX design, coding (which you can split again in frontend, backend, …), down to ops (observability, infra).

The opposite of a product engineering team is team made of several specialists who need to carefully coordinate to ship anything meaningful.

If that’s your case, you can ask yourself: what is* hard* in any of these layers? Can you make it gradually easier?

- What is hard in Product? What does a PM do?

- What is hard in UI / UX design that cannot be accomplished by an engineer?

- What is hard in the various tech layers that prevents people from working full-stack?

- What is hard in ops that prevents engineers from delivering and owning things in production?

For anything that is hard, there are two ways to make it easier:

1. **Create process** — document how choices are made, with procedures.

1. **Create constraints** — physically limit the choices people can make.

Tasks always start as pure human judgement, then graduate into process, and finally into constraints.

Example: if you need to create a new button, that includes design work. What needs to be figure out? Potentially, a lot of things: margins, padding, corner rounding, colors, states, etc.

- **Judgment** — the basic level of this is using your designer’s expert judgment to design the thing, and hand it off to an engineer.

- **Process** — the intermediate level is to write down *rules* for how to do it, so that people can follow it without bothering the designer. E.g. corners are always rounded this way, and brand colors are this and that.

- **Constraint **— the expert level is to have a component library with pre-made buttons, so that engineers just use them and can’t physically do wrong.

The design example might look obvious, because it’s already common wisdom to work this way. But you can adopt this mindset for any part of work: what’s the version of this for product management? Or for observability? Or for backend?

The trick is getting into the habit of reflecting on how you make decisions, so you can continuously *bottle* human judgement into procedures, and eventually constraints.

When you think about it, this is the essence of engineering: turning chaos into rules.

At scale, this means that specific functions should work more and more in *consulting* mode: providing feedback and help on the things that fall outside of the scope of the rules, and constantly improving their respective platform.

They should not be designed to be in the *blocking* loop of regular operations — that would be a waste of their time, plus a limiting factor for throughput.

---

### 📌 Bottom line

And that's it for today! Here are the main takeaways:

- 🎯 **Define your vision before measuring progress** — without knowing what an elite team looks like, you can't assess your untapped potential or where to focus improvements.

- 🎽 **Focus on the team as your atomic unit** — solving how 5-10 people work together effectively unlocks solutions at both individual and organizational levels.

- ⚡ **Optimize for speed and engagement** — marathon speed (not sprint speed) is the ultimate quality that drives everything else, but you must also design for challenging, purposeful work that builds human capital.

- 🧱 **Scale throughput with generalists, quality with specialists** — product engineers who own features end-to-end reduce coordination costs, while platform engineers build tools that empower others to ship quality software.

- 📚 **Turn judgment into constraints** — continuously bottle human expertise into documented procedures and eventually into guardrails that make the right thing the easy thing.

- 🔄 **Move specialists toward consulting mode** — experts should provide feedback and improve platforms, not sit in the blocking path of regular operations.
