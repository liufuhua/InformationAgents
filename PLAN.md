# AI 内容情报平台计划

> 目标：构建一个 AI 辅助的内容生产系统，可以收集 AI 趋势、阅读项目、评估机会、推荐选题、生成短视频脚本、撰写文章，并生成分镜和视觉方向。每个阶段既能独立使用，也能组合成完整流水线。

## 1. 产品愿景

本产品应成为 AI 技术内容创作者的内容供应链平台。

它不只是生成脚本，而是帮助创作者回答完整工作流里的问题：

- 今天 AI 领域发生了什么？
- 哪些项目、论文、产品或新闻值得报道？
- 这个条目为什么重要？
- 它更适合短视频、文章还是深度分析？
- 创作者应该怎么讲？
- 屏幕上应该展示什么？
- 需要生成或录制哪些素材？

首个目标用户是需要在抖音、小红书、微信公众号、Bilibili 或 newsletter 上持续发布内容的 AI 技术内容创作者。

## 2. 核心原则

每个阶段同时具备两种形态：

1. 可以单独使用的独立产品。
2. 读取并写入共享结构化内容对象的流水线节点。

这样可以支持多种产品化方式：

- 创作者只使用选题器。
- 团队只使用项目阅读器。
- 媒体工作流从数据采集一路跑到分镜。
- 未来 SaaS 可以把每个模块作为独立功能暴露。

## 3. 端到端工作流

```text
信息来源
  -> 趋势收集
  -> 项目/文章阅读
  -> 内容机会排序
  -> 选题角度生成
  -> 短视频脚本生成
  -> 文章生成
  -> 分镜生成
  -> 视觉资产规划
  -> 人工审核
  -> 发布
```

早期推荐采用人工在环工作流。AI 负责生成和排序选项，创作者负责确认事实、角度、脚本和最终输出。

## 4. 产品模块

### 4.1 AI Trend Radar

用途：自动收集 AI 相关内容线索。

来源：

- GitHub Trending
- GitHub Search
- Hacker News
- Product Hunt
- Hugging Face
- arXiv
- Reddit
- X/Twitter
- AI newsletter 和博客
- 中文平台，例如知乎、即刻、微信公众号、小红书等，等具备可靠接入条件后再加入

独立产品形态：

> 每日 AI 趋势雷达，为创作者提供排序后的内容线索列表。

核心输出：

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

用途：阅读并解释一个项目、论文、产品或新闻条目。

它不只是摘要器，而是把技术材料翻译成内容策略。

必须回答的问题：

- 这是什么？
- 它解决什么问题？
- 它面向谁？
- 最强的 Demo 或视觉证明是什么？
- 它为什么现在值得关注？
- 它和现有工具有什么不同？
- 风险、限制或炒作点是什么？
- 它适合短视频、长文章，还是两者都适合？

独立产品形态：

> 粘贴 GitHub 链接或文章链接，得到面向创作者的分析报告。

核心输出：

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

用途：判断某个条目是否值得做成内容。

评分维度：

- 新颖性
- 时效性
- 视觉展示潜力
- 解释难度
- 受众相关性
- 标题潜力
- 商业价值
- 技术可信度
- 争议或讨论潜力
- 平台匹配度

独立产品形态：

> 面向 AI 创作者的内容机会评分助手。

推荐评分输出：

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

用途：为同一个条目生成多个内容角度。

示例角度：

- 技术角度
- 创始人/创业角度
- 创作者提效角度
- 普通用户角度
- 争议角度
- 投资/趋势角度
- 对比角度

独立产品形态：

> AI 选题角度和开头钩子生成器。

核心输出：

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

用途：生成适合抖音、小红书、Bilibili、视频号或 YouTube Shorts 的脚本。

支持格式：

- 30 秒快讯
- 60 秒趋势简报
- 90 秒项目解释
- 3 分钟深度讲解
- 屏幕录制解说
- 真人口播脚本
- 数字人旁白

独立产品形态：

> AI 技术短视频脚本写作器。

标准脚本结构：

```text
0-3 秒：钩子
3-15 秒：它是什么
15-45 秒：三个关键点
45-70 秒：使用场景和机会
70-85 秒：限制和事实核查提醒
85-90 秒：结尾和关注提示
```

核心输出：

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

用途：把选定条目转换成长文。

目标平台：

- 微信公众号
- 知乎
- 小红书笔记
- Bilibili 文章
- Newsletter
- SEO 博客

独立产品形态：

> AI 技术文章写作和编辑器。

文章结构：

```text
标题
摘要
背景
项目/产品做什么
核心功能
使用场景
技术亮点
与替代方案对比
商业或创作者机会
风险和限制
结论
```

文章不能只是视频脚本的扩写。它应包含更多上下文、谨慎推理和明确事实核查备注。

### 4.7 Storyboard Agent

用途：把脚本转换成可执行的视频生产计划。

需要描述：

- 镜头时间
- 画面内容
- 屏幕文字
- 需要的屏幕录制
- 需要的 Demo 录制
- 生成图形
- B-roll 建议
- 转场
- 音效
- 封面图方向

独立产品形态：

> AI 技术短视频分镜导演。

核心输出：

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

用途：为视频和文章生成或指定视觉素材。

素材类型：

- 封面图
- 竖版信息卡
- 对比图
- 流程图
- 概念插图
- 架构图
- 时间线图
- 截图标注
- 缩略图文字变体

独立产品形态：

> 面向技术内容的 AI 视觉规划器。

该模块应先生成提示词和布局方向。直接自动生成图片或视频可以后续再做。

## 5. 共享内容数据模型

所有模块都应通过共享内容对象协作。

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

这个对象早期可以存在 JSON 文件或数据库行中。重要规则是：每个模块都读取它，并把自己的结果写回它。

## 6. 协作模式

### 6.1 单模块模式

用户直接使用某一个模块。

示例：

- 粘贴 GitHub URL，得到项目报告。
- 粘贴项目报告，得到抖音脚本。
- 粘贴脚本，得到分镜。

### 6.2 流水线模式

系统按顺序运行所有模块。

示例：

```text
今天收集 100 个 AI 条目
  -> 阅读前 30 个
  -> 排名前 10 个
  -> 为前 5 个生成角度
  -> 为前 3 个生成脚本
  -> 为选中的 1 个生成分镜
```

### 6.3 人工审核模式

每个阶段在进入下一阶段前都需要用户确认。

推荐早期生产工作流：

```text
AI 收集
  -> 人工选择要阅读的来源
  -> AI 阅读
  -> 人工确认事实
  -> AI 排序并建议角度
  -> 人工选择角度
  -> AI 写脚本和文章
  -> 人工编辑
  -> AI 生成分镜和资产计划
```

这种模式最利于质量和信任。

## 7. MVP 范围

第一版应避免完整自动视频生成。最快可用的 MVP 是：

输入：

- GitHub Trending 列表、GitHub 搜索结果，或用户粘贴的 GitHub URL。

输出：

- 项目阅读报告
- 内容机会评分
- 3 个推荐标题
- 3 个内容角度
- 1 条 90 秒抖音脚本
- 1 份分镜草稿

MVP 成功标准：

- 创作者能在 10 分钟内产出一条 AI 项目短视频脚本。
- 系统能解释某个项目为什么值得或不值得报道。
- 输出包含事实核查备注，而不是假装全部已验证。
- 每个阶段都可以独立重跑。

## 8. 建议路线图

### 阶段 1：手动流水线原型

使用提示词、JSON 文件和手动复制粘贴搭建工作流。

交付物：

- 每个模块的提示词模板
- 共享内容 JSON Schema
- 3-5 个 GitHub AI 项目的示例输出
- 手动审核清单

### 阶段 2：半自动工作台

构建一个小型内部应用或 CLI。

交付物：

- 添加 URL 或 GitHub 仓库输入
- 拉取 README 或文章正文
- 生成项目报告
- 生成评分
- 生成脚本和分镜
- 保存每个内容项

### 阶段 3：每日趋势雷达

自动化收集。

交付物：

- 定时来源收集
- 去重
- 分类标签
- 热度评分
- 每日摘要

### 阶段 4：创作者工作区

把能力转成产品工作流。

交付物：

- 内容项仪表盘
- 审核状态
- 脚本编辑器
- 文章编辑器
- 分镜视图
- 导出 Markdown、JSON、CSV 或文档格式

### 阶段 5：视觉和视频集成

把输出连接到生产工具。

交付物：

- 封面提示词生成器
- 截图标注计划
- 适合剪映的分镜导出
- 图片生成提示词导出
- 可选数字人脚本导出

## 9. 推荐技术架构

从简单架构开始：

```text
前端或 CLI
  -> API 层
  -> Agent 编排层
  -> 来源采集器
  -> LLM 生成模块
  -> 存储
```

建议组件：

- 存储：原型阶段使用 JSON 文件，产品阶段使用 PostgreSQL。
- 队列：先使用简单定时任务；如果需要，再引入 Redis/Celery 或同类方案。
- LLM 层：统一封装模型调用、提示词、结构化输出和重试。
- 来源采集器：为 GitHub、Hacker News、Product Hunt、arXiv 等来源建立独立适配器。
- 审核工作流：每个内容项显式记录审核状态。

## 10. 初始提示词资产

### 10.1 项目阅读提示词

```text
你是 AI 技术内容分析师。
阅读下面的项目或文章材料，产出面向创作者的报告。

返回：
1. 一句话解释
2. 通俗摘要
3. 目标用户
4. 三个关键亮点
5. 视觉 Demo 潜力
6. 为什么它正在受到关注
7. 类似工具或竞品
8. 风险和限制
9. 事实核查备注
10. 它适合短视频、长文章，还是两者都适合
```

### 10.2 评分提示词

```text
你是 AI 内容编辑。
请评估这个条目的短视频潜力。

从 1 到 10 评分：
- 新颖性
- 时效性
- 视觉潜力
- 解释难度
- 受众相关性
- 标题潜力
- 商业价值
- 技术可信度
- 讨论潜力

然后给出：
- 总分
- 推荐结论
- 最适合平台
- 最适合内容形式
- 推荐理由
```

### 10.3 短视频脚本提示词

```text
你是抖音科技短视频脚本作者。
基于选定 AI 项目写一条 90 秒脚本。

结构：
0-3 秒：强钩子
3-15 秒：它是什么
15-45 秒：三个关键亮点
45-70 秒：使用场景和机会
70-85 秒：限制或事实核查提醒
85-90 秒：结尾和关注提示

风格：
- 非技术用户也能听懂
- 不夸大
- 口语化
- 适合口播
```

### 10.4 分镜提示词

```text
你是短视频导演。
把这段脚本转换成分镜。

每个镜头包含：
- 时间范围
- 画面内容
- 屏幕字幕
- 素材类型
- 剪辑备注
- 是否需要屏幕录制、Demo 录制、生成图或图表
```

## 11. 质量控制规则

系统必须避免低可信度 AI 内容。

规则：

- 没有来源信号支撑时，不要声称某个项目正在流行。
- 不要编造 star 数、融资、用户、基准测试或作者背景。
- 保持事实核查备注可见。
- 证据不完整时，优先使用“可能”“看起来”“基于 README”等谨慎措辞。
- 区分项目自称能力和已验证行为。
- 始终标记缺少 Demo、许可证不清晰、仓库不活跃和安装困难。

## 12. 产品化策略

最适合的第一产品：

> AI 技术创作者工作台：从 GitHub 项目链接到选题评分、短视频脚本、文章草稿和分镜。

为什么它适合作为第一产品：

- 目标用户清晰。
- 具备强日常使用场景。
- 可以通过自己的内容生产快速验证。
- 一开始不需要完整视频自动化。
- 每个模块后续都可以成为独立付费功能。

潜在独立产品：

- Daily AI Trend Radar
- GitHub Project Reader
- AI Content Topic Ranker
- AI Short Video Script Writer
- AI Article Writer
- AI Storyboard Director
- AI Visual Asset Planner

## 13. 下一步行动

1. 确定首个目标平台：只做抖音，还是抖音加微信公众号/Bilibili。
2. 确定首个来源：推荐 GitHub Trending。
3. 手动创建 5 个示例内容项。
4. 在这些样本上跑完整手动提示词流水线。
5. 对比生成脚本和可发布的人类编辑脚本。
6. 锁定共享 JSON Schema。
7. 围绕 GitHub 项目输入构建第一个半自动 MVP。
