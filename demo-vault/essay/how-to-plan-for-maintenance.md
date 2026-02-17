---
aliases:
  - "How to Plan for Maintenance"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-essays|Publish Essays →]]"
Status: Evergreened
URL: "https://refactoring.fm/how-to-plan-for-maintenance"
"👓 Status": Not started
"Date HH": 2025-06-12
"Created time": "2024-04-18T14:53:00.000Z"
Date: 2023-04-13
"Has Notes":
  - "[[evergreen/platform-teams-maintenance-teams|Platform teams ≠ maintenance teams]]"
  - "[[evergreen/address-maintenance-with-cycling|Address maintenance with “cycling”]]"
  - "[[evergreen/do-small-maintenance-with-the-boy-scout-rule|Do small maintenance with the Boy Scout rule]]"
  - "[[evergreen/lets-define-what-is-not-maintenance|Let’s define what is “not” maintenance]]"
Tags:
  - Software
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 82574e4f-cb83-4e44-97bf-a6002a6e7df8
---

# How to Plan for Maintenance

### 📑 Materials

---

- [https://blog.rstankov.com/bug-duty-process/](https://blog.rstankov.com/bug-duty-process/)

- 

### 💡 Ideas

---

- 

### ✍️ Post

---

One of the most important duties of any engineering team is spending their time and effort on the *right* things*.*

So, in an *ideal world*, you would pull all the possible tasks, calculate their cost, their value, and address them in descending order based on their ROI.

In the *real world*, though, this doesn’t happen.

It doesn’t happen because, in product & engineering, there exist radically different *types* of work: think of a big feature vs a large refactor, or a small product improvement vs updating a dependency. For many of these, figuring out the precise value (or cost) beforehand is tricky. Also, sometimes they just bring different types of value (e.g. more revenues vs more productivity), so the playing field is not even.

*Maintenance *tasks are the ones that suffer the most from this mismatch. They are extremely valuable in the long run, but they can be also utterly technical and hard to grasp by PMs and business folks.

So, in the most successful companies I know, maintenance is addressed in very **specific ways** to *protect *it and make sure people keep doing it.

This article covers the best ideas I have found on how to perform maintenance. It includes real-world case studies from the teams at Product Hunt, Swarmia, Codacy, and Casavo, and more ideas from yours truly.

Here is what we will cover:

- ❓ **What is maintenance** — or, better, what does it feel hard to plan and prioritize?

- 🏅 **Boy Scout Rule **— a cultural staple for handling everyday tasks.

- 🔄 **Cycling **— assigning people to maintenance with *rotating* processes.

- 🏊‍♀️ **Swimlanes **— allocating fixed time to maintenance, separated by product dev.

- 👷 **Dedicated teams **— having a permanent team for it.

- 📋 **Tracking tasks **— on the need and perils of backlogs.

Let’s dive in!

---

### ❓ What is maintenance

When talking about maintenance, you may immediately think of various technical* *tasks like fixing bugs, refactoring code, or updating dependencies.  

However, since I am writing this to help with *planning* and *resource allocation*, I feel we should enlarge the scope a little bit, and ask ourselves: ***what does it feel hard to plan and prioritize*****?**

In my experience, there are two elements that play a role in this: **urgency** and **size**.

#### 1) **High urgency**

Urgency makes things easy from a planning perspective: you just do them.

Aside from stopping on your tracks then *incidents *happen, you may also benefit from hard-and-fast rules for addressing P1 items. [Kendrick Curtis](https://www.linkedin.com/in/kendrickcurtis?originalSubdomain=uk), Lead EM at Codacy, has a zero-tolerance policy: 

> **“*****All outstanding “high” bugs go into the next sprint — PM gets what's left”. ***

It’s simple, and it works. But in general, P1 stuff is not what people have trouble with.  

#### 2) **Large tasks**

Large tasks also kind of make things easier: you sit down, explore the *whys*, figure out effort, and approximate a ROI. 

You can afford to be thorough because, of course, for big items it is worth it.

Pitting large engineering work (e.g. migrating a framework) against other feature work may be a headache, but it’s the right thing to do, and there is little doubt about it. 

![image](../assets/ef1961af92324713.png)

#### 3) Small & non-urgent

Instead, where I have found people struggle the most it’s with the **small & non-urgent**:

- Fixing a nasty bug that few people care about.

- Updating a non-trivial dependency because of a minor vulnerability.

- Spending 2 days to rework an abstraction that has been leaking for a while, but causes no immediate pain.

This is the true *maintenance* that often falls in nowhere* *land. Not urgent enough to be addressed immediately, but relevant enough that you can’t ignore it.

How do you deal with this? Here are the most common approaches, with upsides and downsides.

### 🏅 Boy Scout Rule

> ***Always leave the code better than you found it.***
— Robert Martin (Uncle Bob)

The boy scout rule, coined by Robert Martin, is about taking the chance to improve the code whenever you are already making changes to that code, for any other reasons. Think of adding a test that wasn’t there, or updating a small dependency. 

This approach works well, but not for everything. A few upsides and downsides:

- 🟢 **It avoids context-switch** — it makes the change cheaper than scheduling a separate task

- 🟢 **It doesn’t require negotiation** — it is just agreed that estimates keep some *slack *for this type of tasks.

- 🔴 **Timeline is best-effort **— doing such improvements depends on other tasks, so it’s only suitable for issues that can afford to wait kind of indefinitely.

- 🔴 **Only suitable for very small tasks **— Adding a few hours to improve existing tests is ok, but you can’t slip e.g. two days of maintenance on top of two days of feature work with the *boy scout rule*. I have seen it happen and it breaks trust. Don’t do it.  

A corollary of the rule is to *do immediately* whatever is too small to be otherwise tracked and planned.

> ***"Will it take less than two minutes?" Yes, then do it.
****— *David Allen, Getting Things Done

This is lifted straight from the [GTD](https://en.wikipedia.org/wiki/Getting_Things_Done) methodology, where David Allen advocates to do on the spot any task that requires less than two minutes to complete, like sending a short email or making up the bed.

In software, you might want to put the threshold to 5-10 mins, and there are plenty of stuff that falls into this:

- Small cosmetic updates to the UI

- Very small bugs

- Changing a piece of copy

In these cases, you will spend more time creating a ticket and pondering (multiple times in the long run) when to do it, than just by doing it on the spot. So do it, or ignore it forever (which is equally ok).

### 🔄 **Cycling**

A popular strategy to address maintenance is to have some *rotating* process where people are periodically assigned to a maintenance-only schedule.

Here are a couple of variations:

#### 🪖 Bug Duty

[Radoslav Stankov](https://www.linkedin.com/in/radoslavstankov?originalSubdomain=bg), Head of Engineering at Product Hunt, wrote [a full article](https://blog.rstankov.com/bug-duty-process/) about their *bug duty *process.

A different person from engineering is assigned to the *Bug Duty* every sprint. During that sprint, they don't work on a project. Instead, they work on the bug backlog. Quoting the article:

> *The engineer has the following responsibilities:
* Manage the "Bugs" project in Asana
* Fix outstanding bugs
* Immediately fix the bugs marked as “high priority”
* Attend the Support team weekly sync, where issues with our website are often discussed
* Be available in the *`*#product-feedback*`* Slack channel (our teammates post issues there. The person on bug duty should handle those)
* Handle all upcoming exceptions reported in *`*#engineering-sentry*`* (this Slack channel receives all Sentry errors. We try to keep their number to 0 in production)*

This process works well especially in small teams, where knowledge of the codebase is widespread, and you may generally have full-stack devs. In larger orgs, you can counter the higher specialization by assigning multiple people to *Bug Duty* at the same time, covering the various platforms / layers (e.g. frontend + backend).

In any case, consider keeping one person responsible for the process, for building ownership. In Rado’s own words:

> *For me is important to have a single DRI (Direct Responsible Individual) for bug split even if there is more than one person on bug duty. It should be a different one each sprint, since it is a good learning experience.*

A variation of this is implemented at Swarmia as well. [Ari Koponen](https://www.linkedin.com/in/apkoponen?originalSubdomain=fi), Head of Platform, weighs in:

> *We also have a rotating "Chief Firefighting Officer (CFO)" role. The CFO fixes immediate customer support needs, keeps taps on our production systems, merges dependency updates (PRs generated by *[*Renovate*](https://www.mend.io/renovate/)*), etc. *

#### 🎽 Maintenance Team

The *larger* version of the bug duty process is to assign a whole team to maintenance for a period of time. These are sometimes called *quality sprints*, or [*bug bashes*](https://en.wikipedia.org/wiki/Bug_bash)* *if focused on finding and fixing bugs*.*

[Kendrick](https://www.linkedin.com/in/kendrickcurtis?originalSubdomain=uk) from Codacy weighs in on this:

> *If you have multiple teams working on a product, allocate a whole team to maintenance activities, for a period of time, then cycle them out. So then none of the rest of your squads' time gets contaminated so PM can plan nicely. 

And when there's no "bugs" work to do, the maintenance team can work on dependency updates, refactoring etc. 

I actually had a team at RLDatix who loved being on "release bugs" because all the time they were not on that, they were ripping the code apart and making it better in a really self-directed way.*

Similar initiatives exist for other types of engineering work as well: you may hear about *security sprints*, or *accessibility sprints.*

My take is that such dedicated cycles work well in creating momentum and fixing a large number of issues all together, but suffer from being—inevitably—infrequent, so they can’t be your only maintenance strategy.

If you do a quality sprint once every four sprints, on paper it’s a healthy 25%. In practice, though, with weekly sprints, that means fixing bugs only once a month, which is definitely not enough. If you have multiple teams, rotating them works better, as long as any team can own bugs from anywhere in the product.

A good way to make *maintenance teams* work is to pair them with a strict policy that doesn’t let high priority bugs pile up, as we covered above.

### 🏊‍♀️ **Swimlanes**

*Swimlaning* is an approach that allocates some fixed time to maintenance, separating it from the rest of product dev time.

The main intuition behind it is that you should *balance* your engineering investment across various categories, and this proportion can be more or less stable over time.

![The “balance framework” buckets engineering work in four main categories.](../assets/983dd08dae4b48d5.webp)

I wrote more about balancing your engineering investment in a previous Refactoring article 👇

[https://refactoring.fm/p/engineering-investments](https://refactoring.fm/p/engineering-investments)

In my previous startup, we allocated between 25% and 30% of time to maintenance and small changes, and ran a separate, weekly process entirely for this.

I covered our process in detail in a two-series article:

- 🔨 [**How we Plan Maintenance and Small Changes**](https://refactoring.fm/p/how-to-plan-and-execute-maintenance)

- 🎾 [**How we Use Tennis Rankings for Fixing Bugs**](https://refactoring.fm/p/how-we-use-tennis-rankings-for-fixing)

Fun fact: the latter was the first Refactoring article to ever get to the first page of Hacker News. It generated ~~many insults~~ a heated discussion.

[Ari](https://www.linkedin.com/in/apkoponen?originalSubdomain=fi) also has a smart take on this, based on their use of Kanban:

> *We structure our planned work into "stories" that take ~2 weeks to complete with 2-4 devs. We have 3 swimlanes for stories and an "****Everything else****" lane where smaller improvements and bug fixes (that can be completed in a single task) end up in.

Engineers work on the "Everything else" lane stuff when they don't have work in their current story (e.g., it's winding down, or there is another task that is blocking new work). Most of the time this process works well. Sometimes, we realize that things are not moving in the "Everything else" lane quickly enough, and we wrap them into a story and move it to one of the 3 dedicated swimlanes.

Also, we keep eyes on how much works goes to keeping the lights on (KTLO), and if it's trending up, we might tackle it by creating a story-sized increment that reduces KTLO.*

![image](../assets/1a20c93ea1c54430.png)

Ari and his team would of course use [Swarmia](https://www.swarmia.com/) for tracking this, in a great example of dogfooding.

### 👷 **Dedicated team**

The last strategy that I want to address is having a permanent, dedicated team for maintenance tasks. This is, of course, only in the cards for larger orgs, but the question is: does it make sense anyway? Are these the famous *platform teams?*

Well, yes and no.

Platform teams make sense to address DX improvements, practices, and strategic investments on *horizontal *areas that would otherwise span multiple teams, and therefore be hard to develop.

Now, there is an overlap between platform activities and what we called *maintenance *so far — but it’s far from 100%.

Tasks that are *vertical *to some product area, be them around productivity, bug fixing, or basic KTLO, should be generally owned by the team who also owns that product area. This is just the healthiest option to 1) enforce ownership and 2) leverage the team’s domain expertise.

So, if you are thinking of creating a platform team, make sure they would actually work on *platform*, rather than being the *bug fixing team* no one wants to work in.

### 📋 How to track maintenance

Finally, a few words on tracking maintenance tasks.

In my experience, creating a **technical backlog** is absolutely paramount to make sure things do not get lost and people know what to work on when they are finally able to carve out time for this.

[Jose Escobar](https://www.linkedin.com/in/jaescobar/), CTO at Orbit Technology, also commented on this, with a caveat 👇

> *Just setting the expectation and responsibility on the team that they should keep a prioritised "technical backlog" hasn't been enough. One thing we've tried with moderate success is keeping a "Technical Inbox", where we add all the technical tasks that we want to carry out to a backlog and score each item with a modified ****ICE score****. This has allowed the team to get at least some guidelines when prioritising the work to tackle in that time.*

The ICE score that Jose refers to considers **Impact**, **Confidence**, and **Ease**, and helps you rank tasks so you address the most promising ones first. I covered various prioritization frameworks in this previous article:

[https://refactoring.fm/i/18579637/evaluating-ideas](https://refactoring.fm/i/18579637/evaluating-ideas)

#### Backlogs are bad, though

A word of caveat about backlogs: they are bad. They easily fill up with stuff you know you will never do, you feel guilty deleting anything from them, and they just *degrade* the morale of your team that is faced with a neverending todo list.

To keep your backlog healthy, use it as your **last resort**:

- Set rules to do high priority tasks immediately, or soon enough that they stay in the backlog for very little time.

- Do small, non urgent tasks immediately (i.e. GTD’s 2 minute rule) or track them directly in the code (you can use something like [Stepsize](https://stepsize.com/)) to be later addressed with the boy scout rule.

- Make things very *short-lived*. Be suspicious of anything that has been in the backlog for 2+ months. Most often, you can safely delete it. If it was important, 1) you would have done it already, or 2) it will surface it again. In either case, the risk of deleting it is low.

Here is also a [great article](/c55687cd12524343afbccc681bb26e12) by Mary Poppendieck about why you should burn your backlog.
