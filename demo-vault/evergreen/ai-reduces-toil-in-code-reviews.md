---
aliases:
  - "AI reduces toil in code reviews"
"Is A":
  - Evergreen
"Created at": "2025-06-19T12:38:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to": "[[essay/code-reviews-in-the-age-of-ai|Code Reviews in the Age of AI]]"
"Updated at": "2025-06-26T06:39:00.000Z"
Status: Not started
notion_id: 217bdf02-815c-806a-9448-c1409e3c88de
---

# AI reduces toil in code reviews

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
