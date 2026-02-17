---
aliases:
  - "Break down projects into stepping stones"
"Is A":
  - Evergreen
"Created at": "2024-04-18T14:44:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to":
  - "[[essay/planning-software-under-uncertainty-with-james-cowling|Planning Software under Uncertainty — with James Cowling]]"
  - "[[monday-ideas/monday-81|Monday #81]]"
"Old Created At": "2023-07-06T12:21:00.000+02:00"
"Updated at": "2024-04-19T09:37:00.000Z"
Status: Not started
notion_id: 027c4d5f-4245-468a-a718-b874b62d9d1b
---

# Break down projects into stepping stones

### 🗿 Stepping stones

When there is no linear path from path to finish, James likes to break down work into *stepping stones*. Stepping stones are not your generic *milestones* — they need to have these qualities:

- **Incremental** — you can continue building on top of each one.

- **Valuable** — they are useful. They solve the problem, even if in an inefficient / expensive / precarious way.

- **Instructive **— they make you *learn* more about the problem space, so you can eliminate some of the *fog of war* and design better solutions in the next iterations.

Let’s make a practical example of the Dropbox storage system that James designed. The end game of this project might look like a giant, multi exabyte system deployed in data centers around the US. But, put like this, 1) it would cost a huge sum of money, and 2) it would involve daunting technical challenges, like designing a file system and its hardware architecture.

So, James scopes the problem down into deliverables that get you closer and closer, while being valuable on their own:

1. Let's build an in-memory storage system that just works on one node.

1. Make it run on one node and store data on a disk.

1. Turn it into a distributed system — still not efficient — but correct.

1. Make the distributed system efficient and scalable.

Good stepping stones are a win for all the people involved:

- **They unblock stakeholders **— because they have a partial solution they can interact with. They can give you feedback and create more alignment with engineers.

- **They motivate the team** — because they shipped something that works!

- **They might be a stopping point **— they might turn into *stopping* stones (hehe) if the company decides it’s enough.

The last point is the real litmus test: if, after a stepping stone, you can drop the project and get some value, then it’s a good stepping stone.

And this will happen. If you do your job right, you *will* drop projects before the supposed end. In fact, engineers often think that systems need to be *more* optimal than they really need to be. A surprising upside of designing good stepping stones is that they often make you do *less *work, because you discover you didn’t really need part of it.

#### Stepping stones and MVPs

So, I feel this conversation is closely related to MVPs, and how to design them. There are several examples and pictures online, but personally I dislike most of them.

Here is probably the most famous one 👇 by (the great!) Henrik Kniberg

![image](../assets/6d7a05a772134e55.jpeg)

The problem with this picture — the bottom part — is that intermediate steps *might* be valuable, but don’t get you closer to building a car. 

If your idea is to build a car, there are probably reasons for that: you might want a trunk, you might want 2-5 seats, etc. A bike is great but it doesn’t solve the same problems.

I know this is just a drawing and I am reading too much into it, but I care about getting this right. In software, stepping stones for a good car look more like… a car made of cardboard! Or a car that consumes an outrageous amount of fuel. And that’s where comparisons with reality break: you wouldn’t ship a car made of cardboard in real life — but in software you would. And you would upgrade the *chassis* in a later update.

So, while the whole stepping stones *idea* is intuitive, *how you* *design *them often it is not.

The best way to move forward on a hard problem might be to design a *disgusting* solution in 48 hours, and improve it over time. Because it is much easier to improve a system that works, than to keep everything in your head.
