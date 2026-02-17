---
aliases:
  - "The Power of Inversion 🔃"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-essays|Publish Essays →]]"
Status: Evergreened
URL: "https://refactoring.fm/p/the-power-of-inversion-"
"👓 Status": Not started
"URL 2": "https://twitter.com/lucaronin/status/1406872664162119681"
"Created time": "2024-04-18T14:53:00.000Z"
Date: 2021-06-18
"Has Notes":
  - "[[evergreen/mental-model|Mental Model]]"
  - "[[evergreen/subtracting-over-adding|Subtracting over Adding]]"
  - "[[evergreen/pre-mortem|Pre-mortem]]"
  - "[[evergreen/inversion|Inversion]]"
  - "[[evergreen/premeditatio-malorum|Premeditatio Malorum]]"
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: eaf6a733-a6ef-4ee3-a59f-474c178f68a8
---

# The Power of Inversion 🔃

1. **What is the most important point?**

1. **Why is that the most important point? *****(what can you achieve with it)***

1. **Why should people care? *****(what's the benefit)***

1. **What is the easiest way to understand the most important point?**

1. **How do you want the reader to feel?**

1. **What should the reader do next?**

1. **The Three Qualities (*****pick 2+*****)**

### ✍️ Post

---

[Charlie Munger](https://en.wikipedia.org/wiki/Charlie_Munger), business partner of Warren Buffett and Vice Chairman of Berkshire Hathaway, once famously said: "*All I want to know is where I’m going to die, so I’ll never go there*".

That quote was probably inspired by the German mathematician [Carl Gustav Jacob Jacobi](https://en.wikipedia.org/wiki/Carl_Gustav_Jacob_Jacobi), who often solved hard problems by looking at them *backwards.* In his own words: "*man muss immer umkehren"* — that is: "*Invert, always invert*".

The origin of this approach, though, goes way back in history. Ancient stoic philosophers, like Seneca and Marcus Aurelius, often conducted an exercise called *premeditatio malorum, *that translates to "premeditation of evils". 

Stoics believed that by *visualizing* negative things that could happen in their life, they could make better plans to prevent them.

This mental model is known today as *Inversion*, and was made popular (again) by Munger itself, as a framework that can be applied equally in life and business.

I have been a fan of *Inversion* for a while, but only recently I realized how many useful practices in Product and Engineering work actually stem from it. 

In this article I am going to review my favourite ones:

- 💀 **Pre-mortem**

- 💩 **The Worst Possible Solution**

- ✂️ **Subtracting over Adding**

### 💀 Pre-mortem

A *pre-mortem* exercise is basically the modern version of the stoics' *premeditatio malorum. *It consists in listing all possible situations that would make us miss our goals, and create a plan that takes those into account.

Pre-mortems are run at all levels (e.g. business, product, engineering) but they might take different names. Here are a few 👇

#### How Might We Fail

Google created the [Design Sprint](https://www.thesprintbook.com/) methodology as a way to kick-start new projects in a team. It is a 5-days process that goes from idea inception to building a prototype that gets tested with actual customers. 

![image](../assets/9b78efbf4c3f4e1c.png)

On Monday, at some point participants are asked to reply to the *how might we fail* question — that is, listing all the possible ways the initiative could fail.

From a startup / business perspective, some common ones are:

- The project is a solution for a non-existent problem 

- Customers are not willing to pay for it

- We are not able to reach customers effectively

You could do the same for single features or product areas, asking yourself:

- Why would a customer not want this?

- How might this make the user experience worse?

#### Engineering Pre-mortem

Pre-mortems are popular and useful in engineering as well. As you work on a tech design, you can ask questions to address common issues:

- **Project running late**: *what could cause us to miss our deadline?*

- **Technical Debt**: *what changes to requirements would make this design obsolete in the future?* (see [technical debt as disagreement](https://refactoring.fm/p/the-true-meaning-of-technical-debt))

- **Build the wrong thing: ***are there any requirements missing?*

- **Scaling and reliability issues: ***are we creating any bottlenecks or single points of failure?* 

### 💩 The Worst Possible Solution

This is one of my favourite brainstorming techniques, and one of the most counterintuitive as well.

If you are looking for solutions to a problem, try starting with the worst you can imagine. Literally, those that either make the problem worse, or solve it at the expense of creating much bigger issues.

Bad solutions provide tons of insights and make it easier to work your way towards the good ones.

I have reported below an example of worst and best solutions for the traffic congestion problem, taken from a real brainstorming session I had a few months ago 👇

![Worst and best solutions for traffic congestion](../assets/10b45b1573bc4f09.png)

As you can see, some of the bad solutions are similar to the good ones, or provide direction to them.

If you want to learn more about this approach, I wrote an [full article](https://refactoring.fm/p/the-worst-possible-solution-) about it a few months ago.

### ✂️ Subtracting over Adding

Across several experiments, [researchers have demonstrated](https://www.nature.com/articles/d41586-021-00592-0) that we have a bias towards addressing problems by *adding* new things (e.g. components, initiatives, ideas) rather than removing existing ones.

It is unclear why it is so, but it seems people do not consciously *discard *subtractive solutions — they do not consider them at all.

![*Consider that bricks structure. How would you stabilize the platform on top? Most people do not consider removing the small green brick — they just propose to add more ones.*](../assets/4a7e4c4990cf45cb.png)

This is particularly unfortunate as subtraction is often faster and cheaper than addition.

So keep that in mind and add it to your arsenal. Ask yourself more often: *can I solve this problem by just removing something?*

### 📚 Resources

Inversion is everywhere, so there are a ton of resources this week! Here they are:

- 📑 [**Practice The Stoic Art of Negative Visualization**](https://ryanholiday.net/practice-the-stoic-art-of-negative-visualization/) — [Ryan Holiday](https://twitter.com/RyanHoliday) wrote an entire book about stoics. This article explains one of their favorite practices, *premeditatio malorum*, which is the precursor of today's *inversion* thinking.

- 📑 [**Pre-mortem Instructions**](https://www.atlassian.com/team-playbook/plays/pre-mortem)** **— A playbook to run effective pre-mortems, provided by the folks at Atlassian.

- 📑 [**Adding is favoured over subtracting in problem solving**](https://www.nature.com/articles/d41586-021-00592-0?utm_campaign=tmw-ctocraft&utm_medium=email&utm_source=Revue) — *Nature* reveals our bias in solving problems by *adding* things, instead of *subtracting* them. Even when the latter would be easier.

- 📑 [**Ask Why It Won’t Work**](https://review.firstround.com/ask-why-it-won%27t-work-and-other-lessons-this-founder-relies-on-while-building-from-0-to-1) — this thoughtful interview with [Rick Song](https://www.linkedin.com/in/rick-song-25198b24/) covers many lessons from a successful startup founder. Some of these, about product and hiring, include inversion thinking.

- 📑 [**The Worst Possible Solution**](https://refactoring.fm/p/the-worst-possible-solution-)** **— ** **I wrote this article in November to explain one of my favourite brainstorming techniques. It is about finding the best solutions for a problem, starting with the worst possible ones. 

- 📑 [**Inversion: The Crucial Thinking Skill Nobody Ever Taught You**](https://jamesclear.com/inversion)** **— [James Clear](https://twitter.com/jamesclear), one of my favourite writers, explains Munger's thoughts about inversion, and how avoiding stupidity is often easier than seeking brilliance.

**And that's it for this week! Have you practiced inversion — even unknowingly — in your work or life? Are there other techniques you want to share? Let me know in the comments or via email! **📮
