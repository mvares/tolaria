---
aliases:
  - "When you develop web3 apps you should prepare for failure"
"Is A":
  - Evergreen
"Last Tweeted": 2022-11-30
"Created at": "2024-04-18T14:44:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to":
  - "[[essay/web3-engineering-part-2|Web3 Engineering (Part 2)]]"
  - "[[monday-ideas/monday-26|Monday #26]]"
"Old Created At": "2022-01-14T16:07:00.000+01:00"
"Updated at": "2024-04-19T09:37:00.000Z"
Status: Not started
notion_id: 44171c7e-2414-4242-a923-d8d6460a9070
---

# When you develop web3 apps you should prepare for failure

[ConsenSys](https://consensys.net/), the leading development firm in this space behind projects like [MetaMask](https://metamask.io/) and [Truffle](https://trufflesuite.com/), maintains a list of best practices around software engineering.

As they say:

> *It is not enough to protect yourself against the known attacks. Since the ****cost of failure**** on a blockchain can be very high, you must also adapt the way you write software, to account for that risk.

The approach we advocate is to "****prepare for failure****". It is impossible to know in advance whether your code is secure. However, you can architect your contracts in a way that allows them to ****fail gracefully****, and with minimal damage.*

You find the full document here: 

- **📑 **[**Software Engineering Best Practices**](https://github.com/ConsenSys/smart-contract-best-practices/blob/master/docs/software_engineering.md)

It includes patterns to make contracts upgradeable and techniques to make them fail-proof, like *circuit breakers*, *speed bumps*, and *rate limiting*.
