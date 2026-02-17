---
aliases:
  - "Interview with Birgitta Böckeler"
"✏️ Status": Not started
"Belongs to":
  - "[[responsibility/publish-podcast|Publish Podcast]]"
  - "[[person/birgitta-boeckeler|Birgitta Boeckeler]]"
Status: Evergreened
URL: "https://refactoring.fm/p/navigating-ai-development-workflows"
"👓 Status": Not started
"Created time": "2025-09-25T11:02:00.000Z"
Date: 2025-09-26
"Has Notes":
  - "[[evergreen/reward-critical-thinking-about-ai-both-optimists-and-skeptics-birgitta-boeckeler|Reward critical thinking about AI — both optimists and skeptics (Birgitta Boeckeler)]]"
  - "[[evergreen/ai-productivity-impact-depends-on-many-factors-birgitta-boeckeler|AI productivity impact depends on many factors (Birgitta Boeckeler)]]"
Tags:
  - Podcast
  - Free
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 279bdf02-815c-8044-8fbe-d234681b0310
---

# Interview with Birgitta Böckeler

Today's guest is Birgitta Böckeler!

Birgitta is is a distinguished engineer and global lead for AI-assisted software delivery at ThoughtWorks. Her full-time work is to figure out how engineering teams can make the most out of AI.

With Birgitta we talked about:

- her favorite workflows, how she uses AI in the IDE, in the terminal or in a genetic mode. 

- we discussed AI impact on productivity and what the best teams are getting right, which others are not. 

- we talked about how AI impacts both junior and senior engineers and how we can get the best out of both skeptics and optimists.

### 🎙️ Episode

You can watch the full episode on [Youtube](https://www.youtube.com/@refactoringclub):

Or listen to it on [Spotify](https://open.spotify.com/show/7Luds9dmzZDoDC8Q7EMbSw), [Apple](https://podcasts.apple.com/us/podcast/refactoring-podcast/id1719137305), [Overcast](https://overcast.fm/itunes1719137305), or your podcast app of choice.

---

### 🥇 Interview Summary

If you are a **🔒 paid subscriber 🔒** you will find *my own**** ****summary* of the interview below.

It’s the **10-minute, handcrafted takeaways** of what we talked about, with timestamps to the relevant video moments, for those who don’t have time to sit through the 1-hour chat.

Here is the agenda for today:

1. 🚀 **Birgitta's Role at ThoughtWorks** ([01:42](https://youtu.be/65ctfy3Rmgc&t=102s))

1. 🛠️ **AI Coding Workflows and Tool Preferences** ([07:36](https://youtu.be/65ctfy3Rmgc&t=456s))

1. 📊 **The Productivity Impact Debate** ([21:50](https://youtu.be/65ctfy3Rmgc&t=1310s))

1. 🎯 **What High-Performing Teams Get Right** ([27:58](https://youtu.be/65ctfy3Rmgc&t=1678s))

1. 👥 **Impact on Junior vs Senior Engineers** ([42:04](https://youtu.be/65ctfy3Rmgc&t=2524s))

Let's dive in 👇

---

### 1) 🚀 Birgitta's Role at ThoughtWorks ([01:42](https://youtu.be/65ctfy3Rmgc&t=102s))

Birgitta holds a unique position as Distinguished Engineer and Global Lead for AI-Assisted Software Delivery at ThoughtWorks, a role created specifically in June 2023 as AI tools began gaining mainstream adoption.

Her work spans multiple dimensions: internal subject matter expertise, client consultation, hands-on experimentation, and knowledge sharing. A typical week might include brainstorming sessions with other distinguished engineers, experimenting with generating codebases from requirements, creating presentations for clients, and running "AI for software state of play" sessions with executive teams.

> "June 2023 was around the time that GitHub Copilot started becoming a lot more popular. It was already quite obvious that there was something happening here that would fundamentally change software delivery."

The role reflects ThoughtWorks' recognition that AI would require dedicated expertise to navigate effectively. Birgitta emphasizes that even being "early" in 2023 felt late at the time—a common experience in the rapidly evolving AI landscape where everyone feels behind despite being at the forefront.

### 2) 🛠️ AI Coding Workflows and Tool Preferences ([07:36](https://youtu.be/65ctfy3Rmgc&t=456s))

Birgitta experiments with multiple tools but currently favors Windsurf and Claude Sonnet models consistently across different platforms. She identifies two key dimensions in AI coding tools:

- 💻 **IDE vs Terminal** — She prefers IDE integration for access to Git diffs, linting errors, and debugging tools, though acknowledges Claude's terminal-based approach has strong appeal due to keyboard-centric workflows

- 🤖 **Augmentation vs Autonomous** — She strongly favors human-in-the-loop workflows over autonomous agents that generate large changesets

The core concern with autonomous approaches centers on risk management and code review challenges:

> *"When you send off an agent and it creates a large changeset, I have to think a lot about the risk and review everything at once. Whereas when I have a session where I'm the human in the loop, I can go step by step and review step by step."*

Birgitta views the non-deterministic nature of LLMs as a fundamental feature rather than a bug—hallucinations are simply "intelligence when it does what we want" and problematic when it doesn't. This inherent unpredictability makes large autonomous changes particularly risky for production systems.

### 3) 📊 The Productivity Impact Debate ([21:50](https://youtu.be/65ctfy3Rmgc&t=1310s))

The stark contrast between bold productivity claims and modest research findings stems from AI's "Swiss army knife" nature—dramatically effective in some contexts, completely ineffective in others.

Several factors explain the variation in reported impact:

- 🔧 **Task dependency** — Converting SQL scripts might save 70% time, while working with proprietary libraries shows no benefit

- ⏱️ **Coding vs total work** — If teams spend only 30% of time coding, even perfect coding acceleration yields limited overall improvement

- 🏗️ **System bottlenecks** — Coding faster doesn't help if CI/CD, deployment, or decision-making processes are the limiting factors

> *"If your continuous integration and automation setup is a mess, then giving them a coding assistant to write code faster is not going to resolve that bottleneck."*

The productivity impact also varies dramatically based on developer experience levels, codebase complexity, and tech stack familiarity. A developer who's already extremely fast in their familiar environment may see minimal gains, while others might experience significant acceleration in learning and exploration tasks.

### 4) 🎯 What High-Performing Teams Get Right ([27:58](https://youtu.be/65ctfy3Rmgc&t=1678s))

The most successful teams with AI combine critical thinking with ambitious experimentation, avoiding the extremes of blind faith or complete skepticism.

Key characteristics of high-performing AI-enabled teams:

- 🔍 **Critical evaluation** — They don't treat AI output as party tricks but analyze what it actually produced and its implications

- 🛡️ **Process adaptation** — They modify workflows to mitigate risks, using features like hooks and reusable prompts strategically

- 🎯 **Balanced culture** — They reward both skepticism and optimism when grounded in real experiments and evidence

> "Critical thinking, married with some ambition and some excitement still about this and trying things, I think that's the key. You have to always reward critical thinking, whether it's skepticism or optimism."

However, Birgitta notes a fundamental challenge: it's often impossible to prove which specific customizations or practices actually improve outcomes, making evidence-based optimization difficult even for experienced teams.

### 5) 👥 Impact on Junior vs Senior Engineers ([42:04](https://youtu.be/65ctfy3Rmgc&t=2524s))

The impact on different experience levels is nuanced, with both juniors and seniors facing unique challenges in adapting to AI-assisted development.

For junior engineers, the primary concern involves learning fundamentals when AI can generate solutions without requiring deep understanding. The traditional learn-by-doing approach—building abstractions through repeated exposure to details—becomes complicated when AI handles implementation.

Senior engineers face a different challenge: adapting to non-deterministic tools after years of working with predictable, deterministic systems:

> *"I do think this is a real cognitive shift because of the non-determinism. We're not used to that. I see some people trying to shoehorn generative AI into that same space like being something that automates and then being disappointed when it doesn't fully do that."*

Birgitta emphasizes that experienced engineers who mentor others have an obligation to understand and use AI tools, even if skeptical. The traditional engineering skills—risk assessment, understanding system interconnections, recognizing long-term maintainability issues—remain crucial for evaluating AI-generated code effectively.

The key insight is that both junior and senior engineers need to develop new skills while maintaining their core competencies, rather than one group simply replacing the other.

---

### 🙏 Thank you

Thank you so much for reading & listening! Let me know what you think about the podcast and the brand new summaries in the comments or via email!

We just got started with the Podcast, so if you found this chat valuable, please consider **subscribing to the show** on [YouTube](https://www.youtube.com/@refactoringclub), [Apple](https://podcasts.apple.com/us/podcast/refactoring-podcast/id1719137305), or [Spotify](https://open.spotify.com/show/7Luds9dmzZDoDC8Q7EMbSw).

Also, consider **giving us a rating** or leaving a review on the platform of your choice, as that really helps other listeners find the show.

See you next week! 👋

Luca

### 🐦 Linkedin / Twitter
