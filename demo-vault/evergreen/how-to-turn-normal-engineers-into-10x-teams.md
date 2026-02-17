---
aliases:
  - "How to turn normal engineers into 10x teams"
"Is A":
  - Evergreen
Tags:
  - Has Pic
"Created at": "2025-03-11T09:17:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to":
  - "[[essay/in-praise-of-normal-engineers|In Praise of “Normal” Engineers 🔨]]"
  - "[[monday-ideas/monday-152|Monday #152]]"
"Updated at": "2025-04-15T13:32:00.000Z"
Status: Not started
Tweet: "To turn your engineering team into a powerhouse, focus on shortening deploy cycles, simplifying rollbacks, and fostering an inclusive culture. Diverse teams are more resilient, and everyone should be learning and pushing their boundaries. It's time to make engineering productivity everyone's priority. What steps are you taking to build a better team? #TechLeadership #EngineeringExcellence"
notion_id: 1b3bdf02-815c-80b8-8b84-f69c2b15d8cd
---

# How to turn normal engineers into 10x teams

In order to build the kind of sociotechnical systems for software delivery that enable normal engineers to move fast, learn continuously, and deliver great results as a team, you should:

![image](../assets/1b3bdf02815c80d9.webp)

#### **1) **🤏 **Shrink the interval between when you write the code and when the code goes live**

Make it as short as possible; the shorter the better.

I’ve written and given talks about this many, many times. The shorter the interval, the lower the cognitive carrying costs. The faster you can iterate, the better. The more of your brain can go into the product instead of the process of building it.

One of the most powerful things you can do is have a short, fast enough deploy cycle that you can **ship one commit per deploy**. I’ve referred to this as the “*software engineering death spiral*” … when the deploy cycle takes so long that you end up batching together a bunch of engineers’ diffs in every build. The slower it gets, the more you batch up, and the harder it becomes to figure out what happened or roll back. The longer it takes, the more people you need, the higher the coordination costs, and the more slowly everyone moves.

Deploy time is the feedback loop at the heart of the development process. It is almost impossible to overstate the centrality of keeping this short and tight.

#### **2) **↩️ **Make it easy and fast to roll back or recover from mistakes**.

Developers should be able to deploy their own code, figure out if it’s working as intended or not, and if not, roll forward or back swiftly and easily. No muss, no fuss, no thinking involved.

#### **3) **✅ **Make it easy to do the right thing and hard to do the wrong thing.**

Wrap designers and design thinking into all the touch points your engineers have with production systems. 

Use your platform engineering team to think about how to empower people to swiftly make changes and self-serve, but also remember that a lot of times people will be engaging with production late at night or when they’re very stressed, tired, and possibly freaking out. Build guard rails. The fastest way to ship a single line of code should also be the easiest way to ship a single line of code.

#### **4) **🔍 **Invest in instrumentation and observability**.

You’ll never know — not really — what the code you wrote does just by reading it. The only way to be sure is by instrumenting your code and watching real users run it in production. Good, friendly sociotechnical systems invest *heavily* in tools for sense-making.

Being able to visualize your work is what makes engineering abstractions accessible to actual engineers. You shouldn’t have to be a world-class engineer just to debug your own damn code.

#### **5) **🔧 **Devote engineering cycles to internal tooling and enablement.**

If fast, safe deploys, with guard rails, instrumentation, and highly parallelized test suites are “everybody’s job”, they will end up nobody’s job.

Engineering productivity isn’t something you can outsource. Managing the interfaces between your software vendors and your own teams is both a science and an art. Making it look easy and intuitive is really hard. It needs an owner.

#### **6) **🤗 **Build an inclusive culture.**

Growth is the norm, growth is the baseline. People do their best work when they feel a sense of belonging. 

An inclusive culture is one where everyone feels safe to ask questions, explore, and make mistakes; where everyone is held to the same high standard, and given the support and encouragement they need to achieve their goals.

#### **7) **👨‍🎤 **Diverse teams are resilient teams.**

Yeah, a team of super-senior engineers who all share a similar background can move incredibly fast, but a monoculture is fragile. Someone gets sick, someone gets pregnant, you start to grow and you need to integrate people from other backgrounds and the whole team can get derailed — fast. 

When your teams are used to operating with a mix of genders, racial backgrounds, identities, age ranges, family statuses, geographical locations, skill sets, etc — when this is just table stakes, standard operating procedure — you’re better equipped to roll with it when life happens.

#### **8) **🪜 **Assemble engineering teams from a range of levels.**

The best engineering teams aren’t top-heavy with staff engineers and principal engineers.

The best engineering teams are ones where nobody is running on autopilot, banging out a login page for the 300th time — *everyone* is working on something that challenges them** **and pushes their boundaries. 

**Everyone is learning, everyone is teaching**, everyone is pushing their own boundaries and growing. All the time.

By the way — all of that work you put into making your systems resilient, well-designed, and humane is the same work you would need to do to help onboard new engineers, develop junior talent, or let engineers move between teams. It gets used and reused, over and over.
