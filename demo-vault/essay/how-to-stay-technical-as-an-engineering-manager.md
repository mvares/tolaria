---
aliases:
  - "How to Stay Technical as an Engineering Manager"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-essays|Publish Essays →]]"
Status: Evergreened
URL: "https://refactoring.fm/p/how-to-stay-technical-as-an-engineering"
"👓 Status": Not started
"Date HH": 2025-07-03
"Created time": "2024-05-15T08:10:00.000Z"
Date: 2024-05-29
"Has Notes":
  - "[[evergreen/reactive-vs-proactive-work|Reactive vs Proactive work]]"
  - "[[evergreen/technical-managers-work|Technical Manager’s work]]"
  - "[[evergreen/things-you-can-build-as-a-manager|Things you can build as a manager]]"
Tags:
  - Updated
  - Mgmt
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 2679fd0b-d946-4815-b797-e1fcbba84843
---

# How to Stay Technical as an Engineering Manager

### 📑 Materials

---

[Remaining Technical as an Eng Leader](https://www.notion.so/fb0a293442544a86be3e776c9f804c85)

### ✍️ Post

---

Two weeks ago I published an article about how engineering management is changing.

It was driven by an awesome community thread, which got more than 20 replies, where plenty of managers commented on what their job looks like, what is expected of them, and more.

Then, a few days ago, I also had the chance to discuss this [with Aditya Agarwal on the podcast](https://www.youtube.com/watch?v=9svYG84r0v4).

Aditya is a legend: he joined Facebook as employee #10 and, years later, joined Dropbox as CTO when there were like ~20 engineers. 

In both cases, he experienced what we call *hypergrowth*: hiring sprees fueled by incredible user demand + huge VC money, during which you double your headcount every 6 months or so.

Such hypergrowth cycles, during the last decade, created today’s *big tech*.

However, there is the perception today that big tech is kind of *bloated*. Too many engineers, overblown management, too many layers — so I asked Aditya whether he thinks that we will ever see such headcount explosions again, or we are rather heading towards smaller, leaner engineering teams.

Aditya answered with a great insight, which, like all the best insights, looks obvious in retrospect.

Year after year, tech gets better. This makes us more productive, which in turn makes us accomplish *more* with *less*. It’s always been so: Facebook is smaller than Microsoft, and the next Facebook is bound to be smaller than today’s Facebook.

So we are *all* going to be doing more.

But more of *what*? My bets are the following:

- **Engineers are becoming *****full-stack**** —* and not just in coding. They will own entire features, do their own project mgmt, and often talk with customers.

- **Managers are becoming more technical** — they will be expected to contribute with code, practical directions, and being more hands-on.

However, while for engineers this path looks kinda straightforward, for managers it looks… tricky.

Technical work has little overlap with a classic manager’s work, to the point where we developed different career tracks altogether.

So, the natural follow-up question is: **how can you stay technical as a manager? **This question is actually two separate questions:

1. **How should you contribute *****technically***** to your team?** — what should you even do? How can you be helpful without 1) becoming a bottleneck, or 2) removing ownership from your teammates?

1. **How can you retain your tech skills?** — when you can only spend a fraction of your time on actual tech work?

While these are different questions, they are also *intertwined*. You want to retain the tech skills that are the most *helpful* to your team, which requires you to understand what kind of technical work is the most valuable for you to do.

So, you need to answer (1) first, to being able to address (2) properly. 

In fact, this will be the main angle of this piece: *how to stay technical… on your job. *This was the only possible angle 👇* *

### 💼 Learning on the job

There is a lot of advice about tech skills that looks like: make a side project, read this book, do this course… **on your spare time**.

These can be valuable, of course, but I have two objections:

- **Learning on the job is better **— when your learning is attached to a real goal, everything is better. You go deeper, you retain more information, and have a better feedback loop. 80% of your skills are shaped by your job: if you expect to do *career-changing* learning* *outside of it, it will not happen.

- **Self-directed learning is a luxury **— not everybody can afford to use their spare time on professional growth. You may have family duties, you may have an already demanding job, or you may just not have the extra motivation to do so.

So, today we will focus on how to stay technical as a manager, by making the most out of your work.

Here is our agenda:

- ↔️ **Reactive vs Proactive work** — let’s start from an unlikely place: *your schedule.*

- 🙅 **Giving up main dev work** — making peace with your time and your reliability.

- **👑 Technical manager work** — because coding isn’t everything.

- 👯 **Coding together** — code reviews vs pairing.

- 🔨 **Building things** — your three best bets: dev tools, tech debt, and exploration.

- ❓ **Hard questions** — bonus: seven hard questions you should ask yourself to figure out if you are getting behind.

Let’s dive in!

---

#### ↔️ Reactive vs Proactive work

Paul Graham’s essay about [Maker’s schedule vs Manager’s schedule](https://paulgraham.com/makersschedule.html) has long been a favorite of mine. 

TL;DR Paul argues that managers and makers (e.g. engineers, designers, etc.) run on different schedules:

- 🔨 **As a Maker**, you benefit from long, uninterrupted streaks of time where you do your focus work. 

- 🎽 **As a Manager**, your schedule is run by meetings where you make decisions that move the ball forward.

These schedules are not only very different, they are **incompatible**. 

As a Maker, you shouldn't be bothered with too many meetings, because those come at the expense of your productivity — but managers will drag you into them because that’s how they do their work.

![image](../assets/bbc320275a874f35.png)

Now, while this makes for a great mental model, **I also find it a bit simplistic**, especially when applied to technical management. For two reasons:

1. **☯️ Black / White** — in engineering, it is rare to find managers who run on a *pure* manager’s schedule like PG suggests. Everyone is a *blend *of some maker’s and manager’s work, with the magic being on finding the blend that works best for your team.

1. ⛑️ **Support to makers** — counterintuitively, one of the major reasons why managers don’t have a lot of *guaranteed* focus time, is to support makers. *Wait what? *Hang on with me 👇

I believe a better way to think about your schedule, is in *proactive* vs *reactive* terms:

- ➡️ **Proactive work **— that’s your scheduled, planned work. This is often done in *anticipation* of your team’s needs: *hiring*, *planning*, *1:1s*,* *are all examples of proactive stuff that runs on a schedule.

- ⬅️ **Reactive work **— that’s *unexpected *work that *reacts* to your team’s needs. That’s whenever you need to clarify some specs, jump in on a technical dilemma, handle a resignation, or defuse some conflict.

And here is the thing: managers are naturally subject to way more reactive work than makers, which is what effectively messes up with their calendars.

Reactive work is sneaky. It looks like you can lock those two hours of coding on Wednesday, until you get a DM on Slack and figure out that 3 people are stuck and need your intervention.

This divide between reactive vs proactive work is incredibly important — in fact, improving management’s health can often be framed as some version of turning reactive work into proactive:

- *Improve career framework → make career conversations more predictable*

- *Improve design process → reduce reactive changes to specs*

- *Improve hiring process → make resource allocation more proactive*

- …

So, let’s take a step back: why are we nitpicking about people’s schedule now?* *Because understanding where your time goes is the first step to use it for good.

Which leads us to the very first advice for managers who want to stay technical:

---

### 🙅 Give up main development work

In most cases, the combination of 1) less time for coding, and 2) a less reliable schedule, makes it impractical for managers to take on main dev work. More in particular, as a manager, I wouldn’t take on work that:

- is important and has a well-defined deadline, and/or

- requires collaboration and *hot-potatoing* between multiple people, like other devs and designers.

Basically, in all cases where you need to be *dependable*, you should probably be conservative and accept that… you are not.

Of course, your mileage may vary. What if you are a tech lead and are *expected *to do high-priority coding, in addition to some managerial work? In my experience, people use a *best effort* attitude: they do both as long as it is manageable, and fallback to the one they are the most comfortable with when the pressure is higher. Which is typically coding.

So, experienced managers know that part of their duties is to *stay available* to their team, and keep some slack in their schedules. Then, if reactive work doesn’t *materialize*, you can always fallback to other things — but these are not things you have decisively committed to. 

Fortunately, there is plenty of technical work you can contribute to that is not *mainline* coding. In fact, there is plenty of it that is not coding… at all 👇

---

### 🎽 Technical manager work

As a manager, to understand where you can have an impact in engineering work, you may reflect about the unique qualities you bring to the table, with respect to other engineers.

These may vary, but the main one you should start with is **business perspective**.

As a manager, you have context into a lot of things that other engineers may not have a clue about. Is it time to invest in foundational, long-term work, or is it time to be scrappy? What is the appetite for this feature? Can we get more resources to go after this?

These constraints *need *to affect technical decisions, and you are the best person to make it happen.

Here are the situations where you can use your manager’s acumen to pull your technical weight 👇

#### **1) Design conversations **✏️

In my experience, design conversations are the prime *avenue* for EMs to valuable technical impact. For two reasons:

1. **Good design serves business** — this is where you make sure interests are aligned and people build right thing.

1. **Good design is *****loosely***** coupled to tech stack** — even if your tech chops may *decay* with time, design skills are timeless and you will still retain the ability to jump in and ask good questions, even if you are not coding that much anymore.

#### **2) Technical strategy **🗺️ 

A good technical strategy fits the wider company strategy and shows how to reach its goals by creating leverage through technology.

When it succeeds in doing so, it is a real superpower. It makes it easier to advocate for resources and it creates alignment around the work to be done.

Technical strategy can also be very technical, by including scale assumptions, buy vs build decisions, and design tradeoffs. This is all work you can have a decisive impact on.

#### **3) Asking the right questions **❓

Finally, in your team’s life there is a long tail of situations where technical / semi-technical conversations happen — think of retrospectives, post-mortems, people venting about this or that decision, and so on.

In any of these situations, you may or may not feel like you belong. I have found that this feeling of belonging, or, conversely, the feeling of being an impostor, is prompted by the sneaky idea that you can only contribute by **providing a solution** to things. By giving your take.

That’s not true.

There is a lot — *a lot —* of value in just asking questions. What feels confusing about this? Why is this a constraint? What would the perfect solution look like, and why? What if we had just 2 days to build it?

On technical matters, people on your team will almost always be in the better spot for making the right call, but you can still help them. You can make them think. You can ask questions for *them* to answer, because you are not the best person to answer them anymore — and that’s 100% ok.

---

### 🔨 Building things

All of this doesn’t mean you shouldn’t code anymore — in fact, you probably should. 

So, what should you build? In my experience, here are your best bets:

#### **1) Dev tools **🚚

Do work that improves the developer experience of your team. This is a favorite of mine, because at once it 1) gets you in touch with important pieces of your tech stack, and 2) keeps you aware of the daily life of your engineers. 

This way, if your engineers have a shitty experience, you’ll know it — and you’ll be putting in work to improve it, which helps win their trust.

#### **2) Bugs / tech debt **🦠

Bugs and small pieces of debt are perfect candidates for some coding on your spare (work) time. If your team has some fixed allocation on maintenance, you can join them. 

On top of this, joining on-call rotations as a manager is a great way to stay in touch with the state of your tech. However, only do this if you can be as capable as others to take care of things: don’t do it if you constantly need to page your secondary.

#### **3) Tech exploration **🔭

You can also take some time aside to explore cool technology that may or may not be useful in the future . You can build prototypes, write down your considerations, and discuss findings with the team.

The only caveat is that, for reciprocity, if you take some time for exploration, make sure you allow your engineers to do the same.

---

### 🤝 Coding together

Finally, you can find ways to collaborate with your engineers and build things together. There are two main ways people do this: **code reviews**, and **pairing**.

#### **1) Code reviews **🔍

I know many engineering managers who do code reviews, and, as a CTO, I have done them myself for a long time.

Today, I have mixed feelings about this.

As long as you are 100% proficient in the tech, doing code reviews as a manager can be extremely good. In fact, other than the review itself, you can use them to spot missing docs, things to add to principles/guidelines, and more.

However, as soon as you get a bit rusty, they easily become toxic.

They either turn into an infinite series of *looks good to me*, or you may feel compelled to say something *smart *to prove your value, which kind of always achieves the opposite effect. This way, your reviews can easily turn into an awkward, pointless blocker, and your teammates can *immediately* spot this.

So my take is: only do reviews if you are sure you can be valuable, otherwise, even *no *code* *review is better than a *bad* code review.

#### **2) Pairing **👯

Another way to collaborate with engineers on coding is pairing. In my experience this is generally healthy and escapes many of the traps of the code reviews above.

You can spend more or less time in driver/navigator mode based on your comfort with the tech, you can use it as learning time, and you can still be valuable by rubber ducking and helping on design matters.

Also, like building dev tools, it gives you first-hand experience of your team’s developer experience, which code reviews do not necessarily do.

---

### ❓ How to know if you are getting behind

Finally, do you even* need* to catch up with your technical impact, or your technical skills? How do you figure this out?

I love Alex Ewerlof’s seven questions about, which were published in [this piece](https://blog.alexewerlof.com/i/135946550/how-technical-should-the-em-be):

1. *Do you ****understand what the engineers are doing**** on a daily basis? It’s not about micro-managing, but rather having a solid understanding that is not too high level and abstract.*

1. *If the ****Engineering Manager position disappears from earth**** will you be able to go back to development, or be left jobless?*

1. *If the engineers get stuck in technical tasks, how likely is it for them to come to you for ideation? Do they ****respect your experience as an engineer**** or are you considered out of date?*

1. *When there’s a technical disagreement, how early do you learn about it? Do you primarily rely on one or more favorite team members to chew technical matters and feed you or can you ****digest this first-hand from browsing the repo****?*

1. *And when conflict comes your way, do you quickly ****understand the trade-offs**** to be made?*

1. ***Can you draw the architecture diagram**** for everything your team owns? Can you explain how the testing and CI/CD are set up for your team?*

1. *When meeting with higher-level leaders, how likely is it for you to fight for your team against unrealistic technical expectations? ****Can you assess those situations**** without having to drag the team into every meeting?*

---
