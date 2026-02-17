---
aliases:
  - "Top-down Vibe Coding"
"Is A":
  - Evergreen
Tags:
  - Has Pic
"Created at": "2025-05-18T15:16:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to":
  - "[[essay/vibe-coding-workflow|Vibe-Coding Workflow]]"
  - "[[monday-ideas/monday-164|Monday #164]]"
"Updated at": "2025-07-07T07:42:00.000Z"
Status: Not started
Tweet: "Are we leveraging generative AI effectively in project planning? A top-down approach can enhance clarity and control, reducing errors before code generation. Let's discuss how this workflow impacts developer engagement and project outcomes. #TechLeadership #AI #SoftwareDevelopment"
notion_id: 1f7bdf02-815c-80f2-9e64-edaf8c4b7e9e
---

# Top-down Vibe Coding

Using generative AI can be very incredibly effective to plan out and implement entire projects — but it can also make you run in circles and eventually *lose* time with respect to doing all the work yourself.

The difference between a successful and an unsatisfactory output often lies in good prompting, and, even more, in your prompting *workflow*.

For new developments, like new features or entire small projects, we have found that the most effective workflow is a top-down interaction that goes through several steps.

![image](../assets/1f7bdf02815c8096.png)

You can begin with a discussion about your work requirements, and, step by step, get to high-level system design, the full code spec, classes and functions scaffolding, up to the fully coded version.

Working top-down (as we will see in the example) is incredibly helpful in keeping the developer *engaged* in the work. It optimizes human cognitive load and allows to intercept errors at the right level. In fact, you don’t want to rectify system design elements, or worse, requirements misunderstandings, after the AI has written the full code — just like you don’t want it with humans.

Still, many vibe-coding examples you can find online dive code-first into AI implementation, which is easily overwhelming for humans and more prone to errors.

Let’s see how this works in a real-world example. For an initial requirements brainstorming, you can use a simple prompt like this:

#### Example prompt

> *I am a product manager and you are a senior software architect. Let's have a brainstorming session where you ask me one question at a time about these requirements, and come up with a specification that I can hand to a software developer.*

#### Example output

> *Great! Let’s break this down systematically. I’ll start with foundational questions, then dive deeper into specific requirements and constraints.*

Also remember that voice prompting is faster than typing, and less cognitively intense! You can use that especially for the first steps.

Once you’ve engaged in enough questions, the AI will let you know that you are moving into final questions, and may produce a summary similar to this:

> *Your system is now:*

Given a similar prompt to the one above, the assistant will then ask if you are ready to create a code spec based on these answers, and whether there are any final requirements.

It will produce a spec similar to the following truncated example output:

> ***Software Specification — Cassandra to ElasticSearch Indexing System***

As powerful as this process is already at this stage, we can take this workflow even further by **scaffolding code** from this spec, and then use **mid-loop code generation** on that scaffolding to generate a draft of the application code itself.

By working top-down it is **easier for a developer to** **retain control **over what is being produced, and correct mistakes at the *right* *altitude*. Design mishaps can get rectified before any code is generated, and structure corrections can happen when the code is still at scaffolding stage.

This is still *vibe-coding*, but it focuses on generating the *right vibes*.
