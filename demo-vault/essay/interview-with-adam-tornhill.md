---
aliases:
  - "Interview with Adam Tornhill"
"✏️ Status": Not started
"Belongs to":
  - "[[responsibility/publish-podcast|Publish Podcast]]"
  - "[[person/adam-tornhill|Adam Tornhill]]"
Status: Evergreened
URL: "https://refactoring.fm/p/technical-debt-as-crime-scene-with"
"👓 Status": Not started
"Created time": "2025-07-30T07:35:00.000Z"
Date: 2025-08-29
"Has Notes":
  - "[[evergreen/code-quality-has-astounding-business-impact|Code quality has astounding business impact]]"
  - "[[evergreen/static-analysis-is-not-enough-for-code-quality|Static analysis is not enough for code quality]]"
  - "[[evergreen/the-bus-factor-problem|The bus factor problem]]"
Tags:
  - Podcast
  - Free
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 240bdf02-815c-8096-9ea8-eb70c6e71ab6
---

# Interview with Adam Tornhill

### Notes

---

Today's guest is [Adam Tornhill](https://se.linkedin.com/in/adam-tornhill-71759b48)! 


Adam is the author of the popular book Your Code as a Crime Scene, and he's the founder of Code Scene. 

With Adam, we discussed 

- His unique insights about technical debt and code quality, which come from his study of forensic psychology. 

- We explored how static analysis is not enough to understand code health and why you need to look into version control history to understand hotspots, change distribution and bus factor. 

- And finally, we inevitably talked about AI and how it changes, or maybe does not change, how we should write code.

### 🎙️ Episode

You can watch the full episode on [Youtube](https://www.youtube.com/@refactoringclub):

[Video](https://youtu.be/PhWtlhfrsWI)

Or listen to it on [Spotify](https://open.spotify.com/show/7Luds9dmzZDoDC8Q7EMbSw), [Apple](https://podcasts.apple.com/us/podcast/refactoring-podcast/id1719137305), [Overcast](https://overcast.fm/itunes1719137305), or your podcast app of choice.

---

### 🥇 Interview Summary

If you are a **🔒 paid subscriber 🔒** you will find *my own**** ****summary* of the interview below.

It’s the **10-minute, handcrafted takeaways** of what we talked about, with timestamps to the relevant video moments, for those who don’t have time to sit through the 1-hour chat.

Here is the agenda for today:

1. 🔍 **Adam's Journey from Psychology to Code Analysis** ([02:19](https://youtu.be/PhWtlhfrsWI&t=139s))

1. 🕵️ **Why Static Analysis Isn't Enough** ([08:27](https://youtu.be/PhWtlhfrsWI&t=507s))

1. 📊 **The Business Impact of Code Quality** ([14:35](https://youtu.be/PhWtlhfrsWI&t=875s))

1. 🚌 **The Bus Factor Problem** ([22:39](https://youtu.be/PhWtlhfrsWI&t=1359s))

1. 🤖 **AI and Code Quality: The Unexpected Connection** ([34:53](https://youtu.be/PhWtlhfrsWI&t=2093s))

Let's dive in 👇

---

### 1) 🔍 Adam's Journey from Psychology to Code Analysis ([02:19](https://youtu.be/PhWtlhfrsWI&t=139s))

Adam's path to revolutionizing code analysis began in an unexpected place: forensic psychology. After years of writing software and witnessing the consistent failure of large-scale projects, he decided to look outside the tech industry for answers.

His studies in forensic psychology introduced him to geographical offender profiling, a statistical method used by investigators to identify crime hotspots and predict where offenders might be found. This technique fascinated Adam because it could take vast geographic areas and quickly narrow them down to small, high-probability zones.

> ***"It really struck me how fascinating it is that you can pick up a map of a vast geography and pretty soon you can shrink it down to a small part that forensic psychologists call a hotspot."***

The analogy clicked: what if the same approach could be applied to massive codebases? Instead of analyzing millions of lines of code randomly, teams could identify the specific areas most likely to contain problematic code — their technical debt "hotspots."

This insight became the foundation for both his book "Your Code as a Crime Scene" and later his company CodeScene.

---

### 2) 🕵️ Why Static Analysis Isn't Enough ([08:27](https://youtu.be/PhWtlhfrsWI&t=507s))

Traditional static analysis tools examine code at a single point in time, but Adam argues this approach fundamentally misses the most critical aspect of code complexity: **impact and relevance**.

The problem with static analysis becomes clear when teams spend months rewriting the most complex parts of their codebase, only to see no improvement in performance metrics. Why? Because they've optimized code that hasn't been touched in five years and likely never will be again.

> *"Static analysis lacks the most important part of code complexity and that is impact and relevance. You can have the most complicated code in the world, but if it's been stable in production for five years, there's nothing urgent on the roadmap."*

Adam's solution involves **analyzing version control history** to understand developer behavior patterns. This reveals a surprising but consistent finding across hundreds of codebases:

- 🎯 **The 2-3% Rule** — the majority of development work concentrates in just 2-3% of the total codebase

- 📈 **Pareto Distribution** — change frequency follows a steep power law, with most code in a "long tail" of rarely-touched files

- 🔥 **Hotspot priority** — technical debt in these highly-active areas becomes exponentially more expensive.

This behavioral analysis transforms how teams should think about technical debt prioritization.

---

### 3) 📊 The Business Impact of Code Quality ([14:35](https://youtu.be/PhWtlhfrsWI&t=875s))

One of the strongest criticisms of technical debt work is that its business value remains unclear. Adam's research team tackled this head-on with their "Code Red" study, which analyzed the correlation between code health and development performance.

The findings were striking and provided hard data for what many developers intuitively knew:

- ⚡ **Development Speed** — healthy code enables teams to develop features more than twice as fast as unhealthy code

- 📉 **Predictability Crisis** — unhealthy code creates massive variance in task completion times, making estimation nearly impossible

- 💸 **Hidden Costs** — some tasks in unhealthy code can take up to 10 times longer than expected

> ***"Doing a task in unhealthy code can actually take up to an order of magnitude longer — 9 times, 10 times longer. And that translates into a bunch of undesirable side effects for the business."***

CodeScene's approach to measuring code health combines 25 different factors that contribute to bad code quality — from low cohesion to deep nesting complexity — creating a comprehensive 10-point scale that correlates with real development outcomes.

The research also revealed that **who makes the change** significantly impacts these numbers, with unfamiliar developers taking twice as long to modify unhealthy code, creating substantial hidden onboarding costs.

---

### 4) 🚌 The Bus Factor Problem ([22:39](https://youtu.be/PhWtlhfrsWI&t=1359s))

Perhaps one of the most alarming findings from Adam's analysis is the widespread exposure to "bus factor" risk — how many people can leave an organization before code becomes unmaintainable.

The numbers are sobering: in a typical codebase with 50 developers working on millions of lines of code, the bus factor might be as low as just 2-3 people.

> ***"It turns out that almost all codebases, no matter how large the development team is, are quite exposed to a risk known as the bus factor... your bus factor might be as low as just two, three people, which is really, really scary."***

This concentration happens due to several factors:

- 🏗️ **Early contributor advantage** — developers who join projects early create more code when there are fewer constraints

- 🧠 **Historical knowledge** — long-term contributors accumulate deep understanding of decisions and context

- ⚡ **Productivity differences** — individual capability variations compound over time

Adam's approach to mitigating bus factor risk involves combining three analyses:

- Identifying which areas would be impacted if key people left

- Determining whether those areas are hotspots (frequently changed) or stable

- Assessing the code health of at-risk areas

When code checks all three risk boxes, Adam recommends pairing knowledge-holders with other team members for collaborative refactoring — simultaneously distributing knowledge and improving code quality.

---

### 5) 🤖 AI and Code Quality: The Unexpected Connection ([34:53](https://youtu.be/PhWtlhfrsWI&t=2093s))

Despite the AI coding revolution, Adam offers a surprisingly contrarian view: AI hasn't fundamentally improved our ability to understand code quality, and it may have made good engineering practices even more important.

His core argument centers on a fundamental misunderstanding of where the development bottleneck actually lies:

> ***"Using AI to write more code faster is a very impressive solution to the wrong problem. Writing code is not a bottleneck for a developer. We spend five, maximum 10% of our work week writing code. The majority of the time — 70% — is spent trying to understand what's already there."***

However, Adam discovered something encouraging: **AI-friendly code turns out to be human-friendly code**. The same principles that make code readable and maintainable for humans — clear naming, good structure, expressed intent — also help AI tools work more effectively.

This creates an interesting dynamic where organizations trapped in technical debt may find themselves "not AI ready" because their code quality prevents them from safely and reliably applying AI tools.

Recent studies have shown mixed results for AI coding tools, with some research indicating that AI can actually make developers 20% slower at fixing bugs, suggesting the technology still has significant limitations in real-world scenarios.

Adam's company is focusing on using AI not to write more code, but to help developers understand and improve existing code — addressing the actual bottleneck in software development rather than optimizing for the wrong problem.

---

### 🙏 Thank you

Thank you so much for reading & listening! Let me know what you think about the podcast and the brand new summaries in the comments or via email!

We just got started with the Podcast, so if you found this chat valuable, please consider **subscribing to the show** on [YouTube](https://www.youtube.com/@refactoringclub), [Apple](https://podcasts.apple.com/us/podcast/refactoring-podcast/id1719137305), or [Spotify](https://open.spotify.com/show/7Luds9dmzZDoDC8Q7EMbSw).

Also, consider **giving us a rating** or leaving a review on the platform of your choice, as that really helps other listeners find the show.

See you next week! 👋

Luca

### 🐦 Linkedin / Twitter
