---
aliases:
  - "My favorite AI tools for coding"
"Is A":
  - Evergreen
"Created at": "2024-10-15T12:05:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to":
  - "[[essay/predictions-about-ai|Predictions about AI]]"
  - "[[monday-ideas/monday-131|Monday #131]]"
  - "[[monday-ideas/monday-132|Monday #132]]"
"Updated at": "2024-11-26T09:12:00.000Z"
Status: Not started
notion_id: 120bdf02-815c-807b-828a-d0b6b9393ead
---

# My favorite AI tools for coding

I explored a lot of tools and workflows for coding with AI, and I will list my recommendations as of September 2024 (I don’t expect this list to be exactly timeless).

As for which AI model to use, I consistently get the best results with **Claude 3.5 (Sonnet)**. It is night and day vs GPT-4, and to me it seems still slightly better than [OpenAI O1](https://openai.com/index/introducing-openai-o1-preview/), but admittedly I had little time to play with O1.

All the tools below (except Replit) allow you to plug your preferred model by inserting your own API key. That’s how I recommend using models, not to get locked-in by the native interfaces. I use [TypingMind](https://www.typingmind.com/) for regular chat for the same reason — it makes trying new models a breeze, and I keep all the context of previous chats:

#### 🏆 [**Cursor**](https://cursor.sh/)

Cursor is, in my opinion, the current best IDE for AI. It is a fork of VS Code, has better support for chat, full context into the whole codebase (if you want it to), and it displays changes as diffs. I currently use Cursor

#### 🥇 [**Zed**](https://zed.dev/)

Zed is a refreshing take on AI and IDEs in general. Zed is written in Rust and is a super fast editor by itself, and the way it integrates AI is very interesting. You get more granular control on the context you give to the model, supports workflows, and the assistant panel feels like an extension than the editor itself, rather than a chat.

#### 🥈 [**Supermaven**](https://supermaven.com/)

Supermaven falls more into the code completion category, but it does so *with style*, thanks to two superpowers: speed & context window.

Autocompletions take ~250ms (!) and context window is 1M tokens, which is just ridiculously high (Claude has 200K), and should help with large codebases. This is possible because they use their own proprietary model, called Babble.

I couldn’t test everything of Supermaven (especially the benefits of context window), but I loved the speed, and accuracy was also very good. 

#### 🥉 [**Aider**](https://aider.chat/)

Aider has a different take on coding with AI, because it is a CLI, and is open source. It applies changes directly to files, and even commits to git (with a sensible commit message!). I liked a lot of it.

![image](https://camo.githubusercontent.com/6d2d9a8d839bed3d9dc1bf62d47f0767e19906ce76d369a78ef9805dbfb34609/68747470733a2f2f61696465722e636861742f6173736574732f73637265656e636173742e737667)

#### 🎖️ [Replit Agent](https://docs.replit.com/replitai/agent) (honorable mention)

Replit, which I am a fan of, recently added this *agent* capability to their already excellent AI support (previously called *Ghostwriter*).

Since Replit is a full environment that includes hosting, the agent can do some unique things, like deploying apps or spawning db instances. Honestly it feels like magic and sets a new bar for dx.

The drawback is that these benefits are 100% tied to the Replit environment, for the better or worse. If anything, this gives us a north star for what general purpose tools should become able to accomplish.
