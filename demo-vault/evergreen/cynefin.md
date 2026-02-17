---
aliases:
  - "Cynefin"
"Is A":
  - Evergreen
"Last Tweeted": 2024-04-23
Tags:
  - Has Pic
"Created at": "2024-04-18T14:44:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to":
  - "[[essay/mental-models-for-engineers-and-managers|Mental Models for Engineers and Managers]]"
  - "[[monday-ideas/monday-100|Monday #100]]"
"Old Created At": "2024-03-01T10:23:00.000+01:00"
"Updated at": "2024-09-18T08:44:00.000Z"
Status: Not started
Tweet: "Understanding the Cynefin framework is vital for tech leaders. It categorizes problems into five domains: Clear, Complicated, Complex, Chaotic, and Confused. Each domain requires a distinct approach to decision-making. How are you leveraging this framework to navigate uncertainty in your projects?"
notion_id: efc905ad-8cc6-4ae7-b0b8-ce301cfd6460
---

# Cynefin

Consider the Cynefin framework for decision-making.

It was created by Dave Snowden during his work at IBM in the late 1990s. The term "Cynefin" is a Welsh word meaning “habitat”, and categorizes problems into five domains:

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/631d83ff-20ce-4401-a614-56e2c0f97767/efc0b08b-9c71-4e20-a9d9-7a81285e680a/1089eda7-0fa4-4254-bdcd-223dbde39f68_1642x1446.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46653Z2WCPT%2F20260131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260131T190941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDkdBVaz04eFSCJ9%2BWPM3s26LnCKmtRrqnihnYRCXB7yQIgC8JigYmwQsPhfOMFG9O6KvD92ecRR%2Bez5zDpp1X77QcqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNld%2FFdxnIEHgAC%2BfCrcA4mSitVcCoE31n2ti1OmogUUJHah8PPzInNMj51%2Fj4GvqrhQP3KwO3b9ruF8OWLfDbAMmusrxhmCy6GcvLxNog8O2HLB%2Fv%2BUm4aPwieOZ0eTO677FqwJ2GzFsrseMR2mkQd1Il%2BUbAYA2epdeOHwZ%2FqrgKncHhwPtKzV7BVOarQ14ALGLkPEUrfNBI3eLnqCfpp%2BsQjb1WsNj4m2o%2FvOtLkGce7Ta23fQsTDXZ80wnocbh31Ac8mYP34UxEplgZKalS3yRBYUFcA24WPR0yQzBZ%2BhMakbr7%2B5kVfZj9DNYDvP92zQjXLHg9jRG1InW3hsd0RxrV825zwNmDJbHPZ9Bl0N2dNMutpx0h%2BOMc06je4h1O2FV%2FsvY0w%2BOABHKBPBCjnap3jhzleALzGVNs39%2Btq%2B371X%2FrFpbDgLDSBKqXQ285PqgbGsVKqBCxmmCzMdNCSDzkjaGZCjIJPSSIbntwdmMMU0CyrVcRws3IR81rjWes6sSuQMxEztUc1YMtymkVFSet3%2BQgDkWgGa5A2ypDxTU49Sa128k1uvD7V33IYJAe2D8I8HpIGp1UR8vHmBa0PPeqsuj2kI0LM0xqvowjGM%2B6PpAnl%2BQFHg5pw6ijTqb8jOeKBDIMvFJzDMJeE%2BcsGOqUBIjjvJ2Sf5WjOebJ0X5y%2BHHybBsXutG0koew%2FrJlDB7xderJx%2BBJDATx%2BA2RfuqiRIcViOb68OePDVSsnRNSLXaNfSGjp5O6vigQnE1uOHFPtV%2B0GZyIrhG97rcE8ZsIF07H0%2B5o2Ge1paJ%2BzyKU%2FsNEnAXSVWAi6OWdthJEBYvCeQ9BnCgceeBVsngdlv2f2v8EgeN05urtplOWxpqKRgQEDjihw&X-Amz-Signature=2811a50fcd2663286bbf6b49d6a8d5664d982d36e9e4802e84a56eece9da7e76&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

#### **1) 🟢 Clear**

In this domain, cause-and-effect relationships are clear and predictable. The appropriate approach is to sense the situation, categorize it, and respond based on established best practices.

Example: fixing a known bug, or adding a simple feature.

#### **2) 🟡 Complicated**

Here there may be multiple correct answers, and while there is a clear relationship between cause and effect, it may not be apparent to everyone. Expert analysis or the use of analytical methods is often required.

Example: designing a system with a set of advanced features that require thorough planning.

#### **3) 🔴 Complex**

In this domain, cause-and-effect relationships are only clear in retrospect. The right approach is to 1) *probe* (experiment), 2) *sense* (learn from the experiment), and then 3) *respond*.

This is often the case for innovation and zero-to-one scenarios. For instance, creating a new product needs constant experimentation and feedback from users, which makes it a classic *complex* domain.

#### **4) 🟣 Chaotic**

In chaotic situations, cause-and-effect relationships are unclear and the situation itself is highly unpredictable.

The appropriate approach is to establish order first, then sense where stability is present, and respond to turn the chaotic into the complex.

An example could be responding to a major system outage or security breach.

#### **5) 🔵 Confused**

This is the domain of the unknown, where it is unclear which of the other four domains applies.

The appropriate approach is to break down the situation into constituent parts and assign each to one of the other four domains.

The Cynefin framework is useful because it gives you a blueprint of how to respond to situations, and also an ideal *path* to turn chaos into order.
