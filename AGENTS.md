# AGENTS.md

## Project Overview

This project is an AI Content Intelligence Platform for AI technology creators.
It should help collect AI trends, read projects or articles, rank content
opportunities, generate topic angles, create short-video scripts, draft
articles, produce storyboards, and plan visual assets.

The authoritative product plan is `PLAN.md`. When implementation details are
unclear, follow `PLAN.md` first and ask before expanding scope.

## Core Principles

1. Each module must be usable independently.
2. Each module must produce a structured result that can be passed to the next
   module.
3. The full workflow is a pipeline of independent modules, not one large
   monolithic prompt.
4. Strictly follow the documented product plan and current task instructions.
   Do not invent new product scope, extra agents, new platforms, or unrelated
   features unless the user explicitly asks for them.
5. Keep humans in the review loop. AI output should support creator decisions,
   not silently publish or claim certainty.

## Reference Project

The `example/` directory is a reference project only. It demonstrates a useful
technical route:

- data collection through dedicated dataflow modules
- role-based agents that analyze shared state
- graph or pipeline orchestration
- structured outputs and render helpers
- CLI and programmatic entry points
- tests around routing, configuration, schemas, and output behavior

Do not copy the financial trading domain from `example/` into this project.
Use it as an engineering reference for a data-driven, multi-agent analysis
system.

## Target Workflow

The intended end-to-end flow is:

```text
Information Sources
  -> Trend Collection
  -> Project/Article Reading
  -> Content Opportunity Ranking
  -> Topic Angle Generation
  -> Short Video Script Generation
  -> Article Generation
  -> Storyboard Generation
  -> Visual Asset Planning
  -> Human Review
  -> Publishing
```

Early development should prioritize the documented MVP:

- input from GitHub Trending, GitHub search results, or a pasted GitHub URL
- project reading report
- content opportunity score
- three recommended titles
- three content angles
- one 90-second Douyin script
- one storyboard draft

## Recommended Architecture

Start simple and keep the module boundaries explicit:

```text
CLI or Workbench
  -> API layer
  -> Agent orchestration layer
  -> Source collectors
  -> LLM generation modules
  -> Storage
```

Recommended technical route:

- Python for the backend, collectors, agents, and orchestration.
- LangGraph or a similar graph/pipeline framework for multi-step workflows.
- Pydantic or TypedDict schemas for shared content objects and agent outputs.
- JSON files for prototype storage; PostgreSQL can come later for product use.
- Isolated adapters for each source such as GitHub, Hacker News, Product Hunt,
  Hugging Face, arXiv, newsletters, and Chinese content platforms when added.
- Structured LLM calls where possible, with graceful fallback when a provider
  cannot return structured output.

## Future Directory Guidelines

The repository is still early. When adding implementation, prefer a structure
like this:

- `src/collectors/`: source-specific data collection adapters.
- `src/readers/`: project, article, paper, and product readers.
- `src/agents/`: role-specific agent prompts, schemas, and execution logic.
- `src/graph/`: pipeline or graph orchestration.
- `src/schemas/`: shared content object and module output schemas.
- `src/storage/`: JSON, database, cache, and report persistence.
- `src/llm/`: model clients, provider config, retries, and structured output
  helpers.
- `cli/`: command-line workflows for manual and semi-automated runs.
- `tests/`: unit and integration tests.
- `examples/`: sample input and output artifacts for documented workflows.

Keep `example/` separate from the main implementation. It is a reference, not a
package namespace for this product.

## Module Responsibilities

### AI Trend Radar

Collect AI-related leads from documented sources. Output raw source items with
source URL, title, raw content or metadata, category, and signal fields.

### AI Project Reader

Read a project, article, paper, product page, or news item. Explain what it is,
who it is for, why it matters, what can be demonstrated visually, and what needs
fact-checking.

### Content Opportunity Ranker

Score whether an item is worth turning into content. Use the dimensions from
`PLAN.md`: novelty, timeliness, visual potential, ease of explanation, audience
relevance, title potential, business value, technical credibility, discussion
potential, and platform fit.

### Topic Angle Generator

Generate multiple documented content angles for the same source item. Do not
invent unsupported claims just to make an angle stronger.

### Short Video Script Agent

Generate platform-appropriate scripts, especially the MVP 90-second Douyin
script. Follow the timing structure in `PLAN.md`.

### Article Writer Agent

Create long-form drafts for WeChat, Zhihu, Xiaohongshu notes, Bilibili articles,
newsletters, or SEO blogs when requested. Articles should add context and
reasoning instead of merely expanding the video script.

### Storyboard Agent

Turn an approved script into a shot-by-shot production plan with timing, visual
content, captions, asset types, and editing notes.

### Visual Asset Agent

Plan cover images, information cards, comparison charts, diagrams, timelines,
screenshot annotations, and thumbnail variants. Start with prompts and layout
directions before adding automatic asset generation.

## Shared Content Object

All modules should read and write a shared structured content object. The shape
should follow `PLAN.md` and include:

- `source_item`
- `research`
- `scores`
- `angles`
- `video_scripts`
- `articles`
- `storyboards`
- `visual_assets`
- `review_status`

Do not pass important state only through prose. If a downstream module needs a
field, add it to the schema and cover it with tests.

## Data and Evidence Rules

Trust is central to this product. Follow these rules:

- Do not claim an item is trending unless source signals support it.
- Do not invent star counts, funding, users, benchmarks, company background, or
  author background.
- Keep source URLs and collection timestamps with collected items.
- Distinguish project claims from verified behavior.
- Use cautious wording such as "may", "appears to", and "based on the README"
  when evidence is incomplete.
- Always surface fact-check notes.
- Flag missing demos, unclear licenses, inactive repositories, setup difficulty,
  and unverifiable claims.

## Agent Guidelines

Agent modules should follow this pattern:

1. Read the shared content object or a single documented input.
2. Build prompt/context from explicit fields, not hidden assumptions.
3. Use tools or source adapters through public interfaces.
4. Request structured output when possible.
5. Validate and normalize the output.
6. Write only the fields owned by that module.

Avoid agents directly scraping arbitrary sources when a collector or reader
adapter should own that responsibility.

## Development Guidelines

- Keep changes scoped to the documented module being built.
- Prefer small, testable modules over large prompt chains.
- Prefer schemas and render helpers over parsing free-form text.
- Keep prompts versioned in files when they become stable.
- Do not silently add new data vendors, platforms, or publishing targets.
- Do not reformat or refactor unrelated files.
- Preserve the ability to run one module independently.
- Preserve the ability to run the full pipeline by passing structured outputs
  from one module to the next.

## Testing Guidelines

Most tests should not require real API calls or live network access. Use stored
fixtures, mocked source responses, and fake LLM outputs where possible.

When changing collectors, test:

- source response parsing
- missing or malformed data
- deduplication behavior
- timestamps and source metadata

When changing schemas, test:

- required fields
- defaults
- serialization and deserialization
- backward-compatible migrations when relevant

When changing agents, test:

- prompt input construction
- structured output parsing
- fallback behavior for invalid or partial model output
- ownership of written fields

When changing orchestration, test:

- module order
- independent module execution
- pipeline handoff between modules
- human-review gates

## Common Pitfalls

- Treating `example/` as the main product instead of a reference.
- Building a single giant prompt instead of independent modules.
- Letting downstream modules depend on undocumented prose instead of structured
  fields.
- Expanding the product beyond `PLAN.md` without user approval.
- Generating persuasive content that hides uncertainty.
- Losing source evidence while transforming content through the pipeline.
- Adding real API requirements to tests that should run offline.
