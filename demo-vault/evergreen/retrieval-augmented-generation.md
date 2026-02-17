---
aliases:
  - "Retrieval Augmented Generation"
"Is A":
  - Evergreen
"Last Tweeted": 2024-04-30
Tags:
  - Has Pic
  - Not for Monday
"Created at": "2024-04-18T14:44:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to":
  - "[[essay/how-to-embed-llms-into-your-tech-stack|How to embed LLMs into your tech stack]]"
  - "[[monday-ideas/monday-89|Monday #89]]"
"Old Created At": "2024-01-18T10:59:00.000+01:00"
"Updated at": "2025-11-27T15:33:00.000Z"
Status: Not started
Tweet: "🚀 Considering a Retrieval-Augmented Generation (RAG) system for your AI projects? It's a cost-effective way to leverage external data without the complexity of fine-tuning. Perfect for chatbots and dynamic queries. Let’s discuss the pros and cons—what's your take? #AI #CTO"
notion_id: daa508f8-e7bd-43dd-8ece-e9808f12800a
---

# Retrieval Augmented Generation

**How to create a RAG system with LLMs** 🤖

When you look at how companies are using AI, many use cases are about combining the capabilities of a base model with some company data. Think of AI chatbots, or summarization scenarios.

These are most often implemented through *Retrieval-Augmented Generation*. As opposed to prompt engineering, RAG is an full-blown architecture: it adds an information retrieval component that allows to incorporate relevant documents from external sources, such as databases, document repositories, APIs, and more.

#### How it works

After the user submits a query, a first step of information retrieval is performed, where a separate system (not the LLM) extracts chunks of content that are relevant to the query.

Such content is added to the prompt as additional context for the LLM to be used:

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
