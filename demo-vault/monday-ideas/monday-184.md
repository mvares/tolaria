---
aliases:
  - "Monday #184"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-monday-idea|Publish Monday Idea]]"
Status: Published
"👓 Status": Not started
"Created time": "2025-11-27T15:14:00.000Z"
Date: 2025-12-01
"Has Notes":
  - "[[evergreen/developing-engineers-in-the-age-of-ai-meri-williams|Developing engineers in the age of AI (Meri Williams)]]"
  - "[[evergreen/make-interviews-resemble-actual-work|Make interviews resemble actual work]]"
  - "[[evergreen/minimum-viable-testing-process|Minimum Viable Testing Process]]"
Tags:
  - Monday
  - Free
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 2b8bdf02-815c-80f7-8207-db5c7bed0f09
---

# Monday #184

### 1) 🔍 Minimum Viable Testing

Testing is an evergreen ~~pain in th~~ struggle, and one of the most requested topics on Refactoring.

The most recurring question is not “*how do you test things thoroughly=*”, but rather along the lines of “*how do you get the most out of testing with the minimal effort?*” — aka what does a minimum viable testing process look like?

This is my simple cheatsheet:

- 🔒 **Use a statically typed language** — most languages today have statically typed versions (e.g. Typescript, Sorbet). This is a no-brainer for 99% of teams — static typing catches bugs early and documents code through types and annotations. It’s also good for AI, like most of this list.

- 🧪 **Write unit tests when relevant** — unit tests are important, but don't obsess over coverage. Write them for non-trivial code or areas subject to future changes.

- 🔗 **Write plenty of integration tests** — integration tests cover execution paths involving multiple components. Identify the most important ones by thinking about *business* paths based on how your product is used. API endpoints are also good candidates.

- 🎯 **Write a few, critical end-to-end tests** — end-to-end tests are expensive to maintain. Invest in testing parts you'd otherwise check manually — the goal is to remove manual checks so you can release faster.

- 🚀 [**Avoid staging**](https://refactoring.fm/p/do-you-need-staging)** if you can** — you can probably skip staging by combining gradual rollouts with [*feature flags*](https://refactoring.fm/p/feature-flags), live PR previews, and video walkthroughs. Fewer steps to production means faster releases and better feedback loops.

![image](../assets/2b8bdf02815c80bd.png)

My TL;DR is that integration tests are usually the most valuable tests, or, better, those with the highest ROI. Unit tests and E2E tests are both useful but need more thinking into *when* they are actually a net positive vs when they are going to drag the team down.

I know this is not the *consensus*, especially around unit tests, and I wrote more thoughts here 👇

[https://refactoring.fm/p/how-to-test-software-in-2023](https://refactoring.fm/p/how-to-test-software-in-2023)

---

### 2) 📞 Make interviews resemble actual work

There is a lot of buzz these days about how to design engineering interviews: which techniques are becoming obsolete with AI, which are becoming more important, and so on.

It’s always hard to give prescriptive advice because that depends on your specific setting, team, role you are hiring for, and so on. There is, however, a *north star* principle that is always valid: **make interviews resemble actual work as much as possible**.

This means:

- 🎨 **Topics** — pick problems that are as similar to yours as possible.

- 🤝 **Setting** — test for good collaboration other (rather) than solo output.

This seems obvious, but many interview processes *fail* at doing good selection because they test candidates

1. for problems who look *nothing* like what they will do at work — e.g. strong algorithmic challenges — and

1. in contexts that have zero resemblance to how the team works — e.g. live *solo* coding with a hiring manager peeking over your shoulder.

> *Match the interview with the daily life of the team. You do CQS? Component test? Pair-programming? Slice big task into small one? Most of time you work alone? […]*

After you have designed your interview process, I am also a fan of informing the candidate *in advance* about how it works. Possibly in the job description already.

This is such an underrated power move: sharing the process creates more alignment and commitment upfront, and allows candidates to *prepare* for interviews in a way that makes sense for what you will test for.

For example, Notion has an [incredible section](/50e339f3fa8a4c8a8a4c1cd7a7565110) that helps candidates prepare for interviews. They have *guides* for literally all the positions — insane!

We wrote a full guide on how to interview engineers in 2025 earlier this year 👇

[https://refactoring.fm/p/how-to-interview-engineers](https://refactoring.fm/p/how-to-interview-engineers)

---

### 3) 🎙️ How to grow engineers in the age of AI

In August [I interviewed Meri Williams](https://refactoring.fm/p/diversity-ai-and-junior-engineers), CTO at Pleo, and we discussed a big concern of mine: how AI is changing the junior engineer experience and what we need to do about it.

Meri argues that, up until today, engineers had a perfect learning progression: write small pieces of code, gradually take on bigger tasks, and slowly build expertise. AI disrupts this natural flow:

> ***"A lot of entry level engineers don't review much code. They're not yet trusted to do PR reviews... But with AI, they're reviewing code all the time."***

Junior engineers now spend more time reviewing AI-generated code than writing it themselves — but they lack the experience to spot issues, security vulnerabilities, or architectural problems.

Something needs to change, and we need to work *intentionally* on it. Meri’s best guesses are the following:

- 🔍 **Earlier code review training** — teach juniors to spot problems they've never encountered.

- 🏗️ **Focus on foundational skills** — security, performance, scalability, maintainability.

- 👥 **Double down on mentorship** — pair programming and design sessions become crucial.

And mind you, many junior engineers are using AI brilliantly — they talk to ChatGPT about problem structure before coding, use Claude to think through architecture, and treat AI as an "endlessly patient mentor”, so it’s often a matter of **channelling this energy** in the right direction, in a way that supercharges their professional growth, not only their output.

Here is the full interview with Meri:

[https://youtu.be/MfXaVKC9odg](https://youtu.be/MfXaVKC9odg)

You can also find it on 🎧 [**Spotify**](https://open.spotify.com/episode/3jjGFT3OhKHy3Sas7ELqQr?si=96d0a0607a8c4f0f) and 📬 [**Substack**](https://refactoring.fm/p/diversity-ai-and-junior-engineers)
