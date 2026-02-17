---
aliases:
  - "How to Name Things"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-essays|Publish Essays →]]"
Status: Evergreened
URL: "https://refactoring.fm/p/how-to-name-things"
"👓 Status": Not started
"Date HH": 2024-12-12
"Created time": "2024-04-18T14:53:00.000Z"
Date: 2023-09-14
"Has Notes":
  - "[[evergreen/naming-files-and-folders|Naming files and folders]]"
  - "[[evergreen/names-are-abstractions|Names are abstractions]]"
  - "[[evergreen/clever-vs-descriptive-names|Clever vs descriptive names]]"
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: cc5e68d4-7721-4a3a-b174-0d66c9c2e48c
---

# How to Name Things

### 📑 Materials

---

> *There are only two hard things in Computer Science: cache invalidation and naming things.*

Phil Karlton reportedly came up with this during his time at Netscape, in the late 90s, and it has stayed one of the most popular programming jokes ever since.

A common trait of successful jokes and comedy in general is that they reveal some surprising truth, in a witty way. In fact, I even believe that *laughing *is something we developed, as human beings, to show appreciation towards others’ brilliance — but I digress.

What I want to say is that, if that programming joke is popular, is because it is true in some way. Leaving aside cache invalidation for today, during my career, naming things *well* has been indeed very hard, and very often.

I believe naming things is hard for the combination of two factors:

- ⬆️ **High importance **— good names are important for a surprisingly long list of *deep *reasons, from software itself to communication. 

- ⬇️ **Low consensus **— there is very little out there about how to name things in software. If you search for resources and articles (as I did), most advice focuses on low-level rules about basic hygiene, like using snake_case or camelCase, or starting boolean vars with *is* / *has*. Well, that’s not what makes naming hard.

So, as always on Refactoring, let’s address this from first principles, and move top-down from them.

This article is a collection of ideas, mental models, and tactics that served me well over time. It is bound to be controversial and you may not agree with a lot of what I say. But even if you disagree with most of it, if it makes you think more about this subject while doing so, consider it a win!

So here is what we will cover today:

- 💬 **Names matter **— why good names go a long way, and why bad ones are worse than you think.

- 📡 **Systems and services **— naming strategies for your big architecture pieces, and the feud between *clever* and *descriptive* names.

- 📂 **Folder structures / architectures **— discussing discoverability, using context, and a *critique* of the screaming architecture.

- 🔧 **Naming classes and functions **— discussing nouns, verbs, prefixes, and *grep-ability*.

- 📊 **Keeping consistency** — because good rules are only half of the job.

Let’s dive in!

---

### 💬 Names matter

When you think about it, naming things is hard *only* because we care about it. But why should we?

When I was studying CS at university, I remember going through the [GoF design patterns](https://en.wikipedia.org/wiki/Design_Patterns). One of the main benefits of those patterns is that they build a shared language through which we can describe complex ideas with simple words. Today, if I say I need a *proxy*, a *singleton*, or an *adapter*, most engineers understand what I mean (I hope).

So, names are vectors of meaning. They are like mini abstractions: done right, they label concepts to simplify work and communication. Done wrong, they hold you back, confuse people, and make your work inflexible.

This is true at all levels and works like a fractal: from the [Ubiquitous Language](https://martinfowler.com/bliki/UbiquitousLanguage.html) you develop for your domain, down to the conventions you set for naming methods.

So let’s go top-down 👇

### 📡 Systems and services

I have created separate chapters for naming strategies based on the level of granularity of your pieces of software.

This wasn’t the original plan, but while I was writing this article I realized that my ideas about naming e.g. big systems were different — sometimes radically — from those about e.g. classes and functions.

One area where I am conflicted is the feud between *clever *names vs *descriptive* names:

- 💡 **Clever names** — names that are either *wordplays,* or character names, or else, that have some indirect relation (or not!) to what they refer to. E.g. Dropbox’s feature flag service is called *Gandalf*, because *thou shall not pass.*

- ✏️ **Descriptive names** — names that explicitly refer to what something is doing. E.g. replacing *Gandalf *with a more mundane *FeatureFlagService*.

Most advice out there is adamant about *avoiding* clever names,* *and always using descriptive ones instead. I found this true for individual classes, components, and (of course) methods, but not necessarily for services.

#### 💡 Clever names

Naming systems and services feels different from naming stuff inside code. One reason might that services are *singletons:* e.g. there is exactly *one *auth system at any given time, or *one* feature flag service.

When stuff is *individual* and doesn’t follow a pattern, there is no point in using conventions. Putting “*Service”* at the end of “*FeatureFlagService”* doesn’t tell me much about other services.

Also, descriptive names invariably reduce your design space. After naming your service *FeatureFlagService*, it becomes difficult to evolve it into anything else, such as running A/B tests for marketing or handling access control for features. Although technically possible, the original service would then feel misnamed.

Conversely, I will probably remember that Dropbox’s feature flags were handled by *Gandalf* until I die.

Radoslav Stankov, former Head of Engineering at Product Hunt, told me his take on this 👇

> *I avoid clever names and go with direct names when it is related to code, except in cases we build something larger or cheeky. Like in Product Hunt, we had a sub-system called Housekeeper, which was going to our product db and did some maintenance tasks.*

The typical objection to this approach is: how does it scale when you have tens or hundreds of services? This always reminds me of this awesome [Krazam video](https://www.youtube.com/watch?v=y8OnoxKotPQ).. Names in the video are funny, of course, but the real problem is the proliferation of services. No matter what you call this mess, it's not going to get prettier. You'll have to look up documentation all the time anyway.

> *In general, I prefer descriptive names when it comes to code (classes, variables, etc).  Codenames can be fun and motivational for projects, but I try to keep them out of code artifacts where they'll eventually be obscure to people who weren't there for the project which created them. An exception would be for big complex systems. If a system's purpose can't be easily described in a few words anyway, then understanding what it's for will take learning. In that case a pithy name or codename can be a fine way to uniquely identify the system to anyone who's had the introduction. Bonus points if the name is evocative of the right concepts.

— Andrew Twyman, former Staff Engineer at Dropbox*

Now, I don’t want this to feel like an endless ode to clever names — descriptive ones are fine, of course, but for them to work you need to cover more bases than you might think: they should be consistent with your domain language, describe the right scope, and not overload existing concepts. Whenever this happens, that’s perfect! Otherwise, calling your service “[*Bingo —*](https://youtu.be/y8OnoxKotPQ?t=17)[ ](https://youtu.be/y8OnoxKotPQ?t=17)[*because it knows everyone’s name-o*](https://youtu.be/y8OnoxKotPQ?t=17)*” *is fine, too!

#### 🤝 Conventions and abstractions

A lot of the advice above is a variation over one of the golden rules in software engineering: *do not create premature abstractions*.

Names and naming conventions are particularly *sneaky* because they may not feel like abstractions, but they are. 

Conventions should encode something repetitive, so that when I see one I immediately understand what it does. Instead, codebases are often full of -*Managers*,* -Providers*, -*Services* that have pretty much nothing in common. When I see an *EmailManager*, I will ask myself: *what does a Manager do?* If there isn’t a good answer for that, then 1) it’s confusing, and 2) you are *polluting* the “Manager” keyword for anybody who wants to use it for good in the future.

Of course, it goes both ways: when there is a convention in place, you should use it whenever it is fitting.

### 📂 Folder structures / files

Names are also important for making the various parts of the codebase discoverable — especially file names and folder structures. 

There are two main ways you can find something in a codebase:

- 🔍 **Direct search** — you *grep* for a file/folder name, or part of a name.

- 🔀 **Navigation** — you navigate through the folder structure.

In almost any codebase, good structure for navigation matters more than individual file names. If you do well with the former, in fact, you get some leeway for screwing up the latter, while the opposite is not true.

So, as a rule of thumb, you want to keep as little context as possible encapsulated into file names. E.g. if you have a Hero component, you should rather call it Hero.js and put it into the *components *folder, rather than calling it HeroComponent.js and put into a higher level one.

This may be trivial example, but there are many cases that are not. In general, be suspicious of two things:

- Too much context going into file names

- Bland folder structure that does not tell you anything about the product domain.

About the latter, I am generally a fan of the [Screaming Architecture](https://blog.cleancoder.com/uncle-bob/2011/09/30/Screaming-Architecture.html) approach by Robert Martin, which promotes creating structures that *scream* the domain they are about. He compares software architecture to building architecture: when you look at blueprints of a building, you should immediately understand what the building is about. If you see a kitchen, a living room, and a bedroom, you know you are looking at a residential building. And the same goes for software.

I have a caveat, though.

Martin appears to view the structures promoted by full-stack frameworks such as Rails or Spring as a negative example.

The way I see it, to stay within the *building *metaphor, is that frameworks like Rails are ways to create blueprints for different types of buildings. So, it’s like Rails is for building residential homes, and it gives you already a folder structure with a Kitchen, Bathrooms, Dining room, etc.

This is undeniably good for many reasons:

- Everybody knowing the framework knows where to look at in any project.

- It teaches everyone the basics of what residential homes should look like.

Of course, this means the framework is opinionated and you may not agree with it, but if you do, instead, it saves you a ton of cognitive effort.

There is still room for a *screaming architecture*, then, inside business logic folders.

### 🔧 Naming classes and functions

Moving a level below, you get classes and functions. Here are the ideas that have helped me the most with naming:

#### 1) State and behaviour

Whether you use OOP, functional programming, or else, all applications have some notion of *state* and *behavior*:

- **State **— is the data you store and work on (edit, delete, etc)

- **Behaviour **— are basically actions on such data.

This might sound obvious to you, but I have found that good things happen when state is *encapsulated *in a way that behavior is simple and only acts on one thing at a time.

Let me explain.

When I drive a car, I move the whole car forward. *Car* is a single concept: I don’t say that I move the wheels + the chassis + the seats. Likewise, in software, nouns should encapsulate meaning so that verbs are simple: get, delete, edit, send, etc.

So, be suspicious of functions that are called *doThisAndAlsoThat* — chances are this is not a naming problem, but a more foundational issue with how your state is organized.

#### 2) Prefixes and suffixes

Prefixes and suffixes in code get a lot of usage not only for namespacing and abstractions (see sections above), but also to make things more *searchable, *or *grep-able*,* *if you prefer.

Rado wrote another great take on this 👇

> *I make heavy use of prefixes to make things grep-able. Examples:
– I have all tracking events in the Angry Building Website to be prefixed with "ab_". This way, I can distinguish between custom events and analytics library build-in.
– At Product Hunt, all of our feature flags were named "ph_[something]" This made it very easy to search in the code base. I f team had expanded more, and I would have pushed for."ph_[team]_[feature]"

As much as I use prefixes in the naming of objects when it goes to local variables, having long prefixed names is often a code smell that those things have to be grouped or extracted.*

The last sentence is crucial to me.

Using prefixes for searchability is good for things that have a *distributed *presence in the codebase and you can’t find all in the same place. Feature flags is a perfect example of this.

But, whenever possible, you should prefer namespacing — whatever way is best for your situation: folders, modules, etc — over prefixes (or suffixes).

### Local hygiene

- Don’t abbreviate

- Consistency about horizontal concepts/actions

- Pyramid of conventions

### 📊 How to keep consistency

Defining good naming rules is difficult, and it's only half the job. The other half is actually following them.

In my experience here is how good teams stay consistent with names 👇

#### 1) 🔍 Linting

Linting may only be useful for low-level rules, but it’s still a no brainer. 

With good linting you can enforce things like using the right case for variables and functions, and write [custom rules](https://medium.com/baracoda-engineering/writing-custom-lint-rules-to-maintain-naming-conventions-52955f116d1f) for your use cases. 

#### 2) 🧑‍🤝‍🧑 Code reviews / pair programming

I put these two together because they both belong to the same category: *use a second pair of eyes*.

Collaboration is invaluable at enforcing standards, for two reasons:

- **Mistakes **— naming conventions are not caught by tests, so you need other humans to correct mistakes.

- **Unwritten rules **— as disciplined as you can be with docs, there always exist *unwritten rules *and stuff that only some engineers know.

If I had to choose, I prefer pair programming to code reviews for this, because it is always *pesky* to comment on naming stuff in reviews. Not all engineers will do that, to avoid being pedantic. So, it is better to prevent than cure.

Another *prevention* tactic is simply asking for help 👇

#### 3) 🙋‍♂️ Ask for help

I love the advice by Titouan Benoit, CTO of Dotfile, about this:

> *When you feel it is not describing your variable or feature well, try to get help from others, we use to send small poll on slack to tests naming with others (also outside the tech team when relevant or product related)*

Naming things together, especially *important* things like systems or big abstractions, is a power move, for many reasons:

- **Improve the name** — other devs might have more context on when some word is already used and suggest better options, or may simply have better ideas.

- **Create buy-in** — especially when you use clever names, it is important to get people on board with them.

- **Spread knowledge **— naming things together is also a shortcut to make everyone familiar with any name you choose in the end.
