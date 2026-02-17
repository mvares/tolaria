---
aliases:
  - "How to advocate for tech debt"
"Is A":
  - Evergreen
"Last Tweeted": 2024-07-31
Tags:
  - Has Pic
"Created at": "2024-06-21T07:00:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to":
  - "[[essay/lessons-from-the-mastermind-sessions|Lessons from the Mastermind sessions]]"
  - "[[monday-ideas/monday-124|Monday #124]]"
"Updated at": "2024-10-04T07:06:00.000Z"
Status: Not started
Tweet: "CTOs, are you struggling to advocate for tech debt work? It’s time to ditch separate tech roadmaps. Integrate tech debt into your main product roadmap and treat it as essential business work. Use data to show how it impacts customer experience, team productivity, and product innovation. Build trust with a track record of small wins and involve stakeholders early. Frame it as an opportunity, not an obligation. Let's discuss how to unlock business potential through tech work! #TechDebt #CTO #Leadership"
notion_id: af9dfe4d-a966-4b79-a2b1-b320432bea05
---

# How to advocate for tech debt

A CTO confessed they feel unable to advocate for big tech debt work. How can they convince other executives that some technical work is worth doing?

A few weeks ago we [interviewed Laura Tacho](https://refactoring.fm/p/engineering-productivity-and-developer), CTO at DX. At some point, she said something that stuck with me: **technical roadmaps are destined to fail**. She meant technical roadmaps *as in* roadmaps that are separate from the main product one.

In fact, I believe the (not-so) secret to getting big tech work done is to treat it as normal work: you negotiate it and prioritize it based on the opportunity of getting it done.

So my first advice is 👇

#### Bring data 🔍

> *In God we trust. All others must bring data.*
— Edwards Deming, Economist

When it comes to refactoring, migrations, and other work under the hood, I have found that there are three types of data you can use to advocate for it:

1. 🏅 **Customer KPIs** — the impact of bad code can easily leak to customers through outages, latency, or reported bugs. This is the easiest angle for business stakeholders to understand, and the first you should look into.

1. 🚚 **Productivity** — chances are your dev experience is impacted by the debt. You can measure this in terms of time spent on maintenance, code churn, or other metrics about specific parts of the dev process (e.g. your CI/CD got slower and slower and it now takes 2 hours to deploy). Being able to say “if we get this done we can ship 10% more features”, backed by convincing numbers, is powerful.

1. 🔭 **Enablement** — finally, consider product evolution. Does this work *enable *product features we couldn’t do before? In my experience, the enablement angle is the best way to *partner *with* *PMs on debt, which in turn is one of the most effective ways to get things done.

Now, sometimes data is not enough. Sometimes you don’t have enough of it, or you believe you have, but it’s not enough for your *interlocutors*.

![Tracking your engineering investment (e.g. this is Swarmia) is useful to advocate for work that reduces KTLO, or to showcase the before-and-after from previous success stories.](https://prod-files-secure.s3.us-west-2.amazonaws.com/631d83ff-20ce-4401-a614-56e2c0f97767/eb861b29-52fc-4be1-81db-4338edc1a6a3/CleanShot_2023-04-26_at_11.06.132x.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665WISTPQO%2F20260131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260131T190631Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDGPiILh9vSJWXCVv%2FPCpHOesDI%2Boi7CQltG595liRrAQIgQf8Rfk69HjsryGQCcbn3HQSfyRNbQYc0l4nrNAk7SxAqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAHVBw%2BXnMbKbJaoSSrcA4aqPUmhuvwPW2ZGyX3ptz4skseuufXZhzwBgqZdsE5hBrZ8Oliauj2Q7hN8VBj26vRAYMXqFoVUgupewuCqxQo%2BEFN%2FO0C4liPgjVljtEQrNAMEvvpHM9348ZYTZj9dCWnBGBM%2FHThlDeyt0ukDISHvGuOiB0VyYkoyB7VDNnd%2BL9BI07T7Bm7ErSN3EDN36djfWdSrBCSmdXpXuzHL%2FukFuvrZP0P4SIJ2syayYEQl8lkKJQY37HlFcQ6nx3By86gNdsKiU5g0NI0XDZJ3oH6SXojMgNGlU6qYaTiyu9MCg6Ft%2FxkI1hLhXQ%2FtjEbjhCOxTVmEgNqgYzZg6YXLHFCir%2F5wO08tD7iOtvtXyYllKPaJRfnNf7EoBDKStyVCIn7WcRlP0PJAr5J78J1najXA9iIms8IKnxFT%2F%2B5tAG2uqdL8VVDulX2i%2BWQr3hzVaMrAWFz0e111dMoUFTXXmzvTuLUZDxxVkubq0MSGD68lnpoZylt0aB0u%2Bd4kLeYa57BRYms5x7U4W0rKti%2BpC5AKVBqwrCVypxnffWmz2wlX1YxSWRfMgYELT%2FrNgnk9MTLDwPp1fcEMp%2FE%2FZ51X8NpswaShezZ3WS4jCmKo%2FcE%2BtF1%2BVvHZO0G9LJsSMJWN%2BcsGOqUBR0NlxXEELdL%2FNeiZJtenYEZ51ilqhmNhoUHp1oDnXJ4zegR3SmTSeiz7V%2FGwEyD4dc2%2BygujVf%2B86V5%2BuZY1GYDm1LBDPAnLzK%2BCKL3ReC5bO9FU8m85Xv3BODTChy0f22N5XdO4WL95hdiyLptWGK6dq51GHeEs%2Bc768img3knq7A%2BG%2BjruHK%2BN6wSxiav%2B4hkhRbQHqoTRb0LTYoVIMULI2KPb&X-Amz-Signature=8be7cccd5670355111111736cfd3b0bebd96b06191d5ade2a25513f2e9db835f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

This is where trust comes into play 👇

#### Create trust ❤️

There is a famous quote, by economist Edwards Deming, which says “*In God we trust. All others must bring data*”.

I have seen it used often in product teams and I *disagree* with it — to Deming’s credit, though, he was referring to scientific research, not product work.

There is *a ton* of work that gets done purely because of trust. And that’s ok. Trust makes* *work faster and riskier — which, in many cases, is a good tradeoff.

The impact or trust is also not black or white. A successful argument might be based on 80% data and 20% trust, or 50:50, or you name it.

More trust can *compensate* for less data, so, for tech debt work, if you can’t get your point across, you can either bring more data, or more trust.

To do the latter, here is my advice 👇

#### Create a track record 🥇

Advocating for tech work is easier when you have a successful history of tackling other tech work. 

You can bring this up explicitly in conversation, showing success stories from the past where similar actions led to similar benefits.

If you don’t have such track record, start building it, and start small: solve small pieces of debt, document it, and celebrate it. Build momentum and confidence that you can take larger actions.

#### Involve others in the decision process 🔄

Another strong element to build trust is by involving others *early* in the process. Partner *early* with peers, PMs, and people whose opinion is legitimately important for your cause.

Partner with them when you are still *unsure* that the work is worth doing, and get to a conclusion together.

Conversely, do not autonomously decide for a course of action and *then* make the case to justify it to others. This can come across as disingenuous, and people may feel you are pushing some personal agenda.

#### Don’t make it all-or-nothing ⚖️

Finally, whenever possible, present different levels of investment.

Maybe the leadership isn’t ready to commit to a 6-month rework, but they would test the waters with a 1-month proof of concept. You may 1) do the most important piece first, in a fraction of the time, 2) show success, and 3) get green light for the rest of the work.

---

A fellow CTO recently confessed they feel powerless in advocating for critical technical work 🔨

Sounds familiar? Let's flip this!

In my experience, here is how to convince your exec team that addressing tech debt is not just necessary, but strategic:

1️⃣ 𝗗𝗶𝘁𝗰𝗵 𝘁𝗵𝗲 𝘀𝗲𝗽𝗮𝗿𝗮𝘁𝗲 𝘁𝗲𝗰𝗵 𝗿𝗼𝗮𝗱𝗺𝗮𝗽

Laura Tacho, CTO at DX, nailed it in our recent podcast interview: “Technical roadmaps are destined to fail“. Instead, integrate tech debt work into your main product roadmap.

Treat it as what it is - essential business work.

2️⃣ 𝗦𝗽𝗲𝗮𝗸 𝘁𝗵𝗲 𝗹𝗮𝗻𝗴𝘂𝗮𝗴𝗲 𝗼𝗳 𝗯𝘂𝘀𝗶𝗻𝗲𝘀𝘀

To turn tech debt into business work, back your case with three types of data:

↳ 🎯 𝗖𝘂𝘀𝘁𝗼𝗺𝗲𝗿 𝗞𝗣𝗜𝘀 — show how tech debt directly impacts user experience (outages, latency, bugs).

↳ 📈 𝗣𝗿𝗼𝗱𝘂𝗰𝘁𝗶𝘃𝗶𝘁𝘆 𝗺𝗲𝘁𝗿𝗶𝗰𝘀 — quantify the drain on your team's efficiency. Measure how much time your team is spending on related maintenance.

↳ 🚀 𝗘𝗻𝗮𝗯𝗹𝗲𝗺𝗲𝗻𝘁 𝗽𝗼𝘁𝗲𝗻𝘁𝗶𝗮𝗹 — highlight features and innovation this work unlocks. Partner with PMs on this.

3️⃣ 𝗕𝘂𝗶𝗹𝗱 𝘁𝗿𝘂𝘀𝘁 𝘁𝗵𝗿𝗼𝘂𝗴𝗵 𝘁𝗿𝗮𝗰𝗸 𝗿𝗲𝗰𝗼𝗿𝗱

Can't get traction with data alone? Build progressive trust:

↳ ✅ 𝗦𝘁𝗮𝗿𝘁 𝘀𝗺𝗮𝗹𝗹 — tackle minor debt, document wins, build momentum.

↳ 🤝 𝗖𝗼𝗹𝗹𝗮𝗯𝗼𝗿𝗮𝘁𝗲 𝗲𝗮𝗿𝗹𝘆 — involve stakeholders in the decision process from day one.

↳ 🎛️ 𝗢𝗳𝗳𝗲𝗿 𝗼𝗽𝘁𝗶𝗼𝗻𝘀 — present tiered solutions. A 1-month POC might pave the way for that 6-month overhaul.

More trust can compensate for less data.

Finally, frame it as an opportunity, not an obligation. That’s were the whole debt metaphor looks misleading to me. It's not about "repaying debt" - it's about unlocking business potential.

How do you advocate for critical tech work in your org? Let’s discuss tactics in the comments!

—

♻️ If you found this valuable, please repost it to your friends. It means a lot to me!
