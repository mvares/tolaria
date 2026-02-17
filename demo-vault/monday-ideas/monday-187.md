---
aliases:
  - "Monday #187"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-monday-idea|Publish Monday Idea]]"
Status: Published
"👓 Status": Not started
"Created time": "2025-12-18T16:30:00.000Z"
Date: 2025-12-22
"Has Notes":
  - "[[evergreen/the-age-of-everything-as-code|The age of everything-as-code]]"
  - "[[evergreen/tech-debt-is-bad-only-if-you-need-to-change-the-code|Tech debt is bad only if you need to change the code]]"
  - "[[evergreen/use-notifications-in-automated-processes|Use notifications in automated processes]]"
Tags:
  - Monday
  - Free
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 2cdbdf02-815c-8082-8503-cc5f692ea014
---

# Monday #187

### 1) 💻 Everything as Code

One of the things on which AI is remarkably worse than humans is at using GUIs and navigating websites.

It is *widly* better at writing code, which means that in your tech stack it makes sense to use code—instead of graphical interfaces—whenever you can.

We discussed this several times lately: I discovered that Shopify [betted the farm](https://refactoring.fm/i/167520760/everything-as-code) on **configuration as code**, and Convex [goes even beyond](https://refactoring.fm/p/how-to-design-your-tech-stack-for) and talks about **everything as code**.

This strategy has *always* brought benefits — reproducibility, version control, self-documentation, automation — but at the expense of more cumbersome UX and having people need to remember complex DSLs. The good thing is that the downsides have largely disappeared now, because AI is extremely good at writing this stuff, leaving you mostly with the upsides.

Linking below the article I wrote with Jamie from Convex, which explains this well 👇 

[https://refactoring.fm/p/how-to-design-your-tech-stack-for](https://refactoring.fm/p/how-to-design-your-tech-stack-for) 

---

### 2) 🐛 Bad code is bad only if it needs to be changed

I love the definition of bad code as code that’s hard to change.

But when you think about it, this is only a problem if you actually *need* to change it. Bad code that's *stable* isn't concerning by itself.

So, your tech debt work should be focused on what Adam Tornhill calls **hotspots**: parts of your codebase that are both 1) problematic, and 2) frequently changed.

While this seems obvious, humans are bad at **judging this *****intuitively***. So most tech debt work is misguided: it targets either bad-but-stable code, or active areas already in good shape.

This is also hard to evaluate because *activity distribution* is extremely skewed: in most codebases, **~5% of the code gets 90% of the activity **(see article at the end for sources).

This reminds me of something from my startup days.

During an M&A conversation, the buyer's consulting firm ran a technical due diligence. They found several areas of poor quality code—as we expected. In fact, over time we had doubled down on specific parts of the product we cared about, while phasing out others. The latter stayed experimental: less testing, more duplication, etc.

What I didn't expect was how hard this proved to argue. We pointed to the strategic core we were proud of, but they weighted sketchy marginal code as an equal part of the whole.

In other words, the **frequency of change** wasn't considered.

Eventually the M&A failed for a variety of reasons. This was not explicitly mentioned as a blocker, but I always suspected it contributed.

You can find the full article from my chat with Adam below 👇

[https://refactoring.fm/p/how-to-work-on-the-right-tech-debt](https://refactoring.fm/p/how-to-work-on-the-right-tech-debt)

---

### 3) 🔔 Use notifications for process accountability

In September [I interviewed Antonia Scheidel](https://refactoring.fm/p/automating-team-processes-gracefully) from Duolingo, who told me how she was able to create reliable automated processes for her team.

A key insight from her story is the **tactical use of notifications**. Antonia uses them to create what she calls *system accountability*, rather than invasive micromanagement. For example, when a feature is ready for design review, both the engineer and designer are tagged in a public channel notification:

> *"It brought the engineers into the conversation. Now when something wasn't ready, it was easy for the engineer to say, 'Hey, sorry designer, we're pushing this back a week.' The responsibility shifted from being toward me to being toward each other."*

Antonia's notification strategy follows specific principles:

- **👥 Two-person tagging** — always tag both stakeholders to create mutual accountability.

- **📍 Public but focused channels** — use team channels where other conversations happen, not dedicated notification-only channels.

- **⚠️ Escalating reminders** — DM first, then public tag if the issue persists

- **🚫 Volume limits** — maximum 5 notifications per day, to avoid notification blindness

The most important aspect was helping people understand they had **responsibility to the process**, like a classroom pet—a shared system everyone needed to help maintain, rather than something the manager was personally demanding.

This transformed the dynamic from "*Why should I do this for Antonia*?" to "*We need to help this automated system work properly,*" making compliance feel collaborative rather than punitive.

Here is the full interview with Antonia:

[https://youtu.be/GK8M5tdgXi0](https://youtu.be/GK8M5tdgXi0)

You can also find it on 🎧 [**Spotify**](https://open.spotify.com/episode/18vtH7uq3QSc8SapYUnAP1?si=b8f8f9c4254248e5) and 📬 [**Substack**](https://refactoring.fm/p/automating-team-processes-gracefully)
