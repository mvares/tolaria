---
aliases:
  - "Why code reviews matter: two extremes"
"Is A":
  - Evergreen
"Last Tweeted": 2024-08-26
Tags:
  - Has Pic
"Created at": "2024-07-26T10:02:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to":
  - "[[essay/thoughts-on-code-reviews|Thoughts on Code Reviews]]"
  - "[[monday-ideas/monday-142|Monday #142]]"
"Updated at": "2025-02-04T14:29:00.000Z"
Status: Not started
Tweet: "Code reviews shouldn't be a bottleneck or an afterthought. They’re essential for quality and team culture. Yet, too many teams swing between no reviews and painfully slow ones. Find the balance: fast, thorough reviews can boost productivity and collaboration. What’s your take on optimizing code reviews?"
notion_id: 36a1b27f-90b6-4c44-ad0d-9c40af16f1eb
---

# Why code reviews matter: two extremes

Why code reviews matter: two extremes

This question seems simple.

While the *main* goals (quality, knowledge sharing) are obvious, reviews have second and third-order effects that are worth discussing.

Code reviews are the main (and possibly only) **feedback loop** on how your team writes code.

This feedback loop not only catches defects but also aligns practices and culture. From high-level engineering principles to naming conventions, many of these are enforced and even born out of code reviews.

#### A no-reviews story ❌

I worked as an EM on a team that didn’t review code. The team of 4 senior engineers pushed code to prod all the time.

Things seemed fine, and code quality was good, but there were invisible problems:

- **Gatekeeping** — Each engineer had personal areas of ownership, impenetrable to others.

- **Inconsistency** — Different parts of the code had inconsistent naming, libraries, folder structures, etc.

- **No docs** — Little incentive to write and update docs.

These problems eventually led to more issues:

- **Collaboration** — Design, tradeoff, or estimate discussions were hard due to silos.

- **Hiring** — Onboarding new engineers was a nightmare.

- **Resource allocation** — Hard to invest in specific product areas.

- **Key man risk** — Individual engineers became too important, which was concerning.

This story shows the impact of not doing reviews goes beyond “*more bugs in prod*”. It affects almost everything you do in the long run.

#### A slow-reviews story 🐌

The other end of the spectrum is equally bad. Bad code reviews are usually *bad* in two ways, often simultaneously:

- **They are slow** — delaying release for hours or days.

- **They are superficial** — not improving the code or sharing knowledge.

Superficial reviews have the same problems as *no-reviews*, so no need to elaborate.

Slow reviews mess up engineers’ work. Once a developer submits a PR, their work isn’t over: they may need to implement improvements based on the review and ensure everything works in production.

Including several hours of delay (multiplied by review iterations) makes engineers switch tasks, increasing WIP, cognitive load, reducing productivity, leading to batched releases, and a cycle of *badness.*

![Slower time to production reduces productivity and literally increases the number of devs you need to do the same things.](../assets/f19a16a683124b95.webp)

---

Code reviews are not about catching bugs — they are much more.

They are your main feedback loop on how your team writes code.

Still, many teams are caught in extremes where code reviews (or lack thereof) become detrimental to their team:

🚫 𝗧𝗛𝗘 𝗡𝗢-𝗥𝗘𝗩𝗜𝗘𝗪 𝗧𝗥𝗔𝗣
I once joined a team of senior engineers who pushed code directly to prod, without review.

It seemed efficient, and tbh quality was not bad, but invisible problems had grown over time:

↳ Siloed ownership — 𝘦𝘢𝘤𝘩 𝘦𝘯𝘨𝘪𝘯𝘦𝘦𝘳 𝘩𝘢𝘥 𝘥𝘦𝘷𝘦𝘭𝘰𝘱𝘦𝘥 𝘵𝘩𝘦𝘪𝘳 𝘰𝘸𝘯 "𝘬𝘪𝘯𝘨𝘥𝘰𝘮", 𝘶𝘯𝘵𝘰𝘶𝘤𝘩𝘢𝘣𝘭𝘦 𝘣𝘺 𝘰𝘵𝘩𝘦𝘳𝘴

↳ Inconsistencies — 𝘥𝘪𝘧𝘧𝘦𝘳𝘦𝘯𝘵 𝘴𝘵𝘺𝘭𝘦𝘴, 𝘭𝘪𝘣𝘳𝘢𝘳𝘪𝘦𝘴, 𝘢𝘯𝘥 𝘴𝘵𝘳𝘶𝘤𝘵𝘶𝘳𝘦𝘴 𝘢𝘤𝘳𝘰𝘴𝘴 𝘵𝘩𝘦 𝘤𝘰𝘥𝘦𝘣𝘢𝘴𝘦

↳ Documentation drought — 𝘯𝘰 𝘪𝘯𝘤𝘦𝘯𝘵𝘪𝘷𝘦 𝘵𝘰 𝘸𝘳𝘪𝘵𝘦 𝘰𝘳 𝘮𝘢𝘪𝘯𝘵𝘢𝘪𝘯 𝘥𝘰𝘤𝘴

These problems had led to more ripple effects: collaboration suffered, onboarding became a nightmare, and we couldn't easily allocate resources to different product areas.

🐌 𝗧𝗛𝗘 𝗦𝗟𝗢𝗪 𝗥𝗘𝗩𝗜𝗘𝗪 𝗦𝗟𝗢𝗚
On the flip side, mandatory, slow reviews can be just as detrimental:

↳ Productivity killer — 𝘭𝘰𝘯𝘨 𝘸𝘢𝘪𝘵 𝘵𝘪𝘮𝘦𝘴 𝘧𝘰𝘳𝘤𝘦 𝘤𝘰𝘯𝘵𝘦𝘹𝘵 𝘴𝘸𝘪𝘵𝘤𝘩𝘪𝘯𝘨, 𝘪𝘯𝘤𝘳𝘦𝘢𝘴𝘪𝘯𝘨 𝘞𝘐𝘗
↳ Batched releases — 𝘥𝘦𝘭𝘢𝘺𝘴 𝘭𝘦𝘢𝘥 𝘵𝘰 𝘭𝘢𝘳𝘨𝘦𝘳, 𝘳𝘪𝘴𝘬𝘪𝘦𝘳 𝘳𝘦𝘭𝘦𝘢𝘴𝘦𝘴
↳ Increased cognitive load — 𝘦𝘯𝘨𝘪𝘯𝘦𝘦𝘳𝘴 𝘫𝘶𝘨𝘨𝘭𝘦 𝘮𝘶𝘭𝘵𝘪𝘱𝘭𝘦 𝘵𝘢𝘴𝘬𝘴, 𝘳𝘦𝘥𝘶𝘤𝘪𝘯𝘨 𝘧𝘰𝘤𝘶𝘴 𝘢𝘯𝘥 𝘲𝘶𝘢𝘭𝘪𝘵𝘺

🎯 𝗧𝗛𝗘 𝗦𝗪𝗘𝗘𝗧 𝗦𝗣𝗢𝗧

The ideal code review process hits a sweet spot between being fast and being thorough.

This is easier said than done, and I wrote more about it in this recent free article 👇
