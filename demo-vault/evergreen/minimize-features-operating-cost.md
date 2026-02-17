---
aliases:
  - "Minimize features’ operating cost"
"Is A":
  - Evergreen
"Last Tweeted": 2023-04-20
Tags:
  - Has Pic
"Created at": "2024-04-18T14:44:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to":
  - "[[essay/the-operating-cost-of-new-features|The Operating Cost of New Features]]"
  - "[[monday-ideas/monday-49|Monday #49]]"
"Old Created At": "2023-03-12T17:26:00.000+01:00"
"Updated at": "2024-09-18T08:44:00.000Z"
Status: Not started
Tweet: "Minimizing operating costs is crucial for sustainable tech growth. Good design should focus on lowering both delivery and ongoing costs, but especially the latter, as they compound over time. Let’s discuss strategies to achieve this in our projects. #TechLeadership #CostEfficiency"
notion_id: aa766bf7-9803-4855-9446-afb219736aa8
---

# Minimize features’ operating cost

For each feature, you can roughly divide such costs in two steps:

- **Delivery Costs** — costs you sustain to develop the feature until the first deliverable.

- **Operating Costs** — costs you sustain to maintain and evolve the feature, until...forever! 

If you work in small batches and iterate fast ([which you should](https://refactoring.fm/p/the-four-measures-of-software-delivery)), the line between these two steps is blurred, but the costs follow a predictable distribution nevertheless. They go from being higher before delivery, to being lower over time when your team moves on to new initiatives.

![If you don't plan properly, operating costs are going to kill your team's capacity over time  ](https://prod-files-secure.s3.us-west-2.amazonaws.com/631d83ff-20ce-4401-a614-56e2c0f97767/75faf9c7-1025-49e5-8ae9-98215afbfe74/CleanShot_2021-03-04_at_17.52.442x.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FMW7KJP%2F20260131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260131T190616Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDxTaD956Lf1NYKIOsg1XS31CGdpLxwYjfJDCYl2%2BBGswIgEOaKKDlhoqoWtbkWC2QRkqlYI9rmm0dHtcYRl%2FNNnE8qiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEzU42qN3JErnPxpaSrcA%2FVs3PG36T4j1YF7UZ1UTD%2ByVAY0WbgcSYrQdsyRZnLOLpqnNc074CNHIIj4VfIchgzd%2FnuClB9SMGbYCFu7hggcXEmx%2BUPgLjcC0mJ%2FKOxZ2mBFP4ki633EdkzebrN50Cd8NAiLiXX1AVHcDV59svKv8C6R88%2BkbN9vlssyxGvNQojwVuRLeq0EaIbE7LMk8a7ZvLqPmGNNMhdAQMhe0AssXhGiCv2Q02hxRtM9q6EcDc8i6ir%2FXLrPd37HVloum4cORcXbxQHLhAb3Bb2%2FGg9znvHIoIEVV3gYUnLjjn%2Fcocn2CC0vIJfHwl2lb8OspKbZnGfKK9PnYX2KvfsRYYL5%2FjqMAfnrxswOBLe%2BVoTxKqhZF7GMhbWr8B1vV%2BiQ23nIyaMY7q8rGtEd3Xl%2FirUBmiwfJZbjnRChxUaWRXOfMLgjAR0Z8TKtUDxhB5%2BwWB7%2FwewMnA%2BWa0lxmPQPSy43b6e1iJ2Pw%2F6zTy%2BRk0419a%2Fwvyq3Z64nw5UeSdA3LoLWEotplqKMdWYDlD8gumpQLLpbwJGYYh189jhgtIAdGhCCfW8m3DKQGIIe3HCbFmoHWaooRS9qow6le9FGzY6ovLMDTgX09k1YoJp3Vrm%2Fs6lZpcDnOlpAG6iMMIqK%2BcsGOqUBVi%2BCCP2Ylc5xiJ4tbEsekkbVU9Jp78tdTQQKYm%2Fyg7AUD5%2FJJyf5ahEDnahVvOQ7qDbZAIYnpZer3sZ4%2FZDA7MWfGvD5u9hAUXMC8ru6mR9%2FXBh5OwYULWVedmBC3ZucB9MVTurx5w5IsjjxrHdnGLRt49HvJeR8wuwt3bvnrOT7wjTtjAmgjJSCad8QvEmlVcNOq5IHZIM2imdAp2o3kbRiQvdV&X-Amz-Signature=0b7fc7dc309149f45378873ed773cb4011888ef62955548bf2e5d4fcf682cb24&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

**Good engineering wants to keep such costs low**.

In particular, good design should minimize *both* delivery and operating costs. And I would argue that, out of the two, it's vastly more important to minimize operating costs, as they — in contrast with delivery costs — compound over time with those of other features.
