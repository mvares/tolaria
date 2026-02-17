---
aliases:
  - "How Shopify Executes Editions"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-essays|Publish Essays →]]"
Status: Evergreened
URL: "https://refactoring.fm/p/how-shopify-executes-editions?utm_source=substack&utm_campaign=post_embed&utm_medium=email"
"👓 Status": Not started
"Created time": "2025-04-24T10:00:00.000Z"
Date: 2025-07-09
"Has Notes":
  - "[[evergreen/the-age-of-everything-as-code|The age of everything-as-code]]"
  - "[[evergreen/durable-teams-vs-task-forces|Durable teams vs task forces]]"
Tags:
  - Guest
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 1dfbdf02-815c-801b-91b5-f533a03c950d
---

# How Shopify Executes Editions

#### **Release Philosophy**

#### **Planning & Scope**

#### **Execution & Convergence**

#### **Team Structure**

## 📞 Interview

---

Chat with meeting transcript: [https://notes.granola.ai/d/bdf8c599-e935-463b-bfcf-6c698f6799bf](https://notes.granola.ai/d/bdf8c599-e935-463b-bfcf-6c698f6799bf)

## 📑 Materials

---

## ✏️ Article

### Intro

There’s always been a gap — and will always there be — between how fast startups can operate vs big tech.

In many ways, this is an existential battle:

- Startups need to be fast because that’s the only way they can topple incumbents.

- Incumbents, in turn, need to prevent turning into slow, bureaucratic orgs incapable of building product, to avoid being disrupted by said startups.

Technology plays a big role in this: in times when tech *moves fast*, startups often have the higher ground, as they are *faster* at jumping on it. Conversely, when platforms change less, there is equally less opportunity.

Where does *today* fall on this spectrum? 

If you asked me a couple of years ago I would have said *meh* — web and mobile haven’t changed significantly over the last decade.

But AI, of course, has changed everything. Companies large and small are *scrambling* to embrace the AI opportunity, both internally—upgrading their own tech and processes—and externally—offering AI-powered features across products. 

So, whether or not we agree there is substance or it’s mostly hype for now, we can’t deny there is *race* going on — which is interesting to me because it reveals, among other things, which companies are able to *execute* properly under more urgency, and which simply are not. 

One company that I have followed closely over the years, because of its ability to steer fast and punch above its weight, is Shopify. You may remember our interview to [Farhan Thawar](https://refactoring.fm/p/running-a-remote-big-tech-with-farhan?utm_source=publication-search), VP of Engineering, and [Kaz Nejatian](https://refactoring.fm/p/kaz-nejatian?utm_source=publication-search), COO.

With 8000+ employees, out of which ~50% engineers, Shopify may not operate at the scale of Meta or Google, but is still squarely in big tech territory. Yet, Shopify often likes to *zag* when others *zig*: it stayed remote-first when its peers issued RTOs, doesn’t quite like meetings, and has a peculiar product strategy that focuses on two *big* releases per year: one during summer, and one during winter.

From the outside, it also appears to operate at a higher throughput than its peers: it was one of the first to embed AI as first-class citizen into its product (with the launch of Sidekick last year), and recently revamped all of its dev platform to make everything AI-native (MCP support, infrastructure-as-code, etc).

So last week I sat down with [Eytan Seidman](https://www.linkedin.com/in/eytanseidman/), Director of Product for the Developer Platform, and we talked for an hour about largely two things:

1. **How Shopify creates Editions** — why they do product like that, and how Editions come together from an operational point of view.

1. **How AI made Shopify rethink dev platforms** — what is going to change vs what principles still stand.

It was an extremely interesting chat — so here is what I learned! 👇

---

*Disclaimer: I am a fan of what Shopify is building and I am grateful to them for partnering on this piece. However, I will only write my unbiased opinion about the practices and tools covered here, Shopify included.*

*You can learn more about the latest Shopify Summer Edition below 👇*

[Summer Edition 2025](https://www.shopify.com/editions/summer2025)

---

### 🗺️ The Strategy of Shopify Editions

At first glance, Shopify’s model of shipping two major “Editions” a year seems to defy the very principles of continuous delivery that modern tech companies live by. How can a company with thousands of engineers orchestrate such massive, synchronized releases without grinding to a halt?

The answer is, as Eytan tells me, that the Editions are not what they seem.

They are not a *monolithic release* — they are a **storytelling layer** built on top of a robust, continuous delivery engine. They are designed to *capture customer attention* and create a coherent narrative, without sacrificing the speed and autonomy of individual teams.

Editions, however, are not cosmetic either: the features showcased are indeed made available after the big release. So how does this work in practice? 👇

#### **1) Dual-track execution **🔀

Shopify operates on two parallel tracks:

- 📈 **Continuous improvements** — throughout the year, teams ship features, fixes, and improvements as soon as they are ready. This maintains momentum and ensures the platform is constantly evolving. You can see this happening in public through their regular [developer changelogs](https://changelog.shopify.com/).

- 💥 **Biannual editions** — twice a year, they bundle the most significant updates into a single, cohesive narrative. An Edition isn’t just a list of features; it’s a story with a theme, designed to tell the world where Shopify is heading.

This strategy tries to balance a fundamental truth: engineers thrive on continuous delivery, but **customers and markets respond to *****moments***. 

While small updates get easily lost in the noise, Editions create a gravitational pull, forcing the ecosystem to pay attention. They give Shopify a powerful lever to communicate its vision and a clear *why* behind all the new *whats*.

#### **2) Balancing strategy & opportunities **⚖️

For an Edition to be successful you need a cohesive *theme*, which obviously can’t be cobbled together a few weeks before launch, but is neither fully formed from the start.

Eytan explains that leadership provides some *direction* early on, but remains flexible for opportunities. So, while some long-term strategic work is planned from the very beginning, it only makes for a fraction of teams’ time. A good chunk is left open to develop tactical ideas in response to where the market is going, to customer feedback, or to new emerging tech.

A perfect example of this was the Winter 2025 Edition — aka the [Boring Edition](https://www.shopify.com/editions/winter2025). While the focus on platform integration was clear from the start, a lot of the improvements (e.g. discounts with functions, functions on retail POS) were proposed bottom-up and came together during the period.

FOUR TYPES OF WORK 

#### **3) The Convergence Ritual **🔬

One the most unique parts of Shopify’s process is an internal ritual they call **“Convergence”**.

This is a dedicated, time-boxed period before each Edition launch where teams stop building *new* features and focus entirely on **integration and quality**. The goal is to move from a collection of siloed features to a single, seamless product experience.

DIVERGENCE / CONVERGENCE

During Convergence, teams are forced to simulate the end-to-end user journey. 

A team that built a new API doesn't just test the API — they have to use it to build a complete application, exactly as a third-party developer would. This uncovers friction points, integration gaps, and awkward workflows that would be invisible otherwise.

It’s a mechanism for:

1. Ensuring the final product is more than the sum of its parts

1. Creating a shared sense of ownership across the company, avoiding silos

1. Ensuring that when an Edition ships, it truly works as a cohesive whole

#### **4) Durable teams vs task forces **🎽

During our chat I asked Eytan what kind of team structure they use to deliver this, and in particular whether they use durable, long-lived teams which own specific product areas, or task-forces *assembled* to deliver the individual features.

Eytan says Shopify combines *both*:

- 🌳 **Durable Teams** — own complex areas where deep domain knowledge is critical. Permanent teams allow to build expertise over many years, which ensures the most critical parts of the platform are stable and stewarded by those who know them best.

- 🪖 **Task Forces** — are assembled to tackle new, experimental, or horizontal initiatives. For example, a task force might be spun up to build the first version of an AI feature that cuts across multiple product areas. This allows Shopify to bring together a diverse mix of experts to move quickly on a focused goal, without being burdened by the legacy or biases of any single product area.

The goal of this model is, in a way, to have your cake and eat it too. Durable teams provide the rock-solid foundation, while task forces provide the agility and firepower to make bold bets and drive the innovation that powers each new Edition.

Ultimately, this should help strike a balance between stability and innovation. So, if you are primarily working in one of the two modes, you can ask yourself these questions:

- **If you mostly do** **task forces / feature teams**: *are you creating valuable product expertise for the long term?*

- **If you mostly do** **long-lived teams**: *are you making enough bold bets, as opposed to incremental improvements?*

---

### **🏗️ Dev Platforms in the Age of AI**

In the second part of our chat, Eytan explained how AI forced them to rethink the fundamentals of their developer platform. It’s no longer enough to have good APIs and well-written docs — you have to build a platform that is *human-friendly *for today, but also **AI-ready **for the future.

As Eytan put it:

> *The ROI of doing things right has gone through the roof with AI.*

But what does "doing things right" mean? For Shopify, it means building a platform that is **declarative, code-first, and frictionless **— principles that were always valuable but have become existential in a world where both humans and AI agents need to interact with your platform 👇

#### **1) Frictionless by design 💨**

The biggest focus of Shopify’s developer platform in recent months has been **simplification**. 

Shopify is almost 20 years old, which means over time its platform sprawled into a large surface area that was hard to deal by developers and AI alike.

The latest edition brought a unified dev platform for both merchant developers and third party app developers, and a unified set of UI components to work with.

The simpler the platform surface area, the easier are things to build for both humans and AI.

#### **2) Everything as Code 🏛️**

While many platforms have invested heavily in visual builders and GUI-based configuration tools, Shopify has historically doubled down on a **declarative, code-first approach**.

Every aspect of their platform—from app configuration to access controls—can be defined through code and configuration files. It's the same philosophy behind Infrastructure as Code (IaC), which we've covered many times before: instead of clicking through web dashboards, you declare what you want in a configuration file.

If you ask me, IaC has always been a no-brainer, for many reasons:

- 🪄 **Reproducibility** — infra can be created, destroyed, and recreated consistently.

- ↩️ **Version control** — changes get tracked just like application code.

- 🤖 **Automation** — reduces human error and speeds up provisioning.

- 📑 **Self-documentation** — the code itself documents what exists and how it's configured.

None of this is new, but AI has flipped the economics:

- The overhead of writing config files vs using GUIs has largely vanished, because AI can create the former without us memorizing all the specific DSLs. 

- AI can’t navigate GUIs properly (yet!), which makes them even less appealing.

So, practically speaking, an AI coding assistant can’t click a button, but it *can* read the docs, understand that (e.g.) a new scope is needed, add the right line to the app’s config file, and deploy the app through the CLI.

Eytan believes this *declarative* foundation is the single most important prerequisite for AI dev platforms. The initial investment in building this "everything as code" model might have seemed like an incremental improvement a few years ago, but today, the ROI is mindblowing. 

It’s the groundwork that makes everything else possible.

#### **3) The IDE is the New Hub 🤖**

For as long as Eytan remembers, Shopify developers *split *their screens as follows:

1. **IDE **— for writing code and (sometimes) config files.

1. **Terminal **— for running CLI.

1. **Web browser **— for checking docs and operating apps in production.

This is all changing now, as **everything just happens in the IDE**: AI reads all the docs and provides instant, context-aware answers in Cursor; it updates app config files without humans touching the admin panels, and runs the CLI commands to update the deployed app.

On top of this, Eytan adds, MCPs further expand the *IDE scope* by allowing AI to *operate* full production apps: they can query the platform capabilities, look at logs to debug issues, and analyze ecommerce data to propose enhancements.

The final goal is an **invisible platform**. Developers never have to leave their natural environment, and never have to *context switch.* 

So, a long-lived mantra at Shopify is *"meeting developers where they are”*: at the beginning, this meant supporting their favorite programming languages, but now, in 2025, it increasingly means *enabling* their IDEs and AI assistants to do the work for them.

---

### **📌 Bottom line**

And that’s it for today! When I started this chat with Eytan, I expected to learn more about their peculiar release cycles — but we covered way more than that. 

Here are my favorite takeaways:

- 🎭 **Editions are storytelling, not waterfall** — the biannual releases create market moments while continuous delivery maintains velocity. It's not about choosing one or the other; it's about using both strategically.

- 🤝 **Convergence creates coherence** — dedicated integration periods where teams stress-test the full user journey prevent the feature soup that plagues many large platforms.

- 👥 **Hybrid teams balance innovation and stability** — durable teams build deep expertise in complex domains while task forces enable bold bets.

- 🚀 **Reduce friction to increase leverage** — every bit of cognitive load you remove from developers—whether through unified platforms, better tooling, or AI assistance—directly increases what they can build.

- 💻 **Declarative platforms are AI-native platforms** — by making everything code-first, Shopify created a platform that's equally accessible to humans and AI agents.

- 🏠 **The IDE is the new home** — meeting developers where they are increasingly means never making them leave their development environment. The platform comes to them, not the other way around.

See you next week!

Sincerely
Luca

#### Minimize friction

#### Platform principles

#### AI evolution
