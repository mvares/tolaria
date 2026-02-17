---
aliases:
  - "The age of everything-as-code"
"Is A":
  - Evergreen
"Last Tweeted": 2025-12-22
"Created at": "2025-08-05T06:58:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to":
  - "[[essay/how-shopify-executes-editions|How Shopify Executes Editions]]"
  - "[[essay/how-to-design-your-tech-stack-for-ai|How to Design your Tech Stack for AI]]"
  - "[[monday-ideas/monday-187|Monday #187]]"
"Updated at": "2025-12-22T09:52:00.000Z"
Status: Not started
Tweet: "The age of everything as code is emerging, driven by AI's strength in code generation. Companies like Shopify and Convex embrace a declarative, code-first approach, allowing configurations and controls to be defined through code instead of GUIs. Benefits include:\n↳ 𝗥𝗲𝗽𝗿𝗼𝗱𝘂𝗰𝗶𝗯𝗶𝗹𝗶𝘁𝘆\n↳ 𝗩𝗲𝗿𝘀𝗶𝗼𝗻 𝗰𝗼𝗻𝘁𝗿𝗼𝗹\n↳ 𝗔𝘂𝘁𝗼𝗺𝗮𝘁𝗶𝗼𝗻\n↳ 𝗦𝗲𝗹𝗳-𝗱𝗼𝗰𝘂𝗺𝗲𝗻𝘁𝗮𝘁𝗶𝗼𝗻\nAI reduces the overhead of writing configuration files, making this model increasingly appealing for developers and enhancing the potential for automation and efficiency."
notion_id: 246bdf02-815c-80ce-9356-dc0d2dabdfe8
---

# The age of everything-as-code

The age of everything as code?

One of the most underrated trends that are developing as a second-order effect of AI, is expressing everything as code.

AI is still generally bad at using GUIs and navigating websites, while it’s amazing at reading and writing text — which means that, in your tech stack, whenever you can do something with code (instead of e.g. a dashboard or an admin panel) you probably should.

Infrastructure-as-code has been a thing for a long time, but recently I spoke with several teams who report going further: Shopify designed their developer platform to allow all configuration to be expressed as code, and so did Convex.

This strategy has *always* had upsides — think reproducibility, version control, self-documentation, automation — but at the expense of more cumbersome UX and having developers remember complex DSLs.

What’s changing now is that the downsides have largely disappeared, because AI is extremely good at writing this stuff, leaving you mostly with the upsides.

---

We discussed this several times lately: I discovered that Shopify [betted the farm](https://refactoring.fm/i/167520760/everything-as-code) on **configuration as code**, and Convex [goes even beyond](https://refactoring.fm/p/how-to-design-your-tech-stack-for) and talks about **everything as code**.

This strategy has *always* brought benefits — reproducibility, version control, self-documentation, automation — but at the expense of more cumbersome UX and having people need to remember complex DSLs. The good thing is that the downsides have largely disappeared now, because AI is extremely good at writing this stuff, leaving you mostly with the upsides.

Linking below the article I wrote with Jamie from Convex, which explains this well 👇 

[https://refactoring.fm/p/how-to-design-your-tech-stack-for](https://refactoring.fm/p/how-to-design-your-tech-stack-for) 

---

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
