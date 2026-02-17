---
aliases:
  - "Monday #111"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-monday-idea|Publish Monday Idea]]"
Status: Published
"👓 Status": Not started
"Created time": "2024-06-26T09:05:00.000Z"
Date: 2024-07-08
"Has Notes":
  - "[[evergreen/high-leverage-time-management|High-leverage time management]]"
  - "[[evergreen/hierarchies-are-useful-to-scale-comms|Hierarchies are useful to scale comms]]"
  - "[[evergreen/hire-because-of-bottlenecks|Hire because of bottlenecks]]"
Tags:
  - Monday
  - Free
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: aefffc6b-b56a-4b6e-a96c-b434e1560ad5
---

# Monday #111

### Bright Data

### 1) 🏗️ Hierarchy actually *helps* communication

As long as your team is small, there isn’t much need for a formal organization — 5 to 10 people can work pretty well without much structure.

The main problem, when teams grow larger, is communication. Large teams have a hard time doing things like:

- Keeping people on the same page

- Coordinating and allocating resources

- Making good, participated decisions

When you grow your team from 5 people to, say, 15 or 20, it seems that these problems get worse — at first gradually, and then suddenly.

But why?

As by [Metcalfe’s Law](https://en.wikipedia.org/wiki/Metcalfe%27s_law), the complexity of communication is proportional to the *square* of the number of users involved. So, while people grow linearly, complexity grows geometrically 👇

![image](../assets/1c1bdf02815c80b7.png)

To tame communication complexity, companies usually introduce **hierarchies**. Hierarchies have several advantages:

- They provide clear communication paths, ensuring **alignment** is obtained across the organization.

- They reduce the number of *lines* each person has to manage, allowing the company to **scale**.

- They provide a simple way for **making decisions**, by assigning responsibility to people up in the hierarchy.

Same 7 people, different configurations:

![image](../assets/ac348de876774481.png)

However, they also bring drawbacks:

- **Overhead** — communication has a longer way to travel to a destination, which makes you slower. Longer paths also create all kinds of “work’s work”, like traffic controlling, managing up, presentations, and more.

- **Inflexibility** — once in place, it is hard to reconfigure roles and processes. This in turn reduces agility, resilience to turnover, and velocity, too.

There exist companies who have successfully scaled without introducing hierarchies.

I wrote a two-part series about them 👇

[https://refactoring.fm/p/unusual-teams-1](https://refactoring.fm/p/unusual-teams-1)

---

### 2) 🛑 Hire because of bottlenecks 

When it comes to hiring, I tend to be extremely conservative. 

So, I believe you should mostly hire because of **bottlenecks**, rather than **opportunities.**

Just like with funding—you should only raise money when you know exactly how you would spend it—you should only hire people when you are clearly bottlenecked on something, rather than to chase new things.

For example, let’s say your product relies on integrations with external APIs, and the more integrations you build the more customers your sales people are going to win. It is a **proven process** where higher development velocity brings more business, so you may go for it with confidence.

Now, let’s make a different example — your product relies on sales and word of mouth, and you think you should now invest on SEO because it looks promising: decent volume and low-competition.

This is not a bottleneck, this is a **new opportunity** that may or may not play out the way you think. My preferred way of chasing it would probably be:

- Learn the basic skills yourself (your existing team).

- Prototype the work and get some initial results.

- Get to the point where the **opportunity turns into a bottleneck** — that is, you validate the value that would be brought by a specialist.

- Hire a specialist to make a 10x better work.

You may also work with an agency / consultants in the initial stages to bring in expertise while keeping risk low.

![image](../assets/369d3d00ef914f57.webp)

Overall your final decision of hiring somebody should be a **double no-brainer**:

- **Position** — no-brainer to hire for that position.

- **Candidate** — no-brainer to hire that candidate for that position.

I wrote a full guide about the signs (and anti-signs) that you should hire engineers and/or managers 👇

[https://refactoring.fm/p/when-should-you-hire](https://refactoring.fm/p/when-should-you-hire)

---

### 3) ⏱️ High-leverage time management

You need to be intentional, at a company level, about how people spend their time, and apply what I call **high-leverage time management**.

Here is what you should pay attention to:

#### Minimize waiting ✋

Minimize the time people spend waiting for others to do stuff.

1. More waiting leads to more context switch — people move to other tasks in the meantime

1. More context switch leads to more work in progress — which is detrimental to quality, productivity, and morale.

But why do people wait for others in the first place? In my experience, it’s mostly two things:

- 🤝 **Collaboration **— things that need contribution from multiple people, like a design doc.

- **🏅 Approvals **— things that need to be reviewed and *signed off *by somebody, like a PR.

To reduce waitings, you can try two things:

- **Make high-bandwidth activities *****sync***** **— for creative tasks that require a lot of back and forth, consider doing them *synchronously* in a meeting, instead of passing them around on Slack or a doc. E.g. create that design doc all together with your team, or do pair programming on that thorny issue.

- **Switch from an *****approval***** workflow, to a *****revert***** one** — default to trust your co-workers to go ahead with their decisions, and review only *after* the fact, not to block them. This does wonders for both productivity and accountability. For example, you can do so with code reviews: see the [ship/show/ask](https://refactoring.fm/i/45862551/consider-the-ship-show-ask-framework).

#### Meetings are short & few 💬

Meetings are the *easy default* to get things done, but easily turn into a *low-leverage* way of spending your time.

I have written about meetings many times, including a full guide about how to reduce them: 

[https://refactoring.fm/p/how-to-remove-meetings](https://refactoring.fm/p/how-to-remove-meetings)

A good rule of thumb for when to use a meeting is to follow the ☕ **CUP Rule**. Use meetings when the matter is:

- **Complex** — we need to brainstorm and figure this out together.

- **Personal** — improve bonding, 1:1s

- **Urgent** — there is an incident happening *right now*

Truth is very few things happen *regularly* that meet any of these criteria. So, be especially suspicious of recurring meetings.

#### You apply continuous delegation 🔀

An investor once told me that as a founder I had to continuously replace myself. 

Once I understood how to do something, my job was to delegate or automate such work.

I have found this to be a good mindset for everybody, not just founders. You can ask yourself continuously:

1. **Can I remove this? **—** **Is this really needed?** **You would be surprised by how much work can be safely *removed* and not be replaced by anything. This should always be the first option. 

1. **Can I automate this? **— Automate aggressively any manual work that is not high-leverage. These days, you have plenty of ways to do so: chatOps, internal tools, and workflows are easy to build even without code. 

1. **Can I delegate this? **— Are you the best person to do this?** **Sometimes, what looks like a chore for you, is an opportunity for a younger co-worker to prove themselves. 

Also, the order matters. No work that can be remove should be automated, and no work that can be automated should be delegated.

High-leverage time management was part of a wider *checklist* I wrote for startup teams. You can find it below 👇

[https://refactoring.fm/p/the-startup-healthcheck](https://refactoring.fm/p/the-startup-healthcheck)

---

And that’s it for today! If you are finding this newsletter valuable, consider doing any of these:

**1) **🔒** Subscribe to the paid version** — if you aren’t already, consider becoming a paid subscriber. 1500+ engineers and managers have joined already! Learn more about the [benefits of the paid plan here](http://refactoring.fm/about).

Get full access to Refactoring ✨

[https://refactoring.substack.com/subscribe](https://refactoring.substack.com/subscribe)?

**2)** 🍻 **Read with your friends** — Refactoring lives thanks to word of mouth. Share the article with your with someone who would like it, and **get a free membership** through the new [referral program](https://refactoring.fm/p/referral).

Read with your friends 🍻

[https://refactoring.fm/leaderboard](https://refactoring.fm/leaderboard)

I wish you a great week! ☀️

Luca
