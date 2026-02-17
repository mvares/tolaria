---
aliases:
  - "How to embed LLMs into your tech stack"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-essays|Publish Essays →]]"
Status: Evergreened
URL: "https://refactoring.fm/p/how-to-integrate-llms"
"👓 Status": Discarded
"Created time": "2024-04-18T14:53:00.000Z"
Date: 2023-12-14
"Has Notes":
  - "[[evergreen/self-hosting-llms-vs-apis|Self-hosting LLMs vs APIs]]"
  - "[[evergreen/when-you-should-use-fine-tuning|When you should use fine-tuning]]"
  - "[[evergreen/retrieval-augmented-generation|Retrieval Augmented Generation]]"
  - "[[evergreen/prompt-engineering-strategies|Prompt Engineering Strategies]]"
  - "[[evergreen/use-llms-for-two-main-things|Use LLMs for two main things]]"
Tags:
  - Essay
  - Software
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 7c86c985-412c-483e-9a89-ed5955c8a91d
---

# How to embed LLMs into your tech stack

### 📑 Materials

---

- Use cases

- Technologies

### Andrea

### Disheng

### ✍️ Post

---

A few weeks ago I received this question via email, by Daniel:

> ***What are the best approaches to integrate LLMs into workflows? What are the best alternatives to using ChatGPT / GPT API out of the box? I would love an article where you go through the various options.***

Over the last year I have received many similar questions about AI. I have always kind of restrained from writing such an article because:

1. **Things were moving too fast** — there was a high chance that anything I could write would become legacy in a few months.

1. **Success stories were few** — honestly, despite all the hype, it has long been unclear to me what the best use cases of AI are.

Fast forward to today, I feel the dust is settling and we have a better grasp of what AI is good / not good at. The tech progress, too, has slowed down a bit ([maybe too much?](https://twitter.com/ChatGPTapp/status/1732979491071549792)) and some patterns have emerged.

So, this piece covers the best approaches for embedding LLMs into your workflows and your tech stack:

- 🎯 **Use cases **— what should you use LLMs for?

- ✏️ **Prompt engineering **— the most popular approaches and when to use them. 

- 🔧 **Fine-tuning **— for when prompt engineering is not enough. 

- 🔍 **Retrieval systems **— how to integrate LLMs with external information.

- 🖥️ **Self-hosting **— should you host an open-source model or use APIs?

This subject is quite technical, so for writing about it I asked for help to two of the most knowledgeable people about AI that I know of:

- **Andrea Rossi** — my brother! PhD in Machine Learning and ML Engineer at Google. Andrea has extensive first-hand experience on the technical side of AI, by implementing models himself and working on all the parts of the pipeline.

- **Disheng Qiu** — VP of Engineering at [Translated](https://translated.com/). When it comes to AI, Translated does it all: it has an internal research team, creates its own models from scratch, and embeds AI into all their products. They also collaborate with some of the biggest tech companies out there, like Nvidia, Airbnb, and Amazon. Disheng has vast experience in leading engineering teams and has to navigate through this all!

Let’s dive in!

---

### 🎯 Use cases

What should you use LLMs for? This is a tough question to answer, because LLMs can tackle pretty much anything, but with inconsistent quality. 

Sometimes they look incredibly smart, other times they do poorly, which makes it hard to set expectations right.

About this, they behave similarly to… humans.

In fact, I have found that a quick heuristic for good LLMs use cases is sticking with tasks that would otherwise require humans. Conversely, tasks that you would automate with code are probably still best to be addressed with code.

This is true for AI systems as well. Even though LLMs can seemingly do it all, plenty of common ML use cases, like classification or recommendation, are *still* better served by traditional architectures, which are faster and cheaper.

To any problem you may have, LLMs are possibly your slowest and most expensive option available, only second to people.

Which leads to a general rule of thumb. LLMs are:

- **Expensive and slow** — if the alternative is code.

- **Cheap and fast** — if the alternative is people.

In other words, code is extremely fast, cheap, and predictable, while humans are extremely slow, expensive, and unpredictable. LLMs sit kind of in between.

PICTURE

So, I have found that the best use cases for LLMs usually belong to two categories: **processing information**, and **drafting content 👇**

#### 1) Process / transform information

LLMs seemingly *understand* content, which makes them good at all kinds of tasks where you need to take some piece of information and transform it into something else.

A few examples:

- 📌 **Summarization** — books, documents, [youtube videos](https://eightify.app/), [meetings](https://tldv.io/), you name it. This literally benefits everyone, as we all work with content in a way or another. In many cases, note taking has become something of the past.

- 🔖 **Data entry **— LLMs can easily take emails, chat threads, and other unstructured information, and transform them into structured attributes. Then, they can even call functions (see function calling later) to send such data elsewhere. Use cases for this incredibly common: chances are you can find some manual [slot filling](https://clover.studio/2023/10/04/implement-slot-filling-chatbot-with-llama2-and-chatgpt/) / data entry tasks in your company, for example in sales and customer support.

- ❓ **Asking questions** — a specific version of summarization is being able to ask specific questions about some content, without needing to go through it all. We have only scratched the surface of this so far: imagine LLMs embedded into your docs workspace and being able to retrieve any info without needing to know where a doc lives. This is already possible [on Notion](https://www.notion.so/product/ai).

#### 2) Draft content to be created by humans

Other than transforming existing content, LLMs are useful for *drafting* a lot of what we would need otherwise to create ourselves. Think of code, emails, or documentation.

Whenever you are creating content on a regular basis, chances are you can create some good templates or instructions (like you would do for humans), and let LLMs generate use them to generate drafts.

I have seen teams successfully using this for sales emails, design docs, meeting notes, and more.

I say *draft* for two reasons:

- **Quality** — content produced by LLMs may be good enough to make you save time vs starting from scratch, but not good enough to be published as-is.

- **Consistency **— LLMs are not 100% reliable at following instructions. I have rarely found workflows *entirely* automated with LLMs, without supervision.

So, once you find a good use case, how do you work with LLMs at a tech level?

There exist many ways to integrate LLMs into workflows. This is not as simple as in buy vs build, because these systems can be tailored to your needs in different ways, based on what you need to do.

So let’s look at the most popular options 👇

---

### ✏️ Prompt engineering

There is a lot you can do by simply using good prompts (and good prompt sequences) on a base model. This should always be your first choice — and, in the vast majority of cases, it is the right one.

As models get more capable and context windows get bigger, we have been discovering more and more complex prompting techniques, which leverage the increased ability of the models of understanding us and remembering long instructions.

Here are the most consolidated approaches, from the simplest to the most sophisticated:

#### 1) Zero-shot

Large language models like GPT-4 can perform many tasks by simply following instructions, without being given past examples.

Prompt:

> *Classify the text into neutral, negative or positive.
Text: I think the vacation is okay.
Sentiment:*

Output:

> *Neutral*

The key here is that the LLM already understands the “sentiment” concept, so it can provide a good output without exanples.

#### 2) Few-shots

Few-shots prompting is a technique where the LLM *learns* how to reply by being given a few demonstrations of prompt + answer. It was introduced [in 2020](https://arxiv.org/abs/2005.14165) by Brown et al. to leverage the bigger context window of GPT-3.

Here is an example from the original paper.

Prompt:

> *A "whatpu" is a small, furry animal native to Tanzania. An example of a sentence that usesthe word whatpu is: 
We were traveling in Africa and we saw these very cute whatpus.

To do a "farduddle" means to jump up and down really fast. An example of a sentence that uses the word farduddle is:*

Output:

> *When we won the game, we all started to farduddle in celebration.*

You can experiment with different numbers of examples. There exist successful instances of up to 10-shot prompting.

Few-shots prompting typically falls short of complex reasoning tasks, where displaying correct results is not enough for the model to figure out how to get to the answer.

In these cases, we uses other techniques 👇

#### 3) Chain of thought

Chain-of-thought prompting was introduced [in 2022 by Wei et al](https://arxiv.org/abs/2201.11903), and is a way to *guide* the model to the correct answer by introducing intermediate reasoning steps.

This is often combined with few-shots. In this case, the examples provided in the few-shots prompt include longer answers that embed the reasoning applied 👇

![Example from the original paper. Standard few-shots vs Chain-of-thought few-shots.](../assets/4772300e53da474e.png)

When introduced, this technique was a breakthrough that showed how many base models could outperform even dedicated, fine-tuned ones, when given the correct prompt.

#### 4) Generated knowledge

The last technique I want to cover is *generated knowledge*, introduced by [Liu et al. in late 2022](https://arxiv.org/pdf/2110.08387.pdf).

This technique works as an intermediate layer of reasoning* *where the model is first asked to generate some *knowledge* about the task domain, and only later address the task itself.

The main difference with the *chain-of-thought* approach is that knowledge is generated by the model itself — and not via external input 👇

> *The key insight behind our method, GenerateD Knowledge Prompting (sketched in Figure 1), is that we can generate useful knowledge from a language model, then provide the knowledge as an input prompt that is concatenated with a question — Liu et al.*

![image](../assets/b29df884353e4f4f.png)

By using its own generated knowledge, it is demonstrated that the model gets to more accurate answers — it basically rectifies itself.

![Examples where prompting with generated knowledge rectifies model prediction.](../assets/772afe2a0ce14cd6.png)

A popular way of adopting the generated knowledge approach, especially for complex tasks, is to make the models come up with intermediate answers, like execution plans or task lists. Say you want the model to write a complex piece of software. It is useful to make it generate a task list first, for two main reasons:

- **It acts as generated knowledge** — it is more likely that the model will follow it consistently, as opposed to not having it explicitly attached.

- **You can review it **— if there are any conceptual mistakes, you can intercept them earlier.

Xu Hao, Thoughtworks’ Head of Technology for China, discussed an awesome example of this with Martin Fowler earlier this year:

- [LLM prompting for programming](https://martinfowler.com/articles/2023-chatgpt-xu-hao.html)

---

### 🔧 Fine tuning

Fine-tuning means further specializing a model that has already been trained on a wide data distribution on a smaller, task-specific dataset. The goal is to modify the model’s parameters to make it perform better on the task at hand.

These days, as models get bigger and prompt engineering gets better, fine-tuning is becoming more and more niche. In fact, it only makes sense if these three conditions are met:

- **The base model perform extremely poorly** — you can’t figure out any way to make the base LLM do the job for you

- **You have a *****massive***** amount of data **— that you may fine-tune the model on. We are talking of millions of tokens about something the model has never seen.  

- **You have solid ML expertise in house **— fine-tuning is long, costly, and uncertain. You may easily spend hundreds of thousands of dollars and end up with a model that does not perform better than your standard GPT-4. 

To this day, successful examples of fine-tuning are usually in domains where there is a lot of domain-specific data that is private, like in healthcare or finance. E.g. you may fine-tune a model on a large dataset of medical records to enable the model to assign relevant codes to each patient's diagnosis and treatment, saving medical professionals' time and reducing coding errors.

---

### 🔍 RAG — Retrieval-Augmented Generation

Retrieval-Augmented Generation (RAG) is a technique that enhances the quality of LLMs by incorporating external knowledge, to provide more accurate and contextual responses.

With respect to the other techniques we covered, RAG is an actual architecture: it adds an information retrieval component that allows to incorporate relevant documents from external sources, such as databases, document repositories, APIs, and more.

#### How it works

After the user submits a query, a first step of information retrieval is performed, where a separate system (not the LLM) extracts chunks of content that is relevant to the query.

Such content is added to the prompt as additional context for the LLM to be used

![image](../assets/65fc3444b3084949.png)

#### RAG vs Fine-tuning

RAG use cases have some overlap with fine-tuning: in both scenarios you have additional data that you want to use and does not fit into a prompt.

So when to use one vs the other? Basically, RAG is about queries that can be answered by using, each time, only a subset of relevant docs. Conversely, fine-tuning is about training the model with additional data to teach it how the world works, rather than copying from examples. It’s more *show, don’t tell*.

In practice, for example, if you had to build a chatbot for your docs workspace, you would probably do it with a RAG system. Each query would surface the most relevant chunks of content first, and the LLM would compose an answer based on them.

On the contrary, if you had to use an LLM for creating medical diagnoses, retrieving chunks of past medical records with a RAG system probably wouldn’t be enough. You should rather fine-tune the base model on the whole dataset of records.

Whenever both solutions work, however, RAG has strong benefits:

- **Cheap** — it is extremely cheaper than fine-tuning

- **Easy to update** — because data lives on an external systems.

#### How to build a RAG system?

You can find plenty of tutorials online and going deep into this is out of the scope of this article. However, here is the tl;dr version:

- **Build it yourself **— to make it in house, you should create an embedding of your data (e.g. via [LangChain](https://www.langchain.com/)) and host it in a vector database (e.g. [Pinecone](https://www.pinecone.io/) or [Weaviate](https://weaviate.io/)). Later, you can easily query such database to retrieve chunks of content and pass them as additional context to your LLM’s prompt

- **Low-code-it **— some low-code tools, like [n8n](https://n8n.io/langchain/), allow to create full workflows which include vector databases, querying LLMs, and processing data via LangChain. This looks very promising and by the time you are reading this I am doing various experiments with this!

- **Use ready made tools **— for specific usecases, like chatbots, there exist tools where you just upload your content and they take care of the rest. [Chatbase](https://www.chatbase.co/) and [CustomGPT](https://customgpt.ai/) are among the most popular.

---

### 🖥️ Self-hosting vs APIs

The final question you may have about integrating LLMs is whether to go the OpenAI route, using their APIs, or hosting an open-source system yourself (e.g. Llama).

APIs of course win the *ease of use* and *time to market* arguments, but what about other factors?

#### Cost & Skills

Counterintuitively, **self-hosting LLMs doesn’t typically save money** over using APIs. OpenAI’s price is extremely aggressive, and their team is world-class at optimizing the use of hardware. 

For example, hosting a Llama node on a suitable AWS instance would likely cost you around than **$8-10 / hour**, which means it would lose money on anything but high-load workflows.

And even in high-load cases, the cost upside is unclear when you factor in maintenance, which requires strong technical expertise. If you don’t have such expertise in-house, self-hosting is out of the question.

#### Privacy & Security

Solid arguments for self-hosting are, instead, **privacy and security** concerns. 

While you can opt out from letting OpenAI use your conversations’ data for future training, I completely understand companies who are uneasy at *firehosing *vast amount of private information (possibly including their customers’) to an aggressive startup.

If privacy matters to you, self-hosting an LLM may be worth the hassle.

---

### 📚 Resources

Here are further resources to learn more:

- [**Prompting Guide**](https://www.promptingguide.ai/) — amazing open source project about all-things-prompt-engineering with 150+ contributors.

- [**HuggingFace**](https://huggingface.co/) — the #1 community where people collaborate on AI projects

- [**How to use AI in an Engineering Team**](https://refactoring.fm/p/how-to-use-ai-tools) — a previous Refactoring article where I explore AI use cases for productive teams.

- [**LLM Prompting for Programming**](https://martinfowler.com/articles/2023-chatgpt-xu-hao.html) — a fantastic use case by Thoughtworks

---
