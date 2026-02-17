---
aliases:
  - "The three-stages of an on-call page"
"Is A":
  - Evergreen
Tags:
  - Long
"Created at": "2024-04-18T14:44:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to":
  - "[[essay/on-call-process|On-call Process]]"
  - "[[monday-ideas/monday-57|Monday #57]]"
"Old Created At": "2022-12-23T16:28:00.000+01:00"
"Updated at": "2024-04-19T09:37:00.000Z"
Status: Not started
notion_id: 1f16d0ca-e6c8-4cf9-a89c-16ee4f1b6e77
---

# The three-stages of an on-call page

During an on-call *shift*, you can get paged anytime by alerts that report some issue in the system. When this happens, you follow a three-step process:

1. **Root-cause analysis **— figure out the issue. Enabled by good alerting and instrumentation.

1. **Remediation **— put the system back up. Enabled by good playbooks.

1. **Follow-up activities **— update docs and do a bunch of things. Enabled by good process.

Let’s see all three.

#### Root-cause analysis

Root-cause analysis is about figuring out what’s wrong. This is made possible by good alerting and instrumentation. In fact, alerts you receive are of two kinds:

- **Customer-based** — e.g. slow response time.

- **Engineering-based** — e.g. memory full, various resources, etc.

In a perfect world, people should only be paged by customer alerts. In reality, you may end up with paging people for customer alerts + the most serious engineering ones, in case you have gaps somewhere and the latter do not fire also some of the former.

Andrew Twyman, former Staff Engineer at Dropbox, weighed in on this 👇

> *We had both. The customer-facing alerts were the ones on which we defined our SLA/SLO, and had stated policies about response times, incident severities, etc.  We also had alerts on things like resources, unresponsive machines, etc. Those were often more informational, and provided secondary signals to help the oncall debug what was going on. E.g. if you're paged for a high overall error rate, and you also get an alert that the number of machines in the pool is lower than normal, it gives you a place to start investigating.*

#### Remediation 

Remediation is about putting the system back to an acceptable level of service. This is important to understand because it shouldn’t be confused with fixing bugs.

You can remedy an incident *without* fixing a bug, and without even knowing what the bug is. 

In fact, this is the ideal course of action: you restore the system first, and fix the bug later. It is not always possible, of course. Sometimes, fixing the bug == restoring the system, like with many frontend issues.

But sometimes you can split the two. Think of a memory leak — you may be just fine by restarting the instance, while you take more time to figure out where the issue is.

#### Follow-up activities

After remediation, you have a number of things to do to leave a clean situation. These include:

- **Update docs / playbooks** — if what you did involved anything not documented.

- **Write a postmortem **— for non-negligible incidents.

- **Fix bugs** — for when this is separated from remediation.

These are called *follow-up* because you don’t have to do everything in the same session — especially when you get paged out-of-hours. But the closer to the incident, the more context you will retain, and the easier and the more accurate these will be.
