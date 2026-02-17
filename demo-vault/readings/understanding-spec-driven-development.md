---
aliases:
  - "Understanding Spec-Driven-Development"
"Related to": "[[readings-digest/weekly-digest-2|Weekly Digest #2]]"
Summary: Spec-driven development means writing structured specs before generating code with AI. Different tools (Kiro, spec-kit, Tessl) implement this in varied ways, from spec-first to spec-as-source. The term is still vague and tools differ on how specs are maintained over time.
"Discarded for digest?": false
"Note Status": Saved
URL: "https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html"
Author: Birgitta Böckeler
Category: Articles
"Full Title": "Understanding Spec-Driven-Development: Kiro, Spec-Kit, and Tessl"
Highlights: 2
"Last Synced": 2025-12-10
"Last Highlighted": 2025-11-26
notion_id: 2c5bdf02-815c-81ce-80e8-d7c4654a7779
---

# Understanding Spec-Driven-Development

After looking over the usages of the term, and some of the tools that claim to be implementing SDD, it seems to me that in reality, there are multiple implementation levels to it:
1. **Spec-first**: A well thought-out spec is written first, and then used in the AI-assisted development workflow for the task at hand.
2. **Spec-anchored**: The spec is kept even after the task is complete, to continue using it for evolution and maintenance of the respective feature.
3. **Spec-as-source**: The spec is the main source file over time, and only the spec is edited by the human, the human never touches the code. ([View Highlight](https://read.readwise.io/read/01kb0dngz7bq8zjtpv6av0z5k9))


What is a spec? There doesn’t seem to be a general definition, the closest I’ve seen to a consistent definition is the comparison of a spec to a “Product Requirements Document”. ([View Highlight](https://read.readwise.io/read/01kb0dnxp0ktjt8c63t59q4j05))
