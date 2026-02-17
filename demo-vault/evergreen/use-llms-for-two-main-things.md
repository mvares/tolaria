---
aliases:
  - "Use LLMs for two main things"
"Is A":
  - Evergreen
"Last Tweeted": 2024-08-07
Tags:
  - Has Pic
  - Long
"Created at": "2024-04-18T14:44:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to":
  - "[[essay/how-to-embed-llms-into-your-tech-stack|How to embed LLMs into your tech stack]]"
  - "[[monday-ideas/monday-87|Monday #87]]"
"Old Created At": "2024-01-18T10:56:00.000+01:00"
"Updated at": "2025-05-27T13:44:00.000Z"
Status: Discarded
Tweet: "CTOs, when considering LLMs, remember: they excel in tasks needing human insight but are slow and costly compared to code. Use them for information processing like summarization and data entry, and for drafting content. But don’t automate everything—know when to keep humans in the loop for quality control. What’s your take on finding the right balance? #TechLeadership #AI"
notion_id: 78b20e5b-4408-4d3f-8a77-f3e7919917d9
---

# Use LLMs for two main things

What should you use LLMs for? This is a tough question to answer, because LLMs can tackle pretty much anything, but with inconsistent quality.

Sometimes they look incredibly smart, other times they do poorly. About this, they behave similarly to… humans.

In fact, I have found that a quick heuristic for good LLMs use cases is to stick with tasks that would otherwise **require humans**. Conversely, tasks that you would automate with code are probably still best addressed with code.

This is true for other AI systems as well. Even though LLMs can seemingly do it all, plenty of common ML use cases, like classification or recommendation, are *still* better served by traditional architectures, which are faster and cheaper.

In fact, for any problem you may have, LLMs are possibly your **slowest and most expensive** option available, only second to people. This leads to a general rule of thumb — LLMs are:

- **Expensive and slow** — if the alternative is code.

- **Cheap and fast** — if the alternative is people.

In other words, code is extremely fast, cheap, and predictable, while humans are extremely slow, expensive, and unpredictable. LLMs sit kind of in between.

![image](../assets/961d1a4daacf4667.png)

So, I have found that the best use cases for LLMs usually belong to two categories: **processing information**, and **drafting content 👇**

#### 1) Process / transform information

LLMs seemingly *understand* content, which makes them good at all kinds of tasks where you need to take some piece of information and transform it into something else.

A few examples:

- 📌 **Summarization** — books, documents, [youtube videos](https://eightify.app/), [meetings](https://tldv.io/), you name it. This literally benefits everyone, as we all work with content in a way or another. In many cases, note taking has become something of the past.

- 🔖 **Data entry** — LLMs can easily take emails, chat threads, and other unstructured information, and transform them into structured attributes. Use cases for this are incredibly common: chances are you can find plenty of manual [slot filling](https://clover.studio/2023/10/04/implement-slot-filling-chatbot-with-llama2-and-chatgpt/) / data entry tasks in your company, for example in sales and customer support.

- ❓ **Asking questions** — being able to ask questions about some content, without needing to go through it all. Imagine LLMs embedded into your docs workspace and being able to retrieve any info without needing to know where a doc lives. This is already possible [on Notion](https://www.notion.so/product/ai).

#### 2) Draft content to be created by humans

LLMs are also useful for *drafting* a lot of what we would otherwise create ourselves. Think of code, emails, or docs.

Whenever you are creating content on a regular basis, chances are you can create good templates or instructions (like you would do for humans), and let LLMs use them to generate drafts.

I have seen teams successfully using this for sales emails, design docs, meeting notes, and more.

I say *draft* for two reasons:

- **✅ Quality** — content produced by LLMs may be good enough to save you time vs starting from scratch, but not good enough to be published as-is.

- **📊 Consistency** — LLMs are not 100% reliable at following instructions. I have rarely found workflows *entirely* automated with LLMs, without supervision.

So, once you find a good use case, how do you work with LLMs at a tech level? This is not as simple as in buy vs build, because these systems can be tailored to your needs in different ways, based on what you need to do.

I have covered the most popular options with pros and cons, in a recent article 👇

---

Struggling to find the right use cases for LLMs in your tech stack? You're not alone 🤔

I have talked with a lot of teams who are grappling with this. LLMs seem to do everything, but quality is inconsistent and it’s tricky to embed them into workflows.

Here is what I learned from teams who use them the most:

1️⃣ 𝗨𝗡𝗗𝗘𝗥𝗦𝗧𝗔𝗡𝗗 𝗧𝗛𝗘 𝗦𝗪𝗘𝗘𝗧 𝗦𝗣𝗢𝗧

Counterintuitively, LLMs shine in tasks that typically require human intervention. Here's a simple heuristic to figure out use cases:

↳ 💻 𝗖𝗼𝗱𝗲 𝘃𝘀 𝗟𝗟𝗠𝘀 — If you can automate it with code, stick with code. It's faster and cheaper.

↳ 🧠 𝗛𝘂𝗺𝗮𝗻𝘀 𝘃𝘀 𝗟𝗟𝗠𝘀 — If it requires human input, LLMs can be a game-changer. They're faster and more cost-effective than people.

So, in my experience, good LLM use cases are mostly about two things: 1) information processing, and 2) content drafting. Let’s look at both:

2️⃣ 𝗜𝗡𝗙𝗢𝗥𝗠𝗔𝗧𝗜𝗢𝗡 𝗣𝗥𝗢𝗖𝗘𝗦𝗦𝗜𝗡𝗚

LLMs excel at understanding and transforming content, they are >100x faster than humans at this! Here are a few specific examples:

↳ 📌 𝗦𝘂𝗺𝗺𝗮𝗿𝗶𝘇𝗮𝘁𝗶𝗼𝗻 — from documents to meetings, LLMs can distill key points efficiently.

↳ 🔖 𝗗𝗮𝘁𝗮 𝗲𝗻𝘁𝗿𝘆 — transform unstructured data into structured formats, boosting efficiency in areas like sales and support.

↳ ❓ 𝗤𝘂𝗲𝘀𝘁𝗶𝗼𝗻 𝗮𝗻𝘀𝘄𝗲𝗿𝗶𝗻𝗴 — make LLMs access your data and retrieve information easily. Imagine an AI assistant for your company's knowledge base.

3️⃣ 𝗖𝗢𝗡𝗧𝗘𝗡𝗧 𝗗𝗥𝗔𝗙𝗧𝗜𝗡𝗚

Finally, LLMs are powerful allies in content creation, but with caveats:

↳ ✍️ 𝗗𝗿𝗮𝗳𝘁𝗶𝗻𝗴 — create initial drafts of emails, docs, and of course code.

↳ 🎯 𝗛𝘂𝗺𝗮𝗻 𝗶𝗻 𝘁𝗵𝗲 𝗹𝗼𝗼𝗽 — Human oversight is crucial. LLM output often needs refinement.

I wrote a full article about how engineering teams are using LLMs, which you can find in the first comment! 👇

How are you leveraging LLMs in your organization? Have you found any unexpected use cases or challenges?

♻️ If you found this breakdown helpful, please consider reposting. It means a lot!
