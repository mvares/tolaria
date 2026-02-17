---
aliases:
  - "Open source vs AI coding workflow"
"Is A":
  - Evergreen
"Last Tweeted": 2023-03-02
Tags:
  - Has Pic
"Created at": "2024-04-18T14:44:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to":
  - "[[essay/ai-the-future-of-coding|AI & The Future of Coding]]"
  - "[[monday-ideas/monday-38|Monday #38]]"
  - "[[monday-ideas/monday-130|Monday #130]]"
"Old Created At": "2022-12-23T16:23:00.000+01:00"
"Updated at": "2024-11-13T13:51:00.000Z"
Status: Not started
Tweet: "As AI coding tools become mainstream, we must consider their impact on innovation and workflow in software development. Unlike open source, which fosters collaboration and a robust feedback loop, AI-generated code risks duplicating bugs without a way to learn from them. How can we leverage AI while preserving the dynamics that drive our industry forward? Let's discuss. #TechLeadership #AICoding"
notion_id: 683d8e8b-5b7d-4fb7-b9f3-14296caa3e47
---

# Open source vs AI coding workflow

Coding with the help of AI assistants, like ChatGPT or Github Copilot, genuinely feels like the future. 

However, while these tools are undeniably useful, I am kind of concerned about how the software space will evolve in terms of workflow and innovation, as soon as they get mainstream.

Let’s take, for example, the classic open source workflow, and compare it with the emergent AI-fueled one.  

With open source, people can open up issues about bugs and changes. These issues can be seen by everybody, there is little duplication, owners reply, people have a discussion, and so forth. On top of this, fixing a bug once fixes it for all users (granted they will update their version). 

That looks like a good feedback loop to me.

Let’s compare it now to the current state of AI coding.

AI coding is not based on *reusing* the same code, like open source, but on *creating* new code every time. This is like *code duplication* at scale, and poses the same problems. 

If the AI introduces a bug on something, it will do so for all users that request that code. Those users, in turn will *each* have to fix the same bug by themselves.

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/631d83ff-20ce-4401-a614-56e2c0f97767/940f9d35-466a-4581-9ed8-04966f7f922c/CleanShot_2022-12-13_at_12.20.272x.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T275WDPX%2F20260131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260131T190251Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDMbz6t0%2F3KnbmHshKM14kb%2BMZU1kA9gsGfTUJvn8MH9AiEAnvwON5%2FZRWjC8WX4lW%2BhaoCqXuwDFmDSidf11FBhGGoqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOn4uPyVoNEDRAKwjircA5d97CJvydMsgUBMIKQVAwlDD5gVve66LqCKMm48SesyNlHDgP%2BvIQlPSR8kuhg7r29ieiHkFdwkW3AZzK1Cn4i5%2BqrXS7Krd1yXX2D5KS%2FJCP%2Flp%2FYSDtWB7wrAuuZmRUs%2FU7%2FhXMHgkpyAksKQAisXxq84ieFlqKmFTrBRaqn34gUWE9vJoUZDLCHbLqIMT6SzzBeNiPqSBntcfvJgfXMujEQwKHY%2Fzmmre0uxZG9hKOeV464Y9OqP1tG4fOxbJmYXWLXD2bs2bWYFOQrUHLGIJe4IvADHXeyeEOMyGTDexIW6EO%2FR9hSctwcLZows8yuCyv6lZQLKsfmodhcfmZLrEPID0sWdo3n%2BC7NbjvonHc5hEtRb6jQowST6Y7pgDmTt0EpMBckXgkWTXbBK3cBg7IyfvNzO%2BSseMucjT0w6nE7%2FceXPTUPD0EVpxqJ70l1QtjbhbmerRfNRbgSJzv0DpSDywHvPZrrh17IP4Rtyjv0GbMVvYcLnCkRDkGFhQgFS2OTZKKhrsmge9F5R3D8g40%2FIEq5NWnSXAPT5C2%2F2c6YFDLPyJRnrfLTGDaLuYp6TLQ62mEvPEaZsddOX6KuY3%2FrQznuMuYBmpjL1Uq7J%2BEjoSC%2BwuuHqRMTnMOCF%2BcsGOqUBVYV%2BpRUIbGk5ctrGq6RJdcoPXjlgHtkTiXhquts0J1Dl7g2cxAGDAEtw5ZWJR%2FFGsBkEuMcmWnKHucoQFXqDYrsVC%2BqLA9SAdWeK9aMSMoVksPi67CK4QrF2m9Shi3n9bK6NwvrBFpoZHMXRP9xye9nf3KXv3cUbZrCSzc3CC7rkpNMR0fjoKp8GB5r4ZbEF1UlUqHsi3SJZfWzDKNfArjPeeTUJ&X-Amz-Signature=bd69b89ec8c97d4efa04a896b9ac72814b2e4f8f50231c6c8527b6a9fe6bda97&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

What’s worse, right now we have no way of making the AI learn from its mistakes + our corrections. There is no feedback loop.

So, while AI is surely going to provide incredible benefits, it is also going to change some core dynamics that so far have enabled innovation, open source, and much of the software ecosystem as we know it today.

We will have to wrap our heads around this to figure out what is the best, most productive way of using AI, while also making sure we are moving forward as an industry.
