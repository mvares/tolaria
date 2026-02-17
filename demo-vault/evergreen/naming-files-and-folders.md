---
aliases:
  - "Naming files and folders"
"Is A":
  - Evergreen
"Created at": "2024-04-18T14:44:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to":
  - "[[essay/how-to-name-things|How to Name Things]]"
  - "[[monday-ideas/monday-89|Monday #89]]"
"Old Created At": "2023-10-06T15:22:00.000+02:00"
"Updated at": "2024-04-19T09:37:00.000Z"
Status: Not started
notion_id: 04db2e14-7a7f-4465-b82d-de93c38757f7
---

# Naming files and folders

Good names are important for making the various parts of the codebase discoverable — especially file names and folder structures.

There are two main ways you can find something in a codebase:

- 🔍 **Direct search** — you *grep* for a file/folder name, or part of a name.

- 🔀 **Navigation** — you navigate through the folder structure.

In almost any codebase, good structure for navigation matters more than individual file names. In fact, if you do well with the former, you get some leeway for screwing up the latter, while the opposite is not true.

So, as a rule of thumb, you want to encapsulate as little context as possible into file names. E.g. if you have a `Hero` component, you should probably call it `Hero.js` and put it into a `components` folder, rather than calling it `HeroComponent.js` and put it into the root.

This was a trivial example, but many similar cases are not. In general, be suspicious of two things:

- Too much context going into file names.

- Bland folder structure that does not tell you anything about the product.

About the latter, I am generally a fan of the [**Screaming Architecture**](https://blog.cleancoder.com/uncle-bob/2011/09/30/Screaming-Architecture.html) approach by Robert Martin, which promotes creating structures that *scream* the domain they are about.

He compares software architecture to *building* architecture: when you look at the blueprints of a building, you should immediately understand what the building is about. If you see a kitchen, a living room, and a bedroom, you know you are looking at a residential building. And the same should go for software.

I have a caveat, though.

Martin appears to view the structures promoted by full-stack frameworks such as Rails or Spring as negative examples — because they are *bland* and do not scream anything about your app.

The way I see it, though, to stay within the *building* metaphor, is that frameworks like Rails are ways to create blueprints for different types of buildings.

So, it’s like Rails is for building residential homes, and it already gives you a folder structure with a Kitchen, Bathrooms, Dining room, etc.

This is undeniably good, because:

1. Everybody knowing the framework knows where to look at in any project.

1. It teaches everyone the basics of what residential homes should look like.

Of course, this means the framework is opinionated and you may not agree with it, but when you do, instead, it saves you a ton of cognitive effort. Then, there is still room for a *screaming architecture*, inside the business logic folders.
