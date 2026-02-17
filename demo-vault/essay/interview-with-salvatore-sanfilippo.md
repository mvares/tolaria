---
aliases:
  - "Interview with Salvatore Sanfilippo"
"✏️ Status": Not started
"Belongs to":
  - "[[responsibility/publish-podcast|Publish Podcast]]"
  - "[[person/salvatore-sanfilippo|Salvatore Sanfilippo]]"
Status: Evergreened
URL: "https://refactoring.fm/p/open-source-complexity-and-ai-coding"
"👓 Status": Not started
"Created time": "2025-04-03T06:59:00.000Z"
Date: 2025-04-04
"Has Notes":
  - "[[evergreen/we-are-destroying-software-salvatore-sanfilippo|We are destroying software (Salvatore Sanfilippo)]]"
  - "[[evergreen/staying-in-sicily-salvatore-sanfilippo|Staying in Sicily (Salvatore Sanfilippo)]]"
Tags:
  - Podcast
  - Free
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 1cabdf02-815c-8025-aabc-dc9fc86fc6b4
---

# Interview with Salvatore Sanfilippo

Today's guest is Salvatore Sanfilippo, also known as Antirez!

Salvatore is the creator of Redis, an open source data store used by hundreds of thousands of developers across the world. And he's also a writer. He published the popular sci-fi novel called Wohpe, which anticipated a lot of what is happening today with AI.

With Salvatore, we talked about open source — what makes a project successful and how to make it successful for its maintainers. Then we discussed how Salvatore uses AI for extremely complex coding, which makes him 5x faster than without AI. And finally, I asked him about his writing work and what is the experience of writing a novel versus a software project.

### 🎙️ Episode

You can watch the full episode on [Youtube](https://www.youtube.com/@refactoringclub):

[Video](https://youtu.be/PlyzvM--xbQ)

Or listen to it on [Spotify](https://open.spotify.com/show/7Luds9dmzZDoDC8Q7EMbSw), [Apple](https://podcasts.apple.com/us/podcast/refactoring-podcast/id1719137305), [Overcast](https://overcast.fm/itunes1719137305), or your podcast app of choice.

---

### 🥇 Interview Summary

If you are a **🔒 paid subscriber 🔒** you will find *my own**** ****summary* of the interview below.

It’s the **10-minute, handcrafted takeaways** of what we talked about, with timestamps to the relevant video moments, for those who don’t have time to sit through the 1-hour chat.

Here is the agenda for today:

1. **🏠 Staying in Sicily: Life & Career Choices** ([**05:09**](https://youtu.be/PlyzvM--xbQ&t=309s))

1. **🔧 What Makes Open Source Projects Successful** ([**12:47**](https://youtu.be/PlyzvM--xbQ&t=767s))

1. **💰 Monetizing Open Source Software** ([**19:19**](https://youtu.be/PlyzvM--xbQ&t=1159s))

1. **🧠 "We Are Destroying Software": The Complexity Problem** ([**23:19**](https://youtu.be/PlyzvM--xbQ&t=1399s))

1. **🤖 Using AI for Complex Coding Tasks** ([**34:31**](https://youtu.be/PlyzvM--xbQ&t=2071s))

1. **📚 From Coding to Novel Writing** ([**50:31**](https://youtu.be/PlyzvM--xbQ&t=3031s))

Let’s dive in 👇

---

### **1) 🏠 Staying in Sicily: Life & Career Choices (**[**05:09**](https://youtu.be/PlyzvM--xbQ&t=309s)**)**

Salvatore made a deliberate choice to build his career from Sicily rather than relocating to tech hubs like Silicon Valley.

He explains that while being in tech centers might lead to greater wealth, it's not necessary for engineering excellence:

> ***"To be a successful software engineer, you can be everywhere, but to make a lot of money, it is much better to stay in the center of things... For me, it was not a problem of performance, but how much money you want to make."***

Salvatore believes that once you reach a comfortable income threshold (he mentions around €4,000/month), additional money contributes minimally to wellbeing. His decision to remain in Sicily was driven by:

- **🌍 Personal values** — preferring Europe's balance of capitalism and social services

- **🏡 Community connections** — maintaining important relationships in his hometown

- **🧠 Quality of life** — prioritizing wellbeing over wealth accumulation

He notes that he's seen many young people in the US who "become rich too fast" and experience "lack of purpose" as a result, reinforcing his comfort with his choices.

### **2) 🔧 What Makes Open Source Projects Successful (**[**12:47**](https://youtu.be/PlyzvM--xbQ&t=767s)**)**

Salvatore identifies key ingredients that contribute to open source success in 2025, with simplicity being at the forefront:

> ***"Now there are a few things that make simplicity more interesting than before... There is a need for simplicity in general everywhere."***

He points to Python's UV package manager as an example of a tool gaining traction specifically because it's simpler and faster than alternatives, despite entering a crowded marketplace.

The essential elements for open source success include:

- **📑 Immediate clarity** — A project should be understandable within the first few lines of documentation

- **🎯 Broad usefulness** — Find the intersection between your needs and what many others need

- **⚙️ Engineering differentiation** — Choose areas where excellent engineering can make a meaningful difference

Salvatore emphasizes that while you don't need to be an expert in a specific domain to start, you should have strong "general problem-solving and design abilities" that you can apply to new areas after filling knowledge gaps.

### **3) 💰 Monetizing Open Source Software (**[**19:19**](https://youtu.be/PlyzvM--xbQ&t=1159s)**)**

When it comes to making open source sustainable financially, Salvatore suggests different approaches based on scale ambitions:

For smaller companies focused on steady, sustainable growth:

- Use permissive licenses (like BSD)

- Focus on professional services and expertise

- Aim for a small team size (around 10 people)

- Target modest but consistent revenue (<$10M annually)

For those aiming to build large-scale businesses:

- Consider GPL licensing to ensure cloud providers must pay for compatible licenses

- Keep the core value in the open source offering, not hidden behind closed extensions

- Focus on building products, not just services

Salvatore suggests that founders should decide early on their growth ambitions, as the strategies differ significantly between building a smaller, fully-owned business versus pursuing VC funding that ultimately reduces ownership.

### **4) 🧠 "We Are Destroying Software": The Complexity Problem (**[**23:19**](https://youtu.be/PlyzvM--xbQ&t=1399s)**)**

Salvatore delivers a strong critique of unnecessary complexity in modern software, particularly targeting large tech companies:

> ***"Big entities like Google cannot design good things. They did a terrible job with HTTP, and with new protocols. For small gains, there are huge complexity gains that make the web less accessible, less comfortable."***

He argues that the root causes of this complexity include:

- **🔬 Over-engineering** — Companies like Google are staffed with "PhD engineering types" who optimize for minimal performance gains (like 3-5% faster) while ignoring the massive complexity costs.

- **🧩 Organizational structure** — The separation between frontend and backend developers creates artificial boundaries that lead to duplicated work, like in state management.

- **⚖️ Different priorities** — Large companies optimize for different problems than most developers face.

Salvatore explains how web development became unnecessarily complex:

> ***"Framework after framework the web became slower and more complicated. And it's the same web forms, buttons and listings... 20 years ago was the same. But it was a much simpler stack. It was faster with slower computers."***

He sees this as a difficult cycle to break because developers need to learn these complex technologies to remain employable, even though they recognize the inefficiency.

### **5) 🤖 Using AI for Complex Coding Tasks (**[**34:31**](https://youtu.be/PlyzvM--xbQ&t=2071s)**)**

Salvatore has integrated AI deeply into his coding workflow, particularly while developing complex C code for Redis vector sets (a vector similarity feature):

> ***"I believe I am more or less five times faster than I was before AI. When writing system code... I can create in two months what normally could take like one year of work or six months at least."***

His AI coding approach includes:

- **🧠 Pair programming** — Using Claude (not code editors with AI) as a colleague to discuss approaches and review code

- **🧪 Testing assistance** — Creating comprehensive test suites that would have taken months to develop manually

- **🔍 Code review** — Running multiple different code review prompts to catch potential issues

- **📝 Documentation templates** — Using AI to draft documentation in a consistent style after establishing patterns

Salvatore provides extensive context to AI when prompting, often including source code rather than just documentation to help the AI understand implementation details. He believes effective prompting is crucial:

> ***"For this kind of help, you have to be very good at prompting. I don't believe everybody is the same at using LLMs. So sometimes people believe that if the AI doesn't work well enough, it's because AI is broken."***

He suggests that many developers underreport the productivity gains from AI due to job security concerns or ego, while he openly embraces the technology that makes previously unthinkable optimizations possible.

### **6) 📚 From Coding to Novel Writing (**[**50:31**](https://youtu.be/PlyzvM--xbQ&t=3031s)**)**

Salvatore published a science fiction novel called "Wohpe" in 2022 that anticipated many developments in AI, including prompt engineering, which he began writing around 2020-2021 after seeing early demos of GPT-2 and GPT-3.

He saw the transformative potential of AI before most:

> ***"When I saw GPT-3, I saw that the world like we know it is going to change very soon. And when I was writing Wohpe, I thought this book is too late at this point. It's too late because in a couple of years it will be everything reality."***

For software developers considering writing, Salvatore draws parallels between coding and novel writing:

- **🔄 Similar structures** — Both involve managing many small, connected elements at scale

- **🚀 Natural transition** — Programmers already understand handling complexity, making them well-prepared

- **🤝 Reader connection** — Writing creates meaningful, asynchronous connections between author and readers

Salvatore values the community formed around his book, particularly among Italian IT professionals. He recommends writing as a transformative experience:

> ***"For yourself, it will be a really incredible experience... because it changes completely the way you read after that."***

The novel became a way for Salvatore to express his early understanding of AI's potential when many weren't yet interested in the topic, solidifying his foresight in this rapidly evolving field.

---

### 🙏 Thank you

Thank you so much for reading & listening! Let me know what you think about the podcast and the brand new summaries in the comments or via email!

We just got started with the Podcast, so if you found this chat valuable, please consider **subscribing to the show** on [YouTube](https://www.youtube.com/@refactoringclub), [Apple](https://podcasts.apple.com/us/podcast/refactoring-podcast/id1719137305), or [Spotify](https://open.spotify.com/show/7Luds9dmzZDoDC8Q7EMbSw).

Also, consider **giving us a rating** or leaving a review on the platform of your choice, as that really helps other listeners find the show.

See you next week! 👋

Luca

### 🐦 Linkedin / Twitter
