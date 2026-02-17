---
aliases:
  - "Feature Flags / Feature Management"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-essays|Publish Essays →]]"
Status: Evergreened
URL: "https://refactoring.fm/p/feature-flags"
"👓 Status": Not started
"Date HH": 2025-05-29
"URL 2": "https://twitter.com/lucaronin/status/1555100517545791488"
"Created time": "2024-04-18T14:53:00.000Z"
Date: 2022-06-30
"Has Notes":
  - "[[evergreen/should-you-deploy-on-fridays|Should you deploy on Fridays?]]"
  - "[[evergreen/feature-flags-build-vs-buy|Feature flags build vs buy]]"
  - "[[evergreen/manage-dependencies-in-feature-flags|Manage dependencies in feature flags]]"
  - "[[evergreen/clean-up-feature-flags|Clean up feature flags]]"
  - "[[evergreen/enforce-naming-policies-for-feature-flags|Enforce naming policies for feature flags]]"
  - "[[evergreen/feature-flags-are-useful-for-many-things|Feature flags are useful for many things]]"
  - "[[evergreen/trunk-based-dev-brings-higher-velocity-and-lower-cycle-time|Trunk-based dev brings higher velocity and lower cycle time]]"
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: e650a3c1-c754-4561-bdec-1dc590b17b00
---

# Feature Flags / Feature Management

### ❓ Six Questions

### 📑 Materials

---

[https://martinfowler.com/bliki/FeatureToggle.html](https://martinfowler.com/bliki/FeatureToggle.html)

[https://cloud.google.com/blog/products/devops-sre/the-2019-accelerate-state-of-devops-elite-performance-productivity-and-scaling](https://cloud.google.com/blog/products/devops-sre/the-2019-accelerate-state-of-devops-elite-performance-productivity-and-scaling)

[https://www.atlassian.com/continuous-delivery/principles/feature-flags](https://www.atlassian.com/continuous-delivery/principles/feature-flags)

### 💡 Ideas

---

<details><summary>✅ **Chiamaka Nwolisa **— hide 99% — multiple countries — non-tech people</summary></details>

<details><summary>✅ **Andrew Twyman** — custom-built system — proliferation of flags</summary></details>

<details><summary>✅ **Carlo Caprini **— native feature flags on GitLab</summary></details>

<details><summary>✅ **Maina Wycliffe** – we use them to test changes in conversion</summary></details>

<details><summary>✅ **Miguel Nunes Correia **— don’t block prod — trunk-based dev — env vars with Doppler</summary></details>

<details><summary>✅ **Alex Stoia** — tied to permissions</summary></details>

---

### ✍️ Post

---

Much of modern software engineering is about shipping fast and often.

Studies like [Accelerate](https://en.wikipedia.org/wiki/Accelerate_(book)) and the [State of DevOps](https://cloud.google.com/blog/products/devops-sre/the-2019-accelerate-state-of-devops-elite-performance-productivity-and-scaling) demonstrated that teams that ship the most often are also the most likely to meet or exceed business goals.

> *Highest performers are twice as likely to meet or exceed their organizational performance goals — *Accelerate

One of the key insights about shipping fast is that it doesn’t hurt *stability*.

Rather, it’s the opposite.

Shipping fast and often enables 1) shipping smaller changes, and 2) recovering faster from mistakes. These both reduce risk and bring stability. 

As a rule of thumb, the faster and the more often you are able to release, the more stable your system will be.

[Embed](https://twitter.com/lucaronin/status/1368827812858232833)

When you think about it, this is both wildly **counterintuitive** and entirely unique to software.

When you build a bridge, making it faster doesn’t make mistakes less catastrophic, nor allows you to recover faster from them.

In regular engineering, waterfall pays off. In software it generally doesn’t, but it took a while to figure it out.

### Enter Feature Flags

Many practices exist today to being able to release in production asap, while keeping the risk low. These include trunk-based dev, gradual rollouts, kill switches, and more.

Many of such practices are made possible by **feature flags**.

At their core, feature flags are a simple idea: allow to enable / disable functionality without deploying new code.

Such idea, however, has vast ramifications, and over the years feature flags became a swiss army knife used in the most disparate scenarios.

This article covers everything you need to know about feature flags:

- 📋 **How do feature flags work?** — principles and implementation

- 🎯 **What do you use feature flags for?** — the most useful use cases

- ⭐ **Best Practices** — naming, maintenance, access, and more

- ⚖️ **Build vs buy** — should you build your own system or buy a managed solution?

- 🔨 **Tools **— the best ones to implement feature flags properly

Let’s dive in!

### 📋 How do feature flags work

Feature flags are variables stored in some system and checked in real-time to verify whether a feature is active or not.

The simplest implementation in your code is an **if / else** statement:

```ruby
show_feature = ff_client.get_flag("your.flag.key")

if show_feature
	# application code to show the feature
else
```

A separate panel usually displays your active flags, their status, and allows you to add/remove them.

![image](../assets/56eb52444f1a4df6.jpeg)

From here, things usually get more complex, in two ways:

- Rather than simple on/off values, flags can store **sophisticated rules **about features display.

- Rather than passing just the name of the flag, you can pass the system additional **information about the user** or the **session**, that contribute to the decision.

This way, you can use feature flags to implement more granular use cases, like feature targeting based on user attributes, % shutdown/rollout, A/B tests, and more.

Let’s see the most popular, and useful, use cases 👇 

---

### 🎯 What they are useful for

#### Trunk-based dev

Trunk-based development is a version control workflow where developers work in small batches and merge their work into the main trunk as often as possible — usually at least once a day.

That is opposed to the common workflow of *feature branches*, where developers create a separate branch for each new feature, and then work in isolation on that branch until the feature is complete.

There is convincing evidence that teams who adopt trunk-based workflows achieve higher velocity and shorter cycle time.

[Embed](https://twitter.com/jezhumble/status/1415908836439773185)

However, not all projects can be broken down in small, working parts that get completed within a day. How should you work in those cases? 

Enter feature flags.

![image](../assets/b0076065bda643e2.png)

With feature flags, you can keep code in a *disabled *state, and merge it to the trunk even if the feature is not complete.

Small and frequent merges have some major benefits:

- Easier code reviews

- Less chance of conflicts

- Reduced risk for releases

Miguel Nunes Correia, Head of Engineering at Subly, told in the community how they use flags for productivity 👇

> *At Subly we use feature flags to easily enable and disable new features in the app, this way our production branch doesn't get blocked by new features that aren't production ready yet and allows our team to start testing them in our staging environment. 

It also happened in the past that a new release feature was behaving unexpectedly, so having that quick kill switch at hand was quite useful.

I think we're going to use it even more feature flags in the near feature as we transition into a trunk - flow.*

#### Gradual rollouts

You can make a newly released feature available only to a small subset of users, to reduce risk.

This can be implemented with most feature flag systems, which can be also configured to gradually expand the subset, up to a 100% rollout.

#### Kill switch

You can instantly disable features that are behaving unexpectedly, without rolling back the code. 

This further decreases the risk of each release, to the point where it’s not uncommon for teams that make heavy use of feature flags to skip the staging environment and deploy directly in production 👇

[https://refactoring.fm/p/do-you-need-staging](https://refactoring.fm/p/do-you-need-staging) 

#### A/B tests

Similarly to gradual rollouts, you can A/B test new changes to check their impact on business KPIs.

[Maina Wycliffe](https://mainawycliffe.dev/), Software Engineer at Skyhook, uses them to test for conversion rates 👇

> *We use them to test changes we aren't sure the impact on conversion, something may sound great on paper but might discourage customers from completing their booking with us*

#### Access control

If you have different customer tiers which should access different sets of features, you can use feature flags to implement access control.

**Alex Stoia**, CTO at Innertrends, told me how they do it 👇

> *We use feature flagging quite often, it's integral to our development and deployment process. But in our case it's directly tied to our internal permissions system which handles 'who can access what'. For us a feature is something that eventually would be included in the permissions system so why not included from the start?

This way, if something is in working or not ready yet, no one has permission to access it (or see it), in alpha testing only a few clients have access to it, and so on. And this is easily controlled from an administration page.*

#### Feature management

Gradual rollouts, kill switches and access control allow for a granular control of a feature life cycle. This whole practice is sometimes called *feature management.*

For companies who run features this way, it becomes a central part of their workflow. 

**Chiamaka Nwolisa**, Software Engineer at HelloFresh, explains their vast usage of feature flags

> *At my current company (>1000 engineers), we basically **hide 99% of features** behind feature flags.*

### ⭐ Best Practices

Managing feature flags at scale brings a special set of issues that may not be trivial to anticipate. Here are some best practices I collected from teams who make heavy use of them 👇

#### 🔡 Naming

You should enforce a clear policy about naming flags, to avoid *naming hell *later. Here are two tips:

- **Create buckets **— create bucketing rules that adapt to your workflow. You can use names of modules, parts of products, or totally made up categories. The ideal criterion should be 1)  easy to apply at all times, and 2) should stand the test of time. 

- **Separate permanent and temporary flags **— most teams have temporary flags for testing purposes and permanent ones for general feature mgmt. These have totally different goals, and you should separate them. You may explicitly *flag *temporary flags (hehe) to 1) remember to delete them, and 2) keep them separated from the rest.

#### 🧹 Maintaining flags

When feature flags become a first class citizen of your dev workflow, it may be hard to fight against their proliferation.

In my experience, most feature flags end up being temporary and should be deleted at some point. This is hard to perform reliably at scale, as widely reported.

Andrew Twyman — former Staff Engineer at Dropbox 👇

> *The biggest problem Dropbox ran into was **proliferation of flags which never got deleted**, and became landmines in the code. We had multiple SEVs where the feature gating itself went wrong, and ended up executing code which should never have executed. This ended up creating a very gunshy culture around feature flags, with limitations being built into the systems to force them into specific scenarios, and ensure that no path became dead code*

Zoltan Adamek, Engineering Manager at Prezi 👇

> *One of the most interesting aspects for me is how feature flag usage relates to clean code. Knowing when to clean up those flags exactly is super hard, and the codebase can suffer a lot if you don't manage to keep things under control. Any feature flag usage is by definition introducing tech debt, because

– either the feature stabilizes and you don't need the flag anymore

– or the feature will be removed (e.g. losing variants of A/B tests) so you need to remove the entire thing.

The only exceptions to this are the so-called emergency feature flags, which are stuff you want to keep indefinitely. We have some, which for example can help with keeping more serious infra fails under control.*

To prevent *flag hell*, here are three effective strategies:

- **Clean up branches** — whenever you create a new flag, to also create a *cleanup* branch with the code that removes the flag. You immediately submit the cleanup PR and keep it open until you are ready to remove the flag. You can reject the PR that adds the new flag if the author didn't also submit the cleanup PR.

- **Cap to temporary flags** — you can put a cap to the number of temporary flags that can be active at any given time. When you reach the cap, whenever you would create a new one you should also remove an old one. You can easily check for this at PR time. 

- **Clean up sprints** — if things get really bad, consider allocating dev cycles to clean up the mess. I always prefer gradual solutions that are embedded in the process, but if nothing else work, this should do the trick!

#### 🎌 Dependencies / cascading flags

When your system gets complex enough, you may find yourself with flags that depend on each other to work. There are two kinds:

1. **Nested flags** — a flag controls a feature which is a part of a larger module controller by another flag.

1. **Coupled flags **— a feature controller by a flag that only works if something else, controlled by a different flag, is active.

Two pieces of advice here:

- **Use namespaces **— for nested flags, enforce *namespaces* to make it clear which flags are *children *of others. E.g. you may have flag “a.b.c” and flag “a.b” to make it intuitive that the former depends on the latter.

- **Avoid coupled flags** — just don’t do it. Switching a flag should always leave the system in a working state. Being loose on this rapidly turns flags into nightmare.

### ⚖️ Build vs buy

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
