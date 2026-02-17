---
aliases:
  - "Monday #143"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-monday-idea|Publish Monday Idea]]"
Status: Published
"👓 Status": Not started
"Created time": "2025-02-11T14:03:00.000Z"
Date: 2025-02-17
"Has Notes":
  - "[[evergreen/the-four-domains-of-trust|The Four Domains of Trust]]"
  - "[[evergreen/how-to-get-hired-as-an-em-on-a-different-tech-stack|How to get hired as an EM on a different tech stack]]"
  - "[[evergreen/prioritize-bugs-by-severity-and-priority|Prioritize bugs by severity and priority]]"
Tags:
  - Monday
  - Free
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 197bdf02-815c-80df-87d1-e8349039fe63
---

# Monday #143

### 1) 💼 Can you get hired as an EM on a “foreign” tech stack?

In a recent mastermind session, an experienced EM told us how, in their role, they are also involved on the technical side of things, but the team operates on a very *niche *tech stack.

Such stack may be not relevant in other jobs — in fact, when interviewing, the lack of hands-on experience with more widespread tech seems to be a blocker.

![Screenshot from a recent mastermind session in the community!](../assets/197bdf02815c80c7.jpeg)

So, what to do? Here is the advice from the mastermind:

#### **Focus on language-agnostic skills **🧠

The best tech skills are either language-agnostic or totally transferrable between different stacks, system design being the #1 of these. The way you think about scalability, coupling vs cohesion, domain driven design, and more, are timeless. 

Also, I have found that having *deep* knowledge of some stack/framework (e.g Ruby on Rails), including internals, quirks, and tradeoffs, makes it surprisingly easier to get just as deep on other frameworks as well. That’s because different frameworks need to answer many of the same questions, and even if the answers *vary*, just knowing *what* these questions are puts you way ahead of people who are starting from scratch.

So, during interviews, you may acknowledge your lack of experience in a given stack, but highlight your ability to pick things up quickly, thanks to your wider engineering experience.

#### **Practice your interviewing skills **💬

Interviewing is a skill in itself — which is kind of sad if you ask me, but it is what it is 🤷‍♂️

So, practice your interviews. Look for common questions, prepare the right stories about your past experiences, and have good answers ready for your shortcomings.

#### Apply a lot* *🗳️

Finally, recruiting is a deeply imperfect process, and being rejected doesn’t mean a lot. It’s a numbers game: you should do *tens* of applications, not just 5 or 6. 

The job market is way tougher than it used to be, so you should take heart from the fact that you are getting interviews at all, and accept that some luck is required.

So, learn from rejections whenever possible, don’t get discouraged, and keep going. You got this 💪

More lessons learned from our masterminds below!

[https://refactoring.fm/p/lessons-from-the-mastermind-sessions](https://refactoring.fm/p/lessons-from-the-mastermind-sessions)

---

### 2) 🤝 The Four Domains of Trust

I am a fan of [The Thin Book of Trust](https://www.goodreads.com/book/show/7013813-the-thin-book-of-trust-an-essential-primer-for-building-trust-at-work), in which Charles Feltman breaks trust down into four domains: 

1. **🎭 Sincerity **— you are honest and transparent, even when it’s uncomfortable. This includes admitting mistakes early, being upfront with challenges, and sharing both good and bad news, without sugar-coating the latter.

1. **⏰ Reliability **— this is about consistency and following through. You do what you say you'll do, you set realistic expectations, and communicate proactively through regular update habits. More on this later in the *updates* section.

1. **💝 Care **— you have their best interests in mind. This means understanding their goals and challenges, being proactive in helping them succeed, and showing empathy when things get tough.

1. 🎓 **Competence **— finally, you deliver results. This goes beyond technical skills: it's about delivering business value, learning and growing from feedback, and understanding the big picture.

What I like about this framework is that it is extremely simple and it gives you concrete areas to work on. You can ask yourself: how am I doing in each of these? How can I do better?

![image](../assets/197bdf02815c80ae.png)

Still, trust is alone not enough for good work relationships — I wrote more about it in this recent article about managing up 👇

---

### 3) 🐛 Prioritize bugs by severity + priority

How do you decide what bugs to address first? This is trickier than it seems, as you may have different stakeholders and different opinions.

A good way to get to a consensus is to consider two separate values of importance for a bug: **priority **and **severity**.

- **Priority** — is *how bad this is for business*. How much revenues are we losing? How bad is the experience for customers? It should be assessed by the PM, with the help of customer support in case of user-reported defects.

- **Severity **— is *how badly broken the feature and software are*. Is this still usable? Why is this happening? Severity is assessed by QA and Engineers, who can ignore how *relevant* the broken feature is, to focus on how much it is individually impacted by the bug. Engineers can also evaluate whether the issue is symptom of a larger disease, and things are more broken under the hood than it seems.

Once you have set severity and priority values, you can simply fix bugs in this order:

1. **High Priority + High Severity** —  the login is broken and users can't access the tool.

1. **High Priority + Low Severity** — terms & conditions are not visible when users make the payment.

1. **Low Priority + High Severity **— the checkout doesn't work with some niche combination of device + browser. 

1. **Low Priority + Low Severity **— border radius of the button doesn't match the design system.

Basically, priority wins over severity, with the latter being considered when the former is equal.

![image](../assets/197bdf02815c8054.png)

This is powerful for two reasons:

- **Separation of concerns:** it avoids the negotiation between the business and technical side of the team, because each side gives its own value separately.

- **Clear sorting:** It provides a clear rule for deciding in which order to fix bugs — one that doesn't need to be rediscussed every time.

Does the process above create the perfect sorting? No. But it should be *good enough* as long as you are *fast *at fixing bugs.

The faster you are at fixing, the less important the order is.

More on fixing bugs below!

[https://refactoring.fm/p/how-to-prioritize-bugs-](https://refactoring.fm/p/how-to-prioritize-bugs-)

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
