---
aliases:
  - "Monday #52"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-monday-idea|Publish Monday Idea]]"
Status: Published
"👓 Status": Not started
"Created time": "2024-04-18T15:09:00.000Z"
Date: 2023-05-22
"Has Notes":
  - "[[evergreen/path-to-production-mapping|Path-to-production Mapping]]"
  - "[[RACI Chain / Matrix]]"
  - "[[evergreen/commenting-code-is-good|Commenting code is good]]"
Tags:
  - Monday
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: b3332743-2e32-42e8-b9a5-7fe0800659fd
---

# Monday #52

*Hey, *[*Luca*](https://twitter.com/lucaronin)* here! welcome to the ****Monday 3-2-1 ****✨*

*Every Monday I will send you an email like this with ****3 short ideas**** about engineering management, technical strategy, and good hiring.*

*You will also receive the regular long-form one on Thursday, like the last one:*

- [**Performance Reviews**](https://refactoring.fm/p/performance-reviews)** 🏅**

*To receive all the full articles and support Refactoring, consider subscribing if you haven’t already!*

Become a better tech leader today ✨

[https://refactoring.substack.com/subscribe](https://refactoring.substack.com/subscribe)?

*p.s. you can learn more about the *[*benefits of the paid plan here*](http://refactoring.fm/about)*.*

---

![image](../assets/772687e7a5954154.png)

---

### 🤖 [New Relic Grok](https://newrelic.com/grok?utm_source=refactoring&utm_medium=community&utm_campaign=global-fy-24-q1-grok-early-access-refactoring)

Before we dive into this week’s ideas, I am happy to spread the word about the launch of [**New Relic Grok**](https://newrelic.com/grok?utm_source=refactoring&utm_medium=community&utm_campaign=global-fy-24-q1-grok-early-access-refactoring), the first generative AI assistant for observability.

New Relic Grok makes it easy to get the insights you need without having to make sense of tons of data.

![image](../assets/3400b6bd49034a50.png)

It leverages OpenAI’s large language models (LLMs) so that any engineer can use plain language and a familiar chat interface to ask questions and get insights, without prior observability experience. Observability is now as simple as asking, “*Why is my cart not working?*” or “*Instrument AWS*.”

Grok is in early access stage. As a Refactoring subscriber, you get priority! You can apply below 👇

Request early access

[https://newrelic.com/grok?utm_source=refactoring&utm_medium=community&utm_campaign=global-fy-24-q1-grok-early-access-refactoring](https://newrelic.com/grok?utm_source=refactoring&utm_medium=community&utm_campaign=global-fy-24-q1-grok-early-access-refactoring)

---

### 1) 🪚 Use RACI to unbundle meetings

I believe work meetings have three main goals:

1. 📃 **Sharing info** — for status update. As you do in a sprint review, or when you demo new features to stakeholders.

1. 🎲 **Making decisions** — for when you need to decide how to move forward. E.g. in a planning meeting when you prioritize stuff and decide what to work on next week.

1. 🧱 **Creating stuff** — brainstormings, design sessions, problem solving, and anything where something gets *created* through the collaboration of the participants.

These goals live on an ideal line that goes from mostly passive/unidirectional communication, to mostly active/multidirectional.

More simply, it goes from status to action 👇

![Different meeting goals, ranging from mostly status to mostly action. ](../assets/dc5943154663412b.png)

Just like there are different kinds of meetings, there are different kinds of attendees 👇

#### RACI Chain

The RACI chain is a popular tool to identify the various roles of people in a process. It works well for meetings as well. RACI pits people into four categories:

- 🔨 **Responsible **— those who actually do the job.

- 👑 **Accountable **— those who ultimately sign off the job and are answerable for it.

- 🤝 **Consulted **— those whose opinions are sought but do not work directly on the job.

- 📣 **Informed **— those who are kept up-to-date on the status of the job.

If you think about them as meeting attendees, it’s easy to see that each role is interested in different things:

- 📣 Informed** **people are interested in **status**. They don’t make decisions nor participate in doing stuff.

- 👑 Accountable people **make decisions **and need **status **to do so. But they don’t join the creation process.

- 🔨 Responsible** **people don’t need info (they provide it to others). They usually join the **decision making**, and also **build stuff** themselves.

- 🤝 Consulted** **people don’t need info and don’t participate the decision making, but are involved in the **building** part as domain experts.

![image](../assets/e38edc730a8549f3.png)

Based on this, I believe in two strategies:

1. 🪚 **Unbundle meetings **— most meetings do not belong to a single *type: *they are a mix of many, because they need to be useful to different stakeholders. Rather than removing a meeting altogether, you can remove some parts (and some attendees), to make the rest shorter and more cohesive, so that nobody thinks they are wasting their time.

1. 🏃 **Use meetings for *****action ****— *meetings have *high bandwidth*. The best use of such bandwidth is for *creating* things and solving problems, rather than sharing information. The latter can usually be done asynchronously just as well.

So, the best way to reduce meetings is to 1) split them into parts, and 2) remove / make async those that are mostly about status.

You can find more ideas and examples about how to reduce meetings in this recent Refactoring article 👇

[https://refactoring.fm/p/how-to-remove-meetings](https://refactoring.fm/p/how-to-remove-meetings)

---

### 2) 🗺️ Path-to-Production Mapping

Path-to-production mapping is a practice where teams map all the steps of the release process, in order to identify bottlenecks, risks, and opportunities for improvement.

It is often run as a workshop, as Thoughtworks explains:

> *First, the steps in the process are listed in order, from the developer workstation all the way to production. Then, a facilitated session is used to capture further information and pain points. The most common technique we see is based on *[*value-stream mapping*](https://en.wikipedia.org/wiki/Value-stream_mapping)*, although plenty of *[*process map*](https://caroli.org/en/path-to-production/)* variants are equally valuable.*

Steps should include both technical parts (e.g. build, automated testing) and non-technical ones (e.g. QA on a staging environment) to get the full picture of how software release happens.

For this reason, this is most often a cross-functional activity where many stakeholders are involved. Daniele Salvatore, who leads cloud efforts at FAO, weighed in on this 👇

> *I applied the Path To Production mapping technique while defining the process of the newly created cloud environment at FAO.

Some processes changed as the organization underwent its digital transformation and the mapping exercise helped streamline the product releases, ensuring the required quality gateways were enforced.

One key factor to consider is ensuring that every stakeholder in the process is represented during the exercise.*

A snappy release process that allows you to ship in a few minutes is one of the main factors that separate elite teams from average ones. 

You can find more techniques and ideas in the Tech Radar edition we issued early this year 👇

[https://refactoring.fm/p/tech-radar-2023](https://refactoring.fm/p/tech-radar-2023)

### 3) ✏️ Commenting code

Commenting code is a somewhat controversial practice, as many developers believe that *good code documents itself*.

I found, instead, that top performing teams are consistently good at commenting code, by focusing on the right amount of comments that provide the most value to the codebase.

Here is more about common types of comments:

- ✅ **Comments at the top of the file/class** — a few lines to describe the file’s primary goal can go a long way to help maintainers. It also helps to avoid scope creep over time and to keep the file true to its original goal.

- ✅ **Comments on complex functions** — most functions should be simple enough to be understandable *as-it-is*, but there are algorithms and processes that cannot be so, no matter how well you write them. In these cases, it helps to include a description of the inputs, the logic, and the outputs of the function.

- ❌ **In-line comments** — while there is value in explaining the workings of a complex function, the need to comment single lines of code is most often a code smell. If people understand what the function does but not some of its lines, there is probably something you can rework, rather than commenting the lines themselves.

Code comments are also easier to keep up to date with respect to docs that live elsewhere, as you may update them in place whenever you are making changes to the code itself.

Likewise, it is easy to spot in PRs whenever somebody is changing the code without updating the comments, and report it.

You can find more ideas about code quality in this previous Refactoring article 👇

[https://refactoring.fm/p/what-is-code-quality](https://refactoring.fm/p/what-is-code-quality)

---

### **🏛️ **[**Plato Academy**](https://academy.platohq.com/?utm_source=partner&utm_medium=newsletter&utm_campaign=refactoring)** ($100 gift card!)**

Last week we covered Plato Academy, the mentorship platform for engineering leaders.

At Plato Academy you get cohort-based learning, 1-1 mentorship, and community Q&As with mentors coming from leading tech companies like Reddit, GitLab, Netflix, Box, and more.

Learn more about Plato Academy

As a Refactoring member, you can get an exclusive **$100 Plato Academy gift card **🎁 by filling out [this form](https://coda.io/form/Gift-Card-for-Refactoring-Members_d16C2FopEKV)!

---

And that’s it for today! If you are finding this newsletter valuable, consider doing any of these:

**1) ✉️ Subscribe to the newsletter** — if you aren’t already, consider becoming a paid subscriber. You can learn more about the [benefits of the paid plan here](http://refactoring.fm/about).

Get full access to Refactoring today ✨

[https://refactoring.substack.com/subscribe](https://refactoring.substack.com/subscribe)?

**2)** ❤️ **Share it** — Refactoring lives thanks to word of mouth. Share the article with your team or with someone to whom it might be useful!

I wish you a great week! ☀️

Luca
