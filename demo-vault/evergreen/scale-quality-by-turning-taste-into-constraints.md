---
aliases:
  - "Scale quality by turning taste into constraints"
"Is A":
  - Evergreen
"Created at": "2025-11-27T11:01:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to": "[[essay/what-an-elite-team-looks-like|What an Elite Team Looks Like]]"
"Updated at": "2025-11-27T11:02:00.000Z"
Status: Not started
notion_id: 2b8bdf02-815c-807d-b096-cf0f940cd81b
---

# Scale quality by turning taste into constraints

To build products you need multiple specialties, or layers: product mgmt, UI/UX design, coding (which you can split again in frontend, backend, …), down to ops (observability, infra, …).

The opposite of a product engineering team is a team where, for each feature, each of these layers is taken care of by a separate specialist, which means that to ship anything meaningful everyone needs to carefully coordinate.

If that’s your case, you can ask yourself: what is *hard* in any of these layers? How can you make it gradually easier?

- *What is hard in Product? What does a PM do?*

- *What is hard in UI / UX design that cannot be accomplished by an engineer?*

- *What is hard about the various tech layers that prevents people from working full-stack?*

- *What is hard in ops that prevents engineers from delivering and owning things in production?*

For anything that is hard, there are two ways to make it easier:

1. **🔄 Create process** — document how choices are made, with procedures.

1. **📏 Create constraints** — physically limit the choices people can make.

It’s a journey: we start by using pure human judgment, then graduate into process, and finally into constraints.

Example: if you need to create a new button, that includes design work. What needs to be figured out? Potentially, a lot of things: margins, padding, corner rounding, colors, states, etc. A simple maturity journey might look like this:

- **Judgment** — the basic level is using your designer’s expert judgment to design the thing, and hand it off to an engineer.

- **Process** — the intermediate level is to write down *rules* for how to do it, so that engineers can follow them without bothering the designer. E.g. corners are always rounded this way, and brand colors are this and that.

- **Constraint** — the expert level is to have a component library with pre-made buttons, so that engineers just use them and can’t physically do wrong.

The design example might look obvious, because it’s already common wisdom to work this way. But you can adopt this mindset for any layer of your work: what’s the version of this for product management? Or for observability? Or for backend?

The trick is getting into the habit of reflecting on how you make decisions, so you can continuously **bottle human judgment into rules and procedures**, and eventually constraints.

When you think about it, this is the essence of engineering: **turning chaos into rules**.

At scale, this means that specific functions should work more and more in **consulting mode**: providing feedback and help on the things that fall outside of the scope of the rules, and constantly improving their respective platforms.

They should not be designed to be in the *blocking* loop of regular operations — that would be a waste of their time, plus a limiting factor for throughput.
