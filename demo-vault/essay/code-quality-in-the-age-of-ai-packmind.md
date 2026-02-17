---
aliases:
  - "Code Quality in the Age of AI (Packmind)"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-essays|Publish Essays →]]"
Status: Evergreened
URL: "https://refactoring.fm/p/code-quality-in-the-age-of-ai?utm_source=publication-search"
"👓 Status": Discarded
"Created time": "2024-09-06T07:43:00.000Z"
Date: 2024-11-27
"Has Notes":
  - "[[evergreen/the-lifecycle-of-code-quality|The Lifecycle of Code Quality]]"
  - "[[evergreen/what-makes-code-easy-to-change|What makes code easy to change?]]"
Tags:
  - Guest
  - Software
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: c1a2e2ad-7eb2-4c95-9ae8-7c8f77431863
---

# Code Quality in the Age of AI (Packmind)

[packmind.pdf](https://prod-files-secure.s3.us-west-2.amazonaws.com/631d83ff-20ce-4401-a614-56e2c0f97767/f2206d55-a177-4aa9-8b7d-7864b08c0687/packmind.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664PRWKBBJ%2F20260131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260131T193438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA71n5Nt1WsqnDOJZgjt2yfM8Fbm9vXbyuPxpcbpYaz5AiEAtmEu7SN1aJaCR7rcUjb02Jd6JLngViTZWTvAO9n2iBcqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFdQ6rOrjsiJRrDJECrcA3rgB11x5%2FeiHzmWSLoOhIbnTSDbfF%2FiEB5LjfiR5x8GB%2BNx2egLmKA6sgVlRtEmyrtx3slFtvO28S0967m6zIAO2qK9QnQ4ptHI1rfkqj6SSIRaT0tOCG%2Fwxz8wFQLRhFAJfAl0Se%2FpB6qNGwqKYwC8FbFCnnl5EYpPaKdZFlv48%2F8LVGm3R8TbuCycyoiCCWqrVOPQC0ye1Tql5mOEwZZAX9vwvr9cXpae1MiRZKmMlXFBddJaap8VEsSWlt1paiZXjpcXtyVMZa64o8C5z3LQUzRu1o6lsLPFTbH0z7tUMYYyyr97TbEfp30U7pMu7WfkrFX7VenW5N39SSLY68aCaQE9d1TR34eMhDAEKw5aFWQNbLDStZTruCeSXXGbhgQC%2FIRotSMzzaZO6SCAASdyRpncULk0BZTNGSeaG7%2BZMwlU6PijdFpCYhHSRfpBWsEmGRnQ%2F0v9uyoTispoRp0PN%2FqTWtDa07zNY8ExGBMQveQ%2BkgbmQGIGygpRZuupwHoktnYcds00yn8sfGn83jX9kVzkBOVgGgAaJa1mCsMZ0YKtbfM6vVi7sS%2B6n3XO6R5sjhWAgaHDqqBfG%2Boz0t7hm75aevAcES%2FvhgS4o1ilWrVt%2BP5zHhcQs24kMN%2BM%2BcsGOqUBnYSYQOdnoa3q0dQD8kB891XEj%2BfmXw35Oozcyjpw2tcT9xO6jEypm5vtIQ2sWNGOujpvNJ7eXXn6OB9HMjXnn%2B7k5KGxBPfLp%2Fq5LMNeZKIzPoO70imR1wq26qyBmaSI5HGaRnk%2FZ3N3j2Ug7tK8HyvRLBe%2FcmuUkj%2BLtI5MCZGzB8HTkRwtR5J1UWIBbMuAskdaHyXEbAPfKkYkEi3XzM1OLV31&X-Amz-Signature=b2daa715a7292508ebee6ef364cb317f035245062d4277cde18442c5df490478&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## Outline

---

## Full article

Last month, the 2024 DORA report came out, and as always it was full of interesting insights.

A good part of it explored the impact of AI on engineering teams, and reported a surprising finding:

> *Despite AI’s potential benefits, our research revealed [that] AI adoption may negatively impact software delivery performance. As AI adoption increased, it was accompanied by an estimated ****decrease in delivery throughput by 1.5%****, and an estimated ****reduction in delivery stability by 7.2%****.*

So, in many cases, the productivity gains in pure coding throughput do not translate into general software delivery improvements.

Why is that?

The answer is unclear, and I guess it will take years to figure out all the downstream effects of AI in coding. The key tradeoff, though, is simple: AI allows to create more code, faster, in exchange for it being less under our control.

So, it is easy to see how bad things can happen from this: faster and sloppier coding leading to 1) bigger batches, which equal more risk, and 2) more regressions and maintenance down the line.

This is not inevitable. I am sure the best teams will be able to *constrain* the use of AI under their own good practices, and make it a (huge) net positive — but it will take work.

In particular, I believe it will require a new, intentional approach to code quality.

Quoting Joel Chippindale, our coach-in-residence, *"high quality code is easy to keep changing."* But how do we ensure this when more and more of our code is written by AI?

This is what we are going to explore today. To do this, I am partering with XXX from Packmind. Packmind works at the forefront of this transition, building tools that help enforcing quality through AI. XXX and I put together our respective experiences to create the best guide we are capable of.

So here is the agenda for today:

- 📖 **What makes code easy to change** — we'll explore the fundamental traits of maintainable code, from readability to testing, and why they matter more than ever.

- 🤖 **Coding in the Age of AI** — how AI is changing the way we write and maintain code, and why this makes quality even more crucial.

- 🔄 **The Lifecycle of Quality** — a practical framework for building systems that consistently produce good code, from early practices to final reviews.

- 📈 **Measuring and improving** — concrete ways to track code quality and improve it over time, with examples from successful tech companies.

---

*Disclaimer: I am a fan of Packmind and what XXX is building, and they are also a long-time partner of Refactoring. However, you will only get my unbiased opinion about all the practices and services mentioned here, Packmind included.*

*You can learn more about Packmind below. Also if you mention you are a Refactoring subscriber, they will give you an additional discount *👇

---

### 📖 What makes code easy to change

Before discussing how AI changes things, we need to establish what makes code truly maintainable. After all, you can't improve what you don't understand.

Many people conflate code quality with abstract notions of "cleanliness" or adherence to specific patterns. But there's only one thing that really matters: **how easy it is to change the code**.

This is not just theoretical. When code is hard to change, velocity slows down and engineers spend more time maintaining existing stuff than writing new features.

To me, code that easy to change displays three fundamental traits:

#### **1) Easy to understand 📖**

The first trait of maintainable code is readability. Code that can be easily understood by anyone on the team, regardless of who wrote it or when it was written, is code that can be safely modified.

Here are the key elements that make code easy to understand:

- 🏅 **Clear responsibilities** — each component having a single, well-defined purpose is the foundation of easy understanding. When a file or class tries to do too many things, it becomes harder to grasp and riskier to modify.

- 📁 **Intuitive structure** — your codebase should be organized in a way that makes it easy to find things. This includes: meaningful folder structure that reflects your domain, consistent file naming conventions, clear separation between different layers (e.g., UI, business logic, data access). I wrote more about naming & structure in [this previous piece](https://refactoring.fm/p/how-to-name-things?utm_source=publication-search).

- 💬 **Good comments** — some argue for self-documenting code, but I have found that the best teams consistently write good comments. The key is finding the right balance: I am not a fan of inline comments and overly micro stuff, but I always appreciate comments at the top of files/classes describing their primary goal, or a quick explanation of complex business logic that isn’t immediately obvious from the code. 

#### **2) Small chance of regressions 🎯**

The second trait of maintainable code is **confidence** — how sure are you that your changes won't break something else?

This confidence primarily comes from good testing. This is not just about high coverage, it's about having the right tests that give you the most value:

- **Integration tests** — in my book, these often provide the best ROI, as they can cover large parts of your codebase while being more resilient to refactoring than unit tests.

- **E2E critical testing** — identify the core business flows and harden them first. A bug in your login page is more critical than one in an admin dashboard.

- **Test readability** — good tests also serve as documentation. When a test fails, it should be immediately clear what went wrong and why.

I wrote a lot about 1) [good testing](https://refactoring.fm/p/how-to-test-software-in-2023), and 2) [modern QA](https://refactoring.fm/p/how-to-do-qa-in-2024), if you want to dig more!

#### **3) Good abstractions 🏗️**

The final trait is having abstractions that match your business domain, which to me is the very [definition of low technical debt](https://refactoring.fm/p/the-true-meaning-of-technical-debt?utm_source=publication-search). This is perhaps the hardest to get right, as it requires tech expertise + domain knowledge, for which you need good collaboration between stakeholders.

When abstractions are poor, tech debt sneaks in. The best teams handle this in a variety of ways, which we covered in our [full guide](https://refactoring.fm/p/the-definitive-guide-to-manage-technical?utm_source=publication-search).

The relationship between these three traits is often hierarchical: readable code makes it easier to write good tests, and good tests give you the confidence to improve your abstractions.

However, maintaining these qualities becomes more challenging in the age of AI. When code is increasingly generated by machines, how do we ensure it remains easy to change?

## 🤖 Coding in the age of AI

It is clear by now that the new coding workflow enabled by AI brings in a sneaky tradeoff: **we produce more code, but have less control over it**.

GitHub reported that Copilot helps developers write code ~15% faster, and similar tools showed comparable improvements. How can that *not *translate into overall better delivery?

My guess is three things:

- **Larger changesets** — AI makes it easy to write more code at once. Bigger PRs cause slower + sloppier reviews, and bring in more risk when deployed. More risk equals more bugs and more churn.

- **Non-obvious issues** — if you have played for AI-coding for a while, you should have noticed that AI makes weird mistakes, largely different from what humans make. AI messes up library versions, sometimes hallucinates entire functions, or rewrites a piece of code deleting a previous functionality in the process. These errors are rare, but they take a lot of time to find out because they are different from *our *mistakes.

- **Long-term maintenance** — I suspect the real cost of AI code shows up in maintenance. More code naturally requires more maintenance, and the less we understand some code, the harder the maintenance.

So what’s the way forward? It is early to say, but my bet is to invest in your process for* *quality 👇

## 🔄 The Lifecycle of Quality

Code quality is not about individual performance or heroic efforts. It's about having systems and processes that consistently produce good outcomes.

I believe a team of average developers working within a well-designed system will outperform a group of exceptional developers working in a suboptimal system.

So let's explore the six steps that make up your quality system, and how they reinforce each other 👇

![image](../assets/13dbdf02815c80b1.png)

#### **1) Encoded coding practices 📝**

Everything starts with having clear, documented practices that define what good code looks like for your team. These include: system design principles and patterns, code organization and naming conventions, security and performance guidelines, docs requirements, and more.

Good encoded practices are the foundation of your quality system because they *inform *everything else: they make coaching and pairing easier, they enable laser-focused static analysis, and provide clear guidelines for code reviews. 

They create a shared language that makes all subsequent steps more effective.

#### **2) Coaching & pairing 👥**

Knowledge doesn't spread by osmosis. The best teams actively share it and discuss it through good collaboration.

In my experience, the two most effective forms of collaboration in engineering teams are:

- 👯 **Pairing **— it’s no secret that I am a big fan of pair programming. I [wrote about it](https://refactoring.fm/p/pair-programming-in-2024) plenty of times, and will continue to do so!

- ✏️ **Design discussions** — a good design process, possibly supported by good [design docs](https://refactoring.fm/p/design-docs?utm_source=publication-search), does wonders to your team’s growth. It makes you get to better solutions, coaches younger co-workers, and intercepts issues before it’s too late. When the design is good, pure coding mistakes can’t be *too* bad.

#### **3) Static analysis 🤖**

One of my [predictions about AI](https://refactoring.fm/p/predictions-about-ai) that static analysis is going to be huge. 

What started as simple linting for stylistic errors, is gradually evolving to intercept code smells, security vulnerabilities, optimization opportunities, and more.

This is healthy because the more you can catch with automation, the more code reviews get easier. To the point where I believe good testing + good static analysis will remove a lot of the need for *blocking* reviews, and many teams will be able to switch to a merge first + review later workflow for most changes.

A limitation of most static analysis tools today — which makes me bullish about the work the guys at [Packmind](https://packmind.com/) are doing — is that the set of rules and criteria are fixed. The next step, to me, is AI taking *your own* coding standards and enforcing them in static analysis, like a human reviewer would.

That’s exactly what Packmind is up to, so [check it out](https://packmind.com/) if you want.

#### **4) Automated testing ✅**

We covered this already — a solid test suite makes you *faster* by creating the confidence to change code without fear of breaking things.

I am very opinionated about testing and I don’t believe all tests are good. You should be intentional in what kind of tests to invest in, and for what parts of your codebase, to make sure the ROI is positive. I wrote more about this [here](https://refactoring.fm/p/how-to-test-software-in-2023).

#### **5) Code review 🔍**

Finally, code reviews are your last line of defence. 

When everything else works, reviews should rarely spot crucial issues. Conversely, if they often do, you should ask yourself what other parts of the process are failing: should we discuss design more? do we have enough encoded practices? Is static analysis powerful enough?

Code reviews are literally the *worst* moment (before shipping) in which to spot problems, because they are the last. By *shifting left* and investing in what comes before, you can shrink what goes into reviews considerably, and address many items arguably in better ways.

So, one of the goals of code reviews should be to **continuously reduce their own scope**, by making engineers uncover rules that can be enforced by other parts of the dev process.

So, when done right, they become less about catching basic issues (handled by static analysis) or verifying correctness (covered by tests), and more about sharing knowledge, identifying new patterns, and creating new coding practices.

This way, reviews feed back into the rest of the process, creating a virtuous cycle of continuous improvement.

More thoughts (and hot takes!) about reviews in this [previous article](https://refactoring.fm/p/thoughts-on-code-reviews).

---

## **📌 Bottom line**

So, in an era where AI is reshaping how we write code, maintaining quality becomes at once more challenging and more crucial.

Here are the main takeaways from today:

1. 📖 **Focus on changeability** — high-quality code is fundamentally about being easy to change. Prioritize readability, testability, and good abstractions in your codebase.

1. 🤖 **Understand AI's tradeoffs** — while AI can boost coding speed, it can lead to larger changesets, non-obvious issues, and increased maintenance burden. Be aware of these pitfalls.

1. 🔄 **Implement a quality lifecycle** — create a system that consistently produces good outcomes. This includes encoded practices, coaching, static analysis, automated testing, and effective code reviews.

1. ⬅️ **Shift quality left** — develop the mindset of catching issues as early as possible in the development process. Invest in practices and tools that prevent problems before they reach the code review stage.
