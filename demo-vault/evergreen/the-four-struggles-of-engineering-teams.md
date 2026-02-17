---
aliases:
  - "The four struggles of engineering teams"
"Is A":
  - Evergreen
"Last Tweeted": 2025-12-09
Tags:
  - Has Pic
"Created at": "2025-08-18T13:30:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to":
  - "[[essay/how-to-help-a-struggling-team|How to Help a Struggling Team]]"
  - "[[monday-ideas/monday-176|Monday #176]]"
"Updated at": "2025-12-09T07:54:00.000Z"
Status: Not started
Tweet: "Engineering teams face four key struggles: value, quality, speed, and reliability. Focus on building valuable, high-quality software first—speed will follow. Prioritize feedback loops to uncover issues early. Trust fosters a productive environment, making deadlines less critical. What challenges is your team facing? #Leadership #SoftwareEngineering"
notion_id: 253bdf02-815c-808a-8923-f672a4ffff25
---

# The four struggles of engineering teams

Anna Karenina famously opens by saying: “All happy families are alike. Each unhappy family is unhappy in its own way”.

In my experience, there are four big candidates that make software teams unhappy:

1. 🏆 **Value** — what gets shipped isn’t valuable for customers / business. You build the wrong thing.

1. 🥇 **Quality** — what gets shipped is not polished and/or is constantly bugged.

1. 🥈 **Speed** — the team is (or is perceived as) slow.

1. 🥉 **Reliability** — the team doesn’t hold on its commitments.

Your mileage may vary, but as a rule of thumb, I argue these matter exactly *in this order*.

![image](../assets/23fbdf02815c80b5.png)

Working on the right things is *by far* the most important factor, and what most teams struggle the most with. However, this isn’t always identified correctly: people have a lot misguided conversations about *speed*, where what they really mean is: “*we are not confident that what we ship is good, so better to ship more things faster*”.

But the reality is, teams that ship valuable + high quality stuff (#1 + #2) rarely get questioned about speed.

To work on the right things you need good feedback loops with customers, and feedback loops are what make speed genuinely useful. Otherwise, you may be running fast, but in circles.


Finally, reliability — meant as meeting deadlines, making good estimates, etc — is just cherry on top. When trust is created through the other factors, you discover most deadlines are fictional and estimates are not that useful. In most cases, these are control devices meant to make up for low-trust environments, and most often failing at that. Under good conditions, instead, you can relax a lot of the process and just let people work.

So, how do you figure out what of these problems plague your team?

To me, this is the part where the process stops being workshop-ish, like in the vision stage, and becomes more continuous. You might be able to spot a bunch of these issues at once, but what you need the most is having a good feedback loop in place to intercept them as they appear.

Some of the best devices for this are [1:1 chats](https://refactoring.fm/p/how-to-run-great-11s-in-2023), [retrospectives](https://refactoring.fm/p/retrospectives), and [dev surveys](https://refactoring.fm/p/whats-next-in-measuring-dev-productivity). I have written various times about these so I am just putting some links to previous articles.

There are also [quantitative engineering metrics](https://refactoring.fm/p/how-to-get-started-with-engineering), of course. In my experience, though, they come at a later time — when the team has already a good posture towards problems and some bandwidth to go more in depth. That is, quantitative data may precisely surface that your time-to-first-PR is 14 hours, which is useful to know to track the trend, but people can (and should) already tell you in surveys and 1:1s that your PR process is shit, and that’s enough to make progress start.
