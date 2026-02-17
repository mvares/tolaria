---
aliases:
  - "Minimum Viable Testing Process"
"Is A":
  - Evergreen
"Last Tweeted": 2025-12-02
Tags:
  - Has Pic
"Created at": "2024-04-18T14:44:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to":
  - "[[essay/how-to-test-software-in-2023|How to Test Software in 2023]]"
  - "[[monday-ideas/monday-55|Monday #55]]"
  - "[[monday-ideas/monday-184|Monday #184]]"
"Old Created At": "2023-03-31T18:20:00.000+02:00"
"Updated at": "2025-12-02T08:32:00.000Z"
Status: Not started
Tweet: "CTOs, let's talk minimum viable testing.\n\n1️⃣ Use a statically typed language to catch bugs early and document your code.\n2️⃣ Write unit tests where it counts, don’t stress coverage.\n3️⃣ Prioritize integration tests that reflect real user paths.\n4️⃣ Invest in critical end-to-end tests to replace manual checks.\n5️⃣ Skip staging when possible—feature flags and live previews can streamline your releases.\n\nWhat’s your testing strategy? Let’s discuss!"
notion_id: 2420da0a-b8b3-4e3a-8bbd-d336aaa9c031
---

# Minimum Viable Testing Process

What does minimum viable testing look like?

Testing is one of the topics on which I receive the most questions on the newsletter. But the questions are usually not like: “how do I test things thoroughly? They are rather “how do I get the best bang for my buck?”

So as always YMMV, but here is my quick cheatsheet

𝟭) 𝗨𝘀𝗲 𝗮 𝘀𝘁𝗮𝘁𝗶𝗰𝗮𝗹𝗹𝘆 𝘁𝘆𝗽𝗲𝗱 𝗹𝗮𝗻𝗴𝘂𝗮𝗴𝗲

Most languages today have statically typed versions you can adopt, e.g. Typescript for Javascript, or Sorbet for Ruby.

My opinion is that this is a no-brainer for 99% of teams. 

Static typing not only catches *a ton* of bugs early, it also documents the code thanks to types and annotations, making it easier for others to understand what’s going on.

𝟮) 𝗪𝗿𝗶𝘁𝗲 𝘂𝗻𝗶𝘁 𝘁𝗲𝘀𝘁𝘀 𝘄𝗵𝗲𝗻 𝗿𝗲𝗹𝗲𝘃𝗮𝗻𝘁

Unit tests are still an important part of your testing investment. However, I am not adamant about their coverage — you should write them for whatever is non-trivial or subject to implementation changes in the future.

𝟯) 𝗪𝗿𝗶𝘁𝗲 𝗽𝗹𝗲𝗻𝘁𝘆 𝗼𝗳 𝗶𝗻𝘁𝗲𝗴𝗿𝗮𝘁𝗶𝗼𝗻 𝘁𝗲𝘀𝘁𝘀

Integration tests are about testing execution *paths* that involve multiple functions / components. Figure out the most important ones for each area of your product, and test them in depth. To identify them, you can often think about *business* paths, based on how your product is used.

API endpoints are also good candidates for integration tests.

Sometimes, the difference between unit and integration tests is a bit *murky*,* *but it doesn’t matter that you are able to separate those precisely. Just focus on what feels worthwhile to be tested.

𝟰) 𝗪𝗿𝗶𝘁𝗲 𝗮 𝗳𝗲𝘄, 𝗰𝗿𝗶𝘁𝗶𝗰𝗮𝗹 𝗲𝗻𝗱-𝘁𝗼-𝗲𝗻𝗱 𝘁𝗲𝘀𝘁𝘀

End-to-end tests are expensive to develop and maintain. My rule of thumb is to invest on testing those parts that you would check manually otherwise.

The main goal of end-to-end tests is to remove manual checks, so you can release faster.

If you are an e-commerce, you may start by testing the main purchase funnel, checkout included. If you are a SaaS, you may test that new customers are able to subscribe, and the core features used by your existing ones. 

𝟱) 𝗔𝘃𝗼𝗶𝗱 𝘀𝘁𝗮𝗴𝗶𝗻𝗴 𝗶𝗳 𝘆𝗼𝘂 𝗰𝗮𝗻

I wrote a full article about this. TL;DR is you can probably avoid a staging environment by implementing some combination of canary rollouts and live PR previews. I also have a friend who does video walkthroughs for PR, and they look great.

The idea is: the less steps to production, the faster you release, the better feedback loop you have, which also helps stability because you recover faster from mistakes.

---

### 🔄 My Testing Process

So, when we put all these things together, this is my preferred workflow for testing:

#### 1) Use a statically typed language

Most languages today have statically typed versions you can adopt, e.g. Typescript for Javascript, or Sorbet for Ruby.

My opinion is that this is a no-brainer for 99% of teams. 

Static typing not only catches *a ton* of bugs early, it also documents the code thanks to types and annotations, making it easier for others to understand what’s going on.

#### 2) Write unit tests when relevant

Unit tests are still an important part of your testing investment. However, I am not adamant about their coverage — you should write them for whatever is non-trivial or subject to implementation changes in the future.

#### 3) Write plenty of integration tests

Integration tests are about testing execution *paths* that involve multiple functions / components. Figure out the most important ones for each area of your product, and test them in depth. To identify them, you can often think about *business* paths, based on how your product is used.

API endpoints are also good candidates for integration tests.

Sometimes, the difference between unit and integration tests is a bit *murky*,* *but it doesn’t matter that you are able to separate those precisely. Just focus on what feels worthwhile to be tested.

#### 4) Write a few, critical end-to-end tests

End-to-end tests are expensive to develop and maintain. My rule of thumb is to invest on testing those parts that you would check manually otherwise.

The main goal of end-to-end tests is to **remove manual checks**, so you can release faster.

If you are an e-commerce, you may start by testing the main purchase funnel, checkout included. If you are a SaaS, you may test that new customers are able to subscribe, and the core features used by your existing ones. 

Good tools that you can use for end-to-end testing are [**Cypress**](https://www.cypress.io/) and [**RainforestQA**](https://rainforestqa.com/). You may also consider using an agency that runs manual QA, like [**Lodestone**](lodestoneco.com), which is used by Product Hunt.

#### 5) Avoid staging if you can

I wrote a full article about this. TL;DR is you can probably avoid a staging environment by implementing a combination of:

- Gradual rollouts with [feature flags](https://refactoring.fm/p/feature-flags)

- Live previews for PRs

- Video walkthroughs for PRs (fantastic idea by [Rado](https://www.linkedin.com/in/radoslavstankov/?originalSubdomain=bg))

The idea is: the less steps to production, the faster you release, the better feedback loop you have, which also helps stability because you recover faster from mistakes.

Check out the full article for more ideas 👇

[https://refactoring.fm/p/do-you-need-staging](https://refactoring.fm/p/do-you-need-staging)

![image](../assets/e81ced3303244446.png)

---

Minimum Viable Testing 🔍

In the past few weeks I have interviewed tens of tech leaders about how they test software.

I took a ton of notes and put everything together to design a 5-steps process that works, without overwhelming engineers.

Here it is 👇

1. Use a statically typed language

Most languages today have statically typed versions, e.g. Typescript for JS, or Sorbet for Ruby.

This is a no-brainer for 90% of teams.

Static typing not only catches bugs early, it also auto-documents the code thanks to types and annotations

1. Write unit tests *when relevant*

Unit tests are still an important part of your testing investment.

However, you should not be adamant about their coverage — write them for whatever is non-trivial and/or likely subject to implementation changes in the future.

1. Write plenty of integration tests

Integration tests are about testing execution paths that involve multiple functions / components.

Figure out the most important ones for each area of your product, and test them in depth.

To identify them, think about *business paths*, based on how your product is used.

API endpoints are often good candidates.

Also, the difference between unit and integration tests is a bit murky sometimes, but it doesn’t matter. Focus on what feels worthwhile to be tested.

1. Write a few, critical end-to-end tests

End-to-end tests are expensive to develop and maintain. My rule of thumb is to invest in testing those parts that you would check manually otherwise

The main goal of end-to-end tests is to remove manual checks, so you can release faster

Examples of end-to-end tests:

– If you are an e-commerce, you may start by testing the main purchase funnel, checkout included.

– If you are a SaaS, you may test that new customers are able to subscribe, and the core features used by your existing ones.

Good tools for end-to-end testing are @Cypress_io and @rainforestqa.

You may also consider using an agency that runs some manual QA, like Lodestone.

1. Avoid staging if you can

You can avoid staging and release faster with a combination of:

- Gradual rollouts with feature flags
• Live previews for PRs
• Video walkthroughs for PRs

The less steps to production, the faster you release, the better feedback loop.

And that's it! If you found this thread useful, consider sharing someone who may like it ❤️

I write more ideas on writing good software every week on @refactoringclub.
