---
aliases:
  - "Cloud vs on-premise infrastructure"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-essays|Publish Essays →]]"
Status: Evergreened
URL: "https://refactoring.fm/p/cloud-vs-on-premise"
"👓 Status": Not started
"Created time": "2024-04-18T14:53:00.000Z"
Date: 2022-12-01
"Has Notes":
  - "[[evergreen/cloud-vs-on-prem-is-about-velocity-and-profits|Cloud vs on-prem is about velocity and profits]]"
  - "[[evergreen/cloud-vs-on-prem-vs-hybrid-deployment-options|Cloud vs on-prem vs hybrid deployment options]]"
  - "[[evergreen/cloud-vs-on-prem-is-about-your-application|Cloud vs on-prem is about your application]]"
Tags:
  - Luca
  - Not for HH
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 6ac386d1-c755-44f8-a36f-a7374b7aaf6b
---

# Cloud vs on-premise infrastructure

### 📑 Materials

---

[https://community.refactoring.club/c/tech-strategy/why-we-are-leaving-the-cloud](https://community.refactoring.club/c/tech-strategy/why-we-are-leaving-the-cloud)

[https://world.hey.com/dhh/why-we-re-leaving-the-cloud-654b47e0](https://world.hey.com/dhh/why-we-re-leaving-the-cloud-654b47e0)

[Untitled](https://www.notion.so/657d01767bdc4d71b218c0b3e75bba1d)

### ✍️ Post

---

About a month ago, [Basecamp](https://basecamp.com/) made the decision to move their infrastructure from the cloud (AWS + GCP) back to on premise servers.

[David Heinemeier Hannson](https://twitter.com/dhh), their co-founder, CTO, and chief contrarian tech personality, announced it in a [passionate blog post](https://world.hey.com/dhh/why-we-re-leaving-the-cloud-654b47e0).

Quoting one of the salient passages:

> *We've seen all the cloud has to offer, and tried most of it. It's finally time to conclude: Renting computers [i.e. the cloud] is (mostly) a bad deal for medium-sized companies like ours with stable growth. The savings promised in reduced complexity never materialized. So we're making our plans to leave.*

DHH argues it only makes sense to run your app in the cloud if it belongs to one of two scenarios:

1. **It’s very small** — so you can leverage the free tiers, and the savings on complexity are real.

1. **Traffic is very spiky** — so you save money by using resources that are truly elastic.

Is it really that simple? Is AWS truly some kind of *coup* that has blindfolded us over the last 10 years?

This week I tried to write down some thoughts about whether you should go for cloud services, your own servers, or anything in between.

I will do so by considering three main angles, each with plenty of elements that should affect your choice:

- 🖥️ **Application qualities** — complexity, traffic profile, performance, and data sovereignty.

- 🎽 **Team qualities **— skills and organization structure.

- 💼 **Business qualities **— strategy, margins, and risk.

This article draws from my own experience, extensive research, and chats with some of the best infrastructure experts I know.

Most notably, I sat down with [Daniele](https://www.linkedin.com/in/daniele-salvatore-5b342452/?originalSubdomain=it) and [Francesco](https://furio.me/), who respectively lead the cloud efforts at [FAO](https://fao.org/) and [WFP](https://www.wfp.org/). They work in teams of hundreds of people and manage infrastructure deployed worldwide and serving millions of customers.

Let’s dive in! 👇

---

### 🚢 **Deployment options**

We started with the Basecamp story, but the truth is there are plenty of case studies on the internet about choosing cloud vs on-prem infrastructure.

However, I have found that most assume this is a simple binary choice, where you either go 100% cloud native, or you buy a noisy server and keep it in your closet.

Reality is, of course, more nuanced than that.

When it comes to infrastructure, you have to manage two main things:

- 🔋 **Physical infrastructure **— machines, networking, electricity, and everything that exists in the physical world.

- ✨ **Virtual infrastructure **— virtualization, provisioning, and all lifecycle operations.

So, what options do you have to handle these?

#### 🔋 Physical infrastructure

Three main options here:

- **Fully owned** — you run your own servers in your own datacenter (or closet!).

- **Co-location** **/ Housing **— you run your own servers in someone else’s datacenter.

- **Cloud **— you use servers owned by a cloud provider, in their own datacenter.

These options have ascending nominal cost and descending maintenance effort. 

So, based on how effective you can be at handling maintenance you may or may not save money on any of the first two vs the full cloud.

It should be said, however, that for 99% of companies, running physical servers on their own is totally out of question. Handling electricity, networking, cooling, security, etc. is no joke — you probably don’t have and don’t want to build this kind of specialty on your team.

So, when people say they are “leaving the cloud”, most of the time they are talking of co-location.

#### ✨ Virtual infrastructure

Virtual infrastructure is what you put on top of the bare metal to handle provisioning and virtualization. You have three main options here as well:

- **Fully owned **— with your own servers you have full control and you can use software like VMWare, Red Hat, Oracle.

- **Cloud **— if you run on a major cloud provider, you transparently use their own system. They handle everything for you.

- **Hybrid** — it is little known but you can run (parts) of the virtualization stack of major cloud providers on your own servers. E.g. with [AWS Outposts](https://aws.amazon.com/outposts/?nc1=h_ls), a physical server of yours can run the AWS control plane, and you see it as a Zone on your AWS console. Kind of similarly, with [Google Anthos](https://cloud.google.com/anthos) you can run K8s clusters on a server of yours and manage them from your GCP console alongside your other GCP services.

![image](../assets/a52810b4c2964a4c.webp)

So, how do you choose between all these options? Let’s start with your application.

### 🖥️ **Application**

Qualities and requirements of your application make for a big chunk of what you should take into account for choosing the right infrastructure approach. Let’s see a few elements.

#### Complexity

Complexity is about your system design. 

Simply put, the higher the complexity of your design, the better cloud solutions look, because you can leverage their managed services — like, running your queues on SQS, or storage on S3.

Cloud services are specialized and play nicely together. In the classic tradeoff between cost and ease of use/maintenance, managed services present the most compelling arguments vs if you just rented servers on the cloud. Daniele explained this well 👇

> *The worst error you can make is to consider the cloud environment simply as a remote datacenter, moving your product on EC2s as if they were bare metal servers. Cost comparison between the on-prem and the cloud would always be in favor of the former*.

#### Traffic

Traffic by itself may not be incredibly hard to manage. While traffic naturally leads to more complexity, the *amount* of load is not conclusive on how much work it brings, or whether on-prem is better or worse than cloud.

This tradeoff instead depends more on how your traffic *changes *over time.

- **Growth** — how much your traffic changes in the **mid/long term**.

- **Spikiness **— how much your traffic changes in the **short term**.

The cloud tradeoff here is about elasticity. Cloud resources are naturally more elastic than on-premise ones, both in the short and long term.

- In the short term you benefit from reactivity and auto-scaling. 

- In the long term you benefit from being able to reconfigure your system more easily than if you had committed on a specific set of machines you own.

#### Performance

Performance needs may also affect your infrastructure choices.

You can meet low response times with any infra setup, but you probably need the cloud if your audience is *also* widely distributed geographically.

Truth to be said, though, most applications don’t have this problem. Chances are your performance constraints aren’t so strict, and you can meet them with any setup, plus maybe a CDN on top.

#### Data Sovereignty

Finally, you may have legal and compliance constraints about where your data lives. Data may need to live in specific countries, and/or you may need to exhibit various degrees of ownership.

Such constraints may limit what services you are able to use, and impact your choices.

### 🎽 **Team**

Much of the cloud vs on-premise tradeoff is about trading lower costs for lower maintenance — or vice versa.

Maintenance effort, though, pretty much depends on the **skills** you have on your team. Francesco told me this story 👇

> *Years ago my team used to manage job queues via simple queue brokers written in Python. These would constantly break, because of load and because they were inherently fragile.

At some point we found one guy who was a RabbitMQ expert, and he set up a cluster for the whole team. Things got instantly better.

It was also cheaper than using AWS SQS, but, in hindsight, we could only pull it off because we had specialized skill within the team. The SQS cost hides the cost of the specialist who would otherwise set up and maintain the cluster.*

This skill angle isn’t just about *current* skills — it is also about the future. Whether or not you have experts in this or that *right now*, what are the skills you want to maintain over time in your team?

The RabbitMQ cluster might look convenient now that the expertise seems to come *for free*, but once you invest in the tech, you will also need to *maintain* such knowledge in the future. That means staying up to date with new developments and possibly training new folks to contribute on maintenance and for general resilience.

Again, this might be the right call! But it needs to be an intentional investment, reserved to areas that are strategic to your business.

Speaking of business 👇

### 💼 **Business**

In the end, this cloud debate is subject to the classic rules of *buy vs build*. Rule of thumb is you should build whatever is strategic to your business and can turn into a core competitive advantage, and buy everything else, whenever you are able to.

So when is it that infrastructure is strategic? Whenever it plays a decisive role in preserving important qualities of the business. Among them, two crucial ones are **profits** and **velocity**.

#### 💸 Profits

In high volume + low margin businesses, infrastructure may considerably eat into profits. Think of cloud storage, like Dropbox, or ad-supported businesses, like social networks.

We tend to think that whenever you have high volumes you are better off owning your infra, but that’s not necessarily true. It is only true if you have low margins as well. 

Netflix has more traffic than Twitter, but the former runs on AWS, while the latter runs its own datacenter. That’s because of margins.

#### ⚡ Velocity

In startups and high-growth businesses you need the agility to steer the ship fast to meet ever changing requirements.

There is no way around the fact that owning your infra makes you less flexible than staying on the cloud. Again, your mileage may vary based on your team and skills, but whenever you need to spin new instances, resize existing ones, or sett up a managed service, you are going to be faster on the cloud.

#### 🔒 Lock-in

A popular argument in favor of on-premise setups (or multi-cloud!) is to you avoid locking yourself in with a specific cloud provider.

Honestly, I think the risk here is very low. Even more, this is one example where locking yourself in a single cloud provider can *strategically* pay off, because you benefit from all the services playing nicely with each other.

Vice versa, if you create *abstractions* on top of things to prevent lock-in, then you are stuck with the lowest common denominator among the various implementations. Is it worth it? Well, if you are using a sketchy library you are not sure it will be maintained for long, maybe yes — but if you are using Amazon / Google / Microsoft services adopted by tens of thousands of businesses? I don’t think so.

### 🏅 Ethical stance

Finally, in the Basecamp article, DHH also makes an ethical stance about centralization. Namely, that the internet should be decentralized, so we should avoid making a small handful of players handle most of its traffic.

Whether or not we should root for a decentralized Internet (I believe we should), I am not sure declaring war to cloud providers actually achieves that.

The way I see it is that stuff becomes centralized because that’s just how tech businesses work.

Tech is ruled by power laws and economies of scale, so you have dominant players in every layer of the stack. So yes, AWS controls 33% of cloud infrastructure, but also:

- Cisco sells 40% of all routers

- Intel sells 60% of all CPUs

- Google Chrome is used by 65% of users

And the list goes on.

To me, the only way to fight this is to build superior products that make customers switch because they are *genuinely* better. 

Vice versa, advocating for using something that is *worse* for your business just because it is the right (?) thing to do, it’s probably not going to work.

### 📌 Bottom line

Today, hosting your service in the cloud is the right choice for the vast majority of businesses.

With this I am not saying Basecamp made the wrong call — in fact, I suspect it was the right one. But Basecamp lives in a very peculiar world: 

- The application changes slowly and is 15+ years old.

- Growth is steady and predictable.

- Traffic is not spiky.

- Performance is not a (big) issue.

- They have infrastructure experts already in the team (by DHH’s own admission).

In my experience, most companies have trouble displaying even two or three out of these five qualities.

So, if anything, we should not rush into generalizing case studies, but rather use them to reflect  on our own scenario, and figure out what applies and what not.

[https://refactoring.fm/p/cloud-vs-on-premise](https://refactoring.fm/p/cloud-vs-on-premise)
