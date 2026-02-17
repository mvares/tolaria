---
aliases:
  - "Monday #28"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-monday-idea|Publish Monday Idea]]"
Status: Published
"👓 Status": Not started
"Created time": "2024-04-18T15:09:00.000Z"
Date: 2022-12-12
"Has Notes":
  - "[[evergreen/you-need-to-allocate-engineering-time-for-hiring|You need to allocate engineering time for hiring]]"
  - "[[evergreen/the-rise-of-product-engineers|The Rise of Product Engineers]]"
  - "[[evergreen/use-stacked-diffs-and-trunk-based-dev-to-improve-velocity|Use stacked-diffs and trunk-based dev to improve velocity]]"
Tags:
  - Monday
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 185ebe9f-6b87-4b53-9dad-780ae1adbe89
---

# Monday #28

*Hey, Luca here 👋 welcome to the ****Monday 3-2-1 ****✨*

*Every Monday I will send you an email like this with ****3 short ideas**** about engineering management, technical strategy, and good hiring.*

*You will also receive the regular long-form one on Thursday, like the last one:*

- [***My Desk Setup and Accessories***](https://refactoring.fm/p/my-desk-setup-and-accessories)* *🪑

*To receive all the full articles and support Refactoring, consider subscribing if you haven’t already!*

Become a better tech leader today ✨

*p.s. you can learn more about the *[*benefits of the paid plan here*](http://refactoring.fm/about)*.*

---

![image](../assets/d969a97f886c4d98.png)

---

### 1) Engineers vs Product Engineers ✨

The push for the *Product Engineer* role fits a broader trend in making product / tech roles *wider* and giving people more ownership and autonomy.

To me, the Engineers vs Product Engineers feud resembles the one between Product Owners and Product Managers.

- **Product Owners** have mostly *tactical* responsibilities. They groom the backlog, write user stories, prioritize what to do next, and attend all the Agile meetings. Their focus is short to mid-term.

- **Product Managers** have more *strategic* responsibilities. There is overlap with Product Owners about how they both shape what to do next, but PMs are also responsible for the product vision and success. Their focus is mid to long-term.

![A traditional Agile model](../assets/def3fd2c887f474a.png)

In PM-based teams, there is the opportunity for engineers to step in and take on some of the PO’s duties that the PM is not going to cover.

In high-performing teams, PMs provide direction and support but most often leave Engineers in charge of creating tickets and managing actual tasks. Requirements focus on outcomes, rather than how to explicitly build stuff, leaving engineers free to make decisions that matter.

![The PM + PE model. As the PM scope “shifts to the left”, engineers fill in the gap.](../assets/95a3629d6f7c4a6a.png)

This culture promotes more ownership and enables personal growth.

More on product engineers 👇

[https://refactoring.substack.com/p/product-engineers](https://refactoring.substack.com/p/product-engineers)

### 2) 🔨 Stacked diffs and trunk-based dev

Many big companies like Facebook and Google have a code review workflow that is not based on PRs, but rather on **stacked diffs**.

[Embed](https://twitter.com/dan_abramov/status/1407803004183531527?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1407803004183531527%7Ctwgr%5E%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fgraphite.dev%2Fblog%2Fpost%2FDThX8ffP1gmxWJChEv0y)

Stacked diffs are a way to have your code reviewed *without* firing up a PR. You take a portion of your local changes and make it available for review. You can *stack* these changes into multiple requests for review, so you never get stuck waiting for reviews.

[Embed](https://twitter.com/alexandracoding/status/1278001790907285508?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1278001790907285508%7Ctwgr%5E%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fgraphite.dev%2Fblog%2Fpost%2FDThX8ffP1gmxWJChEv0y)

This workflow, other than being faster, allows to (mostly) get rid of branches and work in [trunk-based development](https://cloud.google.com/architecture/devops/devops-tech-trunk-based-development) mode instead. In turn, there is convincing evidence that teams who adopt trunk-based workflows achieve higher velocity and faster turnaround.

[Embed](https://twitter.com/jezhumble/status/1415908836439773185)

If this seems crazy to you, you may reflect on the fact that engineers working in some of the best companies in the world commit directly to master all the time (and often on a monorepo), unless they have a reason not to.

More ideas on code reviews 👇

[https://refactoring.fm/p/code-reviews](https://refactoring.fm/p/code-reviews)

### 3) 💼 Allocate engineering time for hiring

One of the most common mistakes I see in hiring processes is not explicitly allocating enough engineering time for it.

Engineers, in fact, need to be constantly involved:

- **✍️ They design the interview process** — create and update exercises, take-home tests, questions, and more.

- **📞 They interview candidates** — and manage the subsequent feedback process.

- **📋 They contribute to writing the job post** — by setting requirements and responsibilities.

- **🧑‍🤝‍🧑 They bring in new candidates** — via referrals.

Time spent on hiring should be taken into account in the general planning, because it is sizeable.

[Luca Marchi](https://www.linkedin.com/in/luca-marchi-16111038/), Software Engineer at Picnic, reports on this:

> *All the senior engineers on the team have 2 hours per week allocated for the interviews.*

In my experience, you may need even more time than that. Interviews require prep work, writing notes, decision meetings afterwards, and more. It is not uncommon for senior engineers to spend **>10% of their time** on hiring.

Joel Spolsky similarly advocates for involving most people on the team in interviews:

> *You should always try to have at least six people interview each candidate that gets hired, including at least five who would be peers of that candidate. [...] If even two of the six interviewers thinks that a person is not worth hiring, don’t hire them.*

Six people might be too much for someone, but the main takeaway is that hiring needs **wide consensus**. That’s because you are not only testing for technical prowess, but also wider cultural fit. You want your people to feel 1) excited to work with the candidate, and 2) committed to the hiring decision.

More on designing hiring processes 👇

[https://refactoring.fm/p/good-hiring-process-1](https://refactoring.fm/p/good-hiring-process-1)

---

### 📣 Join the Refactoring Talent Club

If you’re looking for a new gig, join to get personalized opportunities from hand-selected companies. You can join publicly or anonymously, and leave anytime.

Apply now

If you’re hiring, join the Refactoring Talent Club to start getting bi-monthly drops of world-class hand-curated Engineering people who are open to new opportunities.

![image](../assets/82e8bc355b9d4e63.png)

---

And that’s it for today! If you are finding this newsletter valuable, consider doing any of these:

**1) ✉️ Subscribe to the newsletter** — if you aren’t already, consider becoming a paid subscriber. You can learn more about the [benefits of the paid plan here](http://refactoring.fm/about).

Get full access to Refactoring today ✨

**2)** ❤️ **Share it** — Refactoring lives thanks to word of mouth. Share the article with your team or with someone to whom it might be useful!

I wish you a great week! ☀️

Luca
