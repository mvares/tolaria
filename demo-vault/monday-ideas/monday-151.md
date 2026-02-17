---
aliases:
  - "Monday #151"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-monday-idea|Publish Monday Idea]]"
Status: Published
"👓 Status": Not started
"Created time": "2025-04-08T13:35:00.000Z"
Date: 2025-04-14
"Has Notes":
  - "[[evergreen/what-makes-code-easy-to-change|What makes code easy to change?]]"
  - "[[evergreen/involve-your-team-in-creating-okrs|Involve your team in creating OKRs]]"
  - "[[evergreen/write-docs-during-the-whole-lifecycle|Write docs during the whole lifecycle]]"
Tags:
  - Monday
  - Free
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 1cfbdf02-815c-8021-86c0-e0b0d74498c9
---

# Monday #151

### 1) 🎯 OKRs are actually not bad

OKRs get a lot of flak for being an overly complex / formal ritual. 

Honestly I don’t think that’s true. But it’s true that they often *fail*, and since people need to figure out *why*, the ceremony itself becomes an easy scapegoat.

In my experience, the most common reason why OKRs fail is that they are created 100% top-down, and are not participated by people in the team.

Creating OKRs—or simply goals, plans, and anything in this ballpark—is a collective process. You involve your team in the creation because 1) you want to aim at things that are grounded to reality, and 2) you want to create buy-in towards the goals themselves.

So, the ideal journey is a blend of top-down and bottom-up input. In a startup it may look like this:

1. 🎯 **Objectives** — the leadership team sketches high-level goals. These are mostly qualitative, non-measurable, and based on themes that may span multiple quarters. 

1. 📈 **KRs** — some initial KRs are created top-down, involving managers of the respective teams / functions. These KRs are totally provisional and serve as a basis for discussion.

1. 🔨 **Initiatives** — the initial version of the OKRs is presented to the team. People come up with initiatives to achieve the KRs and possibly adjust KRs themselves in the process.

1. 🔄 **Iterate** — KRs and Initiatives are challenged and improved over a couple of rounds of iteration.

![image](../assets/1cfbdf02815c807a.png)

I wrote a full article about creating good OKRs, which I am attaching below 👇

[https://refactoring.fm/p/how-to-create-good-okrs-](https://refactoring.fm/p/how-to-create-good-okrs-)

---

### 2) 📑 Write docs throughout the whole SDLC — not just at the end

These days we often talk about AI *revolutionizing *docs, because of two factors:

1. AI writes (and maintains) high-quality docs effortlessly, from inline comments to full design docs.

1. AI is able to fetch docs from pretty much wherever they are, reducing the need for perfect organization.

That said, we still need to figure out *what* docs are useful to write and maintain, even if we’ll be telling AI to do so.

I have found that teams that are good at writing docs, all have a major property in common: they don’t write docs only *at the end* of a project—they write them throughout its whole lifecycle.

In fact, writing docs—of whatever kind—has many benefits:

1. 💭 **Help your reasoning** — writing is thinking. Going through the process of writing a formal document helps solidify your reasoning and come up with a better solution.

1. ⚡ **Improve output** — you can support your writing with previously created templates, checklists, and examples. These make the work lighter and lead to better results.

1. 💬 **Improve communication** — it is easier to have good conversations about complex topics when these are backed by writing. You get more thorough reasoning and easier convergence.

1. 📔 **Future reference** — docs naturally record decisions and can be used for posterity.

These benefits happen throughout the whole life of a project, from inception to release to future maintenance.

![image](../assets/40c676b0f31047ef.webp)

Now, I have found that most teams **over-index on the future reference** use case, while neglecting the first two. But writing docs only *after* the fact is like retrofitting unit tests to production code: not completely useless, but you miss out on a lot of value.

Also, writing docs at the end is genuinely harder than doing it gradually while the work is in progress. Artifacts like meeting notes and design docs are not only useful *per se —* they naturally turn into long-term docs, later, with very little effort.

So the best way to write more docs — and write better ones — is usually to find ways to write them *throughout* the whole project lifecycle.

I wrote a full guide about creating good documentation, which you can find below 👇

[https://refactoring.fm/p/how-to-write-documentation](https://refactoring.fm/p/how-to-write-documentation)

---

### 3) ✅ High-quality code == easy to change

Before discussing how AI changes things, we need to establish what makes code truly maintainable. After all, you can't improve what you don't understand.

Many people conflate code quality with abstract notions of "cleanliness" or adherence to specific patterns. But in my opinion there's only one thing that really matters: **how easy it is to change the code**.

This is not just theoretical. When code is hard to change, velocity slows down and engineers spend more time maintaining existing stuff than writing new features.

To me, code that is easy to change displays three fundamental traits:

#### 1) Easy to understand 📖

The first trait of maintainable code is readability. Code that can be easily understood by anyone on the team, regardless of who wrote it or when it was written, is code that can be safely modified.

Here are the key elements that make code easy to understand:

- 🏅 **Clear responsibilities** — each component having a single, well-defined purpose is the foundation of easy understanding. When a file or class tries to do too many things, it becomes harder to grasp and riskier to modify.

- 📁 **Intuitive structure** — your codebase should be organized in a way that makes things easy to find. This includes: meaningful folder structure that reflects your domain, consistent file naming conventions, clear separation between different layers (e.g., UI, business logic, data access). I wrote more about naming & structure in [this previous piece](https://refactoring.fm/p/how-to-name-things?utm_source=publication-search).

- 💬 **Good comments** — some argue for self-documenting code, but I have found that the best teams consistently write good comments. The key is finding the right balance: I am not a fan of inline comments and overly micro stuff, but I always appreciate comments at the top of files/classes describing their primary goal, or a quick explanation of complex business logic that isn’t immediately obvious from the code.

#### 2) Small chance of regressions 🎯

The second trait of maintainable code is **confidence** — how sure are you that your changes won't break something else?

This confidence primarily comes from good testing. This is not just about high coverage, it's about having the right tests that give you the most value:

- **Integration tests** — in my book, these often provide the best ROI, as they can cover large parts of your codebase while being more resilient to refactoring than unit tests.

- **E2E critical testing** — identify the core business flows and harden them first. A bug in your login page is more critical than one in an admin dashboard.

- **Test readability** — good tests also serve as docs. When a test fails, it should be immediately clear what went wrong and why.

I wrote a lot about 1) [good testing](https://refactoring.fm/p/how-to-test-software-in-2023), and 2) [modern QA](https://refactoring.fm/p/how-to-do-qa-in-2024), if you want to dig more!

#### 3) Good abstractions 🏗️

The final trait is having abstractions that match your business domain, which to me is the very [definition of low technical debt](https://refactoring.fm/p/the-true-meaning-of-technical-debt?utm_source=publication-search). This is perhaps the hardest to get right, as it requires tech expertise + domain knowledge, for which you need good collaboration between stakeholders.

When abstractions are poor, tech debt sneaks in. The best teams handle this in a variety of ways, which we covered in our [full guide](https://refactoring.fm/p/the-definitive-guide-to-manage-technical?utm_source=publication-search).

The relationship between these three traits is often hierarchical: readable code makes it easier to write good tests, and good tests give you the confidence to improve your abstractions.

However, maintaining these qualities becomes more challenging in the age of AI. When code is increasingly being generated by machines, how do we ensure it remains easy to change?

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
