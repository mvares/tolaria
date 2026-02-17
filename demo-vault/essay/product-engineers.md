---
aliases:
  - "Product Engineers"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-essays|Publish Essays →]]"
Status: Evergreened
URL: "https://refactoring.fm/p/product-engineers"
"👓 Status": Not started
"Created time": "2024-04-18T14:53:00.000Z"
Date: 2022-04-14
"Has Notes":
  - "[[evergreen/assign-ownership-to-develop-engineers-autonomy|Assign ownership to develop engineers’ autonomy]]"
  - "[[evergreen/create-a-feedback-loop-for-engineers|Create a feedback loop for Engineers]]"
  - "[[evergreen/the-rise-of-product-engineers|The Rise of Product Engineers]]"
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: cc46b8f5-2253-48f9-8d3c-e6b16a5297e7
---

# Product Engineers

### 📌 Outline

### ✍️ Post

---

There are many ways to classify engineers, based on their skills and attitude. 

One of the most interesting, to me, is the separation between those who mostly focus on **technical excellence**, and those who love to be engaged in **user problems** and UX.

The latter is more common with frontend developers because of the nature of their work, but I have learned over time that this is more a cultural separation than a technical one.

There are people who are mostly driven by **impact**, and others who care more about **mastering their craft**. Keep in mind, these are not rigid categories. It is a spectrum, and everyone falls somewhere on it.

Now, while there is a personal component to begin with, **company culture** has a strong impact on shaping this tradeoff and how people think about their work.

Startups and product-centric companies, for example, tend to embrace a culture of ownership where engineers have ample autonomy in designing solutions for customers. 

They fall more on the *impact* side of the spectrum.

Fostering an engineering culture based on impact has many advantages:

- **Alignment** — company goals are aligned with teams’ and people’s goals.

- **Autonomy** — alignment makes autonomy easier. You can trust people to take non-trivial decisions on their own.

- **Ownership** — autonomy turns people into owners of their work. This in turn has a strong effect on their motivation and personal growth.

It works.

For this reason, more and more engineering roles are now identified by their **area of impact** (e.g. *Product Engineer*, *Customer Success Engineer*), rather than their technical **platform** (e.g. *Frontend Engineer*, *Backend Engineer*).

Out of these, the **Product Engineer** role is the most representative of this shift and has become a staple in successful companies like Stripe, Intercom, Atlassian, and more. For example, here is how [Intercom](https://intercom.com/) defines it 👇

> *As a product engineer, you’ll be taking ownership of real customer problems by building smart, efficient solutions to both back-end and front-end systems. There are projects for you to own in multiple areas, such as our messenger, bots, rule matching, deliverability, security, app availability, machine learning, and more.*

Does this work for every company, though?

This article helps you navigate this shift by covering why we got here, what it looks like in practice, and whether it can be useful to you. We will talk about:

- 🤔 **Why Product Engineers? **— Let’s clear up the confusion between Product Managers, Product Owners, Product Engineers, and figure out what each one really does. 

- ⚖️ **Does it work for you?** — Design the best strategy based on your business, product stage, company size, and more.

- 🔀 **How to turn engineers into product engineers? **— Practical advice to steer your company culture towards autonomy and impact.

- 📚 **Resources **— real-world case studies taken from the Refactoring community, and the best readings to learn more.

Let’s dive in 👇

### 🤔 Why Product Engineers?

The push for Product Engineers fits a broader trend in making product / tech roles *wider* and give people more ownership and autonomy. 

To me, the Engineers vs Product Engineers feud resembles the one between Product Owners and Product Managers.

- **Product Owners** have *tactical* responsibilities. They *groom* the backlog, write user stories, prioritize what to do next, and attend all the Agile meetings. Their focus is short to mid-term.

- **Product Managers **have *strategic* responsibilities. There is overlap with Product Owners about how they both shape what to do next, but PMs are also responsible for the product vision and success metrics. Their focus is mid to long-term.

![image](../assets/e468dc8634ad4e19.png)

In PM-based teams, there is the opportunity for engineers to step in and take some of the POs duties that PMs are not going to cover.

In fact, in high-performing teams, PMs provide direction and support but leave Engineers in charge of creating tickets and managing actual tasks. Requirements focus on outcomes, rather than how to explicitly build stuff, leaving Engineers free to make decisions that matter.

![image](../assets/491a876976ff4d53.png)

This culture promotes ownership and enables personal growth.

Would this work in your company, though?

### ⚖️ Does it work in your company?

If your business revolves around a product, the answer is **most probably yes***. *

Giving more autonomy and responsibilities to Engineers stays solid advice whatever your company stage is 👇

#### Small startups

Early stage startups benefit from hiring *generalist *Engineers who can own features from top to bottom.

[Bjorn Wahle](https://www.linkedin.com/in/bj%C3%B6rn-wahle-b5307a60), Engineering Manager, says:

> *I have worked in 2-3 startups already where no dedicated Product Manager / Owner or UX Designer was present and then the Product Design basically happened between CEO / Sales and engineers: CEO / Sales figure out the needs for the product by talking to (potential) clients and translate that in quite unspecified and broad feature requests that would be handed to the engineers. 

Simple design sketches usually come from CEO / Sales, but the detail work of figuring out the exact specifications and the desired UX would often fall on the (front-end) engineers plate.*

[Corvin Deboeser](https://twitter.com/CorvinDeboeser), Founder and Data Engineer, also weighted on this:

> *In most early stage startups, there is no budget for a PM, a product designer, user researcher etc. What sets the great founders apart, however, is that they are aware that they won't be able to carry the product function for long and are willing to hand it over (at least partially). That also makes it necessary to intentionally hire for a "Swiss army knife" or Product Engineer.*

#### Large companies

Even larger companies, though, although they have more *specialists* on board, can still create teams where PMs empower Engineers to do their best work.

Ben’s experience at Facebook is indicative 👇

[Embed](https://twitter.com/viableben/status/1420495389770145795)

Ben was criticised for this tweet, with people interpreting it as a sign of PMs not doing meaningful work.

This is not the case.

The best managers are good at 1) hiring, 2) creating alignment, and 3) getting out of the way to let people do their best work. This is what we should all aspire to.

#### When doesn’t it work?

There are situations where it is harder for Engineers to provide meaningful product input.

- **Software agencies **often work on projects where the level of trust from the client is lower than regular product companies. This may lead to *waterfall-ish* processes where Engineers have less room for manoeuvre*.*

- **Corporate products** might be more sales-driven and make it hard for Engineers to get customer feedback and come up with meaningful input.

### 🔀 How to turn Engineers into Product Engineers

How can you build a culture that rewards Engineers’ autonomy and product input? Here are some tactics:

- 👑 **Assign ownership**

- 🎯 **Define success**

- 🔄 **Establish feedback loop**

- 🚫 **Leave room to do wrong**

Let’s see them one by one.

#### 👑 Assign ownership

For each new feature, consider assigning an engineer as **tech owner**. It doesn’t need to be the Tech Lead / EM — you may rotate such role across engineers in your team, based on the different features.

Owners are involved in the design from the very beginning. They provide direction and are later on are responsible for delivering the feature.

[Yurii Mykytyn](https://www.linkedin.com/in/meakovski/), Director of Engineer, applied this tactic successfully and told us how he did it 👇 

> *The feature owner is a tech person responsible, from the very beginning, for:
– spending time with UX, product and stakeholders
– validating the designs & making sure that they are feasible
– decomposing abstract feature into manageable chunks
– facilitating architecture discussions
– communicating specific tasks and coordinating the development of the whole feature.

Effectively everyone could be a project manager for any feature. This is a voluntary role, taken on a feature initiation (pre UX) stage. This had worked exceptionally well, freeing me up from team lead duties, and giving more ownership to developers, allowing them to exercise product mindset and leadership.*

#### 🎯 Define success

To make people focus on impact they should know what impact looks like. This is two-fold:

- **Company Goals **— what does success look like for the* ***business**? Shared company goals let people come up with their own ideas [...] 

- **Feature KPIs** — what does success look like for the **feature**? Are we measuring revenues? Usage? 

Whether you use OKRs or other frameworks, make sure people are on the same page about the outcome you want to achieve.

[Corvin Deboeser](https://twitter.com/CorvinDeboeser), Founder & Data Engineer, recalls how they did it in Celonis 👇

> *In Celonis (when the engineering team had ~80 people), we had this wonderful culture where all engineers would understand their impact on the customer – even the ones who built the heavy process mining algorithms or who were responsible for internal data and build infra. 

The reasons: (1) Every SWE was involved in ideation sessions and (2) Every team was managed by a PM that would reinforce the customer centricity and direct the goals team towards customer impact.*

#### 🔄 Establish a feedback loop

Expose engineers to the outcome of their work by creating an effective feedback loop.

One of the simplest ways to do this is by making them talk with customers. [Kareem Amin](https://twitter.com/kareemamin), CEO at Clay, explained to me how *all* their engineers do so 👇 

> *Customer success engineers spend 80% of the time talking to customers, and 20% of the time coding. Software Engineers, in turn, spend 80% of the time coding, and 20% talking to customers. This helps clarify that people should not be siloed. It’s not that everyone should do everything — it’s about the proportion of how you spend your time.*

There are other ways, too. You may expose feature owners to usage metrics, support tickets, data from user interviews, and more. Basically, anything that is useful to get insights about the feature performance.

### 📚 Resources

- 📑 [**Product Engineers**](https://sherifmansour.medium.com/product-engineers-f424da766871) – Sherif Mansour explains the key role of Product Engineers in a product team. It also enumerates their main characteristics and how to support them as a PM. 

- 📑 [**The Product-Minded Software Engineer**](https://blog.pragmaticengineer.com/the-product-minded-engineer/) – Gergely Orosz articulates the key traits of product-minded engineers and gives out tips on how you can become one.

- 📑 [**Product Owner vs Product Manager**](https://www.productboard.com/blog/product-owner-vs-product-manager/) – Good article that explains the main differences between the PO and PM role, by the folks at Productboard. 
