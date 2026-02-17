---
aliases:
  - "Web3 applications run on five layers"
"Is A":
  - Evergreen
Tags:
  - Has Pic
  - Not for Monday
"Created at": "2024-04-18T14:44:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to":
  - "[[essay/web3-engineering-part-2|Web3 Engineering (Part 2)]]"
  - "[[monday-ideas/monday-86|Monday #86]]"
"Old Created At": "2022-01-14T16:00:00.000+01:00"
"Updated at": "2025-07-07T09:25:00.000Z"
Status: Not started
Tweet: "Web3 applications are built on five key layers: Protocol, Infrastructure, Platform, Contract, and Application. As we navigate this evolving landscape, how do we ensure we balance decentralization with the convenience of services that may inadvertently centralize control? Let's discuss the implications for scalability and privacy in our architecture choices. #Web3 #TechLeadership"
notion_id: 65352d42-7c08-46f9-9714-bcb2efd84ba6
---

# Web3 applications run on five layers

The architecture of web3 applications can be organized in five main layers:

1. **Protocol Layer**

1. **Infrastructure Layer**

1. **Platform Layer**

1. **Contract Layer**

1. **Application Layer**

This is just one of the possible ways to represent web3 stacks. There exist many alternative definitions which are equally valid. This one is useful to be able to draw a comparison with the regular *web2 *stack.

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/631d83ff-20ce-4401-a614-56e2c0f97767/0ac781f3-75fd-4a2c-aac7-4311cf7644ac/CleanShot_2022-01-12_at_18.15.342x.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ZPAHXXP%2F20260131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260131T190235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDDv88PNn2LM3UwvcL0qB2eKS8HDyPI3o2JGs1k7VnjDAIhALAWit5WehV%2BVfe%2FDJNVnt6HuVtufM4CY5nXJUwp3hTkKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx4ijYvjDia3y1pxlkq3AOD%2FtWxrR6rACKnlLi%2FcB3KD0aCE4BSc%2BqRTjKPIQy1Bh1WIrZoDH%2FBo0CCeBQoFQ%2F4dsIjVwkVb3123nuCUKpbgEuB3W6kFo1vIMRY9%2BHq4e9LcsBKDc3mM2JnaFpWwni5%2FgBJ40i%2BDR13WhEuxXr2xy8eNBiZgJiSH2sD2XWtr%2BoqrF4hJlsykPS3g4A46hqaM77nSTYjOhhyPDC8tkv9WtNgJB2uzZWF3UnA5ilfQtWdXzomNYohy8Ul5VMwY6v4cjNoUrG7aBWxDfq42yDdwDnu7bhfmBTXsDWavOqoQTYWxjxigD7UKGtWoWfYMZvwg%2B%2FvQNVcqAtQ2dj5zjslSZcIXssyNQtepjMgWtOofa%2B9zYVmY13%2FdBOnaTmAU3HANgKoBX%2F0oFBqHCCVUQ0V7NCbbeHi3%2FmwPv1xhOXej7fSucWYDZEbxIP5esu%2Bx6mbmjb4EInNmfeqRyebDgvr%2BgGbHxfT60w8zwArnNdaHgsa51roplf%2BUUcVYxyZobnlnbA2zoJe6JXg9xB%2BZpcSCXzSRVqfrM2kq3L%2BXVY6C0cJFLGGzH9b8BJO7F7e53c0FKAoiA6o1OahpAw2wcxqR0j3BkK%2FE0D6ZyUn9hLcPpwsnz9h6Yisw%2BiEWDDpgfnLBjqkAacBoctSik9gmD4sSSQ0mHxwEZCpp7toK27pHxN5RHrZrAkXpZ356bobU5hlKMkBQHaC0dY%2F5ns%2Bgzlo5uAwAJYzCeCnq7B2VAm6cnP7UmB1YU6H64lBFmMUKDmiP3WoEVlYTR0ZI8Fg9qlF3VoXsp6a8bRr3YeUaggudsAA7JAMw0xqjYL%2F6N8wlDvoNpzqVqoawe%2BU2sQ4l0UVvhQ6y%2FD1oipr&X-Amz-Signature=218d02e52a8c12f101759a60ada47ed0822ecb8d718a7f6007a739f07c0ef15f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Most layers leverage existing technology and build on top of them. Let’s see such layers one by one 👇

#### Protocol Layer

When we talk of protocols for web applications, we usually refer to the ones defined in the [OSI model](https://en.wikipedia.org/wiki/OSI_model) — like IP, TCP, SSL, HTTP. 

Web3 adds blockchain protocols *on top* of those. These new protocols regulate how data is stored and updated across the blockchain, and thus, across applications.

#### Infrastructure Layer

[Untitled](https://www.notion.so/ffba2177fb864b23bed829b7620c88c4)s are run by **Nodes**. Nodes are the basic infrastructure piece of the blockchain.

From an infrastructure perspective, the main difference between a node and a computer running regular software is that each node runs *all* the blockchain. 

This poses obvious scalability concerns, which are being addressed in various ways. For example, Eth2 will introduce [sharding](https://ethereum.org/en/eth2/shard-chains/), while Solana introduced [proof-of-history](https://solana.com/news/proof-of-history).

- The problem is to scale [Untitled](https://www.notion.so/610f8b30ad754ffd84dfff0b53ab234b)s

#### Platform Layer

When it comes to running software, just like people don’t want to run their own servers, they don’t want to run their own nodes. It doesn’t help that nodes need to be quite *beefy* machines.

To solve this pain there are companies that provide “*Nodes as a service*”, the main ones being [Alchemy](https://www.alchemy.com/) and [Infura](https://infura.io/). They provide convenient APIs to access the blockchain (read and write) and allow you to scale while keeping the node layer below completely transparent.

They are the **AWS of web3**.

Their role is also somewhat controversial, as they represent a *centralized* layer on top of the blockchain itself, through which most read and write operations are processed.

This is problematic for at least two reasons:

- **Privacy **— these companies can see each and every request before being routed to actual nodes.

- **Control **— they add an [abstraction layer](https://www.alchemy.com/enhanced-apis) on top of regular blockchain APIs that increases lock-in and obfuscates what is really happening below.

These and other concerns have been voiced by Moxie Marlinspike, the founder of Signal, in a recent blog post. It is a great read:

- 📑 [**My first impressions of web3**](https://moxie.org/2022/01/07/web3-first-impressions.html)

#### Contract Layer

Nodes run virtual machines (EVM in case of Ethereum) on top of which smart contracts run. This layer is about the business logic that affects the *state* of the application, which is stored on the blockchain.

#### Application Layer

Applications who rely on smart contracts are still built with traditional backend / frontend stacks. In fact, most apps today are *mixed* — they manage part of the logic and state on the blockchain, and part on regular centralized databases.

This is to be expected because, as we will see, smart contracts impose rigid workflows that have a serious impact on your development velocity. Whenever you have non-critical logic and data (e.g. analytics, caching) you are better off developing it in a traditional fashion.

To access Ethereum nodes, you can find plenty of libraries that act as a bridge between the web3 and web3 world: 

- 📑 [**Backend API Libraries**](https://ethereum.org/en/developers/docs/apis/backend/)

- 📑 [**Javascript API Libraries**](https://ethereum.org/en/developers/docs/apis/javascript/)
