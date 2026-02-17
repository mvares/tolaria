---
aliases:
  - "Monday #132"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-monday-idea|Publish Monday Idea]]"
Status: Published
"👓 Status": Not started
"Created time": "2024-11-26T09:08:00.000Z"
Date: 2024-12-02
"Has Notes":
  - "[[evergreen/my-favorite-ai-tools-for-coding|My favorite AI tools for coding]]"
  - "[[evergreen/how-to-advocate-for-tech-debt|How to advocate for tech debt]]"
  - "[[evergreen/your-manager-feels-more-productive-than-you|Your manager feels more productive than you]]"
Tags:
  - Monday
  - Free
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 14abdf02-815c-8017-a38b-ea6b23aa7aa0
---

# Monday #132

### 1) 🤖 My favorite AI coding tools

I explored a lot of tools and workflows for coding with AI — so here are my recommendations.

As for which AI model to use, I consistently get the best results with **Claude 3.5 (Sonnet)**. It is night and day vs GPT-4, and to me it seems still slightly better than [OpenAI O1](https://openai.com/index/introducing-openai-o1-preview/).

All the tools below (except Replit) allow you to plug your preferred model by inserting your own API key. That’s how I recommend using models, not to get locked-in by the native interfaces. I use [TypingMind](https://www.typingmind.com/) for regular chat for the same reason — it makes trying new models a breeze, and I keep all the context of previous chats:

- 🏆 [**Cursor**](https://cursor.sh/)** **— in my opinion, the current best IDE for AI. It is a fork of VS Code, has better support for chat, full context into the whole codebase (if you want it to), and it displays changes as diffs.

- 🥇 [**Zed**](https://zed.dev/)** **— a refreshing take on AI and IDEs in general. It is written in Rust and is a super fast editor by itself, and the way it integrates AI is very interesting. You get more granular control on the context you give to the model, supports workflows, and the assistant panel feels like an extension than the editor itself.

- 🥈 [**Supermaven**](https://supermaven.com/)** **— falls more into the code completion category, but it does so *with style*, thanks to two superpowers: speed & context window. Autocompletions take ~250ms (!) and context window is 1M tokens, which is just ridiculously high (Claude has 200K), and should help with large codebases.

- 🥉 [**Aider**](https://aider.chat/)** **— has a different take on coding with AI, because it is a CLI, and is open source. It applies changes directly to files, and even commits to git (with a sensible commit message!). I liked a lot of it.

- 🎖️ [**Replit Agent**](https://docs.replit.com/replitai/agent) (*honorable mention*) — Replit, which I am a fan of, recently added this *agent* capability to their already excellent AI support. Since Replit is a full environment that includes hosting, the agent can do some unique things, like deploying apps or spawning db instances. Honestly it feels like magic and sets a new bar for dx. The drawback is that these benefits are 100% tied to the Replit environment, for the better or worse. If anything, this gives us a north star for what general purpose tools should become able to accomplish.

You can find the full article I wrote about AI and coding below 👇

[https://refactoring.fm/p/predictions-about-ai](https://refactoring.fm/p/predictions-about-ai)

---

### 2) 🤷‍♂️ Your manager feels more productive than you

In our [industry survey](https://refactoring.fm/p/the-state-of-engineering-productivity) earlier this year, we asked people how they would rate their personal productivity from 1 to 10, and the one of their team. 

For various [psychological reasons](https://tonyflorida.com/ten-point-rating-scale-without-seven/), broad questions like this always average around 7, so no big insight here — but an interesting result, which probably won’t help with managers’ reputation among engineers, is that the higher people raise through the ranks, the more productive they feel — to the detriment of the rest of their team.

![image](../assets/14abdf02815c803e.png)

While software engineers feel on average *less* productive than their team at large — making the case for widespread impostor syndrome — the same isn’t true for managers and Staff+ ICs, which generally feel significantly better about themselves than how they feel about their teams.

As we will see, factors reported as impacting personal productivity (negatively or positively) significantly differ based on people’s roles, which, combined with the above, points at a general *disconnect* between the needs of regular engineers and that of their higher-ups.

More insights below:

[https://refactoring.fm/p/the-state-of-engineering-productivity](https://refactoring.fm/p/the-state-of-engineering-productivity)

---

### 3) 📣 How to advocate for tech debt

The biggest struggle of engineering leaders around tech debt is usually not the absolute time you have to spend on it, but rather how to *advocate* for it with stakeholders.

About this, I believe the word *tech debt *itself is a bad framing for rework. It feels like you *have* to do them because of a duty (repay a debt) rather than a true business opportunity — as they are instead. So here is my advice:

#### 1) Present a good ROI 📏

Measure both the *bad* (e.g. time spent regularly on maintenance, frustration, latency, …) and the *good* (e.g. product improvements *enabled *by the rework).

Do your homework and treat it like a product initiative.

#### 2) Create success stories 🏆

Big reworks are always daunting, no matter how good your story is. To create enough momentum to go after them, create a solid **track record** of small-scale debt that has been successfully repaid, with proven outcomes.

Whenever you do some small rework, don’t stop there, measure the outcome and make it visible. In other words, build trust 👇

#### 3) Build trust ❤️

No matter how good you are, tech debt items will always be at a disadvantage when pit against regular product features. 

That’s because features have immediate impact — e.g. increasing the conversion rate at checkout — while refactoring has a **delayed feedback loop** that is measured in efficiency, velocity, and all kinds of second-order effects.

It's not a level playing field, so **trust** plays a decisive role. Many times, the #1 element that enables repaying debt is **strong relationships **between stakeholders, as opposed to precise KPIs.

This trust, however, is earned. You earn it over time by being rigorous and by creating a good track record. These, in turn, give you room to go after bigger and bigger things.

More ideas on our majestic guide on technical debt:

[https://refactoring.fm/p/the-definitive-guide-to-manage-technical](https://refactoring.fm/p/the-definitive-guide-to-manage-technical)

---

And that’s it for today! If you are finding this newsletter valuable, consider doing any of these:

**1) **🔒** Subscribe to the paid version** — if you aren’t already, consider becoming a paid subscriber. 1500+ engineers and managers have joined already! Learn more about the [benefits of the paid plan here](http://refactoring.fm/about).

Get full access to Refactoring ✨

[https://refactoring.substack.com/subscribe](https://refactoring.substack.com/subscribe)?

**2)** 🍻 **Read with your friends** — Refactoring lives thanks to word of mouth. Share the article with your with someone who would like it, and **get a free membership** through the new [referral program](https://refactoring.fm/p/referral).

Read with your friends 🍻

[https://refactoring.fm/leaderboard](https://refactoring.fm/leaderboard)

I wish you a great week! ☀️

Luca
