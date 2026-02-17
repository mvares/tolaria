---
aliases:
  - "Interview with Abi Noda"
"✏️ Status": Not started
"Belongs to":
  - "[[responsibility/publish-podcast|Publish Podcast]]"
  - "[[person/abi-noda|Abi Noda]]"
Status: Evergreened
URL: "https://refactoring.fm/p/measuring-and-improving-developer?utm_source=publication-search"
"👓 Status": Not started
"Created time": "2025-04-16T07:16:00.000Z"
Date: 2025-04-18
"Has Notes": "[[evergreen/input-vs-output-metrics|Input vs output metrics]]"
Tags:
  - Podcast
  - Free
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 1d7bdf02-815c-8034-91c3-d3ea97506590
---

# Interview with Abi Noda

### Notes

Today's guest is Abi Noda, the CEO and founder of DX, one of the leading engineering intelligence platforms.

With Abi, we talked about **measuring and improving developer experience**. We started with the early days of [Accelerate](https://www.goodreads.com/book/show/35747076-accelerate) and why we feel like most people got the book wrong. Then we continued to present days and how research focuses on driving great developer experience. And finally, we couldn't avoid talking about AI and why it seems to be a game changer for entrepreneurs, but not so much for teams yet.

### 🎙️ Episode

You can watch the full episode on [Youtube](https://www.youtube.com/@refactoringclub):

[Video](https://www.youtube.com/watch?v=ANvawHql0Wk)

Or listen to it on [Spotify](https://open.spotify.com/show/7Luds9dmzZDoDC8Q7EMbSw), [Apple](https://podcasts.apple.com/us/podcast/refactoring-podcast/id1719137305), [Overcast](https://overcast.fm/itunes1719137305), or your podcast app of choice.

---

### 🥇 Interview Summary

If you are a **🔒 paid subscriber 🔒** you will find *my own**** ****summary* of the interview below.

It’s the **10-minute, handcrafted takeaways** of what we talked about, with timestamps to the relevant video moments, for those who don’t have time to sit through the 1-hour chat.

Here is the agenda for today:

1. 📈 **Abi's Journey and Pull Panda Origin Story** ([**02:10**](https://youtu.be/ANvawHql0Wk&t=130s))

1. 📚 **Revisiting Accelerate and DORA Metrics** ([**07:09**](https://youtu.be/ANvawHql0Wk&t=429s))

1. 🔍 **Output vs. Input Metrics** ([**13:06**](https://youtu.be/ANvawHql0Wk&t=786s))

1. 💻 **Defining and Measuring Developer Experience** ([**21:32**](https://youtu.be/ANvawHql0Wk&t=1292s))

1. 🤖 **AI's Real Impact on Developer Productivity** ([**35:21**](https://youtu.be/ANvawHql0Wk&t=2121s))

Let's dive in 👇

---

### **1) 📈 Abi's Journey and Pull Panda Origin Story (**[**02:10**](https://youtu.be/ANvawHql0Wk&t=130s)**)**

Abi Noda's journey into developer productivity began about eight years ago when he transitioned from software development to engineering management. As a newly appointed CTO at a startup, he faced a critical question from his CEO: how do we measure engineering productivity?

> ***"I always joke with people, I'm still trying to answer that question. Eight years later, I'm still trying to answer that question for my CEO."***

This question led Abi to create Pull Panda, which started as a simple tool to automate pull request reminders for his team. After being let go from his job, he continued developing Pull Panda, which grew to include analytics for measuring pull request metrics. The tool combined both quantitative data and actionable insights, making it particularly valuable for engineering teams.

What made Pull Panda effective wasn't just the dashboards but the **automated alerts that nudged teams toward better behaviors** — demonstrating early on that metrics alone aren't valuable without driving action.

---

### **2) 📚 Revisiting Accelerate and DORA Metrics (**[**07:09**](https://youtu.be/ANvawHql0Wk&t=429s)**)**

The conversation turns to the influential book "Accelerate" and how its legacy has been somewhat misunderstood in the industry. We covered this because I was writing our own review + summary of accelerate, which went out on Wednesday!

[https://refactoring.fm/p/accelerate](https://refactoring.fm/p/accelerate)

While most engineers associate Accelerate with the four DORA metrics, Abi points out that the book is actually 90% about culture and engineering practices, with metrics being just a small component.

> ***"There's a running joke in the community that when the book got published, everyone just jumped to page 19 or 20, read the page with the four metrics, and then put down the rest of the book."***

Until Accelerate, the discourse around engineering metrics focused mainly on whether to measure lines of code or story point velocity. Accelerate was revolutionary because it introduced metrics that were actually meaningful, with statistical backing.

However, Abi emphasizes that organizations often misuse these metrics by focusing too narrowly on the numbers themselves rather than understanding their purpose within the broader organizational context.

---

### **3) 🔍 Output vs. Input Metrics (**[**13:06**](https://youtu.be/ANvawHql0Wk&t=786s)**)**

One of the key insights Abi shares is the distinction between output metrics (diagnostic) and input metrics (controllable):

- ➡️ **Output metrics** — (like DORA metrics) show results but can't be directly controlled.

- ⬅️ **Input metrics** — are what teams can actually influence day-to-day.

Abi uses a health analogy to explain this concept:

> ***"Common diagnostic metrics for health are things like blood glucose, cholesterol levels, weight, blood pressure. They are diagnostic metrics. If you want to improve your blood glucose, you can't just suck glucose out of your blood - you have to control your inputs like protein intake or sugar consumption."***

This distinction is crucial because many organizations mistakenly try to optimize output metrics directly, which leads to number distortion rather than actual improvement. The focus should be on identifying and improving the inputs that drive better outputs.

Abi explains that DX (his company) focuses on developer experience as a controllable input that drives productivity, believing that removing friction in both technical and social aspects of development ultimately leads to better performance metrics.

---

### **4) 💻 Defining and Measuring Developer Experience (**[**21:32**](https://youtu.be/ANvawHql0Wk&t=1292s)**)**

DX has distilled developer experience down to approximately 14 key drivers after extensive research and statistical analysis. These drivers include:

- 🧠 **Focus time** — the ability to work without interruptions

- 🔄 **Feedback loops** — how quickly developers can verify changes

- 🧩 **Code understandability** — how easily developers can comprehend the codebase

- 📝 **Documentation** — access to necessary information

Their approach involves measuring these factors through self-reported data and rolling them up into a composite "*Developer Experience Index*" (DXI). This quantifies the previously ethereal concept of developer experience in a measurable way.

> ***"Developer sentiment toward tech debt is universally low. That data point by itself is not really actionable or meaningful. It's only when you compare it to the rest of the industry that you can understand - this is bad, but it's actually just as bad as everyone else."***

Benchmarking is critical in this process, as it provides context for the numbers and helps leadership understand whether a particular score is concerning. Abi notes that comparing like with like is important - mobile engineering should be compared to other mobile teams, for example.

The most common problem areas Abi identified are:

- 🐢 **Decision-making speed** — slow decision processes often cause more delay than technical issues

- 📚 **Knowledge management** — information is often lost or difficult to find

- ⏱️ **Focus time** — constant interruptions from various sources beyond just meetings

---

### **5) 🤖 AI's Real Impact on Developer Productivity (**[**35:21**](https://youtu.be/ANvawHql0Wk&t=2121s)**)**

Despite the hype around AI's impact on development, DX's data shows more modest gains in the real world:

- 📊 **Actual productivity gains** — only about 5-10% productivity improvement on average

- 🏗️ **Code maintainability concerns** — teams using generative AI more heavily show lower scores in code maintainability

> ***"I think the code maintainability and quality problem is a real concern. Code maintainability is one of the things we measure as part of the developer experience index. And we have seen that be lower for teams that are using Gen AI more."***

Abi explains the disconnect between social media hype and reality: AI tools excel at generating boilerplate code and "0 to 1" development, but most real-world software development is iterative ("1 to 1.1") and maintenance-focused. This context-heavy work is where AI currently struggles, with success rates dropping from 85-90% on abstract coding problems to less than 20% on real-world team tickets.

However, Abi remains optimistic about AI's potential to help with knowledge management problems, including both search/discoverability of existing knowledge and AI-generated documentation.

---

### 🙏 Thank you

And that’s it! Thank you so much for reading & listening! Let me know what you think about the podcast and the summaries in the comments or via email!

We just got started with the Podcast, so if you found this chat valuable, please consider **subscribing to the show** on [YouTube](https://www.youtube.com/@refactoringclub), [Apple](https://podcasts.apple.com/us/podcast/refactoring-podcast/id1719137305), or [Spotify](https://open.spotify.com/show/7Luds9dmzZDoDC8Q7EMbSw).

Also, consider **giving us a rating** or leaving a review on the platform of your choice, as that really helps other listeners find the show.

See you next week! 👋

Luca

### 🐦 Linkedin / Twitter
