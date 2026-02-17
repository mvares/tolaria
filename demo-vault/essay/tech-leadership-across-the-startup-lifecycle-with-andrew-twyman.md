---
aliases:
  - "Tech Leadership across the Startup Lifecycle — with Andrew Twyman"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-essays|Publish Essays →]]"
Status: Evergreened
URL: "https://refactoring.fm/p/tech-leadership-for-startups"
"👓 Status": Not started
"Created time": "2024-04-18T14:53:00.000Z"
Date: 2023-05-25
"Has Notes":
  - "[[evergreen/external-vs-internal-coaching|External vs internal coaching]]"
  - "[[evergreen/anticipate-tech-debt-rather-than-prevent-it|Anticipate tech debt rather than prevent it]]"
  - "[[evergreen/invest-in-abstractions-that-are-core-short-term-payoff|Invest in abstractions that are core + short-term payoff]]"
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 00725f75-d295-46a5-9f1d-f1cb17690562
---

# Tech Leadership across the Startup Lifecycle — with Andrew Twyman

### 📑 Materials

---

### 💡 Ideas

---

### Andrew’s career

### Times

00:01:09 Andrew’s career
00:06:25 Balancing velocity & quality
00:10:16 Two extremes, where is the right tradeoff?
00:14:50 Standard level of rigor into the dev process
00:15:58 Dev quality vs engineers happiness
00:18:10 Handling tech debt
00:27:47 Hack weeks
00:31:18 Boy Scout Rule
00:36:29 Engineering Coaching

### ✍️ Post

---

Hey! We are back with another interview to an accomplished tech leader, after the [last one with Thiago](https://refactoring.fm/p/how-to-design-a-great-tech-career). 

This is a new experimental format that combines video + a regular article. The article includes a summary of what we discussed during the interview, plus my own thoughts about the very same topics.

If you like it and want to see more of these, vote with your feet 😄 by liking/sharing this edition, or replying via email/comments below!

---

A couple of weeks ago I interviewed Andrew Twyman, Engineering Coach and former Staff Engineer at Dropbox, in a live event in the Refactoring community. 

Andrew has had an impressive career so far:

1. He came out of **MIT** in ‘99, and joined **Maker Communications**, which fabricated network processor chips, in the middle of the dot-com boom. There he wrote firmware in assembly and worked through an IPO, acquisition, and subsequent spin off.

1. Then, he joined **Liquid Machines**, where he worked on docs and email encryption. The team grew rapidly from 20 to 75 people before crashing in 2008, together with the rest of the economy. Andrew witnessed 3 rounds of layoffs and the final acquisition by a larger incumbent.

1. In 2012 he joined **Dropbox** in full hyper-growth phase: the team grew from 250 engineers to 2000+ in about three years, more than doubling year over year.

1. Today, Andrew is *semi-retired*—in his own words—and helps tech leaders as a professional Engineering Coach.

What is the most impressive about Andrew’s journey is that he has literally seen it all: from small startups, to mid-size companies, to big tech, together with IPOs, acquisitions, and layoffs.

For this reason, today we will cover some evergreen tech leadership topics for which the answer is usually “*it depends*”. That’s because Andrew is one of the few out there that can also answer the follow-up question: “*depend on what?”*.

Here is what we will cover:

- ⚖️ **Balancing velocity with quality**

- 🦠 **Handling tech debt**

- 🪴 **Engineering Coaching**

Let’s dive in!

---

### ⚖️ Balancing velocity with quality

[Link to the video chapter](https://www.youtube.com/watch?v=onB43s6lBhE&t=385s)

Andrew’s learnings about development *rigor* are particularly interesting because he has lived two experiences, both extreme in their own way, that also led to extreme outcomes.

1. **Liquid machines** — promoted engineering excellence from day one and invested in awesome custom tooling and internal frameworks, mainly in C++. Engineers loved these and were happy to work on them. However, the product eventually failed and it feels like the team didn’t live to see the pay off on such investment.

1. **Dropbox **— was more chaotic in the early days. Early code sometimes felt hacked together and messy, and the team had to deal with sizeable technical debt over time. However, as we know, the product became hugely successful. Problems were gradually addressed and the team was always able to deliver.

So, it would be easy at this point to conclude that you should* “move fast and break things*” — but things are more nuanced than this. Let’s look at more angles from these stories 👇

#### Abstractions and payoff

Most of the times, when talking about startups that need to move fast, we warn against creating premature abstractions because these may be invalidated by the product evolution.

Something that stands true today might not be anymore one day, so we should only invest, engineering-wise, on what feels rock solid.

Now, what strikes me about the Liquid Machines story is that what they built wasn’t *wrong*. The tooling was genuinely useful and grounded — only, the team didn’t live to see the payoff.

The abstractions where *right* but they where built with the idea of 1) using them for a long time to build a lot of stuff, and 2) with a team that would grow to 100s of engineers.

So, they built the right things, but for **too far off in the future**.

![image](../assets/7f4a5dfe6fd74c6c.png)

Let’s look at Dropbox, now 👇

#### MVP vs engineering culture

Andrew stressed a lot during the interview that Dropbox code could be messy sometimes, but they had an *awesome* engineering culture.

Both Drew and Arash, its founders, are MIT engineers. From day one they promoted good habits and encouraged people to sweat the details, but they also prioritized getting the product in front of customers.

How do you do both?

Andrew believes that a great engineering culture is one that rewards not over-engineering stuff. Basically, you should find the *minimum viable engineering* for any problem you need to solve. 

It is okay sometimes to take shortcuts to meet a deadline or validate a feature, as long as the team is *intentional* about it. E.g. you might write code that is a bit redundant, but in a way that is clear and easy to refactor down the line, so that the impact is low.

So, Dropbox tried to combine a *scrappy* mindset with one of excellence on those basics that have the highest ROI even in the short term, like:

- Writing basic tests

- Writing clear code and commenting it

- Keeping clear contracts between components

Their approach was not perfect by any means, but in hindsight was probably closer to ideal than Liquid Machines.

### 🦠 Handling Tech Debt

[Link to the video chapter](https://www.youtube.com/watch?v=onB43s6lBhE&t=1090s)

Technical debt is closely related to how you balance velocity and quality, so our discussion naturally gravitated towards that.

Tech debt is also notoriously hard to define. For Andrew, debt should be mostly judged by the *tax*, or the* interest*, you pay for it, rather than how much or how little debt itself is. 

[https://refactoring.fm/p/the-true-meaning-of-technical-debt](https://refactoring.fm/p/the-true-meaning-of-technical-debt)

In that regard, not all debt is created equal. There are pieces of nasty code that, left alone, do not cause much trouble to anybody. And there are abstractions that leak in a subtle way, on top of which a lot of stuff is built, so that debt only gets worse with time. 

In a way, for tech debt we can have a *dual* conversation with respect to the one on engineering investments above:

- **Engineering Investments **— you want the payoff to be *as high as possible*, and *as early as possible*.

- **Technical Debt **— you want the tax to be *as low as possible*, and pay it *as late as possible*.

So you want to pay early debt that is 1) high-interest — you spend a lot of KTLO time on it — and 2) is more likely to get worse over time.

Riot Games contagion 👇

[https://refactoring.fm/p/technical-debt](https://refactoring.fm/p/technical-debt)

#### Good design is intentional about limits

One of the best way to handle technical debt is *anticipating *it, which is not necessarily the same as *preventing* it.

During the design phase, you can often anticipate that something will not scale over some limit, or an abstraction will not fit if *X* happens. These limits are important to be discussed to make sure you are designing for the right scenario.

A limited design is *good* as long as you won’t touch those limits for a long time.

You can encourage this reasoning by addressing these parts in your design docs. You may include, for example: 

- **Anti goals **— goals and features you are intentionally *not* designing for.

- **Limiting factors / land mines **— stuff that might be problematic for the current design if it happens. E.g. traffic load, or future features.

- **Operational cost **— how much it costs to maintain the feature, if there is any maintenance cost that you can anticipate.

In my experience, when all the cards are on the table, it is rare that you make truly terrible calls.

Let’s talk now of how Andrew repays debt 👇

#### Boy Scout rule

[Link to the video chapter](https://community.refactoring.club/home#:~:text=47%20Hack%20weeks-,00%3A31%3A18,-Boy%20Scout%20Rule)

The gold standard for handling small debt is to encourage people to make those changes whenever they are working on that code for any other reason. You basically follow [Robert C. Martin’s boy scout rule](https://www.oreilly.com/library/view/97-things-every/9780596809515/ch08.html):

> *Always leave the code better than you found it.*

This works also in reverse: if it’s small and unassuming, do not touch it unless you need to do something with it anyway. Which means, for the better or worse, that the timeline for such improvements is *best-effort* (it depends on other tasks), so it is only suitable for issues that are not too harmful.

The boy scout rule should be promoted explicitly to make people take it seriously, especially PMs and non-technical stakeholders who should allow some slack to fit this kind of work. However, I can tell you that many good engineers will sneak it in and do it anyway, even without you promoting it.

#### Swim lane for maintenance

Andrew likes to dedicate some time budget every sprint to maintenance tasks. Such time is mostly self-directed—engineers know better what is causing the most issues—but tech leaders usually put some structure to make sure engineers do not get lost into obscure optimizations.

About such structure, in my experience it works well to have a recurring *maintenance meeting* to brainstorm what needs the most work and have people committing on it.

#### Hack weeks / bug bashes

[Link to the video chapter](https://community.refactoring.club/home#:~:text=Handling%20tech%20debt-,00%3A27%3A47,-Hack%20weeks)

In a great anecdote, Andrew tells how in Dropbox they used to run *hack weeks* twice a year, in which people could pick their own projects and build cool stuff.

To much of the managers’ surprise, many of the projects that came up where about repaying tech debt.

While this looks counterintuitive — if you could work on *anything*, would you choose to work on tech debt? — it just makes sense when you think of it.

People naturally focus on the things that bother them most on a daily basis. These are often areas where they can make engineering investments to bring about decisive improvements. For example, improving the CI/CD, the design system, or the observability pipeline. 

Andrew notes that people took advantage of the open ended nature of hack weeks to tackle problems that wouldn’t be addressed otherwise.

---

### 🪴 Engineering Coaching

[Link to the video chapter](https://www.youtube.com/watch?v=onB43s6lBhE&t=2189s)

In the recent years, Andrew has been working part-time at [Practica](https://practicahq.com/) as a professional engineering coach. That’s actually how we met: I also was a coach there for some time.

I am a big believer in engineering coaching and I took advantage of this interview to discuss its benefits with Andrew.

#### What coaching is useful for?

One of the things we agreed on is that coaching is a natural outgrowth of your role as a tech leader — if you are good at your job, chances are you already coaching people on your team in some fashion.

*External* coaching, though, is different than *internal *coaching in some decisive ways. In particular, a coach is rarely effective on hard technical skills, because 1) they have little context into your work, as they don’t work at your company, and 2) because you only talk/work with them e.g. once every two weeks. 

Practical tech work requires time and a lot of shared context, so don’t expect an external coach to be best choice to grow on this.

What a coach brings, instead, is an external perspective backed by their extensive experience in the industry. In my experience, this is especially useful for:

- ✨ **Universal skills** — leadership, management, collaboration, communication

- 🔄 **Processes** — e.g. how your dev process works, how to manage tech debt, how to organize teams, etc.

- 🪜 **Career growth** — e.g. advice about direction, having more impact, goals, etc.

- 🌱 **Personal** — e.g. relationships with co-workers, healthy/toxic environments, stress, discrimination, etc.

For many of these, having little context is actually an asset. In fact, when you talk with people from your company, you both might take for granted something that you shouldn’t. Say there are some toxic dynamics around management — you might not challenge these with your co-workers because *hey*, it’s been like that forever, it’s ok. An external coach, instead, can tell you “*it’s not ok*” because they look at things with a fresh pair of eyes.

#### What jobs coaching is best for

Based on this, I feel like the more your impact is removed from your pure tech chops, the more external coaching is valuable. So, I would recommend coaching for managers—even fresh ones— and ICs at least at senior levels.

In general, the higher your level the more the external perspective is valuable. Also, the higher your level the less peers you will have to draw opinions from, and the more you risk to live in your echo chamber.

For junior / mid level individual ICs, instead, I would look for someone on their team to be their mentor.

You can be intentional and ask people about mentoring you regularly, but ideally there should be a path for formal mentorship in your team/company. You can your manager about this, both to get their feedback and to keep them in the loop about your initiative. To be clear, your mentor probably *shouldn’t *be your manager. If you are an IC, I have found it more useful to spend time with senior ICs pairing on features, writing design docs together, and in general stealing their craft.
