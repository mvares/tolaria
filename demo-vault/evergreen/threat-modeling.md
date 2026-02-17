---
aliases:
  - "Threat Modeling"
"Is A":
  - Evergreen
"Last Tweeted": 2023-03-26
Tags:
  - Has Pic
"Created at": "2024-04-18T14:44:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to":
  - "[[essay/a-tech-radar-for-2023|A Tech Radar for 2023]]"
  - "[[essay/how-to-write-secure-code|How to Write Secure Code]]"
  - "[[monday-ideas/monday-43|Monday #43]]"
  - "[[monday-ideas/monday-97|Monday #97]]"
  - "[[monday-ideas/monday-153|Monday #153]]"
"Old Created At": "2023-02-16T15:06:00.000+01:00"
"Updated at": "2025-04-22T13:31:00.000Z"
Status: Not started
Tweet: Threat modeling isn't just a one-off task—it's a continuous necessity throughout the entire development lifecycle. The old "security sandwich" approach falls short when specs change. As CTOs, let's prioritize proactive security measures from day one. How are you integrating threat modeling into your workflows?
notion_id: b3e1f50f-bbfb-4641-9439-0bbf7df5fb3f
---

# Threat Modeling

A *threat model *is the description of an application and its environment through security glasses.

Likewise, threat modeling is a family of activities you pursue to identify threats, vulnerabilities, and design countermeasures to prevent or mitigate such threats.

Historically, designing for security has often followed the ***security sandwich**** *approach: you address security during design, and you test things at the end. This *waterfall-ish *approach, though, clashes with reality: specs often change during development, so you end up testing for things that are 1) incomplete, or 2) not relevant anymore.

Good threat modeling should be applied continuously throughout the whole development lifecycle.

You can check the dedicated [OWASP page](https://owasp.org/www-community/Threat_Modeling_Process) for more details about how to perform it, complete with practical examples.

![Example of a threat three with a threat, vulnerabilities, and countermeasures ](https://prod-files-secure.s3.us-west-2.amazonaws.com/631d83ff-20ce-4401-a614-56e2c0f97767/0d5228e6-85be-4cef-8b12-256f9be88e1f/CleanShot_2023-03-08_at_10.50.562x.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKKNPOTN%2F20260131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260131T190645Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHYLcWKGcTUEL4FZELsNoLMvWeELoorKrDH%2FXkjRM78JAiAJriau84E4VpNMcRCKbNqHuHc7%2BaJF60RvcN%2B3J7RdhiqIBAi7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMfGDCC7IK18LTuui8KtwD9HKTxMK8Bv5ROAAIWzz4%2FM0b0kLpOP1E%2FwdU0slDXZROyjXsg2d5NBG8%2FVhe6tNcht1iadNpK2BCRvLPa9%2BzXEa94sjBCdCDd%2FZ%2BM46%2BcH4R8GMUZfNs7RPq6HvwqesESOP5MGZ2Gc2dXlQscCb1rf%2FjGZ7lZ32QZx51z9oo8ihk7xzeac3U7pxXe4GUKq%2BrmJ6OWOm1gmKC6yIA5YAXg0PAUcXB%2FMOmzzBP8ykxYiBLR1xC1ReDn4fUM2fWOD%2B4%2FiwPTh7R1fHSnVDlgU5lbX6LISkM3LoYiiUfAFKnSZ652PNLTRJTLz5o75jmBjS3u81ZRbnAV%2Bd7LBEmGEBZBKtRIlxGH6Ars0s%2F%2FSDfyZ7L0erj2aBTzRQv%2FLkOZypiCi6z31SqNRMT1GrN4bCkzOUGXNbjKi0qzgFANZUrQLzjYrLr2ysuOZSQdd1od4MqSad%2FEUHENKHQja3Egvgk9C539uqWTkCp9f58DZ%2FlDtunrznmWSst2jr0zw9Q3J326a7OxRl3kP9pNwC3QpSj%2FHz3%2Fw6JPsnmlA5BZC2AyWhxMDAjh7e7tpwcuWUUGWrwMa1xJvfkZRLX2Icq%2F9n2cfFW8UO7%2FyyjOEBUg5hn6CIokm99pHXsBCiI3Kswr4z5ywY6pgFe54F8BHe5F5iG7ie7vGSmmkhb0Y%2FTgzXwL68OVqKzo3z7EhMTTzw7h3LV56RBZ2qqDuvd0qAFkdZsEqHiVH99mEgexYvc9jzpRQpVv86FnqCqPeEBB66nC8y0kHayTrYgCCIQxw4JjBV%2Bf8OKoeiRJqupH6aNvTmXnAm7RdGysT5xTItGPdNBVnVmZkVbOL%2BG2cryM2mPpQ9ggZrwWvQThQ6x2iMG&X-Amz-Signature=e06f7bef9423a226f6e9466f1660dad434c5d8fc1dd8bf1b01b8067be7439b3f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
