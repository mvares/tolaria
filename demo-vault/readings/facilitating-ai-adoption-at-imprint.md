---
aliases:
  - "Facilitating AI Adoption at Imprint"
"Related to": "[[readings-digest/weekly-digest-5|Weekly Digest #5]]"
"Reading time": 10 min
Summary: The author led internal AI (LLM and agent) adoption at Imprint, focusing on practical tools, prompt centralization, and platform standards. Success required close partnership with teams, not just building a platform, and emphasis on measuring adoption and learning quickly. The goal is real productivity gains across the company, not just the appearance of using AI.
"Discarded for digest?": false
"Note Status": Saved
URL: "https://lethain.com/company-ai-adoption/"
Author: lethain.com
Category: Articles
"Full Title": Facilitating AI Adoption at Imprint
Highlights: 35
"Last Synced": 2025-12-11
"Last Highlighted": 2025-12-11
notion_id: 2c6bdf02-815c-8100-bac9-fdd416c48562
---

# Facilitating AI Adoption at Imprint

Prework: building my intuition ([View Highlight](https://read.readwise.io/read/01kc66k69r7a49zfd3ftzse6xc))

After a modest amount of debate, the pillars we landed on were: ([View Highlight](https://read.readwise.io/read/01kc66p3qggmk0848v98eww3kt))

- **Pave the path to adoption** by removing obstacles to adoption, especially things like having to explicitly request access to tooling. ([View Highlight](https://read.readwise.io/read/01kc66pgderm99q7mmyya5cpmz))

- **Opportunity for adoption is everywhere**, rather than being isolated to engineering, customer service, or what not. To become a company that widely benefits from AI, we need to be solving the problem of adoption across all teams. ([View Highlight](https://read.readwise.io/read/01kc66q63pg4kwv3g4z5rp73qw))

- **Senior leadership leads from the front** to ensure what we’re doing is genuinely useful, rather than getting caught up in what we’re measuring. ([View Highlight](https://read.readwise.io/read/01kc66qa3j3hhzzmqctmr0mtrf))

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/631d83ff-20ce-4401-a614-56e2c0f97767/f0a6e37f-21c0-4bb6-bea1-b98d1eb31d68/CleanShot_2025-12-11_at_08.57.502x.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGBDNAJJ%2F20260131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260131T185256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH6hu4nMMDjuFNUXuMmPGeqHisterdCJnWxguHfrAJWaAiEAp665RvP4Gua6MGG3tK2gOnzOTcpKts0N%2FjxiDp9HhNEqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHT5auTNHEp6owzQRCrcA0nWe0YVgB%2Fg3eRpxPj%2F6VgCd0bE65lBHobtgOW94RyYamE1xw2MyLQJ3vMV%2FKJ9QkfM5ISr0YfJ5sVwcZD88yC0PWLa9fVPr2LMJ5W3xhTLCVPfg1G8YY4WF0YMRvEHPeKNTgq5S9UG5yofHfRIJ%2F716iR1faJCa4k%2BYpWUCidagQohxjKiXqZhSjMCETDe9lsuIupkqa4IMzAuttGtZye5rjubrdIjvifSrH2j0g2aNBLRJ3o1yejS6p8qb3dNk6Hk8Ef4oOZWfX7cHctRvkDQEPWveIHwNXqOeGNJo%2B6U6RwCFxkC1eNgocqwSB6NYwH2x%2Fkt8Hu2WPVIKXFBppSUTLemkrI8L%2F%2Fb%2FIqvVq8UHaUhI%2FltMqsuoa5UB0oLHGFo0j184gr5Uifep8g%2BxDbOYz82Ih%2BUVI5BAvuxkFrrpAxFitPpExuMMnRfbLnHDWkV7K2N%2FUiKsC%2FkmZrQGz9ZShPTmGCg93SJOa6cC%2F3U7ZykOlczLJZc1xxnyBqcWb0d%2FPcCwIcuxlh46e35NeKCPgaRzjUbBfhjx0u5LXGXYnm9GF%2Fcf4FSoTp7Pn3lEuZiGWF7kanmqa5UhhAyx%2BUJAJ3agVuEpdnaQ%2F176tjZ1X5f6sZ%2FPCymRAjBMMqN%2BcsGOqUBS8bDpNtwr0SsPEjQv3n894iMkTcy%2Bh6Xwhvc5ZDhbgKBxRKhgK7ipcaawXcXJphL3SeiCLiQ47mmSjiFoL1fePUHeIKzf6lbVu6Kw%2FqZkGmRHanmqU4xzfAWdxaD9YI1sLPuLvHLu60Fo44bsEFwNfGDZQx7wcLjAe9P%2FqtNOqCNx8hWxmlL4qLMm773gwDfUjj9w0nUmzV%2B3IhJf2yYEx3BQAk2&X-Amz-Signature=7b3ac696fdfc3f0c7eb4c53af3ffc1bc1b6f88101289b87d72c40f973dbe0118&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Documenting tips & tricks ([View Highlight](https://read.readwise.io/read/01kc66rmyep2pebzz0sb0pcmas))

My first step towards adoption was collecting as many internal examples of tips and tricks as possible into a single Notion database ([View Highlight](https://read.readwise.io/read/01kc66rqpsfrd3khgqddmw85jy))

making prompts discoverable within the company is extremely valuable ([View Highlight](https://read.readwise.io/read/01kc66sxn12m1wbj41shvjj7xy))

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/631d83ff-20ce-4401-a614-56e2c0f97767/5afae9ef-7f71-41ea-ad11-0f9eda7a7579/CleanShot_2025-12-11_at_09.02.342x.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGBDNAJJ%2F20260131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260131T185256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH6hu4nMMDjuFNUXuMmPGeqHisterdCJnWxguHfrAJWaAiEAp665RvP4Gua6MGG3tK2gOnzOTcpKts0N%2FjxiDp9HhNEqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHT5auTNHEp6owzQRCrcA0nWe0YVgB%2Fg3eRpxPj%2F6VgCd0bE65lBHobtgOW94RyYamE1xw2MyLQJ3vMV%2FKJ9QkfM5ISr0YfJ5sVwcZD88yC0PWLa9fVPr2LMJ5W3xhTLCVPfg1G8YY4WF0YMRvEHPeKNTgq5S9UG5yofHfRIJ%2F716iR1faJCa4k%2BYpWUCidagQohxjKiXqZhSjMCETDe9lsuIupkqa4IMzAuttGtZye5rjubrdIjvifSrH2j0g2aNBLRJ3o1yejS6p8qb3dNk6Hk8Ef4oOZWfX7cHctRvkDQEPWveIHwNXqOeGNJo%2B6U6RwCFxkC1eNgocqwSB6NYwH2x%2Fkt8Hu2WPVIKXFBppSUTLemkrI8L%2F%2Fb%2FIqvVq8UHaUhI%2FltMqsuoa5UB0oLHGFo0j184gr5Uifep8g%2BxDbOYz82Ih%2BUVI5BAvuxkFrrpAxFitPpExuMMnRfbLnHDWkV7K2N%2FUiKsC%2FkmZrQGz9ZShPTmGCg93SJOa6cC%2F3U7ZykOlczLJZc1xxnyBqcWb0d%2FPcCwIcuxlh46e35NeKCPgaRzjUbBfhjx0u5LXGXYnm9GF%2Fcf4FSoTp7Pn3lEuZiGWF7kanmqa5UhhAyx%2BUJAJ3agVuEpdnaQ%2F176tjZ1X5f6sZ%2FPCymRAjBMMqN%2BcsGOqUBS8bDpNtwr0SsPEjQv3n894iMkTcy%2Bh6Xwhvc5ZDhbgKBxRKhgK7ipcaawXcXJphL3SeiCLiQ47mmSjiFoL1fePUHeIKzf6lbVu6Kw%2FqZkGmRHanmqU4xzfAWdxaD9YI1sLPuLvHLu60Fo44bsEFwNfGDZQx7wcLjAe9P%2FqtNOqCNx8hWxmlL4qLMm773gwDfUjj9w0nUmzV%2B3IhJf2yYEx3BQAk2&X-Amz-Signature=827901eba010bf35680e917b4a75778ad940769be2f6851b4465a0017bc6ed2d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Discoverability solves four distinct problems: ([View Highlight](https://read.readwise.io/read/01kc66vs6tgk46rtxg7822kf0b))

Creating visibility into what prompt’s can do (so others can be inspired to use them in similar scenarios). For example, that you can use our agents to comment on a Notion doc when it’s created, respond in Slack channels effectively, triage Jira tickets, etc ([View Highlight](https://read.readwise.io/read/01kc66w056my7mfctp0q4a5azk))

Showing what a good prompt looks like (so others can improve their prompts). ([View Highlight](https://read.readwise.io/read/01kc66w6hg50fgjy8aa8n9p1pt))

Serving as a repository of copy-able sections to reuse across prompts. For example, you can copy one of our existing “Jira-issue triaging prompts” to start triaging a new Jira project ([View Highlight](https://read.readwise.io/read/01kc66we3y4jm4sdzf429tw237))

Prompts are joint property of a team or function, not the immutable construct of one person. For example, anyone on our Helpdesk team can improve the prompt responding to Helpdesk requests, not just one person with access to the prompt, and it’s not locked behind being comfortable with Git or Github ([View Highlight](https://read.readwise.io/read/01kc66wzwapjy6mekb8qehe7gy))

Identifying repeating prompt sub-components that imply missing or hard to use tools. ([View Highlight](https://read.readwise.io/read/01kc66xgeb47cc9rkm88jmxz3v))

My core approach is that *every* agent’s prompt is stored in a single Notion database which is readable by everyone in the company. *Most* prompts are editable by everyone, but some have editing restrictions. ([View Highlight](https://read.readwise.io/read/01kc66xrwhkc3x8w0nt8jyn44y))

Pretty much all prompts end with an instruction to include a link to the prompt in the generated message. ([View Highlight](https://read.readwise.io/read/01kc66zraj5a9xyqe9jah1nec5))

Adopting standard platform ([View Highlight](https://read.readwise.io/read/01kc670803w0c66f5hpj0sxnwk))

In addition to collecting tips and prompts, the next obvious step for AI adoption is identifying a standard AI platform to be used within the company, e.g. ChatGPT, Claude, Gemini or what not. ([View Highlight](https://read.readwise.io/read/01kc671b0tm0rvbha6c74cfvjw))

Metrics ([View Highlight](https://read.readwise.io/read/01kc671y6vxfmqkqbcrgbbrgdr))

Altogether, I’ve found measuring tool adoption very useful for identifying the right questions to ask. Why *haven’t* you used Cursor? Or Claude Code? Or whatever? These are fascinating questions to dig into ([View Highlight](https://read.readwise.io/read/01kc672fyk94hsyqg9f4qmqqbg))

I try to look at usage data at least once a month, with a particular focus on two questions:
1. For power adopters, what are they actually doing? Why do they find it useful?
2. For low or non-adopters, why aren’t they using the tooling? How could we help solve that for them? ([View Highlight](https://read.readwise.io/read/01kc672sm139ybtcdz8k6011n0))


What’s really worked is the intersection of platform engineering and old-fashioned product engineering:
1. (product eng) find a workflow with a lot of challenges or potential impact
2. (product eng) work closely with domain experts to get the first version working
3. (platform eng) ensure that working solution is extensible by the team using it
4. (both) monitor adoption as indicator of problem-solution fit, or lack thereof ([View Highlight](https://read.readwise.io/read/01kc674paevavcp7jjwtq8zhnp))


For all of these projects that have worked, the formula has been the opposite of “build a platform and they will come.” Instead it’s required deep partnership from folks with experience building AI agents and using AI tooling to make progress. ([View Highlight](https://read.readwise.io/read/01kc675ccxy720h4awdyr8a707))

Resolving foreign keys ([View Highlight](https://read.readwise.io/read/01kc677vtsarxcer9jyqqvwfha))

one thing that has in practice really interfered with easily writing effective prompts is making it easy to write things like `@Will Larson` which is then translated into `<@U12345>` or whatever the appropriate Slack identifier is for a given user, channel, or user group. The same problem exists for Jira groups, Notion pages and databases, and so on. ([View Highlight](https://read.readwise.io/read/01kc6786t5ybter71vmmsanv8g))

Formatting ([View Highlight](https://read.readwise.io/read/01kc679sp30h5rdyg8fx8059qz))

Slack’s `mrkdwn variant of Markdown`

Logging and debugging ([View Highlight](https://read.readwise.io/read/01kc67ac2szqe3xxe8xavqmzff))

Today, all logs, especially tool usage, are fed into two places. First, it goes into Datadog for full logging visibility. Second, and perhaps more usefully for non-engineers, they feed into a Slack channel, `#ai-logs` which create visibility into which tools are used and with which (potentially truncated) parameters. ([View Highlight](https://read.readwise.io/read/01kc67akhk7y9tvsp8kszec2nz))

The biggest internal opportunity that I see today is figuring out how to get non-engineers an experience equivalent to running Claude Code locally with all their favorite MCP servers plugged in ([View Highlight](https://read.readwise.io/read/01kc67bnfye8s0ehv225tktqz5))

What’s next? ([View Highlight](https://read.readwise.io/read/01kc67c0cgsnddkt7pbe63n575))

focusing on rate of learning is more valuable than anything else ([View Highlight](https://read.readwise.io/read/01kc67c81jtz5pq1tfss379wd7))

If you want to lead an internal AI initiative, you simply *must* be using the tools, and *not* just ChatGPT, but building your own tool-using agent using only an LLM API ([View Highlight](https://read.readwise.io/read/01kc67ch259rrd590pw8zp337y))

*real* AI adoption on *real* problems is a complex blend of: domain context on the problem, domain experience with AI tooling, and old-fashioned IT issues ([View Highlight](https://read.readwise.io/read/01kc67cxffh0p942hmjm53295v))

deeply skeptical of any initiative for internal AI adoption that doesn’t anchor on all three of those ([View Highlight](https://read.readwise.io/read/01kc67d1jvf47ghfxkczb2zfq8))
