---
aliases:
  - "How to Write Secure Code"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-essays|Publish Essays →]]"
Status: Evergreened
URL: "https://refactoring.fm/how-to-write-secure-code"
"👓 Status": Not started
"Date HH": 2025-02-06
"Created time": "2024-04-18T14:53:00.000Z"
Date: 2023-03-09
"Has Notes": "[[evergreen/threat-modeling|Threat Modeling]]"
Tags:
  - Software
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 5f3e3ca9-35ce-45a0-8177-3a5b78cee1d5
---

# How to Write Secure Code

### 📑 Materials

---

- [https://www.goldfiglabs.com/guide/saas-cto-security-checklist/](https://www.goldfiglabs.com/guide/saas-cto-security-checklist/)

- [https://www.security4startups.com/controls-checklist/](https://www.security4startups.com/controls-checklist/)

- [https://review.firstround.com/how-early-stage-startups-can-enlist-the-right-amount-of-security-as-they-grow](https://review.firstround.com/how-early-stage-startups-can-enlist-the-right-amount-of-security-as-they-grow)

### 💡 Ideas

---

- Avoid security sandwitch

- Engineers are not necessarily trained to know what secure code means

- Support by management in prioritizing security

- Include security in your design docs

- PR checklists

- Integrate security tools in your CI/CD

- Do [Untitled](https://www.notion.so/e0c7ba0e19294b7f8afe66c09513b322)

- Embed security into engineers performance frameworks

- Periodic security audits

- Pen Testing

#### Tools

- Compliance

- Pipeline / Development

- In production

- Real-time protection service

### ✍️ Post

---

Security is a peculiar topic in software because it is, at the same time:

- Undisputably *crucial* to the long-term success of an organization, and

- Completely *abhorred* by almost all developers I know

I can go even further and say that, in an ideal ranking of the most despised areas of engineering work, security ranks higher than writing docs and maintaining tests.

I believe there are two reasons for this:

- **Utility** — while things like tests and docs display at least some short-term benefits, taking care of security looks like pure overhead (until it doesn’t).

- **Complexity** — security topics are genuinely complex, and most developers are not trained in them. Managers, of course, even less so.

So, in many teams, this responsibility is all left on the shoulders of a few savvy senior engineers, who have to fight basically everybody else — their peers, PMs, leadership — to get things done.

Of course, we can do better than this.

This article is meant to be a primer about how to deal with security properly. I will cover the most sensible things you should do, without overwhelming engineers.

### 🌡️ Understand your risk tolerance

To set expectations right, it’s important to understand that there is no silver bullet for security, nor a *standard* process that works for all companies.

In fact, different companies are exposed to different kinds of threats, based on the products they build: a healthcare or financial product carries different risks than e.g. a remote job board.

You should be aware of such risks, decide your level of tolerance, and act accordingly. Investing in security often trades off other dimensions, like speed, or profitability, so you should be intentional about such an investment.

In the end you won’t probably be able to *zero in *on all the possible risks, and that’s… fine.

### 🏢 Security is organizational

The second *posture* to get right is that security is mostly an *organizational* topic. Good security is achieved via good process and culture, rather than the heroic skills of single individuals.

> *The dev team has to be empowered by management to refuse to ship a change if it is insecure, or to drop everything to fix a vulnerability on production. If there are no strongly established cultural norms that security is important, it will get left by the wayside in favour of feature development.

— *[*Kendrick Curtis*](https://www.linkedin.com/in/kendrickcurtis/)*, Engineering Manager Lead*

To be honest this is true for most software qualities, but *especially *for security. In fact, security is a complex topic that requires specialized knowledge, and is unreasonable to expect all engineers to become experts in that. All engineers, though, will write code — so what ultimately enforces security is process.

To achieve this, there are three main areas you should invest in:

#### 1) **Hire a security leader early on**

A security leader is an expert that can spearhead security efforts throughout the engineering org. They can:

- Embed security into the development process

- Design the right amount of training

- Act as a point of reference for any security concern

About when to hire for this role, your mileage may vary based on your risk tolerance and how skilled in security your early engineers are, but a good number is within your first 30-50 employees.

#### 2) Train employees in security

This article specifically focuses on secure *development*, rather than security in general, but all employees arguably benefit from security training.

Pagerduty has some great [*open-source *](https://sudo.pagerduty.com/)[courses](https://sudo.pagerduty.com/) you can use to get started. You will find both high-level ones, aimed to everyone, and specific engineering ones.

When it comes to developers, aside from the basics, you don’t need all of them to become experts. Based on your needs, and the attitude of people on your team, here are two options you can implement:

- **Create a security champion program **— designed for those who have a special interest for security. They may exercise this function alongside their other duties.

- **Include security in your career framework** — if your senior engineers have to deal regularly with security concerns, it is a good idea to make this *official* by writing down such skills and expectations in your career framework. You may design more in-depth training to help engineers match them.

[Ben Chiverton](https://www.linkedin.com/in/benjamin-chiverton/), Director of Engineering, weighs in on this 👇

> *[security as a competency in career frameworks] helps emphasise that security is just as important as delivery. At the end of the day, if there is a culture of delivery over security then I don't have to tell you what will be dropped when there is a tight deadline! Org structure helps too here, make sure you have very senior security officers.*

#### 3) **Embed security into the dev process**

The only way to create secure code is to embed security into every step of the dev lifecycle.

Many teams only take care of it during the initial design and with a final review, implementing the infamous [*security sandwich*](https://www.thoughtworks.com/radar/techniques/security-sandwich)*. *The *sandwich *fails for two main reasons:

- Specs often change during development, which leads to inconsistent or incomplete reviews.

- It casts *security* and *development* as two adversarial categories — which leads to conflict.

Instead, just like DevOps makes infra work well with regular development, the same can happen with security.

Let’s see that a secure dev process looks like 👇

### 💻 Secure Development Process

Let’s organize the development process into five main stages:

1. 📋 **Requirements**

1. ✏️ **Design**

1. ⌨️ **Coding**

1. 🔍 **Testing**

1. 🔄 **Maintenance**

Let’s see how you can embed security in each of them. 

For each step I will list the practices you can adopt to embed security properly. I will also separate between two levels:

- **Basic** — essential stuff any team should do.

- **Advanced **— practices that you may or may not adopt based on your product, size, or maturity.

### 📋 Requirements

Security concerns start with product requirements. PMs and designers need to be aware of how information flows and what can or cannot happen.

This ranges from the basics — e.g. on profile pages, you should only display information that is *public* — to more subtle stuff — e.g. people can’t *edit* a stored credit card number because you would need to store it in plain.

Again, your mileage may vary on this: your PMs may grasp this based on their experience, or you may feel the need to [train them](https://sudo.pagerduty.com/).

### ✏️ Design

From a tech design standpoint, here are some techniques you can use:

#### [Basic] Use a design doc

I wrote a [full article](https://refactoring.fm/p/design-docs) about the benefits of design docs, which includes my own template. The template includes a section about security requirements.

If you are unsure about what to put there, in my experience, functional requirements are usually about that *should *happen, while security requirements are about what *shouldn’t.*

A simple example:

- **Functional requirements:** the page should retrieve the username, email, and phone from the table X in the database and display it on screen.

- **Security requirement:** we must verify that the user has a valid *session token* before retrieving information from the database. If absent, the user should be redirected to the login page.

This is also where, when in doubt, you should escalate to a security leader in your company to help with that.

For larger designs, a key part of the design doc is its *threat model *👇

#### [Advanced] Do threat modeling 

A *threat model *is the description of an application and its environment through security glasses.

So, threat modeling is a family of activities you pursue to identify threats, vulnerabilities, and design countermeasures to prevent or mitigate such threats.

You can check the dedicated [OWASP page](https://owasp.org/www-community/Threat_Modeling_Process) for more details about how to perform it, complete with practical examples.

![Example of a threat three with a threat, vulnerabilities, and countermeasures ](../assets/f7fc44908d324425.png)

### ⌨️ Coding + Testing

This is where you should make sure the code is well-written from a security perspective.

Here are tactics you may use:

#### [Basic] Use a checklist

Write down a list of the most common security advice you may need while coding. This is useful in many ways:

- While you write code

- To perform code reviews

- To train junior devs on the basics

Examples of items that may go into the checklist are:

- *Keep secrets away from code*

- *Encrypt data in transit and at rest*

- *Don’t do cryptography yourself*

- *Validate user inputs before processing data contained in them*

- *Sanitize any data that is sent back to the user from the database*

- *Check open source libraries for vulnerabilities before using them*

#### [Basic] Use a Linter

Linters can intercept basic issues while you are writing code. All popular linters, like ESLint, have security plugins you can use to find stuff like unsanitized assignments, dubious regular expressions, or XSS problems.

You may even connect external tools to you linter, like [Sonar](https://github.com/SonarSource/eslint-plugin-sonarjs?ref=fun4code), to perform lightweight SAST while you are coding.

#### [Basic] Run SAST (Static Application Security Testing)

Static security testing is about intercepting insecure programming patterns. SAST tools analyze your source code and scan for vulnerabilities automatically.

You should run these tests in your CI/CD pipeline, as a mandatory step.

The most popular SAST tools, in my circle, are: [**Snyk**](https://snyk.io/), [**Sonarqube**](https://www.sonarsource.com/products/sonarqube/), and [**Bridgecrew**](https://bridgecrew.io/).

#### [Basic] Run SCA (Software Composition Analysis)

If SAST is for double-checking against vulnerabilities in your own code, SCA is for doing the same on all your dependencies.

This is supremely important when you think that 99% of the code that runs on servers is open-source. For each line of code that we write, we take 99 others from external libraries.

SCA testing can be done before you decide to use a library, but most importantly in CI/CD to find outdated / vulnerable versions of dependencies, before you release.

[Ashwin Chandrasekaran](https://www.linkedin.com/in/meetashwin/), Head of Enterprise Engineering on this👇

> *We do this on the deliverables after they are built, by targeting the repos or images. Goal is to ensure there are no lurking vulnerabilities, especially from dependencies and third-party libraries, that may find their way to production.*

[Dependabot](https://docs.github.com/en/code-security/dependabot) is probably the most popular tool to do this, because you can use it natively into Github — as it was acquired by them in 2019. Also consider that most SAST tools *also *do SCA, so you can find plenty of comparisons online. E.g. [Dependabot vs Snyk scanning](https://janaka.dev/devsecops-aking-snyk-github-dependabot-test-drive/).

#### [Advanced] Use DAST tools — Dynamic Application Security Testing

Dynamic application security testing (DAST) is basically end-to-end testing for security. It is a form of *black-box testing, *in that it checks your application from the outside, only relying on inputs and outputs, and is agnostic of programming languages and technical implementations.

DAST complements nicely SAST and SCA, and is able to scan for problems that sit outside of the others’ scope — and viceversa. However, it also requires more work:

- **It** **is laborious to automate** — it *can* be applied to your CI/CD pipeline, but it sits in the *far right*, as it requires the application to be running. Many teams run DAST manually.

- **It requires you to implement and maintain tests **— as opposed to SAST and SCA, that happen quite automatically.

- **It is slow **— end-to-end testing usually have long execution times, which slows down your pipeline.

Some of the most recommended DAST tools include: [**Brightsec**](https://brightsec.com/),** **[**Probely**](https://probely.com/), [**Stackhawk**](https://www.stackhawk.com/), and [**Deep Factor**](https://www.deepfactor.io/).

### 🔄 Maintenance

After your code is in production, here are other practices you should consider:

#### [Basic] Implement good observability 

Modern observability tools can help detect breaches and various kinds of attacks. Handling these inside the same monitoring tools engineers use regularly is an added value.

[**Datadog**](https://www.datadoghq.com/solutions/security-analytics/)** **is the most recommended tool for this by the engineers I know.

#### [Advanced] Run periodic security sprints

If you struggle to find time to address regressions and security issues, consider running periodic sprints dedicated to security. You can use them to fix problems in your backlog, or to go through controls in a security standard. 

[Ari Koponen](https://www.linkedin.com/in/apkoponen/?originalSubdomain=fi), Head of Platform at Swarmia, does just that with his team 👇

> *We do them twice a year by going through all the controls in *[***OWASP ASVS***](https://owasp.org/www-project-application-security-verification-standard/)*. Everyone in the team participates and takes a few chapters from the list. It's a great way to practice security thinking.*

#### [Advanced] Run periodic pen-testing

No system is bulletproof. Also, by testing and securing your own code yourself, you may fall victim of your own biases.

To counter this, you can run periodic penetration tests, executed by independent entities.

Nicola Ballotta, Director of Cloud at Namecheap, commented on this 👇

> *We run periodic pen-tests without making the teams aware of it. As for the companies, I can't disclose much. In my opinion, the important thing is to have turnover and not always use the same testers.*

In my circles, [**HackerOne**](https://www.hackerone.com/) is well regarded for this.

### 📚 Resources

And that’s it! Here are other resources to learn more:

- 📑 [**Securing the SDLC**](https://owasp.org/www-pdf-archive/Jim_Manico_(Hamburg)_-_Securiing_the_SDLC.pdf) — Great presentation by [Jim Manico](https://twitter.com/manicode) about addressing security throughout the whole development lifecycle.

- 📑 [**Startup Security Checklist**](https://www.security4startups.com/controls-checklist/) — There are plenty of security checklists out there, and you should ultimately build your own based on your specific need. However, this is a great starting point, which also segments by your company stage, and recommends plenty of good tools.

- 📑 [**Threat Modeling**](https://owasp.org/www-community/Threat_Modeling_Process) — This is *the* practice you should adopt to level up your security game, and the OWASP page about it is very well made, with plenty of diagrams and examples.

- 📑 [**PagerDuty Security Training**](https://sudo.pagerduty.com/)** **— The best security training I have found, for both engineers and non-technical folks. It balances thoroughness and accessibility, and is also open source.

### 🔨 Tools

Finally, a round up of the tools I have mentioned throughout the article:

- **SAST:** [Snyk](https://snyk.io/), [Sonarqube](https://www.sonarsource.com/products/sonarqube/), [Bridgecrew](https://bridgecrew.io/)

- **SCA: **[Dependabot](https://docs.github.com/en/code-security/dependabot) or almost any other SAST tool

- **DAST:** [Brightsec](https://brightsec.com/), [Probely](https://probely.com/), [Stackhawk](https://www.stackhawk.com/)

- **Observability:** [Datadog](https://www.datadoghq.com/solutions/security-analytics/)

- **Security controls:** [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/)

- **Penetration Testing:** [HackerOne](https://www.hackerone.com/)
