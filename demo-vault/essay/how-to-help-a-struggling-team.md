---
aliases:
  - "How to Help a Struggling Team"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-essays|Publish Essays →]]"
Status: Evergreened
URL: "https://refactoring.fm/p/how-to-help-a-struggling-team"
"👓 Status": Not started
"Created time": "2025-06-19T08:25:00.000Z"
Date: 2025-07-30
"Has Notes":
  - "[[evergreen/the-four-struggles-of-engineering-teams|The four struggles of engineering teams]]"
  - "[[evergreen/find-your-allies-to-turn-teams-around|Find your allies to turn teams around]]"
Tags:
  - Mastermind
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 217bdf02-815c-800a-a15c-c7b6994ad965
---

# How to Help a Struggling Team

### 📑 Materials

---

### Notes

### Mastermind notes

### ✍️ Post

---

Last month we had a great [mastermind session](https://refactoring.fm/p/introducing-the-refactoring-mastermind) about how to raise the *quality* bar of your team.

Intentionally, we kept the term *quality* generic. We didn’t want to fixate on *code quality* specifically, but rather on the all-round quality of the work of your team, which has many shapes and facets, and see what participants needed the most help with.

Out of the various stories, we spent a long time talking about **how to help a team that was struggling**.

A snapshot of our recent Mastermind session

![image](../assets/23fbdf02815c802b.png)

I won’t go into details, because I don’t think these are particularly helpful: they may or may not apply to you. But I will try to take the best advice that was shared, and distill first principles and ideas that should be useful to most.

By the way, this is always hard to do, because of the [Anna Karenina principle](https://en.wikipedia.org/wiki/Anna_Karenina_principle). Anna Karenina starts with a famous line:

***Happy families are all alike; every unhappy family is unhappy in its own way***

What looks as a witty statement about humans, is actually a precise property of systems whose success depends on a number of factors all working well.

Since failures are born out of deficiencies in any number and combinations of factors, the amount of different *failure modes* is bound to be high in any moderately complex system. Conversely, when success is born out of all (or most) factors doing well, it creates less variance.

But I digress!

Now, if we trust this principle, one way to treat this topic could be to model software engineering as a system, identify all these factors, and write recommendations for each of them. This is too hard though!

Instead, I’ll try to address this as a doctor who visits for the first time a patient that is not feeling well. Where do you start? How should you think at the system (the team) as a whole?

So here is what I would like to cover today:

- 🥇 **Most people want to do good work** — and they generally *care* about it.

- 🔭 **Create a shared vision **— setting a *north star* goal and rallying people around it.

- 🔬 **Identify problems **— figuring out what is truly holding the team back.

- 🎌 **Find your allies** — lasting change needs bottom up support.

- 📈 **Create visible progress** — create small victories, and show them!

- 💼 **Help the team from the outside*** —* provide external help once you can show momentum.

Let’s dive in!

---

### **🥇 Most people want to do good work**

What does it even mean that a team is *struggling*?

Visible problems can be many — speed, reliability of commitment, [accuracy](https://refactoring.fm/i/167501213/precision-vs-accuracy-slides) — but there is one property, to me, that is the true mark of a struggling team: **people have capitulated**. They have gotten used to problems and believe they can’t be solved.

This is an important preface. Problems happen all the time, but as long as people are aware and working to do better, they are in a good place. Sometimes, instead, the same problems have been there for so long that people feel they have become a (nasty) part of your culture. Issues are evident, but people stop addressing them. They don’t even talk about them. It is what it is.

When problems are not addressed, you might think it’s because people don’t see them — especially if you joined a team that was already struggling, you might ask yourself: “*how tf people don’t see how bad we are doing?!*”

Well, they most likely do. But they also think there isn’t much they can do about it.

I have met and worked with hundreds of engineers, and I can confidently say >99% of **people want to do good work**. Our default state, as humans, is *caring about what we do*. When we stop, it’s because we don’t think it’s possible to do work *worth caring about*.

So what do you do?

---

### **🐘 Address the elephant in the room**

There is a time and place for small wins and iterative improvements (we’ll see later) but when you are in a hole you also need a singular moment that starts the inversion. The moment you stop digging and start climbing back.

Hard conversations need to be had sometimes, and if you are in a leadership or management position, this might be one of those times.

In my experience, there are two main things that you need to address: 1) the team is, indeed, not doing well, and 2) you care about improving. That’s it! Chances are you don’t have to bring detailed proof or numbers, because people already *know*. They won’t be surprised.

But they need to hear it: the team needs to *identify* the fact that they are falling behind, and working to get better. So they need someone who 1) addresses the elephant in the room, and 2) brings the initial spark that eventually turns into momentum.

---

### **🔭 Create a shared vision**

Once people *agree* the team is struggling, the next step is to create a shared *vision* for what a high performing team looks like.

This is useful to do *before* you even start to address problems. In an ideal world, ask people:

- *How would you spend your engineering time?*

- *What would you work on?*

- *How often would you ship features?*

- *How would you work with product and the other stakeholders?*

- *Which meetings would you have, and which not?*

- *How would CI/CD work?*

Think big, but also be realistic:

- You might love tests to run *instantly*, but you should know that e.g. 15 mins is achievable, down from 1 hour that they take today.

- Spending zero time on maintenance and tech debt is an impossible dream, but going from 60% to 30% is probably doable.

Visualize your *high-performing reality*. Imagine a sprint / dev cycle: what type of work do you commit to? How do engineers spend their time? How does communication work?

Try to run this as a mini-workshop, and write down everything. The goal is to create some initial momentum, plus giving the team a *north star* to work towards.

---

### **🔬 Identify problems**

The next step is to identify what the struggle is about.

Before you talk any specific parts of the process, what are the visible problems in the team’s *outcome*?

Here are the four big candidates:

1. 🏆 **Value** — what gets shipped isn’t valuable for customers / business. You build the wrong thing.

1. 🥇 **Quality** — what gets shipped is not polished and/or is constantly bugged.

1. 🥈 **Speed** — the team is (or is perceived as) slow.

1. 🥉 **Reliability** — the team doesn’t hold on its commitments.

Your mileage may vary, but as a rule of thumb, these matter exactly *in this order*.

![image](../assets/23fbdf02815c80b5.png)

In my experience, working on the right things is *by far* the most important factor, and what most teams struggle the most with. However, this isn’t always identified correctly: people have a lot misguided conversations about *speed*, where what they really mean is: “*we are not confident that what we ship is good, so better to ship more things faster*”.

But the reality is, teams that ship valuable + high quality stuff (#1 + #2) very rarely get questioned about speed.

Working on the right things is a function of good feedback loops with customers, and feedback loops are what make speed genuinely useful. Otherwise, you may be running fast, but in circles, without really going anywhere.

Finally, reliability — meant as meeting deadlines, making good estimates, etc — is just cherry on top. When trust is created through the other factors, you discover most deadlines are fictional and estimates are not that useful. In most cases, these are control devices meant to make up for low-trust environments, and most often failing at that. Under good conditions, instead, you can relax a lot of the process and just let people work.

So, how do you figure out what of these problems plague your team?

To me, this is the part where the process stops being workshop-ish, like in the vision stage, and becomes more continuous. You might be able to spot a bunch of these issues at once, but what you need the most is having a good feedback loop in place to intercept them as they appear.

Some of the best devices for this are [1:1 chats](https://refactoring.fm/p/how-to-run-great-11s-in-2023), [retrospectives](https://refactoring.fm/p/retrospectives), and [dev surveys](https://refactoring.fm/p/whats-next-in-measuring-dev-productivity). I have written various times about these so I am just putting some links to previous articles.

There are also [quantitative engineering metrics](https://refactoring.fm/p/how-to-get-started-with-engineering), of course. In my experience, though, they come at a later time — when the team has already a good posture towards problems and some bandwidth to go more in depth. That is, quantitative data may precisely surface that your time-to-first-PR is 14 hours, which is useful to know to track the trend, but people can (and should) already tell you in surveys and 1:1s that your PR process is shit, and that’s enough to make progress start.

---

### **🎌 Find your allies**

One thing is to correctly identify issues—and possibly even how to do better—another thing is to make change *happen*. Change is hard, and it often starts as an uphill battle against tight roadmaps and already stressed out people.

For this reason, especially for long-term transformations, it is crucial to **find your allies**, and *recruit* them.

Your allies are the people who *care the most* about this change. They are the ones who you trust will not give up when the pressure gets higher, and will keep others accountable. Long lasting change is always a combination of top-down and bottom-up input, and the bottom-up part needs *champions* to pave the road, especially at the beginning.

This reminds me of [Christine Pinto’s three-step process](https://refactoring.fm/p/my-favorite-ideas-from-ldx3) to improve quality in a team. She says quality processes in the real-world do not appear out of the blue, but are usually the final result of a messy progression that looks like this:

1. 🦸 **Crusader** — some engineer acts as a *hero* who spearheads quality, largely on their own + influencing leadership.

1. 🪴 **Coach** — the hero teaches others, establishing quality principles and adoption.

1. 🌳 **System** — when critical mass is achieved, individual efforts turn into team processes.

---

### **📈 Create momentum with visible progress**

No matter how convincing you are, and how much buy-in you got, when a team has been struggling for a while they will need to *experience success* to start believing change is possible.

Here are some ideas to create that initial momentum:

1. 🍒 **Start with low-hanging fruits** — identify a few tasks with 1) a high chance of success and 2) quick feedback loops. It should be stuff that is relatively easy to fix, but with a visible impact. The shorter the cycle between action and result, the better.

1. 📊 **Visualize improvement** — make progress visible. If the goal was to improve some KPI (e.g. bugs count, PR time, user crashes), show it. Create a simple dashboard that displays the key metrics that matter to the team. Also, trends matter more than absolute numbers: show the direction.

1. 🎉 **Celebrate successes publicly** — when the team achieves something meaningful, whatever small, make sure everyone knows about it. Demo it; write it on a public Slack channel; have a small celebration. Reinforce that progress is happening and associate quality work with positive recognition. Create a virtuous cycle where people strive to do better.

Finally, nothing is *too small* to get started. Small victories compound fast into big transformations if you keep the flywheel spinning.

---

### **💼 Help the team from the *****outside***

So far, we have covered how to address problems *from the inside*.

If you are in a management position, there is also typically a lot that you can do to help your team *from the outside*, by working with external stakeholders. If the team is falling behind, you may advocate to hire more people. You may reduce the team’s scope. You may rotate resources from/to other teams to help with bandwidth, with skills gaps, or just to shuffle things a bit. And of course you can shield the team from expectations and requests that don’t match reality.

This all makes sense but, in my experience, it is rarely enough.

True change needs to start from *within* the team and *propagate*, in order for good things to happen from the outside. Otherwise, many of these ideas not only don’t work — they can make things worse: pushback on stakeholders expectations can further reduce the trust in the team, just like hiring more people can lead to more work and stress.

Furthermore, a lot of these are the result of *negotiation*, which becomes way easier when you can demonstrate a (whatever small) trajectory of improvement, as opposed to just a depressed reality.

---

### **📌 Bottom up**

And that's it for today! Here are the main takeaways from today:

1. 🥇 **Most people want to do good work** — when teams struggle, it's usually because people have lost hope, not because they don't care. Start by acknowledging this fundamental truth.

1. 🐘 **Address the elephant in the room** — have the hard conversation upfront. People already know the team is struggling; they need someone to name it and commit to fixing it.

1. 🔭 **Create a shared vision first** — before diving into problems, align the team on what high performance looks like. Visualize your ideal product development cycle, and use it as your north star.

1. 🎯 **Focus on value over speed** — struggling teams often confuse being busy with being effective. Prioritize shipping the right things over shipping fast.

1. 🎌 **Find your champions** — lasting change requires allies who will champion improvements when you're not in the room. Find the people who care most about the transformation.

1. 📈 **Build momentum with quick wins** — start with low-hanging fruits that have high visibility. Small victories compound into major transformations when you keep the flywheel spinning.

1. 🔄 **Change must start from within** — external help (more people, reduced scope, shielding from stakeholders) rarely works unless the team first builds internal momentum for improvement.

---

See you next week!

Sincerely

Luca
