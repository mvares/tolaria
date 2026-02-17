---
aliases:
  - "Monday #89"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-monday-idea|Publish Monday Idea]]"
Status: Published
"👓 Status": Not started
"Created time": "2024-04-18T15:09:00.000Z"
Date: 2024-02-05
"Has Notes":
  - "[[evergreen/retrieval-augmented-generation|Retrieval Augmented Generation]]"
  - "[[evergreen/naming-files-and-folders|Naming files and folders]]"
  - "[[evergreen/keep-a-buffer-between-meetings|Keep a buffer between meetings]]"
Tags:
  - Monday
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 63290590-9814-44f4-b39a-d89761b96c04
---

# Monday #89

*Hey, *[*Luca*](https://twitter.com/lucaronin)* here! Welcome to the ****Monday Ideas ***💡

*Every Monday I send you an email like this with ****3 short ideas**** about making great software, working with humans, and personal growth.*

*Paid members also receive a long-form, original essay on Thursday, like the last one:*

[https://refactoring.fm/p/trillion-dollar-coach](https://refactoring.fm/p/trillion-dollar-coach)

*To receive all the full articles and support Refactoring, consider joining 1400+ engineers and get the paid membership!*

Get full access to Refactoring ✨

[https://refactoring.substack.com/subscribe](https://refactoring.substack.com/subscribe)?

*p.s. learn more about the *[*benefits of the paid plan here*](http://refactoring.fm/about)*.*

---

### 1) 🎈 Meeting buffers

If your agenda is packed with meetings, a simple trick to keep your sanity is to schedule them to be 25 or 50 mins long.

This way, you always have a buffer of 5 or 10 mins in between them to reset your head.

In my experience, it is also better to put this buffer at the beginning, rather than at the end. E.g. you schedule a meeting from 14:05 to 14:30, rather than 14:00 → 14:25. Somewhat, having the buffer at the beginning counters the inevitable few minutes of waiting for people to join, so it’s a win-win.

[https://twitter.com/mmmandel/status/1751002334413701387](https://twitter.com/mmmandel/status/1751002334413701387)

More ideas on defusing stress:

[https://refactoring.fm/p/stress](https://refactoring.fm/p/stress)

---

### 2) ✏️ Naming files and folders

Good names are important for making the various parts of the codebase discoverable — especially file names and folder structures.

There are two main ways you can find something in a codebase:

- 🔍 **Direct search** — you *grep* for a file/folder name, or part of a name.

- 🔀 **Navigation** — you navigate through the folder structure.

In almost any codebase, good structure for navigation matters more than individual file names. In fact, if you do well with the former, you get some leeway for screwing up the latter, while the opposite is not true.

So, as a rule of thumb, you want to encapsulate as little context as possible into file names. E.g. if you have a `Hero` component, you should probably call it `Hero.js` and put it into a `components` folder, rather than calling it `HeroComponent.js` and put it into the root.

This was a trivial example, but many similar cases are not. In general, be suspicious of two things:

- Too much context going into file names.

- Bland folder structure that does not tell you anything about the product.

About the latter, I am generally a fan of the [**Screaming Architecture**](https://blog.cleancoder.com/uncle-bob/2011/09/30/Screaming-Architecture.html) approach by Robert Martin, which promotes creating structures that *scream* the domain they are about.

He compares software architecture to *building* architecture: when you look at the blueprints of a building, you should immediately understand what the building is about. If you see a kitchen, a living room, and a bedroom, you know you are looking at a residential building. And the same should go for software.

I have a caveat, though.

Martin appears to view the structures promoted by full-stack frameworks such as Rails or Spring as negative examples — because they are *bland* and do not scream anything about your app.

The way I see it, though, to stay within the *building* metaphor, is that frameworks like Rails are ways to create blueprints for different types of buildings.

So, it’s like Rails is for building residential homes, and it already gives you a folder structure with a Kitchen, Bathrooms, Dining room, etc.

This is undeniably good, because:

1. Everybody knowing the framework knows where to look at in any project.

1. It teaches everyone the basics of what residential homes should look like.

Of course, this means the framework is opinionated and you may not agree with it, but when you do, instead, it saves you a ton of cognitive effort. Then, there is still room for a *screaming architecture*, inside the business logic folders.

You can find extensive advice on naming things in this Refactoring piece:

[https://refactoring.fm/p/how-to-name-things](https://refactoring.fm/p/how-to-name-things)

---

### 3) 🤖 Retrieval-Augmented Generation

When you look at how companies are using LLMs, either internally or inside their products, many use cases are about combining the capabilities of the base model with some company data. Think of AI chatbots, or summarization scenarios.

Many of these use cases are implemented through *Retrieval-Augmented Generation*. As opposed to prompt engineering, RAG is an actual architecture: it adds an information retrieval component that allows to incorporate relevant documents from external sources, such as databases, document repositories, APIs, and more.

#### How it works

After the user submits a query, a first step of information retrieval is performed, where a separate system (not the LLM) extracts chunks of content that are relevant to the query.

Such content is added to the prompt as additional context for the LLM to be used:

Architecture of a basic RAG system

![image](../assets/ae4e9466957c4703.png)

#### RAG vs Fine-tuning

RAG use cases have some overlap with fine-tuning: in both scenarios you have additional data that you want to use and that does not fit into a prompt.

So when to use one vs the other? Basically, RAG is about queries that can be answered by using, each time, only a subset of relevant docs. Conversely, fine-tuning is about training the model with additional data to teach it how the world works, rather than copying from examples. It’s more *show, don’t tell*.

In practice, for example, if you had to build a chatbot for your docs workspace, you would probably do it with a RAG system. Each query would surface the most relevant chunks of content first, and the LLM would compose an answer based on them.

On the contrary, if you had to use an LLM for creating medical diagnoses, retrieving chunks of past medical records with a RAG system probably wouldn’t be enough. You should rather fine-tune the base model on the whole dataset of records.

Whenever both solutions work, however, RAG has strong benefits:

- **Cheap** — it is extremely cheaper than fine-tuning

- **Easy to update** — because data lives on external systems.

#### How to build a RAG system?

You can find plenty of tutorials online and going deep into this is out of the scope of this article. However, here is the tl;dr version:

- **🔨 Build it yourself** — to make it in house, you should create an embedding of your data (e.g. via [LangChain](https://www.langchain.com/)) and host it in a vector database (e.g. [Pinecone](https://www.pinecone.io/) or [Weaviate](https://weaviate.io/)). Later, you can easily query such database to retrieve chunks of content and pass them as additional context to your LLM’s prompt.

- **🔌 Low-code-it** — some low-code tools, like [n8n](https://n8n.io/langchain/), allow to create full workflows which include vector databases, querying LLMs, and processing data via LangChain. This looks very promising and by the time you are reading this I am doing various experiments with this.

- **💳 Use ready-made tools** — for specific use cases, like chatbots, there exist tools where you just upload your content and they take care of the rest. [Chatbase](https://www.chatbase.co/) and [CustomGPT](https://customgpt.ai/) are among the most popular.

You can find more ideas on how to integrate LLMs into your products in this recent Refactoring edition 👇

[https://refactoring.fm/p/how-to-integrate-llms](https://refactoring.fm/p/how-to-integrate-llms)

---

And that’s it for today! If you are finding this newsletter valuable, consider doing any of these:

**1) ✉️ Subscribe to the newsletter** — if you aren’t already, consider becoming a paid subscriber. 1400+ engineers and managers have joined already! Learn more about the [benefits of the paid plan here](http://refactoring.fm/about).

Get full access to Refactoring ✨

[https://refactoring.substack.com/subscribe](https://refactoring.substack.com/subscribe)?

**2)** 🍻 **Read with your friends** — Refactoring lives thanks to word of mouth. Share the article with your with someone who would like it, and **get a free membership** through the new [referral program](https://refactoring.fm/p/referral).

Read with your friends 🍻

[https://refactoring.fm/leaderboard](https://refactoring.fm/leaderboard)

I wish you a great week! ☀️

Luca
