---
aliases:
  - "How to Do Mobile Testing Right"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-essays|Publish Essays →]]"
Status: Evergreened
URL: "https://refactoring.fm/p/how-to-do-mobile-testing-right"
"👓 Status": Not started
"Created time": "2025-04-18T17:09:00.000Z"
Date: 2025-05-14
"Has Notes":
  - "[[evergreen/what-is-mobile-fragmentation|What is mobile fragmentation]]"
  - "[[evergreen/the-cost-of-fragmentation|The Cost of Fragmentation]]"
  - "[[evergreen/fragmentation-testing-playbook|Fragmentation testing playbook]]"
  - "[[evergreen/fragmentation-testing-vs-product-maturity|Fragmentation testing vs product maturity]]"
Tags:
  - Guest
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 1d9bdf02-815c-805d-a27f-e35e22e769ec
---

# How to Do Mobile Testing Right

### 📑 Materials

---

### ✍️ Post

---

Mobile apps are the primary interface through which hundreds of millions of people interact with services daily. 

Smartphones have been a thing for 15+ years, during which they arguably changed… not so much, especially in recent years. For this reason, it may be reasonable to expect a *flawless* experience at every tap.

Instead, the reality is different and painful — especially for mobile engineering teams: an ever-expanding universe of devices, hardware, OS versions, screen resolutions, and capabilities, that software must navigate correctly. 

Welcome to ~~hell~~ **mobile fragmentation**.

In my previous life as a startup CTO, I ran a travel web app that had native counterparts on iOS and Android, and I swear that mobile testing and QA was one of the things that kept me up at night. It is incredibly hard to do it right, yet supremely important, having a direct impact on user satisfaction, churn, and ultimately, the bottom line.

So today we are publishing a full guide on *fragmentation testing *which provides a comprehensive but pragmatic approach to the problem, by covering principles, strategies, and tools.

We are doing so by drawing from my own learnings, from the ones of people in the Refactoring community, and by bringing in the invaluable experience of **Nakul Aggarwal**, CTO and co-founder of BrowserStack. BrowserStack is a cornerstone of how thousands of teams — including my former own — engage with real-device testing at scale, and Nakul is one of the world’s most knowledgeable people in this space.

So, as you will see, success in mobile testing is about making smart choices, and focusing your efforts where they yield the greatest return. We'll explore how to define "good enough" in a world of infinite variables, and how to build a testing approach that supports, rather than hinders, your engineering velocity.

Here is the agenda:

1. 💥 **What is mobile fragmentation?** — defining the beast and its many heads.

1. 📉 **Cost of fragmentation** — the real-world business consequences.

1. 📖 **Fragmentation testing playbook **— how to build your full testing process, from strategy down to tactics.

1. 🪜 **Testing strategy vs product maturity** — how your playbook should evolve over time. 

1. ⚖️ **Navigating the trade-offs** — balancing cost, speed, coverage, and developer experience.

1. 🔮 **The Future is Still Fragmented** — trends, the role of AI, and some closing notes

Let's dive in!

---

### 💥** What is Mobile Fragmentation?**

We've thrown the term "*mobile fragmentation*" around, but what do we mean by that? Spoiler: it’s not something that happens to your phone screen after a drop.

At its core, mobile fragmentation is the sheer diversity of hardware and software across the millions of devices your application might encounter in the wild.

Such diversity is also *multi-dimensional*:

- 📱**Device manufacturers (the *****who*****) **—** **from the big players like Apple and Samsung, to the long tail of Xiaomi, Oppo, OnePlus, and the countless regional champions. Each comes with its own hardware quirks, custom Android *skins*, and unique interpretations of how Android *should* behave.

- 📋 **Operating systems & versions (the *****what***** & *****when*****)** —** **you need to account for multiple major versions active concurrently. Update rollouts lead to notorious lags, and some devices *never *get updated beyond a certain point. This is true for both iOS and Android, with Android being typically much worse.

- 📏 **Screen sizes & resolutions (the *****where*****)** — today’s smartphones range from compact screens, to *phablets*, foldables, and tablets: the range is vast. Other than physical size, you may also need to account for pixel density, aspect ratios, and newer features like dynamic refresh rates or screen cutouts (notches, punch-holes), that can all wreak havoc on your UI if not handled gracefully.

- ⚙️ **Hardware differences (the *****how*****) **—** **beneath the glass, there's even more: processors, memory constraints, GPUs, and sensors, which may or may not make a difference in how your app behaves.

Trying to account for every permutation is impossible. Understanding these dimensions, however, is the first step to building a *smarter* strategy.

---

### **📉 The Cost of Fragmentation**

One of the things I always try to do at Refactoring is to think from first principles, so the first question here is: what if you just *ignore* this? Seriously, let’s not take anything from granted.

How bad is this, for real?

Unfortunately, when fragmentation is managed poorly, it bites hard — on your users, your team, and the business:

- 💔 **Poor UX** — the most immediate impact. Users encounter crashes, freezes, baffling UI glitches, or sluggish performance that makes the app feel broken. Frustrated users are 1) unlikely to give you a second chance, and 2) they often head straight to… 👇

- ⭐ **Bad reviews **— users are quick to voice their displeasure, and negative App Store reviews are incredibly damaging—it doesn’t matter if they are about a small set of devices. A flood of "unusable on Android 12" reviews will torpedo your app's rating, affecting everyone.

- 📉 **Churn** — if an existing user has a persistent issue on their device after an update, or a new user has a terrible first experience, they're likely to abandon your app. Acquiring users is expensive: losing them due to preventable issues is a painful, self-inflicted wound.

- 📞 **Support costs** — your support team gets swamped with tickets and complaints related to device-specific bugs. Diagnosing these can be a nightmare, requiring detailed information about device models, OS versions, and steps to reproduce that users often struggle to provide.

- 🐌 **Slower dev velocity (*****ironically*****)** — if you are trying to move faster by *avoiding *thorough testing, think again. Fragmentation bugs in production can lead to constant firefighting and a reactive development cycle. This drains morale and pulls your team away from feature development.

Investing in a good testing strategy isn't just about "quality assurance" in an abstract sense: it's about protecting your revenue, your reputation, and your team's ability to move fast.

So how do you do that? 👇

---

### 📖 Fragmentation Testing Playbook

We have established the *why —* now for the *how*. This section should work as your tactical playbook: the core strategies and tools you'll use to construct a robust, pragmatic mobile fragmentation testing process.

This playbook focuses on four key pillars:

1. 📊 **Device matrix** — your clear, data-driven plan of *which* devices and OS versions matter the most to *your* users.

1. 🧪 **Testing mix** — a balanced portfolio of emulators, real devices, and cloud solutions to maximize coverage and efficiency.

1. ✅ **Foundational quality** — strong architecture, base testing, and monitoring to significantly reduce the number of bugs that reach device-specific testing.

1. 🤖 **Automation strategy** — manual testing doesn't scale, and smart automation is crucial for maintaining velocity and reducing toil for your team.

Let's break these down 👇

#### 1) 📊 Build your device matrix

Your **Device Matrix** is the single most important artifact guiding your testing. It’s a curated inventory of devices and OS versions, tiered by importance, against which you validate your app. Here is how you build one:

🔍 **Know your actual users (*****be data driven*****)**

First of all, be data driven. Prioritize based on which devices, OS versions, and even geographical regions are most prevalent among *your* user base.

**Action:** Dive into your analytics. Understand *your* specific device landscape. What are the top 10, 20, 50 devices your active users are on? What OS versions dominate? This data is the bedrock of your device matrix.

**⚖️ Prioritize (*****risk assessment*****)**

Not all devices or features are created equal in terms of risk. 

Risk, in this context, is a function of *likelihood* (how many users on this device/OS?) and *impact *(how critical is this feature? What happens if it breaks?).

**Action:** Focus your most intensive testing on high-traffic user flows running on the most popular devices/OS versions within your user base. A bug in your checkout process on your top 5 Android devices is infinitely more critical than a minor UI glitch on an obscure device with little market share among your users.

**🪜 Define tiers (*****risk acceptance*****)**

Since you can't test everything equally, you need to explicitly define levels of risk you're willing to accept for different device segments. This formalizes your prioritization.

**Action:** Create device/OS tiers. For example:

- 🥇 **Tier 1 (Critical)** — your most popular devices/OS versions (e.g. top 80% of your user base). Bugs here are unacceptable. These devices get the full suite of manual and automated tests for all critical and important features.

- 🥈 **Tier 2 (Important)** — the next significant chunk of devices. Minor cosmetic issues might be tolerable, but core functionality must work. These might get critical path automation and focused manual testing.

- 🥉 **Tier 3 (Supported/Best Effort)** — older or less common devices. You aim for basic functionality, but known issues might be documented and not block a release if non-critical. Testing might be limited to smoke tests or exploratory testing if time permits.

🔄 **Keep it alive**

Finally, create a process in which you review and update the matrix on a periodic basis (e.g. quarterly), as your user base and the market will inevitably evolve. Your matrix is only useful as long as it is up to date.

#### 2) 🧪 Create your testing mix

No single testing method conquers fragmentation, but a balanced portfolio might do. Here are the most common approaches:

- 💻 **Emulators & Simulators **— emulators are the first line of defense for developers. They are fast, free, scalable for basic layout and functional bug checks during development. However, they can't perfectly replicate real hardware performance, sensor behavior, or OEM-specific OS mods.

- 📱 **Real devices (In-house lab) **— they provide the highest fidelity for performance, hardware interactions, and manufacturer quirks… but they can be expensive and logistically challenging to maintain.

- ☁️ **Cloud device farms **— the scalable solution for broad real-device testing (manual and automated) without owning hardware. Platforms like BrowserStack give you on-demand access to thousands of physical devices/OS versions globally, and allow precise matrix mirroring and massive test parallelization.

#### ✅ Establish foundational quality

Strong underlying code quality and good production significantly eases the load on device-specific testing. Your goal should be to minimize the number of issues that get to *device-level*, by intercepting them earlier:

- 🔒 **Strong typing & static analysis** — strongly typed languages like TypeScript (React Native), Kotlin, and Swift help you catch a lot of errors before runtime. Employ linters for further analysis.

- 🧩 **Robust unit & integration tests** — ensure core logic, utilities, and API integrations are thoroughly covered. Unit and integration tests are fast and cheap to run, especially compared to E2E tests.

- 🏛️ **Architect for testability** — design choices matter. Keep the mobile app *light* by pushing as much business logic as possible in the backend layer, where it is easier to test. If you are using a universal framework like React Native or Flutter, restrain as much as possible from writing platform-specific code.

- 📊 **Intensive logging & production monitoring** — your safety net. Implement good monitoring with tools like Firebase Crashlytics or Sentry, to catch issues that slip through as early as possible.

#### 4) 🤖 Automation strategy

Manual testing across a large matrix is unsustainable, but implementing automation across the board can be equally hard. Do smart automation choices for streamlining key areas while maintaining velocity:

- 🎯 **Focus your automation** — don't try to automate everything. Prioritize critical user flows ("must not break" scenarios) on your Tier 1 devices. Use well-established frameworks (Appium, Espresso, XCUITest).

- 🚀 **Parallelize with cloud platforms** — running suites sequentially is a bottleneck. Platforms like BrowserStack enable massive parallel execution across hundreds of configurations, providing fast feedback in CI/CD.

- 👀 **Incorporate visual regression testing** — for UI-heavy apps, these tools automatically detect visual changes across devices, catching layout bugs functional tests miss.

- ✨ **Reduce toil & boost DevEx** — automation's goal is to free your team from repetitive manual checks, leading to faster, more reliable feedback and higher developer confidence.

---

### **🪜 Testing Strategy vs Product Maturity**

The principles we covered should somewhat work for everyone, but the truth is your specific approach to fragmentation should also change over time, and evolve alongside your product and team journey.

Obviously, applying an *enterprise* level of testing rigor to a pre-PMF product is a waste of resources, just as neglecting deeper testing once you *have* scale is a recipe for disaster.

So let's try map your fragmentation strategy to the typical **QA / Product Journey** stages we have discussed [other times in the past](https://refactoring.fm/p/how-to-do-qa-in-2024?utm_source=publication-search).

![Your fragmentation strategy should evolve alongside your product](../assets/1ecbdf02815c801b.png)

There is a lot of nuance and “your mileage may vary” here, but let’s sketch a basic cheatsheet:

#### 1) 🌱 **Zero-to-One**

- **Focus** — Speed, iteration, and validating core hypotheses.

- **Fragmentation Approach** — Minimal and highly pragmatic.

- **Key Takeaway** — Don't let fragmentation concerns prematurely slow you down. Focus on finding PMF.

#### 2) 🪴 **Finding PMF / Early Growth**

- **Focus** — Stabilizing core features, growing the user base, and starting to understand user segments.

- **Fragmentation Approach** — Begin to formalize, driven by initial user data.

- **Key Takeaway** — Use early data to guide a *Minimum Viable Testing* process for fragmentation.

#### 3) 🌳 **Scaling / Established Product**

- **Focus** — Reliability, performance at scale, expanding feature sets, and protecting brand reputation.

- **Fragmentation Approach** — Strategic, data-driven, and increasingly automated.

- **Key Takeaway** — Your fragmentation strategy is now a core part of your quality engineering process, deeply integrated and data-informed.

---

### **🛠️ Strategies for Taming Fragmentation**

---

### **⚖️ Navigating the Trade-offs**

---

### **🔮 The Future is Still Fragmented**

So, will fragmentation ever end?

Probably not, at least not anytime soon. While there are glimmers of hope ([Google's Project Mainline](https://source.android.com/docs/core/ota/modular-system), for instance), the fundamental drivers of diversity remain.

Hardware innovation in smartphones might be questionable today, but new form factors emerge all the time (foldables are already here, wearables are well established, and AR/VR may be on the horizon), and OS customizations persist.

#### What about AI?

There's certainly potential for AI to assist with this. Established tools like BrowserStack are testing AI-powered workflows already. AI may write test cases, better simulate E2E flows, and even predict high-risk device/OS combinations based on code changes.

However, for the core challenge of executing tests across diverse hardware remains, and AI is not a silver bullet.

The reality is that the right mindset and an intentional strategy (data-driven device matrix, smart testing mix, strong foundational quality, targeted automation) remain your most crucial assets for navigating the mobile landscape. 

The landscape will shift, but the principles of smart, risk-based testing will endure.

---

### 📌 Bottom line

And that’s it for today! Remember that navigating the fragmented world of mobile devices is a marathon, not a sprint. Here are some takeaways from today’s guide:

- 📊 **Let data drive your device matrix** — your *actual* user analytics are the most reliable guide for deciding which devices and OS versions deserve your primary testing focus. Don't guess; know.

- ⚖️ **Embrace tiered, risk-based testing** — not all devices or bugs are created equal. Prioritize ruthlessly, focusing maximum effort on high-impact areas and accepting calculated risks elsewhere.

- 🛠️ **Blend your testing mix wisely** — combine emulators (for speed), a curated in-house lab (for frequent access/fidelity), and cloud device farms like BrowserStack (for breadth, scale, and specialized needs).

- 🧱 **Build on foundational quality** — strong typing, linting, robust unit/integration tests, and good architectural choices significantly reduce the burden on expensive end-to-end device testing.

- 🤖 **Automate strategically, not exhaustively** — focus UI automation on stable, critical user flows on your most important devices to reduce toil and get fast feedback, leveraging parallel execution in the cloud.

- 🔄 **Evolve your strategy with maturity** — the right level of testing rigor changes as your product grows from pre-PMF to scale. continuously adapt your approach.

---

### **🎯 A Pragmatic Approach**
