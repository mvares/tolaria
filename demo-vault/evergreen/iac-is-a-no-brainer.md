---
aliases:
  - "IaC is a no brainer"
"Is A":
  - Evergreen
"Created at": "2025-04-22T13:14:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to":
  - "[[essay/good-engineering-techniques-for-2025|Good Engineering Techniques for 2025 📡]]"
  - "[[monday-ideas/monday-168|Monday #168]]"
"Updated at": "2025-08-06T13:35:00.000Z"
Status: Not started
notion_id: 1ddbdf02-815c-8079-8321-d7c37ad65084
---

# IaC is a no brainer

Infrastructure as Code (IaC) is the practice of provisioning infra through code instead of manual processes (i.e. clicking around in cloud consoles).

IaC has overwhelming benefits:

- 🪄 **Reproducibility** — infra can be created, destroyed, and recreated consistently across envs.

- ↩️ **Version control** — infra changes get tracked just like application code.

- 🤖 **Automation** — reduces human error and speeds up deployment.

- 📑 **Self-documentation** — the code itself documents what infra exists and how it's configured.

These benefits have existed for a long time, at the expense of some additional config work upfront. The factor that heavily tips the scale today is, again, AI.

AI is good at understanding and generating infrastructure code. This means you can describe what you want in plain English, and AI can help generate the corresponding infrastructure code.

The most used tools for this are **Terraform** and **Ansible**:

1. [**Terraform**](https://www.terraform.io/) — is the gold standard for cloud-agnostic infrastructure provisioning. It allows you to define what should exist (VMs, networks, databases) in declarative fashion, and it maintains state to track and manage these resources over time.

1. [**Ansible**](https://www.redhat.com/en/ansible-collaborative?intcmp=7015Y000003t7aWQAQ) — configures systems and deploys applications using procedural, stateless automation. It is YAML-based and allows you to install software, manage configurations, and run tasks on infrastructure that already exists.

So, Terraform and Ansible are complementary: the former builds the environment, and the latter sets it up.

> Getting deeper into Infrastructure as Code techniques on my IT estate. (To be specific: containerised workloads; Ansible). I know I’m late to that party, but as a software guy and a one-man shop I tend to operate infrastructure on a “set it up once and hopefully never need to touch it again” basis. Well, this month I have been forced into a hardware upgrade, and suddenly it looks like the time I invested last year is paying off! — Ross Younger
