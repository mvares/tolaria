---
aliases:
  - "Pair Programming"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-essays|Publish Essays →]]"
Status: Evergreened
URL: "https://refactoring.fm/p/pair-programming"
"👓 Status": Not started
"Created time": "2024-04-18T14:53:00.000Z"
Date: 2021-12-09
"Has Notes":
  - "[[evergreen/pair-programming-faqs|Pair Programming FAQs]]"
  - "[[evergreen/how-to-plan-for-pair-programming|How to plan for pair programming]]"
  - "[[evergreen/pair-programming-makes-people-happier|Pair programming makes people happier]]"
  - "[[evergreen/pair-programming-is-productive|Pair Programming is productive]]"
  - "[[evergreen/you-should-pair-program-whenever-there-are-decisions-and-learning|You should pair program whenever there are decisions and learning]]"
  - "[[evergreen/pair-programming-makes-remote-better|Pair programming makes remote better]]"
  - "[[evergreen/pair-programming-develops-manager-behaviour|Pair programming develops manager behaviour]]"
  - "[[evergreen/pair-programming-avoids-code-reviews|Pair programming avoids code reviews]]"
  - "[[evergreen/pair-programming-is-counterintuitive|Pair programming is counterintuitive]]"
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: b9c34ff6-6bc5-4fed-aed1-656388134aad
---

# Pair Programming

### 📑 Materials

---

- [**Code Reviews (Synchronous and Asyncronous)**](https://www.eferro.net/2021/09/code-reviews-synchronous-and.html)

- [**Effective Navigation in Pair Programming**](https://www.thoughtworks.com/insights/blog/effective-navigation-in-pair-programming)

- [**Pairing as Pruning**](https://www.facebook.com/notes/390105442009926/)

- [**Productive Pair Programming**](https://www.carlosble.com/2015/07/productive-pair-programming/)

- [**Pairing Guidelines**](https://docs.google.com/document/d/1dGyhrW-2ivwi0iVdmwJoi0-mhRtKOMQp5eBSYkUR0Ek/edit#heading=h.7c4v3ba7mkle)

- [**On Pair Programming**](https://martinfowler.com/articles/on-pair-programming.html)

- [**The Costs and Benefits of Pair Programming**](https://collaboration.csc.ncsu.edu/laurie/Papers/XPSardinia.PDF)

### ✍️ Post

---

There are well-known engineering practices everyone respects, and then there are *secrets*. 

Things that radically change the way you work, provide a strong benefit to your team, yet few companies dare to adopt.

Secrets are hidden in plain sight. They look unappealing and uncomfortable until you discover their power. 

One of such secrets was **remote work**. For about a decade, remote engineering was a prerogative of open source communities and a handful of visionary companies. Then, the pandemic brought it front and center and shifted the conversation completely.

I argue there is another massive secret in engineering today, that is **pair programming**.

Pair programming is the practice of making two engineers work at the same code, at the same time. If they work in an office, they literally sit side by side. If they work from home, they share the screen and do it remotely. 

Pair programming, just like remote work, is counterintuitive. Even more so, it looks bad to all stakeholders:

- 💼 **To managers, it feels like a waste** — it's two devs working on the same code, when they could be doing two separate things.

- 🔨 **To developers, it feels uncomfortable **— social interaction is draining. And what about the sacred *state of flow*?

Nevertheless there exist very successful companies who pair *regularly*, or *most of the time*, or *all the time* even. In some cases, they have been doing so for *decades*, and today they loudly advocate the case for it.

These companies have driven through the waterfall, found a giant cave behind it, and come back to tell the whole story.

This article is my best attempt to shed light on this underused practice, and to give you everything you need to get started:

- 👁️ **Why you should pair program **— a wide range of benefits that includes code quality, productivity, and overall team happiness.

- 📖 **How to pair program **— a detailed process to do it right, standing on the shoulders of companies who have been doing it for decades. 

- ⚖️ **When you should pair program** — let's see if these benefits apply to all kinds of tasks and situations.

- 🗺️ **How to plan for pair programming **— how it changes management and general planning, how to get stakeholders' buy-in, and everything that's beyond programming itself.

- 💻 **Remote pair programming **— pairing is *especially* effective with remote work. Let's discuss the best approaches and the best modern tools to do so.

- 📚 **More articles to deep dive **— case studies, tutorials and scientific research from an all-star cast that includes [Alistair Cockburn](https://twitter.com/totheralistair), [Laurie Williams](https://twitter.com/lauriewilliams), [Martin Fowler](https://twitter.com/martinfowler), [Eduardo Ferro](https://twitter.com/eferro), and more.

Let's dive in 👇

### 👁️ Why you should pair program

Benefits of pair programming can be organized in five main categories:

- 🏃‍♂️ **Productivity**

- 🔍 **Quality**

- 📖 **Knowledge Sharing**

- ❤️ **Happiness**

- 💬 **Manager Behaviour**

Some of these are to be expected, while others are wildly counterintuitive. 

Nevertheless, these elements are all reported pretty much uniformly by companies who adopt this practice, whether they pair regularly ([GitLab](https://about.gitlab.com/blog/2021/02/04/remote-pair-programming-tips/#how-to-get-the-most-out-of-remote-pairing), [GitHub](https://deepcollaboration.simplecast.com/episodes/jason-warner-cto-github)), most of the time ([Thoughtworks](https://martinfowler.com/articles/on-pair-programming.html)), or all the time ([Pivotal](https://review.firstround.com/Why-Every-Startup-Should-Pair-Program)).

Let's see them one by one 👇

#### 🏃‍♂️ Productivity

Let's talk of the elephant in the room. How could it be a productive strategy to assign two developers to the same task?

It turns out it is, for three reasons:

- **Less Distractions **— two people are way less likely to get distracted and lose focus than one. That short trip to facebook doesn't look all that appealing when there is someone else looking at your screen. 

- **More Awareness **— when working for several hours on some problem, you might dig yourself into a rabbit hole and lose the correct perspective of the main task. This is also called [yak shaving](https://codeahoy.com/2017/02/13/yak-shaving-the-less-you-do-the-better/). Remember that time you spent all the afternoon on a bug and then fixed it in 10 minutes the morning after? This wouldn't probably happen in a team of two.

- **No Code Reviews **— this is the factor I like the most: all the code is automatically reviewed. No further PRs to interrupt your productivity. Also, chances are this kind of review is way better than your usual PR.

Based on these elements, in their paper "[The Costs and Benefits of Pair Programming](https://collaboration.csc.ncsu.edu/laurie/Papers/XPSardinia.PDF)", Cockburn and Williams showed how the immediate, *raw output* of a programming pair is only 15% smaller than that of two independent developers.

This 15%, though, is easily repaid down the line by the improved code quality, automatic knowledge sharing, less turnover, and so forth (see chapters below).

#### 🔍 Quality

It shouldn't surprise anyone that pair programming leads to higher code quality. Two people bring better problem solving, that turns into a **better design** overall.

Part of this is due to having a double contribution, and part is simply because two people are more likely to keep their focus and a balanced perspective. As a solo developer, after some time on a task you may develop **tunnel vision** and fixate on implementation details that are not relevant in the bigger picture. Two people always keep each other in check, instead.

#### 📖 Knowledge Sharing

Pair programming is a phenomenal knowledge sharing device. There are at least three use cases that benefit from it:

- **Ownership **— code written this way has two owners out of the box. This makes your team more cohesive, resilient to turnover, and flexible in work allocation. This is a strong benefit that is hard to replicate in any other way.   

- **Onboarding **— pair programming makes onboarding faster. It makes new hires get in touch with your practices, your culture, and it also helps them develop early relationships with peers.

- **Learning **— you may pair people with different skill levels to accelerate the learning process of younger members. This is very effective and hard to obtain in other ways.

#### ❤️ Happiness

One of the most common objections to pair programming is that it is draining due to the continuous social interaction. It is also believed that, being many developers **introverted**, they would come to despise this interaction.

As an introvert myself I can certainly relate, but I also feel this is not 100% correct. While it is true that introverts don't like much interaction, they *do* crave **intimate interactions** with those that are close to their interests.

Pair programming develops **deep relationships** without being socially overwhelming, which is the best possible scenario for an introvert. 

There is no deny that working with a peer is more intense than working by yourself—and we will account for this in the *how to pair program* chapter—but it is not in a way that jeopardizes the whole practice. 

As Cockburn and Williams report in their study:

> *In statistically significant results, pair programming teams who had earlier programmed
alone reported that they enjoyed pair programming more and that they were more confident in their programs than when they programmed alone.*

But *how* more? In an anonymous survey among the same participants, a stunning 80%+ of developers reported they enjoy work *more* because of pair programming.

![image](../assets/cdf619e268db46a5.png)

 

Among the sources of happiness, they cite:

- I find it reassuring to my partner is constantly reviewing my code while I drive

- It’s nice to celebrate with somebody when something works

#### 💬 Manager Behaviour

Pair programming emphasizes communication, giving and receiving constructive feedback, and working together towards a goal.

These skills, in turn, are crucial in all other kinds of situations, from managing people, to mentoring, to negotiating with stakeholders. 

Engineers who pair regularly experience a personal and professional growth that goes way beyond coding.

### ⚖️ When should you pair program?

Once you appreciate the benefits above, this is a legitimate question.

Pair programming is best when it allows you to produce high quality software and share knowledge in the process. For this reason, as [Kent Beck](https://twitter.com/KentBeck) says 👇

> *Pairing works when there is sufficient uncertainty in the problem be solved and the approach to solving it.
— *Kent Beck

Viceversa, pairing doesn't bring much value for mechanical or trivial tasks that both members could accomplish by themselves.

If the work doesn't require taking any decisions, and there is no learning involved, you might as well avoid pairing.

### 📖 How to pair program

Pair programming is different than regular programming in many decisive ways. Let's dive in to understand how to do it right.

![image](../assets/67495548c48f41c9.png)

#### **Driver vs Navigator**

At any given time, when you pair program there is one person who writes code, and one that observes. They are respectively called **Driver** and **Navigator**.

Aside from who actually writes the code, the main difference between the two is:

- The **Driver** keeps the focus on the **current step**.

- The **Navigator** keeps the focus on the **final goal**.

As a driver, you are focused on the task at hand — what to do and how. To help communication, you should learn to think out loud. Talk about what are doing, what you are going to do and how.

As a navigator, you always walk on a fine line as you should at once 1) provide valuable input, but 2) not continuously interrupt the driver's flow. Skilled navigators understand when their partner is ready to listen, and when they are not.

Navigators basically do two things:

- **Brainstorm and discuss** — they discuss design choices and how the task relates to the final goal.

- **Review code **— they spot errors and make suggestions to improve. Just like a regular code review, but in real time.

#### The Session

This is how you can run your pairing session:

- **Set a clear objective **— define the goal of the session. This is crucial as you and your partner will keep each other accountable.

- **Set a time **— how much should the session last? Schedule it in advance to frame it within the rest of each other's work.

- **Work in iterations** — to stay effective, you will need rest. Most companies who pair regularly report using the [pomodoro technique](https://en.wikipedia.org/wiki/Pomodoro_Technique) or equivalent short iterations, followed by periods of rest.

- **Swap driver / navigator **— swap your roles frequently, for example at the end of each iteration. This helps to keep focus and stay productive.

#### Skills levels

The most common pairing setup is between peers. If the driver and navigator have **different skill levels**, instead, be aware you are working in one of two modes:

- **Driver receives knowledge** — you trade productivity in favour of knowledge transmission.

- **Driver has the most knowledge/practice** — you trade knowledge transmission in favour of productivity. This is an opportunity for novices to see more experience fellows “in action”.

Different skill levels doesn't mean one acts as a supervisor for the other. While you pair, you are two peers, even when your respective contribution is not the same. This is crucial to make pairing works, and it is the reason why you should not pair with your actual supervisor.

### 🗺️ How to plan for pair programming

From a management perspective, pair programming is not a transparent practice — you should actively plan for it.

Here is some advice about how to get started:

- **Get buy-in from management **— elaborate on the benefits of pairing, and propose an experiment with limited scope. In my experience, building small success stories is the best way to propagate a practice over time. 

- **Assign couples of developers to tasks **— pair programming implies shared ownership. Assign couples from the beginning to facilitate coordination.

- **Mix up people **— if possible, mix up couples over time. When partners get comfortable with each other they will resist the change. This is healthy as it allows to share more knowledge and keep productivity high.

- **Don't give up **— pairing is a skill that needs to be trained. At the beginning, it will feel uncomfortable. Get constant feedback and iterate over it for at least a couple of months, before drawing some conclusions. 

### 💻 Remote pair programming

A common argument against pair programming is that it doesn't fit well with remote. In particular, it doesn't fit well with two elements:

- **Async work** — remote is about async, so any practice that requires people to work at exactly the same time is bound to be inefficient. 

- **Interaction **— pair programming only works if you are sitting side by side. Otherwise it's just a long, uncomfortable call.

Let's debunk both, and let's start by noting that some of the biggest proponents of pairing, like Thoughtworks, GitLab, and Github, are remote-first companies. 

> In a remote environment, pair programming is one of the best things you can use for two programmers!” - Jason Warner, CTO @ GitHub

This is not casual. Counterintuitively, pair programming makes remote work *better* in many meaningful ways. 

A major fallacy about async work is it implies you should never have meetings or sync collaboration. These are still valuable, it just means you should be mindful of when using one mode or the other.

Pair programming, in particular, enforces accountability and helps you not to get stuck when you face a challenge.

Ronald from GitLab says 👇

> *Working in isolation, without the distractions of the office, is great when you're in the zone. "It works until you run into a difficult problem to solve," says Ronald. "Spending three days on a problem, before getting to the single line of code that solves it, sucks." If you find yourself not making any progress on a challenge, it's probably time to pair.*

Also, remote pairing can make it easier to focus than when pairing on site, because it is easier to avoid distractions with headphones on.

Finally, if the major drawback of remote work is the lack of human connection, pairing makes for a chance to get closer to each other. There are few ways to build meaningful work relationships from remote — pairing is one of these.

### 🔨 Tools for Pair Programming

The best tools to pair today include the following features:

- **Multi-user editing **— all participants can control the editor (or any app) with their mouse and keyboard

- **Simultaneous screen sharing** — all participants can share their screen simultaneously.

- **Strong video & audio** **experience** — this means high quality and low latency.

- **Drawing / highlighting **— being able to draw something on the screen is incredibly useful to highlight sections and explain ideas.

There are a few great tools that have been designed for this specific purpose. These are the best four I know of: 

- [**CoScreen**](https://www.coscreen.co/)

- [**Pop**](https://pop.com/)

- [**Tuple**](https://tuple.app/)

- [**Drovio**](https://www.drovio.com/)

### 📚 Resources

Here are further readings to deep dive on the topic:

- [**On Pair Programming**](https://martinfowler.com/articles/on-pair-programming.html)** **— this article from Thoughtworks is a comprehensive guide on pair programming that covers the benefits, challenges, and everything you need to know. 

- [**The Costs and Benefits of Pair Programming**](https://collaboration.csc.ncsu.edu/laurie/Papers/XPSardinia.PDF)** **— a peer-reviewed paper by Cockburn and Williams about the outstanding impact of pair programming on engineering teams. A must read.

- [**Why Every Startup Should Pair Program**](https://review.firstround.com/Why-Every-Startup-Should-Pair-Program)** **— [Pivotal](https://www.pivotaltracker.com/) team pairs literally all the time. They built an entire culture around it and explained it in this great article.

- [**Code Reviews (Synchronous and Asyncronous)**](https://www.eferro.net/2021/09/code-reviews-synchronous-and.html)** **— Eduardo Ferro explains the impact of pair programming on code reviews. A very insightful read about one of the most important benefits of pairing.
