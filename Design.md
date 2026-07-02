---
version: alpha
name: InformationAgents-design-system
description: 面向 AI 内容情报工作台的暖色编辑型界面规范。整体以暖白画布、珊瑚色主按钮、深色产品面板和克制的信息密度为核心，适合展示不同来源的数据、筛选趋势线索、阅读证据和进入下游模块。

colors:
  primary: "#cc785c"
  primary-active: "#a9583e"
  primary-disabled: "#e6dfd8"
  ink: "#141413"
  body: "#3d3d3a"
  body-strong: "#252523"
  muted: "#6c6a64"
  muted-soft: "#8e8b82"
  hairline: "#e6dfd8"
  hairline-soft: "#ebe6df"
  canvas: "#faf9f5"
  surface-soft: "#f5f0e8"
  surface-card: "#efe9de"
  surface-cream-strong: "#e8e0d2"
  surface-dark: "#181715"
  surface-dark-elevated: "#252320"
  surface-dark-soft: "#1f1e1b"
  on-primary: "#ffffff"
  on-dark: "#faf9f5"
  on-dark-soft: "#a09d96"
  accent-teal: "#5db8a6"
  accent-amber: "#e8a55a"
  success: "#5db872"
  warning: "#d4a017"
  error: "#c64545"

typography:
  display-xl:
    fontFamily: "Copernicus, Tiempos Headline, serif"
    fontSize: 64px
    fontWeight: 400
    lineHeight: 1.05
    letterSpacing: -1.5px
  display-lg:
    fontFamily: "Copernicus, Tiempos Headline, serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -1px
  display-md:
    fontFamily: "Copernicus, Tiempos Headline, serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-sm:
    fontFamily: "Copernicus, Tiempos Headline, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.3px
  title-lg:
    fontFamily: "StyreneB, Inter, sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "StyreneB, Inter, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "StyreneB, Inter, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "StyreneB, Inter, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  body-sm:
    fontFamily: "StyreneB, Inter, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "StyreneB, Inter, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  caption-uppercase:
    fontFamily: "StyreneB, Inter, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 1.5px
  code:
    fontFamily: "JetBrains Mono, ui-monospace, monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  button:
    fontFamily: "StyreneB, Inter, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0

rounded:
  xs: 4px
  sm: 6px
  md: 8px
  lg: 12px
  xl: 16px
  pill: 9999px
  full: 9999px

spacing:
  xxs: 4px
  xs: 8px
  sm: 12px
  md: 16px
  lg: 24px
  xl: 32px
  xxl: 48px
  section: 96px
---

# 设计规范

## 1. 设计目标

InformationAgents 是一个工作台型产品，不是营销落地页。界面应帮助用户快速查看来源、判断数据质量、筛选值得继续阅读的条目，并把结构化结果传给下游模块。

设计关键词：

- 清晰、可信、可扫描
- 暖色编辑感，而不是冷色仪表盘
- 数据优先，不做装饰性大图
- 来源证据始终可见
- 适合每天重复使用

## 2. 视觉基调

默认页面使用暖白画布 `#faf9f5`。主操作使用珊瑚色 `#cc785c`。深色面板 `#181715` 用于承载关键数据摘要、代码式结构、运行状态或高优先级信息。

不要把界面做成单一色系。暖白和珊瑚是基底，必须用深色面板、中性色文本、少量青绿或琥珀强调来形成层次。

## 3. 字体和排版

标题可以使用 Copernicus / Tiempos Headline 等衬线显示字体；正文、表格、按钮、标签优先使用 StyreneB / Inter。

规则：

- 工作台内部不要使用过大的营销型标题。
- 表格、侧栏、详情抽屉应使用紧凑字号。
- 正文字重以 400 为主，标签和按钮使用 500。
- 字间距默认为 0；只有展示型标题可使用轻微负字距。
- 代码、JSON 和结构化字段使用 JetBrains Mono 或系统等宽字体。

## 4. 布局原则

模块 1 的主要界面应采用三栏工作台：

```text
来源/筛选栏
  -> 结果列表和运行摘要
  -> 详情和证据面板
```

布局要求：

- 首屏直接显示可操作工作台，不做 landing page。
- 侧栏用于来源筛选和数量统计。
- 中间区域优先展示表格或列表。
- 右侧详情区展示来源 URL、原始内容、signals、eligibility 和 evidence。
- 运行状态和错误信息要靠近数据表，而不是藏在页面底部。
- 移动端可把三栏折叠为纵向结构。

## 5. 颜色使用

### 主色

- `primary #cc785c`：主要按钮、关键 CTA、少量高亮。
- `primary-active #a9583e`：按钮 hover/active。
- `primary-disabled #e6dfd8`：禁用态。

### 背景

- `canvas #faf9f5`：页面底色。
- `surface-soft #f5f0e8`：分区背景。
- `surface-card #efe9de`：卡片、筛选按钮、浅色面板。
- `surface-dark #181715`：深色信息面板、状态面板、代码/JSON 预览。

### 文本

- `ink #141413`：标题和主要文本。
- `body #3d3d3a`：正文。
- `muted #6c6a64`：次要说明、标签。
- `on-dark #faf9f5`：深色面板主文本。
- `on-dark-soft #a09d96`：深色面板次要文本。

### 语义色

- `success #5db872`：成功、可读取、已完成。
- `warning #d4a017`：限制、缺少证据、需要核查。
- `error #c64545`：采集失败、接口错误、字段无效。
- `accent-teal #5db8a6`：辅助状态，不应大量使用。
- `accent-amber #e8a55a`：趋势或重点标签，不应大量使用。

## 6. 组件规范

### 按钮

主按钮使用珊瑚色背景、白色文字、8px 圆角。按钮文案应是明确命令，例如“Collect”“Run”“Export”。不要用大段说明性文字做按钮。

次级按钮使用浅色背景和细边框。图标按钮优先使用常见图标，不要用带文字的圆角矩形替代熟悉符号。

### 来源侧栏

来源侧栏展示：

- All
- GitHub Search
- GitHub Trending
- 后续来源

每个来源显示数量。当前来源使用浅色卡片背景或深色文字强化。不要隐藏 0 数量来源，这有助于判断采集结果是否完整。

### 运行摘要

运行摘要至少展示：

- 状态
- item 数量
- error 数量
- run_id
- output_path

如果存在错误，应明确显示错误来源和消息。

### 结果表格

表格列建议：

- 标题
- 来源
- star 数
- 当日增长
- 语言
- 是否可读

行点击后打开或更新详情面板。长标题需要换行或截断，不允许溢出容器。

### 详情面板

详情面板展示：

- 标题
- 来源 URL
- 原始内容或摘要
- signals
- eligibility
- evidence

来源 URL 必须可复制或可点击。没有证据的字段不要伪装成确定事实。

## 7. 卡片和圆角

卡片圆角一般不超过 8px；只有较大的详情面板或深色产品面板可以使用 12px。不要把页面分区都做成浮动卡片，也不要把卡片嵌套进卡片。

重复项卡片、详情抽屉、模态框可以使用卡片样式。普通页面分区应使用全宽背景带或无框布局。

## 8. 数据可信度表现

界面必须帮助用户区分事实、来源信号和模型判断。

建议视觉规则：

- 来源字段和 URL 靠近标题展示。
- `signals` 使用表格或键值列表。
- `eligibility` 用明确状态色和原因说明。
- `errors` 不隐藏，显示在运行摘要附近。
- 未验证信息使用 muted 文本或 warning 状态。

## 9. 前端约束

- 不做自动轮询。
- 不做定时采集。
- 不做后台爬虫提示。
- 不加入手动 URL 输入，除非产品文档更新。
- 首屏应能读取最近一次 run，或提示用户点击采集。
- 用户点击一次 Collect，只触发一次后端采集。
- 采集结果应按来源清晰分组或筛选。

## 10. 响应式要求

桌面端：

- 三栏布局。
- 表格为主视图。
- 详情面板常驻或抽屉式展示。

平板端：

- 来源栏可横向或折叠。
- 表格和详情上下排列。

移动端：

- 纵向布局。
- 来源筛选使用横向滚动标签。
- 表格可转为紧凑列表。
- 按钮和链接必须易点击。

## 11. 禁止事项

- 不做营销型 hero 页。
- 不使用装饰性渐变球、光斑或纯氛围背景。
- 不把数据藏在大卡片和装饰图后面。
- 不使用单一紫蓝、深蓝、棕橙或米色一把梭的配色。
- 不在没有来源信号时用视觉样式暗示“热门”。
- 不让文字溢出按钮、表格单元格或详情面板。
- 不为了好看而隐藏错误、来源或采集时间。
