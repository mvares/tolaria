---
aliases:
  - "On-call Process"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-essays|Publish Essays →]]"
Status: Evergreened
URL: "https://refactoring.fm/p/on-call"
"👓 Status": Not started
"Date HH": 2025-03-27
"Created time": "2024-04-18T14:53:00.000Z"
Date: 2022-12-22
"Has Notes":
  - "[[evergreen/managers-can-go-on-call|Managers can go on call]]"
  - "[[evergreen/should-on-call-be-mandatory|Should on-call be mandatory?]]"
  - "[[evergreen/the-three-stages-of-an-on-call-page|The three-stages of an on-call page]]"
Tags:
  - Luca
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 72682c9f-75df-41cf-a02b-a6899e693b30
---

# On-call Process

### 📑 Materials

---

- [https://increment.com/on-call/crafting-sustainable-on-call-rotations/](https://increment.com/on-call/crafting-sustainable-on-call-rotations/)

- [https://charity.wtf/2020/10/03/on-call-shouldnt-suck-a-guide-for-managers/](https://charity.wtf/2020/10/03/on-call-shouldnt-suck-a-guide-for-managers/)

- [https://dev.to/molly/making-on-call-not-suck-490](https://dev.to/molly/making-on-call-not-suck-490)

- [https://www.intercom.com/blog/rapid-response-how-we-developed-an-on-call-team-at-intercom/](https://www.intercom.com/blog/rapid-response-how-we-developed-an-on-call-team-at-intercom/)

- [https://sre.google/sre-book/being-on-call/](https://sre.google/sre-book/being-on-call/)

### 💡 Ideas

---

![image](../assets/781a69d7ab7e4c6f.png)

### 🔨 Tools

- [GitLab Code Owners](https://docs.gitlab.com/ee/user/project/code_owners.html)

- [OpsGenie](https://www.atlassian.com/software/opsgenie)

- [PagerDuty](https://www.pagerduty.com/)

### ✍️ Post

---

On-call processes are a divisive topic in engineering, and for good reason. People hate being on call because it's stressful and disruptive to their personal lives — even when they don’t get actually paged.

I know it from up close. As a founder & CTO, I feel I spent enough time on-call for this life and the next three or four. In the worst cases, it was disruptive to my sleep, my morale, and left me not wanting to be anywhere close to a computer again.

But it doesn't have to be this way. 

If people hate being on call, chances are you are doing it wrong. In the best teams, being on call actually *improves* the team’s morale. In fact, it can bring several benefits, like:

- Strengthening the relationship between engineers and customers

- Developing better ownership by engineers

- Maintaining better docs

- Enforcing good instrumenting / observability

In this article, we will explore the key elements that make an on-call process successful and we’ll cover how to design a great one. This will be drawn from my own experience and the one of successful companies like Netflix, Dropbox, Honeycomb, Intercom, and Google. 

We will cover:

- 🏅 **Ownership** — the (non)difference between engineers and ops people.

- 📏 **Scope** — what goes into an on-call shift.

- ✏️ **Designing rotations **— everything you should take care of.

- 📉 **Reducing effort **— best practices to make things sustainable.

- 📊 **Metrics** — how to measure your on-call process.

Let’s go!

---

### 🏅 Ownership

The foundation for this whole article is that, as an engineer, you should fully *own* your code. That means your duties do not stop when the code is in production — you are still responsible for it.

This is the essence of DevOps and, in modern engineering, it is simply the most sensible choice.

If you forget about your code after you deploy it and pass the torch to ops, you are in for a bad experience: the feedback loop doesn’t work, and devs and ops people will simply hate each other over the long run.

In fact, the very *divide* between development and ops is blurry, and ultimately wrong. We are all engineers. People just work on different things and will eventually be on call for different things.

> *It is engineering’s responsibility to be on call and own their code. It is management’s responsibility to make sure that**** on call does not suck.**** This is a handshake, it goes both ways, and if you do not hold up your end they should quit and leave you.

– Charity Majors, CTO at Honeycomb*

So, with good docs and instrumentation, all engineers can be included in on-call rotations, but it’s up to management to create a process that works.

But what do engineers exactly do when on-call?

### 📏 Scope

During an on-call *shift*, you can get paged anytime by alerts that report some issue in the system. When this happens, you follow a three-step process:

1. **Root-cause analysis **— figure out the issue. Enabled by good alerting and instrumentation.

1. **Remediation **— put the system back up. Enabled by good playbooks.

1. **Follow-up activities **— update docs and do a bunch of things. Enabled by good process.

Let’s see all three.

#### Root-cause analysis

Root-cause analysis is about figuring out what’s wrong. This is made possible by good alerting and instrumentation. In fact, alerts you receive are of two kinds:

- **Customer-based** — e.g. slow response time.

- **Engineering-based** — e.g. memory full, various resources, etc.

In a perfect world, people should only be paged by customer alerts. In reality, you may end up with paging people for customer alerts + the most serious engineering ones, in case you have  gaps somewhere and the latter do not fire also some of the former.

Andrew Twyman, former Staff Engineer at Dropbox, weighed in on this 👇

> *We had both. The customer-facing alerts were the ones on which we defined our SLA/SLO, and had stated policies about response times, incident severities, etc.  We also had alerts on things like resources, unresponsive machines, etc.  Those were often more informational, and provided secondary signals to help the oncall debug what was going on.  E.g. if you're paged for a high overall error rate, and you also get an alert that the number of machines in the pool is lower than normal, it gives you a place to start investigating.*

#### Remediation 

Remediation is about putting the system back to an acceptable level of service. This is important to understand because it shouldn’t be confused with fixing bugs.

You can remedy an incident *without* fixing a bug, and without even knowing what the bug is. 

In fact, this is the ideal course of action: you restore the system first, and fix the bug later. It is not always possible, of course. Sometimes, fixing the bug == restoring the system, like with many frontend issues.

But sometimes you can split the two. Think of a memory leak — you may be just fine by restarting the instance, while you take more time to figure out where the issue is.

#### Follow-up activities

After remediation, you have a number of things to do to leave a clean situation. These include:

- **Update docs / playbooks** — if what you did involved anything not documented.

- **Write a postmortem **— for non-negligible incidents.

- **Fix bugs** — for when this is separated from remediation.

These are called *follow-up* because you don’t have to do everything in the same session — especially when you get paged out-of-hours. But the closer to the incident, the more context you will retain, and the easier and the more accurate these will be.

### ✏️ Designing Rotations

At its core, a rotation is made by a few core elements. Here are some FAQs, based on the most common setups:

#### **How long people stay on-call?**

Usually one full week at a time.

#### **How many people are on-call at any given time?**

You should have a **primary**, who responds to the pager, and a **secondary**, that covers the primary for when they are temporarily unable to jump in (e.g. they go to the gym for 1 hour).

The secondary should also act as the first point of escalation in case the primary is unable to solve the issue. That is preferred to escalating to a manager or other engineers who aren’t on call.

#### **How frequently should people be on-call?**

Based on most examples I have seen, the sweet spot is around **25-30% of their time**, which means about one every four weeks, either as primary or secondary.

You should strike a balance between:

- **Too frequently** — on-call becomes a burden on productivity and morale.

- **Too infrequently** — people never build the know-how to handle issues.

Of course, if you are in a small team (e.g. 4 engineers), you don’t have such a luxury and you may need to have people on call ~50% of their time, or more. In this case, you should invest as much as possible in making on-calls bearable — more on that later.

#### Should you have separate rotations based on teams?

In an ideal scenario you want to people / teams to go on-call for the code they own. So you may create separate rotations based on the parts of code each team should be responsible for.

However, there is a tension between favoring ownership and balancing the time spent on-call. Small rotations are more likely to be made of people who support code they know well, but they also make people spend more time on-call.

In my experience, you should optimize for time spent on-call first, and ownership second. That’s because the latter can be improved with good docs and runbooks, while there is no way to cope with the former. 

#### Who should go on call?

Virtually anyone. Any engineer for sure, but even managers may join, given they have some technical background.

As a manager, this is very helpful — you see first-hand the state of docs and processes and the conditions your team works in. It also sets a great example with your people, who are likely to respect you more for that.

However, I only recommend this if you feel you can be 100% helpful. You should be able to follow the playbooks and know your way around the code. Conversely, if your on-call shifts are a facade in which you always have to page the secondary, then no thanks!

#### Should on-call be mandatory?

Being on-call can be considered part of the duties of any engineer, so there is no wrong in making it mandatory. 

Especially if you are introducing this from scratch, mandatory on-call for all engineers is healthy to build ownership and to make sure no critical areas of the code are left uncovered by docs and playbooks.

Eventually, however, consider making it *voluntary*. People may be more or less okay with being on-call depending on things like their family responsibilities. If the team is big enough and the process has been battle-tested for a while already, then it's probably best to let people choose if they want to do on-call.

![image](../assets/f1d5ea9a1ff84d21.png)

#### Should people be compensated for being on call?

Indirect compensation is common in the form of extra time off. E.g. you get Friday off the week after being on call.

As for monetary compensation, it depends. As far as I know, most companies do not offer it. Especially if on-call is mandatory, which makes it part of your regular duties.

If on call is voluntary, however, you should consider it, and compensation will naturally depend on how much time people spend on call, and how much of a burden these shifts are (how often you are paged, etc).

#### Do you do other work while being on-call?

Most on-call talk revolves around out-of-hours, but on-call also takes place during regular work time. How does that change your work?

Simply put, while on-call, people should not be responsible for project work. They can’t be dependable for that, and it would add extra stress on them.

The best way to do work while on-call is to use that time for tasks that don't need to be done on a deadline, like maintenance and improving the developer experience.

### 📉 Reducing Effort

Here are your best bets to keep on-call duties manageable and stress-free:

#### 1) Good docs 📑

Good docs are crucial to on-call success. On-call docs are also different from regular docs, as they focus on the elements that help you do troubleshooting and put the systems back up.

These are usually called **playbooks** or **runbooks**, and include descriptions of components, dependencies, logs, instructions on debugging alerts, and common issues.

Whenever you create a new feature, or component, ask yourself:

- How can this fail? How should people who are on-call know when it happens?

- What are common issues it may run into? How would we put this back up?

Andrew weighed in on this:

> *Documentation is key when you're trying to figure something out late at night. We had a whole set of on-call playbooks to guide responses. Every service should have a brief description of its components, dependencies, and where to find logs and dashboards.  When you add an alert, write at least a few sentences about how to debug it. When you finish resolving an issue, write the docs you wish you just had to figure it out.*

#### 2) A few, good alerts 🚨

Alerts are only useful if people can figure out what do to next, so, for each alert you have, make sure you include docs on what issues they are most likely to be triggered by, and how to debug them.

**Be aggressive** and strive to keep only a few, good alerts. Nobody wants to get paged by something that doesn’t matter.

#### 3) Small operations 🤏

You can make the on-call workload lighter by creating systems that don't take much effort to maintain.

Cloud services are your friends when it comes to auto-scaling, failover, and overall availability. Consider also serverless services, that require even less maintenance than your typical cloud ones.

More on cloud vs on-prem infra 👇

[https://refactoring.fm/p/cloud-vs-on-premise](https://refactoring.fm/p/cloud-vs-on-premise)

#### 4) Good tooling 🔨

Keep your pipeline snappy and strive to being able to deploy in 10 mins — and see how most of your problems disappear.

Fast releases keep the *mean time to restore* low, which in turn gives you the confidence to do more frequent releases, and creates a wider virtuous cycle 👇

[https://refactoring.fm/p/how-shipping-fast-changes-your-life](https://refactoring.fm/p/how-shipping-fast-changes-your-life) 

### 📊 Metrics

Measuring your on-call process is important to be aware of what’s going on and figure out how to improve.

There are plenty of metrics you can track, but I would focus on these two to begin with:

1. **Number of pages per session** — to measure the load on those who go on call. This is provided by most on-call mgmt tools (more below in the Tools section)

1. **Mean time to restore **— counted as the time that goes from alert received to system restored. It measures how efficient you are at putting systems back up.

You can also drill down into more specific metrics, like the number of out-of-hours pages, or the avg time to acknowledge alerts — but I would start simple with the two above, that already give you a good feedback loop about people (1) and systems (2).

### 🔨 Tools

Looking at case studies and speaking with people in the SRE space, there are two tools that clearly stand out for managing on-call rotations:   

- [PagerDuty](https://www.pagerduty.com/) — probably the most popular of all. It includes on-call management, runbook automations, and plenty of integrations.

- [OpsGenie](https://www.atlassian.com/software/opsgenie) — once an independent tool, it was bought by Atlassian in 2018. The product itself is comparable with PagerDuty, if a bit less extensive. Recommended if you already work with the Atlassian suite.

### 📚 Resources

Finally, some great readings to learn more:

- 📑 [On Call Process at Dropbox](/fd16cd12b0d047519a577b19f1be526d) — by Andrew Twyman, former Staff Engineer at Dropbox. Andrew shared in the Refactoring Community a thorough description of how they ran on-calls. This is chock-full of insights, including: figuring out the right size of the rotations, customer-facing vs infrastructure alerts, primary vs secondary on-calls, and more.

- 📑 [On Call Shouldn’t Suck: A Guide for Managers](https://charity.wtf/2020/10/03/on-call-shouldnt-suck-a-guide-for-managers/) — by Charity Majors, CTO at Honeycomb. Charity argues that on-call is a responsibility shared between engineering and management, and that you should invest in good deploy tooling, observability, and feedback loops. On-call *can *be turned into a badge of pride and accomplishment, but it requires effort and a unique solution crafted to meet the needs of your company.

- 📑 [Making On-Call Not Suck](https://dev.to/molly/making-on-call-not-suck-490) — by Molly Struve, Sr. SRE at Netflix. A great case study of how Netflix went from infrequent shifts and a burned out SRE team, to 3 separate rotations designed on separate teams. These changes improved alerting, gave each team a sense of ownership, and improved the overall incident response.

- 📑 [How We Fixed Our On Call Process to Avoid Engineer Burnout](https://www.intercom.com/blog/rapid-response-how-we-developed-an-on-call-team-at-intercom/) — by Brian Scanlan, Principal Engineer at Intercom. This is a honest write up of how Intercom went from a stressful on-call process that everybody hated, to a calm one that is praised by the team. They reflect on themes like mandatory vs voluntary on-call, size of the team, and out-of-office hours

- 📑 [Being On-Call](https://sre.google/sre-book/being-on-call/) – by Google. Google's SREs approach to build a sustainable and effective on-call process. It covers the famous *25% rule*, follow-up activities, compensation, and safety.
