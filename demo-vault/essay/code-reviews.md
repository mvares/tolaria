---
aliases:
  - "Code Reviews"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-essays|Publish Essays →]]"
Status: Evergreened
URL: "https://refactoring.fm/p/code-reviews"
"👓 Status": Not started
"Created time": "2024-04-18T14:53:00.000Z"
Date: 2021-12-23
"Has Notes":
  - "[[Ship/Show/Ask framework]]"
  - "[[evergreen/use-stacked-diffs-and-trunk-based-dev-to-improve-velocity|Use stacked-diffs and trunk-based dev to improve velocity]]"
  - "[[evergreen/reviewing-code-as-soon-as-possible-improves-velocity|Reviewing code as soon as possible improves velocity]]"
  - "[[evergreen/make-code-reviews-faster-by-automating-parts-of-the-reviewer-job|Make code reviews faster by automating parts of the reviewer job]]"
  - "[[evergreen/small-prs-improve-speed-and-quality-of-code-reviews|Small PRs improve speed and quality of code reviews]]"
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 3150ff49-9b9c-4637-9824-bacbb92e63f5
---

# Code Reviews

### 📑 Materials

---

- [Untitled](https://www.notion.so/bc67a0c1b84d423eb97d1a37389d9722) 

- LGTM meme

- [Code Review Comments](https://github.com/golang/go/wiki/CodeReviewComments)

- [Those Pesky Pull Request Reviews](https://jessitron.com/2021/03/27/those-pesky-pull-request-reviews/)

- [Code Reviews (Synchronous and Asynchronous)](https://www.eferro.net/2021/09/code-reviews-synchronous-and.html)

- [Ship / Show / Ask](https://martinfowler.com/articles/ship-show-ask.html)

- [Stacked Diffs vs Pull Requests](https://jg.gg/2018/09/29/stacked-diffs-versus-pull-requests/)

- [Stacked Changes: how Facebook and Google engineers stay unblocked and ship faster](https://graphite.dev/blog/post/DThX8ffP1gmxWJChEv0y)

- [Untitled](https://www.notion.so/58cd472e8ca742f6a55bf31555e0198c) 

### ✍️ Post

---

Shipping fast and often is the #1 element shared by top performing engineering teams.

Elite teams release multiple times a day, and it takes less than one hour to go from code committed to code successfully running in production.

This idea was made popular in 2018 by the [Accelerate](https://www.goodreads.com/en/book/show/35747076-accelerate) book — a thorough research that convincingly linked good business results to good DevOps metrics.

I also wrote about this in these past articles:

- [**Shipping Fast Changes Your Life**](https://refactoring.fm/p/how-shipping-fast-changes-your-life)** **⚡

- [**The Four Measures of Software Delivery Performance**](https://refactoring.fm/p/the-four-measures-of-software-delivery) 🚚

Three years after Accelerate, this is even more true. As highlighted in the recent [State of DevOps](https://services.google.com/fh/files/misc/state-of-devops-2021.pdf), by Google, the share of "elite teams" jumped from 7% in 2018, to 26% in 2021.

How is this related to code reviews? 👇

### 🔍 Code Review

The code review is the process of having one developer (or more) review another developer's code before release.

Code reviews have two main goals: 

1. **Improve the quality of code before being released**

1. **Share knowledge across the team**

These are both crucial goals. Better quality translates into less failures and less maintenance down the line. Sharing knowledge makes teams more resilient and engineers grow faster. 

This has been proven time after time, but still, in this need for speed, reviews are one of the **biggest offenders**.

When you think about it, we may work hard to shave **5 to 10 minutes** off our deploy pipeline, and then we may add **hours** of delay as the code is stuck in review.

For this reason, the whole process is still a somewhat controversial topic, with many proposals to make it better.

These proposals are not necessarily at odds with the two main goals. I am a strong proponent of good code reviews, but I also believe the standard PR process is **wildly inefficient**.

This article is about how we can optimize reviews and PRs to be as fast as possible, without compromising on quality and knowledge sharing.

It includes:

- 🗺️ **Tactics** — practical advice on how to improve your code review process.

- 📋 **Guidelines** — how elite companies like Google, Yelp, and GitLab do code reviews.

- 🔨 **Tools **— to help you make faster and better reviews.

- 📚 **Readings** — the best articles I know about code reviews.

Let’s go 👇

### 🗺️ Tactics

Here are six actionable tactics you can use to do good reviews, faster. As you will see, they are more about the *process* than the review itself.  

#### 1) Keep them small

Doing small PRs is one of the best ways to have a short turnaround. 

How small? In my experience, if you break down work properly, 90% of the times you can issue PRs that are less than 200 lines of code.

You can go even further: [at Google, 90% of code changes are <24 lines of code](https://www.michaelagreiler.com/code-reviews-at-google/).

Small PRs improve both speed and quality:

- **Speed** —** **reviewer needs to block a smaller time to review it, so they are more likely to being able to do it sooner.

- **Quality **—** **fewer lines of code means the change is easier to understand, which leads to better reviews.

[Embed](https://twitter.com/iamdevloper/status/397664295875805184?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E397664295875805184%7Ctwgr%5E%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fgraphite.dev%2Fblog%2Fpost%2FDThX8ffP1gmxWJChEv0y)

#### 2) Do them as soon as possible

Even if you want code reviews to be asynchronous, you should be adamant about doing them as soon as possible.

When the code is stuck for several hours (or days!), the developer needs to switch to something else while they wait for it — and when the review is ready, they need to context switch again to make changes or fix bugs.

This leads to cascading delays that ultimately have a strong impact on your velocity.

[Embed](https://twitter.com/jlongster/status/1400511441556459523)

Here are two ways you can help your team have a short review turnaround:

- 🎯 **Set goals** —  analytics tools like [Waydev](https://waydev.co/) and [LinearB](https://linearb.io/) help you discover how long it takes for your team to review code. Use them to assess your current situation, set improvement goals and discuss them in reviews and retros.

- 🚨 **Set notifications** — simple notifications go a long way. Tools like [LinearB](https://linearb.io/) or [Botany](https://botany.io/) can notify developers when a review is required on their side. We made an experiment with [Pull Panda](https://pullpanda.com/) (now retired 😢) years ago and it *halved* our review time.

#### 3) Automate parts of the review

Make the reviewer do less work by automating part of their job. A few ways:

- **Include Tests **— comprehensive tests make the code more comprehensible, replicable, and can vastly reduce reviewer’s work.

- **Apply Linting **— perform static analysis automatically in your CI pipeline, so reviewers can spare themselves stylistic errors, suspicious constructs, etc.

- **Have a list common mistakes **— create a space in your docs to write down common comments made during reviews, so the reviewer can point to them instead of giving detailed explanations every time. Here is one such document created by the Golang team: [Code Review Comments](https://github.com/golang/go/wiki/CodeReviewComments).

#### 4) Use s**tacked diffs and trunk-based development**

Many big companies like Facebook and Google have a code review workflow that is not based on PRs, but rather on **stacked diffs**.

[Embed](https://twitter.com/dan_abramov/status/1407803004183531527?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1407803004183531527%7Ctwgr%5E%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fgraphite.dev%2Fblog%2Fpost%2FDThX8ffP1gmxWJChEv0y)

Stacked diffs are a way to have your code reviewed *without* firing up a PR. You take a portion of your local changes and make it available for review. You can *stack* these changes into multiple requests for review, so you never get stuck waiting for reviews.

[Embed](https://twitter.com/alexandracoding/status/1278001790907285508?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1278001790907285508%7Ctwgr%5E%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fgraphite.dev%2Fblog%2Fpost%2FDThX8ffP1gmxWJChEv0y)

This workflow, other than being faster, allows to (mostly) get rid of branches and work in [trunk-based development](https://cloud.google.com/architecture/devops/devops-tech-trunk-based-development) mode instead. In turn, there is convincing evidence that teams who adopt trunk-based workflows achieve higher velocity and faster turnaround.

[Embed](https://twitter.com/jezhumble/status/1415908836439773185)

If this seems crazy to you, you may reflect on the fact that engineers working in some of the best companies in the world commit directly to master all the time (and often on a monorepo), unless they have a reason not to.

The bad news is that to make this workflow happen you need some tooling, and unfortunately there isn’t much today. Here are the two main things you can try:

- [**Phabricator**](https://www.phacility.com/)** **— originally developed as an internal tool at Facebook, it became an open source project but as of today it is no longer maintained (you can still self-host it and use it). There is a community attempt to maintain it at [Phorge](https://we.phorge.it/), but its future is unclear.

- [**Graphite**](https://graphite.dev/)** **— a new, promising tool that implements the stacked diffs workflow. As of today you can join the waitlist ¯\_(ツ)_/¯.

If you want to learn more about stacked diffs and trunk-based dev, check out these articles:

- 📑 [**Stacked Diffs vs Pull Requests**](https://jg.gg/2018/09/29/stacked-diffs-versus-pull-requests/)** **— by Jackson Gabbard

- 📑 [**DevOps tech: Trunk-based development**](https://cloud.google.com/architecture/devops/devops-tech-trunk-based-development)** **— by Google

#### 5) Consider the Ship / Show / Ask framework

If code reviews are about 1) improving quality, and 2) sharing knowledge, should they be always required? Do *all* changes have room for improvement, or bring new knowledge to share?

[**Rouan Wilsenach**](https://www.rouanw.com/)** **argues you are better off adopting the **Ship / Show / Ask** framework, which considers three cases:

- 🚢 **Ship **— You make the change directly on your mainline, without asking for a code review. This works when you fix unremarkable bugs, add features using established patterns, or do collateral changes like improving docs.

- 🔍 **Show **— You create a PR (run all the CI pipeline), merge it without anyone’s approval, and *then *ask for feedback. This way you release quickly but still create space for discussion. It works in situations where you want to share knowledge but don’t necessarily need feedback, or the feedback is valuable but shouldn’t be blocking.  

- ❓ **Ask **— You make changes on a branch, open a PR and wait for the review before merging. This is the standard process most companies adopt nowadays.

This framework is about choosing every time what is the best strategy, based on the type of change you are making. It encourages active reflection instead of adopting always the same pattern.

![image](../assets/909294bc6be84c6f.png)

In my professional life I have pretty much always worked in “Ask” mode. If you ask my take, I wouldn’t be comfortable with the “Ship” mode unless we are talking of really small, negligible changes. However, I see how the “Show” pattern might be a good way to get the best of both worlds in many scenarios.

#### 6) Do Pair Programming 

Pair programming completely removes the need for code reviews. When you pair, your code is automatically reviewed by your partner, and it can be merged as soon as it’s done.

This also fixes the paradoxical problem that the more engineers are *conscientious* about code reviews, the more they end up despising them 👇

> "*Reviews, done right, have all the painful parts of a software change: understanding what the change is for, loading up the relevant code and tests into working memory, getting my local environment up to see the change, making the tests run. They have none of the fun parts: refactoring to clarity, changing code and seeing a difference. They take hours of time and all my concentration away from whatever it is that I’m personally trying to do*" — [Chelsea Troy](https://twitter.com/HeyChelseaTroy)

This is my favorite way of improving the review process. You can also check out my previous article about it: 

- [**Pair Programming**](https://refactoring.fm/p/pair-programming) 👯

#### 7) Write a good PR description

Including a good description goes a long way to help the reviewer understand what’s there and what they should review. 

But what does a good PR description look like?

We had a great discussion about this on the [Refactoring Community](https://refactoring.fm/p/community) in the last few days. Here are a few contributions 👇

> *I would say that our approach is very simple:
– A summary of what the CR is about.
– A testing summary on how and what was tested
It all should be linked to your project story/task. If the story task is small enough the CR should be proportionate to it.
IMHO if the CRs are getting too big probably the problem is on the story/task breakdown.*

– [Roberto](https://twitter.com/robansuini), Engineering Manager at Amazon

> *We write very small stories so the PRs are self-explanatory. In addition we try to apply pair programming to almost every story.*

– [Pasqualino](https://www.linkedin.com/in/pasqualinosorice/), CTO at MioAssicuratore

> *Actually used custom templates with checklists for PRs (and tickets) as well. Biggest benefit I saw from this as soon as devs get familiar with it is robustness and code quality. By having to tick off a box, there was a sense of responsibility to fulfil the requirements.
*
– [Corvin](https://www.linkedin.com/in/deboeser), Founder at Jaco

> *I tried different approaches, at the end we got good results asking to provide the *[***definition of done***](https://www.agilealliance.org/glossary/definition-of-done/#q=~(infinite~false~filters~(postType~(~%27page~%27post~%27aa_book~%27aa_event_session~%27aa_experience_report~%27aa_glossary~%27aa_research_paper~%27aa_video))~searchTerm~%27~sort~false~sortDirection~%27asc~page~1))*** ****to every ticket. This helps us having the context, the input and the output of the activity. Every task should always be understandable.*

– [Gabriele](https://www.linkedin.com/in/gabrieleproni/), CTO at VoxLoud

### 📋 Guidelines

Here are a few public guidelines from great companies about how they do code reviews:

- **Google** — [Code Review Developer Guide](https://google.github.io/eng-practices/review/). A thorough guide that includes links to further docs to deep dive.

- **Yelp** — [Code Review Guidelines](https://engineeringblog.yelp.com/2017/11/code-review-guidelines.html). Great guide that includes both instructions on how to actually review code, and on how to optimize the whole process.

- **GitLab** — [Code Review Guidelines](https://about.gitlab.com/handbook/engineering/workflow/code-review/). This is a different take because GitLab is an open source project, which adds tons of complexity. It includes issues like balancing the load on maintainers, how to identify domain experts, and more.

### 🔨 Tools

Here are a few tools that can help you improve your review process.

- [LinearB](https://linearb.io/workflow-optimization/) — it improves your dev process by sending you updates and notifications about things you should do, including code reviews. Also, if you are a premium subscriber of Refactoring you get a nice deal!

![image](../assets/7b0d4a0dc81940f9.png)

- [**Graphite**](https://graphite.dev/)** **— up and coming tool that allows you to adopt the *stacked diffs* workflow for your reviews. Right now you can only join the waitlist, but videos are very promising.

- [**Waydev**](https://waydev.co/) — gives you plenty of analytics about your dev process, including code reviews. It helps you identify bottlenecks and speed up the process. If you are a premium subscriber, check it out in the deals section!

### 📚 Readings

- 📑 [**Code Reviews (Synchronous and Asynchronous)**](https://www.eferro.net/2021/09/code-reviews-synchronous-and.html)** **— in this great article, that I referenced also last week, Eduardo Ferro describes different kinds of code reviews, with upsides and downsides.

- 📑 [**Stacked Diffs vs Pull Requests**](https://jg.gg/2018/09/29/stacked-diffs-versus-pull-requests/) — the best article you can find about the famous but elusive “stacked diffs”, and why they should mark an improvement to the regular PR workflow.

- 📑** **[**Ship / Show / Ask**](https://martinfowler.com/articles/ship-show-ask.html) — thought-provoking piece that encourages you to move past dogmatic approaches and reflect on the value of each single review.
