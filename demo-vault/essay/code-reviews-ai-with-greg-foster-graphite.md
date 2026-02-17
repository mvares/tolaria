---
aliases:
  - "Code Reviews & AI — with Greg Foster (Graphite)"
"✏️ Status": Not started
"Belongs to":
  - "[[responsibility/publish-podcast|Publish Podcast]]"
  - "[[person/greg-foster|Greg Foster]]"
Status: Evergreened
URL: "https://refactoring.fm/p/code-reviews-ai-and-modern-engineering?utm_source=publication-search"
"👓 Status": Not started
"Created time": "2024-04-19T10:14:00.000Z"
Date: 2024-07-05
"Has Notes": "[[evergreen/if-you-use-staging-do-automatic-promotion|If you use Staging, do automatic promotion]]"
Tags:
  - Podcast
  - Free
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: e2f00330-861b-4316-9ee7-e2255c8c41c9
---

# Code Reviews & AI — with Greg Foster (Graphite)

Today's guest is XXXX 

XXX is bla bla

With XXX we talked about

### 🎙️ Episode

You can watch the full episode on [Youtube](https://www.youtube.com/@refactoringclub):

Or listen to it on [Spotify](https://open.spotify.com/show/7Luds9dmzZDoDC8Q7EMbSw), [Apple](https://podcasts.apple.com/us/podcast/refactoring-podcast/id1719137305), [Overcast](https://overcast.fm/itunes1719137305), or your podcast app of choice.

---

### 🥇 Interview Summary

If you are a **🔒 paid subscriber 🔒** you will find *my own**** ****summary* of the interview below.

It’s the **10-minute, handcrafted takeaways** of what we talked about, with timestamps to the relevant video moments, for those who don’t have time to sit through the 1-hour chat.

Here is the agenda for today:

1. **🔍 Graphite and stacked changes** ([01:07](https://www.youtube.com/watch?v=tpuK4n-dClI&t=67s))

1. **📊 Code review best practices** ([17:41](https://www.youtube.com/watch?v=tpuK4n-dClI&t=1061s))

1. **🤖 AI's impact on software development** ([29:22](https://www.youtube.com/watch?v=tpuK4n-dClI&t=1762s))

1. **👨‍💻 Graphite's engineering team** ([41:05](https://www.youtube.com/watch?v=tpuK4n-dClI&t=2465s))

1. **🚀 Deployment and staging practices** ([47:32](https://www.youtube.com/watch?v=tpuK4n-dClI&t=2852s))

⠀Let's dive in 👇

---

### **1) 🔍 Graphite and stacked changes (**[**01:07**](https://www.youtube.com/watch?v=tpuK4n-dClI&t=67s)**)**

Greg Foster explains that Graphite is a code change collaboration tool that works on top of GitHub. Its main goal is to help teams create, review, and merge code changes more efficiently.

Greg also provides a **historical perspective** on engineering practices, highlighting a continuous trend towards faster and smaller code changes.

This evolution includes at least three steps:

1. **1980s** — annual software release cycles with in-person code reviews.

1. **2000s** — introduction of Git and pull requests.

1. **Today** — need for even faster and smaller code changes

Graphite aims to continue this trend by enabling developers to break down work into so-called **stacked changes**. Stacked changes have been used by big tech companies like Google, Facebook, and Uber, for a long time through custom tooling, as they offer several advantages:

- **🏃‍♂️ Unblock engineers** — they allow engineers to continue working on code without becoming blocked by reviews.

- **🏅 Improved quality** — they split in smaller batches, which improves the quality of reviews.

- **↩️ Easier rollbacks** — they make it easier to debug and possibly rollback because even large changes are treated as a collection of smaller ones.

While this workflow is also possible without specialized tools, it easily becomes cumbersome. Graphite aims to make this process seamless for teams using GitHub.

After this intro, we moved to discuss code review best practices 👇

---

### **2) 📖 Code review best practices (**[**17:41**](https://www.youtube.com/watch?v=tpuK4n-dClI&t=1061s)**)**

I have written a recent, [opinionated piece about code reviews](https://refactoring.fm/p/thoughts-on-code-reviews), and I discussed many of its points with Greg.

Here is what he told me:

#### **Purpose of code reviews 🎯**

For Greg, code reviews serve multiple purposes:

- 🔒 **Security** — ensuring multiple eyes on each change

- 📚 **Knowledge sharing** — keeping the team informed about codebase evolution

- 🟰 **Consistency** — maintaining coding standards and practices

- 🐛 **Bug catching** — though not the primary focus, reviews can catch some issues before they hit prod.

However, Greg notes that with modern testing and monitoring practices, bug detection has shifted away from being a primary focus of code reviews.

#### **Keeping changes small 🤏**

Greg stresses that the most common mistake teams make with code reviews is submitting overly large code changes.

This has been **studied extensively** — there exist Google research papers from over 15 years ago that have consistently shown how smaller code changes benefit almost every aspect of the dev process.

#### **Balancing sync and async reviews 🔀**

While async reviews are common, Greg acknowledges that sometimes sync discussions are necessary.

His rule of thumb is to use sync reviews when there would be extensive back-and-forth otherwise.

---

### **3) 🤖 AI's impact on software development (**[**29:22**](https://www.youtube.com/watch?v=tpuK4n-dClI&t=1762s)**)**

We spent a lot of time discussing the growing influence of AI in software development. Here are the trends that Greg is clearly seeing:

- **📈 Increased code production **— with tools like GitHub Copilot, engineers are producing more code than ever before. This increase in volume puts strain on other parts of the development process, including code reviews, CI systems, and deployment pipelines.

- **🔍 Renewed importance of human reviews **— despite AI capabilities, Greg emphasizes that human reviews remain crucial for security, understanding, and catching the subtle bugs that AI-generated code introduces.

- **🧱 AI as an augmentation tool **— Greg sees AI not as a replacement for human developers, but as an enhancement. It is invaluable in 1) helping with routine tasks, and 2) assisting in summarization and context-gathering for reviews.

As AI handles more routine coding tasks, Greg predicts humans will move more and more to taking care of the bigger picture, like architecture, modularization, and system design.

This shift might pose **challenges for junior developers**, as entry-level tasks become more automated.

---

### **4) 👨‍💻 Graphite's engineering team (**[**41:05**](https://www.youtube.com/watch?v=tpuK4n-dClI&t=2465s)**)**

Greg shares insights into Graphite's team structure and culture.

Here is what the team looks like:

- About 22 people total, with roughly half being engineers

- Based in New York City, working in-person five days a week

- Emphasis on hiring senior to staff-level engineers

Even non-engineering roles require strong technical understanding due to the nature of Graphite's product. The team heavily *dogfoods* their own tool, using it for hours every day.

Being only ~20 people, the structure is completely flat. Greg is the only person acting as engineering manager, and high autonomy is given to individual contributors.

Graphite also has an extremely clear **product philosophy**. They don’t want to *replace *existing tools, but rather play nicely with them. Graphite syncs perfectly with GitHub, allowing users to fall back to GitHub at any time.

This is often challenging and sets a high bar for the product's quality and user experience.

---

### **5) 🚀 Deployment and staging practices (**[**47:32**](https://www.youtube.com/watch?v=tpuK4n-dClI&t=2852s)**)**

Greg details Graphite's approach to deployment and staging.

Here is a TL;DR:

1. They use a monorepo

1. They deploy via AWS CodePipeline

1. They use a high-quality staging environment

1. They have an automated merge queue for releases

More details 👇

#### **Staging environment 🖥️**

Graphite maintains a full replica of their infrastructure in a separate AWS account for staging:

- The entire Graphite team uses this staging environment for daily work

- There is one-hour lag time before promoting to production, which happens automatically

Greg says staging works well for them because they don’t have a lot of user-generated content, so the environment can be extremely close to what prod looks like.

#### **Automated promotion ⬆️**

Unlike some companies that require manual approval for staging deployments, Graphite, instead, completely automates the process.

It gives engineers **one hour to check changes on staging**, before they are automatically released in prod. This reduces bottlenecks in the deployment pipeline, and ensures consistent traffic and usage in the staging environment.

---

### 🙏 Thank you

Thank you so much for reading & listening! Let me know what you think about the podcast and the brand new summaries in the comments or via email!

We just got started with the Podcast, so if you found this chat valuable, please consider **subscribing to the show** on [YouTube](https://www.youtube.com/@refactoringclub), [Apple](https://podcasts.apple.com/us/podcast/refactoring-podcast/id1719137305), or [Spotify](https://open.spotify.com/show/7Luds9dmzZDoDC8Q7EMbSw).

Also, consider **giving us a rating** or leaving a review on the platform of your choice, as that really helps other listeners find the show.

See you next week! 👋

Luca

---

### 🙏 Thank you

Thank you so much for reading & listening! Let me know what you think about the podcast and the brand new summaries in the comments or via email!

We just got started with the Podcast, so if you found this chat valuable, please consider **subscribing to the show** on [YouTube](https://www.youtube.com/@refactoringclub), [Apple](https://podcasts.apple.com/us/podcast/refactoring-podcast/id1719137305), or [Spotify](https://open.spotify.com/show/7Luds9dmzZDoDC8Q7EMbSw).

Also, consider **giving us a rating** or leaving a review on the platform of your choice, as that really helps other listeners find the show.

See you next week! 👋

Luca

### 🐦 Linkedin / Twitter
