---
aliases:
  - "Testing Pyramid vs Testing Trophy"
"Is A":
  - Evergreen
"Last Tweeted": 2023-05-05
Tags:
  - Has Pic
"Created at": "2024-04-18T14:44:00.000Z"
Reviewed: false
Archived: false
Pinned: false
"Belongs to":
  - "[[essay/how-to-test-software-in-2023|How to Test Software in 2023]]"
  - "[[monday-ideas/monday-49|Monday #49]]"
"Old Created At": "2023-03-31T18:19:00.000+02:00"
"Updated at": "2024-09-18T08:44:00.000Z"
Status: Not started
Tweet: "Is the traditional testing pyramid still the right model for your team? As we shift towards more stable contracts and integration tests that offer better ROI, perhaps it's time to consider the testing trophy. Static and integration tests should take precedence. Let's discuss how your testing strategy evolves! #SoftwareTesting #CTO"
notion_id: 9b3cc425-546e-4c38-a235-08a6188d25dc
---

# Testing Pyramid vs Testing Trophy

One of the most popular testing *models* out there is the testing pyramid, made popular by Martin Fowler.

The larger the layer, the more tests and effort on that layer.

The pyramid is based on the assumption that the earlier you catch a bug the better, which is largely right, and also that the more you move up the more tests get slower to write/run and costlier to maintain.

Andrew Twyman, former Staff Engineer at Dropbox: 

> *The earlier a developer finds out about a bug, the easier it is to fix, and the less time it wastes. That means prefer to catch bugs in static analysis (ideally in the IDE), then in the build, then in unit tests, then in integration tests, then in code review, then in QA, then in deployment, then in user reports.*

What I feel is missing though, is that as you move up you also get more stable *contracts*, and higher chance of *changing implementation* under the hood. This makes integration tests *very* valuable, while unit tests… a bit less so.

![image](https://prod-files-secure.s3.us-west-2.amazonaws.com/631d83ff-20ce-4401-a614-56e2c0f97767/c3d6164a-ab2d-49c6-ade3-ee73d7b74903/CleanShot_2023-03-21_at_11.38.072x.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TT7V4AJU%2F20260131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260131T190511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCmt9MTkbXJ2JySxAuFicCjJi0SXTmbn4On%2F7HaECntBQIgZ95tGtEqSghV1nJNKQSyYh3IL0OjtGo3Wxy8dySBnEMqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCMTUiR8pixBgC4B%2BCrcA9rpOAVz40qKpIS8d36hr1mUCEnkJ7HkrtcYnnGasddQTjMa4zyxCyT%2FsYnriCskaizszufo7Cx%2FCLSKnqsUS0mofCaHofbV01WJwuQ4OFaDWJpJboc4fwdntE8vw6%2FjsMm6WN3Vh1E4rJr5049rhdSjZNyHSIWnKDt8caRVIL3AGfzmtjKLuD8GUO5qyTkkKMUW3hv7XQPQ4zpdAY5AQXFgQOE1Va5PruuMPXHJmtlK1VplR0wHnWhNskTOXfuhxcPSea%2BMuB2YH%2BHyags9elCFdOuFPwita0dD3LUxlYaRkQDIx%2BULCJWUYEtqDR%2FtWdVgFFw52kAQu5nFu2i%2B%2BP%2FtO2%2BgbfZF%2BxrdcEQeI8AhqFu93Yl8NPtjMpj67XDQcEit0z94hvz0r2nzWfJQMHOBmX0qzPv9ozarUlnqJQnIucpf5mtOcNMSqr3gX%2Br2NRqis2kX7ckP7a7v%2FmQdtRdi22yJYZBH08IV1%2FapKB9TuAd3nwMp5ScLMf7DCIFzvlUHMRgoB4Oq0%2BuY8zYGX4qxfQPFq%2B2mwBrwVGBnID4esul7VrorVuAUt%2F2TeEn7NqLJ21aL8OGXPkKTl7mQmiu07IzmoPDNTH5S8%2FhuoVMe7mlWvqh6OD3a%2BiXOMMaL%2BcsGOqUBdfGLG%2BUxXlbTXQps8wEEtwDULZtAxB3bKEuD%2BbhmN6%2FA0ug8vUCsO6c%2BkFU7efdrO%2BnXp6a6EoSqCyi%2F0Z6n6hjwiJnT7nsTmoc9xFyFHOdq0K4gfN22C5m0x2JAWOS2ncBOzGqWMShvj2uhwNpMKd6AgWUHnCkQtAcmDjJPjosiWz5ppaMyjgtWASBR5A16ykF6bHVAu4e8ZH2bYuYo4wI%2BhYOb&X-Amz-Signature=b4fdc200a7ed4b2dbef6b1f785f1deb9f074e4918e26d6def5ec5bc2e4dd8f76&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

To Martin’s (and others’) credit, things haven’t always been like this. In the past we would write most code from scratch. There were lot of custom functions, a lot of algorithms, so unit tests verified complex stuff whose implementation might also change in the future.

Today, especially at unit level, we mostly write software by *composing* stuff. 

Logic in itself is trivial, and when it changes, most often it does because the contract itself changes as well — which puts unit tests into the liability bucket.

So, I don’t feel the pyramid is still the right mental model for most teams.

### 🏆 Testing trophy

When you look at the table above, you see that the ideal testing strategy might not look like a pyramid after all, but more like a diamond.

Or, [as Kent said](https://kentcdodds.com/blog/write-tests), like a trophy.

![The testing trophy proposed by Kent C. Dodds](https://prod-files-secure.s3.us-west-2.amazonaws.com/631d83ff-20ce-4401-a614-56e2c0f97767/70d230bb-2d25-4d7c-a128-18b6ea882058/DVUoM94VQAAzuws.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TT7V4AJU%2F20260131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260131T190511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCmt9MTkbXJ2JySxAuFicCjJi0SXTmbn4On%2F7HaECntBQIgZ95tGtEqSghV1nJNKQSyYh3IL0OjtGo3Wxy8dySBnEMqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCMTUiR8pixBgC4B%2BCrcA9rpOAVz40qKpIS8d36hr1mUCEnkJ7HkrtcYnnGasddQTjMa4zyxCyT%2FsYnriCskaizszufo7Cx%2FCLSKnqsUS0mofCaHofbV01WJwuQ4OFaDWJpJboc4fwdntE8vw6%2FjsMm6WN3Vh1E4rJr5049rhdSjZNyHSIWnKDt8caRVIL3AGfzmtjKLuD8GUO5qyTkkKMUW3hv7XQPQ4zpdAY5AQXFgQOE1Va5PruuMPXHJmtlK1VplR0wHnWhNskTOXfuhxcPSea%2BMuB2YH%2BHyags9elCFdOuFPwita0dD3LUxlYaRkQDIx%2BULCJWUYEtqDR%2FtWdVgFFw52kAQu5nFu2i%2B%2BP%2FtO2%2BgbfZF%2BxrdcEQeI8AhqFu93Yl8NPtjMpj67XDQcEit0z94hvz0r2nzWfJQMHOBmX0qzPv9ozarUlnqJQnIucpf5mtOcNMSqr3gX%2Br2NRqis2kX7ckP7a7v%2FmQdtRdi22yJYZBH08IV1%2FapKB9TuAd3nwMp5ScLMf7DCIFzvlUHMRgoB4Oq0%2BuY8zYGX4qxfQPFq%2B2mwBrwVGBnID4esul7VrorVuAUt%2F2TeEn7NqLJ21aL8OGXPkKTl7mQmiu07IzmoPDNTH5S8%2FhuoVMe7mlWvqh6OD3a%2BiXOMMaL%2BcsGOqUBdfGLG%2BUxXlbTXQps8wEEtwDULZtAxB3bKEuD%2BbhmN6%2FA0ug8vUCsO6c%2BkFU7efdrO%2BnXp6a6EoSqCyi%2F0Z6n6hjwiJnT7nsTmoc9xFyFHOdq0K4gfN22C5m0x2JAWOS2ncBOzGqWMShvj2uhwNpMKd6AgWUHnCkQtAcmDjJPjosiWz5ppaMyjgtWASBR5A16ykF6bHVAu4e8ZH2bYuYo4wI%2BhYOb&X-Amz-Signature=ed9491ca90e4fdafa07b0df8bf9b7f9047002c7dab3e3e27bbd052cacdc00a7b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

The ideas behind the trophy are simple:

1. Static testing is a no-brainer.

1. Integration tests consistently deliver the best ROI, so most of your effort should be spent on those.

1. End to end and Unit tests are good when used for the right things.
