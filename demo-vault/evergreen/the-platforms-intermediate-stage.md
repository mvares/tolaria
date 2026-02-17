---
aliases:
  - "The “platforms” intermediate stage"
"Is A":
  - Evergreen
Tags:
  - Has Pic
"Created at": "2024-04-18T14:44:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to":
  - "[[essay/the-three-stages-of-engineering-teams|The Three Stages of Engineering Teams]]"
  - "[[monday-ideas/monday-41|Monday #41]]"
"Old Created At": "2023-01-13T11:55:00.000+01:00"
"Updated at": "2024-04-19T09:37:00.000Z"
Status: Discarded
Tweet: "As teams grow, moving from generalists to specialists is vital. Organizing your engineering team into layers/platforms can enhance communication and skill application. But beware of the pitfalls with Feature Teams—they may hinder product ownership and complicate resource allocation. How do you navigate these challenges? #TechLeadership #EngineeringCulture"
notion_id: ff42b861-db0c-45da-8c09-f536d46ea0ea
---

# The “platforms” intermediate stage

As your team grows, you get to a point where the *generalists* stage breaks, usually for two reasons:

- 📣 **Communication** — in a larger group of people, “everyone does everything” makes it hard to organize work properly.

- 📚 **Skills **—** **technology becomes more complex and it requires specific skills to move forward.

The most natural choice at this stage is to organize your engineering team into layers/platforms based on your tech stack — e.g. Frontend + Backend.

Separating layers helps to build engineering culture and practices, and slowly makes your team shift from generalists to specialists.

[Embed](https://twitter.com/lucaronin/status/1350025856354308096?s=21)

It also allows for an easy chain of reporting where you identify a *lead* for each layer and make them implement the first management behaviors (e.g. 1:1s).

#### Feature Teams

In a team organized by platforms, complex features are delivered by **Feature Teams**. 

These are cross-functional teams assembled with the purpose of delivering a specific feature, and dismantled later.

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/631d83ff-20ce-4401-a614-56e2c0f97767/ed782b04-483f-4320-869b-f1067b6e5aff/CleanShot_2021-07-30_at_08.58.35.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S5KNH6ZY%2F20260131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260131T191027Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCUDWtax7paoV63R4statgDojg1v2RMXGP6o4M1547jUgIgCSkeNzsygm1QGFLLCmV0365QJBnC3rPn90THNK4hbyMqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNbHvh2Uw4Y0cIeDdCrcA8tiV3vCR%2FRYWe1XRVnW0ud5kc5HeYMbvaQBIGjHviwmkafafcwD0X8B7Ml9OldEGhkNkS1f8Qa75ONPXV7ftjCIpCU2a8CaQQ%2FO%2BUeLB8BNiVI1JkOX3ojjmg8SXDOEFBXtNUyBvcj6E3zTEVpnWNw2HND%2BzrPgXxVyEgcMXP3h9yMcYqbNZgxCJ%2FF1v%2BJPza4nXOeoLFCbw3LwUERVnSA%2B99MiJ3XhU%2Fu3Rkc2MSWFZ0BJ41sDHS04rDDTHNibc37dhNZEfH1QdabXMed41weewbKISAPUtijWst4sO7T6zCBXOj%2BImFWoAkTUodhWfS0huxr1FoanOYa23yHfnLNPiNsKgrhe%2B31KCyJNmBuhmpTNCuT%2By4da0Inb1dQ4wKqkKM7wrofFjfxZe%2Fi7%2B2sB4cBS2eCFazBfvUC7BbIzLdPUGxrs5FqWHAYrq3s6isleX%2F8mm6cXcCYOBgwUHjuZadV0IoterQyKClEtLXtRK%2BDNVDEsfwmXiLX5PiVd3i75JHTQcloVYZchYbnacncCnRJYNYgZ6yGbUUJkN9RYTS6wwdrgNCmb9ndsaHc5Yq6WrW7dHWq2uDM9iikDd3xhohK34aJPNqBo4p%2B31vmnEed5D3K35lJ8gpPnMPeD%2BcsGOqUBWOpus%2BwdXbP3tByTRlW9vV7h554s4Syl7FY0eB7gOIDguq8ux%2BZ4IGacE2ouJItOywssNVSzigbKCdDcJ5tNG1vAxlBZHqbjziWt9I9f%2F%2BVfr4lWtzssdrOV2M8LewHmDoIw21JYc16hpjcOzfXV5YuM4OiwvlJhMyY%2FDwJvPeq7eZMN80ZanI%2FP0lseDOrZDy4tmBj8TRIxc8Z%2Fg3kozGGnqbQ7&X-Amz-Signature=1724d3eab75842fa4d43e7875fcdd06d81bfb0cace9dc4b70b7c848a3a340fd0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

My feeling about Feature Teams is they are a **necessary evil **in between the small, “generalists” stage, and the final “products” one where you can assemble durable, independent, cross-functional teams.

Feature Teams have two major pitfalls:

- **Product ownership **— being temporary, teams retain little ownership of what they build. This in turn makes it harder to 1) properly iterate on features and 2) develop product expertise over time.  

- **Resource allocation **— while it is a flexible way to work, it also requires continuous negotiation between stakeholders to define what is the best way to allocate engineers. 

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/631d83ff-20ce-4401-a614-56e2c0f97767/2961d202-4643-4999-beee-f1926db7b627/CleanShot_2021-08-03_at_16.19.402x.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S5KNH6ZY%2F20260131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260131T191027Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCUDWtax7paoV63R4statgDojg1v2RMXGP6o4M1547jUgIgCSkeNzsygm1QGFLLCmV0365QJBnC3rPn90THNK4hbyMqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNbHvh2Uw4Y0cIeDdCrcA8tiV3vCR%2FRYWe1XRVnW0ud5kc5HeYMbvaQBIGjHviwmkafafcwD0X8B7Ml9OldEGhkNkS1f8Qa75ONPXV7ftjCIpCU2a8CaQQ%2FO%2BUeLB8BNiVI1JkOX3ojjmg8SXDOEFBXtNUyBvcj6E3zTEVpnWNw2HND%2BzrPgXxVyEgcMXP3h9yMcYqbNZgxCJ%2FF1v%2BJPza4nXOeoLFCbw3LwUERVnSA%2B99MiJ3XhU%2Fu3Rkc2MSWFZ0BJ41sDHS04rDDTHNibc37dhNZEfH1QdabXMed41weewbKISAPUtijWst4sO7T6zCBXOj%2BImFWoAkTUodhWfS0huxr1FoanOYa23yHfnLNPiNsKgrhe%2B31KCyJNmBuhmpTNCuT%2By4da0Inb1dQ4wKqkKM7wrofFjfxZe%2Fi7%2B2sB4cBS2eCFazBfvUC7BbIzLdPUGxrs5FqWHAYrq3s6isleX%2F8mm6cXcCYOBgwUHjuZadV0IoterQyKClEtLXtRK%2BDNVDEsfwmXiLX5PiVd3i75JHTQcloVYZchYbnacncCnRJYNYgZ6yGbUUJkN9RYTS6wwdrgNCmb9ndsaHc5Yq6WrW7dHWq2uDM9iikDd3xhohK34aJPNqBo4p%2B31vmnEed5D3K35lJ8gpPnMPeD%2BcsGOqUBWOpus%2BwdXbP3tByTRlW9vV7h554s4Syl7FY0eB7gOIDguq8ux%2BZ4IGacE2ouJItOywssNVSzigbKCdDcJ5tNG1vAxlBZHqbjziWt9I9f%2F%2BVfr4lWtzssdrOV2M8LewHmDoIw21JYc16hpjcOzfXV5YuM4OiwvlJhMyY%2FDwJvPeq7eZMN80ZanI%2FP0lseDOrZDy4tmBj8TRIxc8Z%2Fg3kozGGnqbQ7&X-Amz-Signature=4debdc4093e974535bea503ccef3eb3aa7cd3eaf03d2967e0a40b073d664a43e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
