# AI Content Intelligence Platform Plan

> Goal: Build an AI-assisted content production system that can collect AI trends, read projects, rank opportunities, recommend topics, generate short-video scripts, produce articles, and create storyboards/visual directions. Each stage should work as an independent product and also collaborate as one pipeline.

## 1. Product Vision

The product should become a content supply-chain platform for AI technology creators.

Instead of only generating scripts, it should help creators answer the full workflow:

- What happened today in AI?
- Which projects, papers, products, or news are worth covering?
- Why does this item matter?
- Which angle is best for short video, article, or deep analysis?
- What should the creator say?
- What should appear on screen?
- What assets should be generated or recorded?

The first target user is an AI technology content creator who wants to publish daily Douyin, Xiaohongshu, WeChat, Bilibili, or newsletter content.

## 2. Core Principle

Each stage is both:

1. An independent product that can be used alone.
2. A pipeline node that reads and writes a shared structured content object.

This keeps the system productizable in multiple ways:

- A creator can use only the topic selector.
- A team can use only the project reader.
- A media workflow can run the full pipeline from data collection to storyboard.
- A future SaaS product can expose each module as a separate feature.

## 3. End-to-End Workflow

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

The recommended early workflow is human-in-the-loop. AI should generate and rank options, while the creator approves facts, angles, scripts, and final outputs.

## 4. Product Modules

### 4.1 AI Trend Radar

Purpose: Automatically collect AI-related content leads.

Sources:

- GitHub Trending
- GitHub Search
- Hacker News
- Product Hunt
- Hugging Face
- arXiv
- Reddit
- X/Twitter
- AI newsletters and blogs
- YouTube channels
- Chinese platforms such as Zhihu, Jike, WeChat articles, and Xiaohongshu when available

Independent product form:

> Daily AI trend radar that gives creators a ranked list of content leads.

Core output:

```json
{
  "id": "source-item-id",
  "title": "Project or news title",
  "source": "GitHub",
  "url": "https://example.com",
  "category": "AI Agent",
  "raw_content": "README, article text, abstract, or metadata",
  "signals": {
    "stars": 1200,
    "star_growth": 300,
    "comments": 48,
    "recency": "2026-07-02"
  }
}
```

### 4.2 AI Project Reader

Purpose: Read and explain a project, paper, product, or news item.

It should not only summarize. It should translate technical material into content strategy.

Questions it must answer:

- What is this?
- What problem does it solve?
- Who is it for?
- What is the strongest demo or visual proof?
- Why is it trending now?
- What makes it different from existing tools?
- What are the risks, limitations, or hype points?
- Is it suitable for short video, long article, or both?

Independent product form:

> Paste a GitHub link or article link and get a creator-friendly analysis report.

Core output:

```json
{
  "summary": "One paragraph explanation",
  "one_liner": "One sentence for non-technical audiences",
  "target_users": ["Developers", "AI creators", "Startup founders"],
  "key_points": ["Point 1", "Point 2", "Point 3"],
  "demo_potential": "High",
  "limitations": ["No hosted demo", "Requires local setup"],
  "fact_check_notes": ["Verify star count", "Check license"]
}
```

### 4.3 Content Opportunity Ranker

Purpose: Decide which items are worth turning into content.

Scoring dimensions:

- Novelty
- Timeliness
- Visual demonstration potential
- Ease of explanation
- Audience relevance
- Title potential
- Business value
- Technical credibility
- Controversy or discussion potential
- Platform fit

Independent product form:

> Content opportunity scoring assistant for AI creators.

Recommended scoring:

```json
{
  "overall_score": 87,
  "recommendation": "Strongly recommend",
  "best_platforms": ["Douyin", "Bilibili", "WeChat"],
  "best_formats": ["90-second short video", "3-minute explainer"],
  "reason": "Clear demo, strong hook, useful to creators and developers"
}
```

### 4.4 Topic Angle Generator

Purpose: Generate multiple content angles for the same item.

Example angles:

- Technical angle
- Founder/startup angle
- Creator productivity angle
- Ordinary user angle
- Controversy angle
- Investment/trend angle
- Comparison angle

Independent product form:

> AI topic angle and hook generator.

Core output:

```json
{
  "angles": [
    {
      "name": "Ordinary user angle",
      "hook": "This AI project wants to let anyone build software without coding.",
      "title": "GitHub today is talking about an AI tool that builds apps for you",
      "audience": "Non-technical AI users"
    }
  ]
}
```

### 4.5 Short Video Script Agent

Purpose: Generate scripts for Douyin, Xiaohongshu, Bilibili, video account, or YouTube Shorts.

Supported formats:

- 30-second quick news
- 60-second trend brief
- 90-second project explanation
- 3-minute deep dive
- Screen-recording commentary
- Talking-head script
- Digital human narration

Independent product form:

> AI technology short-video script writer.

Standard script structure:

```text
0-3 seconds: Hook
3-15 seconds: What it is
15-45 seconds: Three key points
45-70 seconds: Use cases and opportunity
70-85 seconds: Limitations and fact-check reminder
85-90 seconds: Closing and follow prompt
```

Core output:

```json
{
  "platform": "Douyin",
  "duration_seconds": 90,
  "title": "GitHub's trending AI project wants to build apps for you",
  "script": "Full spoken script",
  "captions": ["Caption line 1", "Caption line 2"],
  "cta": "Follow for daily AI project picks"
}
```

### 4.6 Article Writer Agent

Purpose: Convert the selected item into a long-form article.

Target platforms:

- WeChat official account
- Zhihu
- Xiaohongshu notes
- Bilibili articles
- Newsletter
- SEO blog

Independent product form:

> AI technology article writer and editor.

Article structure:

```text
Title
Summary
Background
What the project/product does
Core features
Use cases
Technical highlights
Comparison with alternatives
Business or creator opportunities
Risks and limitations
Conclusion
```

The article should not be a simple expansion of the video script. It should include more context, careful reasoning, and explicit fact-check notes.

### 4.7 Storyboard Agent

Purpose: Turn a script into an executable video production plan.

It should describe:

- Shot timing
- Visual content
- On-screen text
- Required screen recording
- Required demo recording
- Generated graphics
- B-roll suggestions
- Transitions
- Sound effects
- Cover image direction

Independent product form:

> AI storyboard director for technology short videos.

Core output:

```json
{
  "shots": [
    {
      "time_range": "0-3s",
      "visual": "Fast zoom into GitHub Trending page",
      "caption": "Today's GitHub AI trend",
      "asset_type": "screen_recording",
      "editing_note": "Use quick push-in transition"
    }
  ]
}
```

### 4.8 Visual Asset Agent

Purpose: Generate or specify visual materials for the video and article.

Asset types:

- Cover image
- Vertical information card
- Comparison chart
- Workflow diagram
- Concept illustration
- Architecture diagram
- Timeline image
- Screenshot annotation
- Thumbnail text variants

Independent product form:

> AI visual planner for tech content.

The module should first generate prompts and layout directions. Direct automatic image/video generation can come later.

## 5. Shared Content Data Model

All modules should collaborate through a shared content object.

```json
{
  "id": "2026-07-02-github-ai-project-001",
  "source_item": {
    "title": "",
    "url": "",
    "source": "",
    "collected_at": "",
    "raw_content": ""
  },
  "research": {
    "summary": "",
    "one_liner": "",
    "key_points": [],
    "limitations": [],
    "fact_check_notes": []
  },
  "scores": {
    "overall_score": 0,
    "novelty": 0,
    "visual_potential": 0,
    "audience_fit": 0,
    "technical_credibility": 0,
    "recommendation": ""
  },
  "angles": [],
  "video_scripts": [],
  "articles": [],
  "storyboards": [],
  "visual_assets": [],
  "review_status": {
    "research_approved": false,
    "topic_approved": false,
    "script_approved": false,
    "storyboard_approved": false
  }
}
```

This object can live first as JSON files or database rows. The important rule is that every module reads from it and writes back to it.

## 6. Collaboration Modes

### 6.1 Single-Module Mode

User directly uses one module.

Examples:

- Paste a GitHub URL and get a project report.
- Paste a project report and get a Douyin script.
- Paste a script and get a storyboard.

### 6.2 Pipeline Mode

The system runs all modules in sequence.

Example:

```text
Collect 100 AI items today
  -> Read top 30
  -> Rank top 10
  -> Generate angles for top 5
  -> Generate scripts for top 3
  -> Generate storyboard for selected 1
```

### 6.3 Human Review Mode

Each stage requires approval before moving to the next stage.

Recommended early production workflow:

```text
AI collects
  -> Human picks sources to read
  -> AI reads
  -> Human confirms facts
  -> AI ranks and suggests angles
  -> Human selects angle
  -> AI writes script and article
  -> Human edits
  -> AI creates storyboard and asset plan
```

This mode is best for quality and trust.

## 7. MVP Scope

The first version should avoid full auto-video generation. The fastest useful MVP is:

Input:

- GitHub Trending list, GitHub search results, or a pasted GitHub URL.

Output:

- Project reading report
- Content opportunity score
- Three recommended titles
- Three content angles
- One 90-second Douyin script
- One storyboard draft

MVP success criteria:

- A creator can produce one AI project short-video script in less than 10 minutes.
- The system can explain why a project is or is not worth covering.
- The output includes fact-check notes instead of pretending everything is verified.
- Each stage can be re-run independently.

## 8. Suggested Roadmap

### Phase 1: Manual Pipeline Prototype

Build the workflow with prompts, JSON files, and manual copy/paste.

Deliverables:

- Prompt templates for each module
- Shared content JSON schema
- Example outputs for 3-5 GitHub AI projects
- Manual review checklist

### Phase 2: Semi-Automated Workbench

Build a small internal app or CLI.

Deliverables:

- Add URL or GitHub repo input
- Fetch README/article text
- Generate project report
- Generate ranking
- Generate script and storyboard
- Save each content item

### Phase 3: Daily Trend Radar

Automate collection.

Deliverables:

- Scheduled source collection
- Deduplication
- Category tagging
- Hotness scoring
- Daily digest

### Phase 4: Creator Workspace

Turn it into a product workflow.

Deliverables:

- Content item dashboard
- Review states
- Script editor
- Article editor
- Storyboard view
- Export to Markdown, JSON, CSV, or document formats

### Phase 5: Visual and Video Integration

Connect the output to production tools.

Deliverables:

- Cover prompt generator
- Screenshot annotation plan
- CapCut/Jianying-friendly storyboard export
- Image-generation prompt export
- Optional digital human script export

## 9. Recommended Technical Architecture

Start simple:

```text
Frontend or CLI
  -> API layer
  -> Agent orchestration layer
  -> Source collectors
  -> LLM generation modules
  -> Storage
```

Suggested components:

- Storage: JSON files for prototype, PostgreSQL for product stage.
- Queue: simple scheduled jobs first, then Redis/Celery or equivalent if needed.
- LLM layer: one abstraction for model calls, prompts, structured output, and retries.
- Source collectors: isolated adapters for GitHub, Hacker News, Product Hunt, arXiv, and other sources.
- Review workflow: explicit state fields for each content item.

## 10. Initial Prompt Assets

### 10.1 Project Reading Prompt

```text
You are an AI technology content analyst.
Read the following project or article material and produce a creator-friendly report.

Return:
1. One-sentence explanation
2. Plain-language summary
3. Target users
4. Three key highlights
5. Visual demo potential
6. Why it is trending
7. Similar tools or competitors
8. Risks and limitations
9. Fact-check notes
10. Whether this is suitable for short video, long article, or both
```

### 10.2 Ranking Prompt

```text
You are an AI content editor.
Score this item for short-video potential.

Score from 1 to 10:
- Novelty
- Timeliness
- Visual potential
- Ease of explanation
- Audience relevance
- Title potential
- Business value
- Technical credibility
- Discussion potential

Then give:
- Overall score
- Recommendation
- Best platform
- Best content format
- Reason for recommendation
```

### 10.3 Short Video Script Prompt

```text
You are a Douyin technology short-video scriptwriter.
Write a 90-second script based on the selected AI project.

Structure:
0-3 seconds: Strong hook
3-15 seconds: What it is
15-45 seconds: Three key highlights
45-70 seconds: Use cases and opportunity
70-85 seconds: Limitations or fact-check reminder
85-90 seconds: Closing and follow prompt

Style:
- Clear to non-technical users
- No exaggerated claims
- Conversational
- Suitable for spoken delivery
```

### 10.4 Storyboard Prompt

```text
You are a short-video director.
Turn this script into a storyboard.

For each shot, include:
- Time range
- Visual content
- On-screen caption
- Asset type
- Editing note
- Whether screen recording, demo recording, generated image, or chart is needed
```

## 11. Quality Control Rules

The system must avoid low-trust AI content.

Rules:

- Do not claim a project is trending unless source signals support it.
- Do not invent star counts, funding, users, benchmarks, or author background.
- Keep fact-check notes visible.
- Prefer "may", "appears to", and "based on the README" when evidence is incomplete.
- Distinguish between project claims and verified behavior.
- Always flag missing demos, unclear licenses, inactive repos, and setup difficulty.

## 12. Productization Strategy

Best first product:

> AI technology creator workbench: from GitHub project link to topic score, short-video script, article draft, and storyboard.

Why this is the best first product:

- Clear target user.
- Strong daily usage scenario.
- Easy to validate by using it for your own content.
- Does not require full video automation at the beginning.
- Each module can later become a standalone paid feature.

Potential standalone products:

- Daily AI Trend Radar
- GitHub Project Reader
- AI Content Topic Ranker
- AI Short Video Script Writer
- AI Article Writer
- AI Storyboard Director
- AI Visual Asset Planner

## 13. Next Actions

1. Define the first target platform: Douyin only, or Douyin plus WeChat/Bilibili.
2. Pick the first source: GitHub Trending is recommended.
3. Create 5 sample content items manually.
4. Run the full manual prompt pipeline on those samples.
5. Compare the generated scripts with publishable human-edited scripts.
6. Lock the shared JSON schema.
7. Build the first semi-automated MVP around GitHub project input.

