### GEO 是什么？和 SEO 有什么区别？

SEO（搜索引擎优化）是让 Google、百度这类搜索引擎把你的网页排在前面。GEO（生成式引擎优化，也叫 AEO）是让 ChatGPT、Perplexity、Google AI 概览、豆包这类 AI 回答提到和引用你。两者有重叠：AI 搜索多半也先去搜索引擎找网页，所以 SEO 做得好是 GEO 的基础；但 AI 更看重能直接摘出来的答案、清楚的出处和被别处提到的次数。专做 GEO 的项目在 [GEO：让 AI 回答引用你](#group-geo)，共 {{group:geo}} 个。

### 有哪些好用的 SEO skill？

收录 {{count}} 个人工核对过的 SEO 和 GEO skill 项目（数据更新于 {{updated}}）。想一套管到底，先看[全套](#group-pipeline)（{{group:pipeline}} 个），星数最高的是 {{top:group:pipeline}}；只缺某一步，看关键词和排名数据、内容、技术审计、外链各节。

### 想被豆包、元宝、Kimi、DeepSeek 引用，有专门的 skill 吗？

有，但不多。专做中文 AI 搜索的在[中文 AI 搜索](#group-cn-ai)（{{group:cn-ai}} 个）；别的分组里也有兼顾豆包、Kimi 的，明确针对豆包的一共 {{facet:engines:doubao}} 个。中文 AI 助手的抓取规则和英文 AI 搜索不一样：比如 GitHub 的 robots.txt 禁止字节的爬虫（Bytespider）抓取，豆包很难直接读到 GitHub 页面，要靠公众号、知乎、头条这类站外内容被引用。按引擎查，见[按搜索引擎和 AI 平台查找](#by-engines)。

### 能装进千问、豆包、龙虾（OpenClaw）、WorkBuddy 这些国产智能体吗？

能。标准 `SKILL.md` 格式的 skill，支持技能的智能体都能装：

- **千问办公**（阿里）：把 skill 文件夹放进 `~/.qwenworkcn/skills/`
- **豆包电脑版**（字节）：在「技能」页面点「+ 添加」，上传 skill 文件夹
- **龙虾 OpenClaw**：`npx skills add 作者/仓库名 -a openclaw`
- **WorkBuddy**（腾讯）：把 skill 文件夹放进 `~/.workbuddy/skills/`
- **Kimi Code、Qwen Code、CodeBuddy、Trae、Qoder**：`npx skills add 作者/仓库名 -a 名字`，名字依次是 `kimi-code-cli`、`qwen-code`、`codebuddy`、`trae`（国内版 `trae-cn`）、`qoder`（国内版 `qoder-cn`）

Claude Code、Codex 用 `npx skills add 作者/仓库名`，每个分组末尾的「安装命令」里有现成命令。

### 要付费的 SEO 数据接口吗？

看项目。只靠模型和网页抓取的 skill 不用；要查关键词搜索量、外链、排名的，多半要接 Search Console（免费）或 Ahrefs、Semrush、DataForSEO 这类付费接口，各条目的说明里写了要什么。

### 这些项目安全吗？

收录前逐个核对过仓库说明、目录和文件，并用脚本查过二进制和压缩包、安装钩子、远程执行和读敏感文件。收录了 {{count}} 个 skill 项目和 {{platforms}} 个工具。看过但没收的，原因逐条记在 [data/ignore.toml](data/ignore.toml)（目前 {{ignored}} 个）。脚本查不到不等于安全，安装前先读一遍它的 `SKILL.md` 和脚本。

### 多久更新一次？

每周一自动刷新星数、最近更新时间和许可证，并搜索新仓库；新仓库人工核对后才收录，见[本周新增](#new)。
