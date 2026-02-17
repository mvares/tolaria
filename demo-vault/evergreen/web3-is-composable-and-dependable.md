---
aliases:
  - "Web3 is composable and dependable"
"Is A":
  - Evergreen
"Created at": "2024-04-18T14:44:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to":
  - "[[essay/web3-engineering-part-1|Web3 Engineering (Part 1)]]"
  - "[[monday-ideas/monday-37|Monday #37]]"
"Old Created At": "2022-01-07T16:25:00.000+01:00"
"Updated at": "2024-04-19T09:37:00.000Z"
Status: Not started
notion_id: f01df4f1-073a-4023-9c4b-a99ade4ea360
---

# Web3 is composable and dependable

Whatever we can think of the web3 space, whether it is a piece of the future, or just a box full of scams, it is useful to reflect on the qualities of the blockchain as a technology. 

The most interesting angle to me, as an engineer and an entrepreneur, is that blockchain is actually a computer — one with two peculiar qualities: it is **public**, and it is **immutable**.

These qualities matter because, in turn:

- A public computer makes data and software 🧩 **composable**

- An immutable computer makes it 🔒 **dependable**

### 🧩 Composable

More than [99% of software](https://tim.blog/2021/10/28/chris-dixon-naval-ravikant-transcript/#:~:text=99.9%20percent%20of%20the%20code%20in%20the%20world%20is%20open%20source%20software%20that%20runs) that runs on servers today is **open source**.

Open source won because of its **composability**. When you think about it, it allows to solve a problem exactly once for everybody, and allows them to combine that solution with others.

Software, however, cannot run itself. It needs to be hosted on servers — and these are arguably *private*. This means production software gets controlled by private entities, and, crucially, this includes data — as databases are software themselves.

Private servers, and especially private databases, vastly reduce the potential for composability. APIs and access are limited to what companies allow people to do.

You can think at Ethereum (and other competing projects) as a protocol that enforces public data and publicly run software. This vastly increases composability* *because it makes it *permissionless*. You can use and contribute to the same database everyone uses, and combine public software at API level (not source code level).

### 🔒 Dependable

Composability wouldn’t work if the blockchain wasn’t also *dependable*. Being blocks immutable, you are guaranteed that data and software won’t change, or will do so only under conditions that are public and well-known.

This means we have now software that can make **commitments**. It is no mistake that a piece of software that runs on blockchains is called a *smart contract*. It is a contract because it is **binding**.

With regular software, databases and apps are run under control of some entity, so software is dependable only if you **trust** such entity to uphold its commitments. With blockchains, instead, these are upheld by software itself.

This allows you to build and combine apps without the need to trust (to a certain extent) parties involved, which in turns vastly expands the design space of what you can build.

- [Untitled](https://www.notion.so/bc251d604e7546f19757dbb161488826) 

Check out this great article by Chris Granger to learn more: [https://chris-granger.com/2021/12/09/is-web3-anything/](https://chris-granger.com/2021/12/09/is-web3-anything/)

 
