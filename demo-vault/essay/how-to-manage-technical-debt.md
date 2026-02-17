---
aliases:
  - "How to Manage Technical Debt"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-essays|Publish Essays →]]"
Status: Evergreened
URL: "https://refactoring.fm/p/technical-debt"
"👓 Status": Not started
"Created time": "2024-04-18T14:53:00.000Z"
Date: 2022-02-03
"Has Notes":
  - "[[evergreen/evaluate-cost-impact-contagion-to-assess-technical-debt|Evaluate Cost + Impact + Contagion to assess technical debt]]"
  - "[[evergreen/brainstorm-with-eng-leaders-to-come-up-with-tech-debt-initiatives|Brainstorm with eng. leaders to come up with tech debt initiatives]]"
  - "[[evergreen/get-help-from-other-areas-to-understand-tech-debt-roi|Get help from other areas to understand tech debt ROI]]"
  - "[[evergreen/repaying-tech-debt-impacts-business-via-second-order-effects|Repaying tech debt impacts business via second-order effects]]"
  - "[[evergreen/address-large-tech-debt-by-understanding-business-opportunity|Address large tech debt by understanding business opportunity]]"
  - "[[evergreen/address-medium-debt-with-regular-maintenance|Address medium debt with regular maintenance]]"
  - "[[evergreen/address-small-tech-debt-with-the-boyscout-rule|Address small tech debt with the boyscout rule]]"
  - "[[evergreen/technical-debt-vs-product-maturity|Technical debt vs product maturity]]"
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: b87b2074-f5ae-41b9-a5fe-2c4eb22b55c2
---

# How to Manage Technical Debt

### 📑 Materials

---

[https://technology.riotgames.com/news/taxonomy-tech-debt](https://technology.riotgames.com/news/taxonomy-tech-debt)

[https://refactoring.fm/p/the-true-meaning-of-technical-debt](https://refactoring.fm/p/the-true-meaning-of-technical-debt)

[https://blog.stepsize.com/the-perfect-process-to-manage-tech-debt/](https://blog.stepsize.com/the-perfect-process-to-manage-tech-debt/)

[https://www.oreilly.com/library/view/97-things-every/9780596809515/ch08.html](https://www.oreilly.com/library/view/97-things-every/9780596809515/ch08.html)

[Untitled](https://www.notion.so/48ec1ef7639e4371bac3953e62f3cbaa) 

[Untitled](https://www.notion.so/01e3304662e54127b4d16a80593877df) 

[Untitled](https://www.notion.so/bb994075181a4c1298596809a90bd548) 

### ✍️ Post

---

About one year ago I stumbled upon an old video by Ward Cunningham, one of the original Agile fathers, about technical debt.

[Video](https://www.youtube.com/watch?v=pqeJFYwnkjE)

There he describes debt as the natural result of writing code about something we don't have a proper understanding of.

> *If we fail to make the program aligned with what we ****understand**** to be the proper way to ****think about**** our [...] objects, then we are going to continuously stumble into ****disagreement****, and that would slow us down like paying interest on a loan.*

The video and the quote above inspired me to write a full article on the [**meaning of technical debt**](https://refactoring.fm/p/the-true-meaning-of-technical-debt), which as of today is my most popular article ever, with more than 50,000 views.

The article focused on what technical debt really is and how you can *prevent* it in various scenarios. It did little, though, to help you address and reduce debt once it’s there. 

This new article is a practical, thorough guide to manage technical debt with your team, from the quarterly strategy down to the day-by-day.

It covers:

- 🔥 **The impact of technical debt on your team**

- 🤝 **How technical debt changes with your company stage** 

- **🏃‍♂️ A process for technical debt: small vs medium vs large debt**

- ⚖️ **How to assess and prioritize technical debt**

It is one of my most researched articles ever. I read tens of articles and spoke with the best engineers I know to get their strategies and insights. 

Let’s dive in 👇

### 🔥 The Impact of Technical Debt

Technical debt has a strong impact on **velocity **and **happiness**. Low morale in turn leads to ever decreasing velocity and higher turnover.

We all have an intuitive understanding of how technical debt can drag down development work, but how so?

I talked with Alex Omeyer, who [surveyed 200+ engineers](https://www.stepsize.com/report) and managers around technical debt. Here are the insights that struck me the most:

- 58% of companies have **no process** for managing technical debt.

- 66% of engineers believe the team would **ship up to 100% faster** if they had a process for technical debt.

- 52% of engineers believe that technical debt negatively **impacts their team’s morale**.

Quoting Alex: 

> *I was surprised to see such high numbers, but I can empirically validate them. Think of it this way: how many times have you estimated a feature would take the sprint, and it ended up taking two, or three? Now imagine this at the scale of an entire company and the ramifications it would have. It’s not hard to believe that companies who truly have a good handle on their technical debt ship twice as fast as those who don’t.*

Does this equally stand for all companies? Or companies at different stages have different relationships with debt?

### 🤝 Technical debt in your company stage

Debt is often described as the result of a trade-off where you prioritize speed and growth over engineering quality.

While this is the case sometimes, it is also true that fast growth *naturally* leads to technical debt, because when the product changes at a fast rate, your engineering assumptions get invalidated equally fast.

How does technical debt changes throughout the various stages of your company? For the sake of simplicity, let’s consider three main stages:

- **0 to 1 **— you start building a product from scratch, with a set of initial assumptions.

- **Product Market Fit **— you figure out what works, double down on it, and scrap the rest.

- **Growth **— you grow your business predictably and harden your tech.

The earlier you are in the scale, the more your product moves fast, and the more *leverage* you get by accruing debt.

The latter you are in the scale, the more debt becomes a drag that *prevents* you to grow. So you get more leverage by *repaying *debt, but you will need more effort than in earlier stages.

For early stage startups it is inevitable and even healthy to accumulate debt early on. At the same time though, you should create processes to help repaying debt from the very beginning.

![image](../assets/45d728743b6d4579.png)

### 🏃‍♂️ A process for technical debt

Watching how great teams address technical debt, a few themes stay remarkably constant. Processes to reduce debt are always:

- **Intentional **— managers are able to articulate well what they do to keep debt in check. Everyone in the team knows how this works. 

- **Continuous **— processes are never based on isolated initiatives. People address debt every day.

- **Multiple** — debt is managed in multiple ways, based on its type and size. There is no one size fits all process.

Let’s see how you can address technical debt, based on the size of debt itself 👇

#### 🟩 Small Debt

Small debt is about minor improvements you can do in a few hours of time. A few examples of small debt: 

- Add some missing tests

- Deduplicate some code by creating a simple abstraction

- Adjust a piece of code to make it adhere with your codebase conventions

The best way to address small debt is to make these changes whenever you are working on that code for some other reason. You basically follow [Robert C. Martin’s](https://www.oreilly.com/library/view/97-things-every/9780596809515/ch08.html)[ boyscout rule](https://blog.stepsize.com/how-to-be-an-effective-boy-girl-scout-engineer/): 

> ***Always leave the code better than you found it***.

This is effective, as opposed to scheduling an independent task, because it avoids context-switch and makes the change cheaper. However, this means the timeline for such improvements is best-effort (it depends on other tasks), so this process is only suitable for issues that are not too harmful. 

Zach Wolfe, Tech Lead at Amazon, described this perfectly, also detailing how they manage it in the sprint 👇

> *For small debts, fostering a culture of ****constantly making minor improvements**** to the team's software as part of the “****definition of done****” is effective both at driving down debt and improving morale. At the level of sprint tasks, empower a team to regularly double the size of one or two small tasks in a sprint to tackle small debts in related components. Great examples here are improving test reliability and speed, automating a manual sprint task.
*

#### 🟨 Medium Debt

Medium Debt is about issues you need to prioritize and schedule, because they are somewhat impactful, but you can still fix them in a few hours to a couple of days at most.

Examples are:

- Automate a tedious manual process

- Adjust performances of a small service that’s been degrading over time

- Remove a bottleneck in the CI/CD pipeline to shave a few minutes off the deploy time

How should you address these?

In my experience, the best approach is to allocate some fixed time every sprint to spend on such maintenance. The right share largely depends on your team, but it might be anything between 10% to 30%. If you need to spend more than 30%, you should probably address debt at a more strategic level (see *large debt*).

You can also decide to assign fixed days to it (e.g. Fridays) to build the habit.

This is not the only approach, though. There are teams who put these tasks in a backlog together with new product features, prioritize the ones against the others and plan what to do sprint by sprint. While this is not wrong by itself, it has a few drawbacks:

- **Expensive **— negotiating tech debt against product work every sprint can bring serious overhead, especially for minor tasks.

- **Apples vs oranges **— sometimes it’s hard to identify the ROI of maintenance tasks like refactoring a small module or speeding up CI/CD.

- **Unreliable **— if you have to negotiate it every time, it is more likely that maintenance will be left behind when you are under pressure, and more generally it will be harder to keep a consistent pace.

[Corvin Deboeser](https://twitter.com/CorvinDeboeser), Software Engineer who also had a PM stint, wrote: 

> *When I was PM, my dev team and I **blocked out some hours per sprint to tackle tech debt**. The total amount of story points we'd plan for would only account for about **90% of dev capacity**. [...]

Tech debt would usually only come in towards the end (last 3-4 of 10 working days sprint) and devs that wanted to pull them in would announce this in daily stand-ups first. If anyone felt this would endanger the sprint success, it could be raised and we timebox-discuss that.*

It is also worthy mentioning that **fixing bugs ≠ reducing debt**. Gianni Fiore, CTO at Rebrandly, warns against this 👇

> *Fix the your specific bugs first, then think at how to improve the ground base in a separate session. Do not refactor code with the purpose of solving a bug: solve the bug first, then commit/push it, close the task and have your merge request accepted.*

#### 🟥 Large Debt

Large debt is about strategic initiatives that span between a few weeks and a few months of work. These might be:

- Refactoring a large piece of legacy code to enable some product improvements

- Migrate a service to a different library / framework because of changed requirements

- Rework a piece of your infrastructure to improve reliability and performance.

These initiatives need to be planned on a longer timeframe — e.g. quarterly — and evaluated strategically, just like product work, based on their business opportunity.

This is not easy, though, because the impact of such initiatives sometimes doesn’t apply to the business *directly*, but via *second-order effects. *Such effects include team velocity, happiness, or reduced turnover.

To evaluate this, you can get help from stakeholders from other areas outside engineering, like product, marketing, or support. Large engineering works may enable new features and processes, or improve existing ones. Leaders from these areas can help you measure such benefits and ultimately support you in advocating for this work.

Zach weighs in on this 👇

> *I think in the case of large debts, the relationship [between Product and Engineering] is joint discovery of business opportunity. Engineering produces a tech debt reduction proposal that uses ROI units comparable to features, whether to do them is a business decision.

Tech debt proposals should at minimum include a ****feasible solution**** and a ****return on investment**** in units that can be used to compare them to features. An example ROI: “by spending 50 engineer hours the team can eliminate 1 engineer hours spent doing a manual repeated tasks we expect to do 100 times this year.”*

Finally, these proposals need to be sourced, collected, and evaluated multiple times a year. Collaboration is crucial here too, as the best ideas to reduce debt might span multiple teams.

Hold brainstorming sessions on a quarterly basis with other engineering leaders and keep a shared backlog of such initiatives. You can evaluate them with the **Riot Taxonomy** 👇

### ⚖️ The Riot Taxonomy of Technical Debt

I am a fan of the [taxonomy used by Riot](https://technology.riotgames.com/news/taxonomy-tech-debt) to evaluate and prioritize tech debt.

They use three main metrics:

- 💣 **Impact **— business issues caused by the debt, or the value you unlock by repaying it. Crucial for the ROI equation.

- 💸 **Fix Cost **— a rough estimate based on some feasible solution. For the sake of prioritization, there is no need for it to be accurate. T-shirt sizing (S, M, L, XL) is fine.

- 🦠 **Contagion **— this answers the question: “*if this tech debt is allowed to continue to exist, how much will it spread?*”. It’s a great angle because, in this regard, not all debt is created equal.

The contagion metric is particularly powerful because it informs on how impact and cost change over time. [Bill Clark](https://www.ltrandolphgames.com/), former Engineering Manager for League of Legends, explains this well 👇

> *If a piece of tech debt is well-contained, the cost to fix it later compared to now is basically identical. You can weigh how much impact it has today when determining when a fix makes sense. 

If, on the other hand, a piece of tech debt is highly contagious, it will steadily become harder and harder to fix. What’s particularly gross about contagious tech debt is that its impact tends to increase as more and more systems become infected by the technical compromise at its core.*

### 📚 Resources

- 🌀 [**The True Meaning of Technical Debt**](https://refactoring.fm/p/the-true-meaning-of-technical-debt) — the original Refactoring article that addressed the meaning of technical debt and how to prevent it.

- 📑 [**What Companies Can Do to Reduce Technical Debt**](https://www.infoq.com/articles/reduce-technical-debt/)** **— Alex Omeyer, Nicolas Carlo and Maarten Dalmijn discuss some of the key findings of the “State of Technical Debt 2021”, that surveyed 200+ engineers around the topic.

- 📑 [**A Taxonomy of Tech Debt**](https://technology.riotgames.com/news/taxonomy-tech-debt)** **— the approach adopted by Riot Games to evaluate and prioritize tech debt initiatives.

- 💬 [**Community Thread**](https://community.refactoring.club/c/coming-up/how-to-prioritize-technical-debt-vs-new-features)** **— the discussion we had in the community around technical debt, that brought many contributions to this post. If you want to join, [fill out this survey](https://airtable.com/shrb2I6TW2QyDqtEZ) and I will get back to you!

---

### How would you rate this week’s edition? 🤔

[**Amazing**](https://reactions.sparkloop.app/questions/2446/react?with=1)** • **[**Great**](https://reactions.sparkloop.app/questions/2446/react?with=2)** • **[**Good**](https://reactions.sparkloop.app/questions/2446/react?with=3)** • **[**OK**](https://reactions.sparkloop.app/questions/2446/react?with=4)** • **[**Meh**](https://reactions.sparkloop.app/questions/2446/react?with=5)
