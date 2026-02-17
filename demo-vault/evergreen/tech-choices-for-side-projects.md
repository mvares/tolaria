---
aliases:
  - "Tech choices for side projects"
"Is A":
  - Evergreen
Tags:
  - Has Pic
"Created at": "2024-04-18T14:44:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to":
  - "[[essay/how-to-build-side-projects|How to Build Side Projects]]"
  - "[[monday-ideas/monday-73|Monday #73]]"
"Old Created At": "2023-10-06T15:13:00.000+02:00"
"Updated at": "2024-04-19T09:37:00.000Z"
Status: Discarded
Tweet: "CTOs, when choosing tech for side projects, clarity is key. Are you learning or shipping an MVP? Mixing goals can derail your progress. Consider using proven tech wisely, and if you want to ship fast, rethink your database. Tools like Airtable or Google Sheets can streamline your workflow and reduce lock-in. Let's discuss: how do you balance innovation with practicality in your projects?"
notion_id: 5b0930bd-fbd1-4930-90c7-1ae3ab00ff2a
---

# Tech choices for side projects

What tech should you use for your side projects? It depends on your goal.

- Is your goal *learning*? Try some new shiny stuff.

- Is your goal shipping an MVP asap and making some money? Use the stack you are most comfortable with.

Not rocket science, of course, but it is still easy to *fuck this up* when you start a project with *conflicting* goals in mind, like: “*I want to create a good SaaS and also learn some new tech”*.

While doing both is not impossible and can even be good for your motivation, think about McFunley’s [innovation tokens](https://mcfunley.com/choose-boring-technology#:~:text=him%20only%20slightly.-,Embrace%20Boredom.,-Let%E2%80%99s%20say%20every) and choose wisely where to use proven tech, and where to take some calculated risks.

To accelerate development, then, consider two things:

- 🍱 **Keep a boilerplate of your favorite stack** — Vic maintains a Github repo with everything he needs to start a new SaaS instantly, complete with payments, auth, backoffice, and UI scaffolding.

- 🪄 **Use no/low-code tools** — there exist plenty of handy tools to lift coding weight from your shoulders. I wrote a full article about them a while back 👇

[**How to Build Anything with No-Code 🪄**](https://refactoring.fm/p/how-to-build-with-no-code)

Feel free to read the full article, but I am also going to give you a hot take: if you are serious about shipping fast, the #1 component to *low-codify* is probably your *database*, by replacing it with something like **Airtable** or **Google Sheets**.

I know, this looks insane, and it also goes against everything I have written in the past about choosing boring / exciting tech 👇

Your database is arguably the most important component of your stack, *and* the one with the highest lock-in — Luca wtf?!

![image](../assets/f9cc34af790b4190.png)

However, consider this:

- Data needs to be edited, and with Airtable/GS you get an awesome admin UI for free.

- Data needs permanent, paid hosting (as opposed to functions and frontend these days) — which you get for free on Airtable/GS.

- Airtable/GS can express an awful lot of business logic via formulas and references, all of which you should code otherwise.

- Airtable/GS give you CRUD API for free.

- Airtable/GS play nicely with plenty of other tools out there, including workflow ones like Zapier, for even more automation.

So think about it!
