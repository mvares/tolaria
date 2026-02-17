---
aliases:
  - "How to Prioritize Bugs"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-essays|Publish Essays →]]"
Status: Everpictured
URL: "https://refactoring.fm/p/how-to-prioritize-bugs-"
"👓 Status": Not started
"URL 2": "https://twitter.com/lucaronin/status/1404337465960194049"
"Created time": "2024-04-18T14:53:00.000Z"
Date: 2021-06-11
"Has Notes": "[[evergreen/prioritize-bugs-by-severity-and-priority|Prioritize bugs by severity and priority]]"
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 7fb9d0ce-2b8b-4c1b-bbc6-246363daa185
---

# How to Prioritize Bugs

1. **What is the most important point?**

1. **Why is that the most important point? *****(what can you achieve with it)***

1. **Why should people care? *****(what's the benefit)***

1. **What is the easiest way to understand the most important point?**

1. **How do you want the reader to feel?**

1. **What should the reader do next?**

1. **The Three Qualities (*****pick 2+*****)**

### 📋 Outline

---

#### Point 1

#### Point 2

### ✍️ Post

---

Bug fixing is not exactly everyone's favourite engineering activity. 

It's a tricky process that requires coordination between several stakeholders, and it's not easy to get it right.

Think about it for a moment. Bugs might be reported by *Users* to *Customer Support*, reproduced by *QAs* / *Testers*, looked into by *PMs* and eventually addressed by *Engineers*.

It's a lot of people involved. 

Now, every team has a slightly different process for this, but it always involves some version of these steps:

1. ✍️ **Report **— bugs are entered in some sort of backlog (...or notified to devs on Slack 🙈)

1. 🚥 **Prioritize **—** **bugs are triaged and a priority is assigned. This might be done by QA, PM or Engineers themselves.

1. 🔨 **Fix **—** **bugs are addressed and fixed by Engineers.

Out of these three, I have seen the most problems happen in the *prioritization* stage. Who takes such decisions? How do we avoid conflicts? How much time should we spend on it?

Let's figure this out 👇

### 👥 Stakeholders

When it comes to the importance of fixing this or that, every person involved in the process has their own opinion.

- 🏅 **Customer Support** knows about users who need the fix, and what workarounds they have put in place.

- 🎨 **PM** knows how bad this is for users and business in general.

- 🔍 **QA** knows how badly broken the feature is.

- 🔨 **Engineering** knows how bad this is for software.

Every point of view is legitimate and complementary, because no one sees the full picture.

Without a clear process that turns such opinions into actions, you might:

- **Spend too much time on negotiation** — there is only so much time you can spend on deciding what do sooner or later, before it becomes more valuable to use that time for fixing bugs in any order instead.

- **Have people/roles feel underrepresented **— if process is unclear, priorities end up being defined by people with the loudest opinion or the most social capital.

- **Work on the wrong things **— You address issues in the wrong order and reduce the value you could bring. 

### 🎯 Goals

With that in mind, my ideal process for bug fixing should achieve two goals:

- **Get basic priorities right** — in a "good enough" fashion, being inclusive with people but without wasting anyone's time.

- **Ship things fast** — so that the order in which you fix things matters less.

How to achieve these goals? Here are a few strategies 👇

### 🔍 Separate severity from priority

A common way to involve all stakeholders in prioritization, while also keeping conflicts low, is to consider two separate values of importance for a bug: **priority **and **severity**.

#### Priority

Priority is **how bad this is for business**. How much revenues are we losing? How bad is the experience for customers?

Priority should be assessed by the **PM**, with the help of **Customer Support** in case of user-reported defects.

In many articles you find priority defined as *how quickly you should fix this*. I don't agree 100% with this definition — I think this is more of a *consequence* of how you define priority itself, that is, as the importance for the business. 

If you lose track of this meaning and only focus on the "how quickly", you get a recursive definition that is not very helpful. 

#### Severity

Severity is **how badly broken the feature and software are**. Is this feature still usable? Why is this happening?

Severity is assessed by **QA** and **Engineers**, who can ignore how relevant the broken feature is, to focus on how much it is individually impacted by the bug. 

Engineers can also evaluate whether the issue is symptom of a larger disease, and things are more broken under the hood than it seems.

#### Process

Once you have set severity and priority values, you can simply fix bugs in this order:

1. **High Priority + High Severity** —  e.g. the login is broken and users can't access the tool.

1. **High Priority + Low Severity** — e.g. terms & conditions are not visible anymore before users make the payment.

1. **Low Priority + High Severity **—  e.g. the checkout doesn't work with some niche combination of device + browser. 

1. **Low Priority + Low Severity **— e.g. border radius of the button doesn't match the design system.

Basically, priority wins over severity, with the latter being considered when the former is equal.

This framework is powerful for two reasons:

- **Separation of concerns:** it avoids the negotiation between the business and technical side of the team, because each side gives its own value separately.

- **Clear sorting:** It provides a clear rule for deciding in which order to fix bugs — one that doesn't need to be rediscussed every time.

![Priority, severity, and the order in which you should address bugs ](../assets/eada3493f4aa466c.png)

### 📋 Keep your backlog small

Does the process above create the perfect sorting? No. But it should be *good enough* as long as you are *fast *at fixing bugs.

The faster you are at fixing, the less important the order is.

How do you understand if you are fast enough? A simple KPI is that **the backlog is slim and it doesn't grow**. It's really important that *both* these conditions are met. In fact:

- If the backlog is *small* but it *grows *week over week, you are going to have a bad time in the long run.

- If the backlog is *big* but it *doesn't grow* anymore, it might simply mean people lost faith in your bug fixing, and stopped reporting new issues.

As a rule of thumb, consider the backlog as a [bad thing](https://thenewstack.io/mary-poppendieck-on-why-you-should-just-burn-your-backlog/) — and try to keep it as small as possible. Long backlogs destroy the feeling of progress and demotivate everyone in the team. 

If, despite your efforts, your backlog becomes too big, consider **declaring bankruptcy** and burn all items older than a few months. It might seem daunting, but important issues always resurface at some point, so you don't really risk to lose anything critical.

### ⏱️ Spend fixed time on maintenance

Spending adequate time on bug fixing is often challenging and subject to continuous negotiation. 

One approach that keeps things simple, while also limiting conflicts, is to allocate for it a fixed amount of time every week.

This time shouldn't be spent only bugs — it could include on general refactoring, library updates, and other small changes.

The right share of time depends on your team and your product, but I have seen many having success with something between 20 and 30%.

We have used this approach for many years, and I have written more about it in a [previous article](https://refactoring.fm/p/how-to-plan-and-execute-maintenance).

### 📚 Resources

To learn more about bugs, priorities and backlog, here are a few great articles:

- 📑 [**Why You Should Just Burn Your Backlog**](https://thenewstack.io/mary-poppendieck-on-why-you-should-just-burn-your-backlog/)** **— by [Mary Poppendieck](http://twitter.com/mpoppendieck). Mary is a legend who has been working on Agile for more of 25 years. In this article she articulates the risk of working with backlogs and excessive prioritization, and advocates for a simpler approach based on throughput.

- 📑 [**As a product manager, how do you prioritize bug fixes vs new product features?**](https://www.quora.com/As-a-product-manager-how-do-you-prioritize-bug-fixes-vs-new-product-features)** **This is a great Quora thread with so many interesting answers. I don't agree with all of them (e.g. not a big fan of the dedicated bug fix team), but it's refreshing to see the various perspectives.

- 📑 [**Difference Between Severity and Priority in Testing**](https://www.lambdatest.com/blog/bug-severity-vs-priority-in-testing-with-examples/#:~:text=Software)** **— by Kirandeep Kaur — This article does a great job at explaining the Severity and Priority concepts, complete with examples, advice and takeaways.

**And that's it for this week! How do you prioritize bugs? Are you happy with your process? Let me know in the comments 👇 or via email 📮**
