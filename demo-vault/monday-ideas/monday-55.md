---
aliases:
  - "Monday #55"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-monday-idea|Publish Monday Idea]]"
Status: Published
"👓 Status": Not started
"Created time": "2024-04-18T15:09:00.000Z"
Date: 2023-06-12
"Has Notes":
  - "[[evergreen/people-shouldnt-be-surprised-by-your-performance-review|People shouldn’t be surprised by your performance review]]"
  - "[[evergreen/minimum-viable-testing-process|Minimum Viable Testing Process]]"
  - "[[evergreen/use-no-code-agencies-to-bootstrap-your-no-code-adoption|Use no-code agencies to bootstrap your no-code adoption]]"
Tags:
  - Monday
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 8e8c7b0a-990c-40df-9509-8ede6807f79c
---

# Monday #55

*Hey, *[*Luca*](https://twitter.com/lucaronin)* here! Welcome to the ****Monday Ideas ***💡

*Every Monday I will send you an email like this with ****3 short ideas**** about making great software, working with humans, and personal growth.*

*You will also receive a long-form, original article on Thursday, like the last one:*

- [**How to Write Documentation**](https://refactoring.fm/p/how-to-write-documentation)** **📑

*To receive all the full articles and support Refactoring, consider subscribing if you haven’t already!*

Get full access to Refactoring ✨

[https://refactoring.substack.com/subscribe](https://refactoring.substack.com/subscribe)?

*p.s. you can learn more about the *[*benefits of the paid plan here*](http://refactoring.fm/about)*.*

---

### 1) 🔍 Minimum Viable Testing

Many people ask me how to test software properly, what types of tests to focus on, how much they should care about coverage, etc.

Here is my preferred testing workflow:

1. **Use a statically typed language** — Most languages today have statically typed versions you can adopt. My opinion is that this is a *no-brainer* for 99% of teams. Static typing catches *a ton* of bugs early, while also documenting the code thanks to types and annotations.

1. **Write unit tests *****when relevant ****— *Unit tests are an important part of your testing investment. However, I am not adamant about coverage. Write them for whatever is non-trivial or subject to implementation changes in the future.

1. **Write plenty of integration tests **— Integration tests are about testing execution *paths* that involve multiple functions / components. Figure out the most important ones for each area of your product, and test them in depth. To identify them, think about *business* paths, based on how your product is used. API endpoints are also good candidates for integration tests.

1. **Write just a few, critical end-to-end tests **— End-to-end tests are expensive to develop and maintain. My rule of thumb is to invest on testing those parts that you would check manually otherwise. The main goal of end-to-end tests is to *remove manual checks*, so you can release faster.

1. **Avoid staging if you can **— I wrote a [full article](https://refactoring.fm/p/do-you-need-staging) about this. TL;DR is you can probably avoid using a staging env by implementing a combination of gradual rollouts (with [feature flags](https://refactoring.fm/p/feature-flags)) and live previews for PRs. The idea is: the less steps to production, the faster you release, the better feedback loop you have, which also helps stability because of faster recovery from mistakes.

Here is a cheatsheet about the ROI of the various types of tests 👇

![image](../assets/c3b1028df3c54d08.png)

Aaand here is the full, exhaustive article I wrote about testing software in 2023 👇

[https://refactoring.fm/p/how-to-test-software-in-2023](https://refactoring.fm/p/how-to-test-software-in-2023)

---

### 2) ✨ Bootstrap no-code adoption with agencies

Sometimes, it might be scary to build a complex product with no-code tools, especially if your team hasn’t much experience with them.

In this case, you can bootstrap the process by working with a specialized agency. Here are the best ones I know of, based on recommendations by readers and reviews on [Clutch](https://clutch.co/) (no affiliation):

- [**8020**](https://www.8020.inc/)** **— US-based. One of the first no-code agencies to appear in the market. They specialize in Webflow development.

- [**9x**](https://www.9x.agency/) — Berlin-based agency that works with the likes of Bubble, Airtable, Zapier, and Retool. They also provide training to your people so they can maintain the product later, and build more in the future. 

- [**AirDev**](https://www.airdev.co/)** **— the most trusted no-code agency on Clutch. They use primarily Bubble to build products for startups, and internal tools. They also run a bootcamp to educate people about developing with Bubble. 

- [**Codemap**](https://codemap.io/) — marketplace that connects companies with vetted no-code experts. A good solution if you are looking to hire someone for the long-term, rather than working with an agency. 

I wrote a full article about how build great software with no-code tools 👇

[https://refactoring.fm/p/how-to-build-with-no-code](https://refactoring.fm/p/how-to-build-with-no-code) 

---

### 3) 🏅 Performance reviews should be unsurprising

I believe performance reviews are mostly useful as a prime moment to *act* on feedback — by setting goals and priorities — rather than *sharing* it. 

In fact, in healthy relationships, feedback is frequent and mainly shared 1) on the spot, and 2) in recurring venues like 1:1s. So, feedback in performance reviews should mostly *ratify* what has already been discussed privately.

![image](../assets/5271d23110554125.png)

As a rule of thumb, if people are surprised by your review, you did something wrong.

You can find more ideas about performance review in this recent Refactoring essay 👇

[https://refactoring.fm/p/performance-reviews](https://refactoring.fm/p/performance-reviews)

---

And that’s it for today! If you are finding this newsletter valuable, consider doing any of these:

**1) ✉️ Subscribe to the newsletter** — if you aren’t already, consider becoming a paid subscriber. You can learn more about the [benefits of the paid plan here](http://refactoring.fm/about).

Get full access to Refactoring ✨

[https://refactoring.substack.com/subscribe](https://refactoring.substack.com/subscribe)?

**2)** ❤️ **Share it** — Refactoring lives thanks to word of mouth. Share the article with your team or with someone to whom it might be useful!

I wish you a great week! ☀️

Luca
