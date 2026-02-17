---
aliases:
  - "When you should use fine-tuning"
"Is A":
  - Evergreen
Tags:
  - Not for Monday
"Created at": "2024-04-18T14:44:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to":
  - "[[essay/how-to-embed-llms-into-your-tech-stack|How to embed LLMs into your tech stack]]"
  - "[[essay/lessons-from-the-podcast|Lessons from the Podcast]]"
"Old Created At": "2024-01-18T11:00:00.000+01:00"
"Updated at": "2025-10-07T15:49:00.000Z"
Status: Not started
notion_id: dccdb82a-41c8-464e-a5ae-8f5b69ac8f1a
---

# When you should use fine-tuning

With the AI FOMO being in full display these days, you may be tempted to create custom LLMs for your business by fine-tuning existing open source solutions, like Llama, with your own data.

Disheng, VP of Engineering at Translated, a company who has built its own models for 20+ years, says *not so fast*.

First of all, what does **fine-tuning*** *even mean? 

Fine-tuning means further specializing a model — that has already been trained on a wide data distribution — on a smaller, task-specific dataset. The goal is to modify the model’s parameters to make it perform better on the task at hand.

These days, as models get bigger and prompt engineering gets better, fine-tuning is becoming more and more niche. In fact, it only makes sense if *all *these conditions are met:

1. 👎 **The base model performs extremely poorly** — you can’t figure out any way to make the base LLM do the job for you

1. 🗃️** You have a *****massive***** amount of data** — that you may fine-tune the model on. We are talking millions of tokens about something the model has never seen.

1. 🎓 **You have solid ML expertise in house** — fine-tuning is long, costly, and uncertain. You may easily spend hundreds of thousands of dollars and end up with a model that doesn’t do better than your standard GPT-4.

To this day, successful examples of fine-tuning are usually in domains where there is a lot of **private** **+ domain-specific data**, like in healthcare or finance. In this case in fact there is a good chance that:

1. **Base models *****haven’t seen***** this data at all** — because it’s usually private, so they perform badly on related tasks.

1. **You don’t want to share this data with OpenAI** — or other commercial entities. That’s because of the data being sensitive, terms and conditions with customers, and your own strategy.

So, how can you figure out if fine-tuning is for you? Disheng suggests to start with a small engine with fewer parameters, validate on it, and only scale up if promising, while ensuring the test set is representative of the final use.
