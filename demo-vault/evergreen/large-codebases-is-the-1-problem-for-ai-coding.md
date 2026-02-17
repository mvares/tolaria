---
aliases:
  - "Large codebases is the #1 problem for AI coding"
"Is A":
  - Evergreen
Tags:
  - Has Pic
"Created at": "2025-03-13T13:58:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to":
  - "[[essay/how-do-engineering-teams-use-ai-augment|How do Engineering Teams use AI? (Augment)]]"
  - "[[monday-ideas/monday-147|Monday #147]]"
"Updated at": "2025-04-01T07:52:00.000Z"
Status: Not started
Tweet: "Large codebases remain the #1 challenge for AI in coding. While today's models excel at solving algorithmic problems, their performance plummets on real tasks due to a critical lack of context. Fine-tuning is slow and costly, and context windows don't scale. RAG shows promise, but we're still learning how to build it effectively. How will human engineers adapt to work alongside smarter AI? Let's discuss."
notion_id: 1b5bdf02-815c-8047-985c-c4369733e2d7
---

# Large codebases is the #1 problem for AI coding

Today’s models are *already* performing like top software engineers in pure algorithmic problems. Already last October, Claude 3.5 was able to autonomously [solve 86% of a random set of LeetCode problems](https://www.thinkevolveconsulting.com/can-claude-cheat-coding-interview/), from all ranges of difficulty. 

However, faced with real freelancing tasks, this percentage drops to 26%. Check out this [OpenAI benchmark](https://openai.com/index/swe-lancer/) from just three weeks ago.

This different is all about **context**. As a senior software engineer from OpenAI noted:

> *"AI can generate code snippets well, but when it comes to fitting them into an existing project, it often fails due to a ****lack of context****."*

![image](../assets/1b5bdf02815c8017.png)

Also, these benchmarks are about the *previous* generation of LLMs. The recent releases of Sonnet 3.7 and GPT 4.5 will surely move the *intelligence* bar higher, making context an even more obvious bottleneck.

So, when it comes to coding, how is context passed to AI? There are three possible ways: **fine-tuning**, **context window**, **RAG**

Out of these, only RAG is showing promise. Fine-tuning is unpredictable, slow, and extremely costly; while adding code to the context window doesn’t work at scale and doesn’t seem to guarantee precision.

![image](../assets/1b5bdf02815c8039.webp)

So, good RAG is the best candidate to scale AI coding tools, but RAG architectures are not a commodity: we are still in the early days of learning how to build them well, for different types of content (code is completely different from e.g. literature), and different use cases. The team at Augment [developed their pipeline from scratch](https://www.augmentcode.com/blog/a-real-time-index-for-your-codebase-secure-personal-scalable) and keeps doing an inordinate amount of work on it.

Now, let’s say models are smart enough and context is somehow solved — how are human engineers going to work with AI? 👇
