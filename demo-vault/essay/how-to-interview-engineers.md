---
aliases:
  - "How to Interview Engineers"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-essays|Publish Essays →]]"
Status: Evergreened
URL: "https://refactoring.fm/p/how-to-interview-engineers"
"👓 Status": Not started
"Created time": "2025-02-19T14:26:00.000Z"
Date: 2025-03-05
"Has Notes":
  - "[[evergreen/speed-vs-quality-in-interviews|Speed vs quality in interviews]]"
  - "[[evergreen/select-for-the-unlearnable-skills|Select for the unlearnable skills]]"
  - "[[evergreen/make-interviews-resemble-actual-work|Make interviews resemble actual work]]"
  - "[[evergreen/interview-methods-for-2025|Interview methods for 2025]]"
Tags:
  - Essay
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 19fbdf02-815c-80fd-b49c-ebfb08701f31
---

# How to Interview Engineers

### 📑 Materials

---

### ✍️ Post

---

Hey there! This article closes our series about hiring engineers. It’s our third piece — in the first two we covered respectively:

- **✨ **[**Hiring Principles for 2025**](https://refactoring.fm/p/hiring-principles-for-engineering) — three ideas that guide the way I think about hiring these days.

- 🎒 [**Nailing your Onboarding Developer Experience**](https://refactoring.fm/p/nailing-your-your-onboarding-developer) — a guest article by Dana Lawson, CTO of Netlify, that covers how to write great job descriptions, how to onboard engineers, tooling and metrics. 

So, today we are wrapping it up by talking about *how to interview engineers*.

This is an ever-hot topic. People have debated good vs bad interviews for as long as I can remember, but over the past two years things got even hotter, thanks to a trend you may have heard of: AI. 

In fact:

- 🔍 **On a tactical level** — AI tools forced hiring managers to rethink the effectiveness of several hiring *devices*, from take-home assignments to cover letters.

- **🔭 On a strategic level** — AI is shifting the type of skills that truly matter, so you need to ask yourself: *what* should I select engineers for?

Today we will address both, starting from first principles, and down to real-world stories of the interview processes run by some of the tech leaders I respect the most.

So here is the agenda:

- ⚔️ **Speed vs Quality **— how to navigate the infamous tradeoff.

- 🪴 **Select for the unlearnable skills **— mentor what you can; hire what you can’t.

- 💼 **Make interviews mimic real work **— how to design interviews that closely resemble your actual environment.

- 📋 **Round-up of interview methods **— discussing LeetCodes, take-home’s, case studies, code reviews, and behaviorals!

Let’s dive in!

---

### ⚔️ Speed vs quality

When designing your interview process, the obvious tradeoff is between **speed and quality**, which resembles the one between **precision and recall **in machine learning.

To get higher precision (== minimize false positives) you need more thorough, and thus slower, interviews, but these will win you less candidates (== lower recall). Conversely, going faster wins more candidates, at the expense of some bad hires. Thorough interviews also require more time and work from your team, so all in all this is a tough tradeoff.

Where should you settle? YMMV, but for regular software engineers, my personal target is **2 weeks from screening to offer**.

This is apparently way below the average, which is [24 days for a software engineer](https://www.paraform.com/blog/average-time-to-hire-software-engineer) in the US 👇

> *In the internet and tech industry in the US, the average length of the interview process is approximately 24 days, while the recruitment process for a software engineer in the US usually spans about 35 days.*

So, if it takes more than two weeks, you can diagnose the process. Where is the time going? In my experience, here are the usual suspects:

1. **Is it too many interviews?** → Make sure different interviews actually test for different things, and are not there only for consensus — e.g. 3 interviews is a good number.

1. **Is it latency because people have other things to do? **→** **Make sure hiring is top priority, as it should be, and people’s time is allocated accordingly.

1. **Are you waiting for multiple candidates to get to the final stage?** → Rookie mistake! You should make an offer as soon as a strong candidate emerges.

Finally, some people just don’t feel comfortable at hiring fast. If that’s the case, it’s probably because you feel that false positives pose too much of a risk. Now, bad hiring sucks for everybody, so that’s a fair concern — but it shouldn’t be overly so.

The best way to *de-risk* bad hires is to make probation do its job. There’s some personal preference in this, but my *style *of hiring is to keep interviews lean and jump soon into doing real (paid) work together. 

That’s because I have found interviews to get into diminishing-returns-land quite fast, so when you are—say—80% sure about a candidate, closing the final 20% costs you just as much as the rest of the process — so better to start real work and see how it goes.

![image](../assets/1acbdf02815c8051.png)

The catch is that for this to work your onboarding needs to be snappy, so that during the initial months you can truly evaluate where the collab is going. But fast onboarding, in turn, is good signal about the health of your dev team, so this is a nice flywheel.

That said, what should you use interviews for?

---

### 🪴 Select for the unlearnable skills

What you should test engineers on totally depends on the role, but there is a key question you should ask yourself:

> ***What can you mentor people on, vs what should they bring from home?***

Most of the times, you should only hire for the latter.

That’s because of two factors:

1. **🎓 Great teams create great mentors** — who are happy to pass knowledge and grow younger folks. We always ask ourselves whether people on our team are learning, but are they *teaching*, too? Mentoring colleagues is an incredible growth experience. 

1. 📈 **Smart people learn fast **— usually faster than we account for. That’s especially true in the AI age.

This also means that in well-functioning teams, where senior leaders act as mentors and knowledge is transferred efficiently, you can **hire mostly junior engineers** and get away with it.

![image](../assets/1acbdf02815c8016.webp)

Charity Majors wrote an incredible piece on the newsletter two weeks ago, which also discussed this 👇

[https://refactoring.fm/p/in-praise-of-normal-engineers](https://refactoring.fm/p/in-praise-of-normal-engineers)

So, you should hire for skills that are hard to learn, or those where your team is unable to mentor new hires. In today’s terms, this usually means less memorization and more quality thinking:

- 📇 **Memorization** — is specific knowledge about frameworks and languages. With AI, this is devaluing at a pretty fast rate.

- 🧠 **Quality thinking** — is system design, product mindset, and good communication. This is timeless and still makes a huge difference.

My hard and fast recipe is: for quality gaps—hard-won experience that your team lacks—hire senior talent; while for pure bandwidth, hire junior talent.

Now that we covered what you should test during interviews, how should you run them? 👇

---

### 💼 Make interviews resemble actual work

There exist *a lot* of interview methods, many of which we will discuss further below. The best ones for you depend on your specific setting, team, and role you are hiring for.

There is, however, a *north star* principle that is always valid: **make interviews resemble actual work as much as possible**. This means:

- 🎨 **Topics** — pick problems that are as similar to yours as possible.

- 🤝 **Setting** — test for good collaboration other (rather) than solo output.

This seems obvious, but many interview processes *fail* at doing good selection because they test candidates 1) for problems who look *nothing* like what they will do at work — e.g. strong algorithmic challenges — and 2) in contexts that have zero resemblance to how the team works — e.g. live *solo* coding with a hiring manager peeking over your shoulder.

> *Match the interview with the daily life of the team. You do CQS? Component test? Pair-programming? Slice big task into small one? Most of time you work alone? […]*

After you have designed your interview process, you should inform the candidate *in advance* about how it works. Possibly in the job description already.

This is such an underrated power move: sharing the process creates more alignment and commitment upfront, and allows candidates to *prepare* for interviews in a way that makes sense for what you will test for.

For example, Notion has an [incredible section](/50e339f3fa8a4c8a8a4c1cd7a7565110) that helps candidates prepare for interviews. They have *guides* for literally all the positions — insane!

---

### 💬 Interview methods

After we covered principles and trade-offs about interviews, it’s time to dive into the specific methods you can use to select engineers. 

We collected many of them from the community, via a dedicated mastermind session, plus an async thread that has been running for one month now!

![image](../assets/1acbdf02815c807b.png)

Many of these methods have *overlaps*, so, to better disambiguate, let’s start by listing the macro areas you should test engineers for. For me, it’s three things:

1. 💻 **Pure coding** — can they write actual code? Do they have a basic understanding of algorithms and CS principles?

1. 🛠️ **System design** — can they reason through complex and nuanced tech problems? Do they understand business constraints? Can they explore tradeoffs and propose sensible alternative solutions?

1. 🤝 **Working together** — do they have the right attitude to work with peers? Can they work through feedback, communicate without ego, and display a growth mindset? Are they focused on business value, instead of building tech for its own sake?

These also create a gradient that goes from pure **tech skills** to pure **human skills**.

The *depth* in which you need to test for these highly depends on your role, but there are also clear trends. For example, for the average developer role, pure coding skills matter less than they used to. Engineers still need solid tech foundations, and you need to probe these to make sure you hire those who can *walk the talk*, but at the same time AI allows engineers to jump more easily into foreign stacks and be proficient, and frees from a lot of trivial and routine tasks.

![image](../assets/1acbdf02815c8035.png)

> *Imagine that your company had its own proprietary and totally secret tech stack. Programming language, framework, etc. How would you hire for that, given that outside people will not have seen that language or framework before?*

This evolution turned *system design* and *working well together* into (even more) top material — which is often said to favor *senior* over *junior *engineers, but to me, it’s a draw: system design is obviously a skill that comes and grows with experience, but the right attitude is something people often display from early on. 

Even more so, I have found that traits like a growth mindset, or putting ego aside, comes definitely easier to fresh engineers than seasoned ones with 10+ years under their belt.

> *Whatever frameworks, libraries and so on we’re using today, in 18 months time we could be using something completely different. So I don’t worry so much about experience in particular languages, tools and techniques; if they’ve got a demonstrated track record of picking things up when needed, that’s a good sign.

— Ross Younger*

So let’s review some of the most popular ways to test for all of these:

#### 1) 🔨 LeetCodes

They have always been despised by engineers, but were once the flagship way of sorting out good engineers from bad ones. Now, in a world where [86% of all LeetCodes can be solved by AI](https://www.thinkevolveconsulting.com/can-claude-cheat-coding-interview/), this is clearly not the case anymore.

> *Think about it like this: If you’re hiring based on math skills and all you ask are questions like “What’s 32 × 12” then of course someone can cheat with a calculator. If you have a meandering conversation about this technique, that approach, etc, you’ll get a much better picture.
— Clemens Adolphs*

Today they still have a place, but to me that place is *screening*. You may just use them to sort out people who can’t program at all. Most people I know either 1) don’t employ LCs anymore, or 2) they only ask for easy / medium ones in early interview stages.

Also, the harder the LCs the lower the correlation with actual performance, because 1) the actual jobs never resemble that, and 2) live hard coding under pressure isn’t for everybody.

#### 2) 🏡 Take-home’s

I have been a huge proponent of take-home assignments for a long time, but I admit they took a hit because of AI.

Take-home’s have always had obvious downsides—takes a lot of work to create a good exercise that actually validates skills, and takes a lot of work to go through submissions—but they compensated through plenty of upsides: they may resemble a real-world task; they can be done asynchronously*, *removing *stress* from the candidate, and they serve as a great basis for a follow-up interview.

The problem today is that green-field development is too much of a convenient scenario for the latest models, and it’s hard to create an exercise that really tests candidates’ skills outside of that. Granted you can complement it with a good discussion later, where the candidate needs to show they understand the code they wrote — but if the code itself is not that probing anymore, and the meat of the selection is the discussion afterwards, is it really worth to stick to this? 

Two interesting alternatives are case studies and code reviews 👇

#### 3) 📋 Case study

A case study is a problem you really worked on, for which you ask the candidate to design a viable solution during a live interview.

Some high-level coding may be involved, but this is mostly about system design, discussing tradeoffs, and exploring different qualities. It should provide good hooks to cover topics like testing, scalability, or code quality.

I like the idea of the case study for many reasons:

1. **It doesn’t require too much prep** **for interviewers **— you can pick a problem that is familiar for them, on which they are already prepared.

1. **Adherence to the work** — it tests the candidate on something that is close to real work.

1. **Tech + communication skills** — it involves real business constraints on which to evaluate collaboration chops. Can the candidate entertain different solutions? Can they elaborate on pros and cons? Are they receptive to feedback?

> *Someone might be technically perfect match, but their mindset would be around code perfection, test coverage perfection, while ignoring the needs of the end user.
— Dusko Bajic*

#### 4) 🔍 Code review

Surprisingly, we spent a lot of time during the mastermind discussing this technique, as more than a few managers started employing it:

> *Having the candidate review a pull request for our own contrived solution to a contrived problem. This provides a surprising amount of signal, takes less time than a take-home project, and usually gives us more to discuss in an interview. It’s easy to tell who did the work to understand the PR’s problem space. I’ve found this especially useful for interviewing managers where I care more about how they interact with others’ work than their own coding skills.
— Jordan Haines*

Our coach-in-residence, Melinda Seckington, also weighed on it:

> *With AI-assisted coding becoming more common, some teams have shifted their interview focus. Instead of hands-on coding exercises, the focus now is on a candidate’s ability to understand and explain code, as well as their communication skills. This involves: having candidates explain what the code does, discussing potential changes and their impact, and evaluating their ability to talk about trade-offs and decisions.*

Various approaches were discussed, with some teams running this as a 1:1 conversation, while others going for an async format (e.g. commenting on a pull request).

The code review method retains many of the goods of the *case study*, but it is more technical. While the case study is centerered on a problem, the code review is centered on code. Up to you to figure out what is best for you!

#### 5) 🥇 Career highlights / stories

Finally, it’s common to ask the candidate stories from his past experience, in the form of “*tell be about the work you are the most proud of*”, or “*tell me about a time when […]*”.

I have found this type of questions to be almost *always* useful, and I always try to save some time in the hiring process to ask something along these lines.

I like to do it towards the end, so that:

- I can use them to ask for things that I am still unsure about from the rest of the interviews.

- Being under control of the candidate, they can use them to highlight qualities that may have not emerged so far, and they feels strong about.

---

### 📌 Bottom line

And that’s it for today! Here are some takeaways:

1. ⚡ **Target two weeks from screening to offer** — the industry average is 24 days, but you can move faster by prioritizing hiring, running only necessary interviews, and making offers as soon as strong candidates emerge.

1. 🧠 **Hire for unlearnable skills** — focus on quality thinking (system design, product mindset, communication) rather than memorized knowledge that AI can now supplement.

1. 💼 **Make interviews mimic real work** — design interview tasks that closely resemble your actual environment, measuring collaborative skills rather than solo performance in artificial scenarios.

1. 🔄 **Use probation effectively** — instead of chasing 100% certainty in interviews (which has diminishing returns), start real work with promising candidates and evaluate on the job.

1. 🎓 **Mentor what you can, hire what you can't** — great teams can grow junior talent through effective mentoring; only hire senior engineers to fill experience gaps your team can't teach.

1. 📝 **Share your interview process upfront** — transparency builds alignment, reduces candidate anxiety, and allows focused preparation that benefits both sides.

1. 🔍 **Consider new evaluation methods** — move beyond LeetCode toward techniques like case studies and code reviews that test problem-solving, system design, and communication in realistic contexts.
