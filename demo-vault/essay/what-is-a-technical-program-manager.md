---
aliases:
  - "What is a Technical Program Manager?"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-essays|Publish Essays →]]"
Status: Evergreened
URL: "https://refactoring.fm/p/tpm"
"👓 Status": Not started
"Created time": "2024-04-18T14:53:00.000Z"
Date: 2023-02-02
"Has Notes":
  - "[[evergreen/signs-you-may-need-or-not-need-a-tpm|Signs you may need or not need a TPM]]"
  - "[[evergreen/definition-of-a-tpm|Definition of a TPM]]"
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: a50fc9a8-8ec3-4b19-b22c-9ad64ff10d3d
---

# What is a Technical Program Manager?

### 📑 Materials

---

### 💡 Ideas

---

- 

### ✍️ Post

---

A few weeks ago I had a good chat with a friend of mine, who has a technical leadership role at a mid-size company (~50 engineers). 

He told me they finally managed to create cross-functional teams that are fairly independent, and that he is happy with how fast they are able to ship new things. However, he also told me he is struggling with a couple of projects that — necessarily — span the work of many of such teams.

Coordination is tricky and so is resource allocation, because ownership is somewhat distributed and each problem goes back and forth like a hot potato.

I asked him if they ever thought about introducing **Technical Program Managers **for such projects. He answered that he wasn’t sure, because we weren't familiar with the role and how it would fit the organization.

This was an honest confession, and it struck a chord with me. The TPM role is often misunderstood, I believe for two main reasons:

- ⏱️ **Timing** — as with many roles that aren’t useful until your team reaches a certain size, it is tricky to figure out when it is the right time to add one.

- 🔬 **Scope** — it sits in your product / engineering org, while not being neither an IC role, nor a classic management one. Most TPMs don’t have direct reports.

So how does Technical Program Management work? To shed light onto this crucial role, I asked for help from my friend [Aadil Maan](https://twitter.com/aadilmaan), who graciously co-authored this piece.

Aadil has tremendous experience having led programs at companies like Apple, Uber, and Google. He is also a fantastic writer — he is the author of the [Building Romes](https://buildingromes.substack.com/) newsletter, where every week he explains and demystifies specific aspects of the TPM role.

This article wants to be a primer on Technical Program Management where we cover the why, the what, and the how. Then, if you want to learn more, I encourage you to check out Aadil's newsletter!

So, today we will talk about:

- 📖 **What is a TPM** — and how they differ from (e.g.) PMs

- 🔍 **Signs you may need a TPM —**

- 🤹‍♀️ **Skills of a good TPM** — let’s talk about project management, technical knowledge, and communication 

- 💼 **How to break into a TPM role** — career advice for people interested in the role

### 📖 What is a TPM

A typical Product team may consist of a Product Manager, Engineering Lead, Design Lead, and some engineers. 

Often times that is enough, but for extremely complex programs where you have multiple teams working together, a Technical Program Manager steps in to orchestrate the collaboration across all these domains.

To put it in another way:

- **Product Managers** focus on the ***what***** **and** *****why***.

- **TPMs** help Engineering Leads with the ***how*** and ***when***.

A TPM is the nervous system ensuring product and engineering continues to stay aligned on the *what*, *why*, *how* and *when*.

At large companies, where it becomes necessary for Product Managers to focus on the strategic aspect of their role, a TPM is brought in like a tactician to help execute on the grand strategy. So, the TPM enters the stage to develop an end-to-end execution plan on how to ship a solution to a technical problem.

![image](../assets/33a1b840832c4ef1.png)

Such problems are of varying complexity, usually ambiguous in definition, and need to be delivered in collaboration with engineering, product, design, and marketing within a certain time & budget.

But how do TPMs do that? 👇

### 🤹 Skills of a good TPM

A Technical Program Manager needs three core competencies: *project management, technical knowledge, *and *soft skills*. Let’s see all three.

#### 🗺️ Project Management

Knowing how to take complex requirements and develop an achievable project plan within the constraints is the bread and butter of every TPM. 

Here are the key Project Management skills every TPM needs:

- **Project plans** — You don’t have to have a GANTT chart to have a project plan. A TPM needs to know when something as simple as a spreadsheet will be more effective or when a PERT chart is needed versus GANTT chart. Remember: at the end of the day, project plans are a series of cascading gates (milestones) with set exit criteria (work to be done, acceptance criteria) that must be reached by a certain schedule.

- **Breaking down work** — Requirements must be translated into actual work to be done by all members of the cross-functional team. This can be as simple as translating requirements or user stories into epics or how to break down epics into their child tasks.

- **Information Architecture** — Complex projects have a large number of moving pieces. It is imperative that information is flowing, referenceable, and available at all times to stakeholders. TPMs often design wikis, living documents, PRDs, archives for meeting minutes, and more, for effective collaboration. TPMs must know how to assess, group, and design artifacts to be stored.

- **Risk Management** — TPMs excel at risk management. Many programs and products fail primarily from not managing risk properly. Keeping track of risk and developing the right response at the right time can make the difference between a slight delay to completely missing the deadline by *quarters*. There are two types of risks: ones you react to (you can never predict these and must react in the moment), and ones you plan against (there are known unknowns which a plan can be formulated for if it does occur).

- **Agile methods** — You don’t have to be a Scrum expert, or religiously adhere to program increment planning or Kanban boards. What is important is that you are aware of the core components of the various agile practices, then help your teams pick and choose the right pieces from them and develop a bespoke methodology that fits the culture and personalities of your team.

- **Communication & Stakeholder Management** — You will work with varying degrees of personalities so it is important for you to know how to deal with and manage everyone's needs and wants. Proactive stakeholder management is key to making sure that your team can focus on building the product instead of constantly answering inconsequential and annoying questions (mostly annoying; TPS reports anyone).

#### 🛠️ **Technical Knowledge**

No one expects Technical Program Managers to know how to code. However, to be successful members of the Product team, TPMs must have a systems-level understanding of how the various components come together to develop complex products.

Here are the key technical skills every TPM must know:

- **Systems Design** — TPMs drive large projects that span across multiple engineering teams. Thus it is important that a TPM understands how backend and frontend systems work together, what APIs are, how modern app dev happens, and what role cloud plays in the workflow.

- **Design Thinking** — if you are responsible for driving UI based products, it is extremely important to understand how design teams think, work, and deliver UX/UI. This understanding will help you create a better plan, design collaboration between engineering and design, and communicate to leadership what is taking design so long to deliver a “simple” button :)

- **Performance and Quality** — in order to ship high-quality, performant products, a TPM must be the voice of quality. You should understand how the various types of tests (e.g. unit, integration, E2E) come together with logging and monitoring to catch quality issues before they become news articles. In addition, when developing project plans, a smart TPM will bake in time for fixing performance issues, quality bugs, and will find time to deal with tech debt.

#### 💬 **Soft Skills**

Technical Program Managers rarely if ever have any direct decision making authority yet are accountable for the success of a program. They are often known as **Leaders Without Authority**. So, to lead they must rely on their soft skills to instead **Lead With Influence**. 

What does it take to lead with influence?

- **Trust building** — Trust is the primary currency that a TPM uses to push programs towards success. A TPM needs to be trusted by engineers to help them resolve road blocks, to keep communication lines open, to manage risk, and to be an advocate for the product team. On the other side, leaders place their trust in TPMs to deliver programs on time and schedule, to make them aware of pending risks, and ensure information flows to all parts of the company for better collaboration. Trust is earned through experience, by showing up for the product teams ready and willing to help.

- **Negotiation** — TPMs don’t just ask for dates. They understand that everyone is under pressure to deliver on their roadmaps and commitments. They leverage empathy to help teams figure out what positions need to be changed to get their program across the finish line.

- **Diplomacy** — This is perhaps the biggest soft skill a TPM brings to the product team. Engineers, Designers, Product Managers, Marketers, everyone is wicked smart at what they do. It is natural for conflict to arise when collaborating on complex projects. The TPM is the one person in the room who takes no sides but focuses on the good of the program and its stakeholders. They help bridge the divides and defuse the tension in the room.

- **Inquisitiveness **— All plans are as great as their weakest link: that single missing detail, or that lack of understanding. TPMs are great at *asking questions* to dig deep into the details, to ensure that nothing is left to chance, that everything that can be understood is understood, and yo prepare for the unknowns that the product team is not aware of.

### 🔍 Signs you may need a TPM

### 💼 How to break into a TPM role

Being a hybrid and often misunderstood role, many people wonder what kind of track record you need to break into TPM. 

A major factor for this is whether or not you come from a technical background. In fact, I have seen people having successful TPM careers in both scenarios, but what you have to exhibit in interviews, and on your resume, is probably different.

#### Coming from a technical background

Going back to the three main skills we discussed above, if you come from a technical position, you must prove that you have the right *Project Management* and *Soft Skills* to excel in the role. 

To do so, both in your resume and interview, you should focus on projects where you played a direct role in:

- Putting together an **execution plan**

- Developing processes and frameworks to improve engineering velocity and efficiency

- Managing communication with stakeholders

- Resolving roadblocks and ensuring all the action items were followed through on

If you lack ‌such skills or a solid track record, there are two ways you can develop them:

- 💪 **Work** — Take a more active role at your current company to lead projects in a project management capacity. For this, you can most often take some initiative even without a formal role.

- 📚 **Study** — look into project management classes, executive education programs, and certifications offered by the [Project Management Institute](https://www.pmi.org/). Even [Google Grow](https://grow.google/certificates/project-management/#?modal_active=none) offers certificates in agile project management which will give you the right foundations.

#### Coming from a non-technical background

If you come from a non-technical background, you must prove that you can hold your own when collaborating with engineering and be more than just “*can you give me date for that task?*”.

You can be the voice of the technical teams with leadership, translating technical knowledge into business impact.

To exhibit this, as part of your interview prep, think of a large project you drove that was successful, and one that was not successful or had issues. Think of what role you played in both, especially driving technical issues, road blocks, and requirements.

Go as deep as you can go but keep it succinct because in the interview your answers will have to be short and on point.

If you lack the technical skills we covered earlier in the post, the best way is to start reading: newsletters, articles, books, anything that gives you a solid foundation in systems architecture and design. 

Some of the best newsletters (other than Refactoring!) to follow right now on systems level education are:

Again — you don’t have to be an engineer to be a TPM, you have to be a quick learner and student. The best TPM I know—my mentor—has an MA in English. Trust me, you can learn the right amount of tech skills but the key thing is that every successful or not successful project you lead will make you better.

[https://refactoring.fm/p/tpm](https://refactoring.fm/p/tpm)
