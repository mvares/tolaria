---
aliases:
  - "Human engineers still do the most valuable work"
"Is A":
  - Evergreen
Tags:
  - Not for Monday
"Created at": "2025-02-11T10:10:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to": "[[essay/will-ai-replace-engineers|Will AI Replace Engineers?]]"
"Updated at": "2025-11-13T16:13:00.000Z"
Status: Not started
notion_id: 197bdf02-815c-80f5-8d77-d03233edfda5
---

# Human engineers still do the most valuable work

A couple of days ago Addy Osmani wrote [this fantastic piece](https://newsletter.pragmaticengineer.com/p/how-ai-will-change-software-engineering?utm_source=post-email-title&publication_id=458709&post_id=154200840&utm_campaign=email-post-title&isFreemail=true&r=3u2qm&triedRedirect=true&utm_medium=email) on The Pragmatic Engineer about AI-assisted coding. It perfectly matches my own experience and I found myself nodding throughout the article.

So let me tell you this story. For a few years now I have had this itch of building a native note-taking app for macOS.

Today, for my notes I rely on a combination of Notion (long-term workspace), [Bear](https://bear.app/) (quick capture), and [Voicepal](https://apps.apple.com/us/app/voicepal-your-ai-ghostwriter/id6471552007) (audio notes), because no single app matches my looong list of ideal requirements (offline-first, API-ready, markdown-based, tags, audio, …).

Now, I know my way around design, but I know absolutely nothing about native macOS development. Zero. Nil. I don’t even know the Swift’s syntax. Still, over the past two months I rolled up my sleeves and tried to *AI* my way around it. I did a basic design on Figma and used Cursor as my main IDE.  

To my surprise, I managed to get to a (pretty awesome) working version: it syncs content with [Sanity](https://www.sanity.io/), supports nested tags and the most common markdown syntax 👇 

![image](../assets/197bdf02815c809c.png)

It also has a lot of handy things that I miss from other apps, like my favorite shortcuts and—I am very proud of this one—one-click to copy the HTTP GET URL for both single notes and entire collections, so I can easily add them as self-updating context to AI.

All the code was written by Cursor, because, again, I don’t know how to write proper Swift. But doesn’t mean I didn’t do any engineering work:

- I told AI I wanted to use Sanity to store notes, because this would save me from writing a proper backend and I would get API and version control for free.

- I told AI I wanted to use [CRDTs](https://en.wikipedia.org/wiki/Conflict-free_replicated_data_type) to enable concurrent changes across multiple devices, and instructed it to use the [Automerge](https://automerge.org/) library to do so, instead of implementing everything from scratch (which, if left unchecked, was very happy to do).

- I regularly broke work down into small, independent features that could get done with as little context as possible.

- I did an awful lot of debugging which, even though I don’t know Swift, still relied on my engineering *instincts*.

So, while there is no doubt this whole project was *enabled* by AI, there was a lot of engineering work done by a human. Also, it was work of the highest caliber: system design, buy vs build, scoping — these are some of the hardest, most important things that people get done in any project, and that require the most expert judgment.
