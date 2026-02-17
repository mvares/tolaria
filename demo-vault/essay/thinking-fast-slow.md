---
aliases:
  - "Thinking, Fast & Slow"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-essays|Publish Essays →]]"
Status: Evergreened
URL: "https://refactoring.fm/p/thinking-fast-and-slow?utm_source=publication-search"
"👓 Status": Not started
"Date HH": 2025-10-30
"Created time": "2024-09-06T07:43:00.000Z"
Date: 2024-11-13
"Has Notes":
  - "[[evergreen/the-two-selves|The Two Selves]]"
  - "[[evergreen/prospect-theory|Prospect Theory]]"
  - "[[evergreen/biases-and-heuristics|Biases and Heuristics]]"
  - "[[evergreen/system-1-vs-system-2|System 1 vs System 2]]"
Tags:
  - Book
  - Personal
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: d49ab2e8-ed42-4f45-831d-bc9b79334c53
---

# Thinking, Fast & Slow

### 📑 Materials

---

![image](../assets/94c3f27460f84a1b.png)

![image](../assets/105bdf02815c809f.png)

![image](../assets/105bdf02815c801c.png)

### Notes from the review

### ✍️ Post

---

Hey there! This is a **Book Edition** 📚 — where I publish our review + summary of a famous non-fiction book in our space.

It is made possible by the book club in the community, where every two months we decide on a non-fiction book to read, and we review it together in a live event at the end of the period.

Over the last two months, we've been diving into "Thinking, Fast and Slow" by Daniel Kahneman.

Kahneman was a psychologist and economist. In 2002 he was awarded the **Nobel Prize** in Economic Sciences for his work in applying psychological insights to economic theory, particularly in the area of judgment under uncertainty.

He passed away earlier this year — so reading and reviewing his work felt like a fitting tribute.

So, "Thinking, Fast and Slow" is not just another **pop psychology book**. It’s a cornerstone work in understanding human decision-making and cognitive biases, backed by decades of rigorous research.

And it shows.

In fact, if you get the physical edition, the first thing you will probably notice is that this is a hefty book. It clocks in at nearly 500 pages, with a 35-page appendix of notes and references. It’s the work of a lifetime: the lifetime of one of the most brilliant and prolific scientists of his generation.

“Thinking, Fast and Slow” is organized following a top-down approach: it starts with big ideas and gradually drills down into specifics. So, while it contains an inordinate amount of ideas, it never feels daunting or overwhelming, thanks to the clear structure, plenty of examples, and the easy writing stile. We will follow its structure pretty much verbatim in this review.

Also, while it wasn't written specifically for people in tech, I have found its insights to be profoundly relevant to our job.

As engineering leaders, we're **constantly making decisions**: we estimate projects, assess risks, allocate resources, and navigate complex human dynamics. Most of these decisions are made under uncertainty, and Kahneman's work shows just how *bad *we are at these. He explains, with scientific precision, why we make irrational decisions, even when we believe we're being perfectly logical.

Ultimately, the book challenges us to **think about thinking**, by revealing invisible forces that shape our judgment. Understanding these forces help us make better decisions, in work and life.

So let’s explore the key concepts from the book, and discuss how they apply to our work. Here's our agenda for today:

- 🧠 **Two Systems** — understanding our dual thinking processes

- 🎭 **Biases and Heuristics **— recognizing our mental shortcuts

- 📊 **Prospect Theory** — rethinking how we assess value and risk

- 🤝 **The Two Selves** — balancing experience and memory in design

Let's dive in!

---

### 🧠 A Tale of Two Systems — understanding our dual thinking

Kahneman's central thesis revolves around two modes of thought: System 1 and System 2. This concept is fundamental to understanding how we make decisions:

- 1️⃣ **System 1** — is fast, intuitive, and emotional. It operates automatically and quickly, with little or no effort and no sense of voluntary control.

- 2️⃣ **System 2** — on the other hand, is slower, more deliberative, and more logical. It allocates attention to effortful mental activities that demand it, including complex computations.

What's surprising — and somewhat unsettling — is how much we rely on System 1, even when we think we're being logical and methodical. We often pride ourselves on our analytical abilities (especially in engineering 🫠), but Kahneman shows that we're far more inclined to do quick, intuitive judgments.

The main problem is that we don’t have a reliable way to figure out *when* to engage System 2 — the analytical side — vs accept the quick answer provided by System 1.

This perfectly displayed in the famous bat and ball problem:

> *"A bat and ball cost $1.10. The bat costs one dollar more than the ball. How much does the ball cost?”*

Most people answer 10 cents, which is System 1 stuff. The correct answer (5 cents) would require engaging System 2, but we usually accept the quick answer because it looks good.

This reminded me of chess. During lunch I often watch [Hikaru](https://www.youtube.com/@GMHikaru) videos, where he often talks about the problem of knowing *when to spend your time*. Modern chess has shifted more and more towards shorter time controls (e.g. 10-minute games), which means players spend little time, on average, on every move. What’s interesting, especially in grandmaster games, is that players do not spend a similar amount of time on every move — they *blitz* most of them (i.e. few seconds) and spend long chunks of several minutes on a few crucial ones.

Blitz moves are System 1 — quick judgment and pattern-matching — while the long ones are when players engage their analytical brain.

Knowing *when* it is worth to spend more time on a move — i.e. when to engage System 2 vs when to trust intuition — is a crucial quality that separates outstanding players from the good ones.

Ok, but chess is time-constrained: in real life, couldn’t we deliberately skew towards System 2 most of the times? No sir, because System 2 is 1) **slow**, and 2) **extremely costly**, while System 1 is basically free. 

Using System 2 quickly leads to cognitive strain, so we can rely on it sparingly.

About this, Kahneman described an experiment where people were asked to solve math problems while simultaneously memorizing a 7-digit number. As their System 2 was occupied with the memorization, they made impulsive (System 1) decisions on the math problems, leading to comical mistakes.

But what mistakes? Time to talk about biases 👇

---

### 🎭 Biases and Heuristics

In the second chapter, Kahneman explores a wide range of cognitive biases and heuristics. These shortcuts often serve us well, but they can also lead us astray, especially in complex scenarios.

The book provides a long list, and you may already know many of them. Here are the ones that resonated the most with my experience:

#### **1) Anchoring** **bias **⚓

Our tendency to rely too heavily on the first piece of information offered. This can significantly impact negotiations and estimations.

Example: In an experiment, Kahneman asked participants to estimate the percentage of African countries in the United Nations. Before answering, they spun a wheel that landed on either 10 or 65. Those who saw 10 guessed an average of 25%, while those who saw 65 guessed 45%. The initial number, despite being random (and they knew it!), significantly influenced their estimates.

#### **2) Availability bias** 🔍

We overestimate the probability of events that are more easily remembered.

Example: Kahneman describes how people often overestimate the likelihood of plane crashes compared to car accidents. That’s because plane crashes, being more dramatic and widely reported, come to mind more easily, leading people to believe they're more common than they actually are.

In tech, this might lead us to overemphasize recent failures or successes when making strategic decisions. How many decisions do we made based on anecdotes and stories, vs grounded data? A lot of “data-driven” behaviour is not really data-driven: we cherry pick (intentionally or not) data that is just recent, or that fits our bias.

#### **3) Confirmation bias **🤝

Confirmation bias is our inclination to search for, interpret, and recall information in a way that confirms our preexisting beliefs. This can be particularly dangerous when evaluating new things, like some tech or practice.

Example: In a classic study cited by Kahneman, participants were given evidence about the effectiveness of capital punishment. Those who initially supported it found the *pro-deterrence* data more convincing, while opponents found the *anti-deterrence* data more persuasive. Both groups just became more entrenched in their original views, despite seeing the same information.

This is also the classic problem with social media: since algorithms tend to show us more of what we like, we end up in a bubble where our feeds are a mirror of our particular view of the world, hitting both on confirmation and availability bias.

So, how do you fight biases? 

Kahneman says you can’t fight them *in the moment*:* *you need to fight them upfront. For scenarios where accurate judgment is required, you have to design systems and procedures that *counteract *biases and ensure good decision-making.

When left to ourselves, improvement is possible but limited. If we want to enforce quality judgement, it’s all about process.

---

### 📊 Prospect Theory — rethinking how we assess value and risk

After biases, Kahneman conveniently segways into Prospect Theory, which is regarded as one of the century’s most significant contributions to behavioral economics. This theory challenges the traditional view that people make **rational decisions** based on the final outcome of their choices.

Instead, Prospect Theory shows three main things:

1. ⚖️ **Relativeness** — people evaluate outcomes of gains and losses relative to a reference point, not absolute values.

1. **💸 Loss aversion** — losses hurt more than equivalent gains feel good.

1. 🧮 **Probability distortions **— we are not good at weighing probability.

By combining all three we get plenty of irrational, *asymmetric* behavior, in which people tend to be risk-averse for gains but risk-seeking for losses.

While a lot of this is conventional wisdom now, what surprised me the most is how *precise the *model is in its predictions. Kahneman doesn’t only show we are biased — he shows exactly *how* biased we are.

For example, there is a stunningly precise reference table for how (badly) probabilities turns into decision weights:

<!-- Table -->

And a mathematical function to display our loss aversion:

![image](../assets/13bbdf02815c8063.png)

The absolute values and parameters of these functions stay reliably constant throughout the study, making our irrational behavior predictable.

This is all summarized into a final 2x2 grid:

<!-- Table -->

Prospect Theory is also the section that offers the most examples from business settings. Risk assessment and decision-making are managers’ bread and butter, and the model shows we are just doing it wrong: we are overly cautious with successful projects, but willing to take excessive risks to save failing ones. It also shows why it is hard to kill projects that are clearly failing: the pain of accepting the loss often outweighs the rational choice to cut our losses.

Knowing these biases is the first step to counter them, but Kahneman also showed that people leaned into irrational behavior, while *knowing* it was irrational! 

Just like with other biases, Kahneman believes process and rules can save us from bad intuitive decisions. Still, it may be hard to make the right calls *even* when we know they are so.

---

### 🤝 The Two Selves

In the final part of the book, Kahneman moves to exploring his latest research interest, which is about how we experience things, how memory works, and how this influences our happiness.

I feel conflicted about this section because, while it presents interesting insights, it is also a surprising departure from previous topics, and, clocking in at only ~20 pages, it feels less cohesive and grounded than the rest.

Still, it made for a fascinating read. 

Kahneman introduces the concept of two selves:

- ✨ **The Experiencing Self** — who lives in the present moment. It's the part of us that undergoes pleasure or pain as events unfold.

- 📖 **The Remembering Self** —  who keeps score and maintains the story of our life. It's the self that makes decisions based on our memories of past experiences.

Kahneman illustrates this with a thought-provoking example: Imagine two people undergoing a painful medical procedure:

- Person A experiences moderate pain for 10 minutes. 

- Person B experiences the same moderate pain for 10 minutes, followed by mild discomfort for an additional 5 minutes. 

Logically, Person B had a worse experience overall. However, when asked later, Person B often reports a less negative memory of the event than Person A.

Why? Because the remembering self doesn't simply *add up* moments of pain or pleasure. Instead, it follows what Kahneman calls the **peak-end rule **— our memory of an experience is disproportionately influenced by two things: 1) its most intense point (the peak) and 2) how it ends.

In this case, the milder ending for Person B results in a more positive overall memory.

This concept has far-reaching implications:

1. 🎲 **Decision-making** — we often make choices based on our remembered experiences, not on how we actually felt during those experiences. This can lead to decisions that don't maximize our actual well-being.

1. 📏 **Happiness measurement** — traditional measures of happiness, which ask people to evaluate their lives, may be capturing the satisfaction of the remembering self rather than the actual experienced well-being of the experiencing self.

1. 🎢 **Experience design** — for those creating products or experiences, it suggests that crafting positive peaks and endings may be more important than ensuring consistent pleasantness throughout.

Kahneman applies this concept to life satisfaction as well. Would you prefer a highly enjoyable vacation where all memories and photos are erased at the end, or a less pleasant trip that you can remember? Many people choose the latter, highlighting how much we value our remembering self over our experiencing self.

The vacation example made me reflect on how we evaluate our own lives and careers. Are we making decisions based on how we actually experience our days, or are we chasing stories we can tell ourselves (and others) later? When we make decisions, which self are we really serving?

---

### 📌 Bottom line

So, in a field like engineering that prides itself on logic and rationality, "Thinking, Fast and Slow" is at once a humbling reminder of our own limitations, and a powerful tool for overcoming them.

The book is long and dense for sure, but that’s because it approaches topics with scientific rigor and is generous with examples. Also, Kahneman’s humor, humility, and gift for writing never makes it dull or unnecessarily complex.

So, here are the main takeaways from today:

1. 🧠 **Recognize your two systems** — understand that your mind operates on two levels: the fast, intuitive System 1 and the slower, more logical System 2. Being aware of when each system is at play can help you make better decisions.

1. 🎭 **Watch out for cognitive biases** — biases like anchoring, availability, and confirmation can significantly skew your judgment. Implement structured processes to counteract these biases in your decision-making.

1. 📊 **Rethink risk and value** — Prospect Theory shows that we're not always rational about gains and losses. Consider how this affects your approach to risk management and overall judgment.

1. 🔍 **Question your confidence** — we're often more confident in our judgments than we should be. Cultivate humility and seek diverse perspectives to challenge your assumptions.

1. 🤝 **Balance your two selves** — remember that your experiencing self and remembering self have different priorities. Consider both when designing experiences or evaluating your own satisfaction.

1. 🛠️ **Design better systems** — finally, armed with these insights, focus on creating decision-making processes that account for our cognitive quirks. The goal isn't to eliminate biases (we can't), but to design environments that help us make better choices despite them.
