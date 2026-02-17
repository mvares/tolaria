---
aliases:
  - "Introducing Brian"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-essays|Publish Essays →]]"
Status: Everpictured
URL: "https://refactoring.fm/p/brian?utm_source=publication-search"
"👓 Status": Discarded
"Created time": "2024-04-18T14:53:00.000Z"
Date: 2023-11-23
Tags:
  - Essay
  - Personal
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: df73299c-2411-4be2-8e59-9fc5e904ae9a
---

# Introducing Brian

### 📑 Materials

---

### ✍️ Post

---

This article is the second in a two-part series about personal knowledge management. Last week’s one covered my process and guiding principles — go check it out if you haven’t already 👇

[https://refactoring.fm/p/how-i-take-notes-part-1](https://refactoring.fm/p/how-i-take-notes-part-1)

This one, instead, is about the **workspace** I have been using for about 4 years, which I called **Brian**.

I like to give my tools the names of people, as if they were my team. Brian comes from *brain*, but I have many others, like Bridget, who keeps the budget. Stories for another time 😂

For this edition, I created a **full template** of Brian that you can clone, plus instructions on how to use it, including automations. It is a full replica of what I built for myself, also improved in various parts that I would do differently if I could restart from scratch (sigh, tech debt).

This is going to become a **permanent resource** for Refactoring members. Just like I update *my* Brian continuously, I will keep this updated and create small release notes about it.

### 🛠️ On using Notion

Brian is built in Notion but, I can’t stress this enough, you don’t have to use Notion if you don’t want. What matters is the process, which is simple enough to be replicated in any tool.

I use Notion because of how powerful and flexible it is: it has databases for organizing structured data, and APIs for building automations. But it is also slow and frustrating at times, and I know the are faster, offline-first tools out there, like Obsidian or Craft. 

All in all I am happy to stick with Notion, but this comes down to personal preference. So, in the article I will explain everything about the workspace, but I will mostly focus on the general structure, while keeping the Notion-specific parts to a minimum.

### ❓ Why this, and why now?

You may also wonder: you have been doing this for 4 years, why publishing it, and why doing it now? I have two answers to this:

1. I got to a point where Brian is a key part of my work and life. I am confident about it being useful, and this is backed by the actual things I achieved because of it, like Refactoring.

1. I believe people who journal and store their knowledge regularly will get massive leverage in the future thanks to AI. The more AI knows about us, the more it can help us. I got a glimpse of this just recently through the release of the new Notion AI Q&A, where you can literally ask questions to your workspace. Though still limited, it felt like chatting with myself, and it was magic!

![image](../assets/ba04a2c6820b4420.png)

### 📌 Agenda

So here is what we will cover today:

- 🏗️ **Structure **— the general organization of the workspace, including principles for evolving it sustainibly.

- 📊 **Dashboard** — how I do most of the action on one page

- ☀️ **Journaling** — recording your days and thoughts.

- 📑 **Notes** — the backbone of the whole workspace.

- 🗃 **Projects / Responsibilities / Topics** — a dead simple project management framework.

- 🍻 **CRM** — staying in touch with people of your life.

For clarity, I will *both* go through these in a video walkthrough, and with a written article.

Let’s dive in 👇

---

### 📹 Video walkthrough

This video covers everything I am writing in text, feel free to check it out if you prefer!

---

### 🏗️ Structure

First of all, if you are going to clone this for yourself, here is some basic advice that is specific to Notion.

The best way of using Notion, to me, is by **using databases for almost everything**. That’s because this way you can create relationships, which are powerful, and custom views for the various kinds of visualizations you need. It’s also easier to use APIs for database entries than individual pages.

Just like in software, though, **databases are rigid**. If you create too many of them and a deep network of relationships, it becomes hard to change things.

So I believe in creating as few databases as possible. Then on the same databases you can put “type” fields to separate further sub-types. 

Brian has four main databases:

- 📑 **Notes** — everything that is just captured information. Articles I read, videos, journal entries, and useful tools, are all Notes.

- 🪣 **Buckets** — everything that goes through a lifecycle, has a status, a progress, or that contains other stuff. Projects, Responsibilities, Topics, but also People, Quarters, and original articles, are represented as Buckets.

- 🗓️ **Days**  — individual days for journaling. Days *could* be buckets in theory, but I found it useful to spin ‌them off into their own table.

- ☀️ **Journal Entries **— individual entries I write on my journal. Useful to record events, thoughts, or things I achieved.

Days and Journal entries have their own databases because their scope and structure is extremely* *clear. 

Everything else is either a Note or a Bucket, which means relationships get generic names, like “*Belongs to*”, or “*Has*” that can work well with different types of records. This makes the structure more similar to a graph db than a relational one, which is just fitting if you ask me.

### 📊 Dashboard

80% of the time I spend on Brian is spent on the homepage, which acts as main dashboard. The dashboard contains actionable views of the four main areas I work the most on: Journaling, Notes, People, and Projects.

Having everything together is helpful in many ways:

1. **Single page** — I don’t have to remember / write down a bunch of different pages to do things. I even created a system-wide, custom shortcut to open up the dashboard (cmd-shift-n) with [Alfred](https://www.alfredapp.com/).

1. **Loading times **— I don’t waste time ‌loading separate pages

1. **Info at a glance **— The stuff on the dashboard is basically everything I need to pay attention to. Having it all together makes it harder to miss anything, because I have everything in front of me all the time.

PICTURE

![image](../assets/d39ac1aa3a984099.png)

### ☀️ Journaling

I use a simple journaling system that is based on two databases: **Days** and **Journal Entries**

For each day I write down four things:

- **Feel** — how I feel in the morning.

- **Rating **— how I would rate the previous day, how good it has been.

- **Grateful for **— something I am grateful for.

- **Worried about **— something I am worried about. This is optional, as I don’t want to force myself to worry about things!

I fill out these in the morning before starting to work. I do a small “standup” every day where I write these down and I briefly review my calendar and my tasks for the day.

Journal entries are stuff that happens during the day and I want to record. Each entry can be one of three things:

- 💭 **Thought **— random observations I want to capture

- 🗓️ **Event** — something that came from my calendar

- ☑️ **Task** — something meaningful I did

This part heavily relies on automations to make sure it doesn’t become a burden: Events are pulled automatically from my calendar, and Tasks from Todoist. I have used Zapier for this for many years and I recently switched to n8n because it allows me to do more (e.g. auto-associate the day to each item).

For each entry, I may connect it to other buckets or notes via the “Related to” and “Related to Notes” relationships.

I also delete a lot of the stuff that comes from the automations: I don’t want all my tasks and events to end up here — only the ones that are meaningful and I want to remember. 

### 📑 Notes

I described how I take notes in [last week’s edition](https://refactoring.fm/p/how-i-take-notes-part-1). 

The work on my notes happens in two main parts of the workspace: the dashboard, and the weekly review page.

![image](../assets/df419413310b4d41.png)

On the dashboard, I display all unreviewed notes, plus the reviewed ones that are less one week old. I do most of the reviewing during the Monday review, and some small bits on the spot.

For each unreviewed item I need to fill out the “Is A” attribute, and at least one between “Related to” (usually a topic) and “Belongs To” (project or responsibility).

If I can’t figure out any of these, it means I can’t answer the question “what this is useful for” and I should delete the note instead.

In the workspace you will find various examples of the kinds of notes I discussed in the previous edition, like article highlights coming from Readwise, clipped websites, and evergreen notes.

---

### 🗃 Projects / Responsibilities / Topics

PRT is my lightweight system for project management and organizing information:

#### 1) Projects

Projects are things I want to achieve on a defined timeframe. They have a beginning and an end, and are bigger than a single task (I can’t complete them in one sitting). I plan them quarterly, organize them as OKRs, and keep a recap of the current ones on the dashboard (see screenshot).

![image](../assets/5a4050e180cb4cf8.png)

#### 2) Responsibilities

Responsibilities** **are activities I do on a regular basis, for which I need to maintain a standard. E.g. writing on social media, or running interviews with guests. Since they are recurring, I usually have them as scheduled tasks on Todoist. For each responsibility I have a Notion page that contains the procedure to perform it, and I link that page in the Todoist task.

![image](../assets/0507f597d00a456b.png)

#### 3) Topics

Topics are simply areas of interest. A topic is anything that can be useful in the future. Examples are “frontend”, “no code”, or “sim racing”. 

![A sample AI topic you will find in the template](../assets/e74a32b4bf134d51.png)

#### 4) Bonus: Areas

Since over time I created *a lot* of PRTs, especially Responsibilities and Topics, I find useful to  group things together by area.

I created a few areas about my life and assigned a color to each of them. Responsibilities and topics belong to an area and get the same color, so I can distinguish them at a glance.

![image](../assets/fe0c4e8d935444b1.png)

Colors are only used for areas throughout the workspace, so they are consistent. When I see a red icon, I know it’s a personal thing. If it’s blue, it’s Refactoring / work.

Colors act as visual clues and I can use them across other tools, like Todoist, or my email client.

![Projects on Todoist](../assets/95c4eabbcdde4265.png)

All in all, I don’t consider areas a mandatory part of the workspace, but they are definitely useful.

---

### 🍻 CRM

I described how I use Notion for keeping track of the people I care about in two previous editions 👇

[https://refactoring.fm/i/71183836/journaling-crm](https://refactoring.fm/i/71183836/journaling-crm)

[https://refactoring.fm/p/personal-crm-template](https://refactoring.fm/p/personal-crm-template)

These already included a small template, which is now embedded in Brian (and improved).
I should say that over time I have seen countless of personal CRMs, both as templates of something (mostly Notion or Airtable) or as standalone products but they were all too complicated for me and I always ended up dropping the ball on them.

So I created this very simple workflow for myself out of frustration, and that worked great also because I can integrate it with the other journaling pieces.

Here is what I do:

#### 1) Journaling about chats

Whenever I have a meaningful conversation with somebody, I write it down as a journal entry — the calendar event gets automatically sent there — and I link the entry to the person record (I create it if it doesn’t exist). This is super fast and easy to do, and is already enough to being able to:

1. Have a place (the journal entries) where to put notes about chats

1. Know at a glance when it is the last time I spoke with somebody, and about what.
In my experience, these two use cases alone are like 80% of what a CRM is useful for.
Then, I added a couple of other things:

#### 2) Staying in touch

For people I want to actively stay in touch with, I write down a number of days, that stands for how frequently I want to stay in touch. If I write 30, that means at least once every 30 days.
Then, on the dashboard, I have a view of the people I need to reconnect with, because the last time I spoke with them (recorded in the journal) is earlier than desired.

#### 3) Tagging people

Since people live in the same Buckets table as most other stuff, I get other relationships for free, and I use the “Related to” one to link people to relevant tags.
I may put “AI” if you do relevant AI work, or “Newsletters” if you are a fellow writer.

And that’s it! This is one of the parts of the workspace that I am the proudest of, because it is extremely low effort and gets the job done.
