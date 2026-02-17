---
aliases:
  - "A Tech Radar for 2023"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-essays|Publish Essays →]]"
Status: Evergreened
URL: "https://refactoring.fm/p/tech-radar-2023"
"👓 Status": Not started
"Created time": "2024-04-18T14:53:00.000Z"
Date: 2023-01-19
"Has Notes":
  - "[[evergreen/beware-superficial-cloud-native|Beware superficial cloud native]]"
  - "[[evergreen/beware-spa-by-default|Beware SPA by default]]"
  - "[[evergreen/beware-hybrid-remote-without-remote-native|Beware hybrid remote without “remote native”]]"
  - "[[evergreen/threat-modeling|Threat Modeling]]"
  - "[[evergreen/cognitive-load-assessment|Cognitive Load Assessment]]"
  - "[[evergreen/path-to-production-mapping|Path-to-production Mapping]]"
Tags:
  - Not for HH
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 1c091b31-5de2-4b80-b579-28c830fa4199
---

# A Tech Radar for 2023

### 📑 Materials

---

[https://www.thoughtworks.com/content/dam/thoughtworks/documents/radar/2022/10/tr_technology_radar_vol_27_en.pdf](https://www.thoughtworks.com/content/dam/thoughtworks/documents/radar/2022/10/tr_technology_radar_vol_27_en.pdf)

### 💡 Ideas

---

### ✍️ Post

---

For many teams, this time of the year is a time of reflection and planning. So I want to spend this edition by covering some new techniques, tools, and frameworks that you may want to adopt for the new year.

And appropriately, just a few weeks ago, Thoughtworks released the new version of its [Technology Radar](https://www.thoughtworks.com/radar/).

For those who don’t know, Thoughtworks is one of the most influential tech consultancies in the world. Some of its leaders, like [Rebecca Parsons](https://www.thoughtworks.com/profiles/leaders/rebecca-parsons), or [Martin Fowler](https://en.wikipedia.org/wiki/Martin_Fowler_(software_engineer)), have literally made the history of software development.

The Technology Radar, released roughly every six months, is an opinionated list of items (100+), organized into four **categories** and four **rings***.*

![Not gonna lie, drawing circles is hard.](../assets/e85791fee66741e8.png)

Categories represent what each item is about:

- 🔬 **Techniques **— elements of development process and ways of structuring software.

- 🧱 **Platforms **— things we build software on top of.

- 🔨 **Tools **— standalone components (e.g. databases) or software development tools.

- 🔤 **Languages & Frameworks **— quite self-explanatory!

Rings, instead, represent Thoughtworks’ subjective *evaluation of* items, based on their experience with them.

- 🟢 **Adopt **— items that Thoughtworks had the best experience with. You can consider them best practices — there is no doubt they are proven and ready to use.

- 🟡 **Trial **— items that are safe and ready to use, but not as completely proven as those in the Adopt ring. I feel *trial* is the perfect word here — you may do experiments and decide whether to move forward.

- 🟣 **Assess **— items worth keeping an eye on but that you shouldn’t necessarily try, unless they are a particular good fit for you. 

- 🔴 **Hold** — items they haven’t had a good experience with and they wish the industry would stop using.

In this article I will go through the most interesting items reported by Thoughtworks (both good and bad), and comment on them based on my own experience, and that of people in the Refactoring community.

The idea is to give you a ***compendium***** of good stuff** you can try in 2023… and also stuff you should probably avoid.

Let’s go!

### 1) 🟢 Path to production mapping

Path to production mapping is a practice where teams map all the steps of the release process, in order to identify bottlenecks, risks, and opportunities for improvement.

It is often run as a workshop, as Thoughtworks itself explains:

> *First, the steps in the process are listed in order, from the developer workstation all the way to production. Then, a facilitated session is used to capture further information and pain points. The most common technique we see is based on *[*value-stream mapping*](https://en.wikipedia.org/wiki/Value-stream_mapping)*, although plenty of *[*process map*](https://caroli.org/en/path-to-production/)* variants are equally valuable.*

Steps should include both technical parts (e.g. build, automated testing) and non-technical ones (e.g. QA on a staging environment) to get the full picture of how software release happens.

For this reason, this is most often a cross-functional activity where many stakeholders are involved. Daniele Salvatore, who leads cloud efforts at FAO, weighed in on this 👇

> *I applied the Path To Production mapping technique while defining the process of the newly created cloud environment at FAO.

Some processes changed as the organization underwent its digital transformation and the mapping exercise helped streamline the product releases, ensuring the required quality gateways were enforced.

One key factor to consider is ensuring that every stakeholder in the process is represented during the exercise.*

A snappy release process that allows you to ship in a few minutes is one of the main factors that separate elite teams from average ones. There is convincing research that it might very well be *the* main factor 👇

[https://refactoring.fm/p/how-shipping-fast-changes-your-life](https://refactoring.fm/p/how-shipping-fast-changes-your-life)

Slimming it down is one of the best resolutions you can make for the new year.

### 2) 🟢 Cognitive load assessment

Team cognitive load measures how hard or easy teams find building and maintaining their software.

A high cognitive load can be a symptom of various diseases, like high technical debt, or wrong organizational design.

For tech teams, this concept was popularized by Matthew Skelton and Manuel Pais, authors of [Team Topologies](https://www.goodreads.com/book/show/44135420-team-topologies), a recent (~2019) but already foundational book that has had a big impact on the way I think about teams these days.

They even designed a template you can use to assess the cognitive load. You can find it [**here**](https://github.com/TeamTopologies/Team-Cognitive-Load-Assessment).

You can run the assessment periodically, on a quarter or semester basis, together with your wider planning activities.

If you have never done this before, this is a great addition to your arsenal for this year. 

### 3) 🟢 Threat modeling

A *threat model *is the description of an application and its environment through security glasses.

So, [*threat modeling*](https://wiki.owasp.org/index.php/Category:Threat_Modeling) is a family of activities you pursue to 1) identify vulnerabilities, and 2) design countermeasures to prevent or mitigate threats.

Historically, designing for security has often followed the ***security sandwich**** *approach: you address security during design, and you test things at the end. This *waterfall-ish *approach, though, clashes with reality: specs often change during development, so you end up testing for things that are 1) incomplete, or 2) not relevant anymore.

Good threat modeling should be applied continuously throughout the whole development lifecycle. You can find a thorough description of the process, together with best practices, in the [OWASP wiki page](https://wiki.owasp.org/index.php/Category:Threat_Modeling).

### 4) 🔴 Satellite workers without “remote native”

Hybrid work setups where part of the team is co-located, and part of it works remotely, are very challenging to manage properly.

People at the office naturally benefit from more face time with managers and the higher *communication bandwidth*. If you do not design your processes intentionally, it is hard for remote folks to get equal treatment.

Wait, Luca, are you saying remote work is *worse*? 

No. I am saying that if you let communication flow naturally without proper design, things will optimize around the clusters of people at the office, making it a shitty experience for those at home.

The best way to run hybrid teams is to run everything *remote* by default. Communications are async-first, everyone joins meetings with their own laptop, etc.

### 5) 🔴 SPA by default

There has been a tendency in recent years to use SPAs (*single page applications*) as the **default architectural choice** for frontend applications.

While SPAs are of course not wrong *per-se*, I feel many people choose them without being aware of the **set of tradeoffs** they are getting themselves into.

SPAs are **challenging** in many departments, like SEO, initial loading times, fine-grained analytics, browser history management, and more. So, based on your requirements, they may or may not be the best architectural choice for your app.

In recent years, interesting frameworks like [Hotwire](https://hotwired.dev/) and [Remix](https://remix.run/) have come up with strategies to keep navigation and more business logic on the server, while still enabling good user experience. You should check them out!

### 6) 🔴 Superficial Cloud Native

Cloud providers today have a strong influence on how applications are designed.

That’s because, over time, they gradually expanded from simply *renting servers* to people, to running *managed services* that you can use like building blocks for composing your software.

Since these services are well-designed in isolation, you may be fooled into thinking that by taking many of them and combining them you will *naturally *end up with a good design.

This is wrong, of course, and lies at the core of many mistakes people do with trendy patterns like microservices, serverless, and more.

Cloud services provide real, tangible benefits, but they should *support* your system design — which is largely independent from them — rather than the other way around.

You can find more ideas about cloud, monoliths and microservices, in these recent articles:

- 🗿 [**Monoliths vs Microservices**](https://refactoring.fm/p/monoliths-vs-microservices)

- ☁️ [**Cloud vs On-premise Infrastructure**](https://refactoring.fm/p/cloud-vs-on-premise)

### 7) 🟢 [Backstage](https://backstage.io/)

Backstage is an open-source platform, created by Spotify, to build developer portals for your teams. It uses *TechDocs*, also created by Spotify, which allows to create Markdown doc files that live together with their code, making it easier to keep them updated and discoverable by the team.

![image](../assets/62011c7850154d22.png)

[Pamela Gotti](https://www.linkedin.com/in/pamelagotti/?originalSubdomain=it), CTO at Credimi, reports on this 👇

> *I do use Backstage and I totally love it! We're using it to keep the documentation of our hundreds + microservices in one place and close to the code as possible!*

Backstage can be used to track ownership of the various services (i.e. via the [Software Catalog](https://backstage.io/docs/features/software-catalog/software-catalog-overview)), and also streamline operations via the so-called [Software Templates](https://backstage.io/docs/features/software-templates/software-templates-index).

Its final goal is to enable autonomous teams by promoting good documentation and good standards.

### 8) 🟢 [Great Expectations](https://docs.greatexpectations.io/docs/)

For ~10 years I ran a startup in the travel space, where we had to integrate data from hundreds of different sources about points of interests, modes of transport, schedules, and more.

Ensuring the quality and consistency of such data was a nightmare that involved a lot of manual work — and, despite this, we often ended up discovering problems in production, reported by somebody on the team, or, worse, customers.

Great Expectations wants to fix this, by doing three things:

1. **Expectation **— you write *expectation* statements about your data in a declarative, human-readable language, to enforce constraints and the *shape* of your data. 

1. **Validation **— it runs automatic pipelines on your data, by using the *expectations* you have created, and generates comprehensive reports.

1. **Documentation **— it takes expectations and validation outcomes and uses them to create *data docs —**** ***HTML pages that work as a continuously updated data quality report.

![image](../assets/498e42dbe0bc4aca.png)

### 9) 🟢 [k6](https://k6.io/)

Load testing has long been a pain in the… development lifecycle, because of its inherent complexity and lack of modern tools for it.

K6 fills this gap. It allows you to write simple tests in Javascript and run them in CI/CD pipelines. Results can be displayed easily on external visualization tools like Grafana and New Relic.

![image](../assets/5a2238ae262b4ade.svg)

K6 is open-source, supports multiple testing modes, and has also a SaaS version that is simple to use and has more useful features, like simulating load from geographically distributed zones. 

### 10) 🟢 [NestJS](https://nestjs.com/)

For a long time, one of the big drawbacks of working with Node.js has been the lack of opinionated frameworks with sane defaults about the general application architecture.

For old grunts like me, coming from the likes of Rails or Django, this was a real concern.

Over the last years, NestJS filled this gap and reached a consensus that seemed unimaginable in a community that, instead, is famous for being fragmented.

![image](../assets/b66b30d6427d428c.png)

In Nest’s own words 👇

> *Nest provides an out-of-the-box application architecture which allows developers and teams to create highly testable, scalable, loosely coupled, and easily maintainable applications.*

And the Refactoring community only had great things to say about it 👇

> *We use Nestjs in production for our GraphQL API, REST API, some serverless function. We are pretty happy with it, the module structure and dependency injection system is perfect to build reusable modules.
*
— [Titouan Benoit](https://www.linkedin.com/in/titouanbenoit/?originalSubdomain=fr), CTO at Dotfile

> *+1 for Nest.js - used it for a couple of years, first as early-ish adopter in minor project, then larger commercial product for last few years.*

> *Go for Nest.JS, very opinionated but enforces you to follow good principles. You can easily connect any ORM, and expose any interface that you would like to.

— *[Pawel Kunicki](https://www.linkedin.com/in/kunickipawel?originalSubdomain=pl), Staff Software Engineer at Moonpay
