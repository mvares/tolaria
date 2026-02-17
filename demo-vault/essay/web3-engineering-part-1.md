---
aliases:
  - "Web3 Engineering (Part 1)"
"✏️ Status": Not started
"Belongs to": "[[responsibility/publish-essays|Publish Essays →]]"
Status: Evergreened
URL: "https://refactoring.fm/p/web3-qualities"
"👓 Status": Not started
"Created time": "2024-04-18T14:53:00.000Z"
Date: 2022-01-06
"Has Notes":
  - "[[evergreen/web3-is-composable-and-dependable|Web3 is composable and dependable]]"
  - "[[evergreen/you-dont-need-to-believe-in-crypto-to-be-curious-about-it|You don’t need to “believe” in crypto to be curious about it]]"
  - "[[evergreen/web3-expands-the-business-design-space-not-the-technical-one|Web3 expands the business design space, not the technical one]]"
"🎙️ Status": Not started
"Is A":
  - Newsletter Edition
notion_id: 621fb048-42ce-45ce-930d-3c6c212106ce
---

# Web3 Engineering (Part 1)

### ❓ Question

---

> **What would web engineering in web3 look like?
**I have been struggling to find an answer to the following in simple language: The shift in skills required for web engineers when building applications on web3. With my limited Know-how it seems the requirements are drastically different! If only blockchain developers can do it, will all developers today have to learn to be a blockchain developer? (Unless there is web4 layer which is like web2 was for web1)
– Jasvir

### 📑 Materials

---

- [Untitled](https://www.notion.so/fd093e0829c544a0ba9e040b53019e3c)

[https://www.chris-granger.com/2021/12/09/is-web3-anything/](https://www.chris-granger.com/2021/12/09/is-web3-anything/)

[https://continuations.com/post/671863718643105792/web3crypto-why-bother](https://continuations.com/post/671863718643105792/web3crypto-why-bother)

### ✍️ Post

---

If you are anything like me, you may feel like this year (last year by now) the Web3 / Crypto space exploded, and you have loud friends and peers talking non-stop about it.

I personally know several engineers who work on NFTs / blockchain games / dapps, and many who don’t but are looking at this space with interest and curiosity.

Notoriously, though, crypto has a steep learning curve. Many concepts look impenetrable unless you go down the proverbial rabbit hole and spend a solid amount of hours on them.

In fact, even though I have been aware and curious about this space for many years, I haven’t been able to dig into the tech side of it until recently. Or, more precisely, I tried in the past but couldn’t wrap my head around it.

The reason why I had a hard time is I lacked a proper **mental model **for this space. A general framework that gets the basics right, so that when I want to learn new concepts I can attach them to it with ease.

After months of research (and pain) I think I finally got it right in my head, so I am writing a primer on **web3 engineering. **It will be divided in two parts, with this being the first one. 

This first part is about **qualities **that make web3 engineering interesting and different. I will write my take about why you should look into it, and why it might or might not be here to stay.

The second part will deep dive into the **tech stack** and **development process**. What are the most significant changes in the way you design an app? What shift of skills do you need to work on such apps? As always, this won’t be about a specific technology, but more around methods and practices.

In other words, the first part is about **why**, the second is about **what **and **how**.

I have not the pretence of covering any of these ideas in detail, as it would require hundreds of thousands of words. The goal here is to turn some of your [*unknown unknowns*](https://en.wikipedia.org/wiki/There_are_known_knowns) into—at least—*known unknowns*, so that if you want to study further, you know where to begin with.

Let’s dive in! 👇

### A public database

Quick recap of the basics. A **blockchain** is a public database that is updated and shared across many computers in a network. 

Data is stored in consecutive **blocks**. If you send BTC to a friend, the transaction data needs to be added to a block to be successful. Each block cryptographically references its parent, which means blocks are *chained *together — hence the “blockchain”.

The blockchain is *run *by computers who participate in the network, called **nodes***. *Each node holds the entire blockchain and must *agree* with other nodes upon each new block and the chain as a whole.

To accomplish this agreement, blockchains adopt a distributed **consensus mechanism**, which is typically either [proof-of-work](https://en.wikipedia.org/wiki/Proof_of_work) or [proof-of-stake](https://en.wikipedia.org/wiki/Proof_of_stake).

New blocks are **broadcast to the nodes** in the network, they are **checked and verified**, and the state of the blockchain is updated for everyone. 

Data in previous blocks, because of the chaining, cannot change without changing all subsequent blocks. Therefore, existing blocks are **immutable**, and the whole *database* is very hard to hack because of the distributed consensus.

### And a public computer

Some blockchains—Ethereum being the most popular—allow to store **code** inside blocks. Code is then run by nodes in the network.

This capability turns the blockchain into a **public computer** with peculiar qualities. 

When you hear excited people talking of web3 today, they usually refer to the realm of possibilities which opens up when you run software in a public, immutable computer, and store data in a public, immutable database.

![image](../assets/83e8959aed0c4b96.png)

Why is this interesting? Because the *public* and *immutable* nature of blockchain, when applied to software, gives it new qualities you cannot find when you run it on regular servers:

- Public → **Composable** 🧩

- Immutable → **Dependable **🔒

### 🧩 Composable

More than [99% of software](https://tim.blog/2021/10/28/chris-dixon-naval-ravikant-transcript/#:~:text=99.9%20percent%20of%20the%20code%20in%20the%20world%20is%20open%20source%20software%20that%20runs) that runs on servers today is **open source**.

Open source won because of its **composability**. When you think about it, it allows to solve a problem exactly once for everybody, and allows them to combine that solution with others. This in turn sped up software development in ways that weren’t imaginable.

Software, however, cannot run itself. It needs to be hosted on servers — and these are arguably *private*. This means production software gets controlled by private entities, and, crucially, this includes data — as databases are software themselves.

Private servers, and especially private databases, vastly reduce the potential for composability. APIs are limited to what companies allow people to do, and they are not dependable neither, as they might change in the future.

You can think at Ethereum (and other competing projects) as a reliable protocol that allows and enforces public data and publicly run software. This vastly increases composability* *because it makes it *permissionless*. You can use and contribute to the same database everyone uses, and combine public software at API level (not source code level).

[of course the OSS model has its fair share of problems and it’s far from perfect, especially for maintainers. More]

### 🔒 Dependable

Composability wouldn’t work if the blockchain wasn’t also *dependable*. Being blocks immutable, you are guaranteed that data and software won’t change, or will do so only under conditions that are public and well-known.

This means we have now software that can make **commitments**. It is no mistake that a piece of software that runs on blockchains is called a *smart contract*. It is a contract because it is **binding**.

With regular software, since databases and apps are run under control of some entity, you may consider software dependable if you **trust** such entity to uphold its commitments. With blockchains, instead, these are upheld by software itself.

Why does this matter? At this point this might look like abstract talk, so let’s look for examples.

Most use cases and predictions you hear about look at scenarios where these commitments today are made by some **authority **— e.g.: the government — and tomorrow could be enforced by the blockchain. Like, if you buy a house, your property deed could be stored publicly on the blockchain and you don’t need to trust the government anymore.

In my opinion, these use cases are not the best to demonstrate the value of “trustless software” because, I mean, I already kind of *trust* the government to store my property deed.

What about, instead, use cases where there is no authority, and there is no or little trust?

Chris Granger framed this very well with a great example 👇

> *Let’s say you want to fix up your local neighborhood’s park. You have the time, but doing so will take a few thousand dollars in supplies. You could go to your neighbours and try to raise the money from them, but that requires them to trust you with the donations. [...]

Trust-less commitments give us a different way forward though. You could specify the amount needed and contractually state what is allowed to be done with it as well as contingencies for if those obligations aren’t met. Once submitted, that “contract” will be carried out exactly as specified. It is observable to everyone, debuggable, and non-falsifiable. So as a community we could come together, raise $2k and require that the person who is going to purchase the physical supplies also puts in 2k as collateral. In the event that the community votes that the funds were misused, the person loses their collateral and everyone is made whole again. Now everyone involved needs very little trust in each other.

This isn’t about removing trust, it’s about increasing what you can do at a given level of it. You might already trust your neighbour with a couple hundred dollars - but how about $10,000? [...]

This framing of using ****verified commitments**** to increase what’s safe at a given level of trust becomes particularly interesting when you apply it to the internet. You’d likely have very little trust of arbitrary folks on the web, but this capability lets you take what small amount of trust you do have and do more with it.*

Here is the full article by Chris if you want to learn more:

- 📑** **[**Is Web3...anything?**](https://chris-granger.com/2021/12/09/is-web3-anything/)

Ultimately, these qualities expand the **design space** of software to use cases that couldn’t be addressed before 👇

### 🔨 Technical design space

One recurring critic you hear about blockchains is that there isn’t really anything from a technical standpoint that you cannot do with regular tech.

[Embed](https://twitter.com/chetfaliszek/status/1477382310278221825)

This is...right! You can build pretty much anything with APIs, regular databases and web services. 

Also, when you consider common health metrics of apps and databases, like latency, cost, or throughput, blockchain tech vastly lags behind regular tech, often by orders of magnitude. And while improvements are to be expected, we shouldn’t expect raw performance to surpass or become even on par with centralized tech.

However, while you can **technically** build anything with a “web2” stack, some use cases are just **improbable** business-wise.

In other words, while the technical design space stays the same, it’s the business design space that changes.

### 💼 Business design space

Years ago, a VC passed on my startup because we were too reliant on some external API. It was considered a liability because that functionality was core to our business. They were right. We eventually replaced it with in-house tech that took 6+ months to be built.

If we could *trust *that service to stay public and immutable, the trajectory of our product would have changed dramatically.

The design space of our product had been ultimately limited not by what *could be done* technically, but by what made sense for the business — *because *of the undependable nature of technology.

If we could all use the same database, and combine public apps that we can always trust, what could we build? And how fast?

### 🔮 Do you need to *believe*?

Crypto is a polarizing space that divides people into skeptics and believers. To be curious and wanting to learn more, though, you don’t need to be neither.

F. Scott Fitzgerald wrote: *The test of a first-rate intelligence is the ability to hold two opposing ideas in mind at the same time and still retain the ability to function*.

Personally, my opposing ideas are:

- I love the **qualities** you get with web3 and I am curious about a future where software and services are built this way...

- ...but the current **tech is still lacking** and I feel it may not stand the test of time.

So, even if you believe this is the *right* future to build, the *tech* *stack* might look very different from the one that exists today. If you were excited by the potential of web apps in the early 2000s, you were right! But you would have learned Java applets, just to throw them away a few years later. 

There are counter examples too. HTML and JS have been mocked and considered a bad fit for web apps since forever. Not only they are still here, but they are attacking desktop and mobile too. When adoption surpasses a critical threshold, it becomes more convenient to improve the current tech than replace it entirely.

PICTURE adoption increases → improvement vs replacement

I don’t know what stage we are in with crypto, and I don’t know if Bitcoin or Ethereum or Solana are here to stay or they will be replaced by 10x better tech in a few years. But to me it feels the right time to dip your toes in the water. Or, if you feel like it, get full wet.

### 📚 Resources

There are close to infinite opinion pieces on web3. These are the ones that shaped my thinking the most and that I really think you should read:

- 📑** **[**Is Web3...anything?**](https://chris-granger.com/2021/12/09/is-web3-anything/)** **— Chris Granger talks of software-based commitments and removing trust.

- 📑 [**Web3/Crypto: Why Bother?**](https://continuations.com/post/671863718643105792/web3crypto-why-bother)** **— Albert Wenger talks of why permissionless data matters, and how the lack of it shaped the current web as we know it.

- 📑** **[**The Tim Ferriss Show: Chris Dixon and Naval Ravikant**](https://tim.blog/2021/10/28/chris-dixon-naval-ravikant/)** **— long podcast (>2 hours) where Chris and Naval cover many topics about web3. It is one of the best podcasts I ever listened to (the transcript is also available).
