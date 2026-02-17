---
aliases:
  - "Monday #87"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-monday-idea|Publish Monday Idea]]"
Status: Published
"👓 Status": Not started
"Created time": "2024-04-18T15:09:00.000Z"
Date: 2024-01-22
"Has Notes":
  - "[[evergreen/use-llms-for-two-main-things|Use LLMs for two main things]]"
  - "[[evergreen/systems-goals|Systems > Goals]]"
Tags:
  - Monday
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: c6decac2-c7a2-4aba-b012-5a16825674a2
---

# Monday #87

*Hey, *[*Luca*](https://twitter.com/lucaronin)* here! Welcome to the ****Monday Ideas ***💡

*Every Monday I send you an email like this with ****3 short ideas**** about making great software, working with humans, and personal growth.*

*Paid members also receive a long-form, original essay on Thursday, like the last one:*

[https://refactoring.fm/p/how-to-plan-and-execute-projects](https://refactoring.fm/p/how-to-plan-and-execute-projects)

*To receive all the full articles and support Refactoring, consider joining 1400+ engineers and get the paid membership!*

Get full access to Refactoring ✨

[https://refactoring.substack.com/subscribe](https://refactoring.substack.com/subscribe)?

*p.s. learn more about the *[*benefits of the paid plan here*](http://refactoring.fm/about)*.*

---

### 🗳️ The State of Engineering Productivity

Before we dive into this week’s ideas, I have a quick ask! 🙏

Together with the guys at [Hatica](https://hatica.io/), **I am conducting a survey** about what makes engineering teams productive: practices, usage of metrics, tools, etc.

The goal is to **gather insights** 🔍 and write a thorough newsletter edition about engineering productivity that will go out to all subscribers.

If you want to help me out on this, you can **fill out the survey below** 👇 it takes less than 5 mins.

[Fill out the survey in 5 mins! 🗳️](https://kdblhxqqqe6.typeform.com/to/JjqsJylz)

Thank you, it means a lot!

### 1) ⚖️ Balancing your engineering work

Speaking of metrics and productivity, I am a fan of measuring where your engineering time is spent, and allocate it intentionally.

Unless you already have a good way of doing this, I recommend starting with the **Balance Framework**, which defines four main types of engineering investments:

1. 🩺 **KTLO** — mandatory maintenance that literally keeps the lights on.

1. 🔨 **New things** — work towards business goals, like new products or features.

1. 🔧 **Improvements** — work to improve existing features, including performance, reliability, and security.

1. ⚙️** Productivity** — improvements to the developer experience. This may also affect operations and other departments’ productivity.

![image](../assets/174bdf02815c801c.png)

Categorizing your work helps you have conversations based on grounded evidence, and build a sustainable work balance.

E.g. are you spending more than 30% on KTLO? You can bring up the data, discuss if there is some debt that slows the team down, and plan actions to improve.

I wrote a full piece about balancing your engineering investment about one year ago, you can find it below:

[https://refactoring.fm/p/engineering-investments](https://refactoring.fm/p/engineering-investments) 

---

### 2) 🎯 Systems > Goals

In November we read Atomic Habits, by James Clear, in the community [book club](https://refactoring.fm/book-club).

One idea that stuck with me from the book is how **systems **in your life are more important than **goals**.

In fact, goals have three problems:

- ⏱️ **Goals are temporary **—** **what happens when the goal is achieved? Goals are about *winning*, but once you win there may be nothing left to do. 

- ⛰️ **Goals are aspirational **— they do not tell you how to get there: that’s what you need systems for.

- ☀️ **Goals delay happiness** — sacrificing something today to get something tomorrow is often a smart play, but there is a catch. It is risky to do something you don’t like for a long time just because of some ideal reward at the end. The outcome you wish for might 1) never materialize, or 2) not be as good as you expected.

There is a great quote in the book that says:

> *People don’t rise to the level of their goals: they fall to the level of their systems*. 

To me, this is similar to another favorite of mine: *play games you enjoy playing, rather than only winning*, which I wrote about in a previous edition 👇

[https://refactoring.fm/p/expectations-vs-happiness](https://refactoring.fm/p/expectations-vs-happiness)

So, as an example, rather than thinking that you should “lose weight” and focus on a target weight, think about what it means to be a healthy, active person. What does this *version* of you look like? What do they do every day? 

Visualize this person and their life, and make it happen with habits.

That’s what James Clear wants you to do, rather than setting your *target weight*.

Still, goals *do* have their place. When you set to go in some direction, you *need* KPIs to check that you are on track. You can place *stepping stones* along the way. But know that goals only *mark *progress, they do not *make* it.

You can find the full review of Atomic Habits here:

[https://refactoring.fm/p/atomic-habits](https://refactoring.fm/p/atomic-habits)

---

### 3) 🤖 What should you use LLMs for?

What should you use LLMs for? This is a tough question to answer, because LLMs can tackle pretty much anything, but with inconsistent quality.

Sometimes they look incredibly smart, other times they do poorly. About this, they behave similarly to… humans.

In fact, I have found that a quick heuristic for good LLMs use cases is to stick with tasks that would otherwise **require humans**. Conversely, tasks that you would automate with code are probably still best addressed with code.

This is true for other AI systems as well. Even though LLMs can seemingly do it all, plenty of common ML use cases, like classification or recommendation, are *still* better served by traditional architectures, which are faster and cheaper.

In fact, for any problem you may have, LLMs are possibly your **slowest and most expensive** option available, only second to people. This leads to a general rule of thumb — LLMs are:

- **Expensive and slow** — if the alternative is code.

- **Cheap and fast** — if the alternative is people.

In other words, code is extremely fast, cheap, and predictable, while humans are extremely slow, expensive, and unpredictable. LLMs sit kind of in between.

![image](../assets/961d1a4daacf4667.png)

So, I have found that the best use cases for LLMs usually belong to two categories: **processing information**, and **drafting content 👇**

#### 1) Process / transform information

LLMs seemingly *understand* content, which makes them good at all kinds of tasks where you need to take some piece of information and transform it into something else.

A few examples:

- 📌 **Summarization** — books, documents, [youtube videos](https://eightify.app/), [meetings](https://tldv.io/), you name it. This literally benefits everyone, as we all work with content in a way or another. In many cases, note taking has become something of the past.

- 🔖 **Data entry** — LLMs can easily take emails, chat threads, and other unstructured information, and transform them into structured attributes. Use cases for this are incredibly common: chances are you can find plenty of manual [slot filling](https://clover.studio/2023/10/04/implement-slot-filling-chatbot-with-llama2-and-chatgpt/) / data entry tasks in your company, for example in sales and customer support.

- ❓ **Asking questions** — being able to ask questions about some content, without needing to go through it all. Imagine LLMs embedded into your docs workspace and being able to retrieve any info without needing to know where a doc lives. This is already possible [on Notion](https://www.notion.so/product/ai).

#### 2) Draft content to be created by humans

LLMs are also useful for *drafting* a lot of what we would otherwise create ourselves. Think of code, emails, or docs.

Whenever you are creating content on a regular basis, chances are you can create good templates or instructions (like you would do for humans), and let LLMs use them to generate drafts.

I have seen teams successfully using this for sales emails, design docs, meeting notes, and more.

I say *draft* for two reasons:

- **✅ Quality** — content produced by LLMs may be good enough to save you time vs starting from scratch, but not good enough to be published as-is.

- **📊 Consistency** — LLMs are not 100% reliable at following instructions. I have rarely found workflows *entirely* automated with LLMs, without supervision.

So, once you find a good use case, how do you work with LLMs at a tech level? This is not as simple as in buy vs build, because these systems can be tailored to your needs in different ways, based on what you need to do.

I have covered the most popular options with pros and cons, in a recent article 👇

[https://refactoring.fm/p/how-to-integrate-llms](https://refactoring.fm/p/how-to-integrate-llms)

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
