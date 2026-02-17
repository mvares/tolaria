---
aliases:
  - "Monday #73"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-monday-idea|Publish Monday Idea]]"
Status: Published
"👓 Status": Not started
"Created time": "2024-04-18T15:09:00.000Z"
Date: 2023-10-16
"Has Notes":
  - "[[evergreen/tech-choices-for-side-projects|Tech choices for side projects]]"
  - "[[evergreen/principles-of-team-organization|Principles of Team Organization]]"
  - "[[evergreen/should-you-deploy-on-fridays|Should you deploy on Fridays?]]"
Tags:
  - Monday
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 2cc060ec-887c-46a7-aab8-3361ed7d637b
---

# Monday #73

*Hey, *[*Luca*](https://twitter.com/lucaronin)* here! Welcome to the ****Monday Ideas ***💡

*Every Monday I send you an email like this with ****3 short ideas**** about making great software, working with humans, and personal growth.*

*Paid members also receive a long-form, original essay on Thursday, like the last one:*

[https://refactoring.fm/p/how-to-organize-personal-work](https://refactoring.fm/p/how-to-organize-personal-work)

*To receive all the full articles and support Refactoring, consider joining 1400+ engineers and get the paid membership!*

Get full access to Refactoring ✨

[https://refactoring.substack.com/subscribe](https://refactoring.substack.com/subscribe)?

*p.s. learn more about the *[*benefits of the paid plan here*](http://refactoring.fm/about)*.*

---

### 1) 🎽 Principles of Team Organization

Within each company, there are groups of people who are more likely to work together than others. 

Creating *teams* means defining *processes* that make it easier for such people to interact on a regular basis. 

So, team structure shapes how *communication* happens, which, in turn, shapes how software gets made. As by Conway’s law 👇

> *Any organization that designs a system (defined broadly) will produce a design whose structure is a copy of the organization's communication structure.
*— Melvin Conway

The main takeaway of Conway’s law is that if you create a good team organization, software will largely take care of itself.

But what makes a team organization good?

I have a personal heuristic that looks at three things: **Autonomy**, **Cognitive Load**, and **Responsibilities**. 

#### 1) Autonomy 🏃‍♂️

You create teams to be *autonomous*.

What makes a small startup go fast is how cohesive and nimble the team is — people can work quick and without overhead. In a larger org, you most likely want to replicate this by creating many of such teams.

#### 2) Cognitive Load 🧠

A good team should own an amount of software that can *fit in their head*. 

Engineers and teams are able to bring the most value when they sustain the right amount of *cognitive load* for their work: not too much, not too little.

Optimizing cognitive load is one of the main lessons by Team Topologies — one of the most influential works on team organization, which we reviewed earlier this year 👇

[https://refactoring.fm/p/team-topologies](https://refactoring.fm/p/team-topologies)

You should spend most of your cognitive load *budget* on domain and business knowledge, which creates actual value, and minimize the load that comes from extraneous stuff like bad DX or convoluted tech.

#### 3) Responsibilities 👑

In good teams, all the bases are covered. You know exactly who is responsible for what, and people have the right skills for the job.

In a modern software team there are three main responsibilities: 

- 🎨 **Product **— owning the roadmap, feature requirements, and communication with customers & stakeholders. Creating alignment and removing obstacles from the way of the team.

- 🔨 **Tech **— owning the technical direction of the product. Making design decisions and guiding the development.

- 🌱 **People **— taking care of people’s growth and wellbeing. Working on processes, hiring, and career tracks.

Should these responsibilities belong to separate people or they can partially conflate on the same ones? I wrote more about this in a full, extensive guide I published this summer 👇

[https://refactoring.fm/p/how-to-structure-engineering-teams](https://refactoring.fm/p/how-to-structure-engineering-teams)

---

### 2) 🕹️ Tech choices for side projects

What tech should you use for your side projects? It depends on your goal.

- Is your goal *learning*? Try some new shiny stuff.

- Is your goal shipping an MVP asap and making some money? Use the stack you are most comfortable with.

Not rocket science, of course, but it is still easy to *fuck this up* when you start a project with *conflicting* goals in mind, like: “*I want to create a good SaaS and also learn some new tech”*.

While doing both is not impossible and can even be good for your motivation, think about McFunley’s [innovation tokens](https://mcfunley.com/choose-boring-technology#:~:text=him%20only%20slightly.-,Embrace%20Boredom.,-Let%E2%80%99s%20say%20every) and choose wisely where to use proven tech, and where to take some calculated risks.

To accelerate development, then, consider two things:

- 🍱 **Keep a boilerplate of your favorite stack** — My friend [Vic](https://twitter.com/VicVijayakumar) maintains a Github repo with everything he needs to start a new SaaS instantly, complete with payments, auth, backoffice, and UI scaffolding.

- 🪄 **Use no/low-code tools** — there exist plenty of handy tools to lift coding weight from your shoulders. I wrote a full article about them a while back 👇

[**How to Build Anything with No-Code 🪄**](https://refactoring.fm/p/how-to-build-with-no-code)

Feel free to read the full article, but I am also going to give you a hot take: if you are serious about shipping fast, the #1 component to *low-codify* is probably your *database*, by replacing it with something like **Airtable** or **Google Sheets**.

I know, this looks insane, and it also goes against everything I have written in the past about choosing boring / exciting tech 👇

![image](../assets/f9cc34af790b4190.png)

Your database is arguably the most important component of your stack, *and* the one with the highest lock-in — Luca wtf?!

However, consider this:

- Data needs to be edited, and with Airtable/GS you get an awesome admin UI for free.

- Data needs permanent, paid hosting (as opposed to functions and frontend these days) — which you get for free on Airtable/GS.

- Airtable/GS can express an awful lot of business logic via formulas and references, all of which you should code otherwise.

- Airtable/GS give you CRUD API for free.

- Airtable/GS play nicely with plenty of other tools out there, including workflow ones like Zapier, for even more automation.

So think about it!

I wrote a full edition about side projects about one month ago 👇

[https://refactoring.fm/p/how-to-build-side-projects](https://refactoring.fm/p/how-to-build-side-projects)

---

### 3) 🔥 Should you release on Fridays?

This is a complicated question that has no singular answer. 

My take is that wellbeing of your team should be your #1 concern, so if your folks don’t feel confident, you shouldn’t release. Full stop.

If you find yourself in this situation, though, you should investigate *why* it is so. You can and should work to build that confidence, knowing that the best engineering teams make no difference between Fridays, Mondays, or Thursdays.

To get you closer, here are a few things you may consider:

- 🌅 **Release in the morning **— with good observability in place, you can catch 95% of issues within a few hours.

- 🚩 **Release behind a feature flag **— push the code but keep it disabled.

- 🔒 **Release to a beta group **—make the update available only to a subset of users, which dramatically reduces the risk.

- 🐛 **Do quality Fridays **— you can use Fridays to squash bugs and do some maintenance, which is low-risk stuff to release.

So, your mileage may vary, but just know that *never* deploying on Fridays has hidden costs:

1. You will batch more stuff together and have a riskier deploy on Monday, and 

1. People will have lost some context and debugging will be harder.

More on maintenance and feature flags 👇

[https://refactoring.fm/p/feature-flags](https://refactoring.fm/p/feature-flags)

[https://refactoring.fm/p/how-to-plan-for-maintenance](https://refactoring.fm/p/how-to-plan-for-maintenance)

---

And that’s it for today! If you are finding this newsletter valuable, consider doing any of these:

**1) ✉️ Subscribe to the newsletter** — if you aren’t already, consider becoming a paid subscriber. 1400+ engineers and managers have joined already! Learn more about the [benefits of the paid plan here](http://refactoring.fm/about).

Get full access to Refactoring ✨

[https://refactoring.substack.com/subscribe](https://refactoring.substack.com/subscribe)?

**2)** 🍻 **Read with your friends** — Refactoring lives thanks to word of mouth. Share the article with your with someone who would like it, and **get a free membership** through the new [referral program](https://refactoring.fm/p/referral).

Read with your friends 🍻

[https://refactoring.fm/leaderboard](https://refactoring.fm/leaderboard)

I wish you a great week! ☀️

Luca
