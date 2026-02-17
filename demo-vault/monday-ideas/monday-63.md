---
aliases:
  - "Monday #63"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-monday-idea|Publish Monday Idea]]"
Status: Published
"👓 Status": Not started
"Created time": "2024-04-18T15:09:00.000Z"
Date: 2023-08-07
"Has Notes":
  - "[[evergreen/ai-coding-use-cases|AI coding use cases]]"
  - "[[evergreen/the-three-keys-of-good-delegation|The three keys of good delegation]]"
  - "[[evergreen/handoff-misconception|Handoff misconception]]"
Tags:
  - Monday
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: f15b7975-5409-424b-bacf-d3785f2e997d
---

# Monday #63

*Hey, *[*Luca*](https://twitter.com/lucaronin)* here! Welcome to the ****Monday Ideas ***💡

*Every Monday I will send you an email like this with ****3 short ideas**** about making great software, working with humans, and personal growth.*

*You will also receive a long-form, original article on Thursday, like the last one:*

[https://refactoring.fm/p/how-to-write-an-accomplishment-journal](https://refactoring.fm/p/how-to-write-an-accomplishment-journal)

*To receive all the full articles and support Refactoring, consider subscribing if you haven’t already!*

Get full access to Refactoring ✨

[https://refactoring.substack.com/subscribe](https://refactoring.substack.com/subscribe)?

*p.s. you can learn more about the *[*benefits of the paid plan here*](http://refactoring.fm/about)*.*

---

### 1) 🥔 Hot potato handoff

In many teams I have seen, the relationship between designers and devs only goes one way. Designers pass requirements to developers, and developers write code. That’s it.

When you think about it, the very word *handoff* seem to suggest this. You push the designs, and it’s done!

While this may work for small features, most projects instead benefit from continuous back and forth collaboration, in what Brad Frost calls “[The Hot Potato Process](https://v4.danmall.com/articles/hot-potato-process/index.html)”.

![image](../assets/d4ca77c85fed45fd.png)

Ideas are frequently passed from designer to developer and back, for the entirety of the creation cycle.

Again, this is nothing new — it is iteration and collaboration, instead of "*waterfall*".

You can take the same advice and apply it to almost any company process!

---

### 2) 🤖 AI Coding use cases

I have used AI for coding *a lot* in the last couple of months — mainly Github Copilot and Replit Ghostwriter (my favorite) — because I wanted to write about it in the newsletter.

My take is that it is useful but not a silver bullet. Here are 7 use cases that worked for me, and 4 that didn't:

1. 🥱 **Boilerplate / Repetitive code** — AI truly excels here. Creating the stubs for new components, common config, or adding libraries (e.g. add Tailwind to your project).

1. 🔍 **Write tests** — This is a specific version of #1. AI can write good tests for your code, but expect to have to add more cases yourself. However, you will never have to write another test stub in your life.

1. 📑 **Explain / document code** — AI is very good at explaining code and creating docs for you. I have tried it with complex stuff and it always handled it well. Obscure code seems like a thing of the past. You can also try [Mintlify](https://mintlify.com/) or [Theneo](https://www.theneo.io/) to generate automatic docs.

1. 🛠️ **Refactor small functions** — For when explaining is not enough! AI is surprisingly good at splitting functions, refactoring them for better performance, and other small-scale maintenance.

1. 🗄 **SQL queries** — This is an awesome use case, because SQL is no one’s favorite language. Queries look very good as long as you provide a schema. You can also try [Mason](https://mason.app/) for this.

1. ⬆️ **Pull Requests** — AI can create automatic descriptions for PRs and scan code to propose improvements, before it gets merged. This is a no-brainer and I expect it to become commonplace. You can use [Codacy Quality](https://ai.codacy.com/) for this.

1. 💻 **Terminal** — I am using [Warp](https://www.warp.dev/) as my main terminal because, other than having a great autocomplete, it includes an AI assistant that can suggest and run commands for you. I always forget how to do shell things, so this is super useful.

#### ❌ Bad use cases

Now, it hasn’t been all sunshine and rainbows. There have been times where I had to spend more time debugging AI-generated code than I would have probably spent writing the full thing myself.

The main problem is that AI almost never tells you “I don’t know how to do this” — it rather hallucinates and gives you the wrong answer.

So, I have learned to watch out for these situations:

1. **Very recent stuff** — If you ask for something that is relatively new (<2 years), there is a higher risk of hallucinations because 1) AI might not have seen it in the training data, and/or 2) examples of it were few.

1. **Niche libraries** — basically the same as above!

1. **Specific library versions** — AI isn’t good at keeping consistency between function signatures and the library versions you are using. Keep that in mind if you need something very specific.

1. **Complex functions with a lot of context needed** — AI is generally good at creating complex functions when they work in isolation (e.g. algorithms, math stuff, etc.) but it isn’t the best when it has to keep into account dependencies from a lot of other code.

More ideas on using AI in an engineering team 👇

[https://refactoring.fm/p/how-to-use-ai-tools](https://refactoring.fm/p/how-to-use-ai-tools)

### 3) 🤝 The three keys of delegation

In a way, delegating is like writing software. You take something you know well and communicate it in a way that is clear, unambiguous, and effective for someone else to execute. 

When this someone else is a person — not a computer — there are three main things you should nail: **purpose**, **outcome**, and **communication**.

#### 👁️ Purpose

Purpose means: *why we are doing this*.

This is not only incredibly important for motivation, it also helps getting better results. In fact, when people are aligned on purpose, they can take more initiative and propose alternative routes.

[Embed](https://twitter.com/lucaronin/status/1579743622424977408)

#### 🎯 Outcome

You need to describe the outcome you want for the project.

In particular, you need to explain **what success looks like**. Sometimes it is easier to do so via [*inversion*](https://refactoring.fm/p/the-power-of-inversion-), by listing all the ways something would fail instead.

You should not, however, turn this into a step-by-step guide.

It’s a fine line, but you should focus on the *what*, rather than the *how*, to create space for people to develop their own solutions.

Focus on what you want to achieve, rather than how you would do it.

#### 🔀 Communication

This is where you explain how the person should interact with you. That’s because, again, delegation is not *binary*, and for any given task you may hand off only a part of what needs to be done.

This is especially true for decision making. Based on the kind of initiative you expect from the delegate, there might be various levels:

1. Delegate comes up with a **short list of solutions** — and you decide the best.

1. Delegate comes up with a short lists of solutions and **suggests the best one** — and you sign off.

1. Delegate decides the best solution in autonomy and **goes for it**.

In my experience, you can and should always go for at least 1+2.

More ideas on good delegation 👇

[https://refactoring.fm/p/how-to-delegate](https://refactoring.fm/p/how-to-delegate)

---

And that’s it for today! If you are finding this newsletter valuable, consider doing any of these:

**1) ✉️ Subscribe to the newsletter** — if you aren’t already, consider becoming a paid subscriber. You can learn more about the [benefits of the paid plan here](http://refactoring.fm/about).

Get full access to Refactoring ✨

[https://refactoring.substack.com/subscribe](https://refactoring.substack.com/subscribe)?

**2)** ❤️ **Share it** — Refactoring lives thanks to word of mouth. Share the article with your team or with someone to whom it might be useful!

I wish you a great week! ☀️

Luca
