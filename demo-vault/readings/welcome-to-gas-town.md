---
aliases:
  - "Welcome to Gas Town"
"Related to": "[[readings-digest/weekly-digest-9|Weekly Digest #9]]"
"Reading time": 10 min
Summary: Gas Town is a tool that helps manage many Claude Code agents working together on large projects. It uses a system called Beads and roles like the Deacon and Polecats to keep work organized and moving smoothly. Gas Town focuses on automation, allowing workflows to run mostly on their own while users oversee progress through a tmux interface.
"Discarded for digest?": false
"Note Status": Saved
URL: "https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04"
Author: Steve Yegge
Category: Articles
"Full Title": Welcome to Gas Town
Highlights: 11
"Last Synced": 2026-01-21
"Last Highlighted": 2026-01-21
notion_id: 2efbdf02-815c-8127-9fab-cf48034e12a3
---

# Welcome to Gas Town

“Orchestrators are next!” ([View Highlight](https://read.readwise.io/read/01kffsvk626952vw4bf99dv6nh))

“It will be like kubernetes, but for agents ([View Highlight](https://read.readwise.io/read/01kffsvty4q0tz01fe2s6bpwms))

First, you should locate yourself on the chart. What stage are you in your AI-assisted coding journey?
Stage 1: **Zero or Near-Zero AI:** maybe code completions, sometimes ask Chat questions
Stage 2: **Coding agent in IDE**, permissions turned on. A narrow coding agent in a sidebar asks your permission to run tools.
Stage 3: **Agent in IDE, YOLO mode:** Trust goes up. You turn off permissions, agent gets wider.
Stage 4: **In IDE, wide agent**: Your agent gradually grows to fill the screen. Code is just for diffs.
Stage 5: **CLI, single agent. YOLO**. Diffs scroll by. You may or may not look at them.
Stage 6: **CLI, multi-agent, YOLO**. You regularly use 3 to 5 parallel instances. You are very fast.
Stage 7: **10+ agents**, **hand-managed**. You are starting to push the limits of hand-management.
Stage 8: **Building your own orchestrator**. You are on the frontier, automating your workflow. ([View Highlight](https://read.readwise.io/read/01kffswgsnk94wjqv5j7vvqzcc))

Gas Town is an industrialized coding factory manned by superintelligent robot chimps ([View Highlight](https://read.readwise.io/read/01kffsxdb89spd6qe934yjd6rd))

Working effectively in Gas Town involves committing to vibe coding. ([View Highlight](https://read.readwise.io/read/01kffsya5yf020ng9h8wz7v6fz))

The focus is *throughput*: creation and correction at the speed of thought. ([View Highlight](https://read.readwise.io/read/01kffsy7vvg9qndv02xw0n1s4w))

Work in Gas Town can be chaotic and sloppy ([View Highlight](https://read.readwise.io/read/01kffszmky9fpmy49qtn18xsdz))

You might not be 100% efficient, but you are *flying*. ([View Highlight](https://read.readwise.io/read/01kffszvepbr5d88jj2wmcscj7))

Gas Town is also expensive as hell. You won’t like Gas Town if you ever have to think, even for a moment, about where money comes from. ([View Highlight](https://read.readwise.io/read/01kfft0zpv3jv4p654fsm42ze5))

Gas Town is designed to scale up in three dimensions this year with (1) model cognition, (2) agents becoming more Gas Town-friendly, and (3) Gas Town and Beads making it into the training corpus for frontier models. ([View Highlight](https://read.readwise.io/read/01kfft297hvkwtzj8vzb9vw6v9))

Here are the key players and concepts:
**🏙️The Town:** This is your HQ. Mine is `~/gt`, and all my project rigs go beneath it: gastown, beads, wyvern, efrit, etc.. The town (Go binary `gt`) manages and orchestrates all the workers across all your rigs. You keep it in a separate repo, mostly for the configuration.
**🏗️Rigs**: Each project (git repo) you put under Gas Town management is called a Rig. Some roles (Witness, Polecats, Refinery, Crew) are per-rig, while others (Mayor, Deacon, Dogs) are town-level roles. `gt rig add` and related commands manage your rig within the Gas Town harness. Rigs are easy to add and remove.
**👤The Overseer**: That’s you, Human. The eighth role. I gave you some eye paint in the picture. As the Overseer, you have an identity in the system, and your own inbox, and you can send and receive town mail. You’re the boss, the head honcho, the big cheese.
**🎩The Mayor**: This is the main agent you talk to most of the time. It’s your concierge and chief-of-staff. But if the Mayor is busy, all the other workers are also Claude Code, so they are all very smart and helpful. The Mayor typically kicks off most of your work convoys, and receives notifications when they finish.
**😺Polecats**: Gas Town is a work-swarming engine. Polecats are ephemeral per-rig workers that spin up on demand. Polecats work, often in swarms, to produce Merge Requests (MRs), then hand them off to the Merge Queue (MQ). After the merge they are fully decommissioned, though their names are recycled.
**🏭Refinery**: As soon as you start swarming workers, you run into the Merge Queue (MQ) problem. Your workers get into a monkey knife fight over rebasing/merging and it can get ugly. The baseline can change so much during a swarm that the final workers getting merged are trying to merge against an unrecognizable new head. They may need to completely reimagine their changes and reimplement them. This is the job of the ...

...Refinery: the engineer agent responsible for intelligently merging all changes, one at a time, to main. No work can be lost, though it is allowed to escalate.
**🦉The Witness:** Once you spin up enough polecats, you realize you need an agent just to watch over them and help them get un-stuck. Gas Town’s propulsion (GUPP) is effective, but still a bit flaky right now, and sometimes you will need to go hustle the polecats to get their MRs submitted, and then hustle the Refinery to deal with them. The Witness patrol helps smooth this out so it’s almost perfect for most runs.
**🐺The Deacon**: The deacon is the daemon beacon. It’s named for a Dennis Hopper character from Waterworld that was *inspired* by the character Lord Humungus in the Mad Max universe, making it a crossover. The Deacon is a Patrol Agent: it runs a “patrol” (a well-defined workflow) in a loop. Gas Town has a daemon that pings the Deacon every couple minutes and says, “Do your job.” The Deacon intelligently propagates this DYFJ signal downward to the other town workers, ensuring Gas Town stays working.
**🐶Dogs**: Inspired by Mick Herron’s MI5 “Dogs”, this is the Deacon’s personal crew. Unlike polecats, Dogs are town-level workers. They do things like maintenance (cleaning up stale branches, etc.) and occasional handyman work for the Deacon, such as running plugins. The Deacon’s patrol got so overloaded with responsibilities that it needed helpers, so I added the Dogs. This keeps the Deacon focused completing on its patrol, rather than getting bogged down and stuck on one of the steps. The Deacon slings work to the Dogs and they handle the grungy details.
**🐕Boot the Dog**: There is a special Dog named Boot who is awakened every 5 minutes by the daemon, just to check on the Deacon. That’s its only job. Boot exists because the daemon kept interrupting the Deacon with annoying heartbeats and pep talks, so now the dog gets to hear it. Boot decide...

...s if the Deacon needs a heartbeat, a nudge, a restart, or simply to be left alone, then goes back to sleep.
**👷The Crew**: The Crew, despite being last in the list, are the agents you’ll personally use the most, after the Mayor. The crew are per-Rig coding agents who work for the Overseer (you), and are not managed by the Witness. You choose their names and they have long-lived identities. You can spin up as many as you like. The tmux bindings let you cycle through the crew in a loop for each rig with `C-b n/p`. The Crew are the direct replacements for whatever workflow you used to be using. It’s just a bunch of named claude code instances that can get mail and can sling work around. The crew are great for stuff like design work, where there is a lot of back-and-forth. They’re great. You’ll love your crew. ([View Highlight](https://read.readwise.io/read/01kfft5b6t9bycjhmrw3wnzwvp))
