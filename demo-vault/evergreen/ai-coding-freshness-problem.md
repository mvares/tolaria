---
aliases:
  - "AI coding freshness problem"
"Is A":
  - Evergreen
"Last Tweeted": 2023-03-12
Tags:
  - Has Pic
"Created at": "2024-04-18T14:44:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to":
  - "[[essay/ai-the-future-of-coding|AI & The Future of Coding]]"
  - "[[monday-ideas/monday-44|Monday #44]]"
"Old Created At": "2022-12-23T16:23:00.000+01:00"
"Updated at": "2024-09-18T08:44:00.000Z"
Status: Not started
Tweet: "As we increasingly rely on AI for coding, the \"freshness\" problem emerges. I recently had ChatGPT generate a Telegram Bot in Node.js, but it relied on outdated practices—callback functions instead of async/await, and deprecated methods. This highlights a crucial issue for tech leaders: how do we ensure we're not perpetuating old frameworks just because AI favors them? Let's discuss the implications for our development practices and adoption of new technologies."
notion_id: b75cd5dd-6e83-4911-896a-5be5b63cebbd
---

# AI coding freshness problem

I am very excited about using AI to write code. One thing I am worried about, though, is freshness 🍎

A few weeks ago I asked ChatGPT to create a Telegram Bot, written in Node.js.

After generating the code, I asked it to use the Serverless framework to turn it into a function that I could easily deploy on AWS.

Amazingly enough, it did it.

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/631d83ff-20ce-4401-a614-56e2c0f97767/83f30963-57b6-4199-9751-a25f210fbdb5/CleanShot_2022-12-14_at_09.41.252x.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BQ7MWM2%2F20260131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260131T190652Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDwcfqw8TOntFX%2F8rxLAqKw2Y%2F0KfP7UNRd4f8%2FE6R8TQIhANElIy%2F%2BeTsR8EWCLw%2BdWJ7csEPR7MBbf0yQ9%2B0qTRe%2FKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgztsETrAGeqlGT%2BxgEq3AN6MeIZ3NQ9SL2xplLM0VI1f9yIwAvLvD0c5I6bgAnYKklCY3IvoEApKSJ9BPJnojQaprEjTdoH0iDidVUdUDqcGciUxqyCSla%2FJldMcCZuuNYr7Uj1m2O0S1VxYvBYEDVifP8st0Ep8XbynxyMA8vA3Lb%2FRCmc8JBKIXIJGeE0tXo9qLGObT3a69l0H0cHYci20AL3zmqEjBg9g3FTWQOKpP6UwwfddYV6UYQl3Sxt2aWQEuQWGpWGtuI4%2FQwP3OU%2FFJw%2Fzb4Vw5CCeKcGSArt0Tfgr0xiZG%2F1%2Fu5I7G0Lo7rw%2BWB0WLAtW1fH9zPXIu8XqMNc9B6oJcigfEyPBKxe2pckXlSBUOhPRWSapHnb7okkycJTMMX6Aw1Cf48F4AAKuLgpPKY2at4bUpgXG36STarhHLniN8JF0PyG3EGsXQ3ulnwJi5ZyJ5UPvqW0B6Z3Sx9ENR5yMkl4BuqcE7VZbmOu1%2BA8DtPVK%2F2RPGKTA4y%2FBlkBE9W9X9J0KZmInVMtbTtQER5fLSSY2zXpC1pgzbi3vbUYzQOM5X5LGHK41XojzZnA1aJb2qVWQ5qqhuJXUFyifKPb6y%2FyrF%2FEcfLr5F%2FCTXFRqsC52%2BY%2BDUidabCC1newZkD4atvnDzD7iPnLBjqkAeAK%2BCe2hvgn4QFys0hQURlgP7fYEZT0mRqTerjUCNfO5bzVILEt4VQQWfPELv0%2FbBT10JOa5Ge20zahOy6vhxNUEQl0iKWiB4%2FI5MsByZYnVrBOGBLNwvA9jr5ufVSwLgh1Vmghim06CqIbHyQ%2FAboOUJ%2BqCYxNzN4%2FW3NMbs8%2FEvz2NqZMTC8EWI%2BKy9%2BcrTX6KT2urXZ%2BnlSCj2w5pCRtGL14&X-Amz-Signature=a25f04c4ad7a5dfec626521b9f1df16255271d458cae8461ff5cabceea5d449c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

 The code works, but there are two problems:

- It uses the old way of handling the function — with the callback — while the recommended way today uses the *async / await *syntax.

- It uses the deprecated “*on*” method for the Telegram Bot, instead of the new filter utils.

This likely happens because you can find way more examples online with these methods than with the new ones, as the former have been around for longer.

This *freshness* problem worries me for two reasons:

- **I have no way of detecting it** — sure, if you know you should use *async/await* you can ask the AI to rewrite the code, which it will happily do, but *you have to know *it first.

- **It is *****intrinsic***** to how AI works** — the model is trained on data and is statistical based, so it is naturally going to favour stuff where it has the most content.

---

I am very excited about using AI to write code. One thing I am worried about, though, is freshness 🍎

A few weeks ago I asked ChatGPT to create a Telegram Bot, written in Node.js.

After generating the code, I asked it to use the Serverless framework to turn it into a function that I could easily deploy on AWS.

Amazingly enough, it did it.

The code works, but there are two problems:

1. It uses the old way of handling the function—with the callback—while the recommended way today uses the async / await syntax.

1. It uses the deprecated "on" method for the Telegram Bot, instead of the new filter utils.

This likely happens because you can find way more examples online with these methods than with the new ones, as the former have been around for longer.

This *freshness* problem worries me for two reasons:

1. I have no way of detecting it — sure, you can ask the AI to rewrite the code in the new way, but you have to know it first.

1. It feels intrinsic to how AI works — the model is trained on data, so it is always going to favor stuff for which it has the most of it.

I wonder whether, in the future, new frameworks will have a tougher adoption curve because people will just stick with the ones where the AI is best.
