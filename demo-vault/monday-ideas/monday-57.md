---
aliases:
  - "Monday #57"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-monday-idea|Publish Monday Idea]]"
Status: Published
"👓 Status": Not started
"Created time": "2024-04-18T15:09:00.000Z"
Date: 2023-06-26
"Has Notes":
  - "[[evergreen/practice-gratitude-everyday|Practice gratitude everyday]]"
  - "[[evergreen/tips-for-creating-great-okrs|Tips for creating great OKRs]]"
  - "[[evergreen/the-three-stages-of-an-on-call-page|The three-stages of an on-call page]]"
Tags:
  - Monday
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: d15ce2ee-f81c-4e5e-9844-b99183358b69
---

# Monday #57

*Hey, *[*Luca*](https://twitter.com/lucaronin)* here! Welcome to the ****Monday Ideas ***💡

*Every Monday I will send you an email like this with ****3 short ideas**** about making great software, working with humans, and personal growth.*

*You will also receive a long-form, original article on Thursday, like the last one:*

- [**Skiller Whale — Inventing the Future of Tech Learning**](https://refactoring.fm/p/skillerwhale) 🎓

*To receive all the full articles and support Refactoring, consider subscribing if you haven’t already!*

Get full access to Refactoring ✨

[https://refactoring.substack.com/subscribe](https://refactoring.substack.com/subscribe)?

*p.s. you can learn more about the *[*benefits of the paid plan here*](http://refactoring.fm/about)*.*

---

### 💼 Are you hiring React developers?

Many people ask me for job opportunities, and just as many tell me they struggle at hiring. I still haven’t cracked how to help with this, so I am giving it a shot here!

**I know 20+ senior React engineers available for hire**. Location is Europe and LatAm.

If you are interested, just reply to this email, or shoot me a DM on [Twitter](https://twitter.com/lucaronin).

---

### 1) 🎯 Tips for creating good OKRs

You can find plenty of articles on how to create good OKRs. 

![image](../assets/bd361ca1963e4030.png)

Every company eventually finds out the secret sauce that works for them. Here are some tips that worked well for me in the past:

- ✍️ **Don’t obsess over the right formulation **— yes, KRs should be *numeric*, but you can really write them any way you want as long as they measure success. Look at them and ask yourself “*would I be happy to achieve this*?” — if the answer is yes, then it’s fine!

- 🙋‍♂️ **Avoid personal OKRs **— if you are new to the process, create only team OKRs. Personal OKRs are tricky and can backfire spectacularly.

- 5️⃣ **Max five** — I have found that five is a magic number for OKRs. Try not to create more than 3-5 KRs for each objective, and to have at most 5 objectives for each team. Ideally, the full OKRs should fit in a single page.

- ⏱️ **Timebox the process **— don’t spend one month over OKRs leaving your team with a 2-month quarter to work on them. Give yourself tight deadlines to create good-enough items. Done is better than perfect. 

- 🗓️ **Don’t assume your will only work on OKRs** — over the OKR period there will be setbacks, maintenance, or unexpected opportunities you will want to catch. Leave some slack to allow your team to work on them. After some iterations we settled with assigning only 50% of the time to OKRs.  

- 👑 **Have someone accountable **— appoint someone to be responsible for the overall process. This person should collect the materials, set meetings and deadlines, follow up with people, and make sure everything is done in time. 

- ⚖️ **70% vs 100% rule** — there is advice that says you should create *stretch *goals that people are happy to achieve at 70%, and there is also counter-advice that says you should create achievable goals to make people happier. To me it doesn’t really matter, as long as you are consistent with the strategy you choose. People adapt quickly to either way.

- ➡️ **Follow up **— grade OKRs regularly: bi-weekly or monthly at most. Do not just create them and revisit them at the end of the period. You can attach OKR review to other review ceremonies you already have to make it more natural.

More ideas and examples about good OKRs below! 👇

[https://refactoring.fm/p/how-to-create-good-okrs-](https://refactoring.fm/p/how-to-create-good-okrs-)

---

### 2) ⏰ The three-step on-call

When you get paged during an on-call *shift*, you should follow a three-step process:

1. 🔍 **Root-cause analysis **— figure out the issue. Enabled by good *alerting* and *instrumentation*.

1. 🛠️ **Remediation **— put the system back up. Enabled by good *playbooks*.

1. ➡️ **Follow-up activities **— update docs and do a bunch of things. Enabled by good *process*.

Let’s see all three.

#### 🔍 Root-cause analysis

Root-cause analysis is about figuring out what’s wrong. This is made possible by good alerting and instrumentation. In fact, alerts you receive are of two kinds:

- **Customer-based** — e.g. slow response time.

- **Engineering-based** — e.g. memory full, various resources, etc.

In a perfect world, people should only be paged by customer alerts. In reality, you may end up with paging people for customer alerts + the most serious engineering ones, in case you have gaps somewhere and the latter do not fire also some of the former.

#### 🛠️ Remediation

Remediation is about putting the system back to an acceptable level of service. 

This shouldn’t be confused with fixing bugs: you can remedy an incident *without* fixing a bug, and without even knowing what the bug is. 

In fact, this is the ideal course of action: you restore the system first, and fix the bug later. 

Of course, this is not always possible. Sometimes, fixing the bug == restoring the system, like with many frontend issues. But other times you can split the two. Think of a memory leak — you may be just fine by restarting the instance, while you take more time to figure out where the issue is.

#### ➡️ Follow-up activities

After remediation, you have a number of things to do to leave a clean situation. These include:

- **Update docs / playbooks** — if what you did involved anything not documented.

- **Write a postmortem **— for non-negligible incidents.

- **Fix bugs** — for when this is separated from remediation.

These are called *follow-up* because you don’t have to do everything in the same session — especially when you get paged out-of-hours. But the closer to the incident, the more context you will retain, and the easier and the more accurate these will be.

I wrote more about good on-call processes in a previous Refactoring article 👇

[https://refactoring.fm/p/on-call](https://refactoring.fm/p/on-call)

---

### 3) 🙏 Gratitude makes me happier

I keep my daily routine very lean. In the past I have been guilty of setting overly complicated habits, just to scrap them after a few months because they were unsustainable.

One of the few that stood the test of time is about *gratitude*.

Every day, before I start to work, I write down something I am grateful for. When I started — about two years ago — I naturally focused on the big things: family, health, work, etc. I still come back to them sometimes, but, since I don’t want to repeat myself too much, over time I started being grateful for smaller and smaller things. Like receiving the call of a friend. Or, like today, for getting better at blitz chess lately 🤷‍♂️

Being grateful for something means **not taking it for granted**, which is like *lowering your expectations*.

![image](../assets/d068451f56694d90.png)

It forces you to be aware of what you already have, so you don’t raise the bar of your expectations uncontrollably.

Which, in turn, makes you happier.

I wrote a full article last year about expectations and happiness 👇

[https://refactoring.fm/p/expectations-vs-happiness](https://refactoring.fm/p/expectations-vs-happiness)

---

### 🗓️ Akiflow

---

And that’s it for today! If you are finding this newsletter valuable, consider doing any of these:

**1) ✉️ Subscribe to the newsletter** — if you aren’t already, consider becoming a paid subscriber. You can learn more about the [benefits of the paid plan here](http://refactoring.fm/about).

Get full access to Refactoring ✨

[https://refactoring.substack.com/subscribe](https://refactoring.substack.com/subscribe)?

**2)** ❤️ **Share it** — Refactoring lives thanks to word of mouth. Share the article with your team or with someone to whom it might be useful!

I wish you a great week! ☀️

Luca
