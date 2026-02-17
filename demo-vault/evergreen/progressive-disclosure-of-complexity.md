---
aliases:
  - "Progressive disclosure of complexity"
"Is A":
  - Evergreen
"Created at": "2025-06-10T06:49:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to":
  - "[[essay/interview-with-guillermo-rauch|Interview with Guillermo Rauch]]"
  - "[[monday-ideas/monday-164|Monday #164]]"
"Updated at": "2025-07-05T08:46:00.000Z"
Status: Not started
notion_id: 20ebdf02-815c-8014-b3c3-f714609527b4
---

# Progressive disclosure of complexity

One of Vercel's core design principles is what Guillermo calls "*progressive disclosure of complexity*" - creating technology that's approachable for beginners but powerful enough for enterprise needs.

This principle guides the design of Next.js, which starts with minimal code (as little as one line) but scales to power some of the internet's most sophisticated websites.

> ***"I'm building a platform that should not be intimidating for your first line of code, and gives you the superpower that you could be one day a top 30 internet website with the same infrastructure, with the same tools, with the same access."***

Guillermo draws inspiration from products like the iPhone, which can be used by both children and the elderly while still serving business professionals with complex needs.

His approach to API design focuses on what he calls *token minimization* — requiring minimal code to get started, then gradually introducing more sophisticated features as needed:

- 🏁 **Low barrier to entry** — a new Next.js project can be started with just a few lines of code.

- 🌱 **Growing with users** — complexity is only introduced when needed for specific requirements.

- 🔄 **Same technology at all scales** — the technology that powers a beginner's first project is the same that can scale to handle millions of users.
