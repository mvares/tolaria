---
aliases:
  - "Monday #53"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-monday-idea|Publish Monday Idea]]"
Status: Published
"👓 Status": Not started
"Created time": "2024-04-18T15:09:00.000Z"
Date: 2023-05-29
"Has Notes":
  - "[[evergreen/investment-metrics-are-extremely-useful|Investment Metrics are extremely useful]]"
  - "[[evergreen/prioritize-bugs-by-severity-and-priority|Prioritize bugs by severity and priority]]"
  - "[[evergreen/avoid-the-monkey-on-your-back|Avoid the monkey on your back]]"
Tags:
  - Monday
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 5de0bb90-54db-42c3-a401-b3f2ce94071a
---

# Monday #53

*Hey, *[*Luca*](https://twitter.com/lucaronin)* here! welcome to the ****Monday 3-2-1 ****✨*

*Every Monday I will send you an email like this with ****3 short ideas**** about engineering management, technical strategy, and good hiring.*

*You will also receive the regular long-form one on Thursday, like the last one:*

- [**Tech Leadership across the Startup Lifecycle**](https://refactoring.fm/p/tech-leadership-for-startups)** 👑**

*To receive all the full articles and support Refactoring, consider subscribing if you haven’t already!*

Get full access ✨

[https://refactoring.substack.com/subscribe](https://refactoring.substack.com/subscribe)?

*p.s. you can learn more about the *[*benefits of the paid plan here*](http://refactoring.fm/about)*.*

---

![image](../assets/a02acfb71d824c08.png)

---

### 🌊 Wave **• Your tailored coach for infinite growth (30% off **🎁**)**

This week I am promoting Wave, because I love the way they are exploring coaching and AI 👇

Wave provides a **tailored coaching experience** to take your career to the next level and overcome any kind of challenges you are facing at work, like:

- Building self-confidence in your role

- Having the success and impact you desire

- Improving your productivity and organization 

- Rethinking the way you lead, inspire, communicate, and build trust

![image](../assets/b31464dc789a4761.gif)

Wave lets you tap into the collective brainpower of multiple **coaching experts empowered by AI**, and take your leadership skills to the next level 🚀

It is used by founders, managers, and leaders from companies like Amazon, Stripe, Google, and Strapi.

Learn more about Wave ✨

[https://www.wave.ai/?utm_source=newsletter&utm_medium=sponsor&utm_campaign=refactoring_may_2023](https://www.wave.ai/?utm_source=newsletter&utm_medium=sponsor&utm_campaign=refactoring_may_2023)

As a Refactoring reader, you get 30% discount on the 3-month plan by using the *GROWWITHREFACTORING* discount code. And the first session is free!

 

### 1) 📊 Investment metrics are underrated

---

Investment metrics are for figuring out how you spend your time as a team. 

For example, how much time goes into maintenance vs new features? How much on new features vs small improvements? 

In my experience, tracking your engineering investment has incredible ROI. It creates *alignment* with the business, builds trust, and counters natural biases your team may have towards specific types of work. 

In fact, based on their culture, most teams naturally skew towards some modes of work. For example: 

- 🏭 **Feature factories** — always pumping out new stuff. 

- 📊 **Optimizers*** — *focus on short-term and small improvements, rather than big initiatives.

- 🏗️ **Perfectionists** — engineering-heavy teams who overly focus on refactoring.

The best way to counter this is to start *visualizing* where your time goes, and adjust.

About this, I am a fan of the *balance framework*, which divides work into four main areas:

1. 🩺 **KTLO** — mandatory maintenance to *Keeps The Lights On*.

1. 🔨 **New things** — work towards business goals, like new products or features.

1. 🔧 **Improvements** — work to improve existing features, including performance, reliability, and security.

1. ⚙️ **Productivity** — improvements to the developer experience. This may also affect operations and other departments’ productivity.

![image](../assets/decdb5e3ba584405.jpeg)

This helps you have conversations based on grounded evidence, and build a sustainable work balance. E.g. are you spending more than 30% on KTLO? You can bring up the data, discuss if there is some debt that slows the team down, and plan actions to improve.

![Tracking investment balance on Swarmia.](../assets/66167dbd28c84bf8.png)

Most engineering metrics tools today provide ways to track your investment (will provide a list at the end of the post).

You can find more ideas about how to use engineering metrics in this previous Refactoring article 👇

[https://refactoring.fm/p/how-to-get-started-with-engineering](https://refactoring.fm/p/how-to-get-started-with-engineering)

### 2) 🐛 Prioritize bugs by severity and priority

---

Bug fixing is not exactly everyone's favorite engineering activity.

It's a tricky process that requires coordination between several stakeholders — PMs, Customer Support, QA, and Engineers.

A good way to involve all stakeholders in prioritization, while also keeping conflicts low, is to consider two separate values of importance for a bug: **priority **and **severity**.

#### 🏆 Priority

Priority is **how bad this is for business**. How much revenues are we losing? How bad is the experience for customers?

Priority can be assessed by the **PM**, with the help of **Customer Support** in case of user-reported defects.

#### 🔨 Severity

Severity is **how badly broken the feature and software are**. Is this feature still usable? Why is this happening?

Severity is assessed by **QA** and **Engineers**, who can ignore how *relevant* the broken feature is, to focus on how much it is individually impacted by the bug.

Engineers can also evaluate whether the issue is symptom of a larger disease, and things are more broken under the hood than it seems.

#### 🔄 Process

Once you have set severity and priority values, you can simply fix bugs in this order:

1. 🏆 **High Priority + High Severity** —  e.g. the login is broken and users can't access the tool.

1. 🥇 **High Priority + Low Severity** — e.g. terms & conditions are not visible anymore before users make the payment.

1. 🥈 **Low Priority + High Severity **—  e.g. the checkout doesn't work with some niche combination of device + browser. 

1. 🥉 **Low Priority + Low Severity **— e.g. border radius of the button doesn't match the design system.

Basically, priority wins over severity, with the latter being considered when the former is equal.

![Priority, severity, and the order in which you should address bugs ](../assets/dc9c55a978304213.png)

This framework is powerful for two reasons:

- **Separation of concerns:** it avoids the negotiation between the business and technical side of the team, because each side gives its own value separately.

- **Clear sorting:** It provides a clear rule for deciding in which order to fix bugs — one that doesn't need to be rediscussed every time.

### 3) 🐒 Avoid the monkey on your back

---

As a manager, having the *monkey on your back* is a metaphor for having the initiative on yourself. You are the one who has to do the next step — the ball is in your court.

For any activity, you should strive to **minimize the time** the monkey is on you, and figure out how to return them asap to your reports.

![image](../assets/3ef6c65ea5bc460c.webp)

I love this metaphor — I explore this and more ideas about delegation in a previous refactoring article 👇

[https://refactoring.fm/p/how-to-delegate](https://refactoring.fm/p/how-to-delegate)

---

And that’s it for today! If you are finding this newsletter valuable, consider doing any of these:

**1) ✉️ Subscribe to the newsletter** — if you aren’t already, consider becoming a paid subscriber. You can learn more about the [benefits of the paid plan here](http://refactoring.fm/about).

Get full access ✨

[https://refactoring.substack.com/subscribe](https://refactoring.substack.com/subscribe)?

**2)** ❤️ **Share it** — Refactoring lives thanks to word of mouth. Share the article with your team or with someone to whom it might be useful!

I wish you a great week! ☀️

Luca
