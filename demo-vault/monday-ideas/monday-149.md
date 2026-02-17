---
aliases:
  - "Monday #149"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-monday-idea|Publish Monday Idea]]"
Status: Published
"👓 Status": Not started
"Created time": "2025-03-25T14:31:00.000Z"
Date: 2025-03-31
"Has Notes":
  - "[[evergreen/binstack|Binstack]]"
  - "[[evergreen/the-three-questions-of-platform-engineering-teams|The three questions of Platform Engineering teams]]"
  - "[[evergreen/hierarchies-are-useful-to-scale-comms|Hierarchies are useful to scale comms]]"
Tags:
  - Monday
  - Free
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 1c1bdf02-815c-8042-bae7-ef0b18c49de0
---

# Monday #149

### 2) ☑️ Binstack

Binstack is a fantastic decision framework that I have discovered thanks to Clemens’ recommendation in the community:

> *Don’t overcomplicate multi-dimensional decisions. Pick the dimension that you most care about, define what “substantial” looks like in that category, and discard any options that aren’t substantial in that category. Rinse and repeat.*

What does this mean? Well, many decision / prioritization frameworks (e.g. [RICE](https://www.intercom.com/blog/rice-simple-prioritization-for-product-managers/)) tell you to pit items against each other by considering various *dimensions*, giving a score to each of them (e.g. from 1 to 5), and considering the total.

In my experience, though, this leads to murky results, for two reasons:

- ⚖️ **Not all dimensions are equally important** — some matter more than others. You can weight them, but that becomes even more cumbersome.

- ❓ **Values are arbitrary** — in many cases it is hard to assign a numeric value to dimensions. It ends up being a bit arbitrary, and driven by what options we *really* want to win.

So, Binstack says two things:

- 🚥 **Turn numeric values into yes/no** — define a level that makes that dimension successful or not, and just note if items are compliant or not. For example, instead of having a “Revenue” score from 1 to 5, have a “*at least a 10% revenue bump*” threshold.

- 🥇 **Put dimensions in order of importance** — rank them from the most important to the least important, and pick the item that meets the most of them, in descending order.

![Move from numeric to binary goals/values for more clarity and less laziness.](../assets/1c1bdf02815c8009.png)

Quoting the [original article](https://longform.asmartbear.com/maximized-decision/) that introduced Binstack:

> *No more values, no more weights, no more scores. Either an item materially contributes to that attribute, or it doesn’t. “Materially” means the effect is so large you can measure it easily.*

Binstack works for me because 1) it is decisive, and 2) it has the right amount of nuance (not too much, not too little) that you need for most decisions.

I wrote a full article about essential mental models for engineers, which you can find below 👇

[https://refactoring.fm/p/mental-models-for-engineers-and-managers](https://refactoring.fm/p/mental-models-for-engineers-and-managers)

---

### 3) 🧱 The Three Questions of Platform Teams

Two months ago we brought in none other than Camille Fournier to write a full Refactoring article about [how to create a good platform team](https://refactoring.fm/p/creating-a-platform-engineering-team)

In the article, one of the ideas that were the most helpful to me is about how to figure out if your platform team is actually doing well.

Camille boils this down to asking three questions:

- 🛠️ **Are you writing code, not just scripts, templates, or docs? **— If you’ve put together a balanced team, the team should be writing software. You have identified a place where you can create leveraged value through custom software, and you’ve started building. You may have taken over ownership of an existing platform from another part of the org, or you may have been given ownership of one that was owned by volunteers in the past.

- 🚨 **Are you operating any critical systems? **— It’s not enough to be writing some code. There should be systems that you actually own and operate. A common failure of new platform teams is that they don’t take on operational ownership of anything, which undermines their value to the rest of the company. Instead, the platform mindset *blends software engineering and operations*.

- 📞 **Are you talking to your customers and stakeholders? **—  if you want to have the years it will take to build out mature platforms, you’re going to need the goodwill and patience of the rest of the company. Some of that comes from operating things for them, some of it might come in providing one-off support to fix problems in their systems, but most should come from *listening to your customers*, creating product roadmaps that reflect their concerns, and showing those customers and their bosses that you are delivering reliably against those roadmaps.

![image](../assets/1a6bdf02815c80fd.png)

So the biggest lesson I learned from Camille is probably that good platform engineering looks a lot like good product management. Your *application team customers* are a market where you are trying to achieve product-market fit, in competition with their ideas about what they could do themselves and what they could get by managing their own vendor offerings or open source.

The product part of your platform mindset is a survival instinct as much as it is about building the right thing. Build both quick wins and strategic needs, operate something critical, talk to your customers, and advertise your work.

You can find the full article below! 👇

[https://refactoring.fm/p/creating-a-platform-engineering-team](https://refactoring.fm/p/creating-a-platform-engineering-team)

---

### 4) 🏯 Are hierarchies good or bad?

As long as your team is small, there isn’t much need for a formal organization — 5 to 10 people can work pretty well without much structure.

The main problem, when teams grow larger, is communication. Large teams have a hard time doing things like:

- Keeping people on the same page

- Coordinating and allocating resources

- Making good, participated decisions

So when you grow from 5 people to, say, 15 or 20, it seems that these problems get worse at first gradually, and then suddenly.

But why?

Because, as by [Metcalfe’s Law](https://en.wikipedia.org/wiki/Metcalfe%27s_law), the complexity of communication is proportional to the *square* of the number of users involved. So, while people grow linearly, complexity grows geometrically 👇

![image](../assets/1c1bdf02815c80b7.png)

To tame communication complexity, companies usually introduce **hierarchies**. Hierarchies have many advantages:

- They provide clear communication paths, ensuring **alignment** is obtained across the organization.

- They reduce the number of *lines* each person has to manage, allowing the company to **scale**.

- They provide a simple way for **making decisions**, by assigning responsibility to people up in the hierarchy.

Same 7 people, different configurations:

![choose your poison: longer path or more lines](../assets/1c1bdf02815c8010.png)

However, they also bring drawbacks:

- 🗃️ **Overhead** — communication has a longer way to travel to a destination, which makes you slower. Longer paths also create all kinds of “work’s work”, like traffic controlling, managing up, presentations, and more.

- 🔀** Inflexibility** — once in place, it is hard to reconfigure roles and processes. This in turn reduces agility, resilience to turnover, and velocity, too.

Hierarchal structures are commonplace all kinds of organizations, but it is lesser known that there are a handful of tech companies that work successfully *without* them.

I wrote a two part series about them a while ago 👇 it’s a fun read!

[https://refactoring.fm/p/unusual-teams-1](https://refactoring.fm/p/unusual-teams-1)

---

And that’s it for today! If you are finding this newsletter valuable, consider doing any of these:

**1) **🔒** Subscribe to the paid version** — if you aren’t already, consider becoming a paid subscriber. 1500+ engineers and managers have joined already! Learn more about the [benefits of the paid plan here](http://refactoring.fm/about).

Get full access to Refactoring ✨

[https://refactoring.substack.com/subscribe](https://refactoring.substack.com/subscribe)?

**2)** 🍻 **Read with your friends** — Refactoring lives thanks to word of mouth. Share the article with your with someone who would like it, and **get a free membership** through the new [referral program](https://refactoring.fm/p/referral).

Read with your friends 🍻

[https://refactoring.fm/leaderboard](https://refactoring.fm/leaderboard)

I wish you a great week! ☀️

Luca
