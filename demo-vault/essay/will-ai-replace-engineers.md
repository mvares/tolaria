---
aliases:
  - "Will AI Replace Engineers?"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-essays|Publish Essays →]]"
Status: Evergreened
URL: "https://refactoring.fm/p/will-ai-replace-engineers"
"👓 Status": Not started
"Created time": "2024-12-22T16:42:00.000Z"
Date: 2025-01-08
"Has Notes":
  - "[[evergreen/tech-has-uncapped-value|Tech has uncapped value]]"
  - "[[evergreen/human-engineers-still-do-the-most-valuable-work|Human engineers still do the most valuable work]]"
  - "[[evergreen/the-connoisseur-engineer|The Connoisseur Engineer]]"
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 164bdf02-815c-806e-a751-ce5e514a60d7
---

# Will AI Replace Engineers? 

### 📑 Materials

---

- Cost center vs uncapped value

- Asymptotic problems

- Founding teams

- Bar higher but not linearly with productivity

### ✍️ Post

---

Happy new year! Everyone is back to work after (hopefully) a few weeks spent with family & friends. 

If you are Italian, like me, this time is mostly spent around the dinner table, and you get to chat with many relatives you rarely meet during the year. This leads, surprisingly, to interesting chats — but also embarassing ones, like me trying to explain what I do for a living.

This year however, the curiosity towards my job took a back seat, making room for… AI!

And the question here was simple: **is AI coming for our jobs?**

I had to answer variants of this at least three times, coming from people from wildly different industries, which I pretty much know nothing about. And since we are on Refactoring now, I will try to answer this for engineers:

**Is AI going to replace (*****some*****) engineers (*****any time*****) soon?** 

I added a couple of qualifiers—some, and any time—to make the question more interesting. In fact, most predictions about AI today are blanket statements that don’t say much. To make things useful, you need *specifics*:

- *What* engineers is AI going to replace? Seniors? Juniors? Specialists? React developers?

- *When* is this going to happen? Next year? In 5 years? 20?

If you are serious about this *replacement *thing*, *these are the real questions — and, today, nobody can answer them. Not even close.

This apparent contradiction, where you get uncontrolled *vibes* about the future, yet nobody can talk specifics, is enabled by two things:

1. Progress in the past 2 years has been amazing.

1. We are still far from human performance on anything nuanced.

Both things can be true at the same time, but many people are mostly exposed to *one* of the two, which makes them blind skeptics or optimists:

- Creators and solopreneurs who do a lot of experimenting and green field dev are amazed by how fast you can get something done, and over index on (1).

- Engineers who work on big codebases are underwhelmed by the impact on real-world, complex work, and over index on (2).

So where is the truth? Is AI closing the gap with humans fast? And what happens next?

I will explore all of this in detail in this piece, but will spoiler my thesis now: **engineers will thrive** thanks to AI, rather than the opposite. So I am an AI-optimist, and will explain why.

Here is the agenda:

- **🧢 Capped vs uncapped value **— more productivity just creates more value.

- 🔧 **A personal example **— building an app on a tech stack I know nothing about.

- 📉 **Asymptotic progress **— singularity might be further than you think.

- ⛵ **Taste vs Skills **— 90% of the work is about recognizing what’s good.

- 🔮 **Engineers of the future **— what does the real 10x engineer look like.

Let’s dive in!

---

### **🧢 **Capped vs uncapped value

In all tech companies I have known, there has never been shortage of work.

There has never been a time, during quarter planning, or looking at the backlog, where someone said: “*well, we don’t have much to do! This will be a light [quarter | month | week]*”

That’s because **tech and product have uncapped value**: more engineering time just means more opportunities and more business.

Which means, if we equal the use of AI to more productivity, that the most likely outcome of that productivity is: **we will just get more things done**.

You can’t say the same for everything.

Think of a cleaning service: let’s say there are 3 people who come clean your office twice a week. If all of a sudden you were able to *triple* their productivity, would you still employ three of them to do *three times* the cleaning? Probably not, because cleaning has capped value — there is only so much you can do.

Tech is not like this. I am convinced software would be even more pervasive than it is today, probably by an order of magnitude, if it wasn’t for the fact that 1) we don’t have enough engineers, and 2) code is extremely expensive to write and maintain.

![image](../assets/173bdf02815c808e.png)

So, what are companies going to do with *more* productivity? Are they going to lay people off to keep getting the same amount of things done as before, or are they going to *do more* with it? To me, it is safe to say they are going for the latter.

But this won’t be true for *all* companies. There exist many companies that **see tech as a cost center with capped value**. They believe there is only so much you can get from it, and in some cases, they may even be right!

Well, these are the cases where you may see layoffs. These are the *cleaning* cases, where tech is employed as a commodity. These cases exist, but they were probably bad jobs to begin with, so I we shouldn’t focus on them.

My prediction is that good companies will use AI to do more, while bad companies will use AI to cut costs.

Now, the popular counter-argument is that this is true *as long* as AI doesn’t match (or surpass) human performance. We call it the *singularity*: after that, AI will replace engineers.

I don’t think this will happen anytime soon, for two reasons:

1. AI progress on software engineering will slow down and become asymptotic.

1. Human skills will gradually shift and focus on the things that AI is worse at, making it increasingly hard for AI to catch up.

Let me elaborate on both:

---

### 🔧 A personal example

A couple of days ago Addy Osmani wrote [this fantastic piece](https://newsletter.pragmaticengineer.com/p/how-ai-will-change-software-engineering?utm_source=post-email-title&publication_id=458709&post_id=154200840&utm_campaign=email-post-title&isFreemail=true&r=3u2qm&triedRedirect=true&utm_medium=email) on The Pragmatic Engineer about AI-assisted coding. It perfectly matches my own experience and I found myself nodding throughout the article.

So let me tell you this story. For a few years now I have had this itch of building a native note-taking app for macOS.

Today, for my notes I rely on a combination of Notion (long-term workspace), [Bear](https://bear.app/) (quick capture), and [Voicepal](https://apps.apple.com/us/app/voicepal-your-ai-ghostwriter/id6471552007) (audio notes), because no single app matches my looong list of ideal requirements (offline-first, API-ready, markdown-based, tags, audio, …).

Now, I know my way around design, but I know absolutely nothing about native macOS development. Zero. Nil. I don’t even know the Swift’s syntax. Still, over the past two months I rolled up my sleeves and tried to *AI* my way around it. I did a basic design on Figma and used Cursor as my main IDE.  

To my surprise, I managed to get to a (pretty awesome) working version: it syncs content with [Sanity](https://www.sanity.io/), supports nested tags and the most common markdown syntax 👇 

![image](../assets/16abdf02815c801f.png)

It also has a lot of handy things that I miss from other apps, like my favorite shortcuts and—I am very proud of this one—one-click to copy the HTTP GET URL for both single notes and entire collections, so I can easily add them as self-updating context to AI.

All the code was written by Cursor, because, again, I don’t know how to write proper Swift. But doesn’t mean I didn’t do any engineering work:

- I told AI I wanted to use Sanity to store notes, because this would save me from writing a proper backend and I would get API and version control for free.

- I told AI I wanted to use [CRDTs](https://en.wikipedia.org/wiki/Conflict-free_replicated_data_type) to enable concurrent changes across multiple devices, and instructed it to use the [Automerge](https://automerge.org/) library to do so, instead of implementing everything from scratch (which, if left unchecked, was very happy to do).

- I regularly broke work down into small, independent features that could get done with as little context as possible.

- I did an awful lot of debugging which, even though I don’t know Swift, still relied on my engineering *instincts*.

So, while there is no doubt this whole project was *enabled* by AI, there was a lot of engineering work done by a human. Also, it was work of the highest caliber: system design, buy vs build, scoping — these are some of the hardest, most important things that people get done in any project, and that require the most expert judgment.

Which leads me to my next point 👇

---

### 📉 Singularity might be further than you think

For a lot of AI use cases, it looks like every year is the right year for AI to surpass humans, but it never does. Think of self-driving, professional translation, or, of course, coding.

Progress on these problems gets asymptotic and, while we get closer and closer to the real thing, we never really get there.

The reason is that while tech grows linearly ([sometimes less than linearly](https://techcrunch.com/2024/11/20/ai-scaling-laws-are-showing-diminishing-returns-forcing-ai-labs-to-change-course/)), the problems we are left with are exponentially harder. Those final corner cases in self-driving are not *slightly *harder than the happy path, they are 10-100x harder. The same goes with system design and the stuff that engineers are left to deal with.

So, I have this feeling that for the next 10 years we will keep saying engineers are going to be replaced *next year*.

That’s not only because of pure tech progress, that’s because **engineers will adapt**, and will keep moving the goal post 👇

---

### ⛵ Taste vs Skills

Last week I tried [Ghostty](https://ghostty.org/) a native terminal emulator for Mac and Linux. It is a delightful product, incredibly fast, and thoughtful in a thousand different ways.

It has also been developed mostly by one person, [Mitchell Hashimoto](https://mitchellh.com/). Mitchell says Ghostty has plenty of contributors, but honestly, looking at [Github](https://github.com/ghostty-org/ghostty), Mitchel made 5000+ commits; and the second in line ~200.

This is the type of work that *can* be done by a single person in 2025, but it is — and I believe it will stay — extremely rare.

Why aren’t there more examples like this? What stops developer to work like this?

To me, it’s *taste*.

Taste for good products, for good UI/UX, for good system design, for good tradeoffs.

Taste is being able to tell what’s good, and, to some extent, being able to express *why*. As pure tech chops get commoditized, this is what 90% of human work will look like.

In a way, it is what Rick Rubin said in his infamous interview last year 👇 which became an instant meme.

[https://www.youtube.com/watch?v=h5EV-JCqAZc](https://www.youtube.com/watch?v=h5EV-JCqAZc)

Fast forward one year, it doesn’t sound silly anymore.

So what does the engineer of the future look like?

---

### 🔮 What does the engineer of the future look like?

A [2022 survey](/164bdf02815c806ea751ce5e514a60d7) to 250K developers found that devs code on average 52 minutes per day — which is about 10% of their time.

![image](../assets/173bdf02815c8066.png)

This seems shockingly low, but I spoke with many others ([Henry](https://refactoring.fm/p/continuous-coordination-with-henry?utm_source=publication-search), [Farhan](https://refactoring.fm/p/running-a-remote-big-tech-with-farhan?utm_source=publication-search)) who reported similar figures, always between 10% and 15%.

So, even if you are able to eliminate coding completely, as of today, that’s at most a 15% improvement.

What goes into the remaining 85%? It’s requirements, design back & forth, meetings, and coordination. To go after that 85%, you need to **reduce the cost of coordination** — and to do that, you need people to do *more things* they didn’t do before, not just more of that they already did.

This comes in many shapes and forms: merge backend and frontend engineering, have engineers own QA, or even [own features from top to bottom](https://refactoring.fm/p/how-to-become-a-product-engineer).

You won’t unlock everything AI has to offer by staying in your lane and pedaling faster. You will do so by learning to do the work of different people, so that we can eliminate more meetings and overhead.

This doesn’t mean we will need *fewer *people overall — it just means teams can get smaller and people can focus on great creative work, instead of passing the ball around.

If you ask me, this is a promising future, which I very much look forward to.

---

### 📌 Bottom line

And that’s it! Here are the main takeaways from today:

- 🚀 **AI won't replace engineers, but empower them** — Good companies will use AI to do more, not cut costs.

- 🔄 **Uncapped value in tech** — More productivity means more opportunities, not fewer jobs.

- 📈 **Asymptotic progress** — AI may struggle to fully match human performance in complex engineering tasks, for a long time.

- 👁️ **Taste becomes crucial** — The ability to recognize and create quality will differentiate engineers.

- 🔨 **Engineering evolves** — Future engineers will focus more on high-level decisions, system design, and full-stack work.

- 🌟 **Adaptability is key** — Engineers who expand their skills beyond coding will thrive in the AI era.

---
