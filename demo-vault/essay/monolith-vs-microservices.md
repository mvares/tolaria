---
aliases:
  - "Monolith vs Microservices"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-essays|Publish Essays →]]"
Status: Evergreened
URL: "https://refactoring.fm/p/monoliths-vs-microservices"
"👓 Status": Not started
"Date HH": 2025-06-19
"Created time": "2024-04-18T14:53:00.000Z"
Date: 2022-10-13
"Has Notes":
  - "[[evergreen/benefits-of-microservices-are-organizational|Benefits of microservices are organizational]]"
  - "[[evergreen/good-microservices-start-with-good-monoliths|Good microservices start with good monoliths]]"
  - "[[evergreen/microservices-are-high-maintenance|Microservices are high maintenance]]"
  - "[[evergreen/microservices-help-with-fault-tolerance|Microservices help with fault tolerance]]"
  - "[[evergreen/microservices-help-with-continuous-delivery|Microservices help with continuous delivery]]"
  - "[[evergreen/microservices-are-hard-to-design-because-of-network-calls|Microservices are hard to design because of network calls]]"
  - "[[evergreen/microservices-are-not-necessarily-more-scalable-than-monoliths|Microservices are not necessarily more scalable than monoliths]]"
  - "[[evergreen/hunters-vs-farmers|Hunters vs Farmers]]"
  - "[[evergreen/the-strangler-pattern|The Strangler Pattern]]"
  - "[[evergreen/galls-law|Gall's Law]]"
Tags:
  - Luca
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 8f2eea00-ee9f-4394-b6ed-c8d5582b07b3
---

# Monolith vs Microservices

### 📑 Materials

---

### 💡 Ideas

---

<details><summary>Hunter gatherer vs farmer</summary></details>

<details><summary>[Untitled](https://www.notion.so/5c13a2221ea1458eb50f86b8f2706c72)</summary></details>

- Microservices

- Four categories — Modularity vs Number of deployment units (Shopify)

- Design payoff

- Productivity

#### Community

<details><summary>✅ [Brendan Mulholland](https://www.linkedin.com/in/brendanmulholland1/?originalSubdomain=de) — hardest problem factoring systems + **network calls**.  Bad for startups because of **fast moving**</summary></details>

<details><summary>❌ [Chris](https://twitter.com/christopheek) — no silver bullet, they have their place</summary></details>

<details><summary>✅ Jeremie Bortier — migrate piece by piece. Benefit = **independent releases**</summary></details>

<details><summary>✅ [Juliette Chevalier](https://twitter.com/_juliettech) — depends on the **skills** of your team. Microservices = bad **discoverability**</summary></details>

<details><summary>✅ [Daniele Salvatore](https://twitter.com/_dani_salv) — microservices additional complexity. **Strangler pattern for migration**</summary></details>

<details><summary>✅ [Nikita Logachev](https://www.linkedin.com/in/nikita-logachev/?originalSubdomain=cz) — full case study</summary></details>

---

<details><summary>**Pictures**</summary></details>

### ✍️ Post

---

In the book [Sapiens](https://www.goodreads.com/book/show/23692271-sapiens), historian Yuval Noah Harari spends some initial chapters explaining the transition of humans from the *hunter-gatherer *lifestyle, to the *farmer* one.

In doing so, he debunks several myths about the life of prehistoric men.

Hunter-gatherers lived a simple, happy life: they had a diverse diet, famine was rare, they were physically fit, and, contrary to popular belief, they only had to work a few hours a day.

The transition to farming, instead, brought some [unexpected setbacks](https://web.cs.ucdavis.edu/~rogaway/classes/188/materials/diamond). Farmers had to work long hours, sometimes twice as much as their hunter ancestors did. Their health got worse because of intense work, bad diet (mainly carbs), and diseases brought by the poor hygiene of primordial villages.

The farmer lifestyle had one main upside, though: it could produce *more food*, which would sustain the creation of larger communities.

In other words, life sucked at pretty much everything, but hey — it was scalable now!

Does it remind you of anything? 

The first farmers were pretty much the engineers of the prehistoric world. To their defense, nobody chose to made their own life worse *on purpose* — on paper, odds where *overwhelmingly *in favour of the farming life. Most downsides were not obvious (e.g. diseases, diet problems) and wouldn’t be so until generations later.

Many big engineering choices are similar. Implications are far reaching, and we may fail to account for the second and third-order consequences.

![image](../assets/8231612ac0a74f2a.png)

One of the most divisive of such choices is about **monoliths vs microservices**.

This article tries to shed light into the tradeoffs, upsides and downsides of adopting one of such architectures (and solutions in between), both from the technical and organizational point of view.

We will go through:

- 📖 **Definitions **— Monoliths, microservices, and everything in between

- ✏️ **System Design **— How is design effort different? And when is it worth it?

- 📈 **Scalability **— Do microservices scale better than monoliths? Well, it’s complicated.

- 🚚** Productivity **— How does your dev process changes based on your architecture? 

- 🔍 **Case Studies **— Three real-world stories of evolving monoliths and microservices

- ⚖️ **How to decide **— Let’s bottom-line all of this and figure out what’s best for you

Let’s go!

### 📖 Definitions

In system design, a **monolith** is a configuration where all functionality lives in a single service. Such service is tested and deployed as a single unit.

With **microservices**, instead, features are delivered by combining many single-purpose, independent network services. Each service can be tested, deployed, and scaled in isolation.

These are of course, two *extremes.*

Real world architectures often live on a *spectrum* between these. You may have monoliths that cover most features, with a few ones provided by independent services, or compositions of microservices where some of them are anything but *micro*.

Unfortunately, it is easier to give names to extremes than to anything more nuanced — but the best solutions often lie in between. 

How do people choose one vs the other? Let’s start with system design 👇

### ✏️ System Design

Most systems start as monoliths, because they are arguably easier to design. 

In a monolith, you don’t have to necessarily think at how to factor things precisely, because all the code lives in a single place and can be referenced easily.

Microservices, instead, interact via network calls. Interaction via network is expensive and hard to reconfigure — so you better be sure about how you split functionality.

[Grug](https://grugbrain.dev/#grug-on-microservices) said it best:

> *grug wonder why big brain take hardest problem, factoring system correctly, and introduce network call too*

Design complexity makes microservices less than ideal in situations where the problem scope is unclear or fast moving — like a startup. Monoliths, instead, pay a lesser price for a wrong abstraction, because they can be more easily reconfigured.

Brendan Mulholland, CTO at Recital, describes it well:

> *The more complex the boundary, the harder it is to move -- and the o11y, security, decoupling, etc, you describe is all complexity on top of a network call. That's also why microservices are so dangerous for a startup: if the architecture of your system (indeed, even your business domain) are still emerging, how likely are the boundaries to be correct?*

But does this design tax repay itself in other ways? Let’s see 👇

### 📈 Scalability

Scalability is often mentioned as one of the key upsides of microservice architectures.

In my experience this is not always true. Let’s separate two qualities: short-term and long-term scalability.

#### **Short-term scalability**

That means resilience to load peaks. 

Since microservices are faster to spawn than the full monolith, you can be more responsive at acting on spikes. However, microservices spikes also tend to be more *brutal* than monolith ones. 

Think about that: let’s say you have 10 API endpoints, and 2 of them at some point get a 5x traffic spike. If each endpoint lives in a separate service, you have to scale the capacity of the two services 5x. That might not be trivial, especially if you need to do it *fast*.

Viceversa, if all the endpoints live in a single monolith, the impact on the overall load is lower and can be more easily absorbed.

There isn’t a clear winner here — it depends on your load patterns.

#### Long-term scalability

Let’s say your product is successful and traffic grows consistently over time. How mileage do you have with a monolith vs microservices?

Again, it depends.

A monolith might be straightforward to scale vertically for a *long *time. Also, regular web apps can go a long way by spinning off the database on a dedicated instance, scale that vertically, and scale the rest horizontally with jobs and queues.

How does that compare to scaling microservices?

Since each service has a different load pattern, in theory you can scale them more precisely and get to a solution that is better and cheaper. In reality, though, this is hard to pull of.

Since each service has a different CPU, memory, and load profile, each also scales in a different way. Spending more engineering time on such maintenance easily eats up, cost-wise, all the other benefits you can get.

#### What about serverless?

It is true that Serverless microservices can be truly seamless (and cheap) to scale for various orders of magnitude. However, they also need to be very small size, which puts additional constraints on your design.

Databases are also still tricky to make properly serverless — some native solutions do exist, though, like [Planetscale](https://planetscale.com/). 

Generally, the more services your system is split into, the more rigid the design and the harder to riconfigure in the future. If you are able to pull this off, you get scalability out of the box, but you should pay attention to the risk-reward ratio.

### 🚚 Productivity

In engineering, [how fast and often you are able to ship](https://refactoring.fm/p/how-shipping-fast-changes-your-life) is a good proxy for productivity. 

Let’s cover how monoliths vs microservices affect this.

#### Continuous Delivery

Monolith deploys are generally longer and riskier, because everything goes up together.

If tests break for one thing, they break for everything, which blocks all that should be released, even unrelated stuff. This is a classic [issue with shared staging environments](https://refactoring.fm/p/do-you-need-staging).

Microservices bring isolated tests and releases, which is a usually win for continuous deployment.

Jeremie Bortier told the community how moving to microservices improved his company pipeline 👇

> *Two years ago, we moved from a monolith to a lighter monolith mixed with microservices.*

Making it easier to have small, isolated releases is probably the best upside of microservices, especially as your org grows large. Different teams can take ownership of different services, avoid step onto each other’s toes, and keep the pace of development high.

This is how, for example, Coinbase is restructuring itself [just recently](https://www.coinbase.com/blog/operating-efficiently-at-scale#:~:text=building%20better%20products.-,APIs%20instead%20of%20meetings,-Larger%20companies%20also), and how Amazon has been run since… almost forever. In 2002 Jeff Bezos sent the following memo to employees, which got known as “**The API Mandate**”:

> *1. All teams will henceforth expose their data and functionality through service interfaces.
2. Teams must communicate with each other through these interfaces.
3. There will be no other form of interprocess communication allowed: no direct linking, no direct reads of another team’s data store, no shared-memory model, no back-doors whatsoever. The only communication allowed is via service interface calls over the network.
4. It doesn’t matter what technology they use. HTTP, Corba, Pubsub, custom protocols — doesn’t matter.
5. All service interfaces, without exception, must be designed from the ground up to be externalizable. That is to say, the team must plan and design to be able to expose the interface to developers in the outside world. No exceptions.
6. Anyone who doesn’t do this will be fired.
7. Thank you; have a nice day!*

We all nod at the Bezos mandate and the Coinbase story, but there are two caveats. You only benefit from this organization if:

1. **Your team is fairly large **— how large? To the point where that coordination and discoverability of code is a meaningful problem. Team communication generally [doesn’t scale](https://en.wikipedia.org/wiki/Metcalfe%27s_law) well, so you get to a point where the overhead introduced by running and maintaining independent services is preferable to that of endless meetings for coordination. 

1. **Your services are truly independent** — so that they can always* *be released in isolation. Viceversa, if they are highly coupled and you need to coordinate concurrent releases, you are better of with monolithic deploys.

#### Fault tolerance

Common sense says that, by enforcing strong boundaries, microservices should help with **fault isolation**. 

While this is true, it is also true that nothing stops you from designing monolith components that are just as low-coupled and isolated. That shines especially for **runtime errors**: handling them for services over the network is arguably more complex than for components of a single service.

Microservices, however, keep an edge at isolating **infrastructure-related faults**. Things like memory leaks or CPU spikes are easier to track down inside individual services than in a single monolith.

#### Maintenance

Microservices come with higher maintenance. Many teams fail to account for this because we are not talking of a few big items that stand out, but rather death by a thousand cuts. For example:

- **Dependencies** — you need to coordinate dependencies and versioning across multiple places, instead of a single one.

- **Monitoring **— staying on top of tens of different services, each with their own load, CPU and memory profiles, is arguably heavier than keeping tabs on a single service.

- **Discoverability **— making services discoverable and usable by people requires more documentation work than components in a monolith.

[Juliette Chevalier](https://twitter.com/_juliettech), developer advocate at Aragon, weighs in on discoverability 👇

> *Microservices are great for flexibility and isolation, but can increase complexity within the codebase, especially for teams that may not be inherently full-stack. 

For ex, a React developer working on a Ruby on Rails monolith will find the right API functions intuitively as long as she/he has done it once, whereas a React dev working on evolving microservices will have a harder time knowing where x call lives. The latter requires a bigger commitment to keep documentation updated and to be extensive so new team members can quickly catch on.*

### 🔍 Case Studies

If you had enough of the theory, here are the three best case studies I know of about moving between monoliths and microservices 👇

- 📑 [**Segment: Goodbye Microservices**](https://segment.com/blog/goodbye-microservices/) — Segment went from monolith to microservices and back, and wrote a fantastic article about the challenges, opportunities and lessons learned along the way.

- 📑 [**Shopify: Deconstructing the Monolith**](https://shopify.engineering/deconstructing-monolith-designing-software-maximizes-developer-productivity)** **— Shopify took a different approach and gradually turned their monolith into a *modular monolith. *The linked article contains plenty of details about how they managed dependencies and boundaries to enforce modularity.

- 📑 [**Scaling a SaaS to $3M/year on the back of a monolith**](/c01b8f5d644f484cadadb02233342cab)** **— A detailed write-up by [Nikita Logachev](https://www.linkedin.com/in/nikita-logachev/?originalSubdomain=cz), VP of Engineering at Omniscope, about the technical issues and choices he faced as a CTO needing to scale a bootstrapped SaaS business multiple folds.

### ⚖️ How to decide

Consider the [Gall's Law](https://en.wikipedia.org/wiki/John_Gall_(author)):

> *A complex system that works is invariably found to have evolved from a simple system that worked. A complex system designed from scratch never works and cannot be patched up to make it work. You have to start over with a working simple system.*

Paraphrasing it, good microservices’ designs are invariably found to have evolved from good monolith designs.

Likewise, if your monolith looks like spaghetti, moving to microservices will not magically fix it. Rather, it will turn it into a **distributed spaghetti**, making problems worse.

![image](../assets/a9be7a9bf6884008.png)

The Shopify case study is enlightening as it considers two main coordinates: **Modularity** and **Deployment Units**.

**1) Modularity** — this is the primary virtue you want to achieve. Most qualities brought by good microservices can also be achieved with a modular monolith. Modularity brings easier coordination, better fault isolation, and generally better maintainability.

**2) Deployment Units **— as a rule of thumb, the more things you need to deploy, the more complex your system becomes. Other things being equal, you want to keep this number low.

Overall, the benefits of isolated services vs a modular monolith seem to be mostly organizational, rather than technical.

As by the [Conway’s Law](https://refactoring.fm/i/71307178/conways-law), your software design structure gets eventually shaped around your team’s communication structure. If your team is large and you want to organize it around small independent teams, you may eventually gravitate towards a service-based architecture. 

![image](../assets/2da1e9efcd284ea1.png)

The opposite is also true: you won’t probably get the full benefits of microservices as long as your team stays a single large unit. The overhead will not be worth it if it is not matched by the communication benefits brought by autonomous teams.

It seems to me that a solid recipe for any team might be to focus on modularity, and spin off independent services when you want to enable equally independent workflows, rather than (supposed) stronger technical qualities.
