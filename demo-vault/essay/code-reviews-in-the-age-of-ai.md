---
aliases:
  - "Code Reviews in the Age of AI"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-essays|Publish Essays →]]"
Status: Evergreened
URL: "https://refactoring.fm/p/ai-code-reviews"
"👓 Status": Not started
"Created time": "2025-04-15T14:08:00.000Z"
Date: 2025-05-28
"Has Notes":
  - "[[evergreen/ai-reduces-toil-in-code-reviews|AI reduces toil in code reviews]]"
  - "[[evergreen/we-need-horizontal-ai-deployment-to-avoid-bottlenecks|We need horizontal AI deployment to avoid bottlenecks]]"
  - "[[evergreen/make-a-leap-of-faith-and-completely-automate-something-small-with-ai|Make a leap of faith and completely automate something small with AI]]"
Tags:
  - Guest
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 1d6bdf02-815c-80b2-98e3-c48dd96a39c8
---

# Code Reviews in the Age of AI

There is no shortage of articles online about the future of software development and AI. I am guilty of that too 🙋‍♂️

Most articles, however, only focus on *AI coding. *They ponder about an hypotethical future where AI may or may not write all of our code, engineers become *AI* *managers*, or they keep coding but 100x faster.

The tools themselves, when you look at the big names — Cursor, Windsurf (just insanely acquired by OpenAI), Lovable, etc — are all about *coding*. Or vibe-coding.

Now, if you ask me, that future might materialize one day, but that day is not today. Vibe-coding only goes so far, and both my own experiments (will write more in an upcoming article!) and those of my friends are falling kind of short of our expectations.

But *coding* is only a part of the development process, and it turns out there are other parts where, perhaps more quietly, AI is making a real dent, and it feels like the future is here.

One of these is *code reviews*.

Also, while in other AI verticals you can usually point to *groups* of similar apps with similar traction and adoption, when it comes to AI-powered code reviews, there is a single tool that is absolutely dominating the conversation: CodeRabbit.

CodeRabbit is **the most installed AI** app both on Github and GitLab. It is used in 1M+ repositories, and trusted by some of the most *picky* customers you can find, like the Linux Foundation, MIT, and Mercury.

So I got in touch with the CodeRabbit team and we talked at length about the future of code reviews and the impact of AI in the development process. 

Here is the agenda for today:

1. **🏆 What is the goal of code reviews in 2025? **— working top-down from first principles.

1. **🔄 Code review workflows **— what companies do today + our proposals to do better.

1. **🪄 How AI changes reviews **— examples and reflections about the current state of AI code reviews.

1. **🔮 Future scenarios **— throwing ourselves into predictions and more long-term thinking.

Let’s dive in!

---

### 🏆 What is the goal of code reviews in 2025?

As you may know if you have been reading Refactoring for some time, code reviews are one of my small obsessions.

Code reviews look, to me, like an imperfect solution to two *supremely important* problems:

1. ✅ **Keeping code quality high** — which leads to ease of change, fewer defects, less maintenance, you name it.

1. 📚 **Sharing knowledge across the team** — which creates alignment, growth, resilience, flexibility, and more.

These are also *self-reinforcing* goals: sharing knowledge helps keep quality high, and, in turn, high quality code is generally crisper and easier to understand for others.

How do code reviews address these goals? Typically, by making code changes inspected by more than one engineer — at least two: the author, and one+ reviewers.

To me, this not only looks fine: it looks like the only possible way.

Still, even if we agree on the above, there is plenty left to figure out, like:

- *Should all code be reviewed?*

- *What goes into a review?*

- *Who should do reviews?*

- *When should reviews be made?*

These questions matter *a lot*, and can make all the difference between an effective, successful review workflow, and a disfunctional, time-wasting one.

---

### 🔄 Code review workflows

Many teams answer these questions with a pretty dogmatic workflow, that looks more or less like this:

- 🔀 **Async** — a PR is opened, one reviewer (or more) is assigned, and they will perform their review asap.

- ⛔ **Blocking** — code isn’t merged and deployed until it passes the review.

- 🔒 **Mandatory** — you do the same workflow for all changes.

The most glaring problem of this strategy is that it continuously breaks developers’ workflow: submitters are blocked waiting for reviews and need to *context-switch* to other tasks (and back), and reviewers need to stop what they are doing to do reviews ASAP.

The second problem is the *one-size-fits-all* approach. Should all reviews be async? Or blocking? Or mandatory? 

If the goal of reviews is 1) improving quality and 2) sharing knowledge, are we sure all code changes need both? Or even one of the two?

So, one one side, teams produce a *swath* of small and inconspicuous changes, for which the *blocking* factor is questionable. On the other side, for big and ambitious PRs, it is unclear how much nuance async + low-context reviews can really capture.

So, last year we discussed a more flexible approach in our article "[**Thoughts on Code Reviews**](https://refactoring.fm/p/thoughts-on-code-reviews)", proposing the **Automate / Defer / Pair** framework. Let's quickly recap:

1. 🤖 **Automate** — for low-risk changes with no remarkable knowledge to share (e.g., small bug fixes, dependency updates, simple refactors), rely heavily on automated checks like linters, static analyzers, and comprehensive test suites. Human review can be minimal or even skipped.

1. ↪️ **Defer** — for most changes, especially in a continuous delivery environment, consider merging first and reviewing *after* the merge. This works especially well when changes are released behind feature flags. The primary goals of knowledge sharing and quality improvement can still be achieved asynchronously, without blocking delivery. Feedback is gathered post-merge and improvements are addressed in follow-up changes.

1. 🤝 **Pair** — for complex, high-risk, or critical changes, consider synchronous collaboration, like pair programming or a dedicated pairing review session. These are 10x more effective than async back-and-forth and allow for real-time discussion, immediate clarification, and deeper knowledge transfer.

This framework isn't about eliminating human oversight but making it more targeted and impactful, reducing bottlenecks while upholding quality and fostering learning. 

Now, how does AI fit into this picture?

---

### 🪄 How AI changes reviews

The reason why *vibe-coding* is still fuzzy and controversial, while AI code reviews are spreading like wildfire, is that the latter are *immediately* useful, and don’t require teams to radically change the way they work.

Here are examples provided by the CodeRabbit team:

So, in my experience, here are the main benefits of AI reviews:

- 🗑️ **Reduce toil**

- ✨ **Increase enjoyment**

- 📉 **Reduce risk**

- 🎓 **Democratize expertise**

Let’s look at each of them:

#### 1) 🗑️ Reduce toil

AI significanly expands what can be automated, *especially *drawing from stuff that human reviews *don’t like* to check.

Because let’s be honest, a lot of reviewing is busy work, and AI makes it easier:

- **Adherence to team-specific best practices / conventions **— AI can learn your team's coding style and common patterns, flagging deviations.

- **Checking for test cases **— as a reviewer, how much do you like looking for tests or suggesting to add more? Yeah, me too. AI figures this out easily + can even boilerplate more ones.

- **Summarize changes **— especially for larger PRs, AI can provide concise summaries of the changes, helping reviewers quickly grasp the scope and intent. E.g. CodeRabbit offers line-by-line explanations of changes.

All together, this helps to 👇

#### 2) ✨ Increase enjoyment

The whole point of reducing toil is to use human time to address higher-value topics that are uniquely human (for now 🙈).

It turns out, this is also the stuff that people enjoy the most:

- **Architectural soundness** — is this the right approach? Does it align with our long-term technical vision? What trade-offs and constraints have been considered?

- **Readability and maintainability** — is the code clear, understandable, and easy for others to work on in the future? Human *taste *here is still unmatched.

- **Knowledge sharing & mentorship** — reviews become less about nitpicking and more about constructive feedback, coaching, and knowledge sharing. This is the *beauty* of reviews, unburdened by the need to do the basic checks discussed above.

#### 3) 📉 Reduce risk

Not to brag, but the *defer* part of our framework becomes much more viable with AI. 

If an AI agent has already performed a thorough first pass, the confidence to merge first and  conduct a human review *later* increases significantly, especially for medium-to-small changes.

In particular:

1. **Developer velocity increases** — because people are not blocked for routine checks

1. **Fatigue is reduced** — because humans are not the first line of defense for *everything*.

#### 4) 🎓 Democratize expertise

AI can act as a basic *expert-in-a-box,* bringing specialized knowledge to every review. Think of hard to access topics like security, performance, or accessibility.

For example, even if your team doesn’t have a dedicated security expert reviewing every PR, AI can flag common vulnerabilities. Same goes with potential performance bottlenecks, or subtle accessibility issues.

This doesn’t *reduce* the need for experts in these domains — it reduces the amount of time they need to spend on routine busy-work, so they can work at a higher level of abstraction on strategy and platform.

---

### 🔮 Future scenarios

As part of our chat, we further brainstormed about the future scenarios of AI coding and what may come in the near future.

Here are the best ideas I believe in:

#### 1) 🌊 **AI needs *****horizontal *****adoption to avoid bottlenecks**

The development process is a *pipeline* that includes several steps. If we only increase throughput of *some* parts thanks to AI, we are going to create bottlenecks elsewhere.

E.g. to reap the benefits of AI allowing us to write more code, we need to speed up also code reviews, testing, and documentation, otherwise we will produce more toil for humans in some of these steps.

So, since AI IDEs like Cursor are commonplace, AI code reviews are not a nice-to-have anymore — they are essential to avoid drowning in PRs (or accepting a lower quality output).

#### 2) 🔍 AI may solve reviews before it solves coding

Speaking of reviews, I feel that it is plausible — and even likely — that AI becomes *more *proficient at reviewing code (identifying errors, suggesting improvements, checking conventions) *before* it becomes truly autonomous and reliable at writing large, complex, novel systems from scratch.

This might seem counterintuitive — if AI writes unreliable code and we need *humans* to guide it, how can it *review* code well?

Because reviewing is, in many ways, a more constrained problem: you're evaluating existing code against known patterns, and when a lot of uncertainty is gone. Instead, generating novel, high-quality code in a complex domain is arguably harder.

So we might see the bulk of code reviews being solved by AI even while humans are still heavily involved in the creative and design aspects of coding. Which would flip the current dynamic on its head, where coding assistance is widespread, while review automation is still catching up.

#### 3) 🧑‍⚖️ **Humans as guarantors of *****taste***** and *****business alignment***

As AI takes on more of the *how* (implementation details), human engineers increasingly focus on the *what* and, even more, on the *why*.

We've talked about [Taste vs. Skills](https://refactoring.fm/p/taste-vs-skills) before — taste being, in engineering, the ability to discern things like quality, good design, and solutions that match business needs.

For engineers, exercising their *taste* will mean asking questions like:

- *Does this AI-generated code accurately reflect what we need?*

- *Is this architecture sound and maintainable?*

- *Is this design coherent with our technical strategy?*

- *Can we make smarter buy-vs-build decisions here?*

#### 4) 🤖 Sometimes you need a leap of faith (automation)

In most workflows, today, people are using AI to create *drafts* — drafts of code, drafts of code reviews, drafts of docs — and have humans do a final pass.

This is nice, but it also corners people into doing a lot of context switching and micro tasks.

I believe that sometimes, under controlled conditions, we should make a leap of faith and completely automate some tasks. We should switch from an “*approve first*” to a “*possibly revert later*” approach.

So ask yourself: *what are those things that AI can do that would be relatively inexpensive to revert in case it does them wrong? *Chances are it’s more than you think.
