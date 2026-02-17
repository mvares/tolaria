---
aliases:
  - "Monday #41"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-monday-idea|Publish Monday Idea]]"
Status: Published
"👓 Status": Not started
"Created time": "2024-04-18T15:09:00.000Z"
Date: 2023-03-13
"Has Notes":
  - "[[evergreen/the-platforms-intermediate-stage|The “platforms” intermediate stage]]"
  - "[[evergreen/trunk-based-dev-brings-higher-velocity-and-lower-cycle-time|Trunk-based dev brings higher velocity and lower cycle time]]"
  - "[[evergreen/the-feedback-quadrant|The Feedback Quadrant]]"
Tags:
  - Monday
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 3ec63279-0117-453e-83e8-3d0c857ba18d
---

# Monday #41

*Hey, *[*Luca*](https://twitter.com/lucaronin)* here! welcome to the ****Monday 3-2-1 ****✨*

*Every Monday I will send you an email like this with ****3 short ideas**** about engineering management, technical strategy, and good hiring.*

*You will also receive the regular long-form one on Thursday, like the last one:*

- [**How to Write Secure Code**](https://refactoring.fm/p/how-to-write-secure-code)** **🔒

*To receive all the full articles and support Refactoring, consider subscribing if you haven’t already!*

Become a better tech leader today ✨

[https://refactoring.substack.com/subscribe](https://refactoring.substack.com/subscribe)?

*p.s. you can learn more about the *[*benefits of the paid plan here*](http://refactoring.fm/about)*.*

---

![image](../assets/e9334aff25c546e8.png)

---

### 📣 New Refactoring Sponsorships

As you know, Refactoring is mainly funded by the subscriptions of its paid members. However, in the past we also had the opportunity to work with a few great products to promote them with our readers.

This has led to working with some of my favourite companies, like [Reforge](https://www.reforge.com/), [Stepsize](https://stepsize.com/), or [Swarmia](https://www.swarmia.com/).

So, in the last few weeks we have completely revamped our sponsorship program to make more of such collaborations possible. If you are interested in learning more, you can find more info below:

Check out the sponsorship program ✨

[https://refactoring.link/working-together](https://refactoring.link/working-together)

I only work with products I can genuinely recommend and that can be helpful to our readers. I would love to discover more.

---

### 1) The Feedback Quadrant ❤️

[Kim Scott](https://www.linkedin.com/in/kimm4/) has seen it all. 

She led teams at Google, coached Twitter and Dropbox CEOs, managed a pediatric clinic in Kosovo, and started a diamond-cutting factory in Moscow.

She spent a lifetime managing the most diverse people and leading them to success. Later, she wrote her learnings in one of the world’s most popular book about management and feedback: [**Radical Candor**](https://www.goodreads.com/book/show/29939161-radical-candor).

Kim breaks feedback into four quadrants. On the horizontal axis you have **unclear to clear** feedback, and on the vertical you have **negative to positive**.

![image](../assets/34ad48e002a048b7.png)

Whether positive or negative, the best feedback is always clear and specific. On the contrary, it sets up our reports for failure.

Softening negative feedback is human — we want to avoid adding even more pressure on our teammates. Such **cruel empathy**, though, doesn’t give them the tools to do things differently. It dampens their growth.

Unclear positive feedback** **is equally ineffective. Simply saying “*you are doing a great job*” doesn’t cut it, because it doesn’t bring any learning. In the worst case, it feels *artificial* and a way to balance the bad one.

You can learn more about giving good feedback in this previous article 👇

[https://refactoring.fm/p/how-to-give-feedback-](https://refactoring.fm/p/how-to-give-feedback-)

---

### 2) 🎽 Platforms and feature teams

As your engineering team grows larger than the initial 10-15 people, you get to a point where people can’t simply all *work together*, usually for two reasons:

- 📣 **Communication** — in a larger group of people, “everyone does everything” makes it hard to organize work properly.

- 📚 **Skills **—** **technology becomes more complex and it requires specific skills to move forward.

The most natural choice at this stage is to organize your engineering team into layers/platforms based on your tech stack — e.g. Frontend + Backend.

Separating layers helps to build engineering culture and practices, and slowly makes your team shift from generalists to specialists.

[Embed](https://twitter.com/lucaronin/status/1350025856354308096?s=21)

In a team organized by platforms, complex features are delivered by **Feature Teams**. 

These are cross-functional teams assembled with the purpose of delivering a specific feature, and dismantled later.

![image](../assets/ad5e1810c2014b58.png)

My feeling about Feature Teams is they are a **necessary evil **in between the small, “generalists” stage, and the final “products” one where you can assemble durable, independent, cross-functional teams.

Feature Teams have two major pitfalls:

- **Product ownership **— being temporary, teams retain little ownership of what they build. This in turn makes it harder to 1) properly iterate on features and 2) develop product expertise over time.  

- **Resource allocation **— while it is a flexible way to work, it also requires continuous negotiation between stakeholders to define what is the best way to allocate engineers. 

![image](../assets/2fd80715fed14a96.png)

You can find more ideas about the various growth stages of an engineering team in this past article 👇

[https://refactoring.fm/p/the-three-stages-of-engineering-teams](https://refactoring.fm/p/the-three-stages-of-engineering-teams)

---

### 3) 🚩 Feature flags enable trunk-based development

Trunk-based development is a version control workflow where developers work in small batches and merge their work into the main trunk as often as possible — usually at least once a day.

That is opposed to the common workflow of *feature branches*, where developers create a separate branch for each new feature, and then work in isolation on that branch until the feature is complete.

There is [convincing evidence](https://services.google.com/fh/files/misc/state-of-devops-2017.pdf) that teams who adopt trunk-based workflows achieve higher velocity and shorter cycle time.

However, not all projects can be broken down in small, working parts that get completed within a day. How should you work in those cases? 

Enter feature flags.

![image](../assets/17276b27824a4347.png)

With feature flags, you can keep code in a *disabled *state, and merge it to the trunk even if the feature is not complete.

Small and frequent merges have some major benefits:

- Easier code reviews

- Less chance of conflicts

- Reduced risk for releases

You can learn more about how to use feature flags, and what they are useful for, in the article below 👇

[https://refactoring.fm/p/feature-flags](https://refactoring.fm/p/feature-flags)

---

And that’s it for today! If you are finding this newsletter valuable, consider doing any of these:

**1) ✉️ Subscribe to the newsletter** — if you aren’t already, consider becoming a paid subscriber. You can learn more about the [benefits of the paid plan here](http://refactoring.fm/about).

Get full access to Refactoring today ✨

[https://refactoring.substack.com/subscribe](https://refactoring.substack.com/subscribe)?

**2)** ❤️ **Share it** — Refactoring lives thanks to word of mouth. Share the article with your team or with someone to whom it might be useful!

I wish you a great week! ☀️

Luca
