# 真实运行文档

本文档说明当前模块 1：AI Trend Radar 的真实运行方式。

模块 1 只做用户主动触发的一次性数据收集，不做爬虫、不做定时任务、
不做后台持续采集，也不自动发布内容。

GitHub 来源会默认抓取仓库 README 原文，并按配置截断后写入
`raw_content`。模块 1 只保存 README 文本，不做阅读分析、总结或评分。

## 当前范围

已支持来源：

- GitHub Search
- GitHub Trending
- Hacker News
- arXiv
- Hugging Face
- V2EX

暂不支持：

- 手动粘贴 URL 后点击收集
- 定时采集
- 连续爬虫
- 自动发布

## 环境位置

项目独立虚拟环境位于：

```bash
/Users/liu/ai/InfomationAgents/.venv
```

如果本地没有 `.venv`，先创建：

```bash
python3 -m venv .venv
```

激活环境：

```bash
source .venv/bin/activate
```

安装后端依赖：

```bash
.venv/bin/pip install -e ".[dev]"
```

可选：设置 GitHub Token，降低 GitHub API 限流影响：

```bash
export GITHUB_TOKEN=your_github_token
```

不要提交 token、`.env`、`.venv/`、`data/runs/` 等环境或运行产物。

## CLI 真实运行

查看命令：

```bash
.venv/bin/python -m cli.trend_radar --help
```

查看采集参数：

```bash
.venv/bin/python -m cli.trend_radar collect --help
```

执行一次真实采集：

```bash
.venv/bin/python -m cli.trend_radar collect --limit 5
```

关闭 README 抓取：

```bash
.venv/bin/python -m cli.trend_radar collect --no-fetch-readme --limit 5
```

调整 README 截断长度：

```bash
.venv/bin/python -m cli.trend_radar collect --readme-max-chars 12000 --limit 5
```

指定 GitHub Search 查询词：

```bash
.venv/bin/python -m cli.trend_radar collect --query "AI agent" --limit 10
```

只运行 GitHub Search：

```bash
.venv/bin/python -m cli.trend_radar collect --source github_search --limit 5
```

显式运行所有来源：

```bash
.venv/bin/python -m cli.trend_radar collect \
  --source github_search \
  --source github_trending \
  --source hacker_news \
  --source arxiv \
  --source hugging_face \
  --source v2ex \
  --limit 5
```

成功时会看到类似输出：

```text
Collected 10 items with 0 errors. Saved to data/runs/<run_id>.json
```

实际数量可能少于 `limit * source_count`，例如 GitHub 返回数据不足、
字段不完整，或某个来源出现错误。

## 输出位置

每次运行会在下面目录写入一个 JSON 文件：

```bash
data/runs/
```

输出对象是结构化的 `CollectorRun`。下游模块必须读取这个结构化 JSON，
不要依赖命令行日志里的自然语言。

重要字段：

- `run_id`
- `collected_at`
- `enabled_sources`
- `items`
- `errors`

每条采集结果会保留来源证据：

- `source`
- `source_url`
- `title`
- `raw_content`
- `category`
- `signals`
- `collected_at`

GitHub README 相关信息记录在：

- `raw_content`：README 截断文本；如果抓取失败，则回退为仓库描述。
- `signals.source_specific.readme_fetched`
- `signals.source_specific.readme_truncated`
- `signals.source_specific.readme_size`
- `signals.source_specific.readme_path`

## API 真实运行

启动后端 API：

```bash
.venv/bin/uvicorn api.main:app --reload --port 8000
```

发起一次采集请求：

```bash
curl -X POST http://127.0.0.1:8000/api/trend-radar/collect \
  -H "Content-Type: application/json" \
  -d '{"query":"AI agent","sources":["github_search","github_trending","hacker_news","arxiv","hugging_face","v2ex"],"limit":5,"fetch_readme":true,"readme_max_chars":20000}'
```

响应会包含结构化 `run` 和保存后的 `output_path`。

## 前端真实运行

安装前端依赖：

```bash
cd web
npm install
```

启动前端：

```bash
npm run dev
```

打开终端输出的 Vite 地址，通常是：

```text
http://127.0.0.1:5173/
```

前端默认调用后端：

```text
http://127.0.0.1:8000
```

所以使用前端前，需要先启动后端 API。

## 验证

运行后端测试：

```bash
.venv/bin/pytest -q
```

当前预期结果：

```text
30 passed
```

运行前端构建：

```bash
cd web
npm run build
```

## 常见问题

### `Got unexpected extra argument(s) (collect)`

说明本地代码不是最新版本。拉取最新 `main` 后重试：

```bash
git pull
.venv/bin/python -m cli.trend_radar collect --help
```

### GitHub 限流或 API 报错

设置 `GITHUB_TOKEN` 后重新运行：

```bash
export GITHUB_TOKEN=your_github_token
.venv/bin/python -m cli.trend_radar collect --limit 5
```

### 前端没有数据

先确认后端 API 是否运行在 `8000` 端口。

采集接口是 `POST` 接口：

```text
http://127.0.0.1:8000/api/trend-radar/collect
```

直接在浏览器打开该地址不是有效测试方式。

## 数据规则

- 只做用户主动触发的一次性采集。
- 未更新产品文档前，不新增爬虫行为。
- 不要在没有来源信号支撑时声称某个项目正在流行。
- 保留来源 URL 和采集时间。
- 运行产物不提交到 git。
