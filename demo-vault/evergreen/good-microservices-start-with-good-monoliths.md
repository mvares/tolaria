---
aliases:
  - "Good microservices start with good monoliths"
"Is A":
  - Evergreen
"Last Tweeted": 2023-07-05
Tags:
  - Has Pic
"Created at": "2024-04-18T14:44:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to":
  - "[[essay/monolith-vs-microservices|Monolith vs Microservices]]"
  - "[[monday-ideas/monday-26|Monday #26]]"
  - "[[monday-ideas/monday-106|Monday #106]]"
  - "[[monday-ideas/monday-165|Monday #165]]"
"Old Created At": "2022-10-13T18:11:00.000+02:00"
"Updated at": "2025-07-07T09:09:00.000Z"
Status: Not started
Tweet: Good microservices designs stem from solid monoliths. If your current monolith is disorganized, transitioning to microservices won't solve the problem—it'll just create distributed chaos. Focus on modularity and efficient deployment units for a more maintainable system. What’s your take?
notion_id: 5e82f635-9fa0-412c-906e-c1dd4dd0fc7b
---

# Good microservices start with good monoliths

Consider the [Gall's Law](https://en.wikipedia.org/wiki/John_Gall_(author)):

> *A complex system that works is invariably found to have evolved from a simple system that worked. A complex system designed from scratch never works and cannot be patched up to make it work. You have to start over with a working simple system.*

Paraphrasing it, good microservices designs are invariably found to have evolved from good monolithic designs.

Likewise, if your monolith looks like spaghetti, moving to microservices will not magically fix it. Rather, it will turn it into **distributed spaghetti**, making problems worse.

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/631d83ff-20ce-4401-a614-56e2c0f97767/b7b0875b-273a-4356-ac78-745cb8c8fbd0/CleanShot_2022-10-13_at_18.12.022x.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UEFBRS4A%2F20260131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260131T190221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDln9MNTfYpvqhZkB0VBPji86yTcFLwmexBh%2BPz5XTk5gIgOT7tXjhAdaxFLrELdtRn8Hkl83XlSYJfNh8%2BW6bFTXcqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFcUQP87wLsWmpQmCircAyYADjpT8Vw7E2rACUiprbLh%2FiIo9NZDPNaLieSCU4AeP6rCMoe%2FzpEihaVaL64gldStxv1mdCKdbiaO876l8Yu9k%2Ff%2FWQq8RNCFCfjhsJGcucEh8TdlrLhB1gmzPUzsiIDaeDEumOm160hc%2FXkiOLZTeCEhqT2sCLMrHeMRuW6Dgtby0b8znTnLc8bwk0WyrqNNgAnIRXO58wZn5N6u5bmOCiKSkpnMHD6e3BfvRtuOWMtU2jQi6SjwlAIJDlE3AnpLaXmdiNH%2B1yk5k9iVXys4l6OEE5GmDiK0Q%2F6DFTM27CeIIKl31DYwtq%2FHTpGLSa%2FeF1uZTci3LY6J%2F%2FF2QZQ831N%2BCBfX2vuQ3hW0zLrBcFISMGNobtuJrNGqhn62Y1dcXyv43LjNdipLS2dnYXHEM3or0ZqIj6RF6va4o%2BYb2qSoq8uf%2BV5BT5X6x1Y2bTc61Sibr%2BGvjO8pUwCDPH1rwr885uh2ZF9Y5gUb38JZOxWEzDP3%2Fku3lgvBTFCqaLtyBYp%2BpXheV2xNsiLDC1X25fjHnWBAxqWb%2FhIp4xvuTaeHgKqOCwxlcClKIpBmdoW6btaDqUU8h0mXcK1Mh5ttEcNF7dupunWNXrOLKWdQn0xpc97EC2vmPTIIMPKJ%2BcsGOqUBt%2FlXhKvdao0x0E7v%2B9%2Fl3F%2BGFjRmJaoHkagMvuy5Hgyz%2BTPKURN6qw6UQgkOpl%2FJ7VdAXjjTdXEwal84NeQmeMjDct6INqQxe4sQSXb0mWU2G5YwYBjuBIGrg8M87tgdUFQMEM2LX9LAVcfQnY4bzsPHdPctncD0D%2ByfHNs%2FLmzblb9Suz8CLsEdljeFKmYQXoaJAi%2FSkOYjExEIoatAnqPvXNsU&X-Amz-Signature=b183393e5503687084fcf8cce0b2e4fcf9d671c7006211951a86b6f9831e5d77&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

The Shopify case study is enlightening as it considers two main coordinates: *modularity *and *deployment units*.

**1) Modularity** — this is the primary virtue you want to achieve. Most qualities brought by good microservices can also be achieved with a modular monolith. Modularity brings easier coordination, better fault isolation, and generally better maintainability.

**2) Deployment Units** — as a rule of thumb, the more things you need to deploy, the more complex your system becomes. Other things being equal, you want to keep this number low.

---

Consider the Gall's Law:

> A complex system that works is invariably found to have evolved from a simple system that worked. A complex system designed from scratch never works and cannot be patched up to make it work. You have to start over with a working simple system.

Paraphrasing it, good microservices are invariably found to have evolved from good monoliths.

Conversely, if your monolith looks like spaghetti, moving to microservices will not magically fix it. Rather, it will turn it into *distributed spaghetti*, making things worse.

So, when you design a complex system, you can consider two qualities:

1. 🧩 Modularity

1. 🚚 Deployment units

1. 🧩 Modularity

This is the primary virtue you want to achieve.

Most qualities brought by good microservices can also be achieved with a modular monolith.

Modularity brings easier coordination, better fault isolation, and generally better maintainability.

1. 🚚 Deployment units

As a rule of thumb, the more things you need to deploy, the more complex your system becomes.

Other things being equal, you want to keep this number low.
