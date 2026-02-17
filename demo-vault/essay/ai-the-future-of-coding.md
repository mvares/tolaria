---
aliases:
  - "AI & The Future of Coding"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-essays|Publish Essays →]]"
Status: Evergreened
URL: "https://refactoring.fm/p/ai-future-of-coding"
"👓 Status": Not started
"Created time": "2024-04-18T14:53:00.000Z"
Date: 2022-12-15
"Has Notes":
  - "[[evergreen/ai-coding-vs-innovation-concern|AI coding vs innovation concern]]"
  - "[[evergreen/ai-coding-freshness-problem|AI coding freshness problem]]"
  - "[[evergreen/open-source-vs-ai-coding-workflow|Open source vs AI coding workflow]]"
Tags:
  - Luca
  - Not for HH
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 5c7999e5-a460-4769-8cb8-7bbe6fb0c01f
---

# AI & The Future of Coding

### ✍️ Post

---

Let’s get something out of the way: this article *has not* been written by an AI.

I know, it sucks. 

So today, if you want, you will just read some very *human* thoughts, packed with emojis and questionable grammar choices.

Over past two weeks, all conversations I had with peers touched the AI subject somehow.

That’s because — for those of you who read this newsletter from inside a cave — OpenAI released a new chat AI called [ChatGPT](https://chat.openai.com/) that seems impossibly good at… everything. 

My Twitter feed has been, and still is, inundated of ChatGPT examples. From writing essays, to coding, to [navigating the browser and casually make a dinner reservation](https://twitter.com/natfriedman/status/1575631194032549888).

The truth is, I started writing down ideas for an “AI & coding” article a long time ago. Reading them back today, some are like “*Copilot is here to stay*”. Looks cute, right? But it had to feel like a big insight back then.

“Back then” is less than one year ago. 

[Github Copilot](https://github.com/features/copilot) was released in private beta in June 2021, and opened up to all developers after [exactly one year](https://github.blog/2022-06-21-github-copilot-is-generally-available-to-all-developers/). Copilot, in turn, is powered by [Codex](https://openai.com/blog/openai-codex/), which is developed by OpenAI, just like ChatGPT.

Codex is a constrained, fine tuned version of the GPT-3 language model, while ChatGPT is based on what OpenAI calls GPT-3.5, a marked improvement on the former. So it is safe to expect the same kind of improvement to come to Copilot* *soon*.*

How will these tools change the way we write code? And, in turn, how will this change our industry? 

This article is a reflection on the first, second, and third order effects of *AI-assisted software development*, which right now feels like an inevitable future.

Here is what I will cover:

- 💻 **Workflow** — I spent two days writing a Telegram Bot with the help of ChatGPT. I got my hands dirty, and I have thoughts.

- 🐛 **Correctness & Bug Fixing** — AI rapidly changed my assumptions about correctness and my approach to fixing bugs. I wrote a reflection on where this is going.

- 🔄 **Feedback Loop **— thoughts on how these models can improve in the future, with the help of human experience. Which will have a big impact on… 👇

- 💡 **Innovation & Incentives **— AI models might change the incentives for creating new frameworks, libraries, and languages. In turn, this might change the open source model forever.

There is a lot to unpack. Let’s dive in!

---

### 💻 Workflow

I have always wanted to create a Telegram Bot, but I wouldn’t know where to start. So, I set out to create one with the help of ChatGPT, with the goal of writing *as least* code as possible myself.

I started with a simple prompt:

![image](../assets/7f1ff749150e4dff.png)

This answer was genuinely impressive. It didn’t only output the code — it also described the general system design and gave me instructions about things to do outside the code editor (e.g. get the OpenAI API key).

This made me think that the way we have mostly used AI in coding so far—namely, Copilot and the likes—is pretty limited with respect to what it is useful for. When you are only using it to write/autocomplete your code, chances are you have already done a lot of prep work yourself about requirements, architecture, where this code needs to go, etc.

Much of this heavy lifting can be done by AI as well. Which means this interaction won’t happen only in your code editor. You will want this in Notion / GDocs when you write a design doc. You will want it in Slack to discuss tradeoffs with your team, and maybe in Zoom calls as well.

When you think about it, the reason is simple: this conversational style mimics the interaction you would have with people — which makes it natural in all the contexts where you work with people.

There is, of course, the question of whether this conversational style is here to stay, or we will invent more efficient ways to prompt the AI. After all, one of the qualities of programming languages is that they are *less verbose* than human languages.

Will we invent more compact languages for AI prompts? 

I don’t know. But let’s go on with the example.

Not knowing anything about Telegram Bots, I asked how to make the bot run the code:

![image](../assets/795d112342e94afd.png)

Again, this was accurate. I asked again where I should run this and it turns out it was a *one time *thing so that the bot remembers where its webhook lives.

So far, so good.

Then, since I am more comfortable with Node, I asked to rewrite the code from Python to Node:

![image](../assets/c622072dcf804b4b.png)

And that’s where the troubles began 👇

### 🐛 Correctness & Bug Fixing

The code above didn’t work. 

In a normal situation, debugging ~10 lines of code wouldn’t be a big deal. However, in this case, the code used libraries I had *zero* knowledge of. Which, mind you, was *exactly* the point of making the AI writing the code.

So I thought of using ChatGPT to get more examples. But how could I trust it if it got that very code wrong before? 🤔

So, I resorted to check the libraries’ docs on my own. 

It turns out, the AI used methods that do not exist in the Node library, probably inspired by the Python ones.

![image](../assets/7c7ae8192f774bf8.png)

I replaced them and things worked fine. Two considerations:

- Debugging the code required me to study the *openai* and *telegraf* libraries, undoing 90% of the benefit of using the AI in the first place.

- Debugging was surprisingly hard, because these were not the kind of mistakes a normal person does. When we debug, our brain is wired for looking at things we are more likely to get wrong. When you debug AI code, instead, literally *anything* can be wrong (maybe over time we will figure out the most common AI mistakes), which makes the work harder. In this case, AI completely made a method up — which is not something people usually do.

So, in the end, using ChatGPT to write this code didn’t help much, but I wouldn’t be fair if this was my takeaway. In fact, had the code been correct, the AI would have saved like 95% of my time.

But how would I even know that the code is correct? This was a simple case—largely, it either works or it doesn’t—but what about a complex algorithm? You may get something that works *apparently*, until it doesn’t in some specific cases.

A simple answer is: you would write tests. We may even get to the point where AI writes most of the code and humans write tests.

Can’t wait, right?

![image](../assets/15835895c3894012.png)

Or, the AI will write both, which poses more questions about making sure AI gets requirements right, and more. 

Anyway, let’s say we are able to spot the mistakes that the AI makes and correct them *manually. *

Is this the right process? Let’s talk of feedback loops 👇

### 🔄 Feedback Loop

As humans, we tend to focus on problems of the here and now, and discount how much things can improve in the future. I try to be self-aware of this bias, and when I am about to write off a product or a service, I ask myself: can this be fixed in the future? And how fast?

So I asked myself the same question about AI and coding. There are problems now, but are things going to get better over time?

To improve steadily, great products need two main things:

- 🗳️ **Getting feedback** — regularly from users, to figure out what to improve.

- ⚡ **High velocity **— a workflow that allows improvements to be made fast. 

How do the current AI tools fare on this? 

Well, it’s complicated.

Let’s compare AI coding to the main other way we have today of using code that is not written by us: **open source**.

#### Open source workflow

With open source, people can open up issues about bugs and changes. These issues can be seen by everybody, there is little duplication, owners reply, people have a discussion, and so forth.

On top of this, fixing a bug once fixes it for all users (granted they will update their version). 

That looks like a good feedback loop to me.

Let’s compare it to the current state of AI coding 👇

#### AI workflow

AI coding is not based on *reusing* the same code, like open source, but on *creating* new code every time.

This is like *code duplication* at scale, and poses the same problems. 

If the AI introduces a bug on something, it will do so for all users that request that code. Those users, in turn will *each* have to fix the same bug by themselves.

![image](../assets/be412671fe4e40d5.png)

I tried to regenerate the Node code for my example several times, and I always got the same bug.

What’s worse, right now we have no way of making the AI learn from its mistakes + our corrections. There is no feedback loop.

Feedback loops don't only matter for bugs. Let’s talk about freshness 👇

### 🌸 Freshness

After generating the Node code for the Telegram Bot, I asked ChatGPT to use the Serverless framework to turn it into a function I could easily deploy on AWS.

Amazingly enough, it did it 👇

![image](../assets/d96f29d9b3884bbb.png)

 The code works, but there are two problems:

- It uses the old way of handling the function — with the callback — while the recommended way today uses the *async / await *syntax.

- It uses the deprecated “*on*” method for the Telegram Bot, instead of the new filter utils.

This likely happens because you can find way more examples online with these methods than with the new ones, as the former have been around for longer.

This *freshness* problem worries me for two reasons:

- **I have no way of detecting it** — sure, if you know you should use *async/await* you can ask the AI to rewrite the code, which it will happily do, but *you have to know *it first.

- **It is *****intrinsic***** to how AI works** — the model is trained on data and is statistical based, so it is naturally going to favour stuff where it has the most content.

### 💡 Innovation

My final concern is about innovation.

Most new languages, libraries, and frameworks, were created to improve the developer experience. Over time we got better at handling complexity, write stuff in a concise way, and write code that is generally more readable. 

When you think about it, this is all to developers’ advantage first, and to businesses’ down the line.

When the most of our time won’t be spent on writing code anymore, will we have the same *drive* for creating better tools?

If 10 years ago the AI could write perfect jQuery, would we have React today?

And back to the freshness issue, new tech will also have *naturally* less examples to learn from, which will make the AI worse at it than at old tech.

### 📌 Bottom Line

AI coding is a tremendous opportunity for the industry and is here to stay.

It is surely going to provide incredible benefits — but it is also going to change some core dynamics that so far have enabled innovation, open source, and much of the software ecosystem as we know it today.

We will have to wrap our heads around this to figure out what is the best, most productive way of using AI, while also making sure we are moving forward as an industry.

Right now it just feels we have found infinite cheap mediocre devs to put behind the keyboard.

It is great, but we need to do better.
