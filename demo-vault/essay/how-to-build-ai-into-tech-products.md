---
aliases:
  - "How to Build AI into Tech Products"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-essays|Publish Essays →]]"
Status: Evergreened
URL: "https://refactoring.fm/p/how-to-build-ai-into-tech-products"
"👓 Status": Not started
"Created time": "2025-08-06T11:45:00.000Z"
Date: 2025-10-29
"Has Notes":
  - "[[evergreen/most-ai-teams-dont-need-researchers|Most AI teams don’t need researchers]]"
  - "[[evergreen/build-vs-buy-for-ai-is-about-capabilties|Build vs buy for AI is about capabilties]]"
  - "[[evergreen/create-good-evals-by-integrating-domain-knowledge|Create good evals by integrating domain knowledge]]"
Tags:
  - Guest
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 247bdf02-815c-8052-aac3-d6c81e75340f
---

# How to Build AI into Tech Products

Hey! With all the AI craze happening right now, there are two questions tech teams usually ask themselves about it: 1) should we use more AI at work? and 2) should we integrate AI into our product?

We talk pretty often about the first one, while I feel the second is a bit *underrepresented*. It is a complex question, that leads to an obvious follow up: *how?*

“How” questions are often tricky because they can be explored into multiple angles, and this makes not exception:

- **How do we build AI from a tech perspective? **It’s a cascade of buy vs build decisions.

- **How do we measure that it’s doing well?** How to make sure it’s actually improving?

- **How do we structure our team to make it happen?** Do we need to hire PhDs? What do AI Engineers actually do?

To explore all of this, today I am bringing in [Barr Yaron](https://www.linkedin.com/in/barryaron/) from [Amplify](amplifypartners.com), who has a unique vantage point on this.

Amplify is peculiar VC fund, who only invests in technical founders, mostly building dev tools. They backed the likes of Datadog, Runway, and Temporal, and are *very opinionated* about what is happening right now in tech.

Barr also runs [a podcast](https://www.amplifypartners.com/barrchives), where she talks every week to CEOs and CTOs of technical products building in AI, so she is perfectly positioned to connect the dots and tell us about some good practices!

---

![image](../assets/294bdf02815c806f.png)

---

Hey, Barr here!

Everyone is racing to build AI into their products. What makes some teams succeed while others fail? 

Thanks to the podcast and to our work with founders we have the chance to go deep into what it *really* takes to build lasting AI products, from technical aspects like evals and data stacks to business decisions like team building and structuring.

In this post I’m going to talk about 3 themes I’ve seen from these leaders in AI that have helped them successfully build AI products (and organizations) for technical audiences – and how you can do the same:

1. 🔍 **Getting evals right** — by integrating domain expertise

1. ⚖️ **Building vs buying models** — how to think through the dilemma

1. 🏗️ **Structuring AI teams** — do you need researchers, engineers, or both??

Let’s dive in!

---

![image](../assets/299bdf02815c8058.png)

---

### 🔍 **Getting evals right by integrating domain expertise**

Every CEO and CTO that I’ve spoken to says their companies have invested significantly in good evals, and it’s very hard to get them right. Like Olivier (**Datadog **CEO) [mentioned](https://www.amplifypartners.com/barrchives/datadogs-ai-story-with-olivier-pomel-datadog-co-founder-and-ceo), you fundamentally cannot improve what you can’t measure.

A few examples:

- [**Replit**](https://www.amplifypartners.com/barrchives/how-replit-is-using-ai-to-help-develop-the-next-billion-coders-with-amjad-masad-michele-catasta)** **— built a multi-step evaluation system that lets them jump into any point in a development trajectory to test how their agent handles prompts and code modifications.

- [**Hex**](https://www.amplifypartners.com/barrchives/how-hex-builds-ai-for-data-scientists)** **—** **discovered that public benchmarks were not representative of real world data workflows, so they developed their own evaluations tailored to how data scientists actually use data.

- [**Decagon**](https://www.amplifypartners.com/barrchives/how-decagon-builds-customer-support-ai-agents-that-really-work)** **— built large-scale tests for voice agents that simulate customer conversations and check for compliance, friendliness, and task completion.

The one theme that was obvious among companies that have nailed evals: they **integrate domain expertise** into every step of the AI development process, especially evals.

[**Vercel**](https://www.amplifypartners.com/barrchives/how-vercel-is-advancing-the-future-of-frontend-with-ai-with-guillermo-rauch) CEO Guillermo Rauch explained it clearly – when customers rely on you for expertise, scaling that expertise is highly impactful:

> *“Imagine if I could deploy my CTO who was at Google for 13 years and he could review the code of all our customers and give performance recommendations. How can I automate that process and make it scalable? If we can do that — build up large datasets, build up our evaluations, and constantly infuse them with what we call frontier data – we get models that continuously learn from the edge.”*

Another great example is [**Vanta**](https://www.amplifypartners.com/barrchives/how-vanta-helps-customers-build-secure-and-compliant-ai-products-with-christina-cacioppo-co-founder-and-ceo-and-iccha-sethi-vp-of-engineering).

To construct their golden dataset — essentially the canonical representation of expected customer inputs to models and desired outputs — they put together a **panel of domain experts** in compliance. These folks actively work with Vanta’s product and engineering teams to build these golden datasets; but also help with human evaluation of model responses in the wild.

When I say actively work with, I mean actively work with. These SMEs, or subject matter experts, are **deeply embedded in the product and engineering workflows**. They essentially do paired sessions with an engineer or PM. A SME might say “*this model response doesn’t look right*” and the engineer might try shifting the prompt, or adding additional context.

The point here is that domain expertise needs to be *deeply integrated* into how your engineers build AI product. It can’t be an afterthought, or a panel who takes a look at things occasionally.

Digging further into the Vanta example: they evaluate at different phases of product development. During the build phase, their golden dataset — built through work with SMEs — represents how the model should respond to customer inputs. Vanta integrates LLM-as-judge into their CI/CD pipeline to automatically evaluate model outputs against this golden dataset. When an engineer pushes code that affects an AI feature, the system immediately signals whether that change improved or degraded the model's performance. They then monitor online quality as well to make sure what they see in their evals matches what they see in production.

#### **The real world is the ultimate “ev****aluation”**

Domain expertise can also come from your biggest experts: **your customers**.

Real-world usage often diverges from the best benchmarks and from initial eval datasets. Replit found early on that benchmark scores didn’t always predict user satisfaction:

> *“Sometimes the benchmark number goes up, but quality goes down. We started measuring quality from human feedback – explicit (‘I like it’) or implicit (‘I rolled back this change’).”*

You can A/B test prompts and measure whether they lead to fewer rollbacks, more accepted suggestions, or faster deployments. And you can only do that if you ship!

[**Suno**](https://www.amplifypartners.com/barrchives/how-suno-builds-ai-models-for-musicians) takes advantage of this in a clever way. 

When you generate a song in Suno, you actually get two songs back – not (just) because they’re generous, but because they can learn a lot from which you prefer. Here are two songs that their model things are equally good, and yet a human prefers one. Why? This kind of feedback, implied or otherwise, is exactly how you steer AI systems towards human preferences over time.

Ultimately, the best evals are living systems. They’re built from domain knowledge, refined through human judgment, and validated in the real world.

---

### ⚖️ **Should you build models, buy models, or both?**

The age-old question for all software is if you should build it or buy it, and many companies building AI products are facing the same dilemma when it comes to models.

**Replit **began its AI journey by training custom models in-house.

Early on, latency was mission-critical: existing models were too slow, and owning the full stack felt like the only way to deliver a seamless experience. But as off-the-shelf models rapidly improved in speed, the tradeoffs shifted. **Accuracy and cost, not latency, became the bottlenecks**. 

Latency mattered when the goal was to replace *AI code completion* – where every millisecond counted. But as Replit’s focus evolved toward replacing *labor *— building end-to-end projects automatically — the calculus changed.

If the Replit Agent could build something mind-blowing in three minutes, cutting that time to ninety seconds didn’t materially improve user value. So the team pivoted: rather than training full models from scratch, they now rely on off-the-shelf models fine-tuned for specific agent actions to boost reliability where it matters most.

Build vs. buy doesn’t just apply to training your own models though. It is about *capabilities* too. 

**Hex **spent months of engineering time building a complex caching system to get model latency down to an acceptable level for their Hex Magic product. But immediately after, a new OpenAI model came out. The performance was so much better than the previous generation of models that it rendered all of this engineering work completely obsolete!

Latency, cost, and even moderate accuracy gaps can disappear fast. The harder and more enduring advantage lies in **understanding model capabilities deeply**: knowing what they can do today, which problems future model generations are likely to solve for you, and where human or domain expertise still needs to fill the gaps.

Sometimes, off-the-shelf models simply cannot do what you need them to do. I’ve had several companies on the podcast for whom a lot of fundamental value is in the unique models they’ve trained:

- [**Abridge**](https://www.amplifypartners.com/barrchives/how-abridge-uses-ai-to-help-doctors-spend-more-time-with-patients-with-zachary-lipton-chief-technology-science-officer-at-abridge-and-raj-reddy-associate-professor-of-machine-learning-at-carnegie-mellon-university)** **— is building enterprise-grade AI for clinical conversations. You might think they could simply use off-the-shelf ASR models like Whisper. However, despite amazing advances in speech, medical language is tricky: models transcribe *Ozempic* as *Olympic*. Much of the medical lexicon consists of new or unusual terms that general-purpose models aren’t trained on and must be constantly updated.

- [**Cartesia**](https://www.amplifypartners.com/barrchives/how-cartesia-edges-out-the-big-labs-with-audio-ai-models-with-karan-goel-founder-and-ceo-at-cartesia)** **— is building a fast voice AI platform—and taking a big architectural bet on state-space models (SSMs). Transformers scale *quadratically* with context length: doubling your context window roughly quadruples the compute you need, which is expensive! SSMs process long, continuous data streams more efficiently and that tradeoff becomes pronounced as models move into multimodal regimes where context spans not just text, but massive amounts of audio and other temporal data.

There are still corners of the stack where building a model will give you a lasting edge. The challenge is in knowing where differentiation truly lives: in the architecture, in the model weights themselves, in the data, or in the scaffolding around them.

Remember, whether you build or buy your model, it is ultimately in service of a great product experience. Ori Goshen at** **[**AI21 Labs**](https://www.amplifypartners.com/barrchives/how-ai21-labs-builds-frontier-models-for-the-enterprise-with-ori-goshen-co-founder-and-co-ceo-at-ai21-labs) calls it “product–algorithm fit”:

> *T**here are great algorithmic capabilities out there today, but you need to find a way to make a product that uses them in a way that’s actually useful for customers. That judgment depends on understanding AI roadmaps and capability shifts—seeing not just what today’s models can do, but what tomorrow’s models almost certainly will.*

---

### 🏗️ **How to build and structure your AI teams**

Some of the fastest-moving AI companies I’ve seen this year have zero papers, zero PhDs, and zero guilt about it.

If you’re building applied AI products on top of foundation models from big labs, your team might look more like a modern software org: strong in prompt engineering, MLOps, and product intuition. 

Companies like [**Regal**](https://www.amplifypartners.com/barrchives/how-regal-builds-real-time-voice-agents-for-contact-centers) and [**dbt Labs**](https://www.amplifypartners.com/barrchives/building-tomorrows-data-ecosystems-for-ai-and-analytics-with-dbt) have built valuable AI features without publishing a single research paper or training models from scratch.

Nearly every applied AI initiative I’ve seen started small: a hackathon project, a curious engineer, or an exec tinkering with a model. Once an early demo proved useful, a small AI team was born. As AI organizations matured, many evolved into a platform-plus-product model: an AI platform team that builds shared capabilities (evals, inference, data pipelines) and helps product engineers ship responsibly. At that stage, internal education becomes the unlock: teaching every product team how to build with AI!

But many companies do need explicit research capabilities. Either because they’re pushing the boundaries of what’s possible, or because off-the-shelf models can’t solve their problem. For these companies, a new challenge emerges: balancing cutting-edge research with shipping actual products.

Two things then matter most: **who you hire**, and **how you structure them**.

#### **1) Hiring the right people **💼

Startups aren’t academic classrooms and they often can’t afford to bring on pure researchers.  The best research hires blend research depth with deep curiosity and strong instincts around engineering and product.

When it comes to hiring the right people, several of the leaders I spoke to specifically called out how important it is to filter research talent beyond just “is this person a good researcher?”

Cris Valenzuela ([**Runway**](https://www.amplifypartners.com/barrchives/runways-vision-for-redefining-the-intersection-of-technology-and-creativity) CEO) described this mindset perfectly:

> *"We tend to run Runway as a neural network, almost as a model itself. You gather data, you have some weights, you use the data to modify the weights... Runway operates like that, where we look for people who can change their weights and the way they work with others as new data comes in."*

AI moves quickly, so Runway specifically asks questions in the interview to screen out anyone too rigid in how they’ve done things in the past.

**AI21** (they build AI for the enterprise) looks for a specific combination of skills when they hire for their AI teams:

> *“You need a combination of people with algorithmic understanding and a theoretical background, but who are also good engineers. Large training workloads are mostly systems problems– distributed computing, cluster reliability, debugging when things break.”*

In practice, this means AI teams need people who can debug CUDA kernels *and* design training objectives, who understand transformer architectures *and* can optimize inference costs for production.

**Cartesia**, which builds low-latency voice models, is built around the same principle. They hire researchers who can thrive under constraints – people who can move between deep algorithmic work and real-world engineering, and who see latency, cost, and user experience as an exciting part of the research problem.

#### **2) Structuring the work **🍱

Even the most talented researchers need the right environment to succeed. The best startups I spoke with don’t separate research and product—they make the boundary intentionally porous. They also often adeptly balance short and long term bets.

**Runway **has been a research company from the start. Their team helped create the original Stable Diffusion model and has since released multiple state-of-the-art video generation systems. Cris told me their secret is balancing chaos and focus:

> *“You operate as a research organization – experimenting, running with assumptions, testing things. If you don’t have an objective to optimize for, it might just be chaos. It’s about experimenting while holding a long-term objective.”*

Runway’s org reflects that duality: big bets like new model generations get long-term investment, while smaller teams run fast post-training and interface experiments. The result is an org that can balance iteration and ambition.

**Cartesia** runs a hybrid structure: self-directed pods, each owned by a founder. Chief scientist **Albert Gu** acts as the company’s *taste and problem-selection engine*—deciding what’s worth solving and ensuring academic work connects directly to product needs. They keep their academic bridge open (with cofounders still at CMU and Stanford) to explore longer-horizon research, while the company executes on short-term production goals that customers want *today,* like better latency, multilingual speech, and on-device deployment.

Zach Lipton, the CTO at **Abridge**, talked a lot about the feedback loop between product and data when it comes to building AI products. So much of what OpenAI has done isn’t just better models or algorithms; it’s that they closed this loop in a really powerful way. ChatGPT generates this huge trove of conversations, which gets tied into this massive data labeling organization, which in turn fuels model development. The research impacts the product, and the product feeds back into the research.

It’s important to remember that while today’s ChatGPT feedback loops are tight, at the very beginning the research came *before* the product**.** In the earliest stages of deep-tech development — or in exploratory work where the innovation lives in the technology itself —**technical discovery often has to precede product definition.**

[**Naveen Rao**](https://www.amplifypartners.com/barrchives/building-deep-tech-beyond-the-saas-playbook-with-naveen-rao-vp-of-ai-at-databricks), three-time CEO/founder in AI-first companies and former VP of AI at Databricks, put it this way:

> *“SaaS product books actually put everyone in the wrong direction for deep tech. It doesn't work that way in deep tech — it's not about customer interviews from day one... You may not be able to know what to build until you understand the problem space well. When your innovation is in the tech part of it, first you’ve got to innovate there. You’ve got to build the tech.”*

Deep-tech product development often starts by **mapping the problem space** before chasing market validation. At **Mosaic**, that meant building an exploratory organization staffed with academic talent—PhDs and post-docs tackling hard problems in neural network training and scalability. The company engaged with open-source communities and technical collaborators across industries, using those relationships to refine its understanding of emerging architectures and bottlenecks. When your innovation is on the tech side, your early feedback loop is *with the frontier itself*, not just customers.

Research should generate product hypotheses. Products should generate research data. The org structure should make this loop fast and tight—co-locating researchers with product teams, measuring research by product impact, and treating qualitative and quantitative user feedback as a critical research input, not a distraction from "real" work.

### 3) 🔄 **The fa****st****est learners win**

The companies succeeding in AI aren't necessarily the ones with the biggest models or the most PhDs—they're the ones making smart bets about where to invest.

They know when evals need domain experts. They understand which capabilities will be commoditized by the next model release and which require building proprietary solutions. They've figured out if they need a research team at all, and how to structure it so research actually ships.

What separates winners from hype is clarity about where lasting advantage lives. This **clarity can be built through iteration**! Sometimes in building strong workflows and developer experience, sometimes in the evaluation pipeline built with domain experts, often in the feedback loop between product and data. The technical decisions flow from that strategic clarity.

The AI landscape will look different in six months. The companies that thrive won't be the ones who made perfect decisions today—they'll be the ones who built organizations that adapt as quickly as the models themselves.

---

### **📌 Bottom line**

And that's it! Here are the main takeaways:

- 🎯 **Domain expertise is the secret to great evals** — the best AI products integrate subject matter experts directly into engineering workflows, not as occasional reviewers but as active collaborators who help build golden datasets and evaluate model outputs.

- 🔄 **Real users are your ultimate test** — ship early and learn from actual usage patterns, implicit feedback, and A/B tests; public benchmarks and synthetic evals rarely capture how customers actually use your product.

- ⚖️ **Build vs buy is about capabilities, not just models** — focus on understanding what today's models can do, what tomorrow's will likely solve, and where your unique advantage lives (hint: it's rarely in training LLMs from scratch).

- 🧠 **Hire researchers who can ship** — if you need research capabilities, look for people who blend algorithmic depth with engineering pragmatism and can adapt quickly as the landscape shifts.

- 🏗️ **Structure teams for tight feedback loops** — the fastest-moving AI companies make the boundary between research and product intentionally porous, ensuring research generates product hypotheses and products generate research data.

- 🚀 **The fastest learners win** — AI advantage comes from building organizations that adapt as quickly as the models themselves, with clear strategic bets about where lasting differentiation truly lives.
