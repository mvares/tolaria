---
aliases:
  - "Monday #81"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-monday-idea|Publish Monday Idea]]"
Status: Published
"👓 Status": Not started
"Created time": "2024-04-18T15:09:00.000Z"
Date: 2023-12-11
"Has Notes":
  - "[[evergreen/the-three-layers-of-change|The Three Layers of Change]]"
  - "[[evergreen/break-down-projects-into-stepping-stones|Break down projects into stepping stones]]"
Tags:
  - Monday
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: e9840bb8-fe21-42cf-826d-7c00f0ef8a97
---

# Monday #81

*Hey, *[*Luca*](https://twitter.com/lucaronin)* here! Welcome to the ****Monday Ideas ***💡

*Every Monday I send you an email like this with ****3 short ideas**** about making great software, working with humans, and personal growth.*

*Paid members also receive a long-form, original essay on Thursday, like the last one:*

[https://refactoring.fm/p/culture](https://refactoring.fm/p/culture)

*To receive all the full articles and support Refactoring, consider joining 1400+ engineers and get the paid membership!*

Get full access to Refactoring ✨

[https://refactoring.substack.com/subscribe](https://refactoring.substack.com/subscribe)?

*p.s. learn more about the *[*benefits of the paid plan here*](http://refactoring.fm/about)*.*

---

### 1) 🔺 The Three Layers of Change

One month ago we reviewed [Atomic Habits](https://www.goodreads.com/en/book/show/40121378), by James Clear, in the community [book club](https://refactoring.fm/book-club).

One of the most memorable ideas from the book is thinking about change as being made of three layers:

1. 🌟 **Identity** — the person you want to become. It is the improved version of you that you look forward to, which unlocks the *why* you are doing this.

1. 🔄 **Processes** — your systems, or habits, to bring you closer to your improved identity, and make the outcomes happen.

1. 🏆 **Outcomes** — the specific things you want to *achieve*. It can only work in combination with the other two.

The author argues that the strongest habits are **identity-based**, rather than **outcome-based**.

Outcomes in fact, like goals, are temporary — what happens after the goal is achieved? — while identity is forever. Outcome-based habits tend to be weaker, while a strong identity is what allows you to play *infinite games* and make things stick.

![image](../assets/e1e562f4c5e34d87.jpg)

As an example, rather than thinking that you should “lose weight” and focus on a target weight, think about what it means to be a healthy, active person. What does this *version* of you look like? What do they do every day? 

Visualize this person and their life, and make it happen with habits.

You can find the full book review in this previous Refactoring edition 👇

[https://refactoring.fm/p/atomic-habits](https://refactoring.fm/p/atomic-habits)

---

### 2) 🗿 Stepping Stones

---

In the latest edition [about engineering culture](https://refactoring.fm/p/culture) I briefly mentioned my [chat with James Cowling](https://refactoring.fm/p/james-cowling), former Principal Engineer at Dropbox, and his way of handling big projects.

When there is no linear path from path to finish, James likes to break down work into **stepping stones**. Stepping stones are not your generic *milestones* — they need to have these qualities:

- 📈 **Incremental** — you can continue building on top of each one.

- 🏆 **Valuable** — they are useful. They solve the problem, even if in an inefficient / expensive / precarious way.

- 🔍 **Instructive **— they make you *learn* more about the problem space, so you can eliminate some of the *fog of war* and design better solutions in the next iterations.

Let’s make a practical example of the Dropbox storage system that James designed. The end game for this might look like a giant, multi-exabyte system deployed in data centers around the US. But, put like this, 1) it would cost a huge sum of money, and 2) it would involve daunting technical challenges, like designing a file system and its hardware architecture.

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

And this will happen. 

If you do your job right, you will definitely drop projects before the supposed end. In fact, engineers often think that systems need to be *more* optimal than they really need to be. A surprising upside of good stepping stones is that they often make you do *less *work, because you discover you didn’t really need part of it.

You can find the full chat with James here 👇

[https://refactoring.fm/p/james-cowling](https://refactoring.fm/p/james-cowling)

### 3) ☁️ Beware superficial cloud native

Cloud providers today have a strong influence on how applications are designed.

That’s because, over time, they have gradually expanded from simply *renting servers* to people, to running *managed services* that you can use like building blocks for composing your software.

Since these services are well-designed in isolation, you may be fooled into thinking that by taking many of them and combining them you will *naturally *end up with a good design.

This is wrong, of course, and lies at the core of many mistakes I see people making with trendy patterns like microservices, serverless, and more.

Cloud services provide real, tangible benefits, but they should *support* your system design — which is largely independent from them — rather than the other way around.

You can find more ideas about cloud, monoliths and microservices, in these previous articles:

[https://refactoring.fm/p/monoliths-vs-microservices](https://refactoring.fm/p/monoliths-vs-microservices)

[https://refactoring.fm/p/cloud-vs-on-premise](https://refactoring.fm/p/cloud-vs-on-premise)

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
