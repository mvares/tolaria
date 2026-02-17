---
aliases:
  - "Interview with DHH"
"✏️ Status": Not started
"Belongs to":
  - "[[responsibility/publish-podcast|Publish Podcast]]"
  - "[[person/dhh|DHH]]"
Status: Evergreened
URL: "https://refactoring.fm/p/merchants-of-complexity-with-dhh"
"👓 Status": Not started
"Created time": "2024-09-05T08:08:00.000Z"
Date: 2024-09-06
"Has Notes": "[[evergreen/merchants-of-complexity|Merchants of complexity]]"
Tags:
  - Podcast
  - Free
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 9f15bbed-d0ea-48c5-82f8-d015e2bdf53a
---

# Interview with DHH

Today's guest is **David Heinemeier Hansson!**

David needs no introduction: he is the creator of Rails, co-founder & CTO of Basecamp, a NYT bestselling author, and professional racing driver for 10+ years.

In our chat, we explored David's opinions on the current state of software development, including excessive complexity in software and infrastructure, the role of AI, and the future of open source.
We also talked about his racing and how he approaches learning any topic from scratch.

### 🎙️ Episode

You can watch the full episode on [Youtube](https://www.youtube.com/@refactoringclub):

Or listen to it on [Spotify](https://open.spotify.com/show/7Luds9dmzZDoDC8Q7EMbSw), [Apple](https://podcasts.apple.com/us/podcast/refactoring-podcast/id1719137305), [Overcast](https://overcast.fm/itunes1719137305), or your podcast app of choice.

---

### 🥇 Interview Summary

If you are a **🔒 paid subscriber 🔒** you will find *my own**** ****summary* of the interview below.

It’s the **10-minute, handcrafted takeaways** of what we talked about, with timestamps to the relevant video moments, for those who don’t have time to sit through the 1-hour chat.

Here is the agenda for today:

1. 🏗️ **Merchants of complexity**

1. **🧩 Compressing vs layering complexity**

1. **🤖 AI in software development**

1. **🏎️ Learning and racing**

Let's dive in 👇

---

### 1) 🏗️ Merchants of complexity

David opens the interview by discussing the concept of "merchants of complexity" in the software industry, which he wrote about in a [recent blog post](https://world.hey.com/dhh/merchants-of-complexity-4851301b).

He argues that companies that profit from complicated layering have an incentive to maintain it. This creates a conflict between simplifying software and sustaining a business model based on such complexity.

This is why—David explains—he never commercialized his work on Rails:

> *I knew that I could have all these noble ideals about how we should build software and we should keep it simple and we should compress complexity instead of layering it away. And I'd go like, all that would eventually disappear because the incentives of needing to sustain and grow a business would overwhelm that.*

By keeping Rails as an open-source project, separate from his commercial ventures, David can maintain his focus on simplicity and complexity *compression*, without the pressure to monetize the framework directly.

---

### 2) 🧩 Compressing vs layering complexity ([03:24](https://www.youtube.com/watch?v=tWduT9ygUQ4&t=204s))

David elaborates on his approach to dealing with complexity in software development:

#### The goal: empowering individual developers

David aims to create tools and approaches that allow a single developer to build a competitive business online. This contrasts with the trend of requiring large teams of specialists to build modern applications.

#### Compressing complexity

So, instead of adding layers that hide complexity, David focuses on *compressing* it. The idea is to keep developers in contact with the actual problem, while still reducing their cognitive load:

> *I want to compress complexity, but retain it so you have a connection to it, just so you can fit more, and then enable a single developer to be completely competitive and capable of building an entire system that they can bootstrap a business around.*

#### Example: ActiveRecord

David uses ActiveRecord, the ORM in Rails, as an example of complexity compression:

1. It doesn't hide SQL completely but makes common operations easier

1. Developers still need to understand databases for advanced use cases

This approach contrasts with most ORMs, that try to abstract away SQL entirely.

#### Infrastructure complexity

David especially criticizes the trend of adding layers to simplify infrastructure management.

Many developers today feel that server management is outside their realm, in part because of overblown solutions like Kubernetes, which often end up more complicated than the original problem.

David advocates for understanding fundamentals like Linux and server management, which less hard than they seem, and would empower developers with timeless knowledge 👇

#### Investing in timeless knowledge

David encourages developers to invest in learning fundamental, long-lasting technologies. E.g. understanding SQL, Linux, and server basics pays dividends over decades.

This contrasts, for example, with constantly changing frontend frameworks. Rails is designed to provide long-term value, with core concepts remaining stable over time.

---

### 3) 🤖 AI in software development ([35:10](https://www.youtube.com/watch?v=tWduT9ygUQ4&t=2110s))

David shares his thoughts on the role of AI in coding and its impact on the future of software development.

#### David’s use of AI

David uses AI as a "*non-driving pair programmer*" — he regularly consults an LLM while coding, similar to asking a human pair programmer.

This approach is helpful for quick questions about APIs or specific tasks, while still keeping him in control.

#### The risk of muscle atrophy

While finding AI helpful, David warns about the potential for skill degradation:

> *It is a very fine line before it is actively eroding your own muscles. It's sort of jumping into an exoskeleton and you go like oh man I have superhuman power but the more you use that exoskeleton and not your own muscles the more those muscles atrophy.*

He noticed this effect while working on [Omakub](https://omakub.org/), his Ubuntu remix project: AI helped him write Bash scripts quickly, but he also found himself repeatedly looking up the same information. This raised concerns about whether he was truly *learning* and internalizing the knowledge.

#### The future of AI in programming

David is uncertain about the long-term impact of AI on programming.

He acknowledges the incredible empowerment for non-technical folks — we discussed the amazing video of an 8-year-old creating a Harry Potter chatbot — however, he questions whether complete AI-driven development is desirable.

There is joy in programming, like in playing an instrument, and that joy is in the process itself. While AI can make us more efficient, it could fail to make us happier.

#### Hype cycles and realistic expectations

David draws parallels between AI hype and previous technological predictions:

- Self-driving cars in 2017

- Virtual reality in the 1990s

- General AI predictions in the 1950s

He suggests that while AI will certainly advance, it's difficult to predict its exact trajectory, and right now we very well may be at the peak of inflated expectations.

---

### 4) 🏎️ Learning and racing ([49:48](https://www.youtube.com/watch?v=tWduT9ygUQ4&t=2988s))

I asked David about his racing career, and how he managed to learn a skill so different from his main job, up to the highest professional level, in his spare time.

#### Universal learning

David applies the same learning techniques across different domains:

- Identify and appreciate good examples in the field

- Develop an eye for quality and understand why something is considered good

- Start by copying and recreating work from experts

- Focus on mastering fundamentals before attempting creative innovations

This was exactly how he learned racing 👇

#### Racing-specific approach

In the context of racing, David's learning process involves:

- Seeking out professional racers and comparing data overlays

- Analyzing throttle, braking, and other technical aspects of their performance

- Identifying what matters most in each phase of driving

- Building up skills by replicating expert techniques

#### The beginner's mindset

To successfully learn new things, you should “*embrace the suck*”, or, more poetically, adopt a beginner’s mindset:

- Embrace that you're initially incompetent in a new field

- Be open to learning from those with more experience

- Avoid the trap of feeling satisfied with basic competence

#### Setting high standards

David advocates for comparing oneself to the best in the world:

> *"I'm not interested in being the fastest racer at my local track. That doesn't do anything for me. Quite early in my racing career, I was like, I want to race at Le Mans."*

This approach keeps him in a constant learning mindset and pushes him to improve continuously.

---

### 🙏 Thank you

Thank you so much for reading & listening! Let me know what you think about the podcast and the brand new summaries in the comments or via email!

We just got started with the Podcast, so if you found this chat valuable, please consider **subscribing to the show** on [YouTube](https://www.youtube.com/@refactoringclub), [Apple](https://podcasts.apple.com/us/podcast/refactoring-podcast/id1719137305), or [Spotify](https://open.spotify.com/show/7Luds9dmzZDoDC8Q7EMbSw).

Also, consider **giving us a rating** or leaving a review on the platform of your choice, as that really helps other listeners find the show.

See you next week! 👋

Luca

### 🐦 Linkedin / Twitter
