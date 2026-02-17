---
aliases:
  - "Feature flags build vs buy"
"Is A":
  - Evergreen
"Last Tweeted": 2022-08-04
"Created at": "2024-04-18T14:44:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to":
  - "[[Feature Flags / Feature Management]]"
  - "[[monday-ideas/monday-35|Monday #35]]"
"Old Created At": "2022-07-21T16:36:00.000+02:00"
"Updated at": "2024-04-19T09:37:00.000Z"
Status: Not started
notion_id: 6864702f-2d54-4a39-8b66-7ea5c9230032
---

# Feature flags build vs buy

Feature flags look like a simple system. Indeed, many teams I know have built in-house solutions to support them.

However, since flags are useful for so many purposes, the scope of these systems tends to creep over time, making them anything but simple 👇

> *Dropbox ended up with two separate custom-built system. The high-level one (Gandalf/Stormcrow) had lots of bells and whistles for A/B testing with complex rules. There was later a lower-level one for infrastructure services called Kiev, which had fewer dependencies and more predictable performance. I made use of Kiev for a lot of gradual rollouts limited to percentages or specific pools of users, and it was invaluable.

– Andrew Twyman, Dropbox*

> *In Prezi we use feature flags extensively via an in-house tool, every team is using it. My team extended it to provide support for configuring A/B tests. This was a major step forward for us to increase experimentation velocity, which was critical for my team as we've scaled up.

Our in-house solution is capable of gradual rollouts, A/B testing and restricting features based on a lot of conditions, so sometimes we need to restrain ourselves from trying to squeeze in too much business logic into it

– Zoltan Adamek, Prezi*

The tricky aspect is that basic flagging behaviour is indeed simple, but you will likely expand on it over time.

People will ask support for A/B testing; for A/B testing you will need metrics and granular targeting; at that point you will likely need auditing, to track who changed what. 

Before you realize it, the flag service becomes the one with the highest load in your system, and keeping it fast and reliable becomes non-trivial.

Putting my CTO hat, my take is that feature flags are a commodity, with a cost of total ownership that can be very high. 

They also have strong lock-in, which is an argument often used *against* external services, but it is equally scary when you are locked into a nightmar-ish custom tool that you need to maintain forever.

My take is that you are probably better off either 1) using a managed service, or 2) hosting one of the many open source tools out there.

Which tools? Here they are 👇

### 🔨 Tools for Feature Flags

- [LaunchDarkly](https://launchdarkly.com/) — arguably the most widely used tool for feature management, it is hosted and allows for granular user targeting.

- [Optimizely](https://www.optimizely.com/) — started as an A/B testing tool, it is now a full suite that includes feature flags, a CMS, marketing and e-commerce tools.

- [Unleash](https://www.getunleash.io/) — the most popular open source solution. Features are comparable to LaunchDarkly, and provides a [native integration](https://docs.gitlab.com/ee/operations/feature_flags.html) with GitLab.

- [GrowthBook](https://www.growthbook.io/?r=prd-ffs) — open source platform that you can either host or choose to use as a managed service. Simpler than many others, it still provides the basics: flags, A/B tests, segmentation.

- [Env vars + Doppler](https://www.doppler.com/) — some companies implement basic feature flagging via environment variables (we did that too, in the past). While this has clear limitations (e.g. changing a variable needs a reboot), it is also simple to setup and performance is very fast. In this case, you can use a service like Doppler to sync variables across the instances and manage them from a single place.
