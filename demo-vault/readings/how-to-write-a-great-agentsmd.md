---
aliases:
  - "How to Write a Great AGENTS.md"
"Related to": "[[readings-digest/weekly-digest-2|Weekly Digest #2]]"
Summary: "GitHub Copilot now supports custom agents via agents.md so you can make specialist assistants (docs, tests, lint, etc.). The best agents are specific: give a clear persona, exact commands, code examples, tech stack, and strict boundaries. Start small, cover commands/testing/structure/style/git/boundaries, and iterate."
"Discarded for digest?": false
"Note Status": Saved
URL: "https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/?aid=recRXGXbVJttNiPz6&_bhlid=dce1707943da35b9c4b36e108f54c29c2863b495"
Author: Matt Nigh
Category: Articles
"Full Title": "How to Write a Great agents.md: Lessons From Over 2,500 Repositories"
Highlights: 4
"Last Synced": 2025-12-10
"Last Highlighted": 2025-11-26
notion_id: 2c5bdf02-815c-81d0-be85-edbce590795f
---

# How to Write a Great AGENTS.md

Example of a great agent.md file ([View Highlight](https://read.readwise.io/read/01kb0en4a0388e765epv874he6))

Pick one simple task. Don’t build a “general helper.” Pick something specific like:
•   Writing function documentation
•   Adding unit tests
•   Fixing linting errors
Start minimal—you only need three things:
•   **Agent name**: `test-agent`, `docs-agent`, `lint-agent`
•   **Description**: “Writes unit tests for TypeScript functions”
•   **Persona**: “You are a quality software engineer who writes comprehensive tests” ([View Highlight](https://read.readwise.io/read/01kb0eqtgnhey6jnjprqx6axn3))

Six agents worth building ([View Highlight](https://read.readwise.io/read/01kb0eqyac9jtsb5rt7y07mrwx))

@docs-agent
One of your early agents should write documentation. It reads your code and generates API docs, function references, and tutorials. Give it commands like `npm run docs:build` and `markdownlint docs/` so it can validate its own work. Tell it to write to `docs/` and never touch `src/`.
•   What it does: Turns code comments and function signatures into Markdown documentation
•   Example commands: `npm run docs:build`, `markdownlint docs/`
•   Example boundaries: Write to `docs/`, never modify source code
@test-agent
This one writes tests. Point it at your test framework (Jest, PyTest, Playwright) and give it the command to run tests. The boundary here is critical: it can write to `tests` but should never remove a test because it is failing and cannot be fixed by the agent.
•   What it does: Writes unit tests, integration tests, and edge case coverage
•   Example commands: `npm test`, `pytest -v`, `cargo test --coverage`
•   Example boundaries: Write to `tests/`, never remove failing tests unless authorized by user
@lint-agent
A fairly safe agent to create early on. It fixes code style and formatting but shouldn’t change logic. Give it commands that let it auto-fix style issues. This one’s low-risk because linters are designed to be safe.
•   What it does: Formats code, fixes import order, enforces naming conventions
•   Example commands: `npm run lint --fix`, `prettier --write`
•   Example boundaries: Only fix style, never change code logic
@api-agent
This agent builds API endpoints. It needs to know your framework (Express, FastAPI, Rails) and where routes live. Give it commands to start the dev server and test endpoints. The key boundary: it can modify API routes but must ask before touching database schemas.
•   What it does: Creates REST endpoints, GraphQL resolvers, error handlers
•   Example commands: `npm run dev`, `curl localhost:3000/api`, `pytest tests/api/`
•   Example boundarie...

...s: Modify routes, ask before schema changes
@dev-deploy-agent
Handles builds and deployments to your local dev environment. Keep it locked down: only deploy to dev environments and require explicit approval. Give it build commands and deployment tools but make the boundaries very clear.
•   What it does: Runs local or dev builds, creates Docker images
•   Example commands: `npm run test`
•   Example boundaries: Only deploy to dev, require user approval for anything with risk ([View Highlight](https://read.readwise.io/read/01kb0etfgvgxzb0sseeg4xf74g))
