---
aliases:
  - "Prioritize bugs by severity and priority"
"Is A":
  - Evergreen
"Last Tweeted": 2023-05-08
Tags:
  - Has Pic
"Created at": "2024-04-18T14:44:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to":
  - "[[essay/how-to-prioritize-bugs|How to Prioritize Bugs]]"
  - "[[monday-ideas/monday-53|Monday #53]]"
  - "[[monday-ideas/monday-143|Monday #143]]"
"Old Created At": "2023-03-12T17:14:00.000+01:00"
"Updated at": "2025-02-11T14:41:00.000Z"
Status: Not started
Tweet: "CTOs, how do you prioritize bug fixes? Separating priority from severity is key. Focus on business impact first, then assess how broken the feature is. This avoids negotiation chaos and ensures a clear fix order. Let's discuss how you've tackled this! #TechLeadership #BugFixing"
notion_id: dadef6c0-b33b-4da4-b1ec-99e8a0c2465c
---

# Prioritize bugs by severity and priority

How do you decide what bugs to address first? This is trickier than it seems, as you may have different stakeholders and different opinions.

A good way to get to a consensus is to consider two separate values of importance for a bug: **priority **and **severity**.

- **Priority** — is *how bad this is for business*. How much revenues are we losing? How bad is the experience for customers? It should be assessed by the PM, with the help of customer support in case of user-reported defects.

- **Severity **— is *how badly broken the feature and software are*. Is this still usable? Why is this happening? Severity is assessed by QA and Engineers, who can ignore how *relevant* the broken feature is, to focus on how much it is individually impacted by the bug. Engineers can also evaluate whether the issue is symptom of a larger disease, and things are more broken under the hood than it seems.

Once you have set severity and priority values, you can simply fix bugs in this order:

1. **High Priority + High Severity** —  the login is broken and users can't access the tool.

1. **High Priority + Low Severity** — terms & conditions are not visible when users make the payment.

1. **Low Priority + High Severity **— the checkout doesn't work with some niche combination of device + browser. 

1. **Low Priority + Low Severity **— border radius of the button doesn't match the design system.

Basically, priority wins over severity, with the latter being considered when the former is equal.

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/631d83ff-20ce-4401-a614-56e2c0f97767/d91ff218-174f-4ae7-80d6-d8def81422c9/CleanShot_2025-02-11_at_15.40.512x.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663QXLXMNB%2F20260131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260131T190830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB7Jzp8W7yMSGKeksPPSBZE2p1%2Bpv7E4STgBHvzqwrGqAiBDO%2B40Du7MIcxk%2BmE9xS5ksE6V6DsF78eHwPFEA%2BfTvCqIBAi7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8m77EFnhZoj5x%2B4OKtwDJeMVClXszvexvCd2mw6SUKiYXwhOckZxxk8HrnN4puYgOcIj9z5PJzxOpeGal4TBukk%2BIsmPBUbIxHJnR59%2BD1zIXK5b1AqaBFnI2Vh%2BOCr0fR08sD02pAOXfkMEpEmjDY%2FCetkow7G3nH32TaMVTKMdRdYF0D%2F%2FiQY2uY3lQIua8mvZL9xhiSBs5xITGu40XvkiguoLzoxGu%2BA3F5FtWJSdaUJXr2UcGcT%2BcKAu25M2dRPbHUIkvmgiEADKKnZqalDYr4nvo7Q5ZRpfIQS3KLDb6EC%2BYtyWqxRNKColQAOcN4RlhsqeWMkPr72nFCDgk6vfwbXMouaI8S09llsgDV0bEXLMtBw0d3n6NVKDEGaHxpiBS47ac5JHvMnMlF1yP7iRF3gMyDUPMQVdhdcX7zvh1%2BhSumEeMExManh%2Fqao8nkrs102nxK%2FGnJ45m1wev%2BaVx45Hl57DOWPEfFXDB0nu%2FNoKKbYYzN2C%2FlGHnyU0IKqHuveaFXerozthriw00zC2aB%2BVgbMDtEdetlmr2fyWaaZQE8KVuy5l05KmuGmj5MkSEyC1j%2BjuCgqKnW%2BlC7GaMX%2Bf0bi%2BVxjja9SQh559%2Bymb7nKnqtqOVHpEAu%2B%2Bc1IXq41PRR9u4Hcwi4T5ywY6pgE7YfeTCIgs6exho4oPqhmc0p%2F81ZcU%2FIRDY6vzblFXlqKPUcHHX7yFM5ba8WaA%2FCcEoWliqqaYl%2BJxNi%2FqxOycTPP2xPI10vxYcwizJCqWugJafl9QWhxRHFTopl5B7EVTYJLKfY1%2FIKGMsmDK5lKH1vFImisw1RY6XR6en%2F0K%2FpRW4pT%2F0xc7YBIf7Lzkn4TqL2Wr0rOL%2BuUr%2B3M5ieoWnQG0gEeN&X-Amz-Signature=bd571c643387b78756f47713b1f1bb49d4e1889ea4ca7430871fa98c0626803e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

This is powerful for two reasons:

- **Separation of concerns:** it avoids the negotiation between the business and technical side of the team, because each side gives its own value separately.

- **Clear sorting:** It provides a clear rule for deciding in which order to fix bugs — one that doesn't need to be rediscussed every time.

Does the process above create the perfect sorting? No. But it should be *good enough* as long as you are *fast *at fixing bugs.

The faster you are at fixing, the less important the order is.

---

How to Prioritize Bugs 🐛

Bug fixing is not exactly everyone's favorite engineering activity.

It's a tricky process that requires coordination between several stakeholders — PMs, Customer Support, QA, and Engineers.

Let's figure out how to make it work 👇

Every team has a slightly different process, but it always involves some version of these steps:

1. ✍️ Report — bugs are entered in some kind of backlog.

1. 🚥 Prioritize — bugs are triaged and a priority is assigned.

1. 🔨 Fix — bugs are addressed and fixed by Engineers.

Out of these three, I have seen the most problems happen in the *prioritization* stage.

👑 Who takes such decisions?
⚔️ How do we avoid conflicts?
⏱️ How much time should we spend on it?

Let's figure this out 👇

👥 Stakeholders (1/2)

When it comes to priority, everyone in the loop has their own opinion:

1. 🏅 Customer Support — knows about users who need the fix, and what workarounds they have put in place.

1. 🎨 PM — knows how bad this is for users and business in general.

👥 Stakeholders (2/2)

1. 🔍 QA — knows how badly broken the feature is.

1. 🔨 Engineering — knows how bad this is for software.

Every point of view is legitimate and complementary, because no one sees the full picture.

Without a clear process that turns such opinions into actions, you risk:

1. ⚔️ Spending too much time and energy on negotiation

1. 🙋🏻‍♀️ Having people/roles feel underrepresented

1. ❌ Working on the wrong things

🎯 Goals

A good bug fixing process should have two goals:

🏆 Set "good enough" priorities — being inclusive, but without wasting anyone's time.

⚡ Ship things fast — so that the order in which things are fixed matters less.

Here are a few strategies to achieve them 👇

🔍 Separate Severity from Priority

To involve all stakeholders while also keeping conflicts low, separate two values of importance:

🥇 Priority
🔨 Severity

What are those? 👇

🥇 Priority

Priority is how bad this is for business.

– How much revenues are we losing?
– How bad is the experience for customers?

Priority should be assessed by PMs, with the help of Customer Support in case of user-reported defects.

🔨 Severity

Severity is how badly broken the feature and software are.

– Is this feature still usable?
– Why is this happening?

Severity is assessed by QA and Engineers. They can ignore how relevant the feature is, to focus on how much it is impacted by the bug.

🏃‍♂️ Process

Once you have set Severity and Priority, you can simply fix bugs in this order:

1. High Prio + High Sev

1. High Prio + Low Sev

1. Low Prio + High Sev

1. Low Prio + Low Sev

Priority wins over Severity, with the latter being considered when the former is equal.

This framework is powerful for two reasons:

🤝 Separation of concerns: it avoids the negotiation between the business and technical side of the team. Each side gives its own value.

🥇 Clear sorting: It provides a clear rule for deciding in which order to fix bugs.
