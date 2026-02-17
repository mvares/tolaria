---
aliases:
  - "Hunters vs Farmers"
"Is A":
  - Evergreen
"Last Tweeted": 2024-05-02
Tags:
  - Has Pic
"Created at": "2024-04-18T14:44:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to":
  - "[[essay/monolith-vs-microservices|Monolith vs Microservices]]"
  - "[[monday-ideas/monday-39|Monday #39]]"
"Old Created At": "2022-10-13T15:18:00.000+02:00"
"Updated at": "2024-05-02T06:51:00.000Z"
Status: Discarded
Tweet: "Transitioning from hunter-gatherer to farming was a pivotal moment in human history, but it came with unexpected drawbacks: longer hours, poorer health, and new diseases. As tech leaders, we face similar decisions—engineering choices that seem beneficial now may have hidden consequences down the line. How do we ensure sustainable growth without sacrificing well-being? Let's discuss."
notion_id: b0aab245-32cb-4fee-be61-bb526274d84b
---

# Hunters vs Farmers

In the book [Sapiens](https://www.goodreads.com/book/show/23692271-sapiens), historian Yuval Noah Harari spends some initial chapters explaining the transition of humans from the *hunter-gatherer *lifestyle, to the *farmer* one.

In doing so, he debunks several myths about the life of prehistoric men.

Hunter-gatherers lived a simple, happy life: they had a diverse diet, famine was rare, they were physically fit, and, contrary to popular belief, they only had to work a few hours a day.

The transition to farming, instead, brought some [unexpected setbacks](https://web.cs.ucdavis.edu/~rogaway/classes/188/materials/diamond). Farmers had to work long hours, sometimes twice as much as their hunter ancestors did. Their health got worse because of intense work, bad diet (mainly carbs), and diseases brought by the poor hygiene of primordial villages.

The farmer lifestyle had one main upside, though: it could produce *more food*, which would sustain the creation of larger communities.

In other words, life sucked at pretty much everything, but hey — it was scalable now!

Does it remind you of anything? 

The first farmers were pretty much the engineers of the prehistoric world. To their defense, nobody chose to made their own life worse *on purpose* — on paper, odds where *overwhelmingly *in favour of the farming life. Most downsides were not obvious (e.g. diseases, diet problems) and wouldn’t be so until generations later.

Many big engineering choices are similar. Implications are far reaching, and we may fail to account for the second and third-order consequences.

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/631d83ff-20ce-4401-a614-56e2c0f97767/ceb83c73-ea28-450a-8850-20464d6f7f58/CleanShot_2022-10-08_at_11.58.582x.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UMAAZ7SR%2F20260131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260131T190635Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBfEbuTQYCosNwMuAapYOFbiZ%2B5vDTauXfrX8OZ62x7XAiBtc%2B1yLN%2BSvRQ6D2h3%2BTET7uVDAIustE0geI7zhPC0syqIBAi7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMCNXiC9zVG%2Fq4sxktKtwDT9Wv3eBXtSLAE8B%2FX963KNczNIcN5Nwo7BK79YtKU2fVokqvbRnPQqtI4ES837DUGCL8DVKu8JJ%2BgxH72TtMXwQPJ6ftBKaEuLPqFL7m7FT4v79xIIW3ADc9Aglv0ToUweqnZzG3MGWZf2Bcnx%2FLgHhMUPMPowWfSfV7dK2IxA4RLAyHgePP3DLG44j74pUzT%2FtNL9W2I8ICvWdEGM5WDttE18bIUDCe8plhqZmo90e%2BXvLZqEFg76yqiVF2bSkW7eWNJO2iMBD4vAKgUEFLek95O0J4x94C0tnQY%2Bf3nGPKUMrJFB7CZ8Jutao4GNCLqG%2BzLR0C%2FZlsLwLsNW%2FLDG9BCKZp1LLhnwm2TEISnLrl3V1KphMgNAa%2BTX4ViybKBRMbqkovpe5DHHi5cQu4AILw%2FvGoa%2BrQAyv5OYhp%2BMkb2PFH1VWFtDI%2B%2Bt%2BtdsJJ8%2FktRDUHlDBS%2BgrbI1TIcWB%2FOXY0Qur0UsiBtEMuxf29FcJf%2BBT1cCuURuWVgubYqefnyMm6QKhJsr0K%2FmITXdM1ACfencdFeUORbIHnDSCCzyKMDi1QdvYCSJ%2FrWyaxrebvimvBGXghMt%2Bybp9jEjkpndVgHz4yTOdl7HNlE7VHLQ4SK9cJRh02S2Uwl4T5ywY6pgF16Y51t%2FhZauDQ1Hoe0XPq9EJboMCStqM7FRh2q6ie0%2F1pcLW4QHa4%2F9n7sRBgnlW9gW7B1TZPgLv5U1RkWr1WufhNt0ze7H5sn5gjCfP6oM3JbhtPYP3AX7yLFzM00zU0ds7JKFqCA2jSq3eK4EvPTZPUdHdjmsp6hP8Wh7bgIiZbM%2FYTrMF9YuZG51zzLztlMPJwDxyx3ollTcb7JAzg7iDIJqVH&X-Amz-Signature=d5fd5a66bd8ae6a267382fd9172629c5dc5bc918d29f094a57878e15bbd481c6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
