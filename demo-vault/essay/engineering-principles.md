---
aliases:
  - "Engineering Principles"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-essays|Publish Essays →]]"
Status: Evergreened
URL: "https://refactoring.fm/p/principles"
"👓 Status": Not started
"Created time": "2024-04-18T14:53:00.000Z"
Date: 2021-10-07
"Has Notes":
  - "[[evergreen/create-principles-together-with-your-team|Create principles together with your team]]"
  - "[[evergreen/good-principles-are-specific|Good principles are specific]]"
  - "[[evergreen/use-principles-in-various-scenarios|Use principles in various scenarios]]"
  - "[[evergreen/principles-create-alignment-and-enable-autonomy|Principles create alignment and enable autonomy]]"
  - "[[evergreen/goals-should-provide-direction-but-preserve-autonomy|Goals should provide direction but preserve autonomy]]"
  - "[[evergreen/autonomy-alignment-trust|Autonomy + Alignment = Trust]]"
  - "[[evergreen/autonomy-drives-motivation-speed-and-scale|Autonomy drives motivation, speed and scale]]"
  - "[[evergreen/the-three-pillars-of-motivation|The Three Pillars of Motivation]]"
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: c0cba038-7da9-41a2-a8b3-a9c3116017f3
---

# Engineering Principles

1. **What is the most important point?**

1. **Why is that the most important point? *****(what can you achieve with it)***

1. **Why should people care? *****(what's the benefit)***

1. **What is the easiest way to understand the most important point?**

1. **How do you want the reader to feel?**

1. **What should the reader do next?**

1. **The Three Qualities (*****pick 2+*****)**

### 📑 Materials

---

[Untitled](https://www.notion.so/fc0eacc78ae947638baeeca3a4f7cfca) 

### ✍️ Post

---

In his bestseller book [Drive](https://www.goodreads.com/book/show/6452796-drive), Daniel Pink argues our motivation is *driven* by three main factors:

- **Autonomy **—** **the desire to be **self-directed**. We get motivation and joy by having control over our life.

- **Mastery **— the desire to **improve our craft**. We get satisfaction by getting better at what we do.

- **Purpose **— the desire to have a **positive impact **on the world. We are empowered by work that serves a higher purpose.

As a manager, you can reflect on how these elements are cultivated in your team and what you can do to support them.

This article is about **autonomy**.

### 🏃 Autonomy

Autonomy is defined as a condition of **self-government**. At work, it is the capacity to make decisions without the need or help of external entities.

![image](../assets/9fc8ec1c494f46ea.png)

Other than driving motivation, autonomy is crucial to make companies *scale. *It reduces the need for **communication**, so people are able to do more work.

This is true both at individual and team level. Cross-functional teams have become popular in tech companies because they can do *autonomous *work on separate product areas. 

In my experience, there are three core elements that enable autonomy, both for teams and individuals: 

- 🎯 **Goals **— people should know what they should achieve

- 📚 **Skills **— people should have the skills to achieve it

- ⭐ **Principles **— people should know how to make decisions

Together they make autonomy possible, and provide the alignment that makes it *effective*.

Autonomy + Alignment = **Trust**

![image](../assets/658f217735ef447c.png)

### 🎯 Goals

Good goals are about what should be achieved, without being prescriptive about *how* it should be achieved. They provide **direction** while preserving autonomy.

Goals should be concrete, combining **qualitative** direction with **measurable** results, while people should stay responsible of *what* should be built to meet such goals.

You can find several goals examples [here](https://hypercontext.com/goal-examples), following the [OKR framework](https://en.wikipedia.org/wiki/OKR). 

### 📚 Skills

Teams and individuals should have all the skills needed to achieve their goals.

For teams, this means being able to carry on work without external **dependencies**. [Feature teams and cross-functional teams](https://refactoring.fm/p/feature-teams-vs-durable-teams-) are born out of this need. 

For individuals, this is about their own skills, plus having resources and support to cover what they miss.

### ⭐ Principles

Chances are you don't just want goals to be met, you want them to be met while respecting your **culture** and your **values**.

Enter principles. 

Principles provide a blueprint for how **decisions** should be made.

Without principles, you might meet goals in a way that doesn't reflect your culture. Engineers might deliver features without peer review, managers might meet deadlines by making people overwork, or teams might cut corners on security and accessibility.  

Principles are a set of **shared beliefs **that create alignment over how you do things in your company. They are, simultaneously:

- 👌 A definition of what **good** looks like.

- 🗣️ A **shared language** to be used in daily work.

#### How to use principles

Principles are useful in a number of circumstances:

- **Evaluate designs **— when creating something new, be it a process or a piece of software, you might use principles to understand if you are missing some crucial aspect of your work.

- **Onboarding **— you can get new members up to speed faster by using principles to instruct them about the way you work.

- **Post-mortems** — you can compare a failure against principles to spot what went wrong, and possibly adjust principles themselves to improve in the future.

- **Reviews **— principles guide people's behaviour, so you can use them to review behaviour as well. Principles provide useful review *lenses* because they go beyond pure performance. 

#### What good principles look like

It might seem counterintuitive, but in order to be useful, principles should be **specific**.

Simple propositions like "*we write high quality software*" or "*we care about customers*", are not going to cut it. They are not going to be useful in real life.

To tell whether a principle is good, ask yourself: how am I able to tell if we are not following it? If you don't have a good answer, chances are the principle is not clear enough.

Here are a few examples of good engineering principles, taken from successful companies:

- [**Fix problems, even when they are not yours**](https://blog.asana.com/2016/05/asana-engineering-values/) — by Asana. Asana strives to create a company that is a collective of peers, where people are encouraged to be *egoless* and always do the right thing. So you should refactor code as you encounter it, work on performance issues whose ownership is hard to pin down, and have rotating on-calls.

- [**We peer review every change**](https://github.com/Skyscanner/engineering-principles#we-peer-review-every-change) — by Skyscanner. Peer review increases the quality of the software you ship, while also spreading knowledge of the codebase across the team. It is a no-brainer practice and I love that Skyscanner puts it front and center in his core engineering principles.

- [**Psychological Safety**](https://github.com/artsy/README/blob/main/culture/engineering-principles.md#psychological-safety)** **— by Artsy. To be productive and do the right thing, engineers must feel safe asking questions and discussing mistakes. Artsy strives to foster a psychologically safe work environment, with leadership being especially accountable for that.

- [**Engineers own their impact**](https://medium.com/airbnb-engineering/engineering-culture-at-airbnb-345797c17cbe#.xvzkgiwml) — by Airbnb. Engineers are involved in goal-setting, planning and brainstorming for all projects, and are individually responsible for creating value. They are also responsible for the code that gets shipped, monitoring that it works fine after it is in production.

#### How to define principles

If you want / need to create principles from scratch, you should involve your team in doing so. There is no better way to create alignment than making people invested in the process. If you are in a leadership position, this is what the process might look like:

- ⬇️ **Provide high-level guidance **— provide your team a few strategic themes you would like to highlight in principles. You might say, for example, you want to define engineering principles that incorporate a few best practices the team believes in (let them propose a few to begin with), and also describe the communication dynamics the team wants to foster.

- ⬆️ **Get proposals from your team **— let people in your team come up with their best proposals, including a description of why these make for good candidates, and how they would use them in practice. 

- 🔄 **Challenge and iterate **— discuss these principles, introduce with your own, improve them and eventually wrap-up. As a leader, it should be clear you are responsible for the final outcome, but people should feel invested and aligned with the result.

### 📚 Resources

- 📑 [**Spotify Engineering Culture**](https://vimeo.com/85490944)** **— great animated video (in [two parts](https://vimeo.com/94950270)) that explains how Spotify's culture is centered on autonomy + alignment. 

- 📑 [**Why Engineering Principles Matter**](https://medium.com/@SkyscannerEng/why-engineering-principles-matter-993298f7d792)** **— by Skyscanner. The article enumerates Skyscanner Engineering principles and explains why they matter. There is also a separate, dedicated [repo](https://github.com/Skyscanner/engineering-principles) for principles. 

- 📑 [**Artsy Engineering Principles**](https://github.com/artsy/README/blob/main/culture/engineering-principles.md) — Artsy's values have a strong focus on how people should work and interact with each other. Each value includes a description, examples, and several further readings.

- 📑 [**Asana Engineering Values**](https://blog.asana.com/2016/05/asana-engineering-values/)** **— Asana's engineering values are few and well articulated. They also include examples of how they are used within the company.

- 📑 [**Engineering Culture at Airbnb**](https://medium.com/airbnb-engineering/engineering-culture-at-airbnb-345797c17cbe#.xvzkgiwml)** **— This is an old (2014) but still valid piece about a few key values that guide Airbnb's Engineering work. They include non trivial elements such as career tracks and team structures.

### ⭐ Weekly Featured Jobs

Here are the remote engineering jobs I recommend this week 👇 I personally review each of these jobs and I have a call with people from the companies to get more context, provide advice and better understand the opportunity.

#### 🆕 Flick — [Full Stack Typescript Engineer](https://pallet.xyz/list/refactoring-jobs/jobs/a0e84d49-8f2a-4e3c-a96c-26f1ace58e2c)

[Flick](https://www.flick.tech/) is an analytics tool for Instagram creators. I talked with their founder [Andreas](https://twitter.com/andyasprou) about their hiring process and needs — their tech stack is cutting edge and they wrote one of the best job posts I have ever seen.

#### 🆕 Makelog — [Senior Full Stack Engineer](https://pallet.xyz/list/refactoring-jobs/jobs/f9d03746-5990-4756-bb2a-8cc958f4c716)

[Makelog](https://makelog.io/) helps companies to keep customers engaged via product updates. It is a brilliant tool that automatically integrates with your engineering process, such as commits and pull requests. Their founder, [JJ](https://twitter.com/HiJulieJennifer) is insightful and driven by a compelling vision.
