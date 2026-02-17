---
aliases:
  - "What is Code Quality?"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-essays|Publish Essays →]]"
Status: Evergreened
URL: "https://refactoring.fm/p/what-is-code-quality"
"👓 Status": Discarded
"Created time": "2024-04-18T14:53:00.000Z"
Date: 2022-10-20
"Has Notes":
  - "[[evergreen/quality-is-systemic|Quality is systemic]]"
  - "[[essay/what-is-code-quality|What is code quality?]]"
  - "[[evergreen/commenting-code-is-good|Commenting code is good]]"
  - "[[evergreen/code-readability-quote-by-fowler|Code readability quote by Fowler]]"
Tags:
  - Free
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 1a3ebc7a-d9eb-4e7f-8acc-4f193e7be537
---

# What is Code Quality?

### 📑 Materials

---

[https://blog.mocoso.co.uk/talks/2020/02/27/take-control-of-code-quality/](https://blog.mocoso.co.uk/talks/2020/02/27/take-control-of-code-quality/)

- [Codacy Draft](https://docs.google.com/document/d/1A8BmARwBGgk7Lz_bZI89NiglmHCcbcsykaSfPj_Vd4s/edit#)

### 💡 Ideas

---

<details><summary>[Joel Chippindale](https://twitter.com/joelchippindale) – **High quality code is easy to keep changing**</summary></details>

- Tech debt ideas (boy scout rule, maintenance)

<details><summary>[Chris](https://twitter.com/christopheek) – readability, maintainability, security, execution, scalability</summary></details>

<details><summary>[Nikita Logachev](https://www.linkedin.com/in/nikita-logachev/?originalSubdomain=cz) — gets out of your way</summary></details>

- Code that helps with your development pace

### ✍️ Post

---

*Hey 👋 this is Luca! Welcome to a ✨ ****free bonus edition**** ✨ of Refactoring.*

*This is a guest post written with *[*Catarina Gralha*](https://www.linkedin.com/in/catarinagralha/?originalSubdomain=pt)*, researcher and writer at *[*Codacy*](https://www.codacy.com/)*, where she explores the practices that help teams create high quality software.*

*This edition is part of the *[*Refactoring partner program*](https://refactoringhq.notion.site/Refactoring-Partner-Program-79e60e65a2424545a65c2e4a5b9aae07)*, which gives selected tech leaders the opportunity to write great pieces about engineering culture on Refactoring, while also giving Refactoring subscribers visibility into the products they are building.*

*I love Codacy personally and I am thrilled to host one of their pieces today.*

Learn more about Codacy

---

Code quality is one of the most discussed topics in engineering, yet stays one of the most elusive.

Intuitively, it impacts your team’s ability to **ship fast** and often, while having an indirect impact on the **customer experience**. But how?

At Codacy we work with more than 250,000 developers, so we have a privileged window into their coding habits. By surveying many of them over the past year, two metrics stand out:

- 66% of developers are not satisfied with their current code quality.

- On average, 45% of development time is spent on maintenance.

How did we get here? And how can we do better?

This article covers everything we learned about code quality in over 10 years working on tools that help exactly with that.

We will talk about:

- 🚗 **What code quality is and why it matters** — a car metaphor.

- 🥇 **Habits of top performing teams** — to keep code quality high.

- 🔄 **Quality is systemic **— creating a system designed to produce quality.

- 🔨 **Using a tool for quality **— how tools can support your process. 

- 📚 **Books and resources **— by our favorite authors.

Let’s go!

---

### 🚗 What is code quality

We talk of *code *quality rather than *product* quality to address values that are often invisible to the final user. So we often say ***under the hood*** — which is a *car *metaphor.

In our context, the car is the full product. Like digital products, a car has a UI/UX, which is how the driver (user) interacts with it — how the car makes them feel.

Then, if we stay with the *under the hood *metaphor, software is the car engine. What makes an engine high quality?

- **Some things are universally important** — like reliability and little need for maintenance.

- **Other things largely depend on the car** — sports cars might be concerned about performance, while city cars care more about consumption.

This still translates well to software. We won’t find a single definition that works for everybody, as some qualities depend on the product, but we can focus on those that are universally desirable.

There is also one area where the car metaphor breaks: **software evolves** — which doesn’t really apply to cars. Evolution gives maintainability a whole another dimension: it’s not just about **repairing defects**, it is about being able to change the code to support what the future brings.

Research shows that there is high correlation between [businesses that ship fast and often](https://refactoring.fm/p/the-four-measures-of-software-delivery), and those that are ultimately successful. So, high quality code has to be that that is **easy to change**.

[Joel Chippindale](https://twitter.com/joelchippindale), CTO and executive coach, weighed in on this in the community 👇

> *This is the definition of high quality code that I have found most useful in my teams because this is what really matters to you as a development team.

Code that is easy to keep changing is code that is enjoyable to work on. It helps us feel smarter and enables us to do more valuable work for the organisations we work for. Everyone wins and that’s why it’s such a valuable lens to look at code quality through.*

What makes code easy to change and enjoyable to work on? Let’s review the most popular traits we found in top performing teams 👇

### 👓 Readability

Code that is readable can picked up easily by anyone in the team, independently of who wrote it in the first place, and even a long time after it was written. 

This makes a lot of difference with maintainability. In healthy teams, readability is the result of many practices, like:

- **Good separation of responsibilities** — to keep code *simple.*

- **Meaningful folder structures** — to make code *discoverable.*

- **Good naming conventions** — to make code *understandable.*

As Martin Fowler says:

> *Any fool can write code that a computer can understand. Good programmers write code that humans can understand.*

Readability is also helped by including good comments 👇

### ✏️ Writing good comments

Commenting code is a somewhat controversial practice, as many developers believe that *good code documents itself*.

We found, instead, that top performing teams are consistently good at commenting code, by focusing on the right amount of comments that provide the most value to the codebase.

Here is more about common types of comments:

- ✅ **Comments at the top of the file/class** — a few lines to describe the file’s primary goal can go a long way to help maintainers. It also helps to avoid scope creep over time and to keep the file true to its original goal.

- ✅ **Comments on complex functions** — most functions should be simple enough to be understandable *as-it-is*, but there are algorithms and processes that cannot be so, no matter how well you write them. In these cases, it helps to include a description of the inputs, the logic, and the outputs of the function.

- ❌ **In-line comments** — while there is value in explaining the workings of a complex function, the need to comment single lines of code is most often a code smell. If people understand what the function does but not some of its lines, there is probably something you can rework, rather than commenting the lines themselves.

Code comments are also easier to keep up to date with respect to docs that live elsewhere, as you may update them in place whenever you are making changes to the code itself.

Likewise, it is easy to spot in PRs whenever somebody is changing the code without updating the comments, and report it.

### 🔍 Testing

Good automated testing boosts your confidence in making changes, which in turn makes you go faster. And by catching bugs earlier, it also reduces the time you spend on maintenance.

This all contributes to keeping the quality of your codebase high.

Finally, we find that the importance of good coverage is real. Getting good coverage doesn’t necessarily mean writing an insane amount of tests. Integration tests can easily cover large parts of your codebase by addressing a few, crucial use cases.

One of our clients recently reported:

> W*e hit 70% code coverage across those pieces [of code], and we’ve reduced our tech support time by about 60%*

How amazing is that?

### 🤝 Code reviews + static analysis

It is no secret that code reviews make code quality higher and help share knowledge across the team.

We find that the best teams combine **manual reviews** with the work of **static analysis tools**, automatically scanning new code against a set of best practices to suggest areas for improvement.

Such tools can greatly improve your review process. They make the reviewer’s job easier by doing some real heavy lifting, like catching bugs, code smells, vulnerabilities, and taking care of style and formatting conventions.

### 🦠 Low Technical Debt

[Technical debt](https://refactoring.fm/p/technical-debt) can slow down the pace of development considerably.

We find that great teams are hyper-aware of the state of their debt and are intentional on addressing it. They continuously track debt items, prioritize them against product initiatives, or create dedicate swim lanes for working on them.

They also have strong communication in place with stakeholders. They can advocate for significant refactoring initiatives and tackle them when the ROI is right.

### Quality is systemic

Most of all, we find that good software quality is more the result of **good systems** and processes than the result of individual performance.

A team of average developers working in a system designed to produce quality will eventually produce better results than a group of amazing developers working with processes that are not designed for that.

### 🔨 Using a code quality tool

At [Codacy](https://www.codacy.com/), we help thousands of developers ship billions of lines of code daily by automating and standardizing code reviews.

We’ve built a suite of products that helps developers act on their software quality, engineering performance, and security:

#### [**Quality**](https://www.codacy.com/product)

We started with software quality, by building the best-in-class solution for static code analysis. 

By integrating seamlessly into your workflow, [Quality](https://www.codacy.com/product) helps engineering teams save time in code reviews and tackle technical debt. 

Users receive notifications on security issues, code coverage, code duplication, and code complexity in every commit and pull request, along with advanced code metrics on the health of a project and team performance. Codacy supports 40 coding languages and is available in free open-source and enterprise versions (cloud and self-hosted).

#### [**Pulse**](https://www.pulse.codacy.com/)

Recently, we introduced Pulse to help companies achieve elite engineering performance through data-driven insights. 

Pulse lets you assess the health of your engineering culture so you can be focused on your business goals, like measuring DORA metrics and get guidance on the best DevOps practices you should adopt based on your current stage.

### 📚 Books about Quality

If you want to dive deeper into code quality, here are our favorite books about it 👇

- 📕 **Clean Architecture** — by Robert Martin

- 📗 **Clean Code** — by Robert Martin

- 📙 **The Pragmatic Programmer** — by David Thomas and Andrew Hunt

- 📘 **Refactoring** — by Martin Fowler
