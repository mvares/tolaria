---
aliases:
  - "New Tools and Techniques for 2024"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-essays|Publish Essays →]]"
Status: Evergreened
URL: "https://refactoring.fm/p/new-tools-and-techniques-for-2024"
"👓 Status": Discarded
"Created time": "2024-04-18T14:53:00.000Z"
Date: 2024-01-04
"Has Notes":
  - "[[evergreen/use-mermaid-for-diagramming|Use Mermaid for Diagramming]]"
  - "[[evergreen/prune-your-dependencies|Prune your dependencies]]"
  - "[[evergreen/use-design-systems|Use Design Systems]]"
  - "[[evergreen/use-owasp-top-10s|Use OWASP Top 10s]]"
Tags:
  - Essay
  - Mgmt
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: e3fa103f-fe94-45c7-b6d5-bdec6fefa9db
---

# New Tools and Techniques for 2024

### 📑 Materials

---

### ✍️ Post

---

Welcome to the first Refactoring edition of 2024! 🥳

For many teams, this time of the year is a time of reflection and planning, so I want to help by covering new, interesting stuff that you may use in the new year.

This edition is a list of recommended items, each with my own commentary about why you should consider it. Items are organized into four categories:

- 🔄 **Techniques **— engineering or management practices for your team. These are about working well together, and are agnostic from your tech stack. E.g. [Threat Modeling](https://owasp.org/www-community/Threat_Modeling).

- 🛠️ **Tools **— ready-made stuff that you can use to achieve a specific goal. I try to cover widespread use cases to maximize the chances that you benefit from the listed items.

- 🧱 **Platforms & Frameworks **— tech you use to build things upon. These are core pieces of your tech stack and may be coupled to your core language / infra choices. Examples from the past are [Backstage](https://backstage.io/), to create developer portals, or [NestJS](https://nestjs.com/), for full-stack JS apps (kind of Rails for JS).

I create this list once a year, and it is heavily inspired by the Thoughtworks’ [Technology Radar](https://www.thoughtworks.com/radar/) framework. To compile my list I do four things:

1. I go through my own list of tools that I have used this year, on my Notion.

1. I go through all the past year editions of the Thoughtworks’ [Technology Radar](https://www.thoughtworks.com/radar/).

1. I reach out to the smartest tech leaders I know about the best things they started using/doing.

1. I survey people in the Refactoring community.

Items should meet a fine balance between being 1) consolidated enough that I can safely recommend them, and 2) novel enough that chances are you are not using them yet.

Basically, we are picking things somewhere in between the early adopters and early majority stages 👇

![image](../assets/2727ed90b101437d.png)

Finally, it goes without saying, none of these tools paid me to be included here. I just used them personally and I am happy to recommend them.

Let’s dive in!

### 🔄 Techniques

---

#### 1) OWASP Top 10 Lists 📋 

Yes, *lists*, plural! The *flagship* [OWASP Top 10](https://owasp.org/www-project-top-ten/) has long served as a reference for critical security risks to web applications, but did you know OWASP publishes *other *lists, too?

Here are some relevant ones:

- [OWASP for API security](https://owasp.org/API-Security/editions/2023/en/0x00-header/)

- [OWASP for LLM applications security](https://owasp.org/www-project-top-10-for-large-language-model-applications/)

- [OWASP for mobile applications security](https://mas.owasp.org/)

The easiest way to use these checklists is to include them in your [design doc](https://refactoring.fm/p/design-docs?utm_source=substack&utm_campaign=post_embed&utm_medium=web) templates. Not all items will be relevant all the time, but it takes zero effort to just go through them at design time to make sure you are not missing anything crucial.

#### 2) ADRs ✏️

Speaking of design docs, a particular implementation of them is **Architecture Decision Records** (ADR), which, as the name suggests, are meant to capture important architecture decisions together with its context and consequences.

ADRs are like commits — they are immutable and meant to be *snapshots* of past decisions. When you change the same piece of software in the future, you just create a new ADR.

Design docs can *naturally* turn into ADRs when the project is complete. You can find everything you need to know about ADRs in this [awesome repo](https://github.com/joelparkerhenderson/architecture-decision-record) by Joel Parker Henderson.

#### 3) Design Systems 🎨

Design systems are not a novel idea — but they are an idea that has only been growing and improving with time.

Design systems address two issues: 1) delivering *consistent* products at scale, and 2) making design work *more efficient*.

What started as simple, static style guides, usually for corporates, has evolved today into full component libraries and best practices that can dramatically improve any team’s workflow. Modern design systems also bridge the gap between design and development: they are typically coded, version-controlled, and supported by dedicated tools, like [Storybook](https://storybook.js.org/).

So, just like there is consensus today about investing in platform and DX, like good CI/CD and automated testing, I believe design systems are going to follow the same route and becoming commonplace.

Here are a couple of recommended resources:

- [Design Systems](https://www.designsystems.com/) — a publication by Figma entirely dedicated to… well, you guessed it.

- [Design ADRs](https://zeroheight.com/blog/capturing-your-design-system-decisions/) — we covered benefits of ADRs above, and you can make basically the same arguments for design work. Checkout this great article to learn more.

#### 4) AI-powered meetings 🤖

One of the best use cases for AI, today, is to improve meetings. There exist several tools now that can, automatically:

- Summarize stuff that has been discussed

- Extract action items

- Create video chapters so you go can back to specific moments

This is helpful in many ways:

- It aligns people about the next steps

- It creates decision records for future reference

- It creates a place where you can have good async conversations about the meeting subject

All of these in turn allow for *less* people to join meetings, because they have a good way to catch up afterwards.

My favorite tools for this are [**TL;DV**](https://tldv.io/), [**Otter**](https://otter.ai/), and [**Bluedot**](https://bluedothq.com/). Key features are similar — Bluedot it is the simplest and only supports Meet, TL;DV supports Meet and Zoom, while Otter supports Meet, Zoom, and Teams. 

All these tools have generous free tiers, work well and are easy to use. In 2024, they are a no-brainer.

#### 5) Dependency pruning ✂️

Most applications today have just too many dependencies. Dependencies spread out for many reasons:

- Templates and boilerplates bring in stuff that you don’t use.

- Different teams use different libraries for the same purpose (e.g. HTTP calls).

- Dependencies from dead or pruned code are never removed (”maybe this is used elsewhere?”)

The proliferation of dependencies brings various problems:

- 🔒 **Security **— they increase your application’s attack surface

- 🚚 **Release **— they increase build and deploy times

- 🔧 **Maintenance **— they require constant work to be kept up to date

The best way to keep your footprint small is prevention:

- Create a developer portal to keep consistency across teams (e.g. with [Backstage](https://backstage.spotify.com/))

- Explicitly favor using already-used libraries (e.g. you can write this down in your design doc template)

- Whenever you remove some code, check if you can remove some dependency

On top of this, you can also do some periodic clean-up — e.g. once a quarter — where the whole team spends a few days squashing unused / redundant dependencies. Or, if you do [bug duty](https://refactoring.fm/i/139963364/bug-duty), you can dependency pruning part of the duties.

### 🛠️ Tools

---

#### 7) [Pinecone](https://www.pinecone.io/) 🌲

Vector databases exploded in popularity this year. Teams who integrate LLMs into their applications often need a way to store and retrieve their data that is suitable for AI — and that’s what vector databases are for.

Pinecone is the most popular vector database out there. It is fully managed, simple to use, and it plays nicely with other tools in the AI stack.

I have written more about LLMs use cases and architectures here 👇

[https://refactoring.fm/p/how-to-integrate-llms](https://refactoring.fm/p/how-to-integrate-llms)

#### 8) [dbt](https://www.getdbt.com/) 🔀

With the rise of AI, the whole *data stack* is getting front and center. Since teams can now leverage their data for good, there is more attention than ever to data transformation and overall lifecycle.

In this context, [dbt](https://www.getdbt.com/) has become extremely popular for creating data pipelines and managing the ETL workflow. It has a strong focus on good engineering practices through reusable data models, testing and documentation features, and version control.

![image](../assets/606bf7d3926d496f.png)

It is both available as open source and as a hosted solution and has plenty of community packages for testing, observability, and more. 

It also sports plenty of [integrations](https://www.getdbt.com/product/integrations): from regular dbs like Postgres, to data warehouses like Redshift, BigQuery, and Snowflake, to various business intelligence and orchestration tools.

#### 9) [Mermaid](https://www.thoughtworks.com/radar/tools/summary/mermaid)

Mermaid is a diagramming tool that uses Markdown to create and modify complex diagrams dynamically.

I am a visual person, and I have probably created hundreds of diagrams in my life. Well, diagrams are always a mess to manage at a team level: you move around jpegs, lose track of the source, get fixated with style, and more.

![image](../assets/f2c07c1953b649fb.png)

Mermaid’s code-first approach fixes most of these issues. In fact, you can now version diagrams just like you do with code, and update them easily. You can also define themes globally, so you keep your focus on content, and saving a ton of time.

Mermaid is almost universally loved and has an incredible number of [integrations](https://mermaid.js.org/ecosystem/integrations-community.html), my favorite being those with [Github](https://github.blog/2022-02-14-include-diagrams-markdown-files-mermaid/) and [Notion](https://lukemerrett.com/using-mermaid-flowchart-syntax-in-notion/).

#### 10) [Snyk](https://snyk.io/)

We covered Snyk for the first time a few months back, in the article about security:

[https://refactoring.fm/p/how-to-write-secure-code](https://refactoring.fm/p/how-to-write-secure-code)

Snyk is a great tool for securing a lot of stuff: code, dependencies, containers, infrastructure-as-code, and more. It integrates directly into dev tools and workflows, making it easy for teams to find and fix vulnerabilities.

It runs both SAST (Static Application Security Testing) to intercept insecure programming patterns, and SCA (Software Composition Analysis) for doing the same on your dependencies.

It is my #1 recommended tool for security.

### 🧱 Platforms & Frameworks

---

#### 11) [Pipedream](https://pipedream.com/)

All teams should have a fast, battle-tested way to build simple automations. Think notifications, data entry, triaging, and more.

If you are in for a no-code solution, [n8n](https://n8n.io/) and [Make](https://make.com/) are my favorites. But if you are an engineer and are happy to throw some code in the mix, you should consider [Pipedream](https://pipedream.com/).

Like others, Pipedream enables the connection of APIs and the automation of tasks and workflows. But it also provides a serverless environment for running code, it supports various programming languages, and offers a vast library of pre-built components. While coding often looks like an afterthought on tools like Zapier, on Pipedream it is a first-class citizen.

I moved most of my personal automations to Pipedream. For example, I store my calendar events on Notion and automatically assign them to relationships (day, tags, etc.) by using a combination of no-code steps and simple node.js scripts 👇  

![image](../assets/4524de44d3b04f9e.png)

#### 12) [**Contentful**](https://www.contentful.com/)** **📑

If you are not using a CMS for you product yet, chances are you should. I mean a *headless *CMS, not a full-stack one like Wordpress.

Headless CMSes provide a backend for creating and managing content, an API, but no frontend interface. You use them to handle content on marketing pages and copy on your product interface.

The main goal of using a CMS is to decouple copy updates from software releases, and make the former an easy task that even non-technical people can perform. A CMS is also invaluable for localizing content in multiple languages, and for handling content *at scale*, on thousands of pages.

There are plenty of capable CMSes these days, and my top pick is [Contentful](https://contentful.com/). We used it extensively at my previous startup to power millions of SEO pages, localized in 4 different languages.

![image](../assets/fd7cfe115fa74b3b.png)

With Contentful you can define your own content types and create a model that fits your needs. It has a CMS-as-code approach, so you can handle your content model (but, crucially, not content itself!) the same way you do with code: with version control, releases, etc.

Having been around for many years, it is extremely feature-rich and has plenty of integrations. Recommended! 👌

#### 13) [Playwright](https://playwright.dev/) 🔍

Playwright is a free Node.js library from Microsoft for creating and running end-to-end tests on web applications.

End-to-end testing is a tricky task that easily leads to unreliable results and a lot of maintenance. Playwright minimizes this with a lot of great features, like the support for multiple browsers, various emulators, auto-waits for reliability, browser contexts for persistent sessions, the ability to mimic notifications, geolocation, and more.

![image](../assets/f8cb23b3bf66425b.png)

The main other framework for end-to-end testing is [Cypress](https://www.cypress.io/). Each framework has its own strengths — but I would eventually pick Playwright over Cypress for its support to multiple languages, speed, and ability to create more complex scenarios. Cypress, on the other hand, is probably easier to setup and use for beginners, and it’s a solid choice nonetheless!

```javascript
import { chromium, FullConfig } from '@playwright/test';

async function globalSetup(config: FullConfig) {
	const { baseURL, storageState } = config-projects[0]-use;
	const browser = await chromium. launch);
	const page = await browser.newPage);
	await page-goto(baseURL!);
	await page.fill('input[name="user"]', 'user');
	await page.fill('input[name="password"]', 'password');
	await page.click('text-Sign in');
	await page.context().storageState({ path: storageState as string });
	await browser.close();
}
export default globalSetup;
```

#### 14) [Airplane](https://www.airplane.dev/)

Airplane is a developer platform for building rich internal tools and workflows. It is particularly useful for creating dashboards, “scripts-with-an-interface” tools, and human-in-the-loop workflows.

With respect to other *low-code* tools, Airplane has a unique approach, in that it is *code-first*. Everything can be specified with code, which means your tools get version control, releases, and everything you would expect from regular code.

Still, the code you need to write is very little! You can select from a vast library of tables, forms, charts, and more, to build apps, which can also be integrated with your own APIs and custom components.

![The simplest use case for Airplane is turning simple one-off scripts into scheduled jobs with a light interface. You do this literally in minutes.](../assets/04fc46e0b3d74d34.png)

When you get into the mindset of creating tools for your workflows, the use cases for Airplane are infinite, and can significantly reduce manual work for both technical, and non-technical folks. 
