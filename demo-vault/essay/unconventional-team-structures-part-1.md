---
aliases:
  - "Unconventional team structures (Part 1)"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-essays|Publish Essays →]]"
Status: Everpictured
URL: "https://refactoring.fm/p/unusual-teams-1"
"👓 Status": Not started
"URL 2": "https://twitter.com/lucaronin/status/1556550034971365376"
"Created time": "2024-04-18T14:53:00.000Z"
Date: 2022-08-04
"Has Notes": "[[evergreen/hierarchies-are-useful-to-scale-comms|Hierarchies are useful to scale comms]]"
Tags:
  - Luca
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: f45202b0-16aa-4ed2-a4b0-7572548b42ed
---

# Unconventional team structures (Part 1)

### 📑 Materials

---

[https://blog.coinbase.com/operating-efficiently-at-scale-e6e2378d3d4](https://blog.coinbase.com/operating-efficiently-at-scale-e6e2378d3d4)

[https://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/two-pizza-teams.html](https://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/two-pizza-teams.html)

### 💡 Ideas

---

#### Examples

- Kishan Sampat — **Dimagi** — pods, non-technical managers ([comment1](https://refactoring.circle.so/c/management/what-makes-a-technical-manager-great#comment_wrapper_7889619), [comment2](https://refactoring.circle.so/c/management/what-makes-a-technical-manager-great#comment_wrapper_7889619))

- Spotify

- Michael Genesini

### ✍️ Post

---

A couple of weeks ago I had a chat with a VC who is also a reader of Refactoring. 

We talked of how today you can find high-quality content about how to organize an engineering team, while just 10 years ago, when I founded my startup, things were pretty messy.

This isn’t happening only to engineering teams.

Popular business categories, like SaaS, have now playbooks where the whole organizational structure has been *decoded*, so that,* *based on your company stage, you can get a pretty good ballpark of what your topology and headcount should be.

Such convergence is useful to both companies and individuals. 

- **Companies** — can share vocabulary and best practices, continuously refining them.

- **Employees** — can more easily swap roles between companies, growing their skills and career coherently.

While this incremental approach is mostly for good, it also poses risks. With too much consolidation, we may get trapped in *local optima* and ignore more radical approaches that bring innovation.

What does *radical* look like in this context?

There are successful companies out there that don’t fit the mold. They have unusual configurations, including things like:

- They don’t have managers

- They have people holding multiple, apparently unrelated roles

- They replace key roles with processes

Why is that? Is it just petty rebellion to the status quo or is there substance? What can we learn from them?

This article investigates that, analysing some of the wildest tech companies out there, and extracting lessons for the rest of us.

The goal is to understand and to build a bridge.

- **Understand **— by comparing traditional and unusual structures, we can strive to find universal principles about building great teams.

- **Build a bridge **— can we take single *rebellious* ideas and apply them to our *traditional* team to make it better? I bet so.

This piece is the result of tons of research and multiple interviews to people in some of such companies. To make it easier to read and digest, I will split this edition into two.

In this first one we will cover 👇

- 🏔️ **Hierarchies** — why you get bottle-necked as you scale, and why companies create hierarchical structures.

- 🏃‍♂️ **Autonomous teams** — the holy grail of scaling, with challenges and examples from successful companies like Amazon, Riot, Spotify, and Coinbase.

- 🔍 **Two in-depth case studies **— about Dimagi and ProntoPro: two companies who came up with innovative topologies while still retaining managers and some traditional processes.

In the second one next week we will turn up things to eleven and cover wild companies who gave up most traditional wisdom about organizational structure. We will talk of **self-organizing teams**, holacracy, zero managers, and more.

Let’s go! 👇

### 🏔️ Hierarchies

To understand what’s unusual, we first need to understand what’s usual. Why do team topologies exist, at all?

As long as your team is small, there isn’t much need for a formal organization — 5-10 people teams can work pretty well without much structure.

The main problem, when teams grow larger, is communication. Large teams have a hard time:

- Keeping people on the same page

- Coordinating and allocating resources

- Making good, participated decisions

When you grow your team from 5 people to — e.g. — 15 or 20, it seems that these problems get worse gradually, and then suddenly, to the point of being unbearable without adding more structure. 

But why?

As by the [Metcalfe’s Law](https://en.wikipedia.org/wiki/Metcalfe%27s_law), the complexity of communication is proportional to the *square* of the number of users involved. So, while people grow linearly, complexity grows geometrically.

![image](../assets/5659d3d85f2c44e4.png)

To tame communication complexity, companies usually introduce **hierarchies**. Hierarchies have several advantages:

- They provide **clear communication** paths, ensuring **alignment** is obtained across the organization.

- They reduce the **number of *****lines*** each person has to manage, allowing the company to **scale**.

- They provide a simple way for **making decisions**, by assigning responsibility to people up in the hierarchy.

<details><summary>PICTURE</summary></details>

However, they also bring two main drawbacks:

- **Overhead **—  communication has a longer way to travel to destination, which makes you slower. It also creates all kinds of “work work”, like traffic controlling, managing up, presentations, and more.

- **Inflexibility **— once in place, it is hard to reconfigure roles and processes. Also, to make overhead more bearable, teams start following longer planning cycles, which further reduces agility.

These problems contribute to the so-called *efficiency gap*, as [described by Eiso Kant](https://refactoring.fm/p/from-5-to-250-engineers), experienced by most teams as they scale.

![image](../assets/5eb2ed0cc8b4491a.png)

How do companies fight this?

### 🏃‍♂️ Autonomous teams

Smart tech companies invariably ask themselves the same question as they scale:

> ***If a 5-10 people team can work efficiently without hierarchy, why can’t we just replicate this over and over?***

Organizing a company in small teams, capable of working autonomously, is the holy grail of scaling modern product and engineering work.

While small teams work well at an operational level, though, they still pose challenges. In fact, while staying mostly independent one from another, they still need to:

- **Collaborate well** when needed — because dependencies can never be entirely removed.

- **Preserve alignment** towards wider company goals — independence is granted within a given, agreed scope.

Here are famous examples of big companies built around small, autonomous teams:

#### **Amazon**

Amazon promotes [Two-Pizza](https://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/two-pizza-teams.html) teams since forever. That means, teams should be small enough that people can be fed by two pizzas.

*To avoid confusion among my Italian friends, these are meant to be two large American pizzas, where you basically take two slices of it.*

Two-pizza teams, in practice, means teams of ~8 people or less.

Teams should be fiercely independent the one from another. For Jeff Bezos, the virtues of being small and independent would prevail over some inevitable disorganization that such independence would cause.

![image](../assets/a5813116cdcb45c8.png)

#### Riot Games

As they scaled from 300 to 1000 engineers, Riot Games turned around their culture to focus on [self-managed teams](https://codingsans.com/blog/self-managed-teams).

To foster autonomy, here are some of their advice:

- **Create clear expectations** — writing down clear principles and goals is crucial. You have to be comfortable with people coming up with their own solutions to reach those goals — and you will be so if goals are clear and comprehensive. More on [principles and goals here](https://refactoring.fm/p/principles?s=w). 

- **Coach your employees** — there is more than one way to help people on your team. Rather than being directive in your advice, encourage introspection and help people come up with their own solutions. [Ask questions rather than give answers](https://refactoring.fm/p/growth-relationships).

- **Hire the right people **— high autonomy doesn’t work with everyone. Focus on people who display entrepreneurial mindset and are genuinely thrilled by the sense of ownership. This is especially important for team leaders. 

#### **Coinbase**

Coinbase is re-organizing the company around small pods, [just now](https://blog.coinbase.com/operating-efficiently-at-scale-e6e2378d3d4#:~:text=Organize%20teams%20into%20small%20pods).

Pods are <10-people teams working on some product area. Each pod has a north star metric they work towards, which ties directly into wider company metrics.

If a pod grows larger than 10 people, it gets split into two, and their KPI is also split into two more specific ones.

To make this shift successful, here is what Coinbase is actively promoting:

- **Push decision-making down** — avoid long chains of command and empower the people who have the most visibility into problems to make decisions. Decisions will not be perfect this way, but the obtained speed more than makes up for it. 

- **Create mini P&Ls** — treat product areas as small product by themselves, with their own P&Ls and goals. Allow product leaders to act as CEOs of their respective areas, striving for positive margins and growth.

- **Aggressively reduce dependencies** — reduce the amount of communication needed between teams, without stifling collaboration. For Coinbase, that means developing tons of internal APIs, so that teams can use them directly without ever needing to schedule a meeting.

#### Spotify

Spotify famously popularized the concept of autonomous, cross-functional tech teams back in 2012, with their influential paper “[Scaling Agile](https://blog.crisp.se/wp-content/uploads/2012/11/SpotifyScaling.pdf)”.

They introduced concepts like **Squads**, **Chapters**, and **Tribes**, that are still used by several tech companies today.

While influential, the model is largely incomplete. It doesn’t explain how it solves collaboration and alignment issues, so that many teams struggled at applying it, crippled by the same issues.

For this reason, the model itself [drew criticism](https://www.jeremiahlee.com/posts/failed-squad-goals/) and was often labelled as *aspirational*, with people doubting it had ever been fully in place at Spotify itself.

This is the risk of relying on high-level advice from large, famous companies. We may agree on the principles, but we are still left with a big gap between such principles and their implementation in the real world.

So, to make this piece more actionable, I also interviewed managers in the [Refactoring Community](https://refactoring.substack.com/p/community), working at companies who built original, high-performing structures and processes for their teams.

From there, I wrote two concrete case studies, with two goals:

- 🔍 **Granularity** — Present how things work at a more granular level than what you usually see on companies’ *aspirational blog posts*, including challenges and things that are less than perfect. 

- 🤝 **Relatability** — select companies whose scale might be more relatable than the Spotifys or Amazons of the world. The following two stories are from companies each with around 40-people engineering teams.

Let’s dive in 👇

### Case Study — Dimagi

Dimagi develops tech solutions for impact-driven work, like that of NGOs, governments, and communities. They do so through a suite of no-code tools, SaaS offerings, and bespoke development.

They are a quiet powerhouse that delivered more than 2000 projects for partners like WHO, Save the Children, and the Bill & Melinda Gates Foundation. 

I interviewed [Kishan Sampat](https://www.linkedin.com/in/kishan-sampat/?originalSubdomain=in), Engineering Manager at Dimagi, who has been working there for 6+ years, and watched the company grow from less than 10 devs to more than 40 today.

Kishan tells me that, at the beginning, **everybody was doing everything**. Somebody might do both product dev and security, while also talking with customers.

As the team grew, they got three main problems:

- **Technical Debt** — tech got messier and velocity got clearly slowed down by debt.

- **Turnover** — more people started joining and leaving. Without much organization, people who left took knowledge away with them, and those who joined had a hard time onboarding properly. 

- **Planning** — prioritising and allocating resources took more and more time, while also becoming less effective. On top of this, when a product person left it could spell disaster for their product area, that would be neglected for months.

To solve this, they started organizing their team in pods 👇

#### Pods

A pod is a team made of less than 10 engineers. Pods have two main characteristics:

- **You can join more than one **— devs can be members of more than one pod. Usually between one and five.

- **They can be either vertical or horizontal** — there are vertical pods for specific product areas, and horizontal pods that resemble more traditional functions, like frontend, security, and high availability.

Each pod has a Tech Lead and an Engineering Manager.

- **Tech Leads** — guide the technical direction and define the work to be done to move the pod forward.

- **Engineering Managers** — negotiate the strategy with the Tech Lead, look for resources to allocate in the pod, and do people management.

Tech Leads are usually 100% dedicated to their pod, while managers might oversee more than one pod at the same time.

Devs rotate frequently across the various pods, to encourage knowledge sharing and follow personal inclinations. Tech Leads rotate less frequently, but might still change pod every few quarters.

#### Planning

Dimagi does quarterly OKRs. Company goals cascade down to pods goals, from which initiatives are created to meet such goals. 

Initiatives are estimated roughly, and people are allocated across the pods accordingly.

#### Lessons

The Dimagi approach is refreshing. To me, there are especially two things they get right: 

**1) “Buddy” relationship between EM and TL** — separating the manager role from the tech lead one is powerful. By working on the same team, they can perform their respective functions and act as *buddies*, sustaining each other. 

A dedicated TL also reduces the need to have highly technical EMs. In fact, several EMs at Dimagi (including Kishan) are non-technical. In Kishan’s own words 👇

> *We have adopted this model after chatting with engineers about their interests and we had most members who were purely interested in technical work only and not performing other managerial functions. We had non-technical leads like me working on the support team and QA team, who were interested in further pursuing a management role, and therefore we created this hybrid model, which has been working well I would say.*

**2) Roles instead of jobs** — keeping the same structure (pods) for vertical and horizontal work is brilliant to make sure nothing gets neglected. It gives the company a simple framework for defining its priorities (create pods for them) and allocating resources.

It also makes it simple for people to rotate across different things, in an intentional way. People could express their inclination to work in some specific pods, and management could try to accomodate those whenever possible.

Finally, it allows people to have *roles* instead of *jobs*, possibly allowing them to allocate the full spectrum of their abilities, instead of doing just one thing all the time. 

#### Challenges

This structure also poses challenges. From my perspective, here are the main ones:

**1) Staffing pods every quarter is expensive** — as the company grows larger, it will become more and more expensive to sit down every quarter and negotiate the full allocation of all the pods. While such reshuffle brings agility in deciding what to work on, it also creates overhead from negotiating with all the stakeholders. 

A likely evolution is to gradually take the areas that have the most constant, predictable work, and turn them into *permanent pods*, with more long-standing staff that rotates less frequently. Since the work is predictable, we can trade some agility for faster planning. 

**2) Working in multiple pods brings overhead**

For the overlapping pods to be a net positive to the final company output, it is crucial to keep their processes nimble and bring minimal overhead to people’s work.

In the worst case, imagine someone working in three teams who has to attend three times the meetings and ceremonies.

Here are some tactics to keep things snappy:

- **Default to written communication **— turn all status updates into async and have meetings only for [complex, urgent, or personal matters](https://refactoring.fm/i/36143627/-the-cup-rule-for-good-meetings).

- **Create stable allocations **— establish in advance the breakdown of devs’ time between the various roles. At my startup, we intentionally spent 70% of time on new features, and 30% on maintenance. The same could be done with pods allocation. Having hard numbers simplifies planning and makes people happier.

### Case Study — ProntoPro

ProntoPro is the largest marketplace for professional services in Italy, and one of the largest in Europe. Almost 700k professionals work on the platform, serving 5M+ customers.

I sit down with [Michael Genesini](https://www.linkedin.com/in/michaelgenesini/?originalSubdomain=it), Engineering Manager, to chat about how they work.

What makes ProntoPro interesting to me is the fact that they blend two popular methodologies: the forementioned Spotify Model, and [Shape Up](https://basecamp.com/shapeup), by Basecamp.

These frameworks work well together because they are complementary:

- The **Spotify Model** mostly focuses on **team topology** — without much advice on processes or how people should work together (which is where they drew the most criticism).

- **Shape Up **is mostly about **process** and **work cycles** — without being prescriptive on how you should structure your team.

So how does this work?

#### Chapters

ProntoPro’s engineering department is made of 32 engineers.

These are organized into *chapters*, which is Spotify’s codename for functions. ProntoPro has chapters for frontend, backend, data, QA, and SRE.

Each chapter has at least one lead and one manager. Large chapters may require more than one manager — e.g. frontend, with 11 devs, has 2 EMs. Conversely, when the chapter is small enough (e.g. QA with 4 devs), the chapter lead may also act as EM.

How do these chapters work together?

#### Process

Shape Up works in 8-weeks cycles: 6 weeks of dev work, followed by 2 weeks of *cool-down* for maintenance and planning.

Every 8 weeks, ProntoPro places [*bets*](https://basecamp.com/shapeup/2.1-chapter-07)* *(projects), whose complexity is expressed in just three sizes: tiny (1 week), small (3 weeks), big (6 weeks).

Based on this, they assemble *squads* (cross-functional teams) taking people from the various chapters, and assigning them the bets.

Engineering Managers take part in the building phase during the first weeks. Later, they partner with product managers to plan the next features, while also performing their people management duties.

#### Lessons

Micheal told me they didn’t start this way. They built this process to be more flexible and resilient:

> *In the past, we had fixed cross-functional teams with a tech lead on each of them. This was not sustainable. […] We were also not very resilient as a department, so even losing a single member was a pain that caused a reorganization every time.

With the current model, we are definitely more resilient in terms of teams because we adapt the capacity on every cycle. Moreover, we can scale more easily than before because we don't need a fully formed team to increase the final throughput.*

These thoughts echo those of Kishan about Dimagi. As long as your team is small, the benefits of being able to adapt capacity on a frequent basis overcome the overhead brought by resource allocation.

ProntoPro further reduces this overhead by having only three, standard sizes for projects, which simplifies estimation.

Also, rotating people is not only about agility — it makes you share knowledge across the team, you reduce* single points of failure*, and help people keep growing by working on various parts of the product.

#### Challenges

Again, this process is probably sustainable as long as the squads to be assembled each time are few (currently 4-5).

Creating 10-15 squads from scratch, every 8 weeks, would likely bring unbearable overhead and take a big toll on managers. At that point, it may become more convenient to identify some stable areas of allocation, and assign part of the engineering team to durable cross-functional teams — the same that where out of place when the company had a smaller scale.

---

And that’s it for this week! 

The next article will continue this conversation with more case studies, focusing on **the rebels** — wild companies who gave up most traditional wisdom about organizational structure!

We will talk of **self-organizing teams**, holacracy, zero managers, and more.

### 📚 Resources
