---
aliases:
  - "Monday #71"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-monday-idea|Publish Monday Idea]]"
Status: Published
"👓 Status": Not started
"Created time": "2024-04-18T15:09:00.000Z"
Date: 2023-10-02
"Has Notes":
  - "[[evergreen/icap-framework|ICAP Framework]]"
  - "[[evergreen/the-three-types-of-cognitive-load|The Three Types of Cognitive Load]]"
  - "[[evergreen/do-small-maintenance-with-the-boy-scout-rule|Do small maintenance with the Boy Scout rule]]"
Tags:
  - Monday
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 8d9b65c2-54ec-484e-b1e0-a1a274e54ab6
---

# Monday #71

*Hey, *[*Luca*](https://twitter.com/lucaronin)* here! Welcome to the ****Monday Ideas ***💡

*Every Monday I will send you an email like this with ****3 short ideas**** about making great software, working with humans, and personal growth.*

*You will also receive a long-form, original article on Thursday, like the last one:*

- **How to Handle a Departure**

*To receive all the full articles and support Refactoring, consider subscribing if you haven’t already!*

Get full access to Refactoring ✨

[https://refactoring.substack.com/subscribe](https://refactoring.substack.com/subscribe)?

*p.s. you can learn more about the *[*benefits of the paid plan here*](http://refactoring.fm/about)*.*

---

### QA Wolf?

---

### 1) 🧠 The Three Types of Cognitive Load 

Engineers and teams are able to bring the most value when they sustain the right amount of *cognitive load* for their work: not too much, not too little.

However, not all cognitive load is created equal. Based on [Team Topologies](https://refactoring.fm/p/team-topologies), there are three kinds:

- 🔨 **Intrinsic** — your tech skills, which are intrinsic to your work. E.g. how classes are defined in Java.

- 🐌 **Extraneous** — stuff you have to remember that doesn’t bring value, so it is mostly a distraction. E.g. *how do I deploy this app, again?*

- 🌟 **Germane** — knowledge about your business domain and the problems you need to solve. E.g. what are good abstractions for financial data, or best practices for an e-commerce checkout.

Germane load is the only knowledge that creates *value*. So, you want to create teams where such load is maximized, while *intrinsic* and *extraneous* ones are minimized.

#### 🔨 Reducing Intrinsic Load

Intrinsic load is about technology. 

You can reduce it via good tech choices that make stuff easy to build. E.g. building your prototype with a low-code tool can reduce the *intrinsic* load required to operate it, as opposed to going for a custom full-stack app.

Also, you can reduce intrinsic load by working on your team capabilities, instead of your tech, with training, pair programming, and hiring for the skills you are missing.

#### 🐌 Reducing Extrinsic Load

Extrinsic load is about *bureaucracy* — meant as the unnecessary tasks and steps you need to perform in your dev process.

Extrinsic load is minimized by creating good DX. I have found that optimizing for fast and frequent releases, good tooling, and, in general, a culture of continuous delivery, is the best cure for this.

#### 🌟 Optimizing Germane Load

When you put all things together, you should organize teams so that they are able to apply their *domain knowledge* to solve problems of the *right size*, minimizing the amount of *plumbing* and non-business-related effort.

You can find the full review and summary of Team Topologies in this past edition 👇

[https://refactoring.fm/p/team-topologies](https://refactoring.fm/p/team-topologies)

---

### 2) 🏅 Boy Scout Maintenance

> ***Always leave the code better than you found it.***
— Robert Martin (Uncle Bob)

The boy scout rule, coined by Robert Martin, is about taking the chance to improve the code whenever you are already making changes to that code, for any other reasons. Think of adding a test that wasn’t there, or updating a small dependency. 

This approach works well, but not for everything. A few upsides and downsides:

- 🟢 **It avoids context-switch** — it makes the change cheaper than scheduling a separate task

- 🟢 **It doesn’t require negotiation** — it is just agreed that estimates keep some *slack *for this type of tasks.

- 🔴 **Timeline is best-effort **— doing such improvements depends on other tasks, so it’s only suitable for issues that can afford to wait kind of indefinitely.

- 🔴 **Only suitable for very small tasks **— Adding a few hours to improve existing tests is ok, but you can’t slip e.g. two days of maintenance on top of two days of feature work with the *boy scout rule*. I have seen it happen and it breaks trust. Don’t do it.  

A corollary of the rule is to *do immediately* whatever is too small to be otherwise tracked and planned.

> ***"Will it take less than two minutes?" Yes, then do it.
****— *David Allen, Getting Things Done

This is lifted straight from the [GTD](https://en.wikipedia.org/wiki/Getting_Things_Done) methodology, where David Allen advocates to do on the spot any task that requires less than two minutes to complete, like sending a short email or making up the bed.

In software, you might want to put the threshold to 5-10 mins, and there are plenty of stuff that falls into this:

- Small cosmetic updates to the UI

- Very small bugs

- Changing a piece of copy

In these cases, you will spend more time creating a ticket and pondering (multiple times in the long run) when to do it, than just by doing it on the spot. So do it, or ignore it forever (which is equally ok).

I wrote a full piece about how great teams handle maintenance 👇

[https://refactoring.fm/p/how-to-plan-for-maintenance](https://refactoring.fm/p/how-to-plan-for-maintenance)

---

### 3) 🎓 The ICAP framework

The ICAP framework was created in 2014 by Michelene Chi, who demonstrated how higher student engagement leads to a better learning outcome.

ICAP buckets learning experiences into four main categories, in ascending order of engagement, and, therefore, effectiveness:

1. **🔴 Passive **— experiences where you are just exposed to some learning material, like a book, or a lecture.

1. **🟡 Active** — experiences where you have exercises to complete as part of your learning like regular online courses.

1. **🟢 Constructive** — experiences where you learn *by doing.* The building is a core part of the learning process, like in a *workshop*.

1. 🟣 **Interactive** — experiences where constructive learning is augmented by asking questions and getting continuous, real-time feedback, like in *pair programming*.

Interactive learning leads to the highest retention, especially in areas that are very *hands-on*, like tech skills.

You can put popular education options on this scale, from the most *passive* to the most *engaging*: books, newsletters, online courses, workshops, 1:1 coaching, pair programming, etc.

![image](../assets/c5026bab88744122.png)

When it comes to the *quality* of the learning, there is no doubt that the more you move to the right, the better.

However, deep interactive experiences are not always the best call. In fact, these are also: 

1. **Hard to design** — it’s tough to create learning material that includes a lot of building and active stuff, as opposed to simple slides or text.

1. **Hard to scale / expensive **— the more feedback loop people need, the more bespoke the experience needs to be, the worse it scales. Some of the most *interactive* learning experiences in tech are pair programming and coaching, which are both 1:1.

1. **Demanding for the learner **— interactivity is about intensity. You are getting more results because you are putting it more effort. You can’t always afford that.

So, passive experiences may have low retention but are also cheaper and low-effort. Sometimes, that’s bad — but sometimes that’s just what you need.

E.g. I am a fan of the [RealLifeLore](https://www.youtube.com/channel/UCP5tjEmvPItGyLhmjdwP7Ww) Youtube channel to learn more about geopolitics. I don’t have a personal goal about this, so I am just happy to watch some videos, knowing that my understanding will be shallow, and retention low. Also, I usually watch them over lunch, so I don’t really have the energy bandwidth for more. For this use case, the passive approach is perfect!

So, I believe you can maximize learning by finding the right blend of passive and active experiences, based on what you need the learning for.

More ideas about investing in your professional growth (and that of your team) 👇

[https://refactoring.fm/p/how-to-invest-in-engineers-growth](https://refactoring.fm/p/how-to-invest-in-engineers-growth) 

---

And that’s it for today! If you are finding this newsletter valuable, consider doing any of these:

**1) ✉️ Subscribe to the newsletter** — if you aren’t already, consider becoming a paid subscriber. You can learn more about the [benefits of the paid plan here](http://refactoring.fm/about).

Get full access to Refactoring ✨

[https://refactoring.substack.com/subscribe](https://refactoring.substack.com/subscribe)?

**2)** 🍻 **Read with your friends** — Refactoring lives thanks to word of mouth. Share the article with your with someone who would like it, and **get a free membership** through the new [referral program](https://refactoring.fm/p/referral).

Read with your friends 🍻

[https://refactoring.fm/leaderboard](https://refactoring.fm/leaderboard)

I wish you a great week! ☀️

Luca
