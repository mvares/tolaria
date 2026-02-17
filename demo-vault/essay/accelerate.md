---
aliases:
  - "Accelerate"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-essays|Publish Essays →]]"
Status: Evergreened
URL: "https://refactoring.fm/p/accelerate"
"👓 Status": Not started
"Created time": "2025-03-28T16:46:00.000Z"
Date: 2025-04-16
"Has Notes":
  - "[[evergreen/accelerate-technical-capabilities|Accelerate — technical capabilities]]"
  - "[[evergreen/accelerate-key-findings|Accelerate — key findings]]"
  - "[[evergreen/accelerate-is-more-than-metrics|Accelerate is more than metrics]]"
Tags:
  - Book
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 1c4bdf02-815c-8046-bf18-c99e1186da90
---

# Accelerate

- Importance of measuring

- Leadership

## Accelerate community Notes

- AI Chat: [https://ai.refactoring.club/#chat=8CfNrFISqz](https://ai.refactoring.club/#chat=8CfNrFISqz) 

---

## Post Draft

Every two months we read a book in the community book club, read it on our own, and review it together in a lively online event.

Last month it was the turn of [**Accelerate**](https://www.goodreads.com/book/show/35747076-accelerate) — the foundational research work on software engineering performance by Nicole Forsgren, Jez Humble, and Gene Kim. 

![image](../assets/1d5bdf02815c8032.png)

This pick brought back memories. 

I read Accelerate in 2019, during a particularly challenging time at my startup. The org had grown after we had raised our Series A, and for the first time we were able to split engineers into long-lived, semi-independent teams working on separate product areas.

However, instead of going *faster*, things started feeling *slower*. Also, not uniformly so: I felt that some teams were doing better than others, but I couldn’t quite put my finger on why.

So I picked up *Accelerate* with promise, as I saw one of the authors was Gene Kim. Gene also wrote The Phoenix Project, which back then was my favorite engineering book (and still kind of is?!).

Accelerate turned out to be special indeed, marking a before-and-after moment in how I thought about engineering work. It is special in a variety of ways, but first of all because it is based on an astounding *six years of research*, where the authors surveyed 20,000+ engineers and managers, across 2,000+ organizations.

It was the largest research ever performed on DevOps and software delivery practices, by orders of magnitude.

Such research was also incredibly *conclusive. *It found clear patterns that correlate good engineering practices to software delivery performance, and, in turn, good software delivery to business success.

Today, seven years after publication, the foundations laid by Accelerate on how we think about engineering performance, and how we measure it, are still rock-solid and undisputed. For this reason, this review has a two-fold goal: we are going to review the main findings and teachings of the book, but also look at their legacy, and how we have built on top of them since then.

So, here is the agenda for today:

1. 📊 **More than just metrics **— if you think Accelerate == DORA metrics, you are simply missing out.

1. 🪴 **Cultural capabilities **— looking into transformational leadership and generative culture.

1. 🔄 **Process & management capabilities **— how to make your work flow well, create tight feedback loops, and minimize waste.

1. ⚙️ **Technical capabilities **— how to enable elite software delivery that will drive immense business value.

1. 💡 **Key findings **— my favorite takeaways from the book, like the speed vs stability paradox, and the link between engineering and business excellence.

Let’s dive in!

![image](../assets/1d5bdf02815c8061.png)

---

### 📊 More than just metrics

Ask anyone about *Accelerate*, and chances are they will mention the DORA metrics. 

These four KPIs define how teams can measure their software delivery performance, and became instantly famous after the book’s publication. They are:

1. 🚀 **Deployment Frequency** — how often you release to production.

1. ⏱️ **Lead Time for Changes** — the amount of time it takes a commit to get to production.

1. 📉 **Change Failure Rate** — the percentage of deployments causing a failure.

1. 🛠️ **Time to Restore Service (MTTR)** — how long it takes to recover from a failure.

One of the reasons why the metrics caught on is because they provided, for the first time, a research-backed way to evaluate software delivery across two dimensions:

- **Throughput** → via Deployment Frequency + Lead Time for Changes.

- **Stability** → via Change Failure Rate + MTTR.

But here’s the thing: if you think *Accelerate* is *only* about metrics, you're missing 90% of the picture. 

Last week I interviewed [Abi Noda](https://www.linkedin.com/in/abinoda/), founder of DX, on the podcast (the episode will come out on Friday). We briefly touched on Accelerate and Abi said there's a kind of a running joke among the *insiders* — people who've been around during the whole Accelerate work. And the joke is that, when the book got published, it’s like everyone just read the page with the four metrics and then put down the rest of the book.

> *Obviously in the book there's a definition of these four key metrics that have statistical power behind them. But really the book is about: how do you transform an organization? What are the best practices that organizations should be focused on at that time in the industry? And the metrics are just a way of sort of demonstrating and verifying the value of adopting those practices. — Abi Noda*

So, the core of Accelerate is not the metrics: it's the *engine *that enables them.

The book meticulously identifies and validates **24 key capabilities** that are statistically shown to improve software delivery performance. The metrics are the *outcome*, while the capabilities are the *drivers*. 

And the research proves this connection with extreme rigor. It moves the conversation from "*what good looks like*" to "*what specific actions demonstrably lead to good*."

So, I don’t want to discount DORA metrics, which has been incredibly consequential to our industry (to learn more about them, you can check out our [full guide](https://refactoring.fm/p/how-to-get-started-with-engineering)), but today we’ll focus on capabilities, which to me are the real star of the book.

24 is a big number, so, with some degree of simplification, let’s start by organizing capabilities into three buckets: **cultural**, **process**, and **technical**.

These buckets work as levels of a pyramid, each one supports the health of the ones above:

1. **Culture** — is what makes people work well together and feel good about their work environment. It keeps retention high, stress low, and enables the creation of good process 👇

1. **Process** — exists to make work flow well through the system. Good process is about tight feedback loops and minimizing waste.

1. **Tech** — good culture and good process naturally lead to the technical practices that enable elite software delivery, like continuous deployment and empowered teams.

![image](../assets/1d5bdf02815c80a2.png)

Let’s look at all of them:

---

### 🪴 Cultural capabilities

*Accelerate* identifies five key cultural capabilities displayed by elite teams:

1. 🧭 **Transformational Leadership** — having leaders who inspire and motivate their teams, possess a strong vision, stimulate their staff intellectually, and provide individual consideration and support. These leaders foster the trust and psychological safety needed for a generative culture to thrive 👇

1. 🌱 **Westrum Generative Culture** — high-performing orgs exhibit a *generative* *culture* characterized by high cooperation, shared risks, treating failure as a learning opportunity, and encouraging novelty. Information flows freely, and messengers aren't punished for delivering bad news. The concept of generative culture is so important that we covered it in a [dedicated newsletter edition](https://refactoring.fm/p/generative-culture?utm_source=publication-search).

1. 🎓 **Supporting Learning** — learning is valued and seen as essential. This includes providing resources for training, giving people time to learn, and fostering a culture where it's safe to admit you don't know something and ask questions. More on [how to invest in engineers’ growth](https://refactoring.fm/p/how-to-invest-in-engineers-growth).

1. 🤝 **Collaboration Among Teams** — fostering strong cooperation and communication *between *different teams (e.g., Dev, Ops, Security, Product). Focus on breaking down silos.

1. 😊 **Job Satisfaction** — ensuring that team members feel satisfied with their work, their team, and the organization. The research found job satisfaction isn't just a consequence of good performance; it's also a *predictor* of it, in a self-reinforcing cycle that contributes to better outcomes and retention.

![Pathological vs Bureaucratic vs Generative cultures, in Westrum classification](../assets/1d5bdf02815c80ed.png)

---

### 🔄 Process & management capabilities

Strong culture is essential, but Accelerate found that performance also heavily depends on **how work flows through the system**. 

Top performers adopt *lean* principles to optimize their processes, reduce waste, and enable faster feedback. Key capabilities here include:

1. 👂 **Customer feedback** — actively and regularly incorporating [feedback from end-users](https://refactoring.fm/p/how-to-talk-with-customers?utm_source=publication-search) into the design and development process. This ensures the team is building the *right* thing and reduces wasted effort on features nobody wants.

1. 🗺️ **Value stream** — mapping and analyzing the flow of work from business idea to end-user value delivery, identifying bottlenecks and areas for improvement.

1. 📦 **Working in small batches** — keeping units of work small (e.g., small features, small commits) to improve flow, reduce risk, shorten feedback loops, and limit the impact of failures.

1. 🧪 **Team experimentation** — fostering a culture where teams are encouraged to try out new ideas, tools, and processes, measure the results, and learn from them, even if they fail.

1. ✅ **Lightweight change approval** — moving away from heavyweight, external [change approval boards](https://en.wikipedia.org/wiki/Change-advisory_board). High performers rely on peer review and automated checks, enforced by strong technical practices. This builds on trust and speeds up delivery significantly.

1. 🔔 **Proactive notification (monitoring)** — Implementing monitoring and alerting systems that proactively inform teams about potential problems *before* they impact users, enabling faster response and prevention.

1. 📊 **WIP limits** — limiting the amount of work in progress (WIP) at any given time. This seems counterintuitive, but it reduces context switching and keeps the focus on completing tasks, which leads to faster overall throughput and less burnout.

1. 👀 **Visualizing work** — using visual displays to show the status of work, WIP limits, and potential bottlenecks. This makes constraints and problems visible to everyone, enabling faster collective problem-solving.

These process improvements don't exist in isolation — they build on the trust developed by generative cultures, and are *implemented* by the technical practices identified below 👇

---

### ⚙️ Technical Capabilities

These are the technical practices that the research proved have the biggest impact on delivery performance:

1. 💾 **Version Control** — having *all* production artifacts (code, configurations, infrastructure) in version control, for reproducibility and traceability.

1. 🧪 **Automated Testing** — reliable automated tests (unit, integration, acceptance) for giving teams the confidence to deploy frequently, strongly correlating with lower change failure rates and faster restoration times*. *Here is our [full guide on testing](https://refactoring.fm/how-to-test-software-in-2023).

1. 📊 **Test Data Management** — the most common bottleneck in reliable testing is having good test data, which requires intentional investment.

1. 🔄 **Continuous Integration (CI)** — developers merge their work into a central repository, after which automated builds and tests are run, catching integration issues early and often. This pairs nicely with 👇

1. 🌳 **Trunk-Based Development** — developers work in short-lived branches and integrate their code frequently (at least daily), avoiding the integration hell of long-lived feature branches.

1. 🚚 **Continuous Delivery** — code on the main branch *can be deployed* at any time, i.e. it is always in a deployable state. Example: code passes CI tests; it is automatically deployed to a staging environment; a human manually approves the release to production. But the final boss is 👇

1. 🚀 **Continuous Deployment** — every change that passes automated tests gets [*automatically *](https://refactoring.fm/p/do-you-need-staging?utm_source=publication-search)[deployed to production](https://refactoring.fm/p/do-you-need-staging?utm_source=publication-search). This is the final, aspirational goal enabled by everything above, which removes manual checks and reduces the need for coordination. Worth noting that deploying code doesn’t necessarily mean to *release* it to users! In fact, you should probably *decouple *the two things with techniques like [1% canary](https://refactoring.fm/i/159691291/canary).

1. 🔒 **Shift Left on Security** — integrating security practices early into the development lifecycle, rather than treating it as an afterthought, often by automating security checks within the delivery pipeline. We wrote about this [here](https://refactoring.fm/p/how-to-write-secure-code).

1. 🧩 **Loosely Coupled Architecture** — designing systems where components can be changed and deployed independently, reducing coordination overhead and minimizing the blast radius of failures. We wrote about this in the [monoliths vs microservices](https://refactoring.fm/p/monoliths-vs-microservices) piece.

1. 💪 **Empowered Teams** — ensuring teams have the autonomy to design, build, test, and deploy their own services without excessive dependencies on other teams or centralized functions.

It’s worth noting that many of these technical capabilities work together. You can't achieve continuous deployment without strong automated testing and CI; loosely coupled architectures are much easier to manage with robust deployment automation, and so on.

---

### **💡 Key Findings**

After digging into the specific capabilities across culture, process, and technology, what are the biggest, most impactful conclusions that the *Accelerate* research hammered home?

Here are my favorite ones:

#### **1) Engineering excellence *****drives***** business success 💰**

Accelerate provides the kind of validation tech leaders need to hear: **strong software delivery performance demonstrably drives organizational performance.** 

The research showed statistically significant correlations between high IT performance (as measured by DORA metrics) and traditional business metrics like profitability, market share, and productivity.

This provides powerful justification for investing in the capabilities discussed: they aren't just tech initiatives — they are direct contributors to the bottom line.

#### **2) Good performance *****requires***** good culture **❤️

The research provides hard evidence that **organizational culture is foundational**.

You can't just implement new tools and processes and expect results if the underlying culture is pathological or bureaucratic. A generative culture, characterized by trust, psychological safety, learning, and collaboration, is not just correlated with high performance; it's a necessary prerequisite for technical and process improvements to actually stick and deliver value. 

Culture *enables* acceleration.

#### **3) There is no tradeoff between speed and stability ⚙️**

Perhaps the most counterintuitive finding for traditional IT thinking is this: **high performers don't trade speed for stability — they achieve both.** 

The same practices that enable faster delivery (like CI/CD, automated testing, loosely coupled architecture) also lead to more reliable systems with lower change failure rates and faster recovery times. The old excuse of "*we need to slow down to be more careful*" is statistically debunked. Elite teams are both faster *and* safer.

#### **4) Continuous deployment reduces pain & burnout ✨**

Implementing Continuous Delivery practices does more than just speed up releases and improve stability. 

The research finds a strong correlation between CD adoption and **reduced deployment pain and lower levels of team burnout.** 

When deployments are automated, low-risk, and frequent, they cease to be terrifying, stressful events. This improves the sustainability of engineering work and contributes significantly to job satisfaction and retention. Investing in CD is investing in your people's well-being.

---

### 📌 Bottom line

So, *Accelerate* was published back in 2017. In tech years, that feels like a lifetime ago. Does a book based on research from the mid-2010s still hold up?

Overwhelmingly, yes.

While the specific tech changes all the time, the underlying principles from *Accelerate* remain 100% relevant. If anything, the bar is way higher now, so for most teams being able to deliver software quickly + reliably has turned from nice to have to tablestakes.

Of course, the conversation has also evolved. Frameworks like [SPACE](https://queue.acm.org/detail.cfm?id=3454124),** **[DX Core 4](https://refactoring.fm/p/whats-next-in-measuring-dev-productivity), and more, now provide a more holistic view of developer productivity and well-being. We now acknowledge factors like satisfaction, collaboration, and flow, which *Accelerate *itself identified but didn't fully operationalize into metrics. These frameworks complement DORA, rather than replacing it, offering a richer picture.

But the core message stands. The 24 capabilities are a timeless blueprint for building high-performing technology orgs.

And that’s it for today! I wish you a great week

Sincerely
Luca
