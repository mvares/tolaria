---
aliases:
  - "Optimize Cycle time — up to a limit"
"Is A":
  - Evergreen
"Last Tweeted": 2024-08-21
Tags:
  - Has Pic
"Created at": "2024-04-18T14:44:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to":
  - "[[buckets/how-to-use-engineering-metrics|How to Use Engineering Metrics]]"
  - "[[monday-ideas/monday-94|Monday #94]]"
"Old Created At": "2023-05-13T16:33:00.000+02:00"
"Updated at": "2024-09-18T08:44:00.000Z"
Status: Not started
Tweet: "CTOs: If you had to focus on one DORA metric, make it Cycle Time. It's objective, easy to understand, and truly actionable. A healthy Cycle Time should be within days, not hours. Optimize but don’t obsess—find the sweet spot for value delivery. Let's talk about your strategies!"
notion_id: fc14ff23-2d43-471f-998c-5a18ad81aa84
---

# Optimize Cycle time — up to a limit

Out of the four DORA metrics, if you had to choose only one to optimize, that would be the *Lead Time for Changes* — which today is more often called **Cycle Time**. 

It is a subset of the overall *Lead Time,* which instead covers the whole cycle from ideation to release.

**Why measuring one instead of the other?**

Lead Time includes *analysis* and *design* phases, with duration varying by initiative. Once broken into deliverables, the delivery process should follow short, predictable *cycles* for better measurement.

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/631d83ff-20ce-4401-a614-56e2c0f97767/31f20f5a-b5a9-4b06-93a5-49120c66199d/dbf3800d-da53-48fc-9d56-6d91dde8ad91_1872x1248.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TBOECPVD%2F20260131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260131T191007Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCIU9SepyBJfTCBG7cnyjt7Sqmu6oAv%2FFjfyU01IuAczAIgEA7gmh9KO7v1ChqsguUO%2F0I6ZvE96ePvF9KfUjM%2F0IcqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPzZ9QP7fXN20th4iircA3fc9JUoCmGrdAzSY6ZQj1vEJL0JG3c9V7gOdWGkpp416utoQ60Zd7Y%2BVc8xxMrYqlCULvo3fQFDFr4P0q3ZX76edpkTit8cZYHAHhmD8lD0VK612yGSCMPk%2FPSUwk1lwdB0uGBByALbsnUM2G98vGRpZnCqed%2FcidTxtEAA72eY2meXiabtzozyjoceT0O4RjhmicEOVvm4qkwBoVtnG14A3pHx9FSCxD1sLfNTBHjRPTUhMR7GUX4G%2FPX1QguDL8CN3b7QOSfvh8PAd5fr3kCdcTA0ICFwjidRR0%2FWUVPcYfd7k3K9gKVnTKjEoFPuNztrIssU%2F7dIUz%2FtUCywVI8uRxyBx%2FxuowjdiqqTOAoo00%2BI1gdRHp3s8mEfFi8joLrYMHacHW3gSlmUKCCWTAu8yIxaroYiMg%2FQclvnobI7d9BpKEkcAB9acq2MPGp8RvANGcsUOjTpCcuuuwglRtcNFY%2FYoRxsmTUjtvyayvimSYmdwpp1xSMu0J2i5RS3jpqJEZ0x2inLEXP9QCY%2BWksxNomVA5gVmPZhoPMcy1IzfmUFZzdtBB77e4eZCkxN4p%2BiwZY2PHwWs3nPUmdGW7UPJclifH7CHoDSJKSbemPDn06Ob2cUMEz2meX%2BMPmK%2BcsGOqUBHQLjlI8Y4992UzGcMmq%2BsO9%2F0g%2BdhXU%2BL5vzc6PXhzGexhNJzbaT1OIw0h3OzFlfdKi14u%2F8yLiaJGuUNuAydsOYZ1kzOludTZ2gyCSN%2FekskbJpp17idG46%2FOBcr7sfpGwTwGSAv6gO07dozMj4pnls6UT2%2Bf5O1CSlO%2B8f3RiSnkQZmZzVoIp%2B%2BBw8nx%2F0vQhW2aj0U1%2BAiwcUPdNOAlx2pT7v&X-Amz-Signature=a4cb6a5854ac4fa6e9a85cb1f23d98c05188f74ea9bbfbbb42c347326ad51a89&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

So, Cycle Time is the most popular engineering metric today — and for good reason. In fact, it possesses all the hallmarks of great KPIs:

- **It's objective**: it doesn't need context to be interpreted, you know exactly what it means.

- **It's easy to understand**: it can be easily discussed and explained to management, as it works like the engineering equivalent of sales cycle and product funnel metrics.

- **It stays relevant as you scale**: it doesn't depend on the size of the team.

- **It's actionable**: it shouldn't fluctuate much. Significant increases usually point to specific problems that can be identified and resolved.

A healthy Cycle Time in real-world scenarios is anything within a few days. Further improvements are fine, but striving for < one day brings diminishing returns.

Breaking down work in small batches is important, but there is kind of an *optimal* batch size — under which you are only pedaling faster without delivering more value.

So it’s ok to optimize Cycle Time, but I wouldn’t obsess on getting it down to *hours*.

---

Out of the four DORA metrics, there is one that stands out.

It's the 𝘓𝘦𝘢𝘥 𝘛𝘪𝘮𝘦 𝘧𝘰𝘳 𝘊𝘩𝘢𝘯𝘨𝘦𝘴 — more commonly known today as 𝗖𝘆𝗰𝗹𝗲 𝗧𝗶𝗺𝗲. Here's why Cycle Time, today, is the rockstar of engineering metrics:

1. 🎯 𝗖𝗬𝗖𝗟𝗘 𝗧𝗜𝗠𝗘 𝗩𝗦 𝗟𝗘𝗔𝗗 𝗧𝗜𝗠𝗘

Cycle Time is a subset of the overall 𝘓𝘦𝘢𝘥 𝘛𝘪𝘮𝘦.

Lead Time includes analysis and design, whose duration can vary based on the initiative. Once broken into deliverables, though, the delivery process should follow short, predictable cycles — hence the Cycle Time.

1. 🏅 𝗪𝗛𝗬 𝗖𝗬𝗖𝗟𝗘 𝗧𝗜𝗠𝗘 𝗠𝗔𝗧𝗧𝗘𝗥𝗦

Cycle Time has all the hallmarks of a great KPI:

↳ Objective — 𝘯𝘰 𝘤𝘰𝘯𝘵𝘦𝘹𝘵 𝘯𝘦𝘦𝘥𝘦𝘥 𝘧𝘰𝘳 𝘪𝘯𝘵𝘦𝘳𝘱𝘳𝘦𝘵𝘢𝘵𝘪𝘰𝘯

↳ Easy to understand — 𝘴𝘪𝘮𝘪𝘭𝘢𝘳 𝘵𝘰 𝘴𝘢𝘭𝘦𝘴 𝘤𝘺𝘤𝘭𝘦 𝘢𝘯𝘥 𝘱𝘳𝘰𝘥𝘶𝘤𝘵 𝘧𝘶𝘯𝘯𝘦𝘭 𝘮𝘦𝘵𝘳𝘪𝘤𝘴

↳ Scalable — 𝘳𝘦𝘮𝘢𝘪𝘯𝘴 𝘳𝘦𝘭𝘦𝘷𝘢𝘯𝘵 𝘳𝘦𝘨𝘢𝘳𝘥𝘭𝘦𝘴𝘴 𝘰𝘧 𝘵𝘦𝘢𝘮 𝘴𝘪𝘻𝘦

↳ Actionable — 𝘴𝘪𝘨𝘯𝘪𝘧𝘪𝘤𝘢𝘯𝘵 𝘤𝘩𝘢𝘯𝘨𝘦𝘴 𝘱𝘰𝘪𝘯𝘵 𝘵𝘰 𝘴𝘱𝘦𝘤𝘪𝘧𝘪𝘤, 𝘳𝘦𝘴𝘰𝘭𝘷𝘢𝘣𝘭𝘦 𝘪𝘴𝘴𝘶𝘦𝘴

1. 🎯 𝗪𝗛𝗔𝗧 𝗧𝗢 𝗔𝗜𝗠 𝗙𝗢𝗥

A healthy Cycle Time in real-world scenarios is anything within a few days. Further improvements are fine, but striving for sub-day cycles brings diminishing returns.

Breaking down work in small batches is important, but there is kind of an optimal batch size — under which you are only pedaling faster, without delivering more value.

So it’s ok to optimize Cycle Time, but I wouldn’t obsess on getting it down to hours.

——

📬 I wrote a full (free!) article about using engineering metrics in your org: [https://refactoring.fm/p/how-to-get-started-with-engineering](https://refactoring.fm/p/how-to-get-started-with-engineering)

♻️ If you found value in these insights, please consider reposting it! It means a lot to me

 
