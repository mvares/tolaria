---
aliases:
  - "Monday #168"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-monday-idea|Publish Monday Idea]]"
Status: Published
"👓 Status": Not started
"Created time": "2025-08-06T13:23:00.000Z"
Date: 2025-08-11
"Has Notes":
  - "[[evergreen/the-four-images-of-leadership|The Four Images of Leadership 🪞]]"
  - "[[evergreen/iac-is-a-no-brainer|IaC is a no brainer]]"
  - "[[evergreen/in-small-teams-hybrid-ems-tls-work|In small teams, hybrid EMs + TLs work]]"
Tags:
  - Monday
  - Free
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 247bdf02-815c-80d5-bcc8-df10e941124c
---

# Monday #168

### 1) 🪞 The Four Images of Leadership

Two months ago we published an incredible article by [Thiago Ghisi](https://www.linkedin.com/in/thiagoghisi/) about [Engineering Manager Archetypes](https://refactoring.fm/p/the-engineering-manager-archetypes).

One of the things I love the most about Thiago’s piece is that it builds on research that goes well beyond engineering. One of the references I love the most is [“The Archetypal Images of Leadership”](https://www.researchgate.net/publication/325819196_The_Archetypal_Images_of_Leadership) by Shirshendu Pandey, which is built on Jungian theory and organizational psychology, proposing four archetypal leader images:

1. 🔒 **Administrator **— focused on *maintenance* and *functioning*, through *stability* and *security.*

1. 🪴 **Guide **— focused on *humanistic growth* and *supporting others*, through *affiliation* and *bonding*.

1. 🏆 **Achiever **— focused on victory and success, through sheer *drive* and *achievement*.

1. 🔋 **Catalyst **— focused on *transformation* and *innovation*, through *inspiration *and *engagement.*

This study speaks to our unconscious projections: how people naturally see leaders, not just how leaders label themselves.

There are other, related, archetypical models, which build on similar principles:

- [Eight Archetypes of Leadership](https://hbr.org/2013/12/the-eight-archetypes-of-leadership) — by Manfred Kets de Vries’, which identifies *Strategists*, *Change-Catalysts*, *Transactors*, and more.

- [Competing Values Framework](https://www.quinnassociation.com/en/robert_e_quinns_competing_values_framework) — from Robert Quinn, which maps cultural archetypes (like Producer, Mentor, Innovator) to organizational behavior.

What all these models have in common is they focus on **how leaders drive impact.**

![image](../assets/247bdf02815c8039.png)

Behaviors like driving change, hardening processes, or nurturing people development feel like core *modes of operation*, rather than skills or tasks.

Thiago then took this approach and tailored it to the tech industry dynamics — like scaling teams, product iterations, or the nuanced split between hands-on engineering and strategic alignment.

You can check out the full piece below 👇

[https://refactoring.fm/p/the-engineering-manager-archetypes](https://refactoring.fm/p/the-engineering-manager-archetypes)

---

### 2) 🏗️ Infrastructure as Code is a no-brainer with AI

Infrastructure as Code (IaC) is the practice of provisioning infra through code instead of manual processes (i.e. clicking around in cloud consoles).

IaC has (always had) overwhelming benefits:

- 🪄 **Reproducibility** — infra can be created, destroyed, and recreated consistently across envs.

- ↩️ **Version control** — infra changes get tracked just like application code.

- 🤖 **Automation** — reduces human error and speeds up deployment.

- 📑 **Self-documentation** — the code itself documents what infra exists and how it's configured.

These benefits have existed for a long time, at the expense of some additional config work upfront. The factor that heavily tips the scale today is, unsurprisingly, AI.

AI is good at understanding and generating infrastructure code. This means you can describe what you want in plain English, and AI can help generate the corresponding infrastructure code.

The most used tools for this are **Terraform** and **Ansible**:

1. [**Terraform**](https://www.terraform.io/) — is the gold standard for cloud-agnostic infrastructure provisioning. It allows you to define what should exist (VMs, networks, databases) in declarative fashion, and it maintains state to track and manage these resources over time.

1. [**Ansible**](https://www.redhat.com/en/ansible-collaborative?intcmp=7015Y000003t7aWQAQ) — configures systems and deploys applications using procedural, stateless automation. It is YAML-based and allows you to install software, manage configurations, and run tasks on infrastructure that already exists.

So, Terraform and Ansible are complementary: the former builds the environment, and the latter sets it up.

We documented more good techniques that you may want to pick up this year in our yearly tech radar 👇

[https://refactoring.fm/p/the-refactoring-tech-radar-for-2025](https://refactoring.fm/p/the-refactoring-tech-radar-for-2025)

---

### 3) 💂‍♂️ Do you need full-time managers?

How do you decide whether you need full-time managers, or you can get away with engineers who also do some manager stuff? 

Let’s be very practical.

The [main responsibilities](https://refactoring.fm/p/how-far-without-managers) of engineering managers are usually about planning, aligning stakeholders, and taking care of the health and growth of the team.

In small teams, this might not equate to a lot of work, because:

- **Planning is straightforward** — timeframes are short, no cascading goals throughout departments, and no endless juggling with resource allocation.

- **Alignment is easy** — your whole team works together on a single product, and external stakeholders are few. Piece of cake!

Hiring, onboarding, and taking care of people might still be hard work, but hey, manager-wise it’s basically everything you have to do!

So when your team grows to the point where you need to establish management behaviour for the first time, it is natural to look at people who already exhibit some leadership traits—tech leads or senior devs—and ask them to take care of 1:1s, planning duties, and so on.

![image](../assets/247bdf02815c800a.png)

It makes sense!

And for these hybrid managers, tech work is still a big chunk of their days:

- They do 1:1s, but also weigh in on design decisions.

- They help with planning but also do PRs and write critical code.

Now, it is important to understand that, for many, this isn’t a quick rite of passage. Most companies are not *hyper-growth VC-fueled* startups. 

Many remain at this stage… *forever*. These companies may *never* need full-time managers, and that’s ok.

For others the levee breaks at some point, because, as you grow, the management side gets heavier (happy problem!).

We talked about this in a group coaching session we held a few years ago 👇

[https://refactoring.fm/p/non-technical-managers](https://refactoring.fm/p/non-technical-managers)

---
