---
aliases:
  - "Monday #44"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-monday-idea|Publish Monday Idea]]"
Status: Published
"👓 Status": Not started
"Created time": "2024-04-18T15:09:00.000Z"
Date: 2023-04-03
"Has Notes":
  - "[[evergreen/hierarchies-are-useful-to-scale-comms|Hierarchies are useful to scale comms]]"
  - "[[evergreen/sqca-framework-pyramid-principle|SQCA Framework + Pyramid principle]]"
  - "[[evergreen/ai-coding-freshness-problem|AI coding freshness problem]]"
Tags:
  - Monday
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 62438c2e-becf-4a8f-a88c-0ce924bf5e55
---

# Monday #44

*Hey, *[*Luca*](https://twitter.com/lucaronin)* here! welcome to the ****Monday 3-2-1 ****✨*

*Every Monday I will send you an email like this with ****3 short ideas**** about engineering management, technical strategy, and good hiring.*

*You will also receive the regular long-form one on Thursday, like the last one:*

- [**Refactoring Quarterly Update! 📣**](https://refactoring.fm/p/refactoring-quarterly-update)

*To receive all the full articles and support Refactoring, consider subscribing if you haven’t already!*

Become a better tech leader today ✨

[https://refactoring.substack.com/subscribe](https://refactoring.substack.com/subscribe)?

*p.s. you can learn more about the *[*benefits of the paid plan here*](http://refactoring.fm/about)*.*

---

![image](../assets/aa347d6c8dd04081.png)

---

### 1) 🔺 The Pyramid Principle

One of the most influential works about structuring effective communication is [The Minto Pyramid Principle](https://www.goodreads.com/book/show/33206.The_Minto_Pyramid_Principle), by Barbara Minto. 

In her book, she introduces the **SCQA framework** for presenting ideas in a way that captures the recipient’s attention and increases the chances they understand them. Each idea should be organized into four sections:

1. **Situation** — the context, or the status quo.

1. **Complication **— a change or a problem in the current situation which makes this communication necessary.

1. **Question** — the main problem statement.

1. **Answer **— your best answer to the posed question, or the process to put in place to get such answer.

At this point, you typically need to support your proposed answer with arguments and ideas. Such ideas should form a *pyramid* under a single thought, which is the answer you propose.

![The SCQA + Pyramid Principle, summarized.](../assets/2260c9dc5faf4934.png)

Below that, you should summarize and group the next level of supporting arguments. So, the Pyramid Principle is based on three key concepts:

1. **Start with the answer first** — most people think better in a top-down fashion. Start with the answer and present supporting ideas later.  

1. **Summarize and group supporting arguments **— force yourself to limit the number of arguments you propose, by grouping them and focusing on the main ones. Minto suggests the [Rule of Three](https://medium.com/lessons-from-mckinsey/the-rule-of-3-c1cd82dbc96e).

1. **Logically order your supporting ideas **— make sure that the ideas you bring together under each group actually belong together, are at the same level of importance, and follow some logical structure.

More ideas and examples on how to improve your communication skills 👇

[https://refactoring.fm/p/how-to-improve-your-communication](https://refactoring.fm/p/how-to-improve-your-communication)

---

### 2)  🤖 AI & Freshness

I am very excited about using AI to write code. One thing I am worried about, though, is freshness.

A few weeks ago I asked ChatGPT to create a Telegram Bot, written in Node.js.

![image](../assets/860fd1dcd93e4b85.png)

After generating the code, I asked it to use the Serverless framework to turn it into a function that I could easily deploy on AWS.

Amazingly enough, it did it.

The code works, but there are two problems:

1. It uses the old way of handling the function—with the callback—while the recommended way today uses the async / await syntax.

1. It uses the deprecated "on" method for the Telegram Bot, instead of the new filter utils.

This likely happens because you can find way more examples online with these methods than with the new ones, as the former have been around for longer.

This *freshness* problem worries me for two reasons:

1. **I have no way of detecting it** — sure, you can ask the AI to rewrite the code in the new way, but you have to know it first.

1. **It feels intrinsic to how AI works** — the model is trained on data, so it is always going to favor stuff for which it has the most of it.

I wonder whether, in the future, new frameworks will have a tougher adoption curve because people will just stick with the ones where the AI is best.

More reflections on AI and coding:

[https://refactoring.fm/p/ai-future-of-coding](https://refactoring.fm/p/ai-future-of-coding)

---

### 3) 🏰 Hierarchy scales communication

As long as your team is small, there isn’t much need for a formal organization — 5 to 10 people can work pretty well without structure.

The main problem, when teams grow larger, is **communication**. Large teams have a hard time keeping people on the same page, allocating resources, and making good, participated decisions.

As you grow, these problems seem to get worse **gradually** at first, and then **suddenly**. Why?

As by [Metcalfe’s Law](https://en.wikipedia.org/wiki/Metcalfe%27s_law), the complexity of communication is proportional to the *square* of the number of users involved. So, while people grow linearly, complexity grows geometrically.

To tame communication complexity, companies usually introduce **hierarchies**. Hierarchies have many advantages:

- They provide clear communication paths, ensuring **alignment** across the org.

- They reduce the number of *lines* each person has to manage, allowing the company to **scale**.

- They provide a simple way for **making decisions**, by assigning clear responsibilities.

Same 7-people team, different configurations 👇

![image](../assets/ac348de876774481.png)

Hierarchy, however, also brings drawbacks:

- **Overhead** — communication has a longer way to travel to a destination, which makes you slower. Longer paths also create all kinds of “work’s work”, like traffic controlling, managing up, presentations, and more.

- **Inflexibility** — once in place, it is hard to reconfigure roles and processes. This in turn reduces agility, resilience to turnover, and velocity, too.

There are companies who successfully scaled *without* introducing hierarchies. I wrote a two-part series about them 👇

[https://refactoring.fm/p/unusual-teams-1](https://refactoring.fm/p/unusual-teams-1)

### 💼 Are you hiring engineers?

In 2+ years of Refactoring and with 30K+ subscribers, I routinely get asked for help about hiring. I always do my best and over time I helped tens of companies to hire probably 100+ engineers.

If you are hiring developers, I can probably help. Feel free to reach out by replying to this email, or DM me anywhere. 

---

And that’s it for today! If you are finding this newsletter valuable, consider doing any of these:

**1) ✉️ Subscribe to the newsletter** — if you aren’t already, consider becoming a paid subscriber. You can learn more about the [benefits of the paid plan here](http://refactoring.fm/about).

Get full access to Refactoring today ✨

[https://refactoring.substack.com/subscribe](https://refactoring.substack.com/subscribe)?

**2)** ❤️ **Share it** — Refactoring lives thanks to word of mouth. Share the article with your team or with someone to whom it might be useful!

I wish you a great week! ☀️

Luca
