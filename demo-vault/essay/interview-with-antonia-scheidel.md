---
aliases:
  - "Interview with Antonia Scheidel"
"✏️ Status": Not started
"Belongs to":
  - "[[responsibility/publish-podcast|Publish Podcast]]"
  - "[[person/antonia-scheidel|Antonia Scheidel]]"
Status: Evergreened
URL: "https://refactoring.fm/p/automating-team-processes-gracefully"
"👓 Status": Not started
"Created time": "2025-08-27T11:53:00.000Z"
Date: 2025-09-12
"Has Notes":
  - "[[evergreen/building-automated-processes-that-work|Building automated processes that work]]"
  - "[[evergreen/use-notifications-in-automated-processes|Use notifications in automated processes]]"
Tags:
  - Podcast
  - Free
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 25cbdf02-815c-80f8-a96a-ed84207d372d
---

# Interview with Antonia Scheidel

Today's guest is [Antonia Scheidel](https://www.linkedin.com/in/antoniascheidel)!

Antonia is Director of Engineering at Duolingo, where she made the whole career progression, starting as a simple intern 12 years ago.

Antonia is an expert at designing good, automated processes for your team. We discuss how to create good automation to avoid people doing glue work, how not to become a bottleneck as a manager, and how to make the team own the process and repair it when needed.

### 🎙️ Episode

You can watch the full episode on [Youtube](https://www.youtube.com/@refactoringclub):

[Video](https://youtu.be/GK8M5tdgXi0)

Or listen to it on [Spotify](https://open.spotify.com/show/7Luds9dmzZDoDC8Q7EMbSw), [Apple](https://podcasts.apple.com/us/podcast/refactoring-podcast/id1719137305), [Overcast](https://overcast.fm/itunes1719137305), or your podcast app of choice.

---

### 🥇 Interview Summary

If you are a **🔒 paid subscriber 🔒** you will find *my own**** ****summary* of the interview below.

It’s the **10-minute, handcrafted takeaways** of what we talked about, with timestamps to the relevant video moments, for those who don’t have time to sit through the 1-hour chat.

Here is the agenda for today:

1. **👋 Antonia's Journey at Duolingo** ([**02:15**](https://youtu.be/GK8M5tdgXi0&t=135s))

1. **📊 The Project Management Problem** ([**09:57**](https://youtu.be/GK8M5tdgXi0&t=597s))

1. **🔧 Getting Out of the Manual Work Trap** ([**19:34**](https://youtu.be/GK8M5tdgXi0&t=1174s))

1. **⚡ Building Automated Processes That Work** ([**23:36**](https://youtu.be/GK8M5tdgXi0&t=1416s))

1. **🔔 Making Notifications Effective** ([**37:24**](https://youtu.be/GK8M5tdgXi0&t=2244s))

Let's dive in 👇

---

### **1) 👋 Antonia's Journey at Duolingo (**[**02:15**](https://youtu.be/GK8M5tdgXi0&t=135s)**)**

Antonia's story is quite unique in today's tech landscape. As a computational linguist by training, she discovered Duolingo when founder Luis von Ahn gave a talk during her master's program. The intersection of language and technology that Duolingo represented was exactly what she'd been studying but hadn't seen in practice.

What's remarkable is her 12-year journey at Duolingo, rising from intern to Director of Engineering. In an industry known for job-hopping, Antonia stayed because of the people:

> "Our founder likes to say that it's not just smart people, but they're kind as well. They're kind people motivated by the mission. I think everybody at Duolingo is really passionate about something."

Her transition to management wasn't planned—it happened when her admired team lead asked her to take over the role. This gave her a unique perspective on what management actually entails, moving from thinking people-focused work was "not really engineering" to realizing it was now her core responsibility.

### **2) 📊 The Project Management Problem (**[**09:57**](https://youtu.be/GK8M5tdgXi0&t=597s)**)**

Antonia leads Duolingo's retention team, which owns the streak mechanic—one of the app's most visible features. Her team runs more experiments than most at the company (over 600 in the streak area alone), creating a unique scaling challenge.

The problem was classic but painful: engineers needed to update project management systems (Jira) to reflect the status of their experiments, but the manual updates rarely happened consistently.

> *"I found myself asking each engineer: 'Hey, what's the status of this project? Do you think we'll have it in this release or the next one?' When you have 12 experiments, it's 12 conversations."*

What made it worse was that Antonia had built automation to pull from Jira for stakeholder updates, but the system contained stale information. Engineers would update tickets once, then focus on actual work when timelines shifted, leaving the project management system increasingly out of sync with reality.

The emotional toll was significant—Antonia felt like she was becoming "their mother," constantly nagging about administrative tasks rather than doing the mentoring and strategic work that management should entail.

### **3) 🔧 Getting Out of the Manual Work Trap (**[**19:34**](https://youtu.be/GK8M5tdgXi0&t=1174s)**)**

The turning point came when Antonia prepared for her two-month sabbatical (a Duolingo benefit after 10 years). Looking at the tasks she'd need others to cover, she realized they looked terrible—no one would see them as development opportunities.

> "I had this vision of being the silent protector, shielding my team from all these administrative missiles. But when I tried to hand off these tasks, I realized: if it's not worthy work for me to ask others to do, why am I doing it?"

The deeper problem was that when Antonia got tired of asking people to update systems, she started doing the updates herself. This created a vicious cycle:

- 🔄 **Hidden work multiplication** — She was spending hours post-processing incorrect information from systems

- 😤 **Relationship damage** — Constant nagging about administrative tasks was affecting her relationships with engineers

- ⏰ **Energy drain** — The emotional heaviness of these interactions left less energy for actual coaching and leadership

This realization forced her to fundamentally rethink the process rather than just trying harder to enforce compliance.

### **4) ⚡ Building Automated Processes That Work (**[**23:36**](https://youtu.be/GK8M5tdgXi0&t=1416s)**)**

Antonia's solution was elegant: distinguish between information that exists elsewhere versus information that only exists in people's heads.

For Duolingo's experiment lifecycle, most status updates were just copying information from their internal experimentation system to Jira. Engineers would hit "launch experiment" in one system, then manually update Jira to say "experiment launched."

> "I really am just asking people to copy information from one place to another. Is there a way to not do that and focus just on the parts that really exist only in people's heads?"

Her approach involved three key elements:

- **🔗 System integration** — Hook up project management to existing sources of truth automatically

- **🧠 Focus on human-only information** — Only ask people for information that genuinely exists nowhere else (like delivery estimates)

- **📢 Stakeholder notifications** — Use automation to notify downstream stakeholders (designers, QA) when their input is needed

This dramatically reduced the manual work while ensuring the information that truly mattered—delivery estimates and timeline changes—still flowed to the right people at the right time.

### **5) 🔔 Making Notifications Effective (**[**37:24**](https://youtu.be/GK8M5tdgXi0&t=2244s)**)**

The key insight was making notifications feel like system accountability rather than managerial nagging. When a feature was ready for design review, both the engineer and designer would be tagged in a public channel notification.

> *"It brought the engineers into the conversation. Now when something wasn't ready, it was easy for the engineer to say, 'Hey, sorry designer, we're pushing this back a week.' The responsibility shifted from being toward me to being toward each other."*

Antonia's notification strategy followed specific principles:

- **👥 Two-person tagging** — Always tag both stakeholders to create mutual accountability

- **📍 Public but focused channels** — Use team channels with other conversations, not dedicated notification-only channels

- **⚠️ Escalating reminders** — Private message first, then public tag if the issue persists

- **🚫 Volume limits** — Maximum 5 notifications per day to avoid notification blindness

The most important aspect was helping people understand they had "responsibility to the process" like a classroom pet—a shared system everyone needed to help maintain, rather than something the manager was personally demanding.

This transformed the dynamic from "Why should I do this for Antonia?" to "We need to help this automated system work properly," making compliance feel collaborative rather than punitive.

---

### 🙏 Thank you

Thank you so much for reading & listening! Let me know what you think about the podcast and the brand new summaries in the comments or via email!

We just got started with the Podcast, so if you found this chat valuable, please consider **subscribing to the show** on [YouTube](https://www.youtube.com/@refactoringclub), [Apple](https://podcasts.apple.com/us/podcast/refactoring-podcast/id1719137305), or [Spotify](https://open.spotify.com/show/7Luds9dmzZDoDC8Q7EMbSw).

Also, consider **giving us a rating** or leaving a review on the platform of your choice, as that really helps other listeners find the show.

See you next week! 👋

Luca

### 🐦 Linkedin / Twitter
