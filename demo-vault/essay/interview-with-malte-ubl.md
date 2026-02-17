---
aliases:
  - "Interview with Malte Ubl"
"✏️ Status": Not started
"Belongs to":
  - "[[responsibility/publish-podcast|Publish Podcast]]"
  - "[[person/malte-ubl|Malte Ubl]]"
Status: Evergreened
URL: "https://refactoring.fm/p/how-vercel-works"
"👓 Status": Not started
"Created time": "2024-04-19T10:14:00.000Z"
Date: 2024-06-28
"Has Notes":
  - "[[evergreen/map-out-your-developer-experience|Map out your developer experience]]"
  - "[[evergreen/the-spider-graph-of-leadership-roles|The Spider Graph of leadership roles]]"
Tags:
  - Podcast
  - Free
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: a29bf649-c47e-46fa-a2b7-7d91028a1d9f
---

# Interview with Malte Ubl

### **1) 🏗️ Vercel's engineering culture (**[**00:41**](https://www.youtube.com/watch?v=IgsKxmNNn3I&t=41s)**)**

Vercel's engineers use the tools they build, creating a natural empathy with users.

This approach allows for **intuitive product development** without extensive market research. By starting with what they themselves would like, engineers often create solutions that resonate well with their audience.

Basically, **the entire organization at Vercel uses their product daily** — Malte mentions that CEO Guillermo Rauch has deployed an app on Vercel every single day for the past five years.

So, as we could expect, Vercel is an **engineering-heavy company** 👇

---

### **2) 🚀 Development process at Vercel (**[**05:45**](https://www.youtube.com/watch?v=IgsKxmNNn3I&t=345s)**)**

Vercel makes extensive use of **feature flags 🚩** throughout the entire development cycle.

Flags can be toggled from local development all the way to production. This approach allows developers to ship code that might not be fully functional, but stays safely hidden behind a flag.

Flags enable a workflow where small, focused PRs can be reviewed and merged quickly, reducing the pain of long-lived branches and complex merges.

This is part of Malte’s focus on getting code **into production as quickly as possible**. Vercel strives to minimize the time between writing code and seeing it live, which is crucial for maintaining developer context and productivity.

#### **Continuous feedback loop 🔁**

Vercel also emphasizes **fast iteration cycles** and testing in production.

Tools like **instant rollback** and **bisecting** provide a safety net and allow for quick problem resolution, all of which makes it more viable to release straight to prod.

The bisecting feature in particular, made possible by **immutable deployments**, allows teams to quickly identify where a bug was introduced, potentially saving hours during incidents.

---

### **3) 👥 Team structure and mgmt (**[**12:51**](https://www.youtube.com/watch?v=IgsKxmNNn3I&t=771s)**)**

Malte introduces the concept of a **spider graph** for leadership roles, encompassing PM, Tech Lead, TPM, and EM responsibilities.

Rather than strictly defining *roles*, Vercel defines *duties*, which allows for more flexibility: individuals can embrace hybrid roles and fill multiple duties at the same time.

This approach enables the team to adapt to project needs and individual strengths, creating a more dynamic and efficient organization.

#### **Engineering managers 👨‍💼**

Vercel has two tiers of engineering managers:

1. The first tier, similar to Google's Tech Lead Managers (TLM), has substantial technical responsibilities and typically manages between 3 and 4 people.

1. The second tier is closer to full-time managers, and may oversee between 8 and 12 engineers.

This structure allows for flexible choices based on what individual teams need.

#### **Project ownership 🏆**

Vercel puts a strong emphasis on **clear ownership** of projects and outcomes.

Malte stresses the importance of having someone who truly owns the outcome and does whatever it takes to achieve it. This ownership mentality allows for quick decision-making and adaptability, as the owner can switch between different roles (product management, team leadership, task management) as needed to drive the project forward.

---

### **4) ⚡ Optimizing dev experience (**[**32:44**](https://www.youtube.com/watch?v=IgsKxmNNn3I&t=1964s)**)**

Malte recommends writing down the entire development process as a **one-dimensional flow**.

This exercise helps identify each step in the process and **potential bottlenecks**. By mapping out the journey from planning to production deployment, teams can pinpoint areas for optimization and improvement:

This process starts with local development, for which Malte says you should aim for **near-instant feedback**, ideally around 50ms.

This rapid feedback loop allows developers to see changes in real-time as they type, significantly enhancing productivity.

Malte also emphasizes **minimizing the time between code push and preview** availability, as this impacts how developers context-switch and manage their workflow.

**Safety net tools** discussed above, like instant rollback and bisecting also help a lot in improving productivity and developer experience.

---

### **5) 🤖 AI and the future of engineering (**[**42:50**](https://www.youtube.com/watch?v=IgsKxmNNn3I&t=2570s)**)**

Malte discusses the emergence of the *AI engineer* role.

These professionals work with model APIs rather than building models from scratch. They focus on skills like evals (evaluations) and fine-tuning existing models.

This shift represents a new specialization in software development, bridging the gap between traditional programming and AI capabilities.

#### **Generative UI 🖥️**

Vercel is also investing in what they call *Generative UI*, which combines existing UI components with AI capabilities.

In this model, AI can call React components and interact with existing business processes. This approach maintains the value of current UI investments while leveraging AI to create more interactive and intelligent applications.

#### **Code comprehensibility 📚**

As AI becomes more involved in code writing, Malte predicts that the importance of **code readability** will increase.

He anticipates a shift from optimizing for write-time to **optimizing for read-time**. This change is driven by the need for humans to understand and maintain AI-generated code effectively.

Malte suggests that we might move away from "low code" to having "a lot of code" with amazing tooling to maintain and understand it.
