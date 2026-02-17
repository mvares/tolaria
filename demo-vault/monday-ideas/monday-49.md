---
aliases:
  - "Monday #49"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-monday-idea|Publish Monday Idea]]"
Status: Published
"👓 Status": Not started
"Created time": "2024-04-18T15:09:00.000Z"
Date: 2023-05-01
"Has Notes":
  - "[[evergreen/side-projects-in-cvs|Side projects in CVs]]"
  - "[[evergreen/testing-pyramid-vs-testing-trophy|Testing Pyramid vs Testing Trophy]]"
  - "[[evergreen/minimize-features-operating-cost|Minimize features’ operating cost]]"
Tags:
  - Monday
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 6f453b09-2043-44c3-a1df-013109a5e0bb
---

# Monday #49

*Hey, *[*Luca*](https://twitter.com/lucaronin)* here! welcome to the ****Monday 3-2-1 ****✨*

*Every Monday I will send you an email like this with ****3 short ideas**** about engineering management, technical strategy, and good hiring.*

*You will also receive the regular long-form one on Thursday, like the last one:*

- [**How to Use Engineering Metrics**](https://refactoring.fm/p/how-to-get-started-with-engineering) 📊

*To receive all the full articles and support Refactoring, consider subscribing if you haven’t already!*

Become a better tech leader today ✨

[https://refactoring.substack.com/subscribe](https://refactoring.substack.com/subscribe)?

*p.s. you can learn more about the *[*benefits of the paid plan here*](http://refactoring.fm/about)*.*

---

![image](../assets/bd219a2d8e0b48b7.png)

---

### 1) ⚖️ Delivery vs Operating costs

For each feature, you can roughly divide costs in two steps:

- **Delivery Costs** — costs you sustain to develop the feature until the first deliverable.

- **Operating Costs** — costs you sustain to maintain and evolve the feature, until...forever! 

If you work in small batches and iterate fast ([which you should](https://refactoring.fm/p/the-four-measures-of-software-delivery)), the line between these two steps is blurred, but the costs follow a predictable distribution nevertheless. They go from being higher before delivery, to being lower over time when your team moves on to new initiatives.

![If you don't plan properly, operating costs are going to kill your team's capacity over time  ](../assets/94737766aa40453d.png)

**Good engineering wants to keep such costs low**.

In particular, good design should minimize *both* delivery and operating costs. And I would argue that, out of the two, it's vastly more important to minimize operating costs, as they — in contrast with delivery costs — compound over time with those of other features.

More ideas on feature costs 👇

[https://refactoring.fm/p/the-operating-cost-of-new-features](https://refactoring.fm/p/the-operating-cost-of-new-features)

---

### 2) 🏆 Testing Pyramid vs Testing Trophy

One of the most popular testing *models* out there is the **testing pyramid**, made popular by Martin Fowler. The larger the layer, the more tests and effort on that layer.

![image](../assets/b658fe9243904ffc.png)

The pyramid is based on the assumption that the earlier you catch a bug the better — which is largely right — and that higher-level tests are slower to write/run and costlier to maintain.

What I feel is missing though, is that as you move up you also get more stable *contracts*, and higher chance of *changing implementation* under the hood. This makes integration tests *very* valuable, while unit tests… a bit less so.

![image](../assets/0ac5e8e2b550485b.png)

To Martin’s (and others’) credit, things haven’t always been like this. In the past we would write most code from scratch. There were lot of custom functions, a lot of algorithms, so unit tests verified complex stuff whose implementation might also change in the future.

Today, especially at unit level, we mostly write software by *composing* stuff. 

Logic in itself is trivial, and when it changes, most often it does because the contract itself changes as well — which puts unit tests into the liability bucket.

So, I don’t feel the pyramid is still the right mental model for most teams.

When you look at the table above, you see that the ideal testing strategy might not look like a pyramid after all, but more like a diamond.

Or, [as Kent said](https://kentcdodds.com/blog/write-tests), like a trophy.

![The testing trophy proposed by Kent C. Dodds](../assets/eed6de87523c42f2.jpeg)

The ideas behind the trophy are simple:

1. Static testing is a no-brainer.

1. Integration tests consistently deliver the best ROI, so most of your effort should be spent on those.

1. End to end and Unit tests are good when used for the right things.

If you want to learn more, I recently wrote a full article about designing a good testing process 👇

[https://refactoring.fm/p/how-to-test-software-in-2023](https://refactoring.fm/p/how-to-test-software-in-2023)

---

### 3) 🕹️ Side-projects in CVs

The goal of your resume is to get you to the first interview call. 

Then, of course, it’s on you — but a good CV can easily bring you 3x the interviews than a mediocre one.

![image](../assets/557deb01fb2a4ccd.png)

Now, there is debate about what other activities are valuable to put on your resume besides your work ones.

To me, the rule of thumb is that you should include anything that proves either **good impact** or **good skill**. Both is better, of course, but it’s also ok to display projects that mostly demonstrate one of them.

About tech skills, common entries are a good stack overflow profile, your open source contributions, or research papers if you are a PhD. Technical side-projects are ok, granted they are **not trivial**:

- Simple dashboard in React → *No thanks*

- Small full-stack app to run a movie club with your friends → *Yes!*

Likewise, it’s ok to display non-tech interests granted they have **real-world impact** or display strong commitment. Examples I have seen are:

- Running a non-profit association → *impact*

- You run marathons → *commitment*

The best advice I can give on this is to treat your interests just like your work experience: be specific and focus on impact.

- OK: “*I like running”*

- Better: “*I like running and I do marathons”*

- Best: “*I like running. Last year I ran 2 marathons and this year I would like to do 4.”*

A separate mention should be made for **blogs** and **writing online** in general. This is almost always useful. A good article can display both tech and communication skills and it’s a fantastic investment for your resume (other than your reputation, your network, etc.).

The minimum viable blog, to me, has at least **two articles** written over the last year. It’s ok for them to be short, like ~1000-words pieces, and I generally prefer two short pieces over a single, long one.

I recently wrote a full article about how to create a great resume 👇

[https://refactoring.fm/p/resume](https://refactoring.fm/p/resume)

---

And that’s it for today! If you are finding this newsletter valuable, consider doing any of these:

**1) ✉️ Subscribe to the newsletter** — if you aren’t already, consider becoming a paid subscriber. You can learn more about the [benefits of the paid plan here](http://refactoring.fm/about).

Get full access to Refactoring today ✨

[https://refactoring.substack.com/subscribe](https://refactoring.substack.com/subscribe)?

**2)** ❤️ **Share it** — Refactoring lives thanks to word of mouth. Share the article with your team or with someone to whom it might be useful!

I wish you a great week! ☀️

Luca
