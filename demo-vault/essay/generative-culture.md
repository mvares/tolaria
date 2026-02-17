---
aliases:
  - "Generative Culture"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-essays|Publish Essays →]]"
Status: Evergreened
URL: "https://refactoring.fm/p/generative-culture"
"👓 Status": Not started
"Date HH": 2025-10-23
"Created time": "2024-09-06T07:43:00.000Z"
Date: 2024-11-20
"Has Notes":
  - "[[evergreen/how-to-share-your-culture|How to share your culture]]"
  - "[[evergreen/generative-culture-in-practice|Generative culture in practice]]"
  - "[[evergreen/most-companies-do-not-conform-to-a-single-culture|Most Companies do not conform to a single culture]]"
  - "[[evergreen/the-three-organizational-cultures|The Three Organizational Cultures]]"
Tags:
  - Essay
  - Mgmt
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 558fed61-b596-480d-9b57-1b6292db9adb
---

# Generative Culture

## Materials

---

## Post

A few weeks ago we wrote about [engineering handbooks](https://refactoring.fm/p/how-to-create-an-engineering-handbook). From there, I got many emails with questions about *culture*, which is a similar but separate topic.

Engineering handbooks are like *instructions for use* — they tell you how to do things. Culture, instead, is about the principles that back how to write those instructions.

Incidentally, this was also the theme of our latest [Mastermind session](https://refactoring.fm/p/introducing-the-refactoring-mastermind?utm_source=publication-search), where we discussed various themes in organizational and engineering culture, and had a long chat about how to share culture with new hires and prospective ones.

I already wrote a piece last year about [**engineering culture**](https://refactoring.fm/p/culture?utm_source=publication-search), so today I want to explore more of the **organizational side**, which I believe is foundational to engineering and everything else.

Also, culture is the quintessential *fluffy* topic — if you Google around, you find plenty of vague statements and aspirational values that are more confusing than helpful. As usual, we'll try to steer away from those and stick to practical ideas.

Here is the agenda:

- 🏢 **The three organizational cultures** — how culture evolves from power to rules to performance.

- 🛠️ **Generative culture in practice** — what it looks like in engineering teams and how to implement it.

- 🤝 **Sharing culture** — with new and prospective hires.

Let's dive in!

---

### 🏢 The Three Organizational Cultures

When Ron Westrum first [studied organizational cultures](https://pmc.ncbi.nlm.nih.gov/articles/PMC1765804/pdf/v013p0ii22.pdf) in the 80s, he probably didn't expect to create a framework that would become a cornerstone of modern tech orgs. Yet, 35+ years later, his model perfectly explains why some engineering teams consistently outperform others.

Westrum identified three types of organizational cultures that exist on a spectrum: **pathological**, **bureaucratic**, and **generative**. Let's see what each of them looks like, especially in tech companies 👇

![image](../assets/142bdf02815c8031.png)

#### 1) Pathological culture is power-oriented 👑

In pathological cultures, the organization is oriented around power and fear. Information is treated as a personal resource to be hoarded for competitive advantage. 

You can probably think of examples you have encountered in your career. Here are typical signs:

- 🤐 **Information hoarding** — documentation is sparse and knowledge is treated as job security.

- 👉 **Blame culture** — incidents lead to finger-pointing and people avoid taking risks.

- 🚫 **Innovation discouraged** — new ideas are crushed as they may threaten existing power structures.

The first step to leave pathological culture is to establish good rules and processes that *prevent* such extremes. This is also, however, how you end up with a bureaucratic culture 👇

#### 2) Bureaucratic culture is rule-oriented 📋

Bureaucratic cultures are focused on rules, processes, and territories. While better than pathological ones, they still create significant friction. In engineering, this is when you see:

- 📝 **Process over outcome** — heavy change management, multiple approvals needed for anything to get done.

- 🏰 **Silos** — knowledge is documented but confined within team boundaries. Collaboration is hard and gate-keeping still exists: only at a team level instead of individual.

- ⚖️ **Risk aversion** — innovation is more or less seen as a potential source of problems, the team serves the process, as opposed to the process serving the team.

Good bureaucratic cultures gradually and eventually get leaner, and blossom into generative cultures 👇

#### 3) Generative culture is performance-oriented 🚀

Generative cultures optimize for performance. They focus on the mission and remove obstacles that get in the way. Generative engineering teams consistently show these traits:

- 🤝 **High cooperation** — information flows freely across teams

- 🔍 **Learning mindset** — failures are seen as opportunities to improve

- 💡 **Innovation enabled** — new ideas are welcomed and implemented

So here is a recap:

![image](../assets/142bdf02815c804e.png)

Most companies, however, don't strictly conform to a single culture type. 

In fact, as organizations grow beyond 30-40 people, teams naturally develop **their own ways of working**. For example, you might find that:

- The *Platform* team has a strong ownership culture — they are conservative with changes, require thorough docs, and have extensive on-call procedures.

- The *Growth* team moves fast and breaks things — they ship multiple times per day, do quick experiments, and optimize for learning velocity.

- The *Mobile* team is more waterfall-oriented — they plan releases weeks in advance, have longer QA cycles, and coordinate closely with design.

This raises an obvious question: should you enforce the same practices across all teams? 

The answer is no. This is just not possible at scale, for a variety of reasons: 1) different teams should *legitimately* work differently, for their own good, and 2) when you hire great people, you want to let them do things their own way, instead of imposing your way.

There is a balance to be found, though, because both alignment and diversity have value. To get the best of both, in my experience, here is what works:

1. **🎯 Focus on outcomes, not implementation **— don't mandate specific processes like "*all teams must do daily standups*". Instead, set clear expectations about outcomes. Teams can then figure out the best way to achieve these outcomes.

1. **🌱 Share success stories **— create avenues for good practices to spread. For example, when a team finds something that works particularly well, you may: have them present it at engineering all-hands; document it in the engineering handbook; make it easy for other teams to adopt in various ways. This creates natural convergence around good practices, without forcing them.

1. **🔄 Create feedback loops **— set up mechanisms to detect when team cultures diverge too much, like: cross-team retrospectives; engineers rotating between teams to share practices, metrics that help highlight performance differences.

The goal is not complete *uniformity* — it's making sure the different approaches **don't create friction**.

Think of your company as a *federation* of high-performing teams, rather than a monolithic org with identical practices everywhere.

---

### 🛠️ Generative culture in practice

Now that we understand how culture evolves across orgs, let's focus on what makes generative cultures special, and how to build one in your team.

While writing this piece, I asked several leaders in our community about how they recognize a generative culture. Their answers converged around three main themes: **how information flows**, **how decisions are made**, and **how failure is handled**.

Let's explore how these manifest in practice 👇

#### **1) Information flows freely 🌊**

In generative cultures, information is treated as a valuable resource to be shared, not hoarded. Here is what this looks like:

- 📝 **Docs are a shared responsibility** — everyone contributes to documentation, not just tech writers or seniors.

- 🔄 **Knowledge sharing is systematic** — regular show & tells, learning sessions, and cross-team demos.

- 🤝 **Collaboration is the default** — teams actively seek input from others rather than working in isolation.

In engineering teams, I have found that a strong litmus test for this is **how incidents are handled**. At its best, incident communication is radically transparent: teams communicate directly about what's happening, focus on resolution rather than blame, and follow up with collaborative (and often public) post-mortems.

This creates a virtuous cycle where people **feel safe to share problems** early, ask for help when needed, and contribute their learnings back to the organization. In the case of incidents, this means that the same incident rarely happens twice, and the system becomes more resilient over time. In the case of practices, it means the good ones spread fast, while the bad ones are easily pruned.

#### **2) Decisions are made at the right level ⚡**

One common misconception about generative cultures is that they are largely bottom-up. Instead, they optimize for making decisions at the most appropriate level:

- 🎯 **Strategic decisions** — leadership provides clear direction about company goals and technical strategy.

- 🛠️ **Implementation decisions** — teams have full autonomy on how to achieve those goals.

- 🤼 **Cross-team decisions** — resolved through collaboration and principles, not authority.

The goal is to allow teams to move fast within clear boundaries. When leaders succeed in sharing context about business goals and technical strategy, teams can make **good local decisions** that align with the bigger picture.

#### **3) Failure is a learning opportunity 📚**

A striking characteristic of generative cultures is how they handle failure. Instead of looking for someone to blame, they focus on:

- 🔍 **Understanding root causes** — especially organizational and systemic factors.

- 📈 **Improving processes** — based on lessons learned.

- 🎓 **Sharing learnings** — making sure the whole organization benefits from the experience.

This approach transforms how the team operates on a daily basis. When people feel psychologically safe, they start treating **failures as experiments** — data points that help improve the system. Engineers become more willing to take calculated risks, surface problems early, and discuss them openly.

Finally, all these elements are enabled by a underlying value: **generative cultures focus on impact** over pure technical excellence. Mastery is important, but it needs to be directed toward user outcomes. Without this focus, you risk creating a "crafters culture" — one that values technical perfection but might lose sight of actual business value.

I wrote more about this balance in our past piece about [engineering culture](https://refactoring.fm/p/culture?utm_source=publication-search).

---

### **🤝 Sharing your culture**

Culture isn't just what you write in your handbook — it's what happens every day in your organization. However, you still need to communicate it effectively, especially to people who are not yet part of your company.

But how do you show, rather than tell, culture to new and prospective hires? This was a big talking point in our mastermind session. So let's explore it.

#### **1) Map your touch points 🗺️**

In hiring, every interaction with candidates is an opportunity to demonstrate your culture. The most important touch points are:

- 🌐 **Public presence** — like your website, blog posts, conference talks, open source work.

- 📝 **Job materials** — job descriptions, career page, application process.

- 👥 **Interview process** — communication style, types of questions, interviewer behavior.

Each step tells a story about who you are. If you claim to have a culture of transparency, but your hiring process is opaque, candidates will notice the disconnect. If you talk about work-life balance, but send emails at midnight, people will trust your actions more than your words.

Companies with the strongest culture ensure consistency across all touch points: 

- **Shopify **has a peculiar culture founded on entrepreneurship and autonomy. If you apply to one of their jobs, the process starts with you receiving a small handbook about Shopify’s culture. You can only move forward by explicitly accepting their principles, and interviewers also ask you about them.

- **Gitlab** values transparency, so they made their entire company handbook is public, containing everything from engineering practices to their remote-first culture.

#### **2) Show, don't tell 🎬**

Instead of writing abstract values, share real stories that demonstrate how your team works. Engineering blogs are perfect for this — they can display technical excellence, but more importantly, they reveal how you think and solve problems.

Consider these powerful ways to demonstrate culture in action:

- 📚 **Public post-mortems** — that show how you learn from incidents

- 🛠️ **Engineering challenges** — blog posts that reveal your problem-solving approach

- 🎯 **Behind-the-scenes content** — about team rituals and collaboration

#### 3) Take from the best 🥇

When documenting your culture, avoid the trap of writing aspirational statements that sound good but don't reflect reality. Instead, look at your best performers — what makes them successful? What behaviors do they exhibit that you'd like to see more of?

For example, instead of writing "we value excellence", you might observe that your best engineers 1) actively seek feedback early in the dev process, and 3) take ownership of problems end-to-end. Write about this, and share examples where this was displayed.

Concrete behaviors are way more useful than abstract values. They give people guidance on what *good* looks like in your organization.

#### **4) Watch the signals 📊**

While culture can feel intangible, you can still find signals that tell you if you're on the right track.

In hiring, you can track candidates conversion rates and the volume of your inbound. For your team’s health, you can look at retention and engagement, and you can run surveys to find gaps between documented and lived values.

This is all hard stuff because most of these are *lagging* indicators — they have long feedback loops, and it takes time to figure out if something is working or not, or is on a good trajectory.

On a more tactical level, I have found some of the best, most actionable signals to come from your onboarding process. Pay attention to questions new hires ask repeatedly (== gaps in docs), where they get stuck (== friction), and how quickly they become productive (== effectiveness of knowledge sharing). Focusing on good onboarding, other than being helpful on its own, helps you spot culture issues before they become problems.

---

### **📌 Bottom Line**

And that’s it for today! Here are the main takeaways:

- 🎯 **Culture is what you do** — not what you write in your handbook. Your actual culture emerges from daily behaviors, decisions, and practices.

- 🌊 **Information flow is key** — generative cultures optimize for transparency and knowledge sharing. This creates better outcomes and faster learning cycles.

- 🔄 **Evolution is natural** — as organizations grow, different teams may develop distinct traits. This is natural and healthy: focus on shared principles rather than enforcing identical practices.

- 👥 **Show, don't tell** — the best way to share your culture is through concrete examples and behaviors, not values statements. Let candidates experience it through every interaction.

- 📈 **Culture needs maintenance** — treat it as a continuous conversation that evolves with your team. Regular check-ins and adjustments keep it healthy.

See you next week 👋

Luca
