---
aliases:
  - "How do Engineering Teams use AI?"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-solo-videos|Publish Solo Videos]]"
Status: Published
URL: "https://youtu.be/NaprqljOV-A"
"👓 Status": Not started
"Created time": "2025-03-13T08:58:00.000Z"
Date: 2025-03-28
"🎙️ Status": Not started
"Is A":
  - Video
notion_id: 1b5bdf02-815c-8058-9de0-ca8e9bea86ea
---

# How do Engineering Teams use AI?

### 📑 Materials

---

- [Jevon’s paradox](https://en.wikipedia.org/wiki/Jevons_paradox)

### ✍️ Post

---

Hey, Luca here! Today we are talking about how real engineering teams are using AI for coding. We will cover four things:

1. **💼 Many companies are hiring *****more***** engineers** — especially *good* companies.

1. **🏢 How AI works with large codebases** — which remains the #1 frontier challenge.

1. **🤖 Robots vs Iron Men **— the philosophical divide with AI tools.

1. **☀️ How the best teams are coding with AI **— and how they optimize for developer happiness, by giving AI the all bad stuff, and keeping the good stuff human.

So let’s dive in!

---

If you are new here, my name is Luca, I am a startup founder and CTO turned content creator. I run a newsletter for 150K engineers and managers, which you can find at refactoring.fm, and of course I run this youtube channel.

---

Over the past few months there has been an explosion of AI tools for coding. 

I have an ever-growing list of things to try — [Lovable](http://lovable.dev/), [Windsurf](https://codeium.com/windsurf), [Bolt](https://bolt.new/), [v0](https://v0.dev/), and more — the FOMO is real and I am not immune.

So, as models become more capable, the future of software engineering looks completely tied to AI. Yet, there is a growing *divide* that I find hard to explain:

- On one side, people are building incredible things just by… *vibe-coding — *see @levelsio with his [latest flight sim](https://x.com/levelsio/status/1894429987006288259).

- On the other side, real engineering teams I speak with are… meh — they report decent but not extraordinary gains.

Why is that? I believe it’s because of two reasons:

- 🛣️ **Green-field vs big codebases** — most tools out there are optimized for green-field development. And so are most of the examples you can find. Real teams with big, seasoned codebases can’t do much with e.g. Lovable.

- 🕹️ **Single-player vs multi-player** — AI workflows are still largely single-player, and they kind of break when working in a team. Harper Reed also reported it in this [awesome article](https://harper.blog/2025/02/16/my-llm-codegen-workflow-atm/) 👇

> *My main complaint about these workflows is that […] the interfaces are all single player mode.*

Now, the *team *angle is the most interesting to me, and that’s what we are diving into this week.

So let’s start with some market pulse — how has AI changed the job market so far? And the surprising reality is that:

---

### **💼 Good companies are hiring *****more***** engineers**

How is that possible? The reason is that in most markets the demand for software is *elastic*, that is, if the price per unit of output drops, the demand grows by at least the same amount.

So you can visualize this in a simple thought experiment: if your team could magically produce 3x the amount of software as today, how would you use this power? Would you reduce your team, or would you keep it as is to grow faster? For companies that are profitable and/or hungry for growth, the right answer is obviously the latter.

Last week I spoke with the folks at Augment, who work with thousands of engineering teams, and they report that many are [hiring ](https://www.augmentcode.com/blog/2025-ai-predictions#:~:text=3.%20Coding%20AIs%20increase%20demand%20for%20software%20engineers)[*more*](https://www.augmentcode.com/blog/2025-ai-predictions#:~:text=3.%20Coding%20AIs%20increase%20demand%20for%20software%20engineers)[ engineers because of AI](https://www.augmentcode.com/blog/2025-ai-predictions#:~:text=3.%20Coding%20AIs%20increase%20demand%20for%20software%20engineers). This is the famous **Jevon’s paradox**: in some areas the demand for software is *highly* *elastic*, which means it grows more than linearly in response to price decrease.

So I believe the response to AI will depend on the type of org you are in:

- **📈 Top teams** — that make the most out of engineers, where teams ship fast, often, and with little overhead, will hire *more* engineers because of AI productivity.

- 📊 **Average teams** — where engineers create value, but are constrained by bureaucracy and the cost of coordination, will simply stay put.

- 📉 **Poor teams** — where tech is a commodity and value is capped, will shrink in size to optimize costs.

So this is the future, but where are we today? And what do we need to make this happen?

---

### 🏢 The #1 frontier challenge is large codebases

Today’s models are *already* performing like top software engineers in pure algorithmic problems. Already last October, Claude 3.5 was able to autonomously [solve 86% of a random set of LeetCode problems](https://www.thinkevolveconsulting.com/can-claude-cheat-coding-interview/), from all ranges of difficulty. 

However, faced with real freelancing tasks, this percentage drops to 26%. Check out this [OpenAI benchmark](https://openai.com/index/swe-lancer/) from just three weeks ago.

This different is all about **context**. As a senior software engineer from OpenAI noted:

> *"AI can generate code snippets well, but when it comes to fitting them into an existing project, it often fails due to a ****lack of context****."*

![image](../assets/1b5bdf02815c81c7.png)

Also, these benchmarks are about the *previous* generation of LLMs. The recent releases of Sonnet 3.7 and GPT 4.5 will surely move the *intelligence* bar higher, making context an even more obvious bottleneck.

So, when it comes to coding, how is context passed to AI? There are three possible ways: **fine-tuning**, **context window**, **RAG**

Out of these, only RAG is showing promise. Fine-tuning is unpredictable, slow, and extremely costly; while adding code to the context window doesn’t work at scale and doesn’t seem to guarantee precision.

![image](../assets/1b5bdf02815c8152.webp)

So, good RAG is the best candidate to scale AI coding tools, but RAG architectures are not a commodity: we are still in the early days of learning how to build them well, for different types of content (code is completely different from e.g. literature), and different use cases. So we’ll see.

Now, let’s say models are smart enough and context is somehow solved — how are human engineers going to work with AI? 👇

---

### 🤖 Robot vs Iron Man

With the current generation of tools, we are witnessing a big divide that is just as practical as it is philosophical.

It’s about *autonomous* tools vs *augmentation *tools, or, of you prefer, **Robots vs Iron Men**:

- 🤖 **Autonomous tools** — are tools that behave like independent *agents*, whose goal is to approximate a *coworker*. Think about [Devin](https://devin.ai/) or [Lindy](https://lindy.ai/).

- 🦸 **Augmentation tools **— are tools that give humans *superpowers*, but where ownership of work is still ultimately human. In software it’s tools like [Augment](https://www.augmentcode.com/) or [Cursor](https://cursor.sh/).

What does it change, on a practical level? Actually, quite a lot.

Autonomous tools *own* work: you may ask them things on Slack and they submit PRs by themselves. Augmentation tools, instead, are aids to humans. You interact with them (e.g.) in your IDE, and the PR is submitted by the human author.

What is the right strategy?

This is not a black-or-white call, as I expect the two to blend over time, but there are fundamental differences nonetheless:

- 🔄 **Feedback loop **— augmentation tools have a tighter human feedback loop, because the batches of autonomous work are smaller. Until we are *really* in the end game of AI engineers, letting AI run autonomously and submit PRs is probably not the most effective way to work with it. You want to intercept errors earlier and iterate faster. 

- 📈 **Scaling **— while augmenting humans doesn’t pose further organizational challenges, using autonomous agents does. How do you orchestrate work? Do you focus individual agents on specific tasks? Will you need to employ… [*manager agents*](https://devin.ai/pricing)* *to oversee a team of IC agents?

- 💪 **Empowerment **— finally, there is a very human angle: I believe in tools that empower humans, as opposed to replacing them. While we are still far from this in either case, but I believe it’s important to point the ship in the right direction and provide the right vision from the start.

In short, I root for AI to help us create the Avengers, rather than the Clone Wars.

So, if the goal is to empower humans — how do you do that? And how are successful teams doing it already? 👇

---

### ☀️ Optimize for human happiness

The #1 rule for creating good AI workflows is not to maximize developer productivity — is to maximize **developer happiness**.

That is, to use AI to reduce *toil*, instead of increasing it. 

This is non-obvious: many workflows you can find online corner humans into mostly fixing AI’s bugs. This is never going to work, because if all that people are left to do is crap, they are going to hate their work and quit.

So the question is the opposite: **what toil can we give AI**? And there are some solid emerging answers here!

#### 1) Testing 🔍

In a surprising turn of events, TDD is having a silent renaissance, thanks to AI.

If you ask me, TDD has always been an obvious good workflow, only hard to put in practice because people 1) hate to write extensive tests, and 2) hate to think too much beforehand. So, for many developers and many teams that already have their own share of troubles, that’s too much *cognitive load *to ask for.

AI is changing all of this, by addressing these issues at their core:

1. AI is very good at writing tests, removing all the *boilerplating* load from humans.

1. AI hugely rewards* *those who think more beforehand. Teams that are getting the best results are those that create [good specs and plans](https://harper.blog/2025/02/16/my-llm-codegen-workflow-atm/) and let AI implement them.

At this point, TDD becomes trivial: if 1) you need to write good specs anyway and 2) testing becomes (almost) free, you might just as well have AI create a testing plan first.

So, add that to the AGI conversation. If AI finally convinces us to write tests, it might really be smarter than us.

#### 2) Documentation 📑

The second domain where AI is changing everything is documentation. 

For many developers, writing docs is the ultimate evil, possibly more despised than testing or fixing bugs. Good docs are hard to write, hard to organize, and hard to maintain.

So, just like with testing, AI is *attacking* this problem from all angles:

1. AI writes (and maintains) high-quality docs effortlessly, from inline comments to full design docs.

1. AI is able to fetch docs from pretty much wherever they are, reducing the need for perfect organization.

1. To add insult to injury, AI is able to explain code well even *without* docs.

This final quality is dangerous, because it can make people think we don’t need docs anymore. We do, because AI can look at some code and explain what it does, but not *why* it does things that way, nor the context that led to our decisions about it.

So, I expect AI and humans to collaborate on docs in different ways based on the type of information: low-level docs, like code comments and tech specs, may become largely AI-generated, while high-level artifacts like engineering principles, design docs, and [ADRs](https://adr.github.io/) will stay human-driven.

![image](../assets/1b5bdf02815c81ff.png)

*From more AI to more human *👆

#### 3) Quality ✅

Finally, quality! And I know! I hear you saying: “*quality is not toil!*” — well, quality is the result of a thousand things, some of which are kind of toil:

- Does code match your standards / conventions?

- Are there any smells / obvious improvements?

- Are there any security vulnerabilities?

When integrated right, AI is good at spotting many of these, which means 1) you are raising the bar of the software quality you produce, while 2) reducing the cognitive load for your developers. 

It’s still early days for tools that help with all of this, but I am already a fan of [Augment](https://www.augmentcode.com/) itself, plus more targeted ones like [Packmind](https://packmind.com/) and [Codacy](https://www.codacy.com/).

---

### 📊 Tracking AI code is an anti-pattern

Finally, a question that I get asked a lot: should AI-generated code be tracked and monitored, like teams do with e.g. their open source dependencies?

My answer kind of goes back to the *autonomous* vs *augmentation* tools: if AI does some things completely on its own, then of course you need to track how it fares against regular human output.

But as long as AI *augments* human work, then how can you really separate AI code from human code? And also, what’s the point?

So, to evaluate the impact of AI, my suggestion is to focus on [overall productivity and developer safistaction](https://refactoring.fm/p/whats-next-in-measuring-dev-productivity?utm_source=publication-search). Are developers happy with the tools? Do they want to keep using them? Are you able to ship faster?

---

### 📌 Bottom Line

And that’s it for today! Let’s recap what we learned:

1.  📈 **Companies are hiring more engineers, not fewer** — top organizations are experiencing Jevon's paradox: as AI makes development more efficient, they're expanding their engineering teams to create even more software.

1. 🤝 **AI workflows need to become multiplayer** — current AI coding tools are optimized for single developers working on greenfield projects, but real teams need collaborative AI experiences that work across shared codebases.

1. 🏢 **Large codebases remain the frontier challenge** — while AI excels at algorithmic problems, it struggles with real-world tasks in existing codebases due to context limitations.

1. 🦸 **Augmentation beats autonomy** — tools that empower humans create tighter feedback loops and better results than fully autonomous coding agents that try to replace engineers.

1. 😊 **Optimize for developer happiness, not just productivity** — successful teams use AI to reduce toil rather than increase it, focusing on making engineers' work more fulfilling.

1.  🧪 **TDD is having a renaissance** — AI excels at writing tests and rewards teams who create good specs upfront, making test-driven development more feasible and less burdensome.

1. 📝 **Documentation gets an AI makeover** — AI is transforming documentation by writing code comments and technical specs while humans focus on higher-level design documents and architectural decisions.

1. ✅ **Quality becomes less burdensome** — AI helps enforce code standards, identifies smells, and catches security vulnerabilities, raising the quality bar while reducing developers' cognitive load.

1. 📊 **Tracking "AI code" is an anti-pattern** — when AI augments human work rather than replacing it, separating "AI code" from "human code" becomes counterproductive; focus instead on overall productivity and satisfaction.

So, I wish you a great week, and as always, thank you for listening
