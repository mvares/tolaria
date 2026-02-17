---
aliases:
  - "What’s Good for Humans is Good for AI"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-essays|Publish Essays →]]"
Status: Evergreened
URL: "https://refactoring.fm/p/whats-good-for-humans-is-good-for"
"👓 Status": Not started
"Created time": "2025-04-18T08:07:00.000Z"
Date: 2025-09-17
"Has Notes":
  - "[[evergreen/the-roi-of-good-engineering-is-skyrocketing-with-ai|The ROI of good engineering is skyrocketing with AI]]"
  - "[[evergreen/ai-should-help-with-code-quality-not-threaten-it|AI should help with code quality, not threaten it]]"
  - "[[evergreen/we-are-lucky-with-ai|We are lucky with AI]]"
Tags:
  - Luca
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 1d9bdf02-815c-8018-a4d8-fbafe3422e3a
---

# What’s Good for Humans is Good for AI

It’s been a couple of months now that a lot of my attention is focused on a single topic: **how good engineering teams are using AI**.

I have been exploring this from many angles:

- We are wrapping up [our newsletter survey](https://refactoring.fm/p/survey-how-do-you-use-ai-at-work?utm_source=publication-search) about it — and the full industry report will come out in a couple of weeks.

- We explored various angles of it in community threads and events

- I had a lot of 1:1 conversations about this topic with podcast guests and real-world engineering teams from AI-first companies like Coderabbit, Unblocked, Augment, Convex, and more.

- Last but not least, I got my hands dirty by coding *a lot* recently, and making good progress on my own side projects.

All in all it’s like a big pyramid of information that goes from broad, quantitative data points, to deep, qualitative (but also more anecdotal) ones 👇

PICTURE

So, if you are a tech leader who’s trying to figure out how they should think about AI, and what to make out of it, here are the main things I believe you should know:

1. 📉 **Progress is slowing down **— so this is a good time to take stock of where we are.

1. 🤷 **Productivity data is inconclusive **— as it has always been.

1. 🤝 **What’s good for humans is good for AI** — there is no secret formula… fortunately.

1. 🔬 **AI should improve code quality** — not threaten it.

1. 🏯 **A lot of teams need to be redesigned **— to get the most out of AI.

There is a lot to unpack, so let’s dive in!

---

### 📉 Progress is slowing down

Over the past two years, whenever I wrote an article about AI I made the same joke that those ideas ought to become outdated in a couple of weeks or so.

Well, today it doesn’t feel that way anymore. In fact, we can arguably say that AI progress — in coding, but also in general — has significantly slowed down.

What do we mean by progress? For software engineering, AI progress is driven by two vectors: **frontier models** and **dev tools**.

![image](../assets/26fbdf02815c8008.png)

These two are not completely orthogonal: improvements in former obviously *drive* changes in the latter, but it’s also true that we are discovering things about tools *ergonomics* on our own, in a way that doesn’t always feel tied to models.

In fact, over the past year we went through different paradigms, the three main ones today being:

- **AI-powered IDEs** → like Cursor and Augment.

- **Autonomous Agents** → like Devin.

- **CLI tools** → like Claude Code.

Boundaries are also fuzzy as each tool often tries to do more than one thing.

In the meantime, AI models seems to be plateauing, or at least getting into the land of diminishing returns. Anthropic models, that have consistently topped the [SWE-Bench](https://www.swebench.com/) (the most reputable coding benchmark), have been following a trend of increasingly smaller, shorter, and more incremental iterations. OpenAI’s latest GPT5 follows the same trend.

![Improvement trend for Anthropic models looks squarely in diminishing-returns land](../assets/26fbdf02815c8023.png)

This is to say: today is probably a good time to stop and take stock of where we are. It’s hard to expect AGI or a singularity moment coming anytime soon, so let’s look at what we have now.  

Starting with data 👇

---

### 🤷 Productivity data is **inconclusive**

I looked at all the available data, from research to individual stories, about the impact of AI on teams’ (and individuals’) productivity, and the truth is data doesn’t say much.

Or, better, whatever your bias is about this matter, you can find data that supports it. 

Let’s start with some individual examples:

> 🟢 **“I am 5x faster at coding because of AI” **— Salvatore Sanfilippo, creator of Redis.

Salvatore is one of the most successful open source authors of all time, writes incredibly complex, low level system code, and is also an extremely grounded and practical person. In other words, I trust him.

> 🟢 **“90% of our code is written by AI” **— Dan Shipper, founder of Every

Every does 1M+ ARR and ships working, revenue-generating software, like [Spiral](https://spiral.computer/) and [Cora](https://cora.computer/). Dan [came on the podcast](https://refactoring.fm/p/the-future-of-creative-organizations?utm_source=publication-search) and explained how they largely vibe-code everything.

There are many individual stories like this, but when you look at more aggregated data, the outlook is less promising:

> 🟡 **“Productivity gains from AI that we see in teams are ~5-10%” **— Abi Noda, CEO of DX

Abi sees *thousands* of codebases through his work at DX, and helps some of the best teams in the world.

> 🔴 **“AI is hurting delivery performance**” — The State of DevOps, DORA

The DORA team pointed to *negative* AI impact: teams that make regular use of AI get -1.5% in delivery throughput, and -7.2% in delivery stability (yikes!).

> 🔴 **“AI makes developers 19% slower” **— [Becker et al.] Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity.

The final nail on the coffin is this widely re-shared research from METR, which even though it looks at a very small sample (19 developers), reports some of the worst-looking numbers on AI productivity I have ever seen.

So, data looks inconclusive, but should this really be surprising? To be honest, software delivery performance has *always* had a lot of variance. If we think at [Accelerate](https://refactoring.fm/p/accelerate), arguably the most influential work ever on this, the gaps it found between elite and average teams are often *staggering*. We are talking 50x values on several measures.

As an industry, we have never found much consensus on many engineering practices, and there have always been teams able to outperform others by (several) orders of magnitudes — so it feels just natural that, with AI as well, we have teams reporting wildly different outcomes.

Which also means, average aggregated data will never say much, but it’s probably more helpful to speak to individual teams and figure out how they are doing things.

> **“When the data and the anecdotes disagree, the anecdotes are usually right” **— Jeff Bezos

And this is what I have done 👇

---

### 🤝 What’s good for humans is good for AI

In recent months I have collected stories from podcast guests, plus from real world teams at AI-first companies like Unblocked, Augment, Convex, CodeRabbit, CodeScene, and more.

I went in with questions like how do you optimize this and that for AI, how do you make this *AI-friendly*, and so on. And the overwhelmingly common response is: there is no magic recipe. **What’s good for humans is good for AI**. Which is incredibly good news.

But what does it mean *good for humans*? Let’s unpack this into the four most important mental models that I noted:

#### 1) Work in small batches 🍱

I feel almost stupid to elaborate on this, but I’ll say it anyway: AI immensely benefits from working in small iterations — just like our biological, carbon-based friends.

In fact, if you look at the most popular blog posts about e.g. how to work well with Claude Code, or Cursor, or the likes, *a lot* of the advice is some variation over this. Don’t bite more than you can chew, plan work, commit often, keep the feedback loop tight.

#### 2) Create constraints 📏

This is more interesting, but still not surprising. AI performs better when it has to make fewer choices and can physically make fewer mistakes. Which reminds me of this fantastic quote by Charity Majors:

> **“Make the right thing to do the easiest thing to do” **— Charity Majors

She meant this for humans, but for AI it is just the same. But what does this look like, on a practical level? Common ideas include:

- Using static typed languages

- Using strong linting 

- Keeping abstractions consistent across the codebase

- Investing in good testing coverage

- …

In other words, it’s design choices that 1) limit the surface of what AI needs to figure out, and 2) make you (and AI) able to intercept errors early.

#### 3) Design context 📑

There is a lot of talk these days about *context engineering*, or how to give AI everything it needs to know to perform well.

[Embed](https://x.com/tobi/status/1935533422589399127)

This is an area where AI is legitimately a bit different than humans, but the conclusions—we’ll see—are similar.

With some degree of simplification, when it comes to parsing—or putting together—info for some task, there are two types of context we work with:

- ↔️ **Broad context **— insights come from making sense of data coming from a variety of tools, like the team chat, ticketing, docs, OKRs, and more. 

- ↕️ **Deep context **— insights come from the analysis of hard, data-heavy individual sources, like the codebase, logs, or analytics.

![image](../assets/26fbdf02815c8081.png)

Humans are just great at broad context and at keeping all these different things in their heads. AI, instead, struggles with it, while it excels at working through individual big chunks of data, way better than we are capable of.

For sure, some of the AI imitations with processing broad context may just be *tooling* limitations: MCPs are clunky, RAG feels like early tech, and some sources are just usually *not *plugged in — but it is what it is, and we have to work with it.

So, today AI works best when you **maximize local reasoning opportunities**: make things self-contained, limit coupling, and and make AI find everything in the same place.

This usually spawns from good design choices, like good componentization, keeping docs in the repo, and the evergreen low coupling + high coesion.

#### 4) Everything as code

Finally, whenever you can express something with code, you probably should. AI is not good at navigating websites and clicking around, while it is fantastic at writing code.

Infrastructure as code, configuration as code, documentation as code, all make much more sense when AI is in the loop. But let’s be honest — they made a lot of sense even before.

So, when we look at everything we have covered here, a lot of it is the* *classic engineering tradeoffs: doing a bit more work now (e.g. good code, good testing, good docs) in order to reap the benefits (i.e. higher velocity) later.

And the thing is: AI is tipping the scale, on both sides:

- On one side, AI makes a lot of the *grunt work* easier: it is good at writing tests, good at writing docs, removes the cognitive load from remembering syntaxes and DSLs

- On the other side, doing things right now doesn’t only benefit us humans, it also benefits AI itself.

![image](../assets/26fbdf02815c8086.png)

In other words, AI *skyrockets* the ROI of good engineering by simultaneously 1) reducing the effort, and 2) increasing the benefits.

Speaking of good engineering, let’s talk about quality.

---

### AI should *help* with code quality, not threaten it

If so far we mostly talked about good engineering practices — which should enable quality by themselves — why do we need to talk about *quality* separately?

I feel we have to because, simply put, code quality is the #1 concern by engineers when it comes to AI.

It’s also at the core of one of the main narratives being pushed today: AI will make you deliver *more *code in less time, but you’ll have less control over it, it will be riddled with bugs, and you will regret it over the long run. 

This *can* be true, but it’s not inevitable, nor I believe it’s the best way of using AI.

In fact, AI is great at *reasoning* about existing code — which, as a skill, is at the core of reviewing and improving code. I would go even as far as to say that **AI code reasoning today is better than AI code generation**. I guess it’s because it’s a more *constrained* domain, which works well with AI’s ability to go deep about something narrow-ish.

Whatever the reason, AI today is already fantastic at picking up code smells, security vulnerabilities, missing tests, but also team-specific items like adherence to your own best practices and conventions, and a long tail of quality of life improvements, like auto-summaries for PRs, release notes, and more.

The list of tools you can try for this gets longer by the day. Some of the ones I used myself (with good success) are [Codacy](http://codacy.com/), [Packmind](http://packmind.com/), [Augment](https://www.augmentcode.com/), and [CodeRabbit](https://www.coderabbit.ai/).

It is also interesting that because of how fast and cheap AI is at working its magic, code quality is continuing to shift-left 👇

![image](../assets/26fbdf02815c800a.png)

Many static analysis checks that before AI belonged to CI/CD are now real-time suggestions in the IDE. And some of these have even become MCP servers that can *steer* AI generated code before you even see it in the editor.

Hard to go more to the left from here! 

So I believe the future of code quality is extremely bright, but you have to be intentional at using AI for that — as opposed to a pure code generator.

---

### A lot of teams need to be redesigned

Finally, so far we mostly talked about *coding*, but the SDLC is a pipeline which is made of many other steps.

The elephant in the room in measuring AI coding productivity gains is that software engineers spend on average very little time coding — less than a hour per day, to be precise 👇

![image](../assets/26fbdf02815c8047.png)

You might be lucky and be around the 90th percentile and spend ~2 hours on it, but it doesn’t change much: it’s still only ~25% of your time.

Where does the rest go? It’s basically **coordination**: waiting for others to do stuff, meetings, managing status, negotiation, and so on.

The cost of coordination is a direct function of the **number of people involved to ship things**, so I am a big believer in *reducing* this number and giving people a broader scope of ownership, by taking advantage, in part, of the **universal basic proficiency** that AI gives people on the whole product stack.

If there is a gap between how an elite startup ship today vs the average team, that’s it. It’s the *layering* that we have built over the last 10 to 15 years, and that we need to *undo *to allow people develop true mastery and max productivity. [DHH is right](https://www.youtube.com/watch?v=tWduT9ygUQ4) about this, and today’s new teams are getting rid of a lot of it.

What can you do about it? Here are ideas:

- **Keep tech stack footprint small** → use full-stack frameworks, buy 10x more than you build, make boring choices, and in general make things *easy*, in order to reduce engineers’ cognitive load.

- **Maintain good design systems** → to unblock engineers and allow them to ship simple things without the need to put everyone in the loop.

- **Define what product success looks like** → so that engineers can figure out if things are working or not, and iterate.

- **Remove gates** — reduce blocking parts of the process: e.g. decouple deploy from release with feature flags, make QA async, and switch to a workflow in which you are quick to *revert* things when they go wrong, as opposed to making them go through multiple blocking gates to make sure they are right.

Again, very little of this is new. We were talking about these very things 10 years ago already, and maybe more. The difference is — and this is the common thread — this stuff is *easier *now with AI, and even more rewarding.

### ❤️ We are lucky

I want to close with a small reflection: **we are lucky**.

We are lucky to have stumbled upon a technology that *thrives* on largely the same things that make us humans thrive. If you care about good software engineering, today is your time to shine. 

Today the things you care about are more valuable and more obvious than ever before.

Let’s get to work and make them happen!

That’s it for today. I wish you a great week

Luca

  
