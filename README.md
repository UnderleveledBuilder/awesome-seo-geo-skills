<!-- 本文件由 scripts/build.py 生成，请勿手改。要改内容请编辑 data/ 或 templates/ 后重新生成。 -->

# Awesome SEO & GEO Skills

**中文** · [English](README.en.md)

> SEO 和 GEO Skill（技能包）精选：关键词研究、内容优化、技术 SEO 审计、排名监测，以及让 ChatGPT、Perplexity、Google AI 概览、豆包、元宝、Kimi 这些 AI 回答引用你的 GEO（生成式引擎优化）。装进 Claude Code、Codex、龙虾（OpenClaw）、千问、豆包、WorkBuddy 等智能体就能用。
>
> A curated list of agent skills for SEO and GEO (generative engine optimization): keyword research, content optimization, technical audits, rank tracking and AI search visibility.

这里收录给 AI 智能体（agent）用的 SEO 和 GEO skill。SEO 是让搜索引擎把你排在前面；GEO 是让 AI 回答提到和引用你。大多是标准 SKILL.md 格式，支持技能的智能体都能装，装法见[常见问题](#faq)。每个项目都经过人工核对，收录前用脚本做过安全检查，按要干的活和针对的搜索引擎、AI 平台整理。中文 AI 搜索（豆包、元宝、Kimi、DeepSeek、千问）单独成一节。

收录 76 个 skill 项目 + 5 个 MCP 和命令行工具 · 元数据更新于 2026-10-19

**图例**：🌟 精选 · 📝 提示词文件（非标准 skill）· 🔌 MCP 或命令行工具 · 🧩 完整应用 · 💤 超过 180 天未更新 · 📦 已归档 · ⚠️ 仓库失效

**让 agent 帮你挑**：这份清单也是一个 skill。运行 `npx skills add UnderleveledBuilder/awesome-seo-geo-skills` 装上 seo-geo-skill-finder，再问你的 agent「我的网站想被 ChatGPT 和豆包引用，装哪个 skill？」。

> [!NOTE]
> 「人工核对」指核对过仓库说明、目录结构和分类，不等于实测过效果。「安全检查」是用脚本查二进制和压缩包、安装钩子、远程执行和读敏感文件，并列出脚本里的联网地址；查不到不等于安全。

## 目录

- [本周新增](#new)（0）
- [按类型](#by-group)
  - [全套：审计 → 关键词 → 内容 → 技术 → 监测](#group-pipeline)（15）
  - [GEO：让 AI 回答引用你](#group-geo)（20）
  - [中文 AI 搜索：豆包、元宝、Kimi、DeepSeek、千问](#group-cn-ai)（5）
  - [关键词、竞品和排名数据](#group-research)（5）
  - [内容写作和优化](#group-content)（9）
  - [技术 SEO 和站点审计](#group-technical)（11）
  - [本地、电商和应用商店](#group-local)（7）
  - [外链、PR 和站外提及](#group-offsite)（4）
  - [MCP 和命令行工具（不是 skill）](#group-mcp)（5）
- [按搜索引擎和 AI 平台查找](#by-engines)
- [常见问题](#faq)
- [相关资源](#resources)
- [收录徽章](#badge)

<a id="new"></a>
## 本周新增

本周暂无新增。发现好项目欢迎[推荐](../../issues/new?template=submit-skill.yml)。

<a id="by-group"></a>
## 按类型

<a id="group-pipeline"></a>
### 全套：审计 → 关键词 → 内容 → 技术 → 监测

一套 skill 覆盖 SEO 的大部分环节，有的连 GEO 也包了。

- 🌟 **[marketingskills](https://github.com/coreyhaines31/marketingskills)** · ★ 55.5k<br>Corey Haines 的营销 skill 合集：转化优化、文案、SEO 和 AI 搜索优化、数据分析、增长，SEO 部分有审计、程序化页面和结构化数据<br><sub>针对：Google · Google AI 概览 · ChatGPT · Perplexity</sub><br><sub>更新于 2026-10-19 · 英文 · 51 个 skill · MIT</sub>

- 🌟 **[claude-seo](https://github.com/AgriciDaniel/claude-seo)** · ★ 19.3k<br>Claude Code 的 SEO 全家桶：26 个子 skill、19 个专家 agent 并行查技术 SEO、E-E-A-T、结构化数据和 GEO<br><sub>针对：Google · Google AI 概览 · Bing · ChatGPT · Perplexity · Gemini</sub><br><sub>更新于 2026-10-04 · 英文 · 33 个 skill · MIT</sub>

- **[notfair-plugin](https://github.com/nowork-studio/notfair-plugin)** · ★ 4k<br>NotFair 的 SEO、GEO 和营销 skill：审计网站、查流量下滑、分析 GA4 和 Search Console、找各平台广告的浪费<br><sub>针对：Google · Google AI 概览 · ChatGPT · Perplexity · Gemini</sub><br><sub>更新于 2026-10-19 · 英文 · 48 个 skill · MIT</sub>

- **[aaron-marketing-skills](https://github.com/aaron-he-zhu/aaron-marketing-skills)** · ★ 3k<br>Aaron 的 120 个营销 skill，其中 16 个管 SEO 和 GEO，另有叙事、社媒、邮件、投放、达人和发布，可装成插件或 8 个 bot 的团队<br><sub>针对：通用</sub><br><sub>更新于 2026-10-19 · 多语言 · 120 个 skill · Apache-2.0</sub>

- **[marketing-skills](https://github.com/kostja94/marketing-skills)** · ★ 1.1k<br>160 多个营销和 SEO skill：技术和页面 SEO、调研、内容、40 多种页面类型、投放和渠道，按你给的产品资料产出<br><sub>针对：Google</sub><br><sub>更新于 2026-10-06 · 英文 · 9 个 skill · MIT</sub>

- **[Agentic-SEO-Skill](https://github.com/Bhanunamikaze/Agentic-SEO-Skill)** · ★ 975<br>LLM 主导的 SEO 分析 skill：16 个子 skill、10 个专家 agent，89 个脚本只负责收集证据<br><sub>针对：Google · Google AI 概览 · ChatGPT · Perplexity</sub><br><sub>更新于 2026-10-14 · 英文 · MIT</sub>

- **[fire-your-seo-agency](https://github.com/leopard627/fire-your-seo-agency)** · ★ 847<br>替你干 SEO/GEO 代运营的活：按公开标准和清单自己审计、优化 SEO、AEO、GEO，也管韩国 Naver 搜索<br><sub>针对：Google · Google AI 概览 · Bing · ChatGPT · Perplexity</sub><br><sub>更新于 2026-09-25 · 多语言 · MIT</sub>

- **[qiaomu-seo](https://github.com/joeseesun/qiaomu-seo)** · ★ 455<br>乔木的 SEO skill：按真实搜索链路排查收录、渲染、canonical、内链和搜索表现，做关键词页面策略、流量诊断、改版迁移和效果验证<br><sub>针对：Google · Google AI 概览 · Bing · ChatGPT · Perplexity</sub><br><sub>更新于 2026-08-03 · 中文 · MIT</sub>

- **[open-seo-advisor-skill](https://github.com/mars-tw/open-seo-advisor-skill)** · ★ 350<br>繁体中文 SEO 顾问 skill：蒸馏权威方法论，给任何行业做 SEO 健检、修复和内容产出，不绑定厂商<br><sub>针对：Google</sub><br><sub>更新于 2026-09-23 · 中文 · Apache-2.0</sub>

- **[7deer_skills](https://github.com/kennyzir/7deer_skills)** · ★ 326<br>做 Roblox 游戏攻略站的 33 个 skill：判断游戏值不值得做、关键词研究、建站规划、SEO 质检、持续更新和找外链<br><sub>针对：Google</sub><br><sub>更新于 2026-09-29 · 中文 · 33 个 skill · MIT</sub>

- **[beyondseo](https://github.com/beyondtahir/beyondseo)** · ★ 188<br>自带爬虫的 SEO 全套：SEO/AEO/GEO、内容、竞品和口碑，附 206 个带 DR 的发稿渠道和外链计划，本体不要 API Key<br><sub>针对：Google · ChatGPT</sub><br><sub>更新于 2026-09-24 · 英文 · MIT</sub>

- **[seo-god](https://github.com/AKCodez/seo-god)** · ★ 116<br>让 Claude Code 每天给自己的网站做 SEO：本地爬站、在你的仓库里修问题、读 Search Console 和前一天对比，定时跑<br><sub>针对：Google</sub><br><sub>更新于 2026-08-03 · 英文 · MIT</sub>

- **[ultimate-seo-geo](https://github.com/mykpono/ultimate-seo-geo)** · ★ 92<br>SEO 加 GEO 的全站审计：打分的问题清单、可直接部署的修复、结构化数据、E-E-A-T 评估，导出 HTML、Excel 或 PDF<br><sub>针对：Google · Google AI 概览 · ChatGPT · Perplexity · Gemini</sub><br><sub>更新于 2026-10-01 · 英文 · 2 个 skill · MIT</sub>

- **[akii-seo-ai-search-optimizer](https://github.com/akii-technologies-ltd/akii-seo-ai-search-optimizer)** · ★ 76<br>Akii 的免费 SEO/AEO/GEO 插件：审计、改内容、生成结构化数据，追踪在 ChatGPT、Claude 等 AI 里的可见度<br><sub>针对：Google · Google AI 概览 · ChatGPT · Perplexity · Gemini · Claude</sub><br><sub>更新于 2026-10-15 · 英文 · 12 个 skill · MIT</sub>

- **[seojuice-skills](https://github.com/calm-north/seojuice-skills)** · ★ 21<br>SEOJuice 出的 14 个 SEO skill：全面审计、速度、关键词策略、内链、内容找回、超越竞品和 AI 可见度<br><sub>针对：Google · Google AI 概览 · ChatGPT · Perplexity · Gemini</sub><br><sub>更新于 2026-02-27 💤 · 英文 · 14 个 skill · MIT</sub>


<details><summary>安装命令</summary>

```bash
# 默认命令基于 skills CLI，未逐个验证，以各仓库 README 为准
# marketingskills
npx skills add coreyhaines31/marketingskills
# claude-seo
npx skills add AgriciDaniel/claude-seo
# notfair-plugin
npx skills add nowork-studio/notfair-plugin
# aaron-marketing-skills
npx skills add aaron-he-zhu/aaron-marketing-skills
# marketing-skills
npx skills add kostja94/marketing-skills
# Agentic-SEO-Skill
npx skills add Bhanunamikaze/Agentic-SEO-Skill
# fire-your-seo-agency
npx skills add leopard627/fire-your-seo-agency
# qiaomu-seo
npx skills add joeseesun/qiaomu-seo
# open-seo-advisor-skill
npx skills add mars-tw/open-seo-advisor-skill
# 7deer_skills
npx skills add kennyzir/7deer_skills
# beyondseo
npx skills add beyondtahir/beyondseo
# seo-god
npx skills add AKCodez/seo-god
# ultimate-seo-geo
npx skills add mykpono/ultimate-seo-geo
# akii-seo-ai-search-optimizer
npx skills add akii-technologies-ltd/akii-seo-ai-search-optimizer
# seojuice-skills
npx skills add calm-north/seojuice-skills
```

</details>

<a id="group-geo"></a>
### GEO：让 AI 回答引用你

GEO（生成式引擎优化）是让 ChatGPT、Perplexity、Google AI 概览这类 AI 回答提到和引用你的网站：查 AI 可见度、改内容结构、写 llms.txt。

- 🌟 **[geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude)** · ★ 11.1k<br>GEO 优先的 SEO skill：可引用度打分、AI 爬虫访问分析、品牌权威、结构化数据，按 ChatGPT、Perplexity 等平台分别优化<br><sub>针对：Google · Google AI 概览 · ChatGPT · Perplexity · Gemini · Claude</sub><br><sub>更新于 2026-10-19 · 英文 · 16 个 skill · MIT</sub>

- **[opc-skills](https://github.com/ReScienceLab/opc-skills)** · ★ 1.9k<br>一人公司 skill 合集：seo-geo 做 SEO 和 GEO，另有找域名、做 banner 和 logo、Reddit 和 X 调研<br><sub>针对：Google · ChatGPT · Perplexity · Gemini</sub><br><sub>更新于 2026-10-19 · 英文 · 12 个 skill · Apache-2.0</sub>

- **[gtm-engineer-skills](https://github.com/onvoyage-ai/gtm-engineer-skills)** · ★ 1.3k<br>GTM 工程师 skill：网站 AEO/GEO 体检、内容审计、做外链和资源页、品牌 DNA、关键词和提示词聚类，每个 skill 交付一份具体产出<br><sub>针对：Google · Google AI 概览 · ChatGPT · Perplexity · Claude</sub><br><sub>更新于 2026-10-11 · 英文 · 12 个 skill · MIT</sub>

- **[geo-optimizer-skill](https://github.com/Auriti-Labs/geo-optimizer-skill)** · ★ 1.1k<br>开源 AEO/GEO 工具：一条命令给网站打 0–100 分，看 ChatGPT、Perplexity 等 AI 能否抓取、读懂并引用你，再列出要改的地方<br><sub>针对：Google · Google AI 概览 · ChatGPT · Perplexity · Gemini · Claude</sub><br><sub>更新于 2026-10-19 · 英文 · MIT</sub>

- **[geolook](https://github.com/aigclink/geolook)** · ★ 777<br>开源 GEO 实施平台：针对一个项目做现状分析、诊断、策略、拆工单、执行和验证，可自己部署，附 skill<br><sub>针对：百度 · ChatGPT · Perplexity · Gemini · Claude · 豆包 · Kimi · DeepSeek</sub><br><sub>更新于 2026-08-10 · 多语言 · MIT</sub>

- **[elmo](https://github.com/elmohq/elmo)** · ★ 470<br>开源 AI 可见度平台：追踪 ChatGPT、Claude、Perplexity、AI 概览等怎么提到和引用你的品牌，附 aeo skill<br><sub>针对：Google AI 概览 · ChatGPT · Perplexity · Gemini · Claude</sub><br><sub>更新于 2026-10-19 · 英文 · 3 个 skill · MIT</sub><br><sub>💡 追踪功能要自己部署 Elmo</sub>

- **[recomby-geo](https://github.com/ViryaZheng/recomby-geo)** · ★ 459<br>GEO 的 AI 员工方案：GEO skill 包（内容写作、质量审核、GEO 流程）加上一份 agent 和办公 CLI 清单，零 API Key<br><sub>针对：通用</sub><br><sub>更新于 2026-07-04 · 中文 · 9 个 skill · MIT</sub>

- **[voyage-geo-agent](https://github.com/onvoyage-ai/voyage-geo-agent)** · ★ 385<br>开源 GEO 命令行：研究你的品牌和竞品，向 ChatGPT、Claude、Gemini、Perplexity、DeepSeek 等提问，统计谁被提到和推荐<br><sub>针对：ChatGPT · Perplexity · Gemini · Claude · DeepSeek</sub><br><sub>更新于 2026-02-24 💤 · 英文 · 3 个 skill · MIT</sub><br><sub>💡 向各家模型提问要它们的 API Key</sub>

- **[geo-score](https://github.com/jianruntech/geo-score)** · ★ 318<br>开源 GEO 打分：按公开评分标准给网站打 0–100 分，再用你自己的 OpenAI、Perplexity、Gemini 等 Key 每周追踪 AI 引用<br><sub>针对：ChatGPT · Perplexity · Gemini · Claude</sub><br><sub>更新于 2026-10-19 · 英文 · MIT</sub>

- **[geo-first-principles](https://github.com/ALLENLION35/geo-first-principles)** · ★ 305<br>给企业负责人的 GEO 判断：从行业竞争、客户需求和成交逻辑出发，判断该不该做 GEO、价值在哪、怎么投入，附五题实测指引<br><sub>针对：通用</sub><br><sub>更新于 2026-09-14 · 中文 · MIT</sub>

- **[geoptimize](https://github.com/cucuwang/geoptimize)** · ★ 299<br>内容质量检查（原 aeoptimize）：在 CI 里做确定性的 GEO 就绪度扫描，发布前拦下退步，另有生成、改写和 SEO 实验记录 skill<br><sub>针对：通用</sub><br><sub>更新于 2026-10-19 · 多语言 · 4 个 skill · MIT</sub>

- **[SEO-GEO-AEO-Skill](https://github.com/SNLabat/SEO-GEO-AEO-Skill)** · ★ 248<br>一个 skill 审三样：传统 SEO（Google、Bing）、GEO（Perplexity、ChatGPT 搜索、AI 概览）和 AEO 答案引擎优化<br><sub>针对：Google · Google AI 概览 · Bing · ChatGPT · Perplexity · Gemini</sub><br><sub>更新于 2026-03-13 💤 · 英文</sub>

- **[GEO-Content-Optimizer-Skill](https://github.com/liangdabiao/GEO-Content-Optimizer-Skill)** · ★ 212<br>GEO 工具箱：三个从轻到重的 skill，给单篇文章或整站做 AI 引用优化，让 ChatGPT、豆包、Perplexity 回答时提到你<br><sub>针对：Google AI 概览 · ChatGPT · Perplexity · Gemini · 豆包 · Kimi</sub><br><sub>更新于 2026-08-05 · 中文 · 3 个 skill</sub>

- **[GEOHub](https://github.com/yaojingang/GEOHub)** · ★ 164<br>GEO SEO Hub：以 GEO 为主的 skill 集，做发现、诊断、内容、监测和 SEO 规划，结论都标明证据边界，实验版<br><sub>针对：通用</sub><br><sub>更新于 2026-08-31 · 英文 · 9 个 skill · AGPL-3.0</sub>

- **[claude-rank](https://github.com/Houseofmvps/claude-rank)** · ★ 147<br>查网站为什么不被 AI 引用并自动修：10 个扫描器 170 多条规则，自动生成 robots.txt、sitemap、llms.txt 和 JSON-LD<br><sub>针对：Google · Google AI 概览 · Bing · ChatGPT · Perplexity · Gemini · Claude</sub><br><sub>更新于 2026-07-08 · 英文 · 6 个 skill · MIT</sub>

- **[aeo.js](https://github.com/rubenmarcus/aeo.js)** · ★ 144<br>AEO 开发库：生成 llms.txt、robots.txt、sitemap 和 JSON-LD，检查网站对 23 种 AI 爬虫的开放情况，附 skill<br><sub>针对：ChatGPT · Perplexity · Claude</sub><br><sub>更新于 2026-10-06 · 英文</sub>

- **[orangeo-ai-visibility-skill](https://github.com/OranAi-Ltd/orangeo-ai-visibility-skill)** · ★ 141<br>品牌官网 AI 可见度初检：查 AI 爬虫访问、llms.txt、结构化数据和引用信号，找竞品差距，生成买家会问 AI 的问题<br><sub>针对：ChatGPT · Perplexity · Gemini · Claude · DeepSeek</sub><br><sub>更新于 2026-06-09 · 英文 · MIT</sub>

- **[google-ai-search-optimization](https://github.com/deepakness/google-ai-search-optimization)** · ★ 139<br>按 Google 官方指南优化 AI 概览和 AI 模式：可抓取、可收录、有独到价值的内容，做 SEO 审计和改进计划（非官方）<br><sub>针对：Google · Google AI 概览</sub><br><sub>更新于 2026-05-16 · 英文</sub>

- **[geoskills](https://github.com/Cognitic-Labs/geoskills)** · ★ 31<br>6 个 GEO skill：诊断、修复和监测网站在 AI 搜索里的可见度，含 Bing AI 数据分析和竞品对比<br><sub>针对：Google · Bing · ChatGPT · Perplexity · Gemini</sub><br><sub>更新于 2026-10-01 · 英文 · 8 个 skill · Apache-2.0</sub>

- **[seo-skills/geo-audit-skill](https://github.com/seo-skills/geo-audit-skill)** · ★ 29<br>SEOmator 的确定性 GEO 审计：Python 命令行算分、skill 解读，看 AI 爬虫能不能进、段落能不能被直接引用<br><sub>针对：Google AI 概览 · Bing · ChatGPT · Perplexity · Gemini · Claude</sub><br><sub>更新于 2026-09-29 · 英文 · 9 个 skill · MIT</sub>


<details><summary>安装命令</summary>

```bash
# 默认命令基于 skills CLI，未逐个验证，以各仓库 README 为准
# geo-seo-claude
npx skills add zubair-trabzada/geo-seo-claude
# opc-skills
npx skills add ReScienceLab/opc-skills
# gtm-engineer-skills
npx skills add onvoyage-ai/gtm-engineer-skills
# geo-optimizer-skill
npx skills add Auriti-Labs/geo-optimizer-skill
# geolook
npx skills add aigclink/geolook
# elmo
npx skills add elmohq/elmo
# recomby-geo
npx skills add ViryaZheng/recomby-geo
# voyage-geo-agent
npx skills add onvoyage-ai/voyage-geo-agent
# geo-score
npx skills add jianruntech/geo-score
# geo-first-principles
npx skills add ALLENLION35/geo-first-principles
# geoptimize
npx skills add cucuwang/geoptimize
# SEO-GEO-AEO-Skill
npx skills add SNLabat/SEO-GEO-AEO-Skill
# GEO-Content-Optimizer-Skill
npx skills add liangdabiao/GEO-Content-Optimizer-Skill
# GEOHub
npx skills add yaojingang/GEOHub
# claude-rank
npx skills add Houseofmvps/claude-rank
# aeo.js
npx skills add rubenmarcus/aeo.js
# orangeo-ai-visibility-skill
npx skills add OranAi-Ltd/orangeo-ai-visibility-skill
# google-ai-search-optimization
npx skills add deepakness/google-ai-search-optimization
# geoskills
npx skills add Cognitic-Labs/geoskills
# seo-skills/geo-audit-skill
npx skills add seo-skills/geo-audit-skill
```

</details>

<a id="group-cn-ai"></a>
### 中文 AI 搜索：豆包、元宝、Kimi、DeepSeek、千问

针对中文 AI 助手和百度的优化。这几家抓取规则和英文 AI 搜索不一样，比如 GitHub 禁止字节的爬虫抓取，豆包很难直接读到 GitHub 页面，要靠站外内容。

- 🌟 **[yao-geo-skills](https://github.com/yaojingang/yao-geo-skills)** · ★ 889<br>Yao GEO Skills：24 个 GEO skill，管战略诊断、页面技术、内容生产、知识资产、监测归因和拓词，能抓豆包、DeepSeek 的回答<br><sub>针对：百度 · ChatGPT · 豆包 · 元宝 · Kimi · DeepSeek · 千问</sub><br><sub>更新于 2026-10-01 · 多语言 · 24 个 skill · MIT</sub>

- **[geo-doctor](https://github.com/Fangx-AI/geo-doctor)** · ★ 78<br>GEO 医生：查豆包、DeepSeek、ChatGPT、Claude 推荐了哪些竞品、为什么不是你、读了哪些网站，再批量写内容并复查推荐率<br><sub>针对：ChatGPT · Perplexity · Gemini · Claude · 豆包 · 元宝 · Kimi · DeepSeek · 千问</sub><br><sub>更新于 2026-10-19 · 多语言 · MIT</sub>

- **[HeiGe-GEO-SEO](https://github.com/HeiGeAi/HeiGe-GEO-SEO)** · ★ 76<br>中国市场优先的 GEO 加 SEO：让内容被豆包、千问、DeepSeek、文心、元宝和 ChatGPT、Perplexity 抓取引用，零依赖<br><sub>针对：百度 · ChatGPT · Perplexity · Gemini · Claude · 豆包 · 元宝 · DeepSeek · 千问</sub><br><sub>更新于 2026-10-15 · 多语言 · 2 个 skill · MIT</sub>

- **[GEOVisibilityTool](https://github.com/MasashiToda1/GEOVisibilityTool)** · ★ 46<br>测品牌在 AI 搜索里的可见度：生成 30 个测试问题，到 Kimi、豆包、DeepSeek、文心等网页端真问，算可见度分，出报告和投放建议<br><sub>针对：百度 · 豆包 · 元宝 · Kimi · DeepSeek · 千问</sub><br><sub>更新于 2026-06-07 · 中文 · 7 个 skill · Apache-2.0</sub>

- **[geo-automation-skill-pack](https://github.com/noahneancy-byte/geo-automation-skill-pack)** · ★ 38<br>豆包 GEO 自动化：客户诊断、关键词挖掘、写稿，改成头条、搜狐、知乎、36 氪等平台版本，再监测豆包引用并复盘<br><sub>针对：豆包</sub><br><sub>更新于 2026-08-30 · 中文 · 5 个 skill</sub>


<details><summary>安装命令</summary>

```bash
# 默认命令基于 skills CLI，未逐个验证，以各仓库 README 为准
# yao-geo-skills
npx skills add yaojingang/yao-geo-skills
# geo-doctor
npx skills add Fangx-AI/geo-doctor
# HeiGe-GEO-SEO
npx skills add HeiGeAi/HeiGe-GEO-SEO
# GEOVisibilityTool
npx skills add MasashiToda1/GEOVisibilityTool
# geo-automation-skill-pack
npx skills add noahneancy-byte/geo-automation-skill-pack
```

</details>

<a id="group-research"></a>
### 关键词、竞品和排名数据

接真实数据做研究：关键词搜索量、SERP、外链、竞品排名，读 Search Console 和 GA4，追排名、出报告。多数要接第三方数据服务。

- 🌟 **[open-seo](https://github.com/every-app/open-seo)** · ★ 24.2k<br>开源版 Semrush/Ahrefs：关键词研究和聚类、竞品分析、外链挖掘、本地 SEO、站点审计和 AI 可见度，自带给 agent 用的 skill<br><sub>针对：通用</sub><br><sub>更新于 2026-10-19 · 英文 · 27 个 skill · MIT</sub><br><sub>💡 skill 接 OpenSEO：自己部署要 DataForSEO 的 Key（按用量付费），也有托管版</sub>

- **[open-seo-mcp-skills](https://github.com/Ryze-AI-Adgent/open-seo-mcp-skills)** · ★ 6.1k<br>免费 SEO MCP 加开源 SEO/GEO skill：用你真实的 Search Console、GA4 和广告数据做关键词、排名、审计、外链和 AI 可见度<br><sub>针对：Google · ChatGPT · Perplexity · Gemini · Claude</sub><br><sub>更新于 2026-10-13 · 英文 · 8 个 skill · MIT</sub><br><sub>💡 数据经 Ryze 托管的 MCP，用 Google 账号授权</sub>

- **[seo](https://github.com/iannuttall/seo)** · ★ 585<br>SEO 命令行和 MCP：让 agent 读你的 Search Console、GA4 和 Bing 数据，标出 Google 更新日期，带 70 多个审计工具<br><sub>针对：Google · Bing</sub><br><sub>更新于 2026-10-18 · 英文 · Apache-2.0</sub>

- **[seo-skills](https://github.com/seranking/seo-skills)** · ★ 177<br>SE Ranking 官方的 32 个 SEO skill：内容简报、AI 搜索声量、审计、外链缺口、关键词聚类、结构化数据，接它的 MCP<br><sub>针对：Google · Google AI 概览 · ChatGPT · Perplexity · Gemini</sub><br><sub>更新于 2026-06-25 · 英文 · 32 个 skill · MIT</sub><br><sub>💡 要 SE Ranking 的付费账号</sub>

- **[dataforseo-claude](https://github.com/zubair-trabzada/dataforseo-claude)** · ★ 168<br>接 DataForSEO 的 13 个 skill 和 5 个子 agent：关键词、排名追踪、外链审计、技术爬取、竞品分析，出 PDF 报告<br><sub>针对：Google</sub><br><sub>更新于 2026-05-20 · 英文 · 16 个 skill · MIT</sub><br><sub>💡 要 DataForSEO 账号，按量付费</sub>


<details><summary>安装命令</summary>

```bash
# 默认命令基于 skills CLI，未逐个验证，以各仓库 README 为准
# open-seo
npx skills add every-app/open-seo
# open-seo-mcp-skills
npx skills add Ryze-AI-Adgent/open-seo-mcp-skills
# seo
npx skills add iannuttall/seo
# seo-skills
npx skills add seranking/seo-skills
# dataforseo-claude
npx skills add zubair-trabzada/dataforseo-claude
```

</details>

<a id="group-content"></a>
### 内容写作和优化

写和改 SEO 文章、标题和描述、内容简报，按 E-E-A-T 补证据。

- 🌟 **[seomachine](https://github.com/TheCraigHewitt/seomachine)** · ★ 7.5k<br>写 SEO 长文的 Claude Code 工作区：调研、写稿、改写、分析和优化，带竞品对比页、内容策略等 25 个 skill<br><sub>针对：Google</sub><br><sub>更新于 2026-10-15 · 英文 · 25 个 skill · MIT</sub>

- **[claude-blog](https://github.com/AgriciDaniel/claude-blog)** · ★ 2.4k<br>博客写作全套：30 个子 skill、5 个 agent 写、改、审、本地化和更新文章，同时照顾 Google 排名和 AI 引用，交付前过 5 道关<br><sub>针对：Google · Google AI 概览 · ChatGPT · Perplexity · Gemini</sub><br><sub>更新于 2026-10-14 · 英文 · 33 个 skill · MIT</sub>

- **[seo-skills](https://github.com/Illyism/seo-skills)** · ★ 542<br>SEO skill 合集：每日自动检查、改标题标签、更新掉排名的文章、外链、梳理搜索意图、写能排名的文案<br><sub>针对：Google</sub><br><sub>更新于 2026-10-15 · 英文 · 11 个 skill</sub>

- **[superseo-skills](https://github.com/inhouseseo/superseo-skills)** · ★ 361<br>11 个 SEO skill：页面审计、内容简报、写文章、E-E-A-T 审计、语义缺口、外链计划和专家访谈，不要 API Key<br><sub>针对：Google</sub><br><sub>更新于 2026-09-03 · 英文 · 11 个 skill · Apache-2.0</sub>

- **[seobuild-onpage](https://github.com/gbessoni/seobuild-onpage)** · ★ 258<br>一条命令写出能排名的页面：拉当前 SERP、分析排名靠前的内容、找缺口，写成完整页面，兼顾 Google 和 AI 引用<br><sub>针对：Google · Google AI 概览 · ChatGPT · Perplexity · Gemini</sub><br><sub>更新于 2026-10-16 · 英文</sub><br><sub>💡 SERP 和竞品数据来自 DataForSEO，按量付费</sub>

- **[geo-content-writer](https://github.com/dageno-agents/geo-content-writer)** · ★ 216<br>按选题清单逐行生产内容：每一行从调研、写稿到复查，适合团队持续做 GEO 和 SEO 内容，而不是一次性生成<br><sub>针对：通用</sub><br><sub>更新于 2026-07-06 · 多语言 · MIT</sub>

- **[Awesome_SEO_Writing_Skill](https://github.com/flaqai/Awesome_SEO_Writing_Skill)** · ★ 90<br>Flaq AI 的 SEO 写作 skill：两年 SEO 写作、核查、配图和发布经验，另有 LinkedIn、Medium 和公众号版本<br><sub>针对：Google</sub><br><sub>更新于 2026-08-13 · 英文 · 4 个 skill · MIT</sub>

- **[dispatchseo](https://github.com/NeoZi12/dispatchseo)** · ★ 86<br>开源版 SEObot/Outrank：让 agent 当 SEO 经理，做关键词研究、写文章并发布，可以整夜无人值守地批量产出<br><sub>针对：Google</sub><br><sub>更新于 2026-10-15 · 英文 · 2 个 skill · AGPL-3.0</sub><br><sub>💡 配合 DispatchSEO 服务用（可 Docker 自己部署）；无人值守写稿跑在你仓库的 GitHub Actions 里，要存你的 Claude Code 或 OpenAI 凭据</sub>

- **[pseo-skills](https://github.com/lisbeth718/pseo-skills)** · ★ 54<br>程序化 SEO（pSEO）全套：批量页面的数据、发现和审计，另有多语言站、改版迁移、日志分析和内容修剪<br><sub>针对：Google</sub><br><sub>更新于 2026-10-12 · 英文 · 18 个 skill · MIT</sub>


<details><summary>安装命令</summary>

```bash
# 默认命令基于 skills CLI，未逐个验证，以各仓库 README 为准
# seomachine
npx skills add TheCraigHewitt/seomachine
# claude-blog
npx skills add AgriciDaniel/claude-blog
# seo-skills
npx skills add Illyism/seo-skills
# superseo-skills
npx skills add inhouseseo/superseo-skills
# seobuild-onpage
npx skills add gbessoni/seobuild-onpage
# geo-content-writer
npx skills add dageno-agents/geo-content-writer
# Awesome_SEO_Writing_Skill
npx skills add flaqai/Awesome_SEO_Writing_Skill
# dispatchseo
npx skills add NeoZi12/dispatchseo
# pseo-skills
npx skills add lisbeth718/pseo-skills
```

</details>

<a id="group-technical"></a>
### 技术 SEO 和站点审计

爬站审计、结构化数据、站点地图、速度、索引问题。

- 🌟 **[web-quality-skills](https://github.com/addyosmani/web-quality-skills)** · ★ 3k<br>Addy Osmani 的网页质量 skill：按 Lighthouse 和 Core Web Vitals 优化性能、无障碍、最佳实践和 SEO，先测量再改<br><sub>针对：Google</sub><br><sub>更新于 2026-08-24 · 英文 · 6 个 skill · MIT</sub>

- **[seo-ops](https://github.com/tigerless-labs/seo-ops)** · ★ 809<br>SEO 基础检查：给一个网址，像爬虫一样抓取，跑 26 项结构检查，出带证据的通过/不通过报告，不调模型<br><sub>针对：通用</sub><br><sub>更新于 2026-09-01 · 英文 · 2 个 skill</sub>

- **[seo-audit-skill](https://github.com/JeffLi1993/seo-audit-skill)** · ★ 766<br>单页 SEO 审计：给网址出 HTML 报告，脚本做确定性检查、模型判断关键词意图和内容质量，分入门和进阶两档<br><sub>针对：Google</sub><br><sub>更新于 2026-06-17 · 多语言 · 2 个 skill · MIT</sub>

- **[seo-skills/seo-audit-skill](https://github.com/seo-skills/seo-audit-skill)** · ★ 632<br>SEOmator 审计：按 20 类 373 条规则扫网站，含技术 SEO、Core Web Vitals、结构化数据、安全头和 AI 搜索就绪度<br><sub>针对：通用</sub><br><sub>更新于 2026-10-15 · 英文 · 2 个 skill · MIT</sub>

- **[Seo-Promt-Master](https://github.com/umutxyp/Seo-Promt-Master)** · ★ 563<br>把 Google SEO 官方文档做成审计 skill：列出项目的全部公开路由，逐页对照 Google、Bing 和 AI 爬虫的规则检查并修复<br><sub>针对：Google · Bing</sub><br><sub>更新于 2026-10-17 · 英文 · MIT</sub>

- **[seo-geo-audit](https://github.com/dageno-agents/seo-geo-audit)** · ★ 176<br>给品牌、SaaS 团队和代理商的 SEO 加 GEO 审计流程，同时看传统搜索和 AI 搜索<br><sub>针对：Google · Google AI 概览 · Bing · ChatGPT · Perplexity · Gemini</sub><br><sub>更新于 2026-08-19 · 多语言 · MIT</sub>

- **[seo-landing](https://github.com/aleksandr-alhoff/seo-landing)** · ★ 171<br>让 agent 像资深技术 SEO 一样做落地页：PageSpeed 冲 100 分、Core Web Vitals、完整结构化数据、AVIF 图片<br><sub>针对：Google</sub><br><sub>更新于 2026-08-30 · 英文 · MIT</sub>

- **[claude-code-seo](https://github.com/huifer/claude-code-seo)** · ★ 111<br>Next.js 项目的 SEO 助手插件：6 个维度 100 分制审计，管元数据、结构化数据、E-E-A-T、内容策略、本地 SEO 和外链<br><sub>针对：Google</sub><br><sub>更新于 2026-01-04 💤 · 中文 · 12 个 skill · MIT</sub>

- **[jdevalk/skills](https://github.com/jdevalk/skills)** · ★ 107<br>Yoast 创始人 Joost de Valk 的 skill：审计和改进 GitHub 主页、WordPress 插件页、Astro 站 SEO 和文章可读性<br><sub>针对：通用</sub><br><sub>更新于 2026-07-05 · 英文 · 12 个 skill · MIT</sub>

- **[squirrelscan/skills](https://github.com/squirrelscan/skills)** · ★ 101<br>squirrelscan 网站审计的 skill：爬全站，按 SEO、性能、安全、无障碍、内容等 300 多条规则打分，列出能修的问题<br><sub>针对：通用</sub><br><sub>更新于 2026-10-16 · 英文 · 2 个 skill · MIT</sub><br><sub>💡 要装 squirrelscan 命令行并登录，按额度使用</sub>

- **[claude-seo-ai](https://github.com/Hainrixz/claude-seo-ai)** · ★ 77<br>SEO 和 AI 可见度分开打两个分：审计任意网站的传统搜索表现和 GEO/AEO，你同意后自动做安全的修复<br><sub>针对：Google · Google AI 概览 · ChatGPT · Perplexity · Gemini · Claude</sub><br><sub>更新于 2026-09-07 · 英文 · 34 个 skill · MIT</sub>


<details><summary>安装命令</summary>

```bash
# 默认命令基于 skills CLI，未逐个验证，以各仓库 README 为准
# web-quality-skills
npx skills add addyosmani/web-quality-skills
# seo-ops
npx skills add tigerless-labs/seo-ops
# seo-audit-skill
npx skills add JeffLi1993/seo-audit-skill
# seo-skills/seo-audit-skill
npx skills add seo-skills/seo-audit-skill
# Seo-Promt-Master
npx skills add umutxyp/Seo-Promt-Master
# seo-geo-audit
npx skills add dageno-agents/seo-geo-audit
# seo-landing
npx skills add aleksandr-alhoff/seo-landing
# claude-code-seo
npx skills add huifer/claude-code-seo
# jdevalk/skills
npx skills add jdevalk/skills
# squirrelscan/skills
npx skills add squirrelscan/skills
# claude-seo-ai
npx skills add Hainrixz/claude-seo-ai
```

</details>

<a id="group-local"></a>
### 本地、电商和应用商店

地图和本地商家、商品页、应用商店优化（ASO）。

- **[aso-skills](https://github.com/appeeky/aso-skills)** · ★ 2.2k<br>应用商店优化（ASO）和 App 推广的 40 个 skill：关键词研究、元数据优化、竞品分析和市场情报<br><sub>针对：应用商店</sub><br><sub>更新于 2026-10-06 · 英文 · 40 个 skill · MIT</sub><br><sub>💡 数据来自 Appeeky API，要它的 Key</sub>

- **[amazon-sorftime-research-MCP-skill](https://github.com/liangdabiao/amazon-sorftime-research-MCP-skill)** · ★ 998<br>亚马逊选品和竞品分析：单个 Listing 全维度拆解、全品类分析、关键词、差评和市场调研，接 Sorftime、西柚、卖家精灵等 MCP<br><sub>针对：电商站内搜索</sub><br><sub>更新于 2026-10-09 · 中文 · 9 个 skill</sub><br><sub>💡 数据来自 Sorftime 等付费服务</sub>

- **[Amazon-Skills](https://github.com/nexscope-ai/Amazon-Skills)** · ★ 783<br>给亚马逊卖家的 53 个免费 skill：关键词研究、竞品分析、Listing 审计和优化、FBA 计算、PPC 广告<br><sub>针对：电商站内搜索</sub><br><sub>更新于 2026-08-26 · 英文 · 52 个 skill · MIT</sub>

- **[mcp-google-map](https://github.com/cablate/mcp-google-map)** · ★ 473<br>Google 地图给 agent 用：18 个只读工具查地点和路线，走 MCP 或命令行，附本地 SEO skill 查商家在地图搜索里的可见度<br><sub>针对：Google</sub><br><sub>更新于 2026-09-26 · 英文 · 4 个 skill · MIT</sub><br><sub>💡 要 Google Maps Platform 的 API Key</sub>

- **[vibe-aso](https://github.com/Kronop/vibe-aso)** · ★ 457<br>从 Claude Code 做完 iOS 应用的 ASO：关键词研究、最多 50 个语种的商店元数据、本地化截图、全球定价和应用内本地化<br><sub>针对：应用商店</sub><br><sub>更新于 2026-08-12 · 英文 · MIT</sub>

- **[localseoskills](https://github.com/garrettjsmith/localseoskills)** · ★ 128<br>本地 SEO 的 38 个 skill：Google 商家资料、Bing Places、Apple 商家、评价管理、本地排名和 AI 本地搜索<br><sub>针对：Google · Google AI 概览 · Bing</sub><br><sub>更新于 2026-08-15 · 英文 · 39 个 skill · MIT</sub>

- **[app-store-aso](https://github.com/TimBroddin/skills)** · ★ 6<br>苹果 App Store 的 ASO：按 Apple 规范和字数限制写应用名、副标题、描述和关键词，用脚本校验字数，附截图顺序建议<br><sub>针对：应用商店</sub><br><sub>更新于 2026-06-29 · 英文 · 5 个 skill</sub><br><sub>💡 在作者的个人 skill 合集里，只装这一个用上面的命令</sub>


<details><summary>安装命令</summary>

```bash
# 默认命令基于 skills CLI，未逐个验证，以各仓库 README 为准
# aso-skills
npx skills add appeeky/aso-skills
# amazon-sorftime-research-MCP-skill
npx skills add liangdabiao/amazon-sorftime-research-MCP-skill
# Amazon-Skills
npx skills add nexscope-ai/Amazon-Skills
# mcp-google-map
npx skills add cablate/mcp-google-map
# vibe-aso
npx skills add Kronop/vibe-aso
# localseoskills
npx skills add garrettjsmith/localseoskills
# app-store-aso
npx skills add TimBroddin/skills --skill app-store-aso
```

</details>

<a id="group-offsite"></a>
### 外链、PR 和站外提及

AI 回答常引用第三方页面：新闻稿、目录站、论坛和测评。这里是做外链、发新闻稿、争取站外提及的 skill。

- **[newsjack](https://github.com/elvisun/newsjack)** · ★ 1.6k<br>让 agent 当 PR 团队：监测行业新闻找借势机会、核实新闻是否还新、想切入角度、核查事实，按 AI 可见度来写<br><sub>针对：ChatGPT · Claude</sub><br><sub>更新于 2026-10-19 · 英文 · 32 个 skill · MIT</sub>

- **[backlink_skills](https://github.com/flaqai/backlink_skills)** · ★ 788<br>外链提交工作流：外链渠道清单、产品目录提交 skill，先查渠道再按授权提交，遇到验证码交给你，提交后留证据<br><sub>针对：Google</sub><br><sub>更新于 2026-10-15 · 多语言 · 15 个 skill · MIT</sub>

- **[distribb-skill](https://github.com/Bomx/distribb-skill)** · ★ 200<br>Distribb 的 SEO skill：用你自己的 AI 写内容，通过 Distribb 的外链网络发布，另有关键词数据和 Search Console 审计<br><sub>针对：Google</sub><br><sub>更新于 2026-10-11 · 英文 · 2 个 skill</sub><br><sub>💡 Distribb 是付费服务</sub>

- **[qwoted-seo-backlinks-skill](https://github.com/Bomx/qwoted-seo-backlinks-skill)** · ★ 148<br>在 Qwoted 上找记者的求助、做带出处的统计数据页当外链素材，再替你回复记者<br><sub>针对：通用</sub><br><sub>更新于 2026-05-02 · 英文</sub><br><sub>💡 要 Qwoted 账号</sub>


<details><summary>安装命令</summary>

```bash
# 默认命令基于 skills CLI，未逐个验证，以各仓库 README 为准
# newsjack
npx skills add elvisun/newsjack
# backlink_skills
npx skills add flaqai/backlink_skills
# distribb-skill
npx skills add Bomx/distribb-skill
# qwoted-seo-backlinks-skill
npx skills add Bomx/qwoted-seo-backlinks-skill
```

</details>

<a id="group-mcp"></a>
### MCP 和命令行工具（不是 skill）

让 agent 能查 SEO 数据的工具，常和上面的 skill 搭配用。不计入 skill 数。

- **[mcp-gsc](https://github.com/AminForou/mcp-gsc)** · ★ 2k<br>Google Search Console 的 MCP：用自然语言分析你的 SEO 数据，附关键词蚕食、内容机会、收录审计、周报等 skill<br><sub>针对：Google</sub><br><sub>更新于 2026-09-15 · 🔌 MCP · 英文 · 4 个 skill · MIT</sub>

- **[seo-monster](https://github.com/avansaber/seo-monster)** · ★ 556<br>本地运行的 SEO 分析 MCP：用你自己的 Search Console、GA4、PageSpeed 和 Cloudflare 数据回答 SEO 问题<br><sub>针对：Google</sub><br><sub>更新于 2026-10-18 · 🔌 MCP · 英文 · MIT</sub>

- **[mcp-server-typescript](https://github.com/dataforseo/mcp-server-typescript)** · ★ 255<br>DataForSEO 官方 MCP 和命令行：让 agent 查 API 文档并调用关键词、SERP、外链等数据接口<br><sub>针对：Google</sub><br><sub>更新于 2026-10-02 · 🔌 MCP · 英文 · Apache-2.0</sub><br><sub>💡 DataForSEO 按量付费</sub>

- **[seo-audit](https://github.com/houtini-ai/seo-audit)** · ★ 71<br>技术 SEO 审计 MCP：合并 Search Console、自有爬虫、DataForSEO 和 Majestic 的数据，在 Claude 里对话式做审计<br><sub>针对：Google</sub><br><sub>更新于 2026-10-17 · 🔌 MCP · 英文 · Apache-2.0</sub>

- **[mcp-geo](https://github.com/AKzar1el/mcp-geo)** · ★ 38<br>DigestSEO：追踪品牌在 7 个 AI 搜索平台的引用，本地运行，用你自己的各家 API Key<br><sub>针对：Google AI 概览 · ChatGPT · Perplexity · Gemini · Claude</sub><br><sub>更新于 2026-09-24 · 🔌 MCP · 英文 · MIT</sub>


<a id="by-engines"></a>
## 按搜索引擎和 AI 平台查找

仓库说明里明确写了针对哪家（按星数排序）。「通用」是不挑引擎的。

**Google**（49）：[marketingskills](https://github.com/coreyhaines31/marketingskills) · [claude-seo](https://github.com/AgriciDaniel/claude-seo) · [geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) · [seomachine](https://github.com/TheCraigHewitt/seomachine) · [open-seo-mcp-skills](https://github.com/Ryze-AI-Adgent/open-seo-mcp-skills) · [notfair-plugin](https://github.com/nowork-studio/notfair-plugin) · [web-quality-skills](https://github.com/addyosmani/web-quality-skills) · [claude-blog](https://github.com/AgriciDaniel/claude-blog) · [mcp-gsc](https://github.com/AminForou/mcp-gsc) · [opc-skills](https://github.com/ReScienceLab/opc-skills) · [gtm-engineer-skills](https://github.com/onvoyage-ai/gtm-engineer-skills) · [geo-optimizer-skill](https://github.com/Auriti-Labs/geo-optimizer-skill) · [marketing-skills](https://github.com/kostja94/marketing-skills) · [Agentic-SEO-Skill](https://github.com/Bhanunamikaze/Agentic-SEO-Skill) · [fire-your-seo-agency](https://github.com/leopard627/fire-your-seo-agency) · [backlink_skills](https://github.com/flaqai/backlink_skills) · [seo-audit-skill](https://github.com/JeffLi1993/seo-audit-skill) · [seo](https://github.com/iannuttall/seo) · [Seo-Promt-Master](https://github.com/umutxyp/Seo-Promt-Master) · [seo-monster](https://github.com/avansaber/seo-monster) · [seo-skills](https://github.com/Illyism/seo-skills) · [mcp-google-map](https://github.com/cablate/mcp-google-map) · [qiaomu-seo](https://github.com/joeseesun/qiaomu-seo) · [superseo-skills](https://github.com/inhouseseo/superseo-skills) · [open-seo-advisor-skill](https://github.com/mars-tw/open-seo-advisor-skill) · [7deer_skills](https://github.com/kennyzir/7deer_skills) · [seobuild-onpage](https://github.com/gbessoni/seobuild-onpage) · [mcp-server-typescript](https://github.com/dataforseo/mcp-server-typescript) · [SEO-GEO-AEO-Skill](https://github.com/SNLabat/SEO-GEO-AEO-Skill) · [distribb-skill](https://github.com/Bomx/distribb-skill) · [beyondseo](https://github.com/beyondtahir/beyondseo) · [seo-skills](https://github.com/seranking/seo-skills) · [seo-geo-audit](https://github.com/dageno-agents/seo-geo-audit) · [seo-landing](https://github.com/aleksandr-alhoff/seo-landing) · [dataforseo-claude](https://github.com/zubair-trabzada/dataforseo-claude) · [claude-rank](https://github.com/Houseofmvps/claude-rank) · [google-ai-search-optimization](https://github.com/deepakness/google-ai-search-optimization) · [localseoskills](https://github.com/garrettjsmith/localseoskills) · [seo-god](https://github.com/AKCodez/seo-god) · [claude-code-seo](https://github.com/huifer/claude-code-seo) · [ultimate-seo-geo](https://github.com/mykpono/ultimate-seo-geo) · [Awesome_SEO_Writing_Skill](https://github.com/flaqai/Awesome_SEO_Writing_Skill) · [dispatchseo](https://github.com/NeoZi12/dispatchseo) · [claude-seo-ai](https://github.com/Hainrixz/claude-seo-ai) · [akii-seo-ai-search-optimizer](https://github.com/akii-technologies-ltd/akii-seo-ai-search-optimizer) · [seo-audit](https://github.com/houtini-ai/seo-audit) · [pseo-skills](https://github.com/lisbeth718/pseo-skills) · [geoskills](https://github.com/Cognitic-Labs/geoskills) · [seojuice-skills](https://github.com/calm-north/seojuice-skills)

**Google AI 概览**（25）：[marketingskills](https://github.com/coreyhaines31/marketingskills) · [claude-seo](https://github.com/AgriciDaniel/claude-seo) · [geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) · [notfair-plugin](https://github.com/nowork-studio/notfair-plugin) · [claude-blog](https://github.com/AgriciDaniel/claude-blog) · [gtm-engineer-skills](https://github.com/onvoyage-ai/gtm-engineer-skills) · [geo-optimizer-skill](https://github.com/Auriti-Labs/geo-optimizer-skill) · [Agentic-SEO-Skill](https://github.com/Bhanunamikaze/Agentic-SEO-Skill) · [fire-your-seo-agency](https://github.com/leopard627/fire-your-seo-agency) · [elmo](https://github.com/elmohq/elmo) · [qiaomu-seo](https://github.com/joeseesun/qiaomu-seo) · [seobuild-onpage](https://github.com/gbessoni/seobuild-onpage) · [SEO-GEO-AEO-Skill](https://github.com/SNLabat/SEO-GEO-AEO-Skill) · [GEO-Content-Optimizer-Skill](https://github.com/liangdabiao/GEO-Content-Optimizer-Skill) · [seo-skills](https://github.com/seranking/seo-skills) · [seo-geo-audit](https://github.com/dageno-agents/seo-geo-audit) · [claude-rank](https://github.com/Houseofmvps/claude-rank) · [google-ai-search-optimization](https://github.com/deepakness/google-ai-search-optimization) · [localseoskills](https://github.com/garrettjsmith/localseoskills) · [ultimate-seo-geo](https://github.com/mykpono/ultimate-seo-geo) · [claude-seo-ai](https://github.com/Hainrixz/claude-seo-ai) · [akii-seo-ai-search-optimizer](https://github.com/akii-technologies-ltd/akii-seo-ai-search-optimizer) · [mcp-geo](https://github.com/AKzar1el/mcp-geo) · [seo-skills/geo-audit-skill](https://github.com/seo-skills/geo-audit-skill) · [seojuice-skills](https://github.com/calm-north/seojuice-skills)

**Bing**（11）：[claude-seo](https://github.com/AgriciDaniel/claude-seo) · [fire-your-seo-agency](https://github.com/leopard627/fire-your-seo-agency) · [seo](https://github.com/iannuttall/seo) · [Seo-Promt-Master](https://github.com/umutxyp/Seo-Promt-Master) · [qiaomu-seo](https://github.com/joeseesun/qiaomu-seo) · [SEO-GEO-AEO-Skill](https://github.com/SNLabat/SEO-GEO-AEO-Skill) · [seo-geo-audit](https://github.com/dageno-agents/seo-geo-audit) · [claude-rank](https://github.com/Houseofmvps/claude-rank) · [localseoskills](https://github.com/garrettjsmith/localseoskills) · [geoskills](https://github.com/Cognitic-Labs/geoskills) · [seo-skills/geo-audit-skill](https://github.com/seo-skills/geo-audit-skill)

**百度**（4）：[yao-geo-skills](https://github.com/yaojingang/yao-geo-skills) · [geolook](https://github.com/aigclink/geolook) · [HeiGe-GEO-SEO](https://github.com/HeiGeAi/HeiGe-GEO-SEO) · [GEOVisibilityTool](https://github.com/MasashiToda1/GEOVisibilityTool)

**ChatGPT**（36）：[marketingskills](https://github.com/coreyhaines31/marketingskills) · [claude-seo](https://github.com/AgriciDaniel/claude-seo) · [geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) · [open-seo-mcp-skills](https://github.com/Ryze-AI-Adgent/open-seo-mcp-skills) · [notfair-plugin](https://github.com/nowork-studio/notfair-plugin) · [claude-blog](https://github.com/AgriciDaniel/claude-blog) · [opc-skills](https://github.com/ReScienceLab/opc-skills) · [newsjack](https://github.com/elvisun/newsjack) · [gtm-engineer-skills](https://github.com/onvoyage-ai/gtm-engineer-skills) · [geo-optimizer-skill](https://github.com/Auriti-Labs/geo-optimizer-skill) · [Agentic-SEO-Skill](https://github.com/Bhanunamikaze/Agentic-SEO-Skill) · [yao-geo-skills](https://github.com/yaojingang/yao-geo-skills) · [fire-your-seo-agency](https://github.com/leopard627/fire-your-seo-agency) · [geolook](https://github.com/aigclink/geolook) · [elmo](https://github.com/elmohq/elmo) · [qiaomu-seo](https://github.com/joeseesun/qiaomu-seo) · [voyage-geo-agent](https://github.com/onvoyage-ai/voyage-geo-agent) · [geo-score](https://github.com/jianruntech/geo-score) · [seobuild-onpage](https://github.com/gbessoni/seobuild-onpage) · [SEO-GEO-AEO-Skill](https://github.com/SNLabat/SEO-GEO-AEO-Skill) · [GEO-Content-Optimizer-Skill](https://github.com/liangdabiao/GEO-Content-Optimizer-Skill) · [beyondseo](https://github.com/beyondtahir/beyondseo) · [seo-skills](https://github.com/seranking/seo-skills) · [seo-geo-audit](https://github.com/dageno-agents/seo-geo-audit) · [claude-rank](https://github.com/Houseofmvps/claude-rank) · [aeo.js](https://github.com/rubenmarcus/aeo.js) · [orangeo-ai-visibility-skill](https://github.com/OranAi-Ltd/orangeo-ai-visibility-skill) · [ultimate-seo-geo](https://github.com/mykpono/ultimate-seo-geo) · [geo-doctor](https://github.com/Fangx-AI/geo-doctor) · [claude-seo-ai](https://github.com/Hainrixz/claude-seo-ai) · [akii-seo-ai-search-optimizer](https://github.com/akii-technologies-ltd/akii-seo-ai-search-optimizer) · [HeiGe-GEO-SEO](https://github.com/HeiGeAi/HeiGe-GEO-SEO) · [mcp-geo](https://github.com/AKzar1el/mcp-geo) · [geoskills](https://github.com/Cognitic-Labs/geoskills) · [seo-skills/geo-audit-skill](https://github.com/seo-skills/geo-audit-skill) · [seojuice-skills](https://github.com/calm-north/seojuice-skills)

**Perplexity**（33）：[marketingskills](https://github.com/coreyhaines31/marketingskills) · [claude-seo](https://github.com/AgriciDaniel/claude-seo) · [geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) · [open-seo-mcp-skills](https://github.com/Ryze-AI-Adgent/open-seo-mcp-skills) · [notfair-plugin](https://github.com/nowork-studio/notfair-plugin) · [claude-blog](https://github.com/AgriciDaniel/claude-blog) · [opc-skills](https://github.com/ReScienceLab/opc-skills) · [gtm-engineer-skills](https://github.com/onvoyage-ai/gtm-engineer-skills) · [geo-optimizer-skill](https://github.com/Auriti-Labs/geo-optimizer-skill) · [Agentic-SEO-Skill](https://github.com/Bhanunamikaze/Agentic-SEO-Skill) · [fire-your-seo-agency](https://github.com/leopard627/fire-your-seo-agency) · [geolook](https://github.com/aigclink/geolook) · [elmo](https://github.com/elmohq/elmo) · [qiaomu-seo](https://github.com/joeseesun/qiaomu-seo) · [voyage-geo-agent](https://github.com/onvoyage-ai/voyage-geo-agent) · [geo-score](https://github.com/jianruntech/geo-score) · [seobuild-onpage](https://github.com/gbessoni/seobuild-onpage) · [SEO-GEO-AEO-Skill](https://github.com/SNLabat/SEO-GEO-AEO-Skill) · [GEO-Content-Optimizer-Skill](https://github.com/liangdabiao/GEO-Content-Optimizer-Skill) · [seo-skills](https://github.com/seranking/seo-skills) · [seo-geo-audit](https://github.com/dageno-agents/seo-geo-audit) · [claude-rank](https://github.com/Houseofmvps/claude-rank) · [aeo.js](https://github.com/rubenmarcus/aeo.js) · [orangeo-ai-visibility-skill](https://github.com/OranAi-Ltd/orangeo-ai-visibility-skill) · [ultimate-seo-geo](https://github.com/mykpono/ultimate-seo-geo) · [geo-doctor](https://github.com/Fangx-AI/geo-doctor) · [claude-seo-ai](https://github.com/Hainrixz/claude-seo-ai) · [akii-seo-ai-search-optimizer](https://github.com/akii-technologies-ltd/akii-seo-ai-search-optimizer) · [HeiGe-GEO-SEO](https://github.com/HeiGeAi/HeiGe-GEO-SEO) · [mcp-geo](https://github.com/AKzar1el/mcp-geo) · [geoskills](https://github.com/Cognitic-Labs/geoskills) · [seo-skills/geo-audit-skill](https://github.com/seo-skills/geo-audit-skill) · [seojuice-skills](https://github.com/calm-north/seojuice-skills)

**Gemini**（27）：[claude-seo](https://github.com/AgriciDaniel/claude-seo) · [geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) · [open-seo-mcp-skills](https://github.com/Ryze-AI-Adgent/open-seo-mcp-skills) · [notfair-plugin](https://github.com/nowork-studio/notfair-plugin) · [claude-blog](https://github.com/AgriciDaniel/claude-blog) · [opc-skills](https://github.com/ReScienceLab/opc-skills) · [geo-optimizer-skill](https://github.com/Auriti-Labs/geo-optimizer-skill) · [geolook](https://github.com/aigclink/geolook) · [elmo](https://github.com/elmohq/elmo) · [voyage-geo-agent](https://github.com/onvoyage-ai/voyage-geo-agent) · [geo-score](https://github.com/jianruntech/geo-score) · [seobuild-onpage](https://github.com/gbessoni/seobuild-onpage) · [SEO-GEO-AEO-Skill](https://github.com/SNLabat/SEO-GEO-AEO-Skill) · [GEO-Content-Optimizer-Skill](https://github.com/liangdabiao/GEO-Content-Optimizer-Skill) · [seo-skills](https://github.com/seranking/seo-skills) · [seo-geo-audit](https://github.com/dageno-agents/seo-geo-audit) · [claude-rank](https://github.com/Houseofmvps/claude-rank) · [orangeo-ai-visibility-skill](https://github.com/OranAi-Ltd/orangeo-ai-visibility-skill) · [ultimate-seo-geo](https://github.com/mykpono/ultimate-seo-geo) · [geo-doctor](https://github.com/Fangx-AI/geo-doctor) · [claude-seo-ai](https://github.com/Hainrixz/claude-seo-ai) · [akii-seo-ai-search-optimizer](https://github.com/akii-technologies-ltd/akii-seo-ai-search-optimizer) · [HeiGe-GEO-SEO](https://github.com/HeiGeAi/HeiGe-GEO-SEO) · [mcp-geo](https://github.com/AKzar1el/mcp-geo) · [geoskills](https://github.com/Cognitic-Labs/geoskills) · [seo-skills/geo-audit-skill](https://github.com/seo-skills/geo-audit-skill) · [seojuice-skills](https://github.com/calm-north/seojuice-skills)

**Claude**（18）：[geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) · [open-seo-mcp-skills](https://github.com/Ryze-AI-Adgent/open-seo-mcp-skills) · [newsjack](https://github.com/elvisun/newsjack) · [gtm-engineer-skills](https://github.com/onvoyage-ai/gtm-engineer-skills) · [geo-optimizer-skill](https://github.com/Auriti-Labs/geo-optimizer-skill) · [geolook](https://github.com/aigclink/geolook) · [elmo](https://github.com/elmohq/elmo) · [voyage-geo-agent](https://github.com/onvoyage-ai/voyage-geo-agent) · [geo-score](https://github.com/jianruntech/geo-score) · [claude-rank](https://github.com/Houseofmvps/claude-rank) · [aeo.js](https://github.com/rubenmarcus/aeo.js) · [orangeo-ai-visibility-skill](https://github.com/OranAi-Ltd/orangeo-ai-visibility-skill) · [geo-doctor](https://github.com/Fangx-AI/geo-doctor) · [claude-seo-ai](https://github.com/Hainrixz/claude-seo-ai) · [akii-seo-ai-search-optimizer](https://github.com/akii-technologies-ltd/akii-seo-ai-search-optimizer) · [HeiGe-GEO-SEO](https://github.com/HeiGeAi/HeiGe-GEO-SEO) · [mcp-geo](https://github.com/AKzar1el/mcp-geo) · [seo-skills/geo-audit-skill](https://github.com/seo-skills/geo-audit-skill)

**豆包**（7）：[yao-geo-skills](https://github.com/yaojingang/yao-geo-skills) · [geolook](https://github.com/aigclink/geolook) · [GEO-Content-Optimizer-Skill](https://github.com/liangdabiao/GEO-Content-Optimizer-Skill) · [geo-doctor](https://github.com/Fangx-AI/geo-doctor) · [HeiGe-GEO-SEO](https://github.com/HeiGeAi/HeiGe-GEO-SEO) · [GEOVisibilityTool](https://github.com/MasashiToda1/GEOVisibilityTool) · [geo-automation-skill-pack](https://github.com/noahneancy-byte/geo-automation-skill-pack)

**腾讯元宝**（4）：[yao-geo-skills](https://github.com/yaojingang/yao-geo-skills) · [geo-doctor](https://github.com/Fangx-AI/geo-doctor) · [HeiGe-GEO-SEO](https://github.com/HeiGeAi/HeiGe-GEO-SEO) · [GEOVisibilityTool](https://github.com/MasashiToda1/GEOVisibilityTool)

**Kimi**（5）：[yao-geo-skills](https://github.com/yaojingang/yao-geo-skills) · [geolook](https://github.com/aigclink/geolook) · [GEO-Content-Optimizer-Skill](https://github.com/liangdabiao/GEO-Content-Optimizer-Skill) · [geo-doctor](https://github.com/Fangx-AI/geo-doctor) · [GEOVisibilityTool](https://github.com/MasashiToda1/GEOVisibilityTool)

**DeepSeek**（7）：[yao-geo-skills](https://github.com/yaojingang/yao-geo-skills) · [geolook](https://github.com/aigclink/geolook) · [voyage-geo-agent](https://github.com/onvoyage-ai/voyage-geo-agent) · [orangeo-ai-visibility-skill](https://github.com/OranAi-Ltd/orangeo-ai-visibility-skill) · [geo-doctor](https://github.com/Fangx-AI/geo-doctor) · [HeiGe-GEO-SEO](https://github.com/HeiGeAi/HeiGe-GEO-SEO) · [GEOVisibilityTool](https://github.com/MasashiToda1/GEOVisibilityTool)

**千问**（4）：[yao-geo-skills](https://github.com/yaojingang/yao-geo-skills) · [geo-doctor](https://github.com/Fangx-AI/geo-doctor) · [HeiGe-GEO-SEO](https://github.com/HeiGeAi/HeiGe-GEO-SEO) · [GEOVisibilityTool](https://github.com/MasashiToda1/GEOVisibilityTool)

**应用商店**（3）：[aso-skills](https://github.com/appeeky/aso-skills) · [vibe-aso](https://github.com/Kronop/vibe-aso) · [app-store-aso](https://github.com/TimBroddin/skills)

**电商站内搜索（亚马逊等）**（2）：[amazon-sorftime-research-MCP-skill](https://github.com/liangdabiao/amazon-sorftime-research-MCP-skill) · [Amazon-Skills](https://github.com/nexscope-ai/Amazon-Skills)

**通用**（12）：[open-seo](https://github.com/every-app/open-seo) · [aaron-marketing-skills](https://github.com/aaron-he-zhu/aaron-marketing-skills) · [seo-ops](https://github.com/tigerless-labs/seo-ops) · [seo-skills/seo-audit-skill](https://github.com/seo-skills/seo-audit-skill) · [recomby-geo](https://github.com/ViryaZheng/recomby-geo) · [geo-first-principles](https://github.com/ALLENLION35/geo-first-principles) · [geoptimize](https://github.com/cucuwang/geoptimize) · [geo-content-writer](https://github.com/dageno-agents/geo-content-writer) · [GEOHub](https://github.com/yaojingang/GEOHub) · [qwoted-seo-backlinks-skill](https://github.com/Bomx/qwoted-seo-backlinks-skill) · [jdevalk/skills](https://github.com/jdevalk/skills) · [squirrelscan/skills](https://github.com/squirrelscan/skills)

<a id="faq"></a>
## 常见问题

### GEO 是什么？和 SEO 有什么区别？

SEO（搜索引擎优化）是让 Google、百度这类搜索引擎把你的网页排在前面。GEO（生成式引擎优化，也叫 AEO）是让 ChatGPT、Perplexity、Google AI 概览、豆包这类 AI 回答提到和引用你。两者有重叠：AI 搜索多半也先去搜索引擎找网页，所以 SEO 做得好是 GEO 的基础；但 AI 更看重能直接摘出来的答案、清楚的出处和被别处提到的次数。专做 GEO 的项目在 [GEO：让 AI 回答引用你](#group-geo)，共 20 个。

### 有哪些好用的 SEO skill？

收录 76 个人工核对过的 SEO 和 GEO skill 项目（数据更新于 2026-10-19）。想一套管到底，先看[全套](#group-pipeline)（15 个），星数最高的是 [marketingskills](https://github.com/coreyhaines31/marketingskills)、[claude-seo](https://github.com/AgriciDaniel/claude-seo)、[notfair-plugin](https://github.com/nowork-studio/notfair-plugin)；只缺某一步，看关键词和排名数据、内容、技术审计、外链各节。

### 想被豆包、元宝、Kimi、DeepSeek 引用，有专门的 skill 吗？

有，但不多。专做中文 AI 搜索的在[中文 AI 搜索](#group-cn-ai)（5 个）；别的分组里也有兼顾豆包、Kimi 的，明确针对豆包的一共 7 个。中文 AI 助手的抓取规则和英文 AI 搜索不一样：比如 GitHub 的 robots.txt 禁止字节的爬虫（Bytespider）抓取，豆包很难直接读到 GitHub 页面，要靠公众号、知乎、头条这类站外内容被引用。按引擎查，见[按搜索引擎和 AI 平台查找](#by-engines)。

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

收录前逐个核对过仓库说明、目录和文件，并用脚本查过二进制和压缩包、安装钩子、远程执行和读敏感文件。收录了 76 个 skill 项目和 5 个工具。看过但没收的，原因逐条记在 [data/ignore.toml](data/ignore.toml)（目前 34 个）。脚本查不到不等于安全，安装前先读一遍它的 `SKILL.md` 和脚本。

### 多久更新一次？

每周一自动刷新星数、最近更新时间和许可证，并搜索新仓库；新仓库人工核对后才收录，见[本周新增](#new)。

<a id="resources"></a>
## 相关资源

- [awesome-social-media-skills](https://github.com/UnderleveledBuilder/awesome-social-media-skills)：自媒体运营 skill 精选，小红书、抖音、公众号、X、YouTube 的选题、写稿、发布和数据
- [awesome-short-drama-skills](https://github.com/UnderleveledBuilder/awesome-short-drama-skills)：AI 短剧 · 漫剧 skill 精选
- [awesome-story-skills](https://github.com/UnderleveledBuilder/awesome-story-skills)：让大模型讲好故事的方法合集
- [anthropics/skills](https://github.com/anthropics/skills)：官方 Agent Skills 仓库，含规范和示例，想自己写 skill 可以从这里看起
- [vercel-labs/skills](https://github.com/vercel-labs/skills)：`npx skills` 安装工具，配套目录 [skills.sh](https://skills.sh)

## 参与贡献

推荐项目可以[提交 issue](../../issues/new?template=submit-skill.yml)，也可以直接改 `data/skills.toml` 发 PR，详见 [CONTRIBUTING.md](CONTRIBUTING.md)。自己写的 SEO 或 GEO skill 也欢迎自荐。

<a id="badge"></a>
## 收录徽章

项目已被收录的作者，可以在自己的 README 里加上这个徽章：

[![收录于 Awesome SEO & GEO Skills](https://img.shields.io/badge/%E6%94%B6%E5%BD%95%E4%BA%8E-Awesome_SEO_%26_GEO_Skills-2da44e)](https://github.com/UnderleveledBuilder/awesome-seo-geo-skills)

```markdown
[![收录于 Awesome SEO & GEO Skills](https://img.shields.io/badge/%E6%94%B6%E5%BD%95%E4%BA%8E-Awesome_SEO_%26_GEO_Skills-2da44e)](https://github.com/UnderleveledBuilder/awesome-seo-geo-skills)
```

## 许可

[CC0 1.0](LICENSE)

---

维护者：X [@UnderleveledDev](https://x.com/UnderleveledDev)
