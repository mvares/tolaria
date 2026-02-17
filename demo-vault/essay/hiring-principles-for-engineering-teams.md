---
aliases:
  - "Hiring Principles for Engineering Teams"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-essays|Publish Essays →]]"
Status: Evergreened
URL: "https://refactoring.fm/p/hiring-principles-for-engineering"
"👓 Status": Not started
"Created time": "2025-02-04T10:49:00.000Z"
Date: 2025-02-19
"Has Notes":
  - "[[evergreen/hire-as-last-resort|Hire as last resort]]"
  - "[[evergreen/hire-junior-engineers|Hire junior engineers]]"
  - "[[evergreen/create-diverse-teams|Create diverse teams]]"
Tags:
  - Essay
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 190bdf02-815c-80b7-adc7-f7e263daf65e
---

# Hiring Principles for Engineering Teams

### 📑 Materials

---

### ✍️ Post

---

Hi everyone! Last week’s [article](https://refactoring.fm/p/in-praise-of-normal-engineers) by Charity Majors is already the most popular Refactoring article of all times. You should check it out if you haven’t already: it’s a fantastic *manifesto* about what it means to create a great team.

One of the topics Charity touched on is *hiring*, which is exactly what we’ll discuss this week. I should rather say this *month*, because—brace yourselves—we are about to dive into a three-part series on what it means to hire well in 2025.

This will be a joint-effort by me, a lot of folks from the community, and my friend Dana Lawson, CTO of Netlify. We are going to cover:

1. **What your hiring strategy should be in 2025** — that’s today’s piece.

1. **How to write a great job post & onboard engineers well** — Dana will jump in on this next week.

1. **How to interview engineers in the age of AI** — a deep article with plenty of examples and real-world stories from people in the community.

But why are we doing this? And why *now*?

There is a famous saying that goes: shipping is your company’s *heartbeat*.* *So, if your company is like a body, with a heart — what is hiring in this picture? To me, hiring is probably nutrition. You bring in elements that contribute to your body’s functioning.

(and sometimes you evacuate them 💩)

Just like with real world nutrition, there are multiple *diets* that lead to different team compositions and sizes, and no real consensus on what’s best. *Trending* diets also changed a lot in recent years, influenced by things like covid, remote, the end of ZIRP, AI, the recent pushback on DEI, and more.

So, how should you *compose* your team today, in 2025?

Often times, things are just confusing: should you hire more engineers? Do you really need them? Seniors or juniors? What about managers? Plus a whole herd of elephants in the room: should you hire more *women*? Is that guy too *old* to fit your team? And more.

I don’t pretend to have a unifying framework about all of this, but I have a small set of ideas that have served me well over time, and I will talk about them today. These are:

1. 🏁** Hire as last resort** — from hiring-first to hiring-last.

1. 🪴 **Make everyone learn** — match everyone’s work to their level of experience.

1. 🎨 **Build diverse teams** — taking the controversy head-on.

Let’s dive in 👇

---

### 🏁 Hiring as last resort

When is it the right time to expand your team? What are the signs? If you search online (or talk to people), you often find conflicting advice:

- **⬅️ You should hire *****early*** — before problems get too big.

- **➡️ You should hire *****late*** — to avoid premature scaling and burning money.

This *dilemma* is high-stakes, for two reasons:

- **Hiring is extremely expensive** — both in terms of compensation money, and time your team needs to spend on the process.

- **Reverting is hard** — firing sucks for everybody, so you want to optimize for doing that as little as possible.

Because of this, I believe in using **hiring as last resort**. Last resort with respect to what? Well, it depends why you are hiring in the first place.

In engineering teams you hire people for one of two reasons (or both): **throughput** or **quality**.

#### 🔍 Hiring for quality

You hire for **quality** when you have a skill gap on something, and it clearly limits growth. Whatever such skill is, before you hire you may ask yourself:

1. **Can you learn it?** — can your engineers acquire that skill? Smart people learn faster than we usually account for, and hiring takes a long time anyway.

1. **Can you build a first version?** — it is rare that you can *only* bring value with top-quality execution, and prototypes are useful to educate your taste and to better understand what you need.

Often times, a combination of (1) and (2) is enough to satisfy (or delay) your need.

#### 📈 Hiring for throughput

You hire for **throughput** when growth is slowed down by pure bandwidth.

In my experience this is trickier to judge than quality, because most factors that slow down your team *do not* get better with size — quite the opposite.

Bad dx, unclear priorities, confusing org structure, are all systemic diseases that you will not solve by throwing more people at them — you will arguably make them worse.

So, counterintuitively, the best time to hire is when your team is in great shape and firing from all cylinders. If that’s not the case right now, you should probably focus on fixing what doesn’t work first.

Finally, increasing headcount has diminishing returns: adding one engineer adds less than one FTE to your dev resources — and the larger your org, the larger this gap. That’s because the** cost of coordination** grows *more than linearly* with respect to your headcount, thanks to [Metcalfe’s Law](https://en.wikipedia.org/wiki/Metcalfe%27s_law) and a bunch of other laws that we don’t need to explain, because I am confident everybody has experienced that empirically in the workplace.

So, when should you hire, instead? This is beyond the scope of this piece, but I wrote more about it here 👇

[https://refactoring.fm/p/when-should-you-hire](https://refactoring.fm/p/when-should-you-hire)

---

### 🪴 Make everyone learn

The second idea is inspired by Charity’s piece, and is about building teams that include engineers from a variety of levels:

> *When people talk about world-class engineering orgs, they often have in mind teams that are top-heavy with staff and principal engineers, or recruiting heavily from the ranks of ex-FAANG employees or top universities.

[Instead] the best engineering teams are the ones where nobody is running on autopilot, banging out a login page for the 300th time — everyone is working on something that challenges them and pushes their boundaries.
*

I am a strong believer in this, because it’s one of the things we got the most right in my previous startup — even though, I admit, kind of by chance. One of my co-founders and myself were ex PhD students and we always kept good ties with our alma mater, so we would often run internships and hire people straight from their [M.Sc](http://m.sc/) or B.Sc. It was the easiest and cheapest way to hire for us, especially in Italy where the tech ecosystem was (and still is) kinda small, and there were few engineer working on our stack (RoR).

However, having fresh engineers in our team brought a ton of benefits that were not always obvious at the beginning:

#### 1) 🔄 Process

A team of senior devs may rely on their own skills to fill the gaps that exist in various procedures — think docs, testing, security, and more.

These areas may become neglected over time as people take them for granted. Everyone knows how things work so there is less pressure to document processes, which in turn makes them degrade over time.

Onboarding young members, instead, requires organizing and explaining everything in a way that is simple and safe.

#### 2) 💸 Cost

Junior devs are obviously cheaper and faster to hire. They also come from predictable channels you can control, like new graduates from universities and bootcamps. So you can plug into these channels and get a steady *deal flow* of candidates.

#### 3) ↔️ Fit

Moreover, these hires can grow into the roles that you actually need to fill. 

Most companies, especially those in the business for some years, have some weird corners that are hard to hire for. Training people about them is usually more effective than looking for someone that exactly matches those requirements.

#### 4) 🪴 Growth

I kept the strongest argument for last, which is growth.

Making people grow is a key driver to make them happier, more productive, and make them stay longer in your company.

Naturally, this is more challenging for Senior devs as—let's be honest—we are not all big tech, where growth is unlimited: in most companies there is a ceiling to what you can learn. Also, in all products there is a variety of work to be done, from the extremely complex, to the extremely mundane.

A team which includes a variety of levels allows you to match people to work that suits their experience, so that everyone does challenging things and is learning most of the time.

This way, in a healthy cycle, Junior devs rise the ranks and compensate for Senior departures, allowing the team to renovate itself at the right pace. Junior devs turned Senior also have a higher chance of success than Senior people hired from outside, because the former already got the trust of their peers and proved to be a good fit over time.

---

### 🎨 Build diverse teams

One of the ugliest trends in our industry in recent years is the pushback on the value of *diversity *in engineering teams.

What’s *diversity* in a team? People immediate think about genders and ethnicities, but it’s about everything, really:

- It’s people from different levels (as discussed above)

- It’s different age groups

- Introverts vs extroverts

- People with kids vs no kids

- Move guys vs tv show guys

Diverse means having people around that are different from you. This is valuable because we all have biases and blind spots — and the more similar we are, the more likely it is that we have the same ones.

In a diverse team, instead, people keep each other in check, and hold each other to higher standards. Higher quality decisions are made, because more points of view are explored.

The most effective argument in favor of diverse teams is not some moral obligation that companies should somewhat match the composition of society — is that diversity makes for better teams, full stop.

So how diverse should your team be?

Your team exists to serve your users, so my rule of thumb, which I stole from Dana, is that you want a team whose composition reflects that of your community of users. Because you create better products by relating to your users. 

Do you serve a global, diverse community of people? The best way to serve their needs is to craft a team that reflects that. Which is just common sense.

---

### 📌 Bottom line

And that’s it for today! Here are a few takeaways:

- 🚀 **Hire as a last resort** — address systemic issues in your team before adding headcount

- 🔄 **Balance team composition** — Mix junior and senior roles to improve processes, manage costs, and create growth opportunities

- 💼 **Match work to experience** — Ensure everyone is challenged and learning, regardless of their level.

- 🎨 **Embrace diversity** — build teams that reflect your user base to enhance decision-making and product quality
