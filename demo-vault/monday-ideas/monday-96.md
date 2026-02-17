---
aliases:
  - "Monday #96"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-monday-idea|Publish Monday Idea]]"
Status: Published
"👓 Status": Not started
"Created time": "2024-04-18T15:09:00.000Z"
Date: 2024-03-25
"Has Notes":
  - "[[evergreen/eisenhower-decision-matrix|Eisenhower Decision Matrix]]"
  - "[[evergreen/scoping-from-appetite|Scoping from appetite]]"
  - "[[evergreen/self-hosting-llms-vs-apis|Self-hosting LLMs vs APIs]]"
Tags:
  - Monday
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 20bddf3d-ecb8-4e5a-90a0-4a2215e411b7
---

# Monday #96

*Hey, Luca here! Welcome to a new edition of the* ***Monday Ideas*** 💡

*Every Monday I send you an email like this with three short ideas about making good software, working with humans, and personal growth. You will also receive a long-form* ***original essay*** **🧵** *every Wednesday, and a* ***podcast episode*** **🎙️** *every Friday.*

*Here are the latest editions you may have missed:*

### 1) 🤖 Self-hosting LLMs vs using APIs

One of the most frequent questions I hear about integrating LLMs is whether to go the OpenAI route (or the likes), using their APIs, or hosting an open-source system yourself (e.g. Llama).

APIs of course win the *ease of use* and *time to market* arguments, but what about other factors?

A few months ago I surveyed various people in the AI engineering space, and here is the consensus:

#### 1) Cost & Skills

Counterintuitively, **self-hosting LLMs doesn’t typically save you money** over using APIs. OpenAI’s pricing is extremely aggressive, and their team is world-class at optimizing the use of hardware.

For example, hosting a Llama node on a suitable AWS instance would likely cost you around **$8-10 / hour**, which means it would lose money on anything but high-load workflows.

And even in high-load cases, the cost upside is unclear when you factor in maintenance, which requires strong technical expertise. If you don’t have such expertise in-house, self-hosting is out of the question.

#### 2) Privacy & Security

Solid arguments for self-hosting are, instead, **privacy and security** concerns.

While you can opt out of letting OpenAI use your conversations’ data for future training, I completely understand companies who are uneasy at *firehosing* vast amounts of private information (possibly including their customers’) to an aggressive startup.

So, if privacy matters to you, self-hosting an LLM may be worth the hassle.

You can find the full piece about how to integrate LLMs into tech stack below 👇

[https://refactoring.fm/p/how-to-integrate-llms](https://refactoring.fm/p/how-to-integrate-llms) 

---

### 2) ➕ Eisenhower Decision Matrix

The Eisenhower Decision Matrix is one of the most famous management frameworks out there. It helps you prioritize tasks based on *urgency* and *importance*.

![image](../assets/ea66f5215a2c44c7.jpg)

The matrix is divided into four quadrants:

1. ✅** Urgent and Important → Do First** — tasks that need immediate attention and contribute significantly to long-term goals. E.g. fixing a critical bug that's affecting a large number of users.

1. ⏱️** Important but Not Urgent → Schedule** — tasks that are important for long-term goals but do not need immediate attention. E.g. planning for a new feature.

1. 🔀** Urgent but Not Important → Delegate** — tasks that need to be done quickly but do not contribute significantly to long-term goals. They can be delegated to others. E.g. routine administrative tasks, or responding to non-critical emails.

1. ❌ **Not Urgent and Not Important → Don't Do** — tasks that do not contribute to long-term goals and do not need immediate attention, so they can be eliminated. Examples could be attending non-essential meetings or browsing the internet aimlessly.

The Eisenhower matrix is a fantastic starting point to reflect on how you spend your time, but it is also pretty basic. Here are a couple of doubts:

1. **Urgent tasks** are often hard to delegate. Delegation is a long-term play; in the short-term it may require more time/effort than doing the thing yourself.

1. **Non-important tasks** are ok, but they are often trivial, so if you only delegate those, you are limiting people’s growth. It doesn’t help that non-important tasks are also often *small*, which makes the ROI of delegation dubious.

I wrote a full piece about delegation where I try to give the matrix more nuance and make it more useful for daily work 👇

[https://refactoring.fm/p/how-to-delegate](https://refactoring.fm/p/how-to-delegate)

### 3) 🪑 Scope projects like IKEA

Over time I have realized that when somebody — a product person, a CEO, whoever — comes up with a product idea, they probably have a **rough timeframe** already in the back of their mind.

They don’t think their idea is worth at *any* cost — they think it would be e.g. a nice experiment if delivered in three months. Three months isn’t just a time here, it is a cost: it is three months multiplied by the salaries of the people on the team.

**Projects only make sense if they fit a budget** — which the Basecamp guys call [*appetite*](https://basecamp.com/shapeup/1.2-chapter-03#setting-the-appetite). The appetite for a project largely exists upfront, and is inseparable from the idea itself.

I have found that most issues with estimates, negotiations, and fighting between stakeholders, arise from such an appetite not being *visible* to the team, and not being treated for what it is: a *constraint*.

Famously, **IKEA designs furniture **[**by creating the price tag upfront**](https://www.ikea.com/gb/en/cat/lowest-price/). They don’t design a chair first and ask manufacture what it would cost later. Instead, they know e.g. that there aren’t many good office chairs for <€200, and that there are people in the market for those. So they ask: what can we ship at that price point? What can we include? What can we give up?

You can treat software projects like IKEA chairs. How can we solve this problem in one month? How can we design a solution that works within this tight scope?

Now, for **small-ish initiatives** that take up to a few weeks, I have found that getting this conversation right is 80% of the work. You align people’s expectations, make constraints visible, figure out a reasonable scope, and go for it.

For **large projects**, instead, things are trickier.

Appetite might be unclear. Sure, if we are right about the need/demand for this, a year of development might be well spent, but 1) we *don’t know* if we are right, and 2) is a full year really needed?

I wrote a full guide about planning and executing projects earlier this year 👇

[https://refactoring.fm/p/how-to-plan-and-execute-projects](https://refactoring.fm/p/how-to-plan-and-execute-projects)

---

And that’s it for today! If you are finding this newsletter valuable, consider doing any of these:

**1) ✉️ Subscribe to the newsletter** — if you aren’t already, consider becoming a paid subscriber. 1500+ engineers and managers have joined already! Learn more about the [benefits of the paid plan here](http://refactoring.fm/about).

Get full access to Refactoring ✨

[https://refactoring.substack.com/subscribe](https://refactoring.substack.com/subscribe)?

**2)** 🍻 **Read with your friends** — Refactoring lives thanks to word of mouth. Share the article with your with someone who would like it, and **get a free membership** through the new [referral program](https://refactoring.fm/p/referral).

Read with your friends 🍻

[https://refactoring.fm/leaderboard](https://refactoring.fm/leaderboard)

I wish you a great week! ☀️

Luca
