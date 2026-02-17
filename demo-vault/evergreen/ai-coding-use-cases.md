---
aliases:
  - "AI coding use cases"
"Is A":
  - Evergreen
"Last Tweeted": 2023-08-02
Tags:
  - Has Pic
"Created at": "2024-04-18T14:44:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to":
  - "[[essay/how-to-use-ai-in-your-team|How to use AI in your team]]"
  - "[[monday-ideas/monday-63|Monday #63]]"
"Old Created At": "2023-07-06T12:19:00.000+02:00"
"Updated at": "2024-09-18T08:44:00.000Z"
Status: Not started
Tweet: "AI can significantly aid in coding, particularly with boilerplate code, writing tests, and explaining complex functions. However, be wary of its limitations—especially with recent tech or niche libraries. While it can enhance productivity, it’s not a silver bullet. Let's discuss: how are you leveraging AI in your development workflows? #TechLeadership #AICoding"
notion_id: 51a5e0e1-f2a6-4d16-b423-3c0d886be54f
---

# AI coding use cases

But what do you use AI for? Here is what I have had the most success with: 

1. **Boilerplate / Repetitive code **— AI truly excels here. Creating the stubs for new components, common config, or adding libraries (e.g. add Tailwind to your project).

1. **Write tests **— this is a specific version of #1. AI can write good tests for your code, but expect to have to add more cases yourself. However, you will never have to write another test stub in your life.

1. **Explain /** **document code **— AI is very good at explaining code and it can also create docs for you. I have tried it with very complex stuff and it always handled it well. Obscure, impenetrable code seems like a thing of the past. You can also try tools like [Mintlify](https://writer.mintlify.com/) or [Theneo](https://www.theneo.io/) that generate automatic docs via AI.

1. **Refactor small functions **— for when explaining is not enough! AI is surprisingly good at splitting functions, refactoring them for better performance, and other small-scale maintenance.

1. **SQL queries **— this is an awesome use case that I learned [from Francesco](https://twitter.com/frankdilo/status/1671448788760940545), as SQL is no one’s favorite language. Queries look very good as long as you provide a schema. You can also try [Mason](https://mason.app/) for this.

1. **Pull Requests **— AI can create [automatic descriptions](https://githubnext.com/projects/copilot-for-pull-requests) for PRs and scan code to propose improvements, before it gets merged. This is a no-brainer and I expect it to become commonplace. You can use [Codacy Quality](https://ai.codacy.com/) for this.

1. **Terminal **— I am using [Warp](https://www.warp.dev/) as my main terminal because, other than having a great autocomplete, it includes an AI assistant that can suggest and run commands for you. I always forget how do to shell things, so this is super useful.

![Warp terminal can suggest shell commands.](https://prod-files-secure.s3.us-west-2.amazonaws.com/631d83ff-20ce-4401-a614-56e2c0f97767/b1958541-3de4-4b06-af92-85add12769a0/CleanShot_2023-06-28_at_10.16.152x.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W52KBDBI%2F20260131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260131T190138Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEClnQ%2BhupYEwnEdDB7oyIxAMMBthISaezpi333FDyO5AiEAq1bGIDopXkhqFax8tCls2hRo%2F9FOdOqUKWyossJsZCUqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDlvUD1zPfM557BdXyrcAz2MoMcnW0Mn3KM%2BR0a95zChSsVbg9FqWllahB1yx5ZQ%2FVXY51Q2hE7xh%2Ba1OUNRt6yB9YWBETwx4HJI2aIdfgdUFaC%2BM2gyHoZ7dfPnhFBJtcDHU4tw%2FVWTXPSQIlhcK0J23y49XSHHKKNUvGWkNtEdjIZRmGQtpKK6EoxJni565PzgD3eP3IXezfSLtfuNEa6Q5F99xksRqZrsgA2urFCtm%2BKtV97rhJUSqr1937wHVZIAUPIH12noUw8pjBWorY61OKnMhf%2BOyzsdroCdnTSNneJghrMw7HDpIgoaw76O3Ttms1pzzqcrbS%2FLQWSETxCCQGy%2Bvn1f9El7TopcacYeZ50edNjDnhoIEDWReMbFkzoIlD%2FiwuvClxbiHdWssLYxdGF3vHYs5%2FU2SPOQak8Qey627zOAoHtMrjKgxv6EzHs%2Boyzj47s0zxhCuFUXftEwzgpdPEWogKFeqXLKEZcztGO3F8fXXQyEmdTBB1odOX681R48k%2F%2BrA5VsDR06uPABKYpe70fyEBbr%2BfdOYnNmapBFo2V6g8t2JGH8NSHsNfOXktPs9RHcwdjW4w4DtRWDD8K6W7K6A4Fqq%2BZlY3tRrBHuqzDSm1U92S2NDaH41dA26jQolQD5%2BeekMPuK%2BcsGOqUBZkUmBJ0k800zcdHk7vnMpWmm2eTIIoTEsxqgmZyh0AiBdV0qTfEL7O4yMIlEQOq7p9gXLMmnmZ2mFbC0f7lU3DSeEwTKlncP8gxY8ugmM7yx8F3OJSrHXQnQEyVfqJN7nm3rhZDkDBOfLBQmsEGpXwUy3nhiCDQJXtcEVpt7RkxRy7G%2FwZ8YkO9um%2FBa4Rfw%2FJwhKbs2JEt4oZ5b3tfEAM7pS1nc&X-Amz-Signature=8130d9f9435efd48e124a7bc96ed5f229cbefc1bb23de75fd6effe225b3aff8a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### Bad use cases

When it comes to coding, it hasn’t been all sunshine and rainbows. There have been times where I had to spend more time debugging AI-generated code than I would have probably spent writing the full thing myself.

The main problem is that AI almost never tells you “*I don’t know how to do this*” — it rather *hallucinates *and gives you a wrong answer.

So, I have learned to watch out for these situations:

- **Very recent stuff **— if you ask for something that is relatively new (<2 years), there is a higher risk of hallucinations because 1) AI might have not seen it in the training data, and/or 2) examples of it were few.

- **Niche libraries **— basically the same as above!

- **Specific library versions **— AI isn’t good at keeping consistency between function signatures and the library versions you are using. Keep that in mind if you need something very specific.

- **Complex functions with a lot of context needed **— AI is generally good at creating complex functions when they work in isolation (e.g. algorithms, math stuff, etc.) but it isn’t the best when it has to keep into account dependencies from a lot of other code.

---

I have used AI for coding *a lot* in the last couple of months — mainly Copilot and @Replit Ghostwriter (my favorite) — because I wanted to write about it in the newsletter.

My take is that it is not a silver bullet — here are 7 use cases that worked for me and 4 that didn't 👇

1. 🥱 Boilerplate / Repetitive code

AI truly excels here. Creating the stubs for new components, common config, or adding libraries (e.g. add Tailwind to your project).

1. 🔍 Write tests

This is a specific version of #1.

AI can write good tests for your code, but expect to have to add more cases yourself. However, you will never have to write another test stub in your life.

1. 📑 Explain / document code

AI is very good at explaining code and creating docs for you.

I have tried it with complex stuff and it always handled it well. Obscure code seems like a thing of the past.

You can also try @mintlify or @theneoapidoc to generate automatic docs.

1. 🛠️ Refactor small functions

For when explaining is not enough! AI is surprisingly good at splitting functions, refactoring them for better performance, and other small-scale maintenance.

1. 🗄 SQL queries

This is an awesome use case that I learned from Francesco, as SQL is no one’s favorite language. Queries look very good as long as you provide a schema. You can also try @mason_app for this.

[https://twitter.com/frankdilo/status/1671448788760940545](https://twitter.com/frankdilo/status/1671448788760940545)

1. ⬆️ Pull Requests

AI can create automatic descriptions for PRs and scan code to propose improvements, before it gets merged.

This is a no-brainer and I expect it to become commonplace. You can use Codacy Quality for this.

[https://ai.codacy.com/](https://ai.codacy.com/)

1. 💻 Terminal

I am using @warpdotdev as my main terminal because, other than having a great autocomplete, it includes an AI assistant that can suggest and run commands for you.

I always forget how to do shell things, so this is super useful.

❌ Bad use cases

When it comes to coding, it hasn’t been all sunshine and rainbows.

There have been times where I had to spend more time debugging AI-generated code than I would have probably spent writing the full thing myself.

The main problem is that AI almost never tells you “I don’t know how to do this” — it rather hallucinates and gives you the wrong answer.

So, I have learned to watch out for these situations:

1. ❌ Very recent stuff

If you ask for something that is relatively new (<2 years), there is a higher risk of hallucinations because 1) AI might not have seen it in the training data, and/or 2) examples of it were few.

1. ❌ Niche libraries — basically the same as above!

1. ❌ Specific library versions

AI isn’t good at keeping consistency between function signatures and the library versions you are using. Keep that in mind if you need something very specific.

1. ❌ Complex functions with a lot of context needed

AI is generally good at creating complex functions when they work in isolation (e.g. algorithms, math stuff, etc.) but it isn’t the best when it has to keep into account dependencies from a lot of other code.
