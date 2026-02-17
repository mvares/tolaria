---
aliases:
  - "How to use AI in your team"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-essays|Publish Essays →]]"
Status: Evergreened
URL: "https://refactoring.fm/p/how-to-use-ai-tools"
"👓 Status": Discarded
"Created time": "2024-04-18T14:53:00.000Z"
Date: 2023-06-29
"Has Notes":
  - "[[evergreen/ai-coding-use-cases|AI coding use cases]]"
  - "[[evergreen/improve-writing-with-ai|Improve writing with AI]]"
  - "[[evergreen/make-meetings-better-with-ai|Make meetings better with AI]]"
Tags:
  - Software
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 24e2c331-30c8-4845-880b-75518a659ce8
---

# How to use AI in your team

### 📑 Materials

---

- [https://newsletter.pragmaticengineer.com/p/ai-coding-tools](https://newsletter.pragmaticengineer.com/p/ai-coding-tools?utm_source=post-email-title&publication_id=458709&post_id=115649522&isFreemail=false&utm_medium=email)

- [https://martinfowler.com/articles/2023-chatgpt-xu-hao.html](https://martinfowler.com/articles/2023-chatgpt-xu-hao.html)

- [https://twitter.com/paulg/status/1668266280187580418?s=46&t=b3RUYZQx-OaP2s0THxObVw](https://twitter.com/paulg/status/1668266280187580418?s=46&t=b3RUYZQx-OaP2s0THxObVw)

- [https://dev.to/github/a-beginners-guide-to-prompt-engineering-with-github-copilot-3ibp](https://dev.to/github/a-beginners-guide-to-prompt-engineering-with-github-copilot-3ibp)

- [https://www.makeuseof.com/ai-chrome-extensions-summarize-youtube-videos/](https://www.makeuseof.com/ai-chrome-extensions-summarize-youtube-videos/)

### 💡 Ideas

---

Hey! This is the first of a series of editions that I will write about using AI for your work.

I am not exactly *early *at this. As you may have noticed, we are *bombarded* everyday with new AI tools, use cases, prompt strategies, and more.

I am not sure how people can be so *fast* at recommending things, but personally I needed a few months to embed AI into my workflows, iterate on it, figure out what works, and scrap the rest.

I made a point that I wouldn’t write an AI article until I felt I was ready to say something meaningful and I could recommend stuff that truly works for me. I feel I am ready now, so here we are!

In this edition we are going *breadth-first*, analyzing the most effective use cases for a product/engineering team, from communication to coding. As always, this is based on two things:

- **Personal experience** — I tried *all* the tools and approaches I list here.

- **Chats with other tech leaders** — from the Refactoring community and my personal network (which are increasingly becoming the same thing).

So, here is what we will cover today:

- 🛠️ **ChatGPT Setup** — I don’t use it much, and never from the website.

- 📚 **Research** — how I use AI for faster and better research.

- 💬** Meetings** — how to improve meetings and communication.

- ✏️ **Writing** — how to improve anything you write.

- 🤖 **Coding** — tools, pros and cons, and a long list of use cases.

Let’s dive in!

---

### 🛠️ ChatGPT Setup

At the beginning, I used ChatGPT for everything. Then, over time, I switched more and more to specific, *AI-enabled* tools.

In part, of course, because tools improved. But that’s also because AI works best when it has *context* about what your are doing, so it can *augment* it. 

ChatGPT is awesome, but it’s also a *silo*, so these days I mostly use it as a *fallback* for stuff for which I don’t have other tools available.

When I use ChatGPT, I do it via [TypingMind](https://www.typingmind.com/). TypingMind describes itself as *a *“*better UI for ChatGPT*”, which is an accurate tagline.

![image](../assets/f9da9e33f25243ee.png)

Nothing about it is *game-changing*, but there are like a thousand quality of life improvements, which together compound and make it a way nicer experience than using plain ChatGPT.

Here are my favorites:

- Organize threads into folders

- Voice prompts with good speech-to-text (via OpenAI Whisper)

- Easy interface for entering system instructions

- Standalone Mac app (which I use less than I like because it doesn’t support voice input yet).

### 📚 Research / Studying

AI is extremely good at summarizing information. 

This is a game changer for me, because now, for anything I want to read/watch, I can start with the summary and only go for the full thing if it feels promising.

I do this both for articles and videos (I don’t listen to many podcasts so I don’t know if there is a way to do it for them, too) 👇

#### 📑 Articles

For articles, I use the Shortform Chrome Extension. It summarizes the web page you are currently on and also fetches additional context and resources about the topic.

The context and links are *hit or miss*, but the summary is usually good, and you can copy it in one click.

So, my workflow for reading articles looks like this now:

1. I skim through the article to figure out the basic structure and how long it is.

1. If it feels interesting but I am not sure I want to read it in full, I check out the summary.

1. If the summary is good, I either save it for later on Readwise Reader (70% of the times) or read it *serendipitously *on the spot (30% of the times). In both cases I highlight good passages (also via Readwise), which automatically creates an article entry with the highlights on Notion.

1. If useful, I copy-paste the Shortform summary into the same Notion entry.

![image](../assets/d51567af63b14977.png)

Shortform is a *paid *service that is mostly known for summarizing books — and that’s how I started using it, before they even created the Chrome extension.

If you are not into book summaries (but you should try them, they are awesome) you can try these other services:

- [Upword](https://www.upword.ai/) — also paid

- [Gimme Summary](https://gimmesummary.ai/) — completely free

- [TLDR This](https://tldrthis.com/) — has a free tier

#### 📺 Videos

I do the same for videos, which is even more useful than for articles. In fact:

- **Long videos are commonplace** — it is rare to find 1-hour long articles, but 1-hour videos are totally normal.

- **You can’t *****skim *****videos** — if the author didn’t include chapters, well, good luck!

You could use Shortform to summarize videos, too, but it doesn’t include video chapters, so use a different app. 

I have tried both [Eightify](https://eightify.app/) and [YoutubeDigest](https://chrome.google.com/webstore/detail/youtubedigest-summarize-u/agjkjablkiapmpbeglmdcmhnihlofija):

- **Eightify** — is faster (summary is instant for popular videos) and makes for a better overall experience, but it is paid ($48/year).

- **YoutubeDigest** — is slower (it takes a couple of minutes for a 2-hour video), but still very well made, and most of all it is free.

![image](../assets/62d607868229424f.png)

### 💬 Meetings

The key idea about meetings is that you can give them the same treatment of Youtube videos. AI tools allow you to:

- Summarize stuff that has been discussed

- Extract action items

- Create video *chapters *so you go can back to specific moments

If for regular videos this is a *nice to have*, for meetings it is a total game changer.

In fact, this is helpful in many ways:

- It aligns people about next steps and action items.

- It creates decision records for future reference.

- It creates a place where you can have good async conversations about the meeting subject.

All of these in turn allows for *less* people to join meetings, because they have a good way to catch up afterwards.

My favorite tools for this are [TL;DV](https://tldv.io/) and [Otter](https://otter.ai/). Key features are similar — crucially, for some people, Otter also supports Microsoft Teams, while TL;DV only Meet and Zoom — and both have generous free tiers you can try.

They are both very good — I have a slight preference for TL;DV, which also can export meeting notes to Notion automatically. 😇 

### ✏️ Writing

So far I couldn’t make AI write fully *original* content that is good enough for my standards, so, Refactoring is still, painstakingly, written by humans!

However, I have found AI useful for improving my writing, in various ways:

- **Improve grammar** — general proof-reading, similar to what you do with Grammarly or Writer.

- **Simplify** — if I feel that a sentence is a bit convoluted, I ask AI to simplify it, and it usually works.

- **Make it shorter** — similar to *simplify*, but this especially for when something feels redundant.

I use this mostly for my newsletter writing, but I can totally see how this is helpful in a team, too. We create a lot of writing that can benefit from this — emails, product specs, design docs, etc. — especially when authors are not native speakers, or are not particularly versed in writing.

> *We use it for proofreading. I fostered this from the beginning. Being a remote team with people coming from all over the world, and a lot of them not being native English speakers, can create communication issues. Proofreading your important chats, emails, documentation, slides, etc., can help avoid misunderstandings.

— *Nicola Ballotta, Director of Cloud at Namecheap

This kind of AI is embedded in many tools already, including Google Docs and Microsoft Office

I personally use [Notion AI](https://www.notion.so/product/ai?utm_source=google&utm_campaign=19760657944&utm_medium=147709666538&utm_content=649989555747&utm_term=notion%20ai&targetid=kwd-1547008718840&gclid=CjwKCAjwkeqkBhAnEiwA5U-uMxU2dkkJ2PED6DmyEjN-HgLcISUFFzIUIqXoC17vEWOT5cq3AJoDjBoCsAgQAvD_BwE), which is one of the best implementations of AI in a product that I have seen so far.

![The Notion AI context menu. Plenty of good recipes + you can ask for anything.](../assets/23f6d9e67d014774.png)

### 🤖 Coding

Coding is impacted big way by AI. This is not a prediction about the future, this is the reality. Today.

A lot of data backs this already:

- Github CEO [last week said](https://www.freethink.com/robots-ai/github-copilot#:~:text=%E2%80%9CAlmost%20half%20the%20code%20on%20average%20is%20written%20by%20Copilot.%20That%20alone%20is%20mind%20boggling.%E2%80%9D) that, for customers that use Copilot, 46% of all new code is written by Copilot.

- 75% of engineers feel more productive with AI tools (source: [this survey](https://newsletter.pragmaticengineer.com/p/ai-coding-tools?utm_source=post-email-title&publication_id=458709&post_id=115649522&isFreemail=false&utm_medium=email) by Gergely)

- Overall, combining various surveys, perceived productivity gains range from a lower bound of +50%, to an (optimistic, if you ask me) upper bound of 10x, based on the situation (person, task, etc.).

There are also various individual takes by respected leaders 👇

> *I have felt improvements of 50%, the process of getting started is very simple* —** **Sebastian Barrios, VP of Technology at Mercado Libre

> *Talked to a programmer today who said AI coding tools made him about 10x more productive. Though 10 seems like a round number, this was an attempt at a precise estimate.* — Paul Graham, founder at Y Combinator

The whole AI coding topic is so vast that I will write a separate, dedicated edition about it. That will include workflows, prompt strategies, and everything you need to know to create good code with AI, based on today’s state of the art.

For today, instead, let’s talk about tools and popular use cases at a high-level.

#### 🔨 Tools

Coding is one of those tasks where you vastly* *benefit from using AI *inside* the tools you already use (i.e. IDEs), as opposed to keeping a ChatGPT tab open all the time.

And there are *many* AI tools that you can use in the IDE already. To me, here are the most relevant:

- [Github Copilot](https://github.com/features/copilot) — the OG of AI coding tools.** **

- [Replit Ghostwriter](https://replit.com/site/ghostwriter) — the AI embedded into the Replit IDE, built in-house by their team.

- [Tabnine](https://www.tabnine.com/) — standalone tool with two killer features for larger companies: you can self-host it, and you can train the model on your codebase.

- [Amazon Codewhisperer](https://aws.amazon.com/codewhisperer/) — it is from AWS and is free for individual use.

To understand how AI coding works today, a bit of history is useful. Copilot *started *this whole space in late 2021, integrating AI as a *supercharged* code autocomplete. This UX was natural because it felt like an extension of what IDEs already did — that is, autocompleting code.

Later, when ChatGPT came out, people immediately figured out that they could use it to write code, and the *chat *interaction proved extremely useful to provide more context and follow-up instructions.

So, many engineers I know started working with Copilot in the IDE, for the small stuff, plus a ChatGPT tab open all the time, for larger instructions.

Fast forward to today, some tools still provide autocompletion only (e.g. Tabnine, Codewhisperer), while others have caught up and also provide first-class support for AI chat in the IDE. To me, the latter is the obvious, better way of using AI for coding, and unless you have other special needs, you should use one of the tools that support it.

Personally, I have used mostly two: **Github Copilot** and **Replit Ghostwriter**. They are similar, but different, mostly because of what the wider Github and Replit products do.

Let’s look at both 👇

#### 🧑‍✈️ Github Copilot

Copilot doesn’t offer the chat by default. To enable it, you should [join the waitlist](https://github.com/github-copilot/chat_waitlist_signup) (but they should admit you very soon), and enable Github Copilot Nightly [on VS Code](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-nightly) or any other supported IDE you are using.

Once you are in, you will still be able to use the autocompletion, but you will also have a chat panel you can use on the left, where you can chat with Copilot as if it was ChatGPT. 

As opposed to ChatGPT, though, Copilot can see your code in its context (I don’t know to which extent) so you can reference specific parts in your instructions, or perform tasks on more files together.

![image](../assets/9c831503ea114365.png)

So you can do something like this:

`Create a Testimonials component in a separate file and add it to the bottom of the home page`

or this:

`Extract the brand collar (#177BFD) from the files inside the components folder into a constant variable defined in a new Branding component, to be used everywhere. Refactor existing components to use it.`

Copilot will come up with code snippets, instructions on which files to create, and where to put the code.

You can’t do this neither with ChatGPT nor autocompletion alone.

#### 👻 Replit Ghostwriter

Ghostwriter is very similar to Copilot: you have a chat panel + autocomplete in the editor.

The chat experience, though, has a better UX — it explains better what it is doing, it highlights files names, and various other quality of live improvements.

![image](../assets/130e4da15fff41d2.png)

Ghostwriter can also do more things because of the differences between Replit and a traditional IDE.

For those who are not familiar with it, Replit is an *all-in-one* cloud IDE that does everything you would expect from a modern IDE + it is nix-based and it allows to *host* pretty much anything you can think of. I personally love it and I believe it is one of the most slept on tools in our industry.

So, you can use Ghostwriter to do more Replit things, like figuring out how to fire up a Postgres instance, or increase the CPU of your production instance.

![image](../assets/5aa03f23f892453c.png)

#### 📖 Coding use cases

But what do you use AI for? Here is what I have had the most success with:

1. **Boilerplate / Repetitive code **— AI truly excels here. Creating the stubs for new components, common config, or adding libraries (e.g. add Tailwind to your project).

1. **Write tests **— this is a specific version of #1. AI can write good tests for your code, but expect to have to add more cases yourself. However, you will never have to write another test stub in your life.

1. **Explain /** **document code **— AI is very good at explaining code and it can also create docs for you. I have tried it with very complex stuff and it always handled it well. Obscure, impenetrable code seems like a thing of the past. You can also try tools like [Mintlify](https://writer.mintlify.com/) or [Theneo](https://www.theneo.io/) that generate automatic docs via AI.

1. **Refactor small functions **— for when explaining is not enough! AI is surprisingly good at splitting functions, refactoring them for better performance, and other small-scale maintenance.

1. **SQL queries **— this is an awesome use case that I learned [from Francesco](https://twitter.com/frankdilo/status/1671448788760940545), as SQL is no one’s favorite language. Queries look very good as long as you provide a schema. You can also try [Mason](https://mason.app/) for this.

1. **Pull Requests **— AI can create [automatic descriptions](https://githubnext.com/projects/copilot-for-pull-requests) for PRs and scan code to propose improvements, before it gets merged. This is a no-brainer and I expect it to become commonplace. You can use [Codacy Quality](https://ai.codacy.com/) for this.

1. **Terminal **— I am using [Warp](https://www.warp.dev/) as my main terminal because, other than having a great autocomplete, it includes an AI assistant that can suggest and run commands for you. I always forget how do to shell things, so this is super useful.

![Warp terminal can suggest shell commands.](../assets/e1844159dd674e1f.png)

#### Bad use cases

When it comes to coding, it hasn’t been all sunshine and rainbows. There have been times where I had to spend more time debugging AI-generated code than I would have probably spent writing the full thing myself.

The main problem is that AI almost never tells you “*I don’t know how to do this*” — it rather *hallucinates *and gives you a wrong answer.

So, I have learned to watch out for these situations:

- **Very recent stuff **— if you ask for something that is relatively new (<2 years), there is a higher risk of hallucinations because 1) AI might have not seen it in the training data, and/or 2) examples of it were few.

- **Niche libraries **— basically the same as above!

- **Specific library versions **— AI isn’t good at keeping consistency between function signatures and the library versions you are using. Keep that in mind if you need something very specific.

- **Complex functions with a lot of context needed **— AI is generally good at creating complex functions when they work in isolation (e.g. algorithms, math stuff, etc.) but it isn’t the best when it has to keep into account dependencies from a lot of other code.
