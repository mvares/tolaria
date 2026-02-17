---
aliases:
  - "How to Estimate Software Projects"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-essays|Publish Essays →]]"
Status: Evergreened
"👓 Status": Not started
"URL 2": "https://twitter.com/lucaronin/status/1450016324017610754"
"Created time": "2024-04-18T14:53:00.000Z"
Date: 2021-10-14
"Has Notes":
  - "[[evergreen/use-story-count-to-calculate-velocity-and-effort|Use story count to calculate velocity and effort]]"
  - "[[evergreen/create-stories-that-are-clear-small-and-independent|Create stories that are clear, small and independent]]"
  - "[[evergreen/assign-story-points-in-6-steps|Assign story points in 6 steps]]"
  - "[[evergreen/story-points-are-arbitrary-and-thats-fine|Story points are arbitrary — and that's fine]]"
  - "[[evergreen/using-time-to-size-work-is-bad|Using time to size work is bad]]"
  - "[[evergreen/delivering-value-vs-delivering-plans|Delivering value vs delivering plans]]"
  - "[[evergreen/estimates-are-useful-for-three-things|Estimates are useful for three things]]"
  - "[[evergreen/get-rid-of-estimates-if-they-are-not-useful|Get rid of estimates if they are not useful]]"
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 9b06b324-724d-44e2-85f0-7569aa9cc60e
---

# How to Estimate Software Projects

### 📑 Materials

---

[Untitled](https://www.notion.so/b7d1aa4ba25d46549b28c1ac3fb7548d) 

[Untitled](https://www.notion.so/1c5eff29301d425f98958f879afe8995) 

[Untitled](https://www.notion.so/8f95ab5e48fa4ee3b269ad59db431119)

[Untitled](https://www.notion.so/c22a22ee58524b1a832a375f2aefe961) 

### ✍️ Post

---

A few weeks ago I write an article on [how to avoid negotiating on estimates](https://refactoring.fm/p/negotiating-estimates).

There I argue you can reduce conflicts by working in **small batches** and focusing on continuous delivery. When stakeholders realize they get some value every week, they naturally reduce their attention on* *estimates and deadlines.

After that article, many people reached out with questions about estimates. 

- So, what's the best way to estimate projects? 

- Do I think estimates are inevitably bad?

- Should we estimate projects...at all?

So here are my complete thoughts on how and why to estimate projects 👇

### Why you should estimate projects

This question is less trivial than it seems. I know teams who don't estimate pretty much anything, and others who care religiously about points, burndowns and such. 

You will find successful stories from both camps, so do not take anything for granted.

Estimates, like all metrics, are only useful if they are **actionable**. So the question is: how are your decisions affected by them?

There are three major areas for which estimates are useful:

1. 🥇 **Prioritization** — you need to decide which features you should develop first, based on the highest value / cost ratio.

1. 🍱 **Allocation of Resources** — you need to set a budget for a project, or a team. You want to know if you need to hire more people, or maybe work with an agency, and so on. 

1. 🤹 **Coordination** — you have multiple projects that depend on each other, and you need to schedule things in a way that nobody gets stuck.

These are all situations where estimates provide value. 

There are, however, also plenty of scenarios where you don't have such needs.

Say your team works autonomously on a specific product area. You have a PM that collects feedback from users and provides ideas for new features, and these get delivered in continuous fashion. You do this week after week. 

Do you need to estimate all the things? Probably not.

But after all, why shouldn't you? Are there any downsides to estimation? 

### Delivering value vs delivering plans

Estimates set expectations, and expectations need to be managed. Once you have them in place, you are pressed to follow the plan and meet them as much as possible. 

This pressure can be healthy, and plans are not bad *per se*. But you should not forget the final goal is to **deliver value**, not to **deliver plans**. If you find better ways to deliver value to the final user, you should be able to change the plan and go for it.

A big investment in estimates reduces your **agility** and can lead to [*feature devotion*](https://martinfowler.com/bliki/FeatureDevotion.html)* —* that is, when you value delivering features more than the actual outcome for the user.

### How do you estimate projects?

After all these caveats, let's talk of how to estimate projects. I know three main ways:

1. ⏱️ **Effort **— size is estimated in time (hours, days, and so on)

1. 🔢 **Story Points **— size is estimated in abstract *points*

1. 🧮 **Story Count **— size is estimated in number of stories

Even though you can be successful using any of these methods, it looks like there is a *path of enlightenment* where teams move from estimating effort, to points, to eventually just counting the stories.

There is a scene in [*Leon: The Professional*](https://www.imdb.com/title/tt0110413/) movie, where the titular hitman trains a young girl about the various methods to assassinate a man. He shows her a sniper rifle first, then a gun, and finally a knife. He explains that, counterintuitively, you have to learn them in this order. Because the more experienced you are, the closer you can get to your target. 

Likewise (but we are not killing anyone here) these estimation methods look progressively *simpler *to implement, they actually require a higher level of maturity to be successful.

Let's see them one by one 👇

### ⏱️ Effort

Measuring effort means writing down you will need X hours or days to complete a task.

This is the most intuitive technique of all, and also the worst.

Measuring effort is bad because:

1. 👥 **It depends on the developer** — the estimate is bound to the person that is assigned to the task. Junior vs Senior devs might take very different times to complete the same task.

1. ⚒️ **It depends on** **other activities** — even though you can strive to measure an absolute effort, devs will naturally take into account the time they expect to lose on concurrent activities, like maintenance, meetings, and interruptions.

1. x🗓️** It turns estimates into** **deadlines **— it comes natural to set deadlines based on the sum of days that come up from estimates. This creates a **commitment **that is fragile — see (2) — and imprecise, because estimates are rough. It also puts more stress on developers, which may lead to the vicious cycle of inflated estimates.

![image](../assets/4477c18c62a94a2c.png)

So if you shouldn't measure effort, how can you find out how much time you need for a project? There are two other ways 👇  

### 🔢 Story Points

Story points are an **arbitrary measure** for *sizing* a task (or story). They do not represent how much time you need to complete a task — they represent the task **complexity**.

Many people find strange to use an abstract unit to measure the size of a story. To make it easier, think that, as humans, we have been doing it forever. 

Units of measure we use in real life are totally made up: meters, kgs, are all arbitrary. Nevertheless, they are useful for many purposes. The most relevant for our case are:

- **Velocity** — Once you have meters, you can say you can run (say) 10 km / hour, while that other guy can run 12 km / hour. Together you can cover 22 km in an hour. 

- **Relative sizing **— You can easily measure things by comparing them to those you have already measured.

Story points allow for easy sizing. Then, you can measure and use your team **velocity **to estimate how much time it will take to complete a group of stories.

#### Why should you use story points?

Story points solve many issues we had using *effort*:

- They do not depend on the developer — velocity does.

- They do not depend on other activities.

- It's psychologically safer than providing a time estimate. Deadlines stay under control of the team.

Basically, effort is a bad measure because it couples two different values together: **size + velocity**. Story points keep them separate.

#### How to assign story points?

Here is a practical guide to size stories with points:

- **Start small** — If you are starting from scratch, take a story that looks *smallish* and assign 2 points to it.

- **Compare** — measure other stories by comparing them to similar sized ones (or to the initial one). It should be easy to say "this looks twice as complex", or "this looks similar".

- **Be fast** — do not spend more than a few minutes to size a story. Spending more than that brings diminishing returns. 

- **Use an exponential scale** — (1, 2, 4, 8, 16), because relative sizing works better with that and you don't really need more precision. In alternative, you can use Fibonacci's (1, 2, 3, 5, 8, 13)

- **Keep story sizes small** — if you have to go over 16, just assign a provisional "Epic" to it, and split it into multiple stories later. As a rule of thumb, you should be able to deliver any story within an iteration (e.g. two-weeks cycle).

- **Involve your team **— if you have a small team (<10 devs), involve everyone in sizing stories (e.g. with [planning poker](https://en.wikipedia.org/wiki/Planning_poker)). Otherwise, involve a few team representatives.

#### Who creates the stories?

Creating good stories requires **Product Managers** and **Engineers** to work together. 

This is not a top-down process, but rather an iterative one where the PM comes with some requirements, and these are refined and split into separate items based on the engineering work.

This is one of the reasons why you can afford to spend just a few minutes on estimates. At that point, the bulk of **analysis** should have been already done at story creation time.

![image](../assets/e4c6adbb3a4e43a6.png)

### 🧮 Story Count

Some teams calculate velocity and effort just based on the number of stories that get implemented.

Most of the times you do not give up sizing altogether, but you use a much simpler scale (e.g. S, M, L). In this case, size is just used for internal reference and not for planning capacity.

The beauty of this method is that it works as long as there is not too much variance among stories' size. So it shifts your attention to **creating good stories**.

This doesn't mean everything has to be the same size. You may still have stories that are 3-4x others. But compared to the classic story points scale (1 → 16) it requires more effort into splitting stories properly.

Using the story count brings several benefits:

- 📈 **Same accuracy as story points **— story count is a surprisingly stable and reliable metric. You might think story points are more accurate, but [it's not the case](https://www.thoughtworks.com/insights/blog/how-estimating-story-counts-worked-us). 

- ✍️ **Forces you to create good stories **— this is the most important benefit. Creating good stories improves estimates by itself, and it helps with continuous delivery too.

- 🧘 **Simpler **— it is both simpler to implement and simpler to communicate to stakeholders. Do not discount the power of simplicity.

### 📚 Resources

- 📑 [**Purpose of Estimation**](https://martinfowler.com/bliki/PurposeOfEstimation.html)** **— Martin Fowler argues you should only estimate projects when it helps you to make significant decisions. I loved it and incorporated many insights into this article.

- 📑 [**How Do You Estimate an Agile Project?**](https://info.thoughtworks.com/rs/thoughtworks2/images/twebook-perspectives-estimation_1.pdf)** **— great presentation by Thoughtworks about the different techniques you can use to estimate projects. It includes the techniques we discussed here, with additional examples and insights.

- 🌀 [**How to Avoid Negotiating on Estimates**](https://refactoring.fm/p/negotiating-estimates)** **— continuous delivery reduces conflicts and can make estimates less relevant. It is a crucial step on your *path of enlightenment.*

### ⭐ Weekly Featured Jobs

Here are the remote engineering jobs I recommend this week 👇 

I personally review each of these jobs and have a call with people from the companies to get more context, provide advice and better understand the opportunity.

#### Flick — [Full Stack Typescript Engineer](https://pallet.xyz/list/refactoring-jobs/jobs/a0e84d49-8f2a-4e3c-a96c-26f1ace58e2c)

[Flick](https://www.flick.tech/) is an analytics tool for Instagram creators. I talked with their founder [Andreas](https://twitter.com/andyasprou) about their hiring process and needs — their tech stack is cutting edge and they wrote one of the best job posts I have ever seen.

#### Makelog — [Senior Full Stack Engineer](https://pallet.xyz/list/refactoring-jobs/jobs/f9d03746-5990-4756-bb2a-8cc958f4c716)

[Makelog](https://makelog.io/) helps companies to keep customers engaged via product updates. It is a brilliant tool that automatically integrates with your engineering process, such as commits and pull requests. Their founder, [JJ](https://twitter.com/HiJulieJennifer) is insightful and driven by a compelling vision.

### 📣 CTO Craft Con 3.0

I am really happy to promote the CTO Craft conference, just like I did last year.

CTO Craft is one of the truly great conferences for engineering leaders out there, I always attend it and it always delivers.

![image](../assets/90130da1d3274ca5.png)

This time it lasts four days, from Nov 8th to 11th, and it gathers great tech leaders to share stories, case studies and best practices around four topics: Hiring, Learning & Development, Strategy, plus Burnout and Stress.

It includes CTOs from incredible companies like Slack, LikedIn, CircleCI, Firefox, and more.

Check it out below
