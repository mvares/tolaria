---
aliases:
  - "Mental Models for Engineers and Managers"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-essays|Publish Essays →]]"
Status: Evergreened
URL: "https://refactoring.fm/p/mental-models-for-engineers-and-managers"
"👓 Status": Not started
"Date HH": 2024-11-14
"Created time": "2024-04-18T14:53:00.000Z"
Date: 2024-02-08
"Has Notes":
  - "[[evergreen/cynefin|Cynefin]]"
  - "[[evergreen/theory-of-constraints|Theory of Constraints]]"
  - "[[evergreen/sunk-cost-fallacy|Sunk Cost Fallacy]]"
  - "[[evergreen/binstack|Binstack]]"
  - "[[evergreen/second-order-thinking-first-principles|Second-order Thinking & First Principles]]"
  - "[[evergreen/type-1-vs-type-2-decisions|Type 1 vs Type 2 Decisions]]"
  - "[[evergreen/the-map-is-not-the-territory|The Map is not the Territory]]"
Tags:
  - Essay
  - Mgmt
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 004bd037-f1c8-4868-ba22-d9159672c5cd
---

# Mental Models for Engineers and Managers

### 📑 Materials

---

[https://fs.blog/eisenhower-matrix/](https://fs.blog/eisenhower-matrix/)

[https://fs.blog/smart-decisions/](https://fs.blog/smart-decisions/)

[https://athenian.com/blog/6-decision-making-frameworks-for-engineering-leaders](https://athenian.com/blog/6-decision-making-frameworks-for-engineering-leaders)

[https://fs.blog/second-order-thinking/](https://fs.blog/second-order-thinking/)

[https://fs.blog/mental-models/](https://fs.blog/mental-models/)

[https://untools.co/](https://untools.co/)

### Post

---

I am a big fan of mental models, and over time I have built a small *arsenal* of favorites that I use in many situations.

To me, a mental model is like software for my brain. It is a thought process that I can *run*, under the appropriate circumstances, to get to some output.

Mental models are also popular with engineers — I suspect because of our familiarity with processes. As engineers, we don’t like ambiguity and uncertainty, so it is comforting to turn something messy into a deterministic series of steps.

So for today I am listing the 10 mental models I like the most, together with the most popular ones in the Refactoring community.

For each model, I will explain it in detail, provide examples for engineering and management, create drawings whenever possible, and include further resources to learn more.

So, consider this post article *compendium* of the best mental models for engineers and managers in tech. You will be able to bookmark this and revisit it over time.

Here is the agenda:

1. **🗺️ Map vs Territory**

1. **⚖️ Type 1 vs Type 2**

1. **🔭 Second-order Thinking + First Principles**

1. **↩️ Inversion**

1. **🥇 Binstack**

1. **🪣 Sunk Cost Fallacy**

1. **🔗 Theory of Constraints**

1. **🌪️ Cynefin**

1. **➕ Eisenhower Decision Matrix**

1. **⭕ Circle of Competence**

Let’s dive in!

---

### 🗺️ The Map is not the Territory

*The Map is Not the Territory* is a mental model that emphasizes the difference between our perceptions / models (the map) and the actual reality (the territory).

It is the first one that we are covering, for a reason. It reminds us that models are useful, but they are not the reality: their goal is to represent a *slice* of reality, in a way that is useful for a specific goal.

In other words, they are just *tools —* if you overstep their boundaries / goal, they may turn useless or even harmful.

This is true for all kinds of models, not just the big, high level frameworks we are covering today. We create models all the time:

- 💻** Software** — when designing software, we model of how the system works in the form of diagrams, docs, and even tests. However, these are not a perfect representation of the actual code. A diagram could help understand the structure of your codebase, but it may not be exhaustive about dependencies, which makes it insufficient to decide e.g. how to partition the system.

- ⏱️** Project management** — we create plans, roadmaps, and resource estimates, to help us organize and deliver projects. However, these are not *the* project itself, and we must be prepared to adapt our plans if new information becomes available or unforeseen challenges arise.

Whenever you encounter a hard problem, focus on what you need to accomplish, and figure out what models / frameworks can be helpful.

### ⚖️ Type 1 vs Type 2

Type 1 vs Type 2 is a simple framework by Jeff Bezos to help with decision-making. It divides decisions into two categories:

1. **Type 1** — *irreversible* decisions that represent a large amount of risk. They require thorough decision-making and careful consideration. Examples in tech may include choosing your database or committing to a specific stack.

1. **Type 2** — *reversible* decisions that can be easily adjusted or undone if they don't work out as planned. They don't require excessive attention and can be made more quickly. Examples may include choosing between two similar tools, or making minor adjustments to a project.

The reason why this matters is that *most* decisions in life and work are Type 2, so you should move forward quickly with them, as opposed to applying the Type 1 decision-making style. In my experience, analysis paralysis on Type 2 stuff is way more common than the opposite — that is, being careless on irreversible decisions.

This mental model is similar, or correlated to other ones:

#### **1) Bias for action**

The general tendency to favor action over inaction. Type 2 decisions are *bias for action *material, while Type 1 ones are those where you stop and consider.

#### **2) Asymmetric risk-reward** 

This was made popular by Nassim Taleb in Antifragile, and refers to the strategy of positioning yourself in situations where the potential losses are limited, while the potential gains are high or unlimited.

In other words, aim for capped downside + uncapped upside. This is ideal for Type 2 bets — where you potentially get a big benefit, but quickly cut your losses if things don’t work out.

### 🔭 Second-order Thinking + First Principles

Second-order thinking is about considering the future consequences of a decision, going beyond the immediate implications.

In engineering, this is literally the name of the game. Whenever you design a system, or create an abstraction, you are never only thinking at solving the problem here and now — you are also thinking at the impact on the larger system, on your team workload, on infrastructure, and more.

On a practical level, I know two ways to prompt second-order thinking:

- **Logically • “*****and then what*****” **— For any decision you are considering, ask yourself “*and then what?*” many times over. Do that 4-5 times and you will be surprised by how far you can go.

- **Temporally • the rule of 10 **— many choices look different under different timeframes. Ask yourself about the consequences in 10 hours, 10 days, 10 months, and 10 years.

The dual version of second-order thinking is *first principles*.

When you ask yourself “*and then what”*, you are moving forward*. *Likewise, you can ask yourself “*why*” several times (e.g. [the five whys](https://en.wikipedia.org/wiki/Five_whys)) to go *backwards*, and get to the principles backing the decision, or root causes in case of a problem.

- PICTURE

Combining forward and backward reasoning is powerful to come to better conclusions.

### 🔀 Inversion

Inversion has long been a favorite of mine. It is a way of addressing problems by trying to *avoid the negative*, rather than striving to achieve the positive.

Pre-mortems are a popular example of inversion in engineering. As you work on a project, you can ask questions to address common issues *before* they actually happen:

- **Project running late** — *what could cause us to miss our deadline?*

- **Technical Debt** — *what changes to requirements would make this design obsolete in the future?* (also, second-order thinking)

- **Build the wrong thing **—** ***are there any requirements missing?*

- **Scaling and reliability issues **—** ***are we creating any bottlenecks or single points of failure?*

 I wrote a full newsletter edition about Inversion 👇

[https://refactoring.fm/p/the-power-of-inversion-](https://refactoring.fm/p/the-power-of-inversion-)

### 🥇 Binstack

Binstack is a fantastic decision framework that I have discovered thanks to Clemens’ recommendation in the community

> *Don’t overcomplicate multi-dimensional decisions. Pick the dimension that you most care about, define what “substantial” looks like in that category, and discard any options that aren’t substantial in that category. Rinse and repeat.

— Clemens Adolphs*

What does this mean? Well, many decision / prioritization frameworks (e.g. [RICE](https://www.intercom.com/blog/rice-simple-prioritization-for-product-managers/)) tell you to pit items against each other by considering various *dimensions*, giving a score to each of them (e.g. from 1 to 5), and considering the total.

In my experience, though, this leads to murky results, for two reasons:

- **Not all dimensions are equally important** — some matter more than others. You can weight them, but that becomes even more cumbersome.

- **Values are arbitrary **— in many cases it is hard to assign a numeric value to dimensions. It ends up being a bit arbitrary, and driven by the what options we *really* want to win.

So, Binstack says two things:

- **Turn numeric values into yes/no **— define a level that makes that dimension successful or not, and just note if items are compliant or not. For example, instead of having a “Revenue” score from 1 to 5, have a “*at least a 10% revenue bump*” threshold

- **Put dimensions in order of importance **— rank them from the most important to the least important, and pick the item that meets the most of them, in descending order.

Binstack works for me because 1) it is decisive, and 2) has the right amount of nuance (not too much, not too little) that you need for most decisions.

You can find the full, original article about Binstack, with examples and details, below 👇

- [**Binstack: Making a maximal multi-dimensional decision**](https://longform.asmartbear.com/maximized-decision/)

### 🪣 Sunk Cost Fallacy

Sunk Cost Fallacy is the cognitive bias that describes our tendency to continue investing in a project / activity because of the time / effort / money we have already invested into it, regardless of whether the future costs outweight the future benefits.

In software, one of the ways this is most often displayed by over-committing to an initial plan, even when it becomes more rational to invest resources in a different way. 

But the final goal of software, of course, is to **deliver value**, not to **deliver plans**, so if you find better ways to deliver value users, you should change the plan and go for it.

A practical way to limit the sunk cost fallacy, other than talking yourself out of it, is… to limit costs. For example, to avoid the temptation of fixating over a plan, invest in a plan that is detailed *just enough* to support your decision making, not more.

Or, to avoid sticking too long with a leaky abstraction because of all the work you have put into it, create small abstractions in the first place.

In engineering, in most cases, smaller is better. This is obvious to hear, and it takes a lifetime to master.

### 🔗 Theory of Constraints

The Theory of Constraints (TOC) is a model that views any system as being limited by a very small number of constraints — and, more immediately, by its weakest link.

The corollary of TOC is that, to improve the performance of a system, you should focus on bottlenecks, one at a time.

For example, you may measure the various steps of your release process and discover that the biggest bottleneck is the time the code spends idle, waiting for review. Or you may do tracing for your API calls and figure out that the largest chunk of response times come from the database.

TOC was introduced by Eliyahu M. Goldratt in his 1984 book titled [*The Goal*](https://en.wikipedia.org/wiki/The_Goal_(novel))*. *The author suggests a four-step process to improve a system’s performance:

1. **Identify** • the system's constraint.

1. **Decide** • how to *exploit* the system's constraint.

1. **Subordinate** • everything else to the above decision.

1. **Elevate** • the system's constraint.

1. **Repeat** • this is a continuous improvement cycle. Once a constraint is addressed, you should move to the next.

If you want to learn more, here is the most thorough description of TOC I have found, which includes detailed guidance on each of the steps:

- 📑 [**Theory of Constraints — by Lean Production**](https://www.leanproduction.com/theory-of-constraints/)

### 🌪️ Cynefin

The Cynefin Framework is a decision-making tool created by Dave Snowden during his work at IBM in the late 1990s. The term "Cynefin" is a Welsh word meaning 'habitat', and categorizes problems into five domains:

![image](../assets/5d80b513071f4009.png)

#### **1) **🟢** Clear**

In this domain, cause-and-effect relationships are clear and predictable. The appropriate approach is to sense the situation, categorize it, and respond based on established best practices. 

Example: fixing a known bug, or adding a simple feature.

#### **2) **🟡** Complicated**

Here there may be multiple correct answers, and while there is a clear relationship between cause and effect, it may not be apparent to everyone. Expert analysis or the use of analytical methods is often required. 

Example: designing a system with a set of advanced features that require thorough planning.

#### **3) **🔴** Complex**

In this domain, cause-and-effect relationships are only clear in retrospect. The right approach is to 1) *probe* (experiment), 2) *sense* (learn from the experiment), and then 3) *respond*. 

This is often the case for innovation and zero-to-one scenarios. For instance, creating a new product needs constant experimentation and feedback from users, which makes a classic *complex* domain.

#### **4) **🟣** Chaotic**

In chaotic situations, cause-and-effect relationships are unclear and the situation is highly unpredictable. 

The appropriate approach is to establish order first, then sense where stability is present, and respond to turn the chaotic into the complex. 

An example could be responding to a major system outage or security breach.

#### **5) **🔵** Confused**

This is the domain of the unknown, where it is unclear which of the other four domains applies. 

The appropriate approach is to break down the situation into constituent parts and assign each to one of the other four domains.

![image](../assets/7bb904dbcf3b416d.gif)

The Cynefin framework is useful because it gives you a blueprint of how to respond to situations, and also an ideal *path *to turn chaos into order.

Thanks to Umberto Nicoletti for recommending it on the community 🙏

More info and examples about Cynefin below 👇

- 📑 [A Leader’s Framework for Decision Making](https://hbr.org/2007/11/a-leaders-framework-for-decision-making)

- [Cynefin for Developers](https://lizkeogh.com/cynefin-for-developers/)

### ➕ Eisenhower Decision Matrix

The Eisenhower Decision Matrix is one of the most famous management frameworks out there. It helps you prioritize tasks based on *urgency* and *importance*.

![image](../assets/9c32c2638e1f4587.jpg)

The matrix is divided into four quadrants:

1. **Urgent and Important → Do First** — tasks that need immediate attention and contribute significantly to long-term goals. E.g. fixing a critical bug that's affecting a large number of users.

1. **Important but Not Urgent → Schedule** — tasks that are important for long-term goals but do not need immediate attention. E.g. planning for a new feature.

1. **Urgent but Not Important → Delegate** — tasks that need to be done quickly but do not contribute significantly to long-term goals. They can be delegated to others. E.g. routine administrative tasks, or responding to non-critical emails.

1. **Not Urgent and Not Important → Don't Do **— tasks that do not contribute to long-term goals and do not need immediate attention, so they can be eliminated. Examples could be attending non-essential meetings or browsing the internet aimlessly.

The Eisenhower matrix is a fantastic starting point to reflect on how you spend your time, but it is also pretty basic. I tried to give it more nuance in this previous piece about delegation 👇

[https://refactoring.fm/p/how-to-delegate](https://refactoring.fm/p/how-to-delegate)

### ⭕ Circle of Competence

The Circle of Competence, by the great Charlie Munger, is about recognizing the boundaries of your knowledge, to guide effective decision-making.

Munger mainly used it for his investment decisions — he would only invest in things he truly understood and on which he would have an *edge* because of his skills.

Personally, I think about it often when it comes to my career path, and opportunities I *may *or* may not *pursue. 

I basically ask myself: ***why me?***

- *Am I better positioned than most other people for doing that?*

- *Do I have a special shot at being successful?*

The best opportunities are often about hard things for which you happen to have good answers to the questions above.

Also, I don’t think at my circle of competence — and that of everyone, really — as an actual circle. Each circle is a unique combination of skills, passions, and life experiences, so I imagine it more as a weird shape, with both regular parts and a good share of twists and turns.

So, the best opportunities are those that overlap *the most* with our circle, and to do that they may look weird — just like the circle. 

Writing a newsletter full-time definitely classifies as weird — I am grateful to have found it, and that it matches my circle well.

More about the [circle of competence](https://fs.blog/circle-of-competence/).

### ⚡ Quick models

Finally, here are some quicker ideas that you can apply in a snap:

#### **Rule of Three**

recommended by Radoslav Stankov, CTO at AngryBuilding:

> *I often use this in programming to extract abstractions. Only extract when you see at least 3 instances. This is one of the first things I coach new engineers. It is also useful for helping you to add needless processes around one-offs. Example: Don't add rule to stop deploying on Fridays because this is one time.*

#### **You Are Not Google**

recommended by Kendrick Curtis, VP of Eng at Codacy: 

> *Build your software, and your team, and your process, according to the scale you are currently operating at. Most CRUD webapps don’t need to be highly redundant scalable microservice architectures with queues and dead letter topics and and and. But this also applies to teams and organizations too: your 10-person startup does not need a performance review matrix or quarterly roadmap planning events.*

#### Hill Chart

The Hill Chart represents the project's progress on a spectrum from "unknown" to "known" to "done." It is named after the metaphor of a hill, where the climb represents the exploration and learning phase, and the descent represents the building and execution phase.

1. 📈 **Exploration phase** (*climbing the hill*) — This phase is characterized by uncertainty and a lack of clarity. At the beginning of a project, you know less than you will ever know for the rest of the project. You might have false starts and feel like you are climbing up a hill. Tasks in this phase are often granular and not yet organized into higher-level categories.

1. 📉** Building phase** (*running down the hill*) — as the team starts doing real work on the project, they learn how tasks are related and can factor the project into scopes. This phase is more straightforward, as you can see the final form of things and gather inertia as you progress. It feels like you are running down the hill.

It was introduced by the Basecamp guys in [Shape Up](https://basecamp.com/shapeup/3.4-chapter-13).

#### **Pareto** 

We couldn’t wrap up the article without the 80/20 rule. 

Pareto suggests that a minority of inputs (~20%) often leads to the majority of outputs (~80%). E.g.:

- 20% of features bring 80% of the revenues

- 20% of bugs make 80% of the damage

- 20% of a developer’s time brings 80% of the output

In many cases, the best strategy is to identify the 20%, double down on it, and aggressively cut the rest.

### 📚 Resources

Finally, here are some useful links to discover even *more* mental models, or getting deeper into the ones we discussed:

- 📑** **[**Principles and Mental Models for Software Developers**](https://www.adamwaselnuk.com/principles-and-mental-models)** **— a lot of great models listed here, many of whom specific for devs, like YAGNI and Hill Charts.

- 📑 [**Mental Models on Farhnam Street**](https://fs.blog/mental-models/) — FS is a blog and newsletter by Shane Parrish, focused on clear thinking and decision making. It covers many models, and explains them wonderfully.

- 📑 [**Untools**](https://untools.co/)** **— Untools explains several models clearly and succintly. It organizes them into categories, and includes templates and graphics to get you started.
