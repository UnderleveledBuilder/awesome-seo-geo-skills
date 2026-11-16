<!-- 本文件由 scripts/build.py 生成，请勿手改。要改内容请编辑 data/ 或 templates/ 后重新生成。 -->

# Awesome SEO & GEO Skills

**中文** · [English](README.en.md)

> SEO 和 GEO Skill（技能包）精选：关键词研究、内容优化、技术 SEO 审计、排名监测，以及让 ChatGPT、Perplexity、Google AI 概览、豆包、元宝、Kimi 这些 AI 回答引用你的 GEO（生成式引擎优化）。装进 Claude Code、Codex、龙虾（OpenClaw）、千问、豆包、WorkBuddy 等智能体就能用。
>
> A curated list of agent skills for SEO and GEO (generative engine optimization): keyword research, content optimization, technical audits, rank tracking and AI search visibility.

这里收录给 AI 智能体（agent）用的 SEO 和 GEO skill。SEO 是让搜索引擎把你排在前面；GEO 是让 AI 回答提到和引用你。大多是标准 SKILL.md 格式，支持技能的智能体都能装，装法见[常见问题](#faq)。每个项目都经过人工核对，收录前用脚本做过安全检查，按要干的活和针对的搜索引擎、AI 平台整理。中文 AI 搜索（豆包、元宝、Kimi、DeepSeek、千问）单独成一节。

收录 175 个 skill 项目 + 51 个 MCP 和命令行工具 · 元数据更新于 2026-11-16

**图例**：🌟 精选 · 📝 提示词文件（非标准 skill）· 🔌 MCP 或命令行工具 · 🧩 完整应用 · 💤 超过 180 天未更新 · 📦 已归档 · ⚠️ 仓库失效

**让 agent 帮你挑**：这份清单也是一个 skill。运行 `npx skills add UnderleveledBuilder/awesome-seo-geo-skills` 装上 seo-geo-skill-finder，再问你的 agent「我的网站想被 ChatGPT 和豆包引用，装哪个 skill？」。

> [!NOTE]
> 「人工核对」指核对过仓库说明、目录结构和分类，不等于实测过效果。「安全检查」是用脚本查二进制和压缩包、安装钩子、远程执行和读敏感文件，并列出脚本里的联网地址；查不到不等于安全。

## 目录

- [本周新增](#new)（145）
- [按类型](#by-group)
  - [全套：审计 → 关键词 → 内容 → 技术 → 监测](#group-pipeline)（35）
  - [GEO：让 AI 回答引用你](#group-geo)（42）
  - [中文 AI 搜索：豆包、元宝、Kimi、DeepSeek、千问](#group-cn-ai)（5）
  - [关键词、竞品和排名数据](#group-research)（22）
  - [内容写作和优化](#group-content)（17）
  - [技术 SEO 和站点审计](#group-technical)（35）
  - [本地、电商和应用商店](#group-local)（13）
  - [外链、PR 和站外提及](#group-offsite)（6）
  - [MCP 和命令行工具（不是 skill）](#group-mcp)（48）
  - [相关开源平台（完整应用，不是 skill）](#group-apps)（3）
- [按搜索引擎和 AI 平台查找](#by-engines)
- [常见问题](#faq)
- [相关资源](#resources)
- [收录徽章](#badge)

<a id="new"></a>
## 本周新增

近 7 天新收录 145 个：

- [niubigeo](https://github.com/Albert-Weasker/niubigeo) ★10.3k：NiubiGEO 开源 GEO 研究工具：输入域名，比较各家模型怎么描述你的产品、推荐了谁、引用哪些来源，可以重复测
- [GEOFlow](https://github.com/yaojingang/GEOFlow) ★4.1k：开源 GEO 内容工程和多站分发平台：AI 质检、托管站点、浏览器辅助发布和签名更新，附操作它的 skill
- [growth-lab](https://github.com/tsingyuai/growth-lab) ★2k：开源增长工具：让 Claude Code 或 Codex 跑 SEO 页面闭环（找搜索需求、写页面、复查、看表现），另有公众号文章闭环和多平台内容抓取
- [python-seo-analyzer](https://github.com/sethblack/python-seo-analyzer) ★1.5k：老牌 SEO 分析命令行和 Python 库：爬站、统计正文用词、提示技术 SEO 问题，可选用 Claude 做内容评估
- [LibreCrawl](https://github.com/PhialsBasement/LibreCrawl) ★1.1k：免费的 SEO 爬虫，Screaming Frog 的开源替代：爬站、分析链接、提取 SEO 数据并导出，不用订阅
- [specification.website](https://github.com/jdevalk/specification.website) ★925：Joost de Valk 的网站规范：185 页讲 HTML、无障碍、安全、SEO、agent 就绪该怎么做，每条注出处，skill 和 MCP 供对照
- [bisibility](https://github.com/CorgiCorner/bisibility) ★605：开源 SEO 平台：追踪 Google 排名、研究关键词、查外链，附 20 个 skill 做聚类、竞品、本地 SEO 和 AI 可见度
- [limelit-co/open](https://github.com/limelit-co/open) ★445：自己部署的 AI 可见度追踪（Go 单文件），看 ChatGPT、Claude 等怎么提到你，附查 AI 爬虫和 llms.txt 的 skill
- [OpenGSO](https://github.com/sherwinvishesh/OpenGSO) ★433：让网站对 AI 好读的命令行：打 0–100 分，给每页生成 Markdown 副本和 robots.txt、llms.txt、sitemap
- [GetCito](https://github.com/ai-search-guru/getcito-worlds-first-open-source-aio-aeo-or-geo-tool) ★429：GetCito 开源 AI 搜索优化和可见度追踪平台，附 30 个 skill：答案前置改写、FAQ、竞品对比、引用缺口、内容刷新、错误说法纠正等
- [geo-aeo-tracker](https://github.com/danishashko/geo-aeo-tracker) ★329：开源 AI 可见度追踪和 AEO 检查：看 ChatGPT、Perplexity、Gemini、AI 模式怎么提到你，带 MCP，skill 调它的命令行
- [everyinfra/seo-skills](https://github.com/everyinfra/seo-skills) ★328：免费的全球 SEO/GEO skill：18 个市场入口、56 个脚本，管多语言 GEO、程序化 SEO、Core Web Vitals 和降权恢复
- [yan-skills](https://github.com/yan-labs/yan-skills) ★309：给做 SEO 和独立站的人用的 skill：选词建站到上线增长（rankup）、外链去哪发和是否生效（backlink），另有浏览器取数和生图
- [ansvisor](https://github.com/ansvisor/ansvisor) ★242：开源 AI 搜索执行平台：追踪各家 AI 的可见度，让 agent 把信号变成排好序的动作和修改草稿，附 41 个 skill
- [eGEOagents](https://github.com/mverab/eGEOagents) ★218：开源 GEO/AEO 工具包：内容打分、结构化数据生成、竞品分析、校验修复和 GEO 迭代循环，带命令行和 MCP
- [canonry](https://github.com/Canonry/canonry) ★209：agent 优先的 AEO/GEO 平台：追踪 ChatGPT、Claude、Gemini 的引用，合并 Search Console，再让 agent 写内容
- [codex-seo](https://github.com/zhtyyx/codex-seo) ★157：在 Codex CLI 里做 SEO 审计：26 个子 skill、19 个专家角色，查技术 SEO、结构化数据、GEO、本地和电商，最后给排好优先级的行动计划
- [All-In-One-Free-SEO-Tool](https://github.com/IamRamgarhia/All-In-One-Free-SEO-Tool) ★129：自己部署的免费 SEO 平台：站点审计、排名、关键词、AI 可见度、外链和客户报告，附 5 个 skill 写报告、定关键词、改问题
- [jev-seo](https://github.com/AkashPriyadarshii/jev-seo) ★102：免费的 Rust SEO/GEO 命令行：64 条规则审计、爬站、AI 引用打分、排名漂移、CI 门禁，带 MCP，skill 直接调它
- [screaming-frog-mcp](https://github.com/bzsasson/screaming-frog-mcp) ★96：Screaming Frog SEO Spider 的无界面 MCP：让 agent 跑爬取、导出和分析爬取数据，适合定时审计和 CI
- [vercel-seo-audit](https://github.com/JosephDoUrden/vercel-seo-audit) ★81：查 Next.js 和 Vercel 网站为什么不被 Google 收录：按服务器实际返回查流式元数据、跳转、robots、sitemap 等
- [pagespeed-insights-mcp](https://github.com/ruslanlap/pagespeed-insights-mcp) ★81：Google PageSpeed Insights 和 Chrome 用户体验报告的 MCP：在 agent 里分析、对比和优化网页性能
- [lighthouse-mcp-server](https://github.com/danielsogl/lighthouse-mcp-server) ★75：用 Google Lighthouse 做网页审计的 MCP：13 个以上工具查性能、无障碍、SEO 和安全
- [legends-geogrid](https://github.com/avalonreset/legends-geogrid) ★59：Google 地图排名查询和本地排名追踪：审计 Google 商家资料，出环形网格地图和 18 页本地 SEO PDF 报告
- [OpenGSC](https://github.com/fenjo26/OpenGSC) ★58：自己部署的 Search Console 面板：排名追踪、关键词研究、AI 可见度审计和内容生产，自带 105 个工具的 MCP 和 8 个 skill
- [zens-ink-seo-package](https://github.com/ZensInk/zens-ink-seo-package) ★57：给独立开发者的免费关键词研究工具：20 个命令行查关键词、难度、竞品差距和排名，纯 Python，附 9 个 skill
- [southwellmedia/seo-audit](https://github.com/southwellmedia/seo-audit) ★54：给服务类企业做 SEO 审计和竞品分析，出能直接发给客户的 PDF 提案：关键词、技术和 AI 可见度、内容策略、快速见效项
- [duckduckdeploy/openseo](https://github.com/duckduckdeploy/openseo) ★52：开源版 Ahrefs、Semrush（openseo.gg）：站点审计、关键词、排名、外链、AI 概览和本地排名，附 7 个 skill 走它的 MCP
- [seo-party-skills](https://github.com/every-app/seo-party-skills) ★50：OpenSEO 的实验性 skill：认领 ChatGPT 商家资料、竞品策略、客户搜索词、关键词缺口、高价值页面、AI 排名和拆解别人的 SEO
- [sitewalk](https://github.com/adityaarsharma/sitewalk) ★48：Sitewalk 的开源技术 SEO 审计 MCP：像搜索引擎爬虫一样爬站，给按影响排序的问题和修法、健康分，出 PDF 和 CSV
- [openspider](https://github.com/wojcikdominik/openspider) ★47：面向 agent 的开源网站爬虫和技术 SEO 审计（macOS、Windows），Rust 加 Tauri，自带 MCP，agent 默认只读，开爬要你授权
- [mxfschr/claude-code-seo](https://github.com/mxfschr/claude-code-seo) ★46：Claude Code 的 SEO 系统：26 节知识库加 9 个命令，接 Search Console 和 DataForSEO 实时查蚕食、竞品和见效快的项
- [shopify-theme-audit-skill](https://github.com/tanujrajputdev/shopify-theme-audit-skill) ★45：90 秒审计 Shopify 主题的性能、SEO、AEO 和 GEO：80 多项检查，打分报告，给能直接粘贴的 Liquid 修复代码
- [fat-agent-skill](https://github.com/spruikco/fat-agent-skill) ★40：网站上线后的检查 agent：审计 SEO、AI 爬虫权限、安全、无障碍、性能、本地 SEO 等，再一项项带你修
- [surendranb/google-search-console-mcp](https://github.com/surendranb/google-search-console-mcp) ★40：Google Search Console 的 MCP，附品牌可见度、引用机会、搜索意图分析和搜索外观审计 5 个 skill
- [claude-seo-skill](https://github.com/mangollc/claude-seo-skill) ★39：给代理商用的 SEO/AEO 插件：关键词研究、技术审计、内容优化、本地 SEO、外链和 AI 搜索优化，6 个 skill，不用 API Key
- [seo-ai-link](https://github.com/chenchaoge/seo-ai-link) ★38：独立站外链全流程：挖竞品外链、管外链库、AI 自动发外链、回访收录，配可视化报表，内置作者实测整理的外链库
- [seo-guide-skill](https://github.com/lesishu/seo-guide-skill) ★33：SEO 全流程 skill：网站诊断、页面优化、技术 SEO、内容策略和外链建设
- [contentforge](https://github.com/indranilbanerjee/contentforge) ★33：长文内容生产系统：10 步流程调研、核实、写稿、去 AI 腔、加内链，出可发布的 Word 稿，发布后再查 AI 引用和内容老化
- [google-seo-mcp](https://github.com/Akxan/google-seo-mcp) ★30：SEO/GEO 的 MCP，102 个工具：Search Console、GA4、PageSpeed、结构化数据、AI 爬虫检查，还能改 WordPress
- [agentmarkup](https://github.com/agentmarkup/agentmarkup) ★27：构建时生成 llms.txt、JSON-LD、Markdown 镜像页和 AI 爬虫规则并校验，支持 Vite、Astro、Next.js 等，附 skill
- [local-falcon/mcp](https://github.com/local-falcon/mcp) ★26：Local Falcon 的 MCP：地图网格排名追踪、活动管理、竞品分析，查 Google 地图、苹果地图和 AI 回答里的本地可见度，附 skill
- [aicw-ai-mentions](https://github.com/aichatwatch/aicw-ai-mentions) ★25：命令行和 MCP：追踪 ChatGPT、Claude、Gemini、Grok、Perplexity 怎么提到你和竞品，抽出被引用的链接，出 HTML 报告
- [autoseo](https://github.com/codextde/autoseo) ★25：开源 AI SEO/GEO 平台：追踪品牌在各家 AI 回答里的表现，加关键词研究、排名追踪、站点审计和外链，附 17 个 skill
- [launch-seo-skill](https://github.com/iamjeeth/launch-seo-skill) ★21：网站上线后要做的 10 件 SEO 事：Search Console、GA、robots.txt、sitemap、标题描述、Bing 站长工具等，能改就改
- [yandex-mcp](https://github.com/stufently/yandex-mcp) ★21：Yandex 接口的一组 MCP，94 个工具：搜索、Wordstat 关键词、站长平台、Metrika 和 Direct，附俄语市场选词 skill
- [WorkSmartAI-alt/ai-visibility-monitor](https://github.com/WorkSmartAI-alt/ai-visibility-monitor) ★21：AI 可见度命令行：把买家会问的问题拿去问 ChatGPT、Claude、Perplexity，找你能赢的问题和该写的内容
- [tipsai/product-seo](https://github.com/tipsai/product-seo) ★20：卖产品的网站做 SEO：从 Search Console 数据出发，先挑产品正好能回答的搜索，再改页面、做工具页、清理、站外提及，每项改动定复查日期
- [vinpatel/aeorank](https://github.com/vinpatel/aeorank) ★20：扫描网站的 AI 可见度：12 个维度打 0–100 分，生成 llms.txt 等 8 个给 AI 读的文件，命令行和 GitHub Action
- [99-website](https://github.com/NicoSKOOL/99-website) ★19：用 Claude Code 建 Lighthouse 99 分的 SEO 网站（Astro 加 Cloudflare）：按关键词定结构、配图、审计、部署
- [agent-lighthouse](https://github.com/ForkPoint/agent-lighthouse) ★17：给 AI 用的 Lighthouse：223 项检查，看 ChatGPT、Perplexity、AI 爬虫和 agent 浏览器能否发现、读懂、引用你的网站
- [SoDam-SeoMedic](https://github.com/sodam-ai/SoDam-SeoMedic) ★16：韩语的 SEO/GEO 诊断插件：爬取、渲染、CWV、结构化数据、AI 爬虫策略，接 Search Console 和 GA4，能自动修 Next.js
- [mcp-abilities-rankmath](https://github.com/bjornfix/mcp-abilities-rankmath) ★16：让 agent 通过 MCP 读写 Rank Math 的 SEO 字段：元描述、标题、焦点关键词，基于 WordPress 的 Abilities API
- [seo-signal-skills](https://github.com/daily-growth-signals/seo-signal-skills) ★14：SignalDig 的调研 skill：查关键词需求、相关搜索、SERP、趋势、竞品、GEO 可见度和外链，也查 X、Reddit、小红书、知乎的公开讨论
- [CodoSEO](https://github.com/SafrowLabs/CodoSEO) ★14：Rust 写的开源 SEO/GEO 监测和站点审计，Screaming Frog 和 Ahrefs 站点审计的替代，带 MCP 和审计 skill
- [where-to-submit-your-startup](https://github.com/mmmmingos/where-to-submit-your-startup) ★13：1085 个创业产品提交和发布网站的清单，标了免费、有条件免费、付费和实测问题，skill 让 agent 回答该不该投、怎么投
- [GBP Autopilot](https://github.com/tanzeeldevAi/google-business-profile-ai-automation) ★13：Google 商家资料自动化命令行：按 57 条本地 SEO 规则打分出报告，再通过接口修资料、回评价、每周发帖、设节假日营业时间，资料被改时提醒
- [webappski/aeo-platform](https://github.com/webappski/aeo-platform) ★13：AEO/GEO 命令行：量品牌在 ChatGPT、Claude、Gemini、Perplexity 里的可见度，查 AI 爬虫可抓取性和权威信号
- [seo-utils-skills](https://github.com/seoutilsapp/seo-utils-skills) ★12：SEO Utils 的 MCP 使用指南：教 agent 分清查本地数据、付费查询和写操作，查排名报告、竞品关键词、关键词蚕食时选对工具
- [seo-survival-kit](https://github.com/maxschottke-spec/seo-survival-kit) ★11：电商和 D2C 站的 SEO 恢复工具箱：18 个 skill 管核心更新后的诊断恢复、AI 搜索可见度和引用追踪，出 PDF 报告
- [etsy-listing-helper](https://github.com/silennsong/etsy-listing-helper) ★11：把按需印刷（POD）商品的规格和照片变成 Etsy 上架内容：标题、13 个 SEO 标签、描述、官方类目路径和属性
- [croftweaver](https://github.com/karero/croftweaver) ★10：从简报建出完整网站（Astro、Cloudflare），自带 SEO、结构化数据和测试，上线后按 Search Console 和 AI 提及提示下一步
- [topcited-skills](https://github.com/TopCited/topcited-skills) ★10：TopCited 的 skill：SEO/GEO 知识、调用 TopCited 接口和一套带引导的 AI 可见度排查流程
- [gscdump](https://github.com/harlan-zw/gscdump) ★10：把整个 Search Console 数据导到本地，命令行和 MCP 出 JSON 报告，让 agent 从里面找洞察、改进 SEO
- [seo-night-skill](https://github.com/IncomeStreamSurfer/seo-night-skill) ★10：修 AI 建的网站的 SEO 毛病：审计网站代码，把空泛的标题改成人们真搜的词，补缺的内容，每处改动一个提交，放在待审分支
- [taobao-shop-growth](https://github.com/yuyang2230/taobao-shop-growth) ★10：淘宝千牛小店获客 skill：店铺诊断、改标题、补属性防流量受限、内容引流和批量自动化，方法在一家真实小店上跑通并标了实测结果
- [acamolese/google-search-console-mcp](https://github.com/acamolese/google-search-console-mcp) ★10：Google Search Console 的只读 MCP，17 个工具：快速见效项、点击率缺口、关键词蚕食、流量下滑诊断、收录，还能出白标 HTML 审计报告
- [fiverr-gig-optimizer](https://github.com/waseemnasir2k26/fiverr-gig-optimizer) ★10：Fiverr 服务页优化命令行：给标题、标签、描述打分并给改法，附 Claude Code 命令，离线跑
- [onlymoein/google-search-console-mcp](https://github.com/onlymoein/google-search-console-mcp) ★10：本地跑的 Search Console MCP：搜索数据、按小时数据、网址检查和站点地图，处理好接口的各种坑
- [legends-github](https://github.com/avalonreset/legends-github) ★9：GitHub 仓库的 SEO：审计仓库，按 Google 和 GitHub 的真实搜索需求改描述、话题、README 和社交预览图，再规范发版
- [mcp-web-validator](https://github.com/AKzar1el/mcp-web-validator) ★9：W3C HTML/CSS 校验加技术 SEO 审计的 MCP，DigestSEO 套件之一
- [mcp-yandex-wordstat](https://github.com/askads/mcp-yandex-wordstat) ★9：俄语 Yandex Wordstat 的 MCP：查热门和相似搜索词、需求走势和地区分布，只读
- [seo-aeo-geo-ultimate](https://github.com/oegeyilmaz9/seo-aeo-geo-ultimate) ★8：SEO、AEO、GEO 一整套：一个总入口分派 27 个 skill，审计、技术、内容、外链、本地、电商、AI 搜索，每步留证据
- [pseolint](https://github.com/ouranos-labs/pseolint) ★8：程序化 SEO 发布前的检查：审页面之间的关系而不只是单页，防被 SpamBrain 当成垃圾页，AI 分诊问题，带 MCP
- [AKzar1el/mcp-gsc](https://github.com/AKzar1el/mcp-gsc) ★8：Google Search Console 的 MCP：查点击、展示、排名、网址检查、站点地图和收录，本地跑或部署到 Cloudflare Workers
- [crawlgraph-mcp](https://github.com/pucilpet/crawlgraph-mcp) ★8：CrawlGraph 外链数据接口的 MCP：基于 Common Crawl 网页图查外链、外链变化和竞品外链缺口
- [sudomichael/search-console-mcp](https://github.com/sudomichael/search-console-mcp) ★8：只读的 Search Console MCP：用 Google 账号登录一次就能用，不用建 Google Cloud 项目，令牌只存本机
- [citation-intelligence](https://github.com/AutomateLab-tech/citation-intelligence) ★8：量 AI 引用的 MCP：查 Perplexity、AI 概览、ChatGPT、Claude、Gemini、Bing 对一个问题引用了哪些网址，12 个工具
- [search-os](https://github.com/vamsireddy4/search-os) ★7：一个 skill 管 SEO、AEO、GEO 和 AI 可见度：让网站出现在 Google、Bing、ChatGPT、Perplexity 和 AI 概览里
- [agent-readiness](https://github.com/Canonry/agent-readiness) ★7：开源的 agent 就绪度审计：按 llms.txt、AI 爬虫访问、结构化数据等 16 项打分，给 agent 能直接改的修复清单，离线跑
- [ubersuggest/seo-skills](https://github.com/ubersuggest/seo-skills) ★7：Ubersuggest 官方 SEO skill：关键词研究、竞品、内容简报、找内容需求、站点审计、AI 可见度和行动计划
- [skill-seo-co-ban](https://github.com/ibangtam/skill-seo-co-ban) ★7：越南语 SEO 写作 3 件套：关键词研究、照 Google 前几名列大纲、写带出处的文章，不用付费 SEO 工具
- [literallydotdev/aeo](https://github.com/literallydotdev/aeo) ★7：在本地跑 AI 可见度审计的命令行：看 ChatGPT、Claude、Gemini、Perplexity 会不会提到和引用你，结果可离线核验
- [gsc-mcp](https://github.com/geniushub-seo/gsc-mcp) ★7：Search Console 的本地 MCP：Go 单文件、一行安装、用自己的 Google 账号登录，附点击率缺口、流量下滑等 6 个 skill
- [mcp-trendpulse](https://github.com/AKzar1el/mcp-trendpulse) ★7：Google 新闻加 Google 趋势的 MCP：比较关键词热度、找相关需求、跟当下新闻，做关键词和内容调研
- [my-claude-skills](https://github.com/vincentventalon/my-claude-skills) ★6：法语 SEO skill 包：技术审计、竞品、下一篇写什么、内链和读懂 Search Console，不用付费工具
- [foreign-trade-geo-skill](https://github.com/Elvinaskill/foreign-trade-geo-skill) ★6：外贸 B2B 独立站 GEO 审计：查可发现性、AI 爬虫访问、Schema、内容证据和英文页面能否被 AI 引用，出带证据的整改建议
- [peec-ai-tracking-strategy-builder](https://github.com/rebelytics/peec-ai-tracking-strategy-builder) ★6：AI 可见度追踪方案 skill 的 Peec AI 配套：在 Peec 里落地追踪方案，管字段、额度、写入和核对
- [altorank](https://github.com/AltoRank/altorank) ★6：开源版 Outrank：研究关键词、写文章、打分并核实数字出处，导出 Markdown 或 HTML 或发到 CMS，每次发布都要人批，附 skill
- [sayiyla-seo-ajan](https://github.com/sayiyla/sayiyla-seo-ajan) ★6：土耳其语 SEO/AEO/GEO 改稿 agent：改网页标题、描述、开头答案和 FAQ，写社媒说明，附站点审计和检查命令行
- [seo-audit-skills](https://github.com/carlosuhart/seo-audit-skills) ★6：西班牙语技术 SEO 审计 41 个 skill：WordPress、PrestaShop、JS 框架、核心网页指标、Schema、GEO
- [JittoJoseph/seo-skills](https://github.com/JittoJoseph/seo-skills) ★6：免费的 Shopify 和通用网站 SEO 审计：给网址，看 Google 和 AI 爬虫能读到什么、先修什么；Shopify 店另给按后台和主题说法的修复
- [blacksparrow](https://github.com/Shantodotdev/blacksparrow) ★6：Rust 写的本地爬虫和 120 条规则的技术 SEO 审计，Screaming Frog 的轻量替代，自带 MCP，也查 AI 爬虫权限
- [ai-bot-access](https://github.com/codevibe-technology/ai-bot-access) ★6：一条命令查 24 种 AI、搜索和链接预览爬虫能不能读你的网站：robots.txt 加真实请求，另有分享预览、爬虫 IP 核验和访问日志报告
- [google-webtools-mcp](https://github.com/stufently/google-webtools-mcp) ★6：Search Console 加 GA4 的 MCP：管站点、看搜索表现、查收录、出 GA4 报表、验证站点
- [geo-scope](https://github.com/tmolavi/geo-scope) ★6：AI 可见度测量框架：多家模型同题对比，记品牌提及、推荐和引用，可复现，带命令行和 MCP
- [World-Class-SEO-Agent-System](https://github.com/wfprieto/World-Class-SEO-Agent-System) ★5：不挑模型的 SEO 操作手册：技术 SEO、内容策略、GEO、本地 SEO、无障碍、数字 PR 和竞品情报的知识、提示词和证据规范，附 seoctl 命令行
- [aeo-toolkit](https://github.com/Advance-Labs/aeo-toolkit) ★5：开源 AEO 工具套件：44 项小检查决定 ChatGPT、Claude、Perplexity 会不会引用你，含爬取打分引擎、MCP 和 24 个 skill
- [CiteLadder](https://github.com/abhij1306/CiteLadder) ★5：可自己部署的 AI 搜索可见度追踪：看 ChatGPT、Gemini、Claude、AI 概览点名哪些品牌和页面，附 17 个 skill
- [aeo-geo-bestpractices](https://github.com/micaelgomestavares/aeo-geo-bestpractices) ★5：葡萄牙语 SEO/AEO/GEO skill：标签、JSON-LD、llms.txt、AI 爬虫规则，再把 Lighthouse 四项刷到 98–100
- [seo-gsc-ga4-analyst](https://github.com/owensky-dev/seo-gsc-ga4-analyst) ★5：Codex 的 SEO 数据分析 skill：合并 Search Console 搜索表现和 GA4 自然流量、关键行为，在本地出周报和行动清单
- [Manifold](https://github.com/manifoldmcp/marketing-skills) ★5：免费托管的营销数据 MCP 加 skill：Google 搜索、AI 回答、Search Console、地图、应用商店、亚马逊，也有社媒和广告库
- [rankmath-seo-wp](https://github.com/Moksa1123/rankmath-seo-wp) ★5：写 Rank Math 能打 80 分以上的 WordPress 文章：输出能直接粘进区块编辑器的 Gutenberg 区块，含 HowTo、FAQ 等区块
- [rankcontrol](https://github.com/rankcontrol/rankcontrol) ★5：RankControl 的命令行 skill：查 AI 搜索可见度和引用，规划和生成 SEO 文章并发到你的 CMS，管外链外联和报告
- [research-first-writer](https://github.com/jayanti-prajapati/research-first-writer) ★5：先研究再写的文章 skill：看真实排名页缺什么、每个数字记出处，不编“我们测过”，写给 Google 排名和 AI 引用
- [sitebulb-plugin](https://github.com/sitebulb/sitebulb-plugin) ★5：Sitebulb 官方 skill：基于你的 Sitebulb 审计数据，回答先修什么、这次爬取变了什么，出客户审计文档、开发工单和发版后检查
- [pagination-independence-architecture](https://github.com/rebelytics/pagination-independence-architecture) ★5：进阶技术 SEO skill：让列表站的可收录价值不依赖分页，审计被分页孤立的条目，设计有搜索需求的子分类，再按类别修剪
- [one-step-seo](https://github.com/6t9xstar/one-step-seo) ★5：零依赖的 Node.js SEO 工具：技术审计、AI 搜索可见度（GEO/AEO）、自动修复和持续监测，附 24 个 skill
- [searvex](https://github.com/cihantopac/searvex) ★5：开源 SEO 和 AI 搜索审计：查网站或代码仓库，按根因归类问题，安全的部分自动修、可回滚，出离线 HTML 报告
- [bulk-ai-cli-connector](https://github.com/puneetindersingh/bulk-ai-cli-connector) ★5：WordPress 插件加 MCP：让 AI 批量改 Yoast 和 Rank Math 的 SEO 元信息、JSON-LD、跳转和页面文案，可撤销
- [google-discover-api-mcp-server](https://github.com/cotletdev/google-discover-api-mcp-server) ★5：Google Discover 的接口和 MCP：读任意国家的 Discover 信息流，看哪些媒体和文章在涨，追踪你的站在不在里面
- [WordRocket/claude-seo-skills](https://github.com/WordRocket/claude-seo-skills) ★4：WordRocket 的免费 SEO skill：6 个 agent 并行审计全站，另有本地 SEO 页面、AI 概览可见度、外链和核心更新恢复
- [seranking/marketing-automation-plugins](https://github.com/seranking/marketing-automation-plugins) ★4：SE Ranking 和 Planable 的营销 skill：内容简报、编辑计划、旧文刷新、AI 可见度对标、对比页，另有投放和社媒
- [lighthouse-skill](https://github.com/nimajafari/lighthouse-skill) ★4：让 agent 跑 Google Lighthouse：测性能、无障碍、SEO 和最佳实践，设预算、卡 CI，改完再测一遍验证
- [Quincunx33/ai-seo-skill](https://github.com/Quincunx33/ai-seo-skill) ★4：讲证据的 SEO 工程 skill：技术审计、结构化数据、页面体验，只在有仓库权限时改代码
- [yandex-webmaster-mcp](https://github.com/BoxLab-Ltd/yandex-webmaster-mcp) ★4：Yandex 站长平台的只读 MCP：用自然语言查收录、搜索词、诊断和外链，可提交重抓，不存密钥
- [geolint](https://github.com/iliasabk/geolint) ★4：AI 搜索的 ESLint：查 51 种 AI 爬虫的 robots.txt 权限、llms.txt、结构化数据和可引用度，52 条规则，命令行和 MCP
- [geo-audit](https://github.com/g-shevchenko/geo-audit) ★4：开源 GEO 审计命令行：给网址打 AI 搜索可见度分（ChatGPT、Perplexity、Claude、Gemini、AI 概览），写成能交给团队的行动计划
- [semust-mcp](https://github.com/Semust-com/semust-mcp) ★4：Semust 的 MCP：Search Console、GA4、排名追踪、AI 概览可见度、Bing、Yandex，另有 Google 广告和社媒发帖
- [sonnivasquez/gsc-mcp](https://github.com/sonnivasquez/gsc-mcp) ★4：本地 Search Console MCP，34 个工具：对比搜索表现、找 SEO 机会、查网址收录，默认只读
- [rankparse-mcp](https://github.com/Rankparse/rankparse-mcp) ★4：RankParse 托管的 SEO 数据 MCP：外链、域名权重、技术栈和页面审计，数据来自 Common Crawl
- [cloro-dev/geo-tracker](https://github.com/cloro-dev/geo-tracker) ★4：给 agent 用的 GEO 加 SEO 追踪 MCP：定时把问题发给 ChatGPT、Gemini、Google AI 模式等，回答存进你自己的数据库
- [claude-code-seo-starter](https://github.com/AntonioBlago/claude-code-seo-starter) ★3：SEO 自由职业者和代理商的 Claude Code 模板：现状分析、潜力测算、报价到出 PDF 的完整接单流程，带按搜索意图算的点击率模型
- [raulveneri/seo-kit](https://github.com/raulveneri/seo-kit) ★3：SEO/GEO 工作流：定改什么、动手改、跑 PageSpeed、读 Google 数据、改前改后各爬一次对比，附 10 个 skill
- [llms-txt-writer](https://github.com/shimo4228/llms-txt-writer) ★3：写和检查只给 AI 读的文档（llms.txt、llms-full.txt、FAQ、术语表），本地脚本按 AI 引用研究的阈值给草稿打分
- [get-cited-by-ai](https://github.com/paultaki/get-cited-by-ai) ★3：让 AI 搜索引用你的 GEO skill：每条规则都来自作者七个站 2.6 万多次实测引用，先看有没有需求再动手
- [ai-visibility-tracking-strategy-builder](https://github.com/rebelytics/ai-visibility-tracking-strategy-builder) ★3：设计 AI 可见度追踪方案的方法论 skill：提示词集、分组、品牌名单和报告拆法，不挑监测平台
- [ai-search-audit-full](https://github.com/Olexan-art/ai-search-audit-full) ★3：给一页或最多 50 页做搜索和 AI 搜索审计：每个问题写明出处和修法，出问答地图、问题热力图、前后对比和本地历史，一份 HTML 报告
- [aizaloapp/aeorank](https://github.com/aizaloapp/aeorank) ★3：AEORank 的 SEO/AEO/GEO 诊断 skill：62 条技术规则加语义维度，查 Perplexity 和 AI 模式的引用，调它的接口或 MCP
- [agenticseo](https://github.com/kid7st/agenticseo) ★3：给编程 agent 的本地 SEO 命令行加 10 个 skill：关键词、竞品、外链、本地 SEO、排名追踪和站点审计，不用服务器
- [yandex-wordstat](https://github.com/prikotov/yandex-wordstat) ★3：俄语 Yandex Wordstat skill：查词的搜索量、相似词、按天周月的走势和地区分布，出 CSV 和 Markdown
- [IndexGap](https://github.com/borisowlexa2010-star/IndexGap) ★3：批量生成页面（programmatic SEO）发布前的质检：查编造的数字、整批模板出错、近似重复和 hreflang，中英俄输出
- [JakeLabate/Claude-SEO-Skills](https://github.com/JakeLabate/Claude-SEO-Skills) ★3：20 个技术 SEO 审计 skill：canonical、标题层级、内链、蚕食、llms.txt、robots、sitemap 等，导出 CSV 或 Word
- [seo-aeo-audit](https://github.com/ssheleg/seo-aeo-audit) ★3：审计网站在搜索引擎和 AI 回答里的可见度（Google、Bing、Yandex 和各家 AI），每个结论带来源证据，给排好优先级的修改计划
- [seo-geo-smart-audit-skill](https://github.com/yangjing6213-dev/seo-geo-smart-audit-skill) ★3：独立站 SEO/GEO 只读巡检：查收录、robots、sitemap、canonical、结构化数据、AI 爬虫和 llms.txt，确认的和待补的分开写
- [jorgejaramillo/seoskills](https://github.com/jorgejaramillo/seoskills) ★3：西班牙语 SEO 审计 skill：渲染抓取、robots.txt、站内审计、内链、图片、标题和描述，汇成一份网页报告
- [applyra-aso-skill](https://github.com/lucholabs/applyra-aso-skill) ★3：App Store 和 Google Play 的 ASO skill：关键词、排名、竞品、元数据校验、本地化、截图简报和转化实验
- [localseodata/mcp-server](https://github.com/localseodata/mcp-server) ★3：Local SEO Data 的 MCP，53 个本地 SEO 工具：SERP 和地图排名、评价、审计、关键词、竞品、网格追踪和 AI 可见度打分
- [a-bibikov/ai-search-audit](https://github.com/a-bibikov/ai-search-audit) ★3：查 ChatGPT、Claude、Perplexity 能否读懂并引用你的网站：56 项检查，命令行和 GitHub Action，可出 JSON
- [seo-cartograph-mcp](https://github.com/tom-ned/seo-cartograph-mcp) ★3：SEO Cartograph 的 MCP 加 13 个法语 skill：读你的抓取、Search Console、GA4、排名和内链图，再出审计和简报
- [zaDojo](https://github.com/zaDojo/seo-geo-mcp) ★2：zaDojo 的 12 个 SEO/GEO skill，接它托管的 MCP：关键词、实时 SERP、竞品、外链、站点审计、排名追踪、本地 SEO、AI 可见度
- [geo-skills](https://github.com/aivisibilitycensus/geo-skills) ★5：不打分的 GEO 测量：列出挡住 AI 搜索读页面的问题，统计 AI 回答提到品牌的比例并给 95% 区间，按公开 IP 核验 AI 爬虫
- [crakseo-mcp-plugins](https://github.com/CrakSEO/crakseo-mcp-plugins) ★0：CrakSEO 的 SEO 插件：查关键词、实时 SERP、外链、排名追踪、站点审计、本地 SEO、AI 可见度、收录提交和 Search Console
- [seo-skills](https://github.com/RomeoSEO/seo-skills) ★8：RomeoSEO 的免费 SEO/GEO skill 包：选词、技术审计、写对比页、发布前质检，查 AI 怎么说你，上 Reddit、LinkedIn 拿引用
- [saas-growth-agents](https://github.com/Pluviobyte/saas-growth-agents) ★541：出海站增长 Bot：每天早中晚扫新搜索词，按词找竞品站、查它们的外链和 DR，自动提交免费导航站

<a id="by-group"></a>
## 按类型

<a id="group-pipeline"></a>
### 全套：审计 → 关键词 → 内容 → 技术 → 监测

一套 skill 覆盖 SEO 的大部分环节，有的连 GEO 也包了。

- 🌟 **[marketingskills](https://github.com/coreyhaines31/marketingskills)** · ★ 60.6k<br>Corey Haines 的营销 skill 合集：转化优化、文案、SEO 和 AI 搜索优化、数据分析、增长，SEO 部分有审计、程序化页面和结构化数据<br><sub>针对：Google · Google AI 概览 · ChatGPT · Perplexity</sub><br><sub>更新于 2026-11-11 · 英文 · 53 个 skill · MIT</sub>

- 🌟 **[claude-seo](https://github.com/AgriciDaniel/claude-seo)** · ★ 29.7k<br>Claude Code 的 SEO 全家桶：26 个子 skill、19 个专家 agent 并行查技术 SEO、E-E-A-T、结构化数据和 GEO<br><sub>针对：Google · Google AI 概览 · Bing · ChatGPT · Perplexity · Gemini</sub><br><sub>更新于 2026-11-15 · 英文 · 35 个 skill · MIT</sub>

- **[notfair-plugin](https://github.com/nowork-studio/notfair-plugin)** · ★ 4.2k<br>NotFair 的 SEO、GEO 和营销 skill：审计网站、查流量下滑、分析 GA4 和 Search Console、找各平台广告的浪费<br><sub>针对：Google · Google AI 概览 · ChatGPT · Perplexity · Gemini</sub><br><sub>更新于 2026-11-13 · 英文 · 45 个 skill · MIT</sub>

- **[aaron-marketing-skills](https://github.com/aaron-he-zhu/aaron-marketing-skills)** · ★ 3.1k<br>Aaron 的 120 个营销 skill，其中 16 个管 SEO 和 GEO，另有叙事、社媒、邮件、投放、达人和发布，可装成插件或 8 个 bot 的团队<br><sub>针对：通用</sub><br><sub>更新于 2026-11-15 · 多语言 · 120 个 skill · Apache-2.0</sub>

- **[growth-lab](https://github.com/tsingyuai/growth-lab)** · ★ 2k<br>开源增长工具：让 Claude Code 或 Codex 跑 SEO 页面闭环（找搜索需求、写页面、复查、看表现），另有公众号文章闭环和多平台内容抓取<br><sub>针对：通用</sub><br><sub>更新于 2026-11-13 · 多语言 · 22 个 skill · Apache-2.0</sub>

- **[seo-skills](https://github.com/Illyism/seo-skills)** · ★ 1.3k<br>Illyism 的 SEO skill 合集：每天自动跑仓库 SEO、技术诊断、Ahrefs/DataForSEO 查词、对比页、AI 引用追踪、外链和目录提交<br><sub>针对：Google · Google AI 概览 · ChatGPT · Perplexity · Gemini</sub><br><sub>更新于 2026-11-12 · 英文 · 30 个 skill</sub><br><sub>💡 作者也卖 SEO 服务：外链（linkdr）、AI 引用追踪（aiseotracker）、目录（awesome-tools）这几个 skill 接的是他自己的付费产品；Ahrefs、DataForSEO 要自己的账号</sub>

- **[marketing-skills](https://github.com/kostja94/marketing-skills)** · ★ 1.1k<br>160 多个营销和 SEO skill：技术和页面 SEO、调研、内容、40 多种页面类型、投放和渠道，按你给的产品资料产出<br><sub>针对：Google</sub><br><sub>更新于 2026-11-06 · 英文 · 15 个 skill · MIT</sub>

- **[Agentic-SEO-Skill](https://github.com/Bhanunamikaze/Agentic-SEO-Skill)** · ★ 1.1k<br>LLM 主导的 SEO 分析 skill：16 个子 skill、10 个专家 agent，89 个脚本只负责收集证据<br><sub>针对：Google · Google AI 概览 · ChatGPT · Perplexity</sub><br><sub>更新于 2026-10-14 · 英文 · MIT</sub>

- **[fire-your-seo-agency](https://github.com/leopard627/fire-your-seo-agency)** · ★ 1k<br>替你干 SEO/GEO 代运营的活：按公开标准和清单自己审计、优化 SEO、AEO、GEO，也管韩国 Naver 搜索<br><sub>针对：Google · Google AI 概览 · Bing · ChatGPT · Perplexity</sub><br><sub>更新于 2026-11-03 · 多语言 · MIT</sub>

- **[qiaomu-seo](https://github.com/joeseesun/qiaomu-seo)** · ★ 474<br>乔木的 SEO skill：按真实搜索链路排查收录、渲染、canonical、内链和搜索表现，做关键词页面策略、流量诊断、改版迁移和效果验证<br><sub>针对：Google · Google AI 概览 · Bing · ChatGPT · Perplexity</sub><br><sub>更新于 2026-08-03 · 中文 · MIT</sub>

- **[open-seo-advisor-skill](https://github.com/mars-tw/open-seo-advisor-skill)** · ★ 354<br>繁体中文 SEO 顾问 skill：蒸馏权威方法论，给任何行业做 SEO 健检、修复和内容产出，不绑定厂商<br><sub>针对：Google</sub><br><sub>更新于 2026-09-23 · 中文 · Apache-2.0</sub>

- **[7deer_skills](https://github.com/kennyzir/7deer_skills)** · ★ 342<br>做 Roblox 游戏攻略站的 33 个 skill：判断游戏值不值得做、关键词研究、建站规划、SEO 质检、持续更新和找外链<br><sub>针对：Google</sub><br><sub>更新于 2026-09-29 · 中文 · 33 个 skill · MIT</sub>

- **[everyinfra/seo-skills](https://github.com/everyinfra/seo-skills)** · ★ 328<br>免费的全球 SEO/GEO skill：18 个市场入口、56 个脚本，管多语言 GEO、程序化 SEO、Core Web Vitals 和降权恢复<br><sub>针对：Google · Google AI 概览 · Bing · Yandex · ChatGPT · Gemini</sub><br><sub>更新于 2026-11-16 · 多语言 · Apache-2.0</sub>

- **[yan-skills](https://github.com/yan-labs/yan-skills)** · ★ 309<br>给做 SEO 和独立站的人用的 skill：选词建站到上线增长（rankup）、外链去哪发和是否生效（backlink），另有浏览器取数和生图<br><sub>针对：Google</sub><br><sub>更新于 2026-11-16 · 中文 · 11 个 skill · MIT</sub>

- **[beyondseo](https://github.com/beyondtahir/beyondseo)** · ★ 267<br>自带爬虫的 SEO 全套：SEO/AEO/GEO、内容、竞品和口碑，附 206 个带 DR 的发稿渠道和外链计划，本体不要 API Key<br><sub>针对：Google · ChatGPT</sub><br><sub>更新于 2026-11-04 · 英文 · MIT</sub>

- **[codex-seo](https://github.com/zhtyyx/codex-seo)** · ★ 157<br>在 Codex CLI 里做 SEO 审计：26 个子 skill、19 个专家角色，查技术 SEO、结构化数据、GEO、本地和电商，最后给排好优先级的行动计划<br><sub>针对：Google · Google AI 概览 · ChatGPT · Perplexity · Gemini</sub><br><sub>更新于 2026-11-09 · 多语言 · 33 个 skill · MIT</sub><br><sub>💡 移植自已收录的 AgriciDaniel/claude-seo，改成在 Codex CLI 里跑，附中文说明</sub>

- **[All-In-One-Free-SEO-Tool](https://github.com/IamRamgarhia/All-In-One-Free-SEO-Tool)** · ★ 129<br>自己部署的免费 SEO 平台：站点审计、排名、关键词、AI 可见度、外链和客户报告，附 5 个 skill 写报告、定关键词、改问题<br><sub>针对：Google · Google AI 概览 · ChatGPT · Perplexity · Gemini</sub><br><sub>更新于 2026-10-30 · 英文 · 5 个 skill · MIT</sub><br><sub>💡 skill 要先自己部署这个平台（Docker），通过它的 MCP 干活</sub>

- **[seo-god](https://github.com/AKCodez/seo-god)** · ★ 123<br>让 Claude Code 每天给自己的网站做 SEO：本地爬站、在你的仓库里修问题、读 Search Console 和前一天对比，定时跑<br><sub>针对：Google</sub><br><sub>更新于 2026-08-03 · 英文 · MIT</sub>

- **[ultimate-seo-geo](https://github.com/mykpono/ultimate-seo-geo)** · ★ 103<br>SEO 加 GEO 的全站审计：打分的问题清单、可直接部署的修复、结构化数据、E-E-A-T 评估，导出 HTML、Excel 或 PDF<br><sub>针对：Google · Google AI 概览 · ChatGPT · Perplexity · Gemini</sub><br><sub>更新于 2026-10-01 · 英文 · 2 个 skill · MIT</sub>

- **[akii-seo-ai-search-optimizer](https://github.com/akii-technologies-ltd/akii-seo-ai-search-optimizer)** · ★ 80<br>Akii 的免费 SEO/AEO/GEO 插件：网站审计、内容规划、查链接、生成结构化数据，用公开网页信号或 Ahrefs 数据估算 AI 可见度<br><sub>针对：Google · Google AI 概览 · ChatGPT · Perplexity · Gemini · Claude</sub><br><sub>更新于 2026-11-13 · 英文 · 12 个 skill · MIT</sub><br><sub>💡 每台机器每天给 akii.com 发一次匿名安装计数（不含代码和网址），设 DO_NOT_TRACK=1 可关</sub>

- **[mxfschr/claude-code-seo](https://github.com/mxfschr/claude-code-seo)** · ★ 46<br>Claude Code 的 SEO 系统：26 节知识库加 9 个命令，接 Search Console 和 DataForSEO 实时查蚕食、竞品和见效快的项<br><sub>针对：Google</sub><br><sub>更新于 2026-11-11 · 英文 · 12 个 skill</sub><br><sub>💡 实时数据要 Search Console 授权和 DataForSEO 账号（按量付费）</sub>

- **[claude-seo-skill](https://github.com/mangollc/claude-seo-skill)** · ★ 39<br>给代理商用的 SEO/AEO 插件：关键词研究、技术审计、内容优化、本地 SEO、外链和 AI 搜索优化，6 个 skill，不用 API Key<br><sub>针对：Google · Google AI 概览 · ChatGPT · Perplexity</sub><br><sub>更新于 2026-11-06 · 英文 · 6 个 skill</sub>

- **[seo-guide-skill](https://github.com/lesishu/seo-guide-skill)** · ★ 33<br>SEO 全流程 skill：网站诊断、页面优化、技术 SEO、内容策略和外链建设<br><sub>针对：Google</sub><br><sub>更新于 2026-11-01 · 中文 · MIT</sub>

- **[seojuice-skills](https://github.com/calm-north/seojuice-skills)** · ★ 22<br>SEOJuice 出的 14 个 SEO skill：全面审计、速度、关键词策略、内链、内容找回、超越竞品和 AI 可见度<br><sub>针对：Google · Google AI 概览 · ChatGPT · Perplexity · Gemini</sub><br><sub>更新于 2026-02-27 💤 · 英文 · 14 个 skill · MIT</sub>

- **[tipsai/product-seo](https://github.com/tipsai/product-seo)** · ★ 20<br>卖产品的网站做 SEO：从 Search Console 数据出发，先挑产品正好能回答的搜索，再改页面、做工具页、清理、站外提及，每项改动定复查日期<br><sub>针对：Google · Bing</sub><br><sub>更新于 2026-11-16 · 英文 · MIT</sub>

- **[seo-survival-kit](https://github.com/maxschottke-spec/seo-survival-kit)** · ★ 11<br>电商和 D2C 站的 SEO 恢复工具箱：18 个 skill 管核心更新后的诊断恢复、AI 搜索可见度和引用追踪，出 PDF 报告<br><sub>针对：Google · Google AI 概览 · ChatGPT · Perplexity</sub><br><sub>更新于 2026-11-13 · 英文 · 19 个 skill · MIT</sub>

- **[croftweaver](https://github.com/karero/croftweaver)** · ★ 10<br>从简报建出完整网站（Astro、Cloudflare），自带 SEO、结构化数据和测试，上线后按 Search Console 和 AI 提及提示下一步<br><sub>针对：Google</sub><br><sub>更新于 2026-11-16 · 英文 · 40 个 skill · MIT</sub>

- **[seo-aeo-geo-ultimate](https://github.com/oegeyilmaz9/seo-aeo-geo-ultimate)** · ★ 8<br>SEO、AEO、GEO 一整套：一个总入口分派 27 个 skill，审计、技术、内容、外链、本地、电商、AI 搜索，每步留证据<br><sub>针对：通用</sub><br><sub>更新于 2026-11-03 · 英文 · 27 个 skill · Apache-2.0</sub>

- **[seo-skills](https://github.com/RomeoSEO/seo-skills)** · ★ 8<br>RomeoSEO 的免费 SEO/GEO skill 包：选词、技术审计、写对比页、发布前质检，查 AI 怎么说你，上 Reddit、LinkedIn 拿引用<br><sub>针对：Google · Google AI 概览 · ChatGPT · Perplexity · Gemini · Claude</sub><br><sub>更新于 2026-11-11 · 英文 · 50 个 skill · MIT</sub><br><sub>💡 网站上那条 curl \| bash 会从 romeoseo.com 下载压缩包再装；想先看文件，就 git clone 后跑仓库里的 install.sh。接 DataForSEO 是可选的，按次收费，skill 里写了花费上限</sub>

- **[search-os](https://github.com/vamsireddy4/search-os)** · ★ 7<br>一个 skill 管 SEO、AEO、GEO 和 AI 可见度：让网站出现在 Google、Bing、ChatGPT、Perplexity 和 AI 概览里<br><sub>针对：Google · Google AI 概览 · Bing · ChatGPT · Perplexity · Claude</sub><br><sub>更新于 2026-11-12 · 英文 · MIT</sub>

- **[my-claude-skills](https://github.com/vincentventalon/my-claude-skills)** · ★ 6<br>法语 SEO skill 包：技术审计、竞品、下一篇写什么、内链和读懂 Search Console，不用付费工具<br><sub>针对：Google</sub><br><sub>更新于 2026-11-16 · 法文 · 2 个 skill · MIT</sub><br><sub>💡 在作者的个人合集里，另一包是短视频 skill；只装 skills/seo 那包就行</sub>

- **[World-Class-SEO-Agent-System](https://github.com/wfprieto/World-Class-SEO-Agent-System)** · ★ 5<br>不挑模型的 SEO 操作手册：技术 SEO、内容策略、GEO、本地 SEO、无障碍、数字 PR 和竞品情报的知识、提示词和证据规范，附 seoctl 命令行<br><sub>针对：Google · Google AI 概览</sub><br><sub>更新于 2026-11-15 · 📝 提示词 · 英文 · MIT</sub>

- **[WordRocket/claude-seo-skills](https://github.com/WordRocket/claude-seo-skills)** · ★ 4<br>WordRocket 的免费 SEO skill：6 个 agent 并行审计全站，另有本地 SEO 页面、AI 概览可见度、外链和核心更新恢复<br><sub>针对：Google · Google AI 概览 · ChatGPT</sub><br><sub>更新于 2026-11-14 · 英文 · 18 个 skill · MIT</sub><br><sub>💡 dataforseo-seo-tool 要 DataForSEO 账号（按量付费），其余不用 Key</sub>

- **[claude-code-seo-starter](https://github.com/AntonioBlago/claude-code-seo-starter)** · ★ 3<br>SEO 自由职业者和代理商的 Claude Code 模板：现状分析、潜力测算、报价到出 PDF 的完整接单流程，带按搜索意图算的点击率模型<br><sub>针对：Google</sub><br><sub>更新于 2026-11-12 · 英文 · 4 个 skill · MIT</sub><br><sub>💡 默认免 Key 连 Visibly AI 的 MCP（知识类工具免费），查 Search Console、关键词、外链等实时数据要它的 Key</sub>

- **[raulveneri/seo-kit](https://github.com/raulveneri/seo-kit)** · ★ 3<br>SEO/GEO 工作流：定改什么、动手改、跑 PageSpeed、读 Google 数据、改前改后各爬一次对比，附 10 个 skill<br><sub>针对：Google</sub><br><sub>更新于 2026-11-08 · 英文 · 10 个 skill</sub>


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
# growth-lab
npx skills add tsingyuai/growth-lab
# seo-skills
npx skills add Illyism/seo-skills
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
# everyinfra/seo-skills
npx skills add everyinfra/seo-skills
# yan-skills
npx skills add yan-labs/yan-skills
# beyondseo
npx skills add beyondtahir/beyondseo
# codex-seo
npx skills add zhtyyx/codex-seo
# All-In-One-Free-SEO-Tool
npx skills add IamRamgarhia/All-In-One-Free-SEO-Tool
# seo-god
npx skills add AKCodez/seo-god
# ultimate-seo-geo
npx skills add mykpono/ultimate-seo-geo
# akii-seo-ai-search-optimizer
npx skills add akii-technologies-ltd/akii-seo-ai-search-optimizer
# mxfschr/claude-code-seo
npx skills add mxfschr/claude-code-seo
# claude-seo-skill
npx skills add mangollc/claude-seo-skill
# seo-guide-skill
npx skills add lesishu/seo-guide-skill
# seojuice-skills
npx skills add calm-north/seojuice-skills
# tipsai/product-seo
npx skills add tipsai/product-seo
# seo-survival-kit
npx skills add maxschottke-spec/seo-survival-kit
# croftweaver
npx skills add karero/croftweaver
# seo-aeo-geo-ultimate
npx skills add oegeyilmaz9/seo-aeo-geo-ultimate
# seo-skills
npx skills add RomeoSEO/seo-skills
# search-os
npx skills add vamsireddy4/search-os
# my-claude-skills
npx skills add vincentventalon/my-claude-skills
# WordRocket/claude-seo-skills
npx skills add WordRocket/claude-seo-skills
# claude-code-seo-starter
npx skills add AntonioBlago/claude-code-seo-starter
# raulveneri/seo-kit
npx skills add raulveneri/seo-kit
```

</details>

<a id="group-geo"></a>
### GEO：让 AI 回答引用你

GEO（生成式引擎优化）是让 ChatGPT、Perplexity、Google AI 概览这类 AI 回答提到和引用你的网站：查 AI 可见度、改内容结构、写 llms.txt。

- 🌟 **[geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude)** · ★ 11.7k<br>GEO 优先的 SEO skill：可引用度打分、AI 爬虫访问分析、品牌权威、结构化数据，按 ChatGPT、Perplexity 等平台分别优化<br><sub>针对：Google · Google AI 概览 · ChatGPT · Perplexity · Gemini · Claude</sub><br><sub>更新于 2026-11-15 · 英文 · 16 个 skill · MIT</sub>

- **[opc-skills](https://github.com/ReScienceLab/opc-skills)** · ★ 1.9k<br>一人公司 skill 合集：seo-geo 做 SEO 和 GEO，另有找域名、做 banner 和 logo、Reddit 和 X 调研<br><sub>针对：Google · ChatGPT · Perplexity · Gemini</sub><br><sub>更新于 2026-11-15 · 英文 · 12 个 skill · Apache-2.0</sub>

- **[gtm-engineer-skills](https://github.com/onvoyage-ai/gtm-engineer-skills)** · ★ 1.4k<br>GTM 工程师 skill：网站 AEO/GEO 体检、内容审计、做外链和资源页、品牌 DNA、关键词和提示词聚类，每个 skill 交付一份具体产出<br><sub>针对：Google · Google AI 概览 · ChatGPT · Perplexity · Claude</sub><br><sub>更新于 2026-10-11 · 英文 · 12 个 skill · MIT</sub>

- **[geo-optimizer-skill](https://github.com/Auriti-Labs/geo-optimizer-skill)** · ★ 1.3k<br>开源 AEO/GEO 工具：一条命令给网站打 0–100 分，看 ChatGPT、Perplexity 等 AI 能否抓取、读懂并引用你，再列出要改的地方<br><sub>针对：Google · Google AI 概览 · ChatGPT · Perplexity · Gemini · Claude</sub><br><sub>更新于 2026-11-14 · 英文 · 2 个 skill · MIT</sub>

- **[geolook](https://github.com/aigclink/geolook)** · ★ 819<br>开源 GEO 实施平台：针对一个项目做现状分析、诊断、策略、拆工单、执行和验证，可自己部署，附 skill<br><sub>针对：百度 · ChatGPT · Perplexity · Gemini · Claude · 豆包 · Kimi · DeepSeek</sub><br><sub>更新于 2026-08-10 · 多语言 · MIT</sub>

- **[elmo](https://github.com/elmohq/elmo)** · ★ 602<br>开源 AI 可见度平台：追踪 ChatGPT、Claude、Perplexity、AI 概览等怎么提到和引用你的品牌，附 aeo skill<br><sub>针对：Google AI 概览 · ChatGPT · Perplexity · Gemini · Claude</sub><br><sub>更新于 2026-11-14 · 英文 · 3 个 skill · MIT</sub><br><sub>💡 追踪功能要自己部署 Elmo</sub>

- **[recomby-geo](https://github.com/ViryaZheng/recomby-geo)** · ★ 456<br>GEO 的 AI 员工方案：GEO skill 包（内容写作、质量审核、GEO 流程）加上一份 agent 和办公 CLI 清单，零 API Key<br><sub>针对：通用</sub><br><sub>更新于 2026-07-04 · 中文 · 9 个 skill · MIT</sub>

- **[limelit-co/open](https://github.com/limelit-co/open)** · ★ 445<br>自己部署的 AI 可见度追踪（Go 单文件），看 ChatGPT、Claude 等怎么提到你，附查 AI 爬虫和 llms.txt 的 skill<br><sub>针对：Google AI 概览 · ChatGPT · Perplexity · Gemini · Claude</sub><br><sub>更新于 2026-11-14 · 英文 · 3 个 skill · Apache-2.0</sub><br><sub>💡 查 AI 爬虫和 llms.txt 的 skill 不用账号；可见度追踪要自己部署 Limelit，用你自己的模型 API Key</sub>

- **[GetCito](https://github.com/ai-search-guru/getcito-worlds-first-open-source-aio-aeo-or-geo-tool)** · ★ 429<br>GetCito 开源 AI 搜索优化和可见度追踪平台，附 30 个 skill：答案前置改写、FAQ、竞品对比、引用缺口、内容刷新、错误说法纠正等<br><sub>针对：Google AI 概览 · Gemini</sub><br><sub>更新于 2026-11-05 · 英文 · 30 个 skill · MIT</sub><br><sub>💡 追踪功能要自己部署 GetCito，用你自己的模型 API Key；独立版 AEO 教练 skill 不用部署</sub>

- **[voyage-geo-agent](https://github.com/onvoyage-ai/voyage-geo-agent)** · ★ 385<br>开源 GEO 命令行：研究你的品牌和竞品，向 ChatGPT、Claude、Gemini、Perplexity、DeepSeek 等提问，统计谁被提到和推荐<br><sub>针对：ChatGPT · Perplexity · Gemini · Claude · DeepSeek</sub><br><sub>更新于 2026-02-24 💤 · 英文 · 3 个 skill · MIT</sub><br><sub>💡 向各家模型提问要它们的 API Key</sub>

- **[geo-aeo-tracker](https://github.com/danishashko/geo-aeo-tracker)** · ★ 329<br>开源 AI 可见度追踪和 AEO 检查：看 ChatGPT、Perplexity、Gemini、AI 模式怎么提到你，带 MCP，skill 调它的命令行<br><sub>针对：Google AI 概览 · ChatGPT · Perplexity · Gemini</sub><br><sub>更新于 2026-11-11 · 英文 · MIT</sub><br><sub>💡 收集 AI 回答走 Bright Data 的抓取接口（付费）</sub>

- **[geo-first-principles](https://github.com/ALLENLION35/geo-first-principles)** · ★ 303<br>给企业负责人的 GEO 判断：从行业竞争、客户需求和成交逻辑出发，判断该不该做 GEO、价值在哪、怎么投入，附五题实测指引<br><sub>针对：通用</sub><br><sub>更新于 2026-09-14 · 中文 · MIT</sub>

- **[SEO-GEO-AEO-Skill](https://github.com/SNLabat/SEO-GEO-AEO-Skill)** · ★ 291<br>一个 skill 审三样：传统 SEO（Google、Bing）、GEO（Perplexity、ChatGPT 搜索、AI 概览）和 AEO 答案引擎优化<br><sub>针对：Google · Google AI 概览 · Bing · ChatGPT · Perplexity · Gemini</sub><br><sub>更新于 2026-03-13 💤 · 英文</sub>

- **[geoptimize](https://github.com/cucuwang/geoptimize)** · ★ 263<br>内容质量检查（原 aeoptimize）：在 CI 里做确定性的 GEO 就绪度扫描，发布前拦下退步，另有生成、改写和 SEO 实验记录 skill<br><sub>针对：通用</sub><br><sub>更新于 2026-11-01 · 多语言 · 4 个 skill · MIT</sub>

- **[ansvisor](https://github.com/ansvisor/ansvisor)** · ★ 242<br>开源 AI 搜索执行平台：追踪各家 AI 的可见度，让 agent 把信号变成排好序的动作和修改草稿，附 41 个 skill<br><sub>针对：Google AI 概览 · ChatGPT · Perplexity · Gemini · Claude</sub><br><sub>更新于 2026-11-16 · 英文 · 41 个 skill · MIT</sub><br><sub>💡 追踪要自己部署 Ansvisor；独立版 AEO 教练 skill 不用部署</sub>

- **[GEO-Content-Optimizer-Skill](https://github.com/liangdabiao/GEO-Content-Optimizer-Skill)** · ★ 240<br>GEO 工具箱：三个从轻到重的 skill，给单篇文章或整站做 AI 引用优化，让 ChatGPT、豆包、Perplexity 回答时提到你<br><sub>针对：Google AI 概览 · ChatGPT · Perplexity · Gemini · 豆包 · Kimi</sub><br><sub>更新于 2026-08-05 · 中文 · 3 个 skill</sub>

- **[eGEOagents](https://github.com/mverab/eGEOagents)** · ★ 218<br>开源 GEO/AEO 工具包：内容打分、结构化数据生成、竞品分析、校验修复和 GEO 迭代循环，带命令行和 MCP<br><sub>针对：ChatGPT · Perplexity · Gemini · Claude</sub><br><sub>更新于 2026-11-11 · 英文 · 5 个 skill · MIT</sub>

- **[canonry](https://github.com/Canonry/canonry)** · ★ 209<br>agent 优先的 AEO/GEO 平台：追踪 ChatGPT、Claude、Gemini 的引用，合并 Search Console，再让 agent 写内容<br><sub>针对：ChatGPT · Gemini · Claude</sub><br><sub>更新于 2026-11-16 · 英文 · 3 个 skill · MIT</sub><br><sub>💡 要自己部署 Canonry 或用它的托管版</sub>

- **[GEOHub](https://github.com/yaojingang/GEOHub)** · ★ 169<br>GEO SEO Hub：以 GEO 为主的 skill 集，做发现、诊断、内容、监测和 SEO 规划，结论都标明证据边界，实验版<br><sub>针对：通用</sub><br><sub>更新于 2026-08-31 · 英文 · 9 个 skill · AGPL-3.0</sub>

- **[claude-rank](https://github.com/Houseofmvps/claude-rank)** · ★ 149<br>查网站为什么不被 AI 引用并自动修：10 个扫描器 170 多条规则，自动生成 robots.txt、sitemap、llms.txt 和 JSON-LD<br><sub>针对：Google · Google AI 概览 · Bing · ChatGPT · Perplexity · Gemini · Claude</sub><br><sub>更新于 2026-07-08 · 英文 · 6 个 skill · MIT</sub>

- **[aeo.js](https://github.com/rubenmarcus/aeo.js)** · ★ 147<br>AEO 开发库：生成 llms.txt、robots.txt、sitemap 和 JSON-LD，检查网站对 23 种 AI 爬虫的开放情况，附 skill<br><sub>针对：ChatGPT · Perplexity · Claude</sub><br><sub>更新于 2026-11-14 · 英文</sub>

- **[orangeo-ai-visibility-skill](https://github.com/OranAi-Ltd/orangeo-ai-visibility-skill)** · ★ 145<br>品牌官网 AI 可见度初检：查 AI 爬虫访问、llms.txt、结构化数据和引用信号，找竞品差距，生成买家会问 AI 的问题<br><sub>针对：ChatGPT · Perplexity · Gemini · Claude · DeepSeek</sub><br><sub>更新于 2026-06-09 · 英文 · MIT</sub>

- **[google-ai-search-optimization](https://github.com/deepakness/google-ai-search-optimization)** · ★ 141<br>按 Google 官方指南优化 AI 概览和 AI 模式：可抓取、可收录、有独到价值的内容，做 SEO 审计和改进计划（非官方）<br><sub>针对：Google · Google AI 概览</sub><br><sub>更新于 2026-05-16 💤 · 英文</sub>

- **[seo-skills/geo-audit-skill](https://github.com/seo-skills/geo-audit-skill)** · ★ 40<br>SEOmator 的确定性 GEO 审计：Python 命令行算分、skill 解读，看 AI 爬虫能不能进、段落能不能被直接引用<br><sub>针对：Google AI 概览 · Bing · ChatGPT · Perplexity · Gemini · Claude</sub><br><sub>更新于 2026-09-29 · 英文 · 9 个 skill · MIT</sub>

- **[geo-score](https://github.com/jianruntech/geo-score)** · ★ 34<br>开源 GEO 打分：按公开评分标准给网站打 0–100 分，再用你自己的 OpenAI、Perplexity、Gemini 等 Key 每周追踪 AI 引用<br><sub>针对：ChatGPT · Perplexity · Gemini · Claude</sub><br><sub>更新于 2026-11-14 · 英文 · MIT</sub>

- **[geoskills](https://github.com/Cognitic-Labs/geoskills)** · ★ 32<br>6 个 GEO skill：诊断、修复和监测网站在 AI 搜索里的可见度，含 Bing AI 数据分析和竞品对比<br><sub>针对：Google · Bing · ChatGPT · Perplexity · Gemini</sub><br><sub>更新于 2026-10-01 · 英文 · 8 个 skill · Apache-2.0</sub>

- **[agentmarkup](https://github.com/agentmarkup/agentmarkup)** · ★ 27<br>构建时生成 llms.txt、JSON-LD、Markdown 镜像页和 AI 爬虫规则并校验，支持 Vite、Astro、Next.js 等，附 skill<br><sub>针对：通用</sub><br><sub>更新于 2026-11-11 · 英文 · MIT</sub>

- **[aicw-ai-mentions](https://github.com/aichatwatch/aicw-ai-mentions)** · ★ 25<br>命令行和 MCP：追踪 ChatGPT、Claude、Gemini、Grok、Perplexity 怎么提到你和竞品，抽出被引用的链接，出 HTML 报告<br><sub>针对：ChatGPT · Perplexity · Gemini · Claude</sub><br><sub>更新于 2026-11-13 · 英文 · MIT</sub><br><sub>💡 用你自己的各家模型 API Key</sub>

- **[agent-lighthouse](https://github.com/ForkPoint/agent-lighthouse)** · ★ 17<br>给 AI 用的 Lighthouse：223 项检查，看 ChatGPT、Perplexity、AI 爬虫和 agent 浏览器能否发现、读懂、引用你的网站<br><sub>针对：ChatGPT · Perplexity · Claude</sub><br><sub>更新于 2026-11-16 · 英文 · Apache-2.0</sub>

- **[topcited-skills](https://github.com/TopCited/topcited-skills)** · ★ 10<br>TopCited 的 skill：SEO/GEO 知识、调用 TopCited 接口和一套带引导的 AI 可见度排查流程<br><sub>针对：ChatGPT · Perplexity · Gemini · Claude</sub><br><sub>更新于 2026-11-09 · 英文 · 3 个 skill · MIT</sub><br><sub>💡 接口部分要 TopCited 的 API Key</sub>

- **[agent-readiness](https://github.com/Canonry/agent-readiness)** · ★ 7<br>开源的 agent 就绪度审计：按 llms.txt、AI 爬虫访问、结构化数据等 16 项打分，给 agent 能直接改的修复清单，离线跑<br><sub>针对：ChatGPT · Perplexity · Gemini · Claude</sub><br><sub>更新于 2026-11-10 · 英文 · 2 个 skill · MIT</sub>

- **[foreign-trade-geo-skill](https://github.com/Elvinaskill/foreign-trade-geo-skill)** · ★ 6<br>外贸 B2B 独立站 GEO 审计：查可发现性、AI 爬虫访问、Schema、内容证据和英文页面能否被 AI 引用，出带证据的整改建议<br><sub>针对：通用</sub><br><sub>更新于 2026-11-05 · 中文</sub><br><sub>💡 许可是 PolyForm 非商用</sub>

- **[peec-ai-tracking-strategy-builder](https://github.com/rebelytics/peec-ai-tracking-strategy-builder)** · ★ 6<br>AI 可见度追踪方案 skill 的 Peec AI 配套：在 Peec 里落地追踪方案，管字段、额度、写入和核对<br><sub>针对：Google AI 概览 · ChatGPT · Perplexity · Gemini</sub><br><sub>更新于 2026-11-16 · 英文 · CC-BY-4.0</sub><br><sub>💡 要 Peec AI 账号，并和 ai-visibility-tracking-strategy-builder 一起装</sub>

- **[aeo-geo-bestpractices](https://github.com/micaelgomestavares/aeo-geo-bestpractices)** · ★ 5<br>葡萄牙语 SEO/AEO/GEO skill：标签、JSON-LD、llms.txt、AI 爬虫规则，再把 Lighthouse 四项刷到 98–100<br><sub>针对：Google · ChatGPT · Perplexity · Gemini · Claude</sub><br><sub>更新于 2026-10-31 · 葡萄牙文 · MIT</sub><br><sub>💡 README 有英文版，SKILL.md 和指南是巴西葡萄牙语</sub>

- **[aeo-toolkit](https://github.com/Advance-Labs/aeo-toolkit)** · ★ 5<br>开源 AEO 工具套件：44 项小检查决定 ChatGPT、Claude、Perplexity 会不会引用你，含爬取打分引擎、MCP 和 24 个 skill<br><sub>针对：ChatGPT · Perplexity · Claude</sub><br><sub>更新于 2026-11-15 · 英文 · 24 个 skill · Apache-2.0</sub>

- **[CiteLadder](https://github.com/abhij1306/CiteLadder)** · ★ 5<br>可自己部署的 AI 搜索可见度追踪：看 ChatGPT、Gemini、Claude、AI 概览点名哪些品牌和页面，附 17 个 skill<br><sub>针对：Google AI 概览 · ChatGPT · Gemini · Claude</sub><br><sub>更新于 2026-11-13 · 英文 · 17 个 skill · AGPL-3.0</sub><br><sub>💡 追踪要自己部署 CiteLadder 或用它的托管版</sub>

- **[geo-skills](https://github.com/aivisibilitycensus/geo-skills)** · ★ 5<br>不打分的 GEO 测量：列出挡住 AI 搜索读页面的问题，统计 AI 回答提到品牌的比例并给 95% 区间，按公开 IP 核验 AI 爬虫<br><sub>针对：Google AI 概览 · ChatGPT · Gemini</sub><br><sub>更新于 2026-11-14 · 英文 · 9 个 skill · MIT</sub><br><sub>💡 检查类脚本只要 Python 3、不用账号；收集 AI 回答那个要你自己的 DataForSEO 或 SerpApi key</sub>

- **[ai-search-audit-full](https://github.com/Olexan-art/ai-search-audit-full)** · ★ 3<br>给一页或最多 50 页做搜索和 AI 搜索审计：每个问题写明出处和修法，出问答地图、问题热力图、前后对比和本地历史，一份 HTML 报告<br><sub>针对：Google · Bing</sub><br><sub>更新于 2026-11-14 · 英文 · MIT</sub>

- **[ai-visibility-tracking-strategy-builder](https://github.com/rebelytics/ai-visibility-tracking-strategy-builder)** · ★ 3<br>设计 AI 可见度追踪方案的方法论 skill：提示词集、分组、品牌名单和报告拆法，不挑监测平台<br><sub>针对：Google AI 概览 · ChatGPT · Perplexity · Gemini</sub><br><sub>更新于 2026-11-16 · 英文 · CC-BY-4.0</sub>

- **[aizaloapp/aeorank](https://github.com/aizaloapp/aeorank)** · ★ 3<br>AEORank 的 SEO/AEO/GEO 诊断 skill：62 条技术规则加语义维度，查 Perplexity 和 AI 模式的引用，调它的接口或 MCP<br><sub>针对：Google · Google AI 概览 · Perplexity</sub><br><sub>更新于 2026-11-16 · 英文 · 2 个 skill</sub><br><sub>💡 调 AEORank 的托管接口，按额度收费</sub>

- **[get-cited-by-ai](https://github.com/paultaki/get-cited-by-ai)** · ★ 3<br>让 AI 搜索引用你的 GEO skill：每条规则都来自作者七个站 2.6 万多次实测引用，先看有没有需求再动手<br><sub>针对：Bing</sub><br><sub>更新于 2026-11-13 · 英文 · MIT</sub>

- **[llms-txt-writer](https://github.com/shimo4228/llms-txt-writer)** · ★ 3<br>写和检查只给 AI 读的文档（llms.txt、llms-full.txt、FAQ、术语表），本地脚本按 AI 引用研究的阈值给草稿打分<br><sub>针对：ChatGPT · Perplexity · Gemini</sub><br><sub>更新于 2026-11-15 · 英文 · MIT</sub>


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
# limelit-co/open
npx skills add limelit-co/open
# GetCito
npx skills add ai-search-guru/getcito-worlds-first-open-source-aio-aeo-or-geo-tool
# voyage-geo-agent
npx skills add onvoyage-ai/voyage-geo-agent
# geo-aeo-tracker
npx skills add danishashko/geo-aeo-tracker
# geo-first-principles
npx skills add ALLENLION35/geo-first-principles
# SEO-GEO-AEO-Skill
npx skills add SNLabat/SEO-GEO-AEO-Skill
# geoptimize
npx skills add cucuwang/geoptimize
# ansvisor
npx skills add ansvisor/ansvisor
# GEO-Content-Optimizer-Skill
npx skills add liangdabiao/GEO-Content-Optimizer-Skill
# eGEOagents
npx skills add mverab/eGEOagents
# canonry
npx skills add Canonry/canonry
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
# seo-skills/geo-audit-skill
npx skills add seo-skills/geo-audit-skill
# geo-score
npx skills add jianruntech/geo-score
# geoskills
npx skills add Cognitic-Labs/geoskills
# agentmarkup
npx skills add agentmarkup/agentmarkup
# aicw-ai-mentions
npx skills add aichatwatch/aicw-ai-mentions
# agent-lighthouse
npx skills add ForkPoint/agent-lighthouse
# topcited-skills
npx skills add TopCited/topcited-skills
# agent-readiness
npx skills add Canonry/agent-readiness
# foreign-trade-geo-skill
npx skills add Elvinaskill/foreign-trade-geo-skill
# peec-ai-tracking-strategy-builder
npx skills add rebelytics/peec-ai-tracking-strategy-builder
# aeo-geo-bestpractices
npx skills add micaelgomestavares/aeo-geo-bestpractices
# aeo-toolkit
npx skills add Advance-Labs/aeo-toolkit
# CiteLadder
npx skills add abhij1306/CiteLadder
# geo-skills
npx skills add aivisibilitycensus/geo-skills
# ai-search-audit-full
npx skills add Olexan-art/ai-search-audit-full
# ai-visibility-tracking-strategy-builder
npx skills add rebelytics/ai-visibility-tracking-strategy-builder
# aizaloapp/aeorank
npx skills add aizaloapp/aeorank
# get-cited-by-ai
npx skills add paultaki/get-cited-by-ai
# llms-txt-writer
npx skills add shimo4228/llms-txt-writer
```

</details>

<a id="group-cn-ai"></a>
### 中文 AI 搜索：豆包、元宝、Kimi、DeepSeek、千问

针对中文 AI 助手和百度的优化。这几家抓取规则和英文 AI 搜索不一样，比如 GitHub 禁止字节的爬虫抓取，豆包很难直接读到 GitHub 页面，要靠站外内容。

- 🌟 **[yao-geo-skills](https://github.com/yaojingang/yao-geo-skills)** · ★ 920<br>Yao GEO Skills：24 个 GEO skill，管战略诊断、页面技术、内容生产、知识资产、监测归因和拓词，能抓豆包、DeepSeek 的回答<br><sub>针对：百度 · ChatGPT · 豆包 · 元宝 · Kimi · DeepSeek · 千问</sub><br><sub>更新于 2026-10-01 · 多语言 · 24 个 skill · MIT</sub>

- **[geo-doctor](https://github.com/Fangx-AI/geo-doctor)** · ★ 609<br>GEO 医生：查豆包、DeepSeek、ChatGPT、Claude 推荐了哪些竞品、为什么不是你、读了哪些网站，再批量写内容并复查推荐率<br><sub>针对：ChatGPT · Perplexity · Gemini · Claude · 豆包 · 元宝 · Kimi · DeepSeek · 千问</sub><br><sub>更新于 2026-11-09 · 多语言 · MIT</sub>

- **[HeiGe-GEO-SEO](https://github.com/HeiGeAi/HeiGe-GEO-SEO)** · ★ 95<br>中国市场优先的 GEO 加 SEO：让内容被豆包、千问、DeepSeek、文心、元宝和 ChatGPT、Perplexity 抓取引用，零依赖<br><sub>针对：百度 · ChatGPT · Perplexity · Gemini · Claude · 豆包 · 元宝 · DeepSeek · 千问</sub><br><sub>更新于 2026-10-15 · 多语言 · 2 个 skill · MIT</sub>

- **[GEOVisibilityTool](https://github.com/MasashiToda1/GEOVisibilityTool)** · ★ 50<br>测品牌在 AI 搜索里的可见度：生成 30 个测试问题，到 Kimi、豆包、DeepSeek、文心等网页端真问，算可见度分，出报告和投放建议<br><sub>针对：百度 · 豆包 · 元宝 · Kimi · DeepSeek · 千问</sub><br><sub>更新于 2026-06-07 · 中文 · 7 个 skill · Apache-2.0</sub>

- **[geo-automation-skill-pack](https://github.com/noahneancy-byte/geo-automation-skill-pack)** · ★ 37<br>豆包 GEO 自动化：客户诊断、关键词挖掘、写稿，改成头条、搜狐、知乎、36 氪等平台版本，再监测豆包引用并复盘<br><sub>针对：豆包</sub><br><sub>更新于 2026-08-30 · 中文 · 5 个 skill</sub>


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

- 🌟 **[open-seo](https://github.com/every-app/open-seo)** · ★ 27.8k<br>开源版 Semrush/Ahrefs：关键词研究和聚类、竞品分析、外链挖掘、本地 SEO、站点审计和 AI 可见度，自带给 agent 用的 skill<br><sub>针对：通用</sub><br><sub>更新于 2026-11-13 · 英文 · 28 个 skill · MIT</sub><br><sub>💡 skill 接 OpenSEO：自己部署要 DataForSEO 的 Key（按用量付费），也有托管版</sub>

- **[open-seo-mcp-skills](https://github.com/Ryze-AI-Adgent/open-seo-mcp-skills)** · ★ 10k<br>免费 SEO MCP 加开源 SEO/GEO skill：用你真实的 Search Console、GA4 和广告数据做关键词、排名、审计、外链和 AI 可见度<br><sub>针对：Google · ChatGPT · Perplexity · Gemini · Claude</sub><br><sub>更新于 2026-10-27 · 英文 · 8 个 skill · MIT</sub><br><sub>💡 数据经 Ryze 托管的 MCP，用 Google 账号授权</sub>

- **[seo](https://github.com/iannuttall/seo)** · ★ 628<br>SEO 命令行和 MCP：让 agent 读你的 Search Console、GA4 和 Bing 数据，标出 Google 更新日期，带 70 多个审计工具<br><sub>针对：Google · Bing</sub><br><sub>更新于 2026-11-15 · 英文 · 2 个 skill · Apache-2.0</sub>

- **[bisibility](https://github.com/CorgiCorner/bisibility)** · ★ 605<br>开源 SEO 平台：追踪 Google 排名、研究关键词、查外链，附 20 个 skill 做聚类、竞品、本地 SEO 和 AI 可见度<br><sub>针对：Google</sub><br><sub>更新于 2026-11-13 · 英文 · 20 个 skill · AGPL-3.0</sub><br><sub>💡 要自己部署 Bisibility 或用托管版，数据用你自己的数据商 Key</sub>

- **[saas-growth-agents](https://github.com/Pluviobyte/saas-growth-agents)** · ★ 541<br>出海站增长 Bot：每天早中晚扫新搜索词，按词找竞品站、查它们的外链和 DR，自动提交免费导航站<br><sub>针对：Google</sub><br><sub>更新于 2026-11-10 · 中文 · 5 个 skill · MIT</sub><br><sub>💡 数据都走 AIsa（按次付费，README 里是作者的邀请链接）；按 Grok Bot 这类常驻 agent 写的，Claude Code、Codex 要自己配定时任务</sub>

- **[seo-skills](https://github.com/seranking/seo-skills)** · ★ 210<br>SE Ranking 官方的 32 个 SEO skill：内容简报、AI 搜索声量、审计、外链缺口、关键词聚类、结构化数据，接它的 MCP<br><sub>针对：Google · Google AI 概览 · ChatGPT · Perplexity · Gemini</sub><br><sub>更新于 2026-11-05 · 英文 · 32 个 skill · MIT</sub><br><sub>💡 要 SE Ranking 的付费账号</sub>

- **[dataforseo-claude](https://github.com/zubair-trabzada/dataforseo-claude)** · ★ 178<br>接 DataForSEO 的 13 个 skill 和 5 个子 agent：关键词、排名追踪、外链审计、技术爬取、竞品分析，出 PDF 报告<br><sub>针对：Google</sub><br><sub>更新于 2026-05-20 · 英文 · 16 个 skill · MIT</sub><br><sub>💡 要 DataForSEO 账号，按量付费</sub>

- **[OpenGSC](https://github.com/fenjo26/OpenGSC)** · ★ 58<br>自己部署的 Search Console 面板：排名追踪、关键词研究、AI 可见度审计和内容生产，自带 105 个工具的 MCP 和 8 个 skill<br><sub>针对：Google · Bing · Yandex</sub><br><sub>更新于 2026-11-16 · 英文 · 8 个 skill · MIT</sub><br><sub>💡 要自己部署（VPS、你自己的 API Key）；还带 PBN、索引器网络这类灰帽外链功能</sub>

- **[zens-ink-seo-package](https://github.com/ZensInk/zens-ink-seo-package)** · ★ 57<br>给独立开发者的免费关键词研究工具：20 个命令行查关键词、难度、竞品差距和排名，纯 Python，附 9 个 skill<br><sub>针对：Google · Bing</sub><br><sub>更新于 2026-11-16 · 英文 · 9 个 skill · MIT</sub><br><sub>💡 搜索量要免费的 Bing 站长 Key</sub>

- **[duckduckdeploy/openseo](https://github.com/duckduckdeploy/openseo)** · ★ 52<br>开源版 Ahrefs、Semrush（openseo.gg）：站点审计、关键词、排名、外链、AI 概览和本地排名，附 7 个 skill 走它的 MCP<br><sub>针对：Google · Google AI 概览</sub><br><sub>更新于 2026-10-31 · 英文 · 7 个 skill · MIT</sub><br><sub>💡 skill 接它的 MCP：可自己部署或用托管版，查数据按次付费</sub>

- **[seo-party-skills](https://github.com/every-app/seo-party-skills)** · ★ 50<br>OpenSEO 的实验性 skill：认领 ChatGPT 商家资料、竞品策略、客户搜索词、关键词缺口、高价值页面、AI 排名和拆解别人的 SEO<br><sub>针对：Google · ChatGPT</sub><br><sub>更新于 2026-11-12 · 英文 · 9 个 skill · MIT</sub><br><sub>💡 都要先接 OpenSEO 的 MCP，部分要付费版</sub>

- **[autoseo](https://github.com/codextde/autoseo)** · ★ 25<br>开源 AI SEO/GEO 平台：追踪品牌在各家 AI 回答里的表现，加关键词研究、排名追踪、站点审计和外链，附 17 个 skill<br><sub>针对：Google · Google AI 概览 · ChatGPT · Perplexity · Gemini · Claude</sub><br><sub>更新于 2026-11-07 · 英文 · 17 个 skill</sub><br><sub>💡 要自己部署 AutoSEO（免费）或用它的云服务（每月 50 美元）</sub>

- **[seo-signal-skills](https://github.com/daily-growth-signals/seo-signal-skills)** · ★ 14<br>SignalDig 的调研 skill：查关键词需求、相关搜索、SERP、趋势、竞品、GEO 可见度和外链，也查 X、Reddit、小红书、知乎的公开讨论<br><sub>针对：通用</sub><br><sub>更新于 2026-11-16 · 多语言 · MIT</sub><br><sub>💡 要 SignalDig 的 API Key，接它的 MCP</sub>

- **[seo-utils-skills](https://github.com/seoutilsapp/seo-utils-skills)** · ★ 12<br>SEO Utils 的 MCP 使用指南：教 agent 分清查本地数据、付费查询和写操作，查排名报告、竞品关键词、关键词蚕食时选对工具<br><sub>针对：Google</sub><br><sub>更新于 2026-11-14 · 英文 · 2 个 skill</sub><br><sub>💡 要先装 SEO Utils 桌面应用并打开它的 MCP；付费查询走 DataForSEO 额度</sub>

- **[gscdump](https://github.com/harlan-zw/gscdump)** · ★ 10<br>把整个 Search Console 数据导到本地，命令行和 MCP 出 JSON 报告，让 agent 从里面找洞察、改进 SEO<br><sub>针对：Google</sub><br><sub>更新于 2026-11-16 · 英文 · 2 个 skill · MIT</sub>

- **[ubersuggest/seo-skills](https://github.com/ubersuggest/seo-skills)** · ★ 7<br>Ubersuggest 官方 SEO skill：关键词研究、竞品、内容简报、找内容需求、站点审计、AI 可见度和行动计划<br><sub>针对：通用</sub><br><sub>更新于 2026-10-30 · 英文 · 9 个 skill · Apache-2.0</sub><br><sub>💡 9 个里 8 个要接 Ubersuggest 的 MCP，用它的账号</sub>

- **[Manifold](https://github.com/manifoldmcp/marketing-skills)** · ★ 5<br>免费托管的营销数据 MCP 加 skill：Google 搜索、AI 回答、Search Console、地图、应用商店、亚马逊，也有社媒和广告库<br><sub>针对：Google · ChatGPT · 应用商店 · 电商站内搜索</sub><br><sub>更新于 2026-11-11 · 英文 · 26 个 skill · MIT</sub><br><sub>💡 MCP 由 Manifold 托管，要用它的账号登录，每月有免费额度</sub>

- **[seo-gsc-ga4-analyst](https://github.com/owensky-dev/seo-gsc-ga4-analyst)** · ★ 5<br>Codex 的 SEO 数据分析 skill：合并 Search Console 搜索表现和 GA4 自然流量、关键行为，在本地出周报和行动清单<br><sub>针对：Google</sub><br><sub>更新于 2026-11-15 · 多语言</sub>

- **[agenticseo](https://github.com/kid7st/agenticseo)** · ★ 3<br>给编程 agent 的本地 SEO 命令行加 10 个 skill：关键词、竞品、外链、本地 SEO、排名追踪和站点审计，不用服务器<br><sub>针对：Google</sub><br><sub>更新于 2026-11-12 · 英文 · 10 个 skill · MIT</sub><br><sub>💡 skill 改编自 OpenSEO；付费查询走 DataForSEO，按次付费</sub>

- **[yandex-wordstat](https://github.com/prikotov/yandex-wordstat)** · ★ 3<br>俄语 Yandex Wordstat skill：查词的搜索量、相似词、按天周月的走势和地区分布，出 CSV 和 Markdown<br><sub>针对：Yandex</sub><br><sub>更新于 2026-11-13 · 俄文</sub><br><sub>💡 要 Yandex Cloud 服务账号的 Search API Key</sub>

- **[zaDojo](https://github.com/zaDojo/seo-geo-mcp)** · ★ 2<br>zaDojo 的 12 个 SEO/GEO skill，接它托管的 MCP：关键词、实时 SERP、竞品、外链、站点审计、排名追踪、本地 SEO、AI 可见度<br><sub>针对：Google · Google AI 概览 · ChatGPT · Perplexity · Gemini</sub><br><sub>更新于 2026-10-29 · 英文 · 12 个 skill · MIT</sub><br><sub>💡 接 zaDojo 托管的 MCP，用他家账号登录；Search Console 和 GA4 免费，其余按用量扣费，月费 10 欧元含 10 欧元用量</sub>

- **[crakseo-mcp-plugins](https://github.com/CrakSEO/crakseo-mcp-plugins)** · ★ 0<br>CrakSEO 的 SEO 插件：查关键词、实时 SERP、外链、排名追踪、站点审计、本地 SEO、AI 可见度、收录提交和 Search Console<br><sub>针对：Google · Google AI 概览 · Bing · ChatGPT · Perplexity</sub><br><sub>更新于 2026-11-09 · 英文 · 10 个 skill · MIT</sub><br><sub>💡 接 CrakSEO 自家托管的 MCP，用他家账号登录，查数据扣预付积分；Search Console 和 Bing 站长那个免费</sub>


<details><summary>安装命令</summary>

```bash
# 默认命令基于 skills CLI，未逐个验证，以各仓库 README 为准
# open-seo
npx skills add every-app/open-seo
# open-seo-mcp-skills
npx skills add Ryze-AI-Adgent/open-seo-mcp-skills
# seo
npx skills add iannuttall/seo
# bisibility
npx skills add CorgiCorner/bisibility
# saas-growth-agents
npx skills add Pluviobyte/saas-growth-agents
# seo-skills
npx skills add seranking/seo-skills
# dataforseo-claude
npx skills add zubair-trabzada/dataforseo-claude
# OpenGSC
npx skills add fenjo26/OpenGSC
# zens-ink-seo-package
npx skills add ZensInk/zens-ink-seo-package
# duckduckdeploy/openseo
npx skills add duckduckdeploy/openseo
# seo-party-skills
npx skills add every-app/seo-party-skills
# autoseo
npx skills add codextde/autoseo
# seo-signal-skills
npx skills add daily-growth-signals/seo-signal-skills
# seo-utils-skills
npx skills add seoutilsapp/seo-utils-skills
# gscdump
npx skills add harlan-zw/gscdump
# ubersuggest/seo-skills
npx skills add ubersuggest/seo-skills
# Manifold
npx skills add manifoldmcp/marketing-skills
# seo-gsc-ga4-analyst
npx skills add owensky-dev/seo-gsc-ga4-analyst
# agenticseo
npx skills add kid7st/agenticseo
# yandex-wordstat
npx skills add prikotov/yandex-wordstat
# zaDojo
npx skills add zaDojo/seo-geo-mcp
# crakseo-mcp-plugins
npx skills add CrakSEO/crakseo-mcp-plugins
```

</details>

<a id="group-content"></a>
### 内容写作和优化

写和改 SEO 文章、标题和描述、内容简报，按 E-E-A-T 补证据。

- 🌟 **[seomachine](https://github.com/TheCraigHewitt/seomachine)** · ★ 7.6k<br>写 SEO 长文的 Claude Code 工作区：调研、写稿、改写、分析和优化，带竞品对比页、内容策略等 26 个 skill<br><sub>针对：Google</sub><br><sub>更新于 2026-10-23 · 英文 · 26 个 skill · MIT</sub>

- **[claude-blog](https://github.com/AgriciDaniel/claude-blog)** · ★ 2.8k<br>博客写作全套：31 个子 skill、5 个 agent 写、改、审、本地化和更新文章，同时照顾 Google 排名和 AI 引用，交付前过 5 道关<br><sub>针对：Google · Google AI 概览 · ChatGPT · Perplexity · Gemini</sub><br><sub>更新于 2026-11-03 · 英文 · 33 个 skill · MIT</sub>

- **[superseo-skills](https://github.com/inhouseseo/superseo-skills)** · ★ 397<br>11 个 SEO skill：页面审计、内容简报、写文章、E-E-A-T 审计、语义缺口、外链计划和专家访谈，不要 API Key<br><sub>针对：Google</sub><br><sub>更新于 2026-09-03 · 英文 · 11 个 skill · Apache-2.0</sub>

- **[seobuild-onpage](https://github.com/gbessoni/seobuild-onpage)** · ★ 267<br>一条命令写出能排名的页面：拉当前 SERP、分析排名靠前的内容、找缺口，写成完整页面，兼顾 Google 和 AI 引用<br><sub>针对：Google · Google AI 概览 · ChatGPT · Perplexity · Gemini</sub><br><sub>更新于 2026-11-12 · 英文 · MIT</sub><br><sub>💡 SERP 和竞品数据来自 DataForSEO，按量付费</sub>

- **[geo-content-writer](https://github.com/dageno-agents/geo-content-writer)** · ★ 217<br>按选题清单逐行生产内容：每一行从调研、写稿到复查，适合团队持续做 GEO 和 SEO 内容，而不是一次性生成<br><sub>针对：通用</sub><br><sub>更新于 2026-07-06 ⚠️ · 多语言 · MIT</sub>

- **[dispatchseo](https://github.com/NeoZi12/dispatchseo)** · ★ 99<br>开源版 SEObot/Outrank：让 agent 当 SEO 经理，做关键词研究、写文章并发布，可以整夜无人值守地批量产出<br><sub>针对：Google</sub><br><sub>更新于 2026-11-15 · 英文 · 2 个 skill · AGPL-3.0</sub><br><sub>💡 配合 DispatchSEO 服务用（可 Docker 自己部署）；无人值守写稿跑在你仓库的 GitHub Actions 里，要存你的 Claude Code 或 OpenAI 凭据</sub>

- **[Awesome_SEO_Writing_Skill](https://github.com/flaqai/Awesome_SEO_Writing_Skill)** · ★ 91<br>Flaq AI 的 SEO 写作 skill：两年 SEO 写作、核查、配图和发布经验，另有 LinkedIn、Medium 和公众号版本<br><sub>针对：Google</sub><br><sub>更新于 2026-08-13 · 英文 · 4 个 skill · MIT</sub>

- **[pseo-skills](https://github.com/lisbeth718/pseo-skills)** · ★ 57<br>程序化 SEO（pSEO）全套：批量页面的数据、发现和审计，另有多语言站、改版迁移、日志分析和内容修剪<br><sub>针对：Google</sub><br><sub>更新于 2026-10-28 · 英文 · 18 个 skill · MIT</sub>

- **[contentforge](https://github.com/indranilbanerjee/contentforge)** · ★ 33<br>长文内容生产系统：10 步流程调研、核实、写稿、去 AI 腔、加内链，出可发布的 Word 稿，发布后再查 AI 引用和内容老化<br><sub>针对：通用</sub><br><sub>更新于 2026-11-07 · 英文 · 22 个 skill · MIT</sub>

- **[skill-seo-co-ban](https://github.com/ibangtam/skill-seo-co-ban)** · ★ 7<br>越南语 SEO 写作 3 件套：关键词研究、照 Google 前几名列大纲、写带出处的文章，不用付费 SEO 工具<br><sub>针对：Google</sub><br><sub>更新于 2026-11-09 · 越南文 · 3 个 skill · MIT</sub>

- **[altorank](https://github.com/AltoRank/altorank)** · ★ 6<br>开源版 Outrank：研究关键词、写文章、打分并核实数字出处，导出 Markdown 或 HTML 或发到 CMS，每次发布都要人批，附 skill<br><sub>针对：Google</sub><br><sub>更新于 2026-11-16 · 英文 · 2 个 skill · AGPL-3.0</sub><br><sub>💡 要自己部署 AltoRank（免费）或用它的托管版</sub>

- **[sayiyla-seo-ajan](https://github.com/sayiyla/sayiyla-seo-ajan)** · ★ 6<br>土耳其语 SEO/AEO/GEO 改稿 agent：改网页标题、描述、开头答案和 FAQ，写社媒说明，附站点审计和检查命令行<br><sub>针对：Google · Yandex</sub><br><sub>更新于 2026-11-08 · 土耳其文 · MIT</sub><br><sub>💡 是 Claude Code 子 agent 加 Node 命令行，没有 SKILL.md；Codex 读仓库里的 AGENTS.md</sub>

- **[rankcontrol](https://github.com/rankcontrol/rankcontrol)** · ★ 5<br>RankControl 的命令行 skill：查 AI 搜索可见度和引用，规划和生成 SEO 文章并发到你的 CMS，管外链外联和报告<br><sub>针对：Google · Google AI 概览 · ChatGPT · Perplexity · Gemini · Claude</sub><br><sub>更新于 2026-11-13 · 英文 · 2 个 skill · MIT</sub><br><sub>💡 要有 RankControl 账号</sub>

- **[rankmath-seo-wp](https://github.com/Moksa1123/rankmath-seo-wp)** · ★ 5<br>写 Rank Math 能打 80 分以上的 WordPress 文章：输出能直接粘进区块编辑器的 Gutenberg 区块，含 HowTo、FAQ 等区块<br><sub>针对：Google</sub><br><sub>更新于 2026-11-15 · 多语言 · MIT</sub>

- **[research-first-writer](https://github.com/jayanti-prajapati/research-first-writer)** · ★ 5<br>先研究再写的文章 skill：看真实排名页缺什么、每个数字记出处，不编“我们测过”，写给 Google 排名和 AI 引用<br><sub>针对：Google · Google AI 概览 · ChatGPT · Perplexity</sub><br><sub>更新于 2026-11-07 · 英文 · MIT</sub>

- **[seranking/marketing-automation-plugins](https://github.com/seranking/marketing-automation-plugins)** · ★ 4<br>SE Ranking 和 Planable 的营销 skill：内容简报、编辑计划、旧文刷新、AI 可见度对标、对比页，另有投放和社媒<br><sub>针对：通用</sub><br><sub>更新于 2026-11-16 · 英文 · 38 个 skill</sub><br><sub>💡 要 SE Ranking 的 API，社媒部分要 Planable</sub>

- **[IndexGap](https://github.com/borisowlexa2010-star/IndexGap)** · ★ 3<br>批量生成页面（programmatic SEO）发布前的质检：查编造的数字、整批模板出错、近似重复和 hreflang，中英俄输出<br><sub>针对：Google · Bing · Yandex</sub><br><sub>更新于 2026-11-16 · 多语言 · 6 个 skill · MIT</sub>


<details><summary>安装命令</summary>

```bash
# 默认命令基于 skills CLI，未逐个验证，以各仓库 README 为准
# seomachine
npx skills add TheCraigHewitt/seomachine
# claude-blog
npx skills add AgriciDaniel/claude-blog
# superseo-skills
npx skills add inhouseseo/superseo-skills
# seobuild-onpage
npx skills add gbessoni/seobuild-onpage
# geo-content-writer
npx skills add dageno-agents/geo-content-writer
# dispatchseo
npx skills add NeoZi12/dispatchseo
# Awesome_SEO_Writing_Skill
npx skills add flaqai/Awesome_SEO_Writing_Skill
# pseo-skills
npx skills add lisbeth718/pseo-skills
# contentforge
npx skills add indranilbanerjee/contentforge
# skill-seo-co-ban
npx skills add ibangtam/skill-seo-co-ban
# altorank
npx skills add AltoRank/altorank
# sayiyla-seo-ajan
npx skills add sayiyla/sayiyla-seo-ajan
# rankcontrol
npx skills add rankcontrol/rankcontrol
# rankmath-seo-wp
npx skills add Moksa1123/rankmath-seo-wp
# research-first-writer
npx skills add jayanti-prajapati/research-first-writer
# seranking/marketing-automation-plugins
npx skills add seranking/marketing-automation-plugins
# IndexGap
npx skills add borisowlexa2010-star/IndexGap
```

</details>

<a id="group-technical"></a>
### 技术 SEO 和站点审计

爬站审计、结构化数据、站点地图、速度、索引问题。

- 🌟 **[web-quality-skills](https://github.com/addyosmani/web-quality-skills)** · ★ 3.1k<br>Addy Osmani 的网页质量 skill：按 Lighthouse 和 Core Web Vitals 优化性能、无障碍、最佳实践和 SEO，先测量再改<br><sub>针对：Google</sub><br><sub>更新于 2026-08-24 · 英文 · 6 个 skill · MIT</sub>

- **[seo-ops](https://github.com/tigerless-labs/seo-ops)** · ★ 989<br>SEO 基础检查：给一个网址，像爬虫一样抓取，跑 26 项结构检查，出带证据的通过/不通过报告，不调模型<br><sub>针对：通用</sub><br><sub>更新于 2026-11-06 · 英文 · 2 个 skill</sub>

- **[specification.website](https://github.com/jdevalk/specification.website)** · ★ 925<br>Joost de Valk 的网站规范：185 页讲 HTML、无障碍、安全、SEO、agent 就绪该怎么做，每条注出处，skill 和 MCP 供对照<br><sub>针对：通用</sub><br><sub>更新于 2026-11-16 · 英文</sub>

- **[seo-audit-skill](https://github.com/JeffLi1993/seo-audit-skill)** · ★ 788<br>单页 SEO 审计：给网址出 HTML 报告，脚本做确定性检查、模型判断关键词意图和内容质量，分入门和进阶两档<br><sub>针对：Google</sub><br><sub>更新于 2026-06-17 · 多语言 · 2 个 skill · MIT</sub>

- **[seo-skills/seo-audit-skill](https://github.com/seo-skills/seo-audit-skill)** · ★ 670<br>SEOmator 审计：按 20 类 373 条规则扫网站，含技术 SEO、Core Web Vitals、结构化数据、安全头和 AI 搜索就绪度<br><sub>针对：通用</sub><br><sub>更新于 2026-11-12 · 英文 · 2 个 skill · MIT</sub>

- **[Seo-Promt-Master](https://github.com/umutxyp/Seo-Promt-Master)** · ★ 587<br>把 Google SEO 官方文档做成审计 skill：列出项目的全部公开路由，逐页对照 Google、Bing 和 AI 爬虫的规则检查并修复<br><sub>针对：Google · Bing</sub><br><sub>更新于 2026-11-11 · 英文 · MIT</sub>

- **[seo-landing](https://github.com/aleksandr-alhoff/seo-landing)** · ★ 212<br>让 agent 像资深技术 SEO 一样做落地页：PageSpeed 冲 100 分、Core Web Vitals、完整结构化数据、AVIF 图片<br><sub>针对：Google</sub><br><sub>更新于 2026-10-21 · 英文 · MIT</sub>

- **[seo-geo-audit](https://github.com/dageno-agents/seo-geo-audit)** · ★ 177<br>给品牌、SaaS 团队和代理商的 SEO 加 GEO 审计流程，同时看传统搜索和 AI 搜索<br><sub>针对：Google · Google AI 概览 · Bing · ChatGPT · Perplexity · Gemini</sub><br><sub>更新于 2026-08-19 ⚠️ · 多语言 · MIT</sub>

- **[claude-code-seo](https://github.com/huifer/claude-code-seo)** · ★ 111<br>Next.js 项目的 SEO 助手插件：6 个维度 100 分制审计，管元数据、结构化数据、E-E-A-T、内容策略、本地 SEO 和外链<br><sub>针对：Google</sub><br><sub>更新于 2026-01-04 💤 · 中文 · 12 个 skill · MIT</sub>

- **[jdevalk/skills](https://github.com/jdevalk/skills)** · ★ 110<br>Yoast 创始人 Joost de Valk 的 skill：审计和改进 GitHub 主页、WordPress 插件页、Astro 站 SEO 和文章可读性<br><sub>针对：通用</sub><br><sub>更新于 2026-07-05 · 英文 · 12 个 skill · MIT</sub>

- **[squirrelscan/skills](https://github.com/squirrelscan/skills)** · ★ 109<br>squirrelscan 网站审计的 skill：爬全站，按 SEO、性能、安全、无障碍、内容等 300 多条规则打分，列出能修的问题<br><sub>针对：通用</sub><br><sub>更新于 2026-11-12 · 英文 · 2 个 skill · MIT</sub><br><sub>💡 要装 squirrelscan 命令行并登录，按额度使用</sub>

- **[jev-seo](https://github.com/AkashPriyadarshii/jev-seo)** · ★ 102<br>免费的 Rust SEO/GEO 命令行：64 条规则审计、爬站、AI 引用打分、排名漂移、CI 门禁，带 MCP，skill 直接调它<br><sub>针对：Google · ChatGPT · Perplexity</sub><br><sub>更新于 2026-11-11 · 英文 · 2 个 skill · MIT</sub><br><sub>💡 要先装 jev-seo（cargo 或发布包）；可选接作者的 TypeSafe Jev 付费服务</sub>

- **[claude-seo-ai](https://github.com/Hainrixz/claude-seo-ai)** · ★ 87<br>SEO 和 AI 可见度分开打两个分：审计任意网站的传统搜索表现和 GEO/AEO，你同意后自动做安全的修复<br><sub>针对：Google · Google AI 概览 · ChatGPT · Perplexity · Gemini · Claude</sub><br><sub>更新于 2026-10-25 · 英文 · 34 个 skill · MIT</sub>

- **[vercel-seo-audit](https://github.com/JosephDoUrden/vercel-seo-audit)** · ★ 81<br>查 Next.js 和 Vercel 网站为什么不被 Google 收录：按服务器实际返回查流式元数据、跳转、robots、sitemap 等<br><sub>针对：Google</sub><br><sub>更新于 2026-11-13 · 英文 · MIT</sub>

- **[southwellmedia/seo-audit](https://github.com/southwellmedia/seo-audit)** · ★ 54<br>给服务类企业做 SEO 审计和竞品分析，出能直接发给客户的 PDF 提案：关键词、技术和 AI 可见度、内容策略、快速见效项<br><sub>针对：Google · Google AI 概览 · ChatGPT · Perplexity</sub><br><sub>更新于 2026-11-16 · 英文</sub>

- **[openspider](https://github.com/wojcikdominik/openspider)** · ★ 47<br>面向 agent 的开源网站爬虫和技术 SEO 审计（macOS、Windows），Rust 加 Tauri，自带 MCP，agent 默认只读，开爬要你授权<br><sub>针对：通用</sub><br><sub>更新于 2026-11-16 · 英文 · Apache-2.0</sub><br><sub>💡 要先装 OpenSpider（桌面版或命令行）</sub>

- **[fat-agent-skill](https://github.com/spruikco/fat-agent-skill)** · ★ 40<br>网站上线后的检查 agent：审计 SEO、AI 爬虫权限、安全、无障碍、性能、本地 SEO 等，再一项项带你修<br><sub>针对：Google · Google AI 概览</sub><br><sub>更新于 2026-10-30 · 英文 · 2 个 skill · MIT</sub><br><sub>💡 可选的 ctx 工具要用 curl \| sh 装，skill 会先问你，不装也能用</sub>

- **[launch-seo-skill](https://github.com/iamjeeth/launch-seo-skill)** · ★ 21<br>网站上线后要做的 10 件 SEO 事：Search Console、GA、robots.txt、sitemap、标题描述、Bing 站长工具等，能改就改<br><sub>针对：Google · Bing</sub><br><sub>更新于 2026-11-16 · 英文</sub><br><sub>💡 第 10 项推荐作者自己的 scorebadge.com，会先问你，可以跳过</sub>

- **[99-website](https://github.com/NicoSKOOL/99-website)** · ★ 19<br>用 Claude Code 建 Lighthouse 99 分的 SEO 网站（Astro 加 Cloudflare）：按关键词定结构、配图、审计、部署<br><sub>针对：Google</sub><br><sub>更新于 2026-11-15 · 英文 · 12 个 skill</sub><br><sub>💡 关键词数据接 DataForSEO（按量付费）</sub>

- **[SoDam-SeoMedic](https://github.com/sodam-ai/SoDam-SeoMedic)** · ★ 16<br>韩语的 SEO/GEO 诊断插件：爬取、渲染、CWV、结构化数据、AI 爬虫策略，接 Search Console 和 GA4，能自动修 Next.js<br><sub>针对：Google · Bing · ChatGPT · Perplexity</sub><br><sub>更新于 2026-11-02 · 韩文 · Apache-2.0</sub>

- **[CodoSEO](https://github.com/SafrowLabs/CodoSEO)** · ★ 14<br>Rust 写的开源 SEO/GEO 监测和站点审计，Screaming Frog 和 Ahrefs 站点审计的替代，带 MCP 和审计 skill<br><sub>针对：通用</sub><br><sub>更新于 2026-11-10 · 英文 · AGPL-3.0</sub><br><sub>💡 要先装 CodoSEO</sub>

- **[seo-night-skill](https://github.com/IncomeStreamSurfer/seo-night-skill)** · ★ 10<br>修 AI 建的网站的 SEO 毛病：审计网站代码，把空泛的标题改成人们真搜的词，补缺的内容，每处改动一个提交，放在待审分支<br><sub>针对：Google</sub><br><sub>更新于 2026-11-14 · 英文</sub><br><sub>💡 关键词数据来自 Semrush，要它的账号</sub>

- **[legends-github](https://github.com/avalonreset/legends-github)** · ★ 9<br>GitHub 仓库的 SEO：审计仓库，按 Google 和 GitHub 的真实搜索需求改描述、话题、README 和社交预览图，再规范发版<br><sub>针对：Google</sub><br><sub>更新于 2026-11-14 · 英文 · MIT</sub><br><sub>💡 通过 cto-legends 调用；搜索需求数据走 DataForSEO（按量付费）</sub>

- **[pseolint](https://github.com/ouranos-labs/pseolint)** · ★ 8<br>程序化 SEO 发布前的检查：审页面之间的关系而不只是单页，防被 SpamBrain 当成垃圾页，AI 分诊问题，带 MCP<br><sub>针对：Google</sub><br><sub>更新于 2026-11-15 · 英文 · 7 个 skill · MIT</sub>

- **[seo-audit-skills](https://github.com/carlosuhart/seo-audit-skills)** · ★ 6<br>西班牙语技术 SEO 审计 41 个 skill：WordPress、PrestaShop、JS 框架、核心网页指标、Schema、GEO<br><sub>针对：Google</sub><br><sub>更新于 2026-11-01 · 西班牙文 · 41 个 skill · MIT</sub>

- **[one-step-seo](https://github.com/6t9xstar/one-step-seo)** · ★ 5<br>零依赖的 Node.js SEO 工具：技术审计、AI 搜索可见度（GEO/AEO）、自动修复和持续监测，附 24 个 skill<br><sub>针对：Google · Google AI 概览 · ChatGPT · Perplexity</sub><br><sub>更新于 2026-11-13 · 英文 · 25 个 skill · MIT</sub>

- **[pagination-independence-architecture](https://github.com/rebelytics/pagination-independence-architecture)** · ★ 5<br>进阶技术 SEO skill：让列表站的可收录价值不依赖分页，审计被分页孤立的条目，设计有搜索需求的子分类，再按类别修剪<br><sub>针对：Google</sub><br><sub>更新于 2026-11-16 · 英文 · CC-BY-4.0</sub>

- **[searvex](https://github.com/cihantopac/searvex)** · ★ 5<br>开源 SEO 和 AI 搜索审计：查网站或代码仓库，按根因归类问题，安全的部分自动修、可回滚，出离线 HTML 报告<br><sub>针对：通用</sub><br><sub>更新于 2026-11-16 · 英文 · 6 个 skill · Apache-2.0</sub>

- **[sitebulb-plugin](https://github.com/sitebulb/sitebulb-plugin)** · ★ 5<br>Sitebulb 官方 skill：基于你的 Sitebulb 审计数据，回答先修什么、这次爬取变了什么，出客户审计文档、开发工单和发版后检查<br><sub>针对：通用</sub><br><sub>更新于 2026-11-13 · 英文 · 5 个 skill · MIT</sub><br><sub>💡 要 Sitebulb 桌面版或云版（付费）的审计数据</sub>

- **[lighthouse-skill](https://github.com/nimajafari/lighthouse-skill)** · ★ 4<br>让 agent 跑 Google Lighthouse：测性能、无障碍、SEO 和最佳实践，设预算、卡 CI，改完再测一遍验证<br><sub>针对：Google</sub><br><sub>更新于 2026-11-13 · 英文 · MIT</sub>

- **[Quincunx33/ai-seo-skill](https://github.com/Quincunx33/ai-seo-skill)** · ★ 4<br>讲证据的 SEO 工程 skill：技术审计、结构化数据、页面体验，只在有仓库权限时改代码<br><sub>针对：通用</sub><br><sub>更新于 2026-11-07 · 英文 · MIT</sub>

- **[JakeLabate/Claude-SEO-Skills](https://github.com/JakeLabate/Claude-SEO-Skills)** · ★ 3<br>20 个技术 SEO 审计 skill：canonical、标题层级、内链、蚕食、llms.txt、robots、sitemap 等，导出 CSV 或 Word<br><sub>针对：Google</sub><br><sub>更新于 2026-11-15 · 英文 · 20 个 skill · MIT</sub>

- **[jorgejaramillo/seoskills](https://github.com/jorgejaramillo/seoskills)** · ★ 3<br>西班牙语 SEO 审计 skill：渲染抓取、robots.txt、站内审计、内链、图片、标题和描述，汇成一份网页报告<br><sub>针对：Google</sub><br><sub>更新于 2026-11-16 · 西班牙文 · 9 个 skill · MIT</sub><br><sub>💡 渲染抓取要 Cloudflare 账号（Browser Run），也可以直接读 sitemap</sub>

- **[seo-aeo-audit](https://github.com/ssheleg/seo-aeo-audit)** · ★ 3<br>审计网站在搜索引擎和 AI 回答里的可见度（Google、Bing、Yandex 和各家 AI），每个结论带来源证据，给排好优先级的修改计划<br><sub>针对：Google · Google AI 概览 · Bing · Yandex · ChatGPT · Perplexity · Gemini · Claude</sub><br><sub>更新于 2026-11-11 · 英文 · MIT</sub>

- **[seo-geo-smart-audit-skill](https://github.com/yangjing6213-dev/seo-geo-smart-audit-skill)** · ★ 3<br>独立站 SEO/GEO 只读巡检：查收录、robots、sitemap、canonical、结构化数据、AI 爬虫和 llms.txt，确认的和待补的分开写<br><sub>针对：Google · Bing · ChatGPT · Perplexity · Gemini · Claude</sub><br><sub>更新于 2026-11-02 · 中文 · Apache-2.0</sub>


<details><summary>安装命令</summary>

```bash
# 默认命令基于 skills CLI，未逐个验证，以各仓库 README 为准
# web-quality-skills
npx skills add addyosmani/web-quality-skills
# seo-ops
npx skills add tigerless-labs/seo-ops
# specification.website
npx skills add jdevalk/specification.website
# seo-audit-skill
npx skills add JeffLi1993/seo-audit-skill
# seo-skills/seo-audit-skill
npx skills add seo-skills/seo-audit-skill
# Seo-Promt-Master
npx skills add umutxyp/Seo-Promt-Master
# seo-landing
npx skills add aleksandr-alhoff/seo-landing
# seo-geo-audit
npx skills add dageno-agents/seo-geo-audit
# claude-code-seo
npx skills add huifer/claude-code-seo
# jdevalk/skills
npx skills add jdevalk/skills
# squirrelscan/skills
npx skills add squirrelscan/skills
# jev-seo
npx skills add AkashPriyadarshii/jev-seo
# claude-seo-ai
npx skills add Hainrixz/claude-seo-ai
# vercel-seo-audit
npx skills add JosephDoUrden/vercel-seo-audit
# southwellmedia/seo-audit
npx skills add southwellmedia/seo-audit
# openspider
npx skills add wojcikdominik/openspider
# fat-agent-skill
npx skills add spruikco/fat-agent-skill
# launch-seo-skill
npx skills add iamjeeth/launch-seo-skill
# 99-website
npx skills add NicoSKOOL/99-website
# SoDam-SeoMedic
npx skills add sodam-ai/SoDam-SeoMedic
# CodoSEO
npx skills add SafrowLabs/CodoSEO
# seo-night-skill
npx skills add IncomeStreamSurfer/seo-night-skill
# legends-github
npx skills add avalonreset/legends-github
# pseolint
npx skills add ouranos-labs/pseolint
# seo-audit-skills
npx skills add carlosuhart/seo-audit-skills
# one-step-seo
npx skills add 6t9xstar/one-step-seo
# pagination-independence-architecture
npx skills add rebelytics/pagination-independence-architecture
# searvex
npx skills add cihantopac/searvex
# sitebulb-plugin
npx skills add sitebulb/sitebulb-plugin
# lighthouse-skill
npx skills add nimajafari/lighthouse-skill
# Quincunx33/ai-seo-skill
npx skills add Quincunx33/ai-seo-skill
# JakeLabate/Claude-SEO-Skills
npx skills add JakeLabate/Claude-SEO-Skills
# jorgejaramillo/seoskills
npx skills add jorgejaramillo/seoskills
# seo-aeo-audit
npx skills add ssheleg/seo-aeo-audit
# seo-geo-smart-audit-skill
npx skills add yangjing6213-dev/seo-geo-smart-audit-skill
```

</details>

<a id="group-local"></a>
### 本地、电商和应用商店

地图和本地商家、商品页、应用商店优化（ASO）。

- **[aso-skills](https://github.com/appeeky/aso-skills)** · ★ 2.3k<br>应用商店优化（ASO）和 App 推广的 40 个 skill：关键词研究、元数据优化、竞品分析和市场情报<br><sub>针对：应用商店</sub><br><sub>更新于 2026-11-13 · 英文 · 40 个 skill · MIT</sub><br><sub>💡 数据来自 Appeeky API，要它的 Key</sub>

- **[amazon-sorftime-research-MCP-skill](https://github.com/liangdabiao/amazon-sorftime-research-MCP-skill)** · ★ 1.1k<br>亚马逊选品和竞品分析：单个 Listing 全维度拆解、全品类分析、关键词、差评和市场调研，接 Sorftime、西柚、卖家精灵等 MCP<br><sub>针对：电商站内搜索</sub><br><sub>更新于 2026-11-12 · 中文 · 9 个 skill</sub><br><sub>💡 数据来自 Sorftime 等付费服务</sub>

- **[Amazon-Skills](https://github.com/nexscope-ai/Amazon-Skills)** · ★ 870<br>给亚马逊卖家的 53 个免费 skill：关键词研究、竞品分析、Listing 审计和优化、FBA 计算、PPC 广告<br><sub>针对：电商站内搜索</sub><br><sub>更新于 2026-11-11 · 英文 · 52 个 skill · MIT</sub>

- **[mcp-google-map](https://github.com/cablate/mcp-google-map)** · ★ 499<br>Google 地图给 agent 用：18 个只读工具查地点和路线，走 MCP 或命令行，附本地 SEO skill 查商家在地图搜索里的可见度<br><sub>针对：Google</sub><br><sub>更新于 2026-10-22 · 英文 · 4 个 skill · MIT</sub><br><sub>💡 要 Google Maps Platform 的 API Key</sub>

- **[vibe-aso](https://github.com/Kronop/vibe-aso)** · ★ 480<br>从 Claude Code 做完 iOS 应用的 ASO：关键词研究、最多 50 个语种的商店元数据、本地化截图、全球定价和应用内本地化<br><sub>针对：应用商店</sub><br><sub>更新于 2026-08-12 · 英文 · MIT</sub>

- **[localseoskills](https://github.com/garrettjsmith/localseoskills)** · ★ 151<br>本地 SEO 的 38 个 skill：Google 商家资料、Bing Places、Apple 商家、评价管理、本地排名和 AI 本地搜索<br><sub>针对：Google · Google AI 概览 · Bing</sub><br><sub>更新于 2026-10-30 · 英文 · 39 个 skill · MIT</sub>

- **[legends-geogrid](https://github.com/avalonreset/legends-geogrid)** · ★ 59<br>Google 地图排名查询和本地排名追踪：审计 Google 商家资料，出环形网格地图和 18 页本地 SEO PDF 报告<br><sub>针对：Google</sub><br><sub>更新于 2026-11-12 · 英文 · MIT</sub><br><sub>💡 通过 cto-legends 调用；排名数据走 DataForSEO，按调用付费</sub>

- **[shopify-theme-audit-skill](https://github.com/tanujrajputdev/shopify-theme-audit-skill)** · ★ 45<br>90 秒审计 Shopify 主题的性能、SEO、AEO 和 GEO：80 多项检查，打分报告，给能直接粘贴的 Liquid 修复代码<br><sub>针对：Google · ChatGPT · Perplexity · Claude</sub><br><sub>更新于 2026-11-13 · 英文 · MIT</sub>

- **[etsy-listing-helper](https://github.com/silennsong/etsy-listing-helper)** · ★ 11<br>把按需印刷（POD）商品的规格和照片变成 Etsy 上架内容：标题、13 个 SEO 标签、描述、官方类目路径和属性<br><sub>针对：电商站内搜索</sub><br><sub>更新于 2026-11-11 · 英文 · MIT</sub>

- **[taobao-shop-growth](https://github.com/yuyang2230/taobao-shop-growth)** · ★ 10<br>淘宝千牛小店获客 skill：店铺诊断、改标题、补属性防流量受限、内容引流和批量自动化，方法在一家真实小店上跑通并标了实测结果<br><sub>针对：电商站内搜索</sub><br><sub>更新于 2026-11-12 · 中文 · MIT</sub>

- **[app-store-aso](https://github.com/TimBroddin/skills)** · ★ 7<br>苹果 App Store 的 ASO：按 Apple 规范和字数限制写应用名、副标题、描述和关键词，用脚本校验字数，附截图顺序建议<br><sub>针对：应用商店</sub><br><sub>更新于 2026-06-29 · 英文 · 5 个 skill</sub><br><sub>💡 在作者的个人 skill 合集里，只装这一个用上面的命令</sub>

- **[JittoJoseph/seo-skills](https://github.com/JittoJoseph/seo-skills)** · ★ 6<br>免费的 Shopify 和通用网站 SEO 审计：给网址，看 Google 和 AI 爬虫能读到什么、先修什么；Shopify 店另给按后台和主题说法的修复<br><sub>针对：Google</sub><br><sub>更新于 2026-11-16 · 英文 · 3 个 skill · MIT</sub>

- **[applyra-aso-skill](https://github.com/lucholabs/applyra-aso-skill)** · ★ 3<br>App Store 和 Google Play 的 ASO skill：关键词、排名、竞品、元数据校验、本地化、截图简报和转化实验<br><sub>针对：应用商店</sub><br><sub>更新于 2026-11-02 · 英文 · MIT</sub><br><sub>💡 实时数据要 Applyra 账号（免费档也能用接口）</sub>


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
# legends-geogrid
npx skills add avalonreset/legends-geogrid
# shopify-theme-audit-skill
npx skills add tanujrajputdev/shopify-theme-audit-skill
# etsy-listing-helper
npx skills add silennsong/etsy-listing-helper
# taobao-shop-growth
npx skills add yuyang2230/taobao-shop-growth
# app-store-aso
npx skills add TimBroddin/skills --skill app-store-aso
# JittoJoseph/seo-skills
npx skills add JittoJoseph/seo-skills
# applyra-aso-skill
npx skills add lucholabs/applyra-aso-skill
```

</details>

<a id="group-offsite"></a>
### 外链、PR 和站外提及

AI 回答常引用第三方页面：新闻稿、目录站、论坛和测评。这里是做外链、发新闻稿、争取站外提及的 skill。

- **[newsjack](https://github.com/elvisun/newsjack)** · ★ 1.7k<br>让 agent 当 PR 团队：监测行业新闻找借势机会、核实新闻是否还新、想切入角度、核查事实，按 AI 可见度来写<br><sub>针对：ChatGPT · Claude</sub><br><sub>更新于 2026-11-11 · 英文 · 35 个 skill · MIT</sub>

- **[backlink_skills](https://github.com/flaqai/backlink_skills)** · ★ 896<br>外链提交工作流：外链渠道清单、产品目录提交 skill，先查渠道再按授权提交，遇到验证码交给你，提交后留证据<br><sub>针对：Google</sub><br><sub>更新于 2026-11-12 · 多语言 · 16 个 skill · MIT</sub>

- **[distribb-skill](https://github.com/Bomx/distribb-skill)** · ★ 204<br>Distribb 的 SEO skill：用你自己的 AI 写内容，通过 Distribb 的外链网络发布，另有关键词数据和 Search Console 审计<br><sub>针对：Google</sub><br><sub>更新于 2026-10-11 · 英文 · 2 个 skill</sub><br><sub>💡 Distribb 是付费服务</sub>

- **[qwoted-seo-backlinks-skill](https://github.com/Bomx/qwoted-seo-backlinks-skill)** · ★ 156<br>在 Qwoted 上找记者的求助、做带出处的统计数据页当外链素材，再替你回复记者<br><sub>针对：通用</sub><br><sub>更新于 2026-05-02 💤 · 英文</sub><br><sub>💡 要 Qwoted 账号</sub>

- **[seo-ai-link](https://github.com/chenchaoge/seo-ai-link)** · ★ 38<br>独立站外链全流程：挖竞品外链、管外链库、AI 自动发外链、回访收录，配可视化报表，内置作者实测整理的外链库<br><sub>针对：Google</sub><br><sub>更新于 2026-11-10 · 中文</sub><br><sub>💡 竞品外链默认走 DataForSEO（按量付费），可换别的外链工具</sub>

- **[where-to-submit-your-startup](https://github.com/mmmmingos/where-to-submit-your-startup)** · ★ 13<br>1085 个创业产品提交和发布网站的清单，标了免费、有条件免费、付费和实测问题，skill 让 agent 回答该不该投、怎么投<br><sub>针对：通用</sub><br><sub>更新于 2026-11-09 · 英文 · MIT</sub><br><sub>💡 skill 通过 submitmystartup.com 的只读接口查，不用账号</sub>


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
# seo-ai-link
npx skills add chenchaoge/seo-ai-link
# where-to-submit-your-startup
npx skills add mmmmingos/where-to-submit-your-startup
```

</details>

<a id="group-mcp"></a>
### MCP 和命令行工具（不是 skill）

让 agent 能查 SEO 数据的工具，常和上面的 skill 搭配用。不计入 skill 数。

- **[mcp-gsc](https://github.com/AminForou/mcp-gsc)** · ★ 2.2k<br>Google Search Console 的 MCP：用自然语言分析你的 SEO 数据，附关键词蚕食、内容机会、收录审计、周报等 skill<br><sub>针对：Google</sub><br><sub>更新于 2026-11-06 · 🔌 MCP · 英文 · 4 个 skill · MIT</sub>

- **[python-seo-analyzer](https://github.com/sethblack/python-seo-analyzer)** · ★ 1.5k<br>老牌 SEO 分析命令行和 Python 库：爬站、统计正文用词、提示技术 SEO 问题，可选用 Claude 做内容评估<br><sub>针对：通用</sub><br><sub>更新于 2026-11-12 · 🔌 MCP · 英文</sub><br><sub>💡 AI 评估一步要 Anthropic API Key</sub>

- **[seo-monster](https://github.com/avansaber/seo-monster)** · ★ 496<br>本地运行的 SEO 分析 MCP：用你自己的 Search Console、GA4、PageSpeed 和 Cloudflare 数据回答 SEO 问题<br><sub>针对：Google</sub><br><sub>更新于 2026-11-13 · 🔌 MCP · 英文 · MIT</sub>

- **[OpenGSO](https://github.com/sherwinvishesh/OpenGSO)** · ★ 433<br>让网站对 AI 好读的命令行：打 0–100 分，给每页生成 Markdown 副本和 robots.txt、llms.txt、sitemap<br><sub>针对：ChatGPT · Perplexity · Claude</sub><br><sub>更新于 2026-11-09 · 🔌 MCP · 英文 · Apache-2.0</sub>

- **[mcp-server-typescript](https://github.com/dataforseo/mcp-server-typescript)** · ★ 262<br>DataForSEO 官方 MCP 和命令行：让 agent 查 API 文档并调用关键词、SERP、外链等数据接口<br><sub>针对：Google</sub><br><sub>更新于 2026-11-02 · 🔌 MCP · 英文 · Apache-2.0</sub><br><sub>💡 DataForSEO 按量付费</sub>

- **[seo-audit](https://github.com/houtini-ai/seo-audit)** · ★ 101<br>技术 SEO 审计 MCP：合并 Search Console、自有爬虫、DataForSEO 和 Majestic 的数据，在 Claude 里对话式做审计<br><sub>针对：Google</sub><br><sub>更新于 2026-11-11 · 🔌 MCP · 英文 · Apache-2.0</sub>

- **[screaming-frog-mcp](https://github.com/bzsasson/screaming-frog-mcp)** · ★ 96<br>Screaming Frog SEO Spider 的无界面 MCP：让 agent 跑爬取、导出和分析爬取数据，适合定时审计和 CI<br><sub>针对：通用</sub><br><sub>更新于 2026-11-14 · 🔌 MCP · 英文 · MIT</sub><br><sub>💡 要本机装 Screaming Frog，大部分功能要付费授权（免费版限 500 个网址）</sub>

- **[pagespeed-insights-mcp](https://github.com/ruslanlap/pagespeed-insights-mcp)** · ★ 81<br>Google PageSpeed Insights 和 Chrome 用户体验报告的 MCP：在 agent 里分析、对比和优化网页性能<br><sub>针对：Google</sub><br><sub>更新于 2026-11-15 · 🔌 MCP · 英文 · Apache-2.0</sub><br><sub>💡 要一个免费的 Google API Key</sub>

- **[lighthouse-mcp-server](https://github.com/danielsogl/lighthouse-mcp-server)** · ★ 75<br>用 Google Lighthouse 做网页审计的 MCP：13 个以上工具查性能、无障碍、SEO 和安全<br><sub>针对：Google</sub><br><sub>更新于 2026-11-16 · 🔌 MCP · 英文 · MIT</sub>

- **[sitewalk](https://github.com/adityaarsharma/sitewalk)** · ★ 48<br>Sitewalk 的开源技术 SEO 审计 MCP：像搜索引擎爬虫一样爬站，给按影响排序的问题和修法、健康分，出 PDF 和 CSV<br><sub>针对：Google</sub><br><sub>更新于 2026-11-13 · 🔌 MCP · 英文 · MIT</sub><br><sub>💡 自己部署要 Docker，开源版 30 多项检查；ChatGPT 里的托管版 200 多项，每月免费 5 次</sub>

- **[surendranb/google-search-console-mcp](https://github.com/surendranb/google-search-console-mcp)** · ★ 40<br>Google Search Console 的 MCP，附品牌可见度、引用机会、搜索意图分析和搜索外观审计 5 个 skill<br><sub>针对：Google</sub><br><sub>更新于 2026-11-10 · 🔌 MCP · 英文 · 5 个 skill · MIT</sub><br><sub>💡 默认向作者发送匿名诊断统计，README 写了怎么关</sub>

- **[mcp-geo](https://github.com/AKzar1el/mcp-geo)** · ★ 39<br>DigestSEO：追踪品牌在 7 个 AI 搜索平台的引用，本地运行，用你自己的各家 API Key<br><sub>针对：Google AI 概览 · ChatGPT · Perplexity · Gemini · Claude</sub><br><sub>更新于 2026-11-16 · 🔌 MCP · 英文 · MIT</sub>

- **[google-seo-mcp](https://github.com/Akxan/google-seo-mcp)** · ★ 30<br>SEO/GEO 的 MCP，102 个工具：Search Console、GA4、PageSpeed、结构化数据、AI 爬虫检查，还能改 WordPress<br><sub>针对：Google</sub><br><sub>更新于 2026-11-16 · 🔌 MCP · 英文 · MIT</sub>

- **[local-falcon/mcp](https://github.com/local-falcon/mcp)** · ★ 26<br>Local Falcon 的 MCP：地图网格排名追踪、活动管理、竞品分析，查 Google 地图、苹果地图和 AI 回答里的本地可见度，附 skill<br><sub>针对：Google · Google AI 概览 · ChatGPT · Gemini</sub><br><sub>更新于 2026-11-11 · 🔌 MCP · 英文 · 2 个 skill · MIT</sub><br><sub>💡 要 Local Falcon 账号（OAuth 登录或 API Key）</sub>

- **[WorkSmartAI-alt/ai-visibility-monitor](https://github.com/WorkSmartAI-alt/ai-visibility-monitor)** · ★ 21<br>AI 可见度命令行：把买家会问的问题拿去问 ChatGPT、Claude、Perplexity，找你能赢的问题和该写的内容<br><sub>针对：ChatGPT · Perplexity · Claude</sub><br><sub>更新于 2026-10-30 · 🔌 MCP · 英文 · MIT</sub><br><sub>💡 用你自己的各家模型 API Key</sub>

- **[yandex-mcp](https://github.com/stufently/yandex-mcp)** · ★ 21<br>Yandex 接口的一组 MCP，94 个工具：搜索、Wordstat 关键词、站长平台、Metrika 和 Direct，附俄语市场选词 skill<br><sub>针对：Yandex</sub><br><sub>更新于 2026-11-14 · 🔌 MCP · 英文 · 3 个 skill · MIT</sub><br><sub>💡 要 Yandex 各服务的 OAuth 令牌</sub>

- **[vinpatel/aeorank](https://github.com/vinpatel/aeorank)** · ★ 20<br>扫描网站的 AI 可见度：12 个维度打 0–100 分，生成 llms.txt 等 8 个给 AI 读的文件，命令行和 GitHub Action<br><sub>针对：ChatGPT · Perplexity · Claude</sub><br><sub>更新于 2026-11-15 · 🔌 MCP · 英文 · MIT</sub>

- **[mcp-abilities-rankmath](https://github.com/bjornfix/mcp-abilities-rankmath)** · ★ 16<br>让 agent 通过 MCP 读写 Rank Math 的 SEO 字段：元描述、标题、焦点关键词，基于 WordPress 的 Abilities API<br><sub>针对：通用</sub><br><sub>更新于 2026-11-06 · 🔌 MCP · 英文</sub><br><sub>💡 要在 WordPress 装这个插件和 MCP 适配器</sub>

- **[GBP Autopilot](https://github.com/tanzeeldevAi/google-business-profile-ai-automation)** · ★ 13<br>Google 商家资料自动化命令行：按 57 条本地 SEO 规则打分出报告，再通过接口修资料、回评价、每周发帖、设节假日营业时间，资料被改时提醒<br><sub>针对：Google</sub><br><sub>更新于 2026-11-10 · 🔌 MCP · 英文 · MIT</sub><br><sub>💡 要申请 Google 商家资料 API 权限；写内容走你的 Claude Code 订阅</sub>

- **[webappski/aeo-platform](https://github.com/webappski/aeo-platform)** · ★ 13<br>AEO/GEO 命令行：量品牌在 ChatGPT、Claude、Gemini、Perplexity 里的可见度，查 AI 爬虫可抓取性和权威信号<br><sub>针对：ChatGPT · Perplexity · Gemini · Claude</sub><br><sub>更新于 2026-11-16 · 🔌 MCP · 英文 · MIT</sub><br><sub>💡 用你自己的模型 API Key（建议至少两家）；npm 安装时会跑 git config core.hooksPath .githooks，按 README 全局装或用 npx，别装进自己的 git 项目</sub>

- **[acamolese/google-search-console-mcp](https://github.com/acamolese/google-search-console-mcp)** · ★ 10<br>Google Search Console 的只读 MCP，17 个工具：快速见效项、点击率缺口、关键词蚕食、流量下滑诊断、收录，还能出白标 HTML 审计报告<br><sub>针对：Google</sub><br><sub>更新于 2026-11-14 · 🔌 MCP · 英文 · 5 个 skill · MIT</sub>

- **[fiverr-gig-optimizer](https://github.com/waseemnasir2k26/fiverr-gig-optimizer)** · ★ 10<br>Fiverr 服务页优化命令行：给标题、标签、描述打分并给改法，附 Claude Code 命令，离线跑<br><sub>针对：电商站内搜索</sub><br><sub>更新于 2026-11-02 · 🔌 MCP · 英文 · MIT</sub>

- **[onlymoein/google-search-console-mcp](https://github.com/onlymoein/google-search-console-mcp)** · ★ 10<br>本地跑的 Search Console MCP：搜索数据、按小时数据、网址检查和站点地图，处理好接口的各种坑<br><sub>针对：Google</sub><br><sub>更新于 2026-11-11 · 🔌 MCP · 英文 · MIT</sub>

- **[mcp-web-validator](https://github.com/AKzar1el/mcp-web-validator)** · ★ 9<br>W3C HTML/CSS 校验加技术 SEO 审计的 MCP，DigestSEO 套件之一<br><sub>针对：通用</sub><br><sub>更新于 2026-11-13 · 🔌 MCP · 英文 · MIT</sub>

- **[mcp-yandex-wordstat](https://github.com/askads/mcp-yandex-wordstat)** · ★ 9<br>俄语 Yandex Wordstat 的 MCP：查热门和相似搜索词、需求走势和地区分布，只读<br><sub>针对：Yandex</sub><br><sub>更新于 2026-11-04 · 🔌 MCP · 俄文 · MIT</sub><br><sub>💡 要 Yandex Cloud 的 Search API Key 和目录 ID；默认向作者发送匿名使用统计（不含参数和 Key），设 ASKADS_TELEMETRY=0 可关</sub>

- **[AKzar1el/mcp-gsc](https://github.com/AKzar1el/mcp-gsc)** · ★ 8<br>Google Search Console 的 MCP：查点击、展示、排名、网址检查、站点地图和收录，本地跑或部署到 Cloudflare Workers<br><sub>针对：Google</sub><br><sub>更新于 2026-11-16 · 🔌 MCP · 英文 · 3 个 skill · MIT</sub>

- **[citation-intelligence](https://github.com/AutomateLab-tech/citation-intelligence)** · ★ 8<br>量 AI 引用的 MCP：查 Perplexity、AI 概览、ChatGPT、Claude、Gemini、Bing 对一个问题引用了哪些网址，12 个工具<br><sub>针对：Google AI 概览 · Bing · ChatGPT · Perplexity · Gemini · Claude</sub><br><sub>更新于 2026-11-02 · 🔌 MCP · 英文 · MIT</sub><br><sub>💡 用你自己的各家 API Key</sub>

- **[crawlgraph-mcp](https://github.com/pucilpet/crawlgraph-mcp)** · ★ 8<br>CrawlGraph 外链数据接口的 MCP：基于 Common Crawl 网页图查外链、外链变化和竞品外链缺口<br><sub>针对：通用</sub><br><sub>更新于 2026-11-12 · 🔌 MCP · 英文 · MIT</sub><br><sub>💡 要 CrawlGraph 的 API Key</sub>

- **[sudomichael/search-console-mcp](https://github.com/sudomichael/search-console-mcp)** · ★ 8<br>只读的 Search Console MCP：用 Google 账号登录一次就能用，不用建 Google Cloud 项目，令牌只存本机<br><sub>针对：Google</sub><br><sub>更新于 2026-11-08 · 🔌 MCP · 英文 · MIT</sub>

- **[gsc-mcp](https://github.com/geniushub-seo/gsc-mcp)** · ★ 7<br>Search Console 的本地 MCP：Go 单文件、一行安装、用自己的 Google 账号登录，附点击率缺口、流量下滑等 6 个 skill<br><sub>针对：Google</sub><br><sub>更新于 2026-11-15 · 🔌 MCP · 多语言 · 6 个 skill · MIT</sub>

- **[literallydotdev/aeo](https://github.com/literallydotdev/aeo)** · ★ 7<br>在本地跑 AI 可见度审计的命令行：看 ChatGPT、Claude、Gemini、Perplexity 会不会提到和引用你，结果可离线核验<br><sub>针对：Google AI 概览 · ChatGPT · Perplexity · Gemini · Claude</sub><br><sub>更新于 2026-11-12 · 🔌 MCP · 英文 · 3 个 skill · MIT</sub><br><sub>💡 用你自己的各家模型 Key，花钱前先让你批金额</sub>

- **[mcp-trendpulse](https://github.com/AKzar1el/mcp-trendpulse)** · ★ 7<br>Google 新闻加 Google 趋势的 MCP：比较关键词热度、找相关需求、跟当下新闻，做关键词和内容调研<br><sub>针对：Google</sub><br><sub>更新于 2026-11-15 · 🔌 MCP · 英文 · MIT</sub>

- **[ai-bot-access](https://github.com/codevibe-technology/ai-bot-access)** · ★ 6<br>一条命令查 24 种 AI、搜索和链接预览爬虫能不能读你的网站：robots.txt 加真实请求，另有分享预览、爬虫 IP 核验和访问日志报告<br><sub>针对：Google · ChatGPT · Perplexity · Claude</sub><br><sub>更新于 2026-11-15 · 🔌 MCP · 英文 · MIT</sub>

- **[blacksparrow](https://github.com/Shantodotdev/blacksparrow)** · ★ 6<br>Rust 写的本地爬虫和 120 条规则的技术 SEO 审计，Screaming Frog 的轻量替代，自带 MCP，也查 AI 爬虫权限<br><sub>针对：通用</sub><br><sub>更新于 2026-11-14 · 🔌 MCP · 英文 · Apache-2.0</sub>

- **[geo-scope](https://github.com/tmolavi/geo-scope)** · ★ 6<br>AI 可见度测量框架：多家模型同题对比，记品牌提及、推荐和引用，可复现，带命令行和 MCP<br><sub>针对：ChatGPT · Perplexity · Gemini</sub><br><sub>更新于 2026-11-16 · 🔌 MCP · 英文 · MIT</sub><br><sub>💡 用你自己的模型 API Key</sub>

- **[google-webtools-mcp](https://github.com/stufently/google-webtools-mcp)** · ★ 6<br>Search Console 加 GA4 的 MCP：管站点、看搜索表现、查收录、出 GA4 报表、验证站点<br><sub>针对：Google</sub><br><sub>更新于 2026-11-06 · 🔌 MCP · 英文 · MIT</sub><br><sub>💡 要 Google 服务账号；附带的 SKILL.md 是俄语</sub>

- **[bulk-ai-cli-connector](https://github.com/puneetindersingh/bulk-ai-cli-connector)** · ★ 5<br>WordPress 插件加 MCP：让 AI 批量改 Yoast 和 Rank Math 的 SEO 元信息、JSON-LD、跳转和页面文案，可撤销<br><sub>针对：通用</sub><br><sub>更新于 2026-11-16 · 🔌 MCP · 英文 · GPL-2.0</sub>

- **[google-discover-api-mcp-server](https://github.com/cotletdev/google-discover-api-mcp-server)** · ★ 5<br>Google Discover 的接口和 MCP：读任意国家的 Discover 信息流，看哪些媒体和文章在涨，追踪你的站在不在里面<br><sub>针对：Google</sub><br><sub>更新于 2026-11-10 · 🔌 MCP · 英文</sub><br><sub>💡 托管版要它的 API Key（付费），也可以自己部署</sub>

- **[cloro-dev/geo-tracker](https://github.com/cloro-dev/geo-tracker)** · ★ 4<br>给 agent 用的 GEO 加 SEO 追踪 MCP：定时把问题发给 ChatGPT、Gemini、Google AI 模式等，回答存进你自己的数据库<br><sub>针对：Google · Google AI 概览 · Bing · ChatGPT · Gemini</sub><br><sub>更新于 2026-11-07 · 🔌 MCP · 英文 · MIT</sub><br><sub>💡 要自己部署，查询走 cloro 的接口（要它的 API Key）</sub>

- **[geo-audit](https://github.com/g-shevchenko/geo-audit)** · ★ 4<br>开源 GEO 审计命令行：给网址打 AI 搜索可见度分（ChatGPT、Perplexity、Claude、Gemini、AI 概览），写成能交给团队的行动计划<br><sub>针对：Google AI 概览 · ChatGPT · Perplexity · Gemini · Claude</sub><br><sub>更新于 2026-11-16 · 🔌 MCP · 英文 · MIT</sub><br><sub>💡 品牌提及扫描要你自己的模型 API Key</sub>

- **[geolint](https://github.com/iliasabk/geolint)** · ★ 4<br>AI 搜索的 ESLint：查 51 种 AI 爬虫的 robots.txt 权限、llms.txt、结构化数据和可引用度，52 条规则，命令行和 MCP<br><sub>针对：ChatGPT · Perplexity · Claude</sub><br><sub>更新于 2026-11-16 · 🔌 MCP · 英文 · MIT</sub>

- **[rankparse-mcp](https://github.com/Rankparse/rankparse-mcp)** · ★ 4<br>RankParse 托管的 SEO 数据 MCP：外链、域名权重、技术栈和页面审计，数据来自 Common Crawl<br><sub>针对：通用</sub><br><sub>更新于 2026-11-07 · 🔌 MCP · 英文</sub><br><sub>💡 托管服务，仓库里只有接口文档；免 Key 有 25 个工具，全部 85 个要它的 API Key，按次付费</sub>

- **[semust-mcp](https://github.com/Semust-com/semust-mcp)** · ★ 4<br>Semust 的 MCP：Search Console、GA4、排名追踪、AI 概览可见度、Bing、Yandex，另有 Google 广告和社媒发帖<br><sub>针对：Google · Google AI 概览 · Bing · Yandex</sub><br><sub>更新于 2026-11-16 · 🔌 MCP · 英文 · MIT</sub><br><sub>💡 要 Semust 账号</sub>

- **[sonnivasquez/gsc-mcp](https://github.com/sonnivasquez/gsc-mcp)** · ★ 4<br>本地 Search Console MCP，34 个工具：对比搜索表现、找 SEO 机会、查网址收录，默认只读<br><sub>针对：Google</sub><br><sub>更新于 2026-11-05 · 🔌 MCP · 英文 · Apache-2.0</sub>

- **[yandex-webmaster-mcp](https://github.com/BoxLab-Ltd/yandex-webmaster-mcp)** · ★ 4<br>Yandex 站长平台的只读 MCP：用自然语言查收录、搜索词、诊断和外链，可提交重抓，不存密钥<br><sub>针对：Yandex</sub><br><sub>更新于 2026-11-09 · 🔌 MCP · 英文 · MIT</sub>

- **[a-bibikov/ai-search-audit](https://github.com/a-bibikov/ai-search-audit)** · ★ 3<br>查 ChatGPT、Claude、Perplexity 能否读懂并引用你的网站：56 项检查，命令行和 GitHub Action，可出 JSON<br><sub>针对：ChatGPT · Perplexity · Claude</sub><br><sub>更新于 2026-11-11 · 🔌 MCP · 英文 · MIT</sub>

- **[localseodata/mcp-server](https://github.com/localseodata/mcp-server)** · ★ 3<br>Local SEO Data 的 MCP，53 个本地 SEO 工具：SERP 和地图排名、评价、审计、关键词、竞品、网格追踪和 AI 可见度打分<br><sub>针对：Google</sub><br><sub>更新于 2026-11-11 · 🔌 MCP · 英文 · MIT</sub><br><sub>💡 要 Local SEO Data 账号，按额度付费</sub>

- **[seo-cartograph-mcp](https://github.com/tom-ned/seo-cartograph-mcp)** · ★ 3<br>SEO Cartograph 的 MCP 加 13 个法语 skill：读你的抓取、Search Console、GA4、排名和内链图，再出审计和简报<br><sub>针对：Google</sub><br><sub>更新于 2026-11-03 · 🔌 MCP · 法文 · 13 个 skill</sub><br><sub>💡 MCP 要 SEO Cartograph 账号（OAuth 登录，只读）；README 标明的几个免费 skill 不用账号</sub>


<a id="group-apps"></a>
### 相关开源平台（完整应用，不是 skill）

能自己部署的 SEO 和 GEO 平台。不计入 skill 数。

- **[niubigeo](https://github.com/Albert-Weasker/niubigeo)** · ★ 10.3k<br>NiubiGEO 开源 GEO 研究工具：输入域名，比较各家模型怎么描述你的产品、推荐了谁、引用哪些来源，可以重复测<br><sub>针对：通用</sub><br><sub>更新于 2026-11-16 · 🧩 应用 · 多语言 · Apache-2.0</sub><br><sub>💡 要自己部署，用你自己的模型 API Key；作者另卖真人测试和 GEO 代运营</sub>

- **[GEOFlow](https://github.com/yaojingang/GEOFlow)** · ★ 4.1k<br>开源 GEO 内容工程和多站分发平台：AI 质检、托管站点、浏览器辅助发布和签名更新，附操作它的 skill<br><sub>针对：通用</sub><br><sub>更新于 2026-11-13 · 🧩 应用 · 多语言 · 6 个 skill · AGPL-3.0</sub>

- **[LibreCrawl](https://github.com/PhialsBasement/LibreCrawl)** · ★ 1.1k<br>免费的 SEO 爬虫，Screaming Frog 的开源替代：爬站、分析链接、提取 SEO 数据并导出，不用订阅<br><sub>针对：通用</sub><br><sub>更新于 2026-11-10 · 🧩 应用 · 英文 · MIT</sub>


<a id="by-engines"></a>
## 按搜索引擎和 AI 平台查找

仓库说明里明确写了针对哪家（按星数排序）。「通用」是不挑引擎的。

**Google**（133）：[marketingskills](https://github.com/coreyhaines31/marketingskills) · [claude-seo](https://github.com/AgriciDaniel/claude-seo) · [geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) · [open-seo-mcp-skills](https://github.com/Ryze-AI-Adgent/open-seo-mcp-skills) · [seomachine](https://github.com/TheCraigHewitt/seomachine) · [notfair-plugin](https://github.com/nowork-studio/notfair-plugin) · [web-quality-skills](https://github.com/addyosmani/web-quality-skills) · [claude-blog](https://github.com/AgriciDaniel/claude-blog) · [mcp-gsc](https://github.com/AminForou/mcp-gsc) · [opc-skills](https://github.com/ReScienceLab/opc-skills) · [gtm-engineer-skills](https://github.com/onvoyage-ai/gtm-engineer-skills) · [geo-optimizer-skill](https://github.com/Auriti-Labs/geo-optimizer-skill) · [seo-skills](https://github.com/Illyism/seo-skills) · [marketing-skills](https://github.com/kostja94/marketing-skills) · [Agentic-SEO-Skill](https://github.com/Bhanunamikaze/Agentic-SEO-Skill) · [fire-your-seo-agency](https://github.com/leopard627/fire-your-seo-agency) · [backlink_skills](https://github.com/flaqai/backlink_skills) · [seo-audit-skill](https://github.com/JeffLi1993/seo-audit-skill) · [seo](https://github.com/iannuttall/seo) · [bisibility](https://github.com/CorgiCorner/bisibility) · [Seo-Promt-Master](https://github.com/umutxyp/Seo-Promt-Master) · [saas-growth-agents](https://github.com/Pluviobyte/saas-growth-agents) · [mcp-google-map](https://github.com/cablate/mcp-google-map) · [seo-monster](https://github.com/avansaber/seo-monster) · [qiaomu-seo](https://github.com/joeseesun/qiaomu-seo) · [superseo-skills](https://github.com/inhouseseo/superseo-skills) · [open-seo-advisor-skill](https://github.com/mars-tw/open-seo-advisor-skill) · [7deer_skills](https://github.com/kennyzir/7deer_skills) · [everyinfra/seo-skills](https://github.com/everyinfra/seo-skills) · [yan-skills](https://github.com/yan-labs/yan-skills) · [SEO-GEO-AEO-Skill](https://github.com/SNLabat/SEO-GEO-AEO-Skill) · [beyondseo](https://github.com/beyondtahir/beyondseo) · [seobuild-onpage](https://github.com/gbessoni/seobuild-onpage) · [mcp-server-typescript](https://github.com/dataforseo/mcp-server-typescript) · [seo-landing](https://github.com/aleksandr-alhoff/seo-landing) · [seo-skills](https://github.com/seranking/seo-skills) · [distribb-skill](https://github.com/Bomx/distribb-skill) · [dataforseo-claude](https://github.com/zubair-trabzada/dataforseo-claude) · [seo-geo-audit](https://github.com/dageno-agents/seo-geo-audit) · [codex-seo](https://github.com/zhtyyx/codex-seo) · [localseoskills](https://github.com/garrettjsmith/localseoskills) · [claude-rank](https://github.com/Houseofmvps/claude-rank) · [google-ai-search-optimization](https://github.com/deepakness/google-ai-search-optimization) · [All-In-One-Free-SEO-Tool](https://github.com/IamRamgarhia/All-In-One-Free-SEO-Tool) · [seo-god](https://github.com/AKCodez/seo-god) · [claude-code-seo](https://github.com/huifer/claude-code-seo) · [ultimate-seo-geo](https://github.com/mykpono/ultimate-seo-geo) · [jev-seo](https://github.com/AkashPriyadarshii/jev-seo) · [seo-audit](https://github.com/houtini-ai/seo-audit) · [dispatchseo](https://github.com/NeoZi12/dispatchseo) · [Awesome_SEO_Writing_Skill](https://github.com/flaqai/Awesome_SEO_Writing_Skill) · [claude-seo-ai](https://github.com/Hainrixz/claude-seo-ai) · [vercel-seo-audit](https://github.com/JosephDoUrden/vercel-seo-audit) · [pagespeed-insights-mcp](https://github.com/ruslanlap/pagespeed-insights-mcp) · [akii-seo-ai-search-optimizer](https://github.com/akii-technologies-ltd/akii-seo-ai-search-optimizer) · [lighthouse-mcp-server](https://github.com/danielsogl/lighthouse-mcp-server) · [legends-geogrid](https://github.com/avalonreset/legends-geogrid) · [OpenGSC](https://github.com/fenjo26/OpenGSC) · [zens-ink-seo-package](https://github.com/ZensInk/zens-ink-seo-package) · [pseo-skills](https://github.com/lisbeth718/pseo-skills) · [southwellmedia/seo-audit](https://github.com/southwellmedia/seo-audit) · [duckduckdeploy/openseo](https://github.com/duckduckdeploy/openseo) · [seo-party-skills](https://github.com/every-app/seo-party-skills) · [sitewalk](https://github.com/adityaarsharma/sitewalk) · [mxfschr/claude-code-seo](https://github.com/mxfschr/claude-code-seo) · [shopify-theme-audit-skill](https://github.com/tanujrajputdev/shopify-theme-audit-skill) · [fat-agent-skill](https://github.com/spruikco/fat-agent-skill) · [surendranb/google-search-console-mcp](https://github.com/surendranb/google-search-console-mcp) · [claude-seo-skill](https://github.com/mangollc/claude-seo-skill) · [seo-ai-link](https://github.com/chenchaoge/seo-ai-link) · [seo-guide-skill](https://github.com/lesishu/seo-guide-skill) · [geoskills](https://github.com/Cognitic-Labs/geoskills) · [google-seo-mcp](https://github.com/Akxan/google-seo-mcp) · [local-falcon/mcp](https://github.com/local-falcon/mcp) · [autoseo](https://github.com/codextde/autoseo) · [seojuice-skills](https://github.com/calm-north/seojuice-skills) · [launch-seo-skill](https://github.com/iamjeeth/launch-seo-skill) · [tipsai/product-seo](https://github.com/tipsai/product-seo) · [99-website](https://github.com/NicoSKOOL/99-website) · [SoDam-SeoMedic](https://github.com/sodam-ai/SoDam-SeoMedic) · [GBP Autopilot](https://github.com/tanzeeldevAi/google-business-profile-ai-automation) · [seo-utils-skills](https://github.com/seoutilsapp/seo-utils-skills) · [seo-survival-kit](https://github.com/maxschottke-spec/seo-survival-kit) · [croftweaver](https://github.com/karero/croftweaver) · [gscdump](https://github.com/harlan-zw/gscdump) · [seo-night-skill](https://github.com/IncomeStreamSurfer/seo-night-skill) · [acamolese/google-search-console-mcp](https://github.com/acamolese/google-search-console-mcp) · [onlymoein/google-search-console-mcp](https://github.com/onlymoein/google-search-console-mcp) · [legends-github](https://github.com/avalonreset/legends-github) · [seo-skills](https://github.com/RomeoSEO/seo-skills) · [pseolint](https://github.com/ouranos-labs/pseolint) · [AKzar1el/mcp-gsc](https://github.com/AKzar1el/mcp-gsc) · [sudomichael/search-console-mcp](https://github.com/sudomichael/search-console-mcp) · [search-os](https://github.com/vamsireddy4/search-os) · [skill-seo-co-ban](https://github.com/ibangtam/skill-seo-co-ban) · [gsc-mcp](https://github.com/geniushub-seo/gsc-mcp) · [mcp-trendpulse](https://github.com/AKzar1el/mcp-trendpulse) · [my-claude-skills](https://github.com/vincentventalon/my-claude-skills) · [altorank](https://github.com/AltoRank/altorank) · [sayiyla-seo-ajan](https://github.com/sayiyla/sayiyla-seo-ajan) · [seo-audit-skills](https://github.com/carlosuhart/seo-audit-skills) · [JittoJoseph/seo-skills](https://github.com/JittoJoseph/seo-skills) · [ai-bot-access](https://github.com/codevibe-technology/ai-bot-access) · [google-webtools-mcp](https://github.com/stufently/google-webtools-mcp) · [World-Class-SEO-Agent-System](https://github.com/wfprieto/World-Class-SEO-Agent-System) · [aeo-geo-bestpractices](https://github.com/micaelgomestavares/aeo-geo-bestpractices) · [seo-gsc-ga4-analyst](https://github.com/owensky-dev/seo-gsc-ga4-analyst) · [Manifold](https://github.com/manifoldmcp/marketing-skills) · [rankmath-seo-wp](https://github.com/Moksa1123/rankmath-seo-wp) · [rankcontrol](https://github.com/rankcontrol/rankcontrol) · [research-first-writer](https://github.com/jayanti-prajapati/research-first-writer) · [pagination-independence-architecture](https://github.com/rebelytics/pagination-independence-architecture) · [one-step-seo](https://github.com/6t9xstar/one-step-seo) · [google-discover-api-mcp-server](https://github.com/cotletdev/google-discover-api-mcp-server) · [WordRocket/claude-seo-skills](https://github.com/WordRocket/claude-seo-skills) · [lighthouse-skill](https://github.com/nimajafari/lighthouse-skill) · [semust-mcp](https://github.com/Semust-com/semust-mcp) · [sonnivasquez/gsc-mcp](https://github.com/sonnivasquez/gsc-mcp) · [cloro-dev/geo-tracker](https://github.com/cloro-dev/geo-tracker) · [claude-code-seo-starter](https://github.com/AntonioBlago/claude-code-seo-starter) · [raulveneri/seo-kit](https://github.com/raulveneri/seo-kit) · [ai-search-audit-full](https://github.com/Olexan-art/ai-search-audit-full) · [aizaloapp/aeorank](https://github.com/aizaloapp/aeorank) · [agenticseo](https://github.com/kid7st/agenticseo) · [IndexGap](https://github.com/borisowlexa2010-star/IndexGap) · [JakeLabate/Claude-SEO-Skills](https://github.com/JakeLabate/Claude-SEO-Skills) · [seo-aeo-audit](https://github.com/ssheleg/seo-aeo-audit) · [seo-geo-smart-audit-skill](https://github.com/yangjing6213-dev/seo-geo-smart-audit-skill) · [jorgejaramillo/seoskills](https://github.com/jorgejaramillo/seoskills) · [localseodata/mcp-server](https://github.com/localseodata/mcp-server) · [seo-cartograph-mcp](https://github.com/tom-ned/seo-cartograph-mcp) · [zaDojo](https://github.com/zaDojo/seo-geo-mcp) · [crakseo-mcp-plugins](https://github.com/CrakSEO/crakseo-mcp-plugins)

**Google AI 概览**（60）：[marketingskills](https://github.com/coreyhaines31/marketingskills) · [claude-seo](https://github.com/AgriciDaniel/claude-seo) · [geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) · [notfair-plugin](https://github.com/nowork-studio/notfair-plugin) · [claude-blog](https://github.com/AgriciDaniel/claude-blog) · [gtm-engineer-skills](https://github.com/onvoyage-ai/gtm-engineer-skills) · [geo-optimizer-skill](https://github.com/Auriti-Labs/geo-optimizer-skill) · [seo-skills](https://github.com/Illyism/seo-skills) · [Agentic-SEO-Skill](https://github.com/Bhanunamikaze/Agentic-SEO-Skill) · [fire-your-seo-agency](https://github.com/leopard627/fire-your-seo-agency) · [elmo](https://github.com/elmohq/elmo) · [qiaomu-seo](https://github.com/joeseesun/qiaomu-seo) · [limelit-co/open](https://github.com/limelit-co/open) · [GetCito](https://github.com/ai-search-guru/getcito-worlds-first-open-source-aio-aeo-or-geo-tool) · [geo-aeo-tracker](https://github.com/danishashko/geo-aeo-tracker) · [everyinfra/seo-skills](https://github.com/everyinfra/seo-skills) · [SEO-GEO-AEO-Skill](https://github.com/SNLabat/SEO-GEO-AEO-Skill) · [seobuild-onpage](https://github.com/gbessoni/seobuild-onpage) · [ansvisor](https://github.com/ansvisor/ansvisor) · [GEO-Content-Optimizer-Skill](https://github.com/liangdabiao/GEO-Content-Optimizer-Skill) · [seo-skills](https://github.com/seranking/seo-skills) · [seo-geo-audit](https://github.com/dageno-agents/seo-geo-audit) · [codex-seo](https://github.com/zhtyyx/codex-seo) · [localseoskills](https://github.com/garrettjsmith/localseoskills) · [claude-rank](https://github.com/Houseofmvps/claude-rank) · [google-ai-search-optimization](https://github.com/deepakness/google-ai-search-optimization) · [All-In-One-Free-SEO-Tool](https://github.com/IamRamgarhia/All-In-One-Free-SEO-Tool) · [ultimate-seo-geo](https://github.com/mykpono/ultimate-seo-geo) · [claude-seo-ai](https://github.com/Hainrixz/claude-seo-ai) · [akii-seo-ai-search-optimizer](https://github.com/akii-technologies-ltd/akii-seo-ai-search-optimizer) · [southwellmedia/seo-audit](https://github.com/southwellmedia/seo-audit) · [duckduckdeploy/openseo](https://github.com/duckduckdeploy/openseo) · [seo-skills/geo-audit-skill](https://github.com/seo-skills/geo-audit-skill) · [fat-agent-skill](https://github.com/spruikco/fat-agent-skill) · [claude-seo-skill](https://github.com/mangollc/claude-seo-skill) · [mcp-geo](https://github.com/AKzar1el/mcp-geo) · [local-falcon/mcp](https://github.com/local-falcon/mcp) · [autoseo](https://github.com/codextde/autoseo) · [seojuice-skills](https://github.com/calm-north/seojuice-skills) · [seo-survival-kit](https://github.com/maxschottke-spec/seo-survival-kit) · [seo-skills](https://github.com/RomeoSEO/seo-skills) · [citation-intelligence](https://github.com/AutomateLab-tech/citation-intelligence) · [search-os](https://github.com/vamsireddy4/search-os) · [literallydotdev/aeo](https://github.com/literallydotdev/aeo) · [peec-ai-tracking-strategy-builder](https://github.com/rebelytics/peec-ai-tracking-strategy-builder) · [World-Class-SEO-Agent-System](https://github.com/wfprieto/World-Class-SEO-Agent-System) · [geo-skills](https://github.com/aivisibilitycensus/geo-skills) · [CiteLadder](https://github.com/abhij1306/CiteLadder) · [rankcontrol](https://github.com/rankcontrol/rankcontrol) · [research-first-writer](https://github.com/jayanti-prajapati/research-first-writer) · [one-step-seo](https://github.com/6t9xstar/one-step-seo) · [WordRocket/claude-seo-skills](https://github.com/WordRocket/claude-seo-skills) · [geo-audit](https://github.com/g-shevchenko/geo-audit) · [semust-mcp](https://github.com/Semust-com/semust-mcp) · [cloro-dev/geo-tracker](https://github.com/cloro-dev/geo-tracker) · [ai-visibility-tracking-strategy-builder](https://github.com/rebelytics/ai-visibility-tracking-strategy-builder) · [aizaloapp/aeorank](https://github.com/aizaloapp/aeorank) · [seo-aeo-audit](https://github.com/ssheleg/seo-aeo-audit) · [zaDojo](https://github.com/zaDojo/seo-geo-mcp) · [crakseo-mcp-plugins](https://github.com/CrakSEO/crakseo-mcp-plugins)

**Bing**（27）：[claude-seo](https://github.com/AgriciDaniel/claude-seo) · [fire-your-seo-agency](https://github.com/leopard627/fire-your-seo-agency) · [seo](https://github.com/iannuttall/seo) · [Seo-Promt-Master](https://github.com/umutxyp/Seo-Promt-Master) · [qiaomu-seo](https://github.com/joeseesun/qiaomu-seo) · [everyinfra/seo-skills](https://github.com/everyinfra/seo-skills) · [SEO-GEO-AEO-Skill](https://github.com/SNLabat/SEO-GEO-AEO-Skill) · [seo-geo-audit](https://github.com/dageno-agents/seo-geo-audit) · [localseoskills](https://github.com/garrettjsmith/localseoskills) · [claude-rank](https://github.com/Houseofmvps/claude-rank) · [OpenGSC](https://github.com/fenjo26/OpenGSC) · [zens-ink-seo-package](https://github.com/ZensInk/zens-ink-seo-package) · [seo-skills/geo-audit-skill](https://github.com/seo-skills/geo-audit-skill) · [geoskills](https://github.com/Cognitic-Labs/geoskills) · [launch-seo-skill](https://github.com/iamjeeth/launch-seo-skill) · [tipsai/product-seo](https://github.com/tipsai/product-seo) · [SoDam-SeoMedic](https://github.com/sodam-ai/SoDam-SeoMedic) · [citation-intelligence](https://github.com/AutomateLab-tech/citation-intelligence) · [search-os](https://github.com/vamsireddy4/search-os) · [semust-mcp](https://github.com/Semust-com/semust-mcp) · [cloro-dev/geo-tracker](https://github.com/cloro-dev/geo-tracker) · [get-cited-by-ai](https://github.com/paultaki/get-cited-by-ai) · [ai-search-audit-full](https://github.com/Olexan-art/ai-search-audit-full) · [IndexGap](https://github.com/borisowlexa2010-star/IndexGap) · [seo-aeo-audit](https://github.com/ssheleg/seo-aeo-audit) · [seo-geo-smart-audit-skill](https://github.com/yangjing6213-dev/seo-geo-smart-audit-skill) · [crakseo-mcp-plugins](https://github.com/CrakSEO/crakseo-mcp-plugins)

**百度**（4）：[yao-geo-skills](https://github.com/yaojingang/yao-geo-skills) · [geolook](https://github.com/aigclink/geolook) · [HeiGe-GEO-SEO](https://github.com/HeiGeAi/HeiGe-GEO-SEO) · [GEOVisibilityTool](https://github.com/MasashiToda1/GEOVisibilityTool)

**Yandex**（10）：[everyinfra/seo-skills](https://github.com/everyinfra/seo-skills) · [OpenGSC](https://github.com/fenjo26/OpenGSC) · [yandex-mcp](https://github.com/stufently/yandex-mcp) · [mcp-yandex-wordstat](https://github.com/askads/mcp-yandex-wordstat) · [sayiyla-seo-ajan](https://github.com/sayiyla/sayiyla-seo-ajan) · [yandex-webmaster-mcp](https://github.com/BoxLab-Ltd/yandex-webmaster-mcp) · [semust-mcp](https://github.com/Semust-com/semust-mcp) · [yandex-wordstat](https://github.com/prikotov/yandex-wordstat) · [IndexGap](https://github.com/borisowlexa2010-star/IndexGap) · [seo-aeo-audit](https://github.com/ssheleg/seo-aeo-audit)

**ChatGPT**（88）：[marketingskills](https://github.com/coreyhaines31/marketingskills) · [claude-seo](https://github.com/AgriciDaniel/claude-seo) · [geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) · [open-seo-mcp-skills](https://github.com/Ryze-AI-Adgent/open-seo-mcp-skills) · [notfair-plugin](https://github.com/nowork-studio/notfair-plugin) · [claude-blog](https://github.com/AgriciDaniel/claude-blog) · [opc-skills](https://github.com/ReScienceLab/opc-skills) · [newsjack](https://github.com/elvisun/newsjack) · [gtm-engineer-skills](https://github.com/onvoyage-ai/gtm-engineer-skills) · [geo-optimizer-skill](https://github.com/Auriti-Labs/geo-optimizer-skill) · [seo-skills](https://github.com/Illyism/seo-skills) · [Agentic-SEO-Skill](https://github.com/Bhanunamikaze/Agentic-SEO-Skill) · [fire-your-seo-agency](https://github.com/leopard627/fire-your-seo-agency) · [yao-geo-skills](https://github.com/yaojingang/yao-geo-skills) · [geolook](https://github.com/aigclink/geolook) · [geo-doctor](https://github.com/Fangx-AI/geo-doctor) · [elmo](https://github.com/elmohq/elmo) · [qiaomu-seo](https://github.com/joeseesun/qiaomu-seo) · [limelit-co/open](https://github.com/limelit-co/open) · [OpenGSO](https://github.com/sherwinvishesh/OpenGSO) · [voyage-geo-agent](https://github.com/onvoyage-ai/voyage-geo-agent) · [geo-aeo-tracker](https://github.com/danishashko/geo-aeo-tracker) · [everyinfra/seo-skills](https://github.com/everyinfra/seo-skills) · [SEO-GEO-AEO-Skill](https://github.com/SNLabat/SEO-GEO-AEO-Skill) · [beyondseo](https://github.com/beyondtahir/beyondseo) · [seobuild-onpage](https://github.com/gbessoni/seobuild-onpage) · [ansvisor](https://github.com/ansvisor/ansvisor) · [GEO-Content-Optimizer-Skill](https://github.com/liangdabiao/GEO-Content-Optimizer-Skill) · [eGEOagents](https://github.com/mverab/eGEOagents) · [seo-skills](https://github.com/seranking/seo-skills) · [canonry](https://github.com/Canonry/canonry) · [seo-geo-audit](https://github.com/dageno-agents/seo-geo-audit) · [codex-seo](https://github.com/zhtyyx/codex-seo) · [claude-rank](https://github.com/Houseofmvps/claude-rank) · [aeo.js](https://github.com/rubenmarcus/aeo.js) · [orangeo-ai-visibility-skill](https://github.com/OranAi-Ltd/orangeo-ai-visibility-skill) · [All-In-One-Free-SEO-Tool](https://github.com/IamRamgarhia/All-In-One-Free-SEO-Tool) · [ultimate-seo-geo](https://github.com/mykpono/ultimate-seo-geo) · [jev-seo](https://github.com/AkashPriyadarshii/jev-seo) · [HeiGe-GEO-SEO](https://github.com/HeiGeAi/HeiGe-GEO-SEO) · [claude-seo-ai](https://github.com/Hainrixz/claude-seo-ai) · [akii-seo-ai-search-optimizer](https://github.com/akii-technologies-ltd/akii-seo-ai-search-optimizer) · [southwellmedia/seo-audit](https://github.com/southwellmedia/seo-audit) · [seo-party-skills](https://github.com/every-app/seo-party-skills) · [shopify-theme-audit-skill](https://github.com/tanujrajputdev/shopify-theme-audit-skill) · [seo-skills/geo-audit-skill](https://github.com/seo-skills/geo-audit-skill) · [claude-seo-skill](https://github.com/mangollc/claude-seo-skill) · [mcp-geo](https://github.com/AKzar1el/mcp-geo) · [geo-score](https://github.com/jianruntech/geo-score) · [geoskills](https://github.com/Cognitic-Labs/geoskills) · [local-falcon/mcp](https://github.com/local-falcon/mcp) · [aicw-ai-mentions](https://github.com/aichatwatch/aicw-ai-mentions) · [autoseo](https://github.com/codextde/autoseo) · [seojuice-skills](https://github.com/calm-north/seojuice-skills) · [WorkSmartAI-alt/ai-visibility-monitor](https://github.com/WorkSmartAI-alt/ai-visibility-monitor) · [vinpatel/aeorank](https://github.com/vinpatel/aeorank) · [agent-lighthouse](https://github.com/ForkPoint/agent-lighthouse) · [SoDam-SeoMedic](https://github.com/sodam-ai/SoDam-SeoMedic) · [webappski/aeo-platform](https://github.com/webappski/aeo-platform) · [seo-survival-kit](https://github.com/maxschottke-spec/seo-survival-kit) · [topcited-skills](https://github.com/TopCited/topcited-skills) · [seo-skills](https://github.com/RomeoSEO/seo-skills) · [citation-intelligence](https://github.com/AutomateLab-tech/citation-intelligence) · [search-os](https://github.com/vamsireddy4/search-os) · [agent-readiness](https://github.com/Canonry/agent-readiness) · [literallydotdev/aeo](https://github.com/literallydotdev/aeo) · [peec-ai-tracking-strategy-builder](https://github.com/rebelytics/peec-ai-tracking-strategy-builder) · [ai-bot-access](https://github.com/codevibe-technology/ai-bot-access) · [geo-scope](https://github.com/tmolavi/geo-scope) · [geo-skills](https://github.com/aivisibilitycensus/geo-skills) · [aeo-toolkit](https://github.com/Advance-Labs/aeo-toolkit) · [CiteLadder](https://github.com/abhij1306/CiteLadder) · [aeo-geo-bestpractices](https://github.com/micaelgomestavares/aeo-geo-bestpractices) · [Manifold](https://github.com/manifoldmcp/marketing-skills) · [rankcontrol](https://github.com/rankcontrol/rankcontrol) · [research-first-writer](https://github.com/jayanti-prajapati/research-first-writer) · [one-step-seo](https://github.com/6t9xstar/one-step-seo) · [WordRocket/claude-seo-skills](https://github.com/WordRocket/claude-seo-skills) · [geolint](https://github.com/iliasabk/geolint) · [geo-audit](https://github.com/g-shevchenko/geo-audit) · [cloro-dev/geo-tracker](https://github.com/cloro-dev/geo-tracker) · [llms-txt-writer](https://github.com/shimo4228/llms-txt-writer) · [ai-visibility-tracking-strategy-builder](https://github.com/rebelytics/ai-visibility-tracking-strategy-builder) · [seo-aeo-audit](https://github.com/ssheleg/seo-aeo-audit) · [seo-geo-smart-audit-skill](https://github.com/yangjing6213-dev/seo-geo-smart-audit-skill) · [a-bibikov/ai-search-audit](https://github.com/a-bibikov/ai-search-audit) · [zaDojo](https://github.com/zaDojo/seo-geo-mcp) · [crakseo-mcp-plugins](https://github.com/CrakSEO/crakseo-mcp-plugins)

**Perplexity**（77）：[marketingskills](https://github.com/coreyhaines31/marketingskills) · [claude-seo](https://github.com/AgriciDaniel/claude-seo) · [geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) · [open-seo-mcp-skills](https://github.com/Ryze-AI-Adgent/open-seo-mcp-skills) · [notfair-plugin](https://github.com/nowork-studio/notfair-plugin) · [claude-blog](https://github.com/AgriciDaniel/claude-blog) · [opc-skills](https://github.com/ReScienceLab/opc-skills) · [gtm-engineer-skills](https://github.com/onvoyage-ai/gtm-engineer-skills) · [geo-optimizer-skill](https://github.com/Auriti-Labs/geo-optimizer-skill) · [seo-skills](https://github.com/Illyism/seo-skills) · [Agentic-SEO-Skill](https://github.com/Bhanunamikaze/Agentic-SEO-Skill) · [fire-your-seo-agency](https://github.com/leopard627/fire-your-seo-agency) · [geolook](https://github.com/aigclink/geolook) · [geo-doctor](https://github.com/Fangx-AI/geo-doctor) · [elmo](https://github.com/elmohq/elmo) · [qiaomu-seo](https://github.com/joeseesun/qiaomu-seo) · [limelit-co/open](https://github.com/limelit-co/open) · [OpenGSO](https://github.com/sherwinvishesh/OpenGSO) · [voyage-geo-agent](https://github.com/onvoyage-ai/voyage-geo-agent) · [geo-aeo-tracker](https://github.com/danishashko/geo-aeo-tracker) · [SEO-GEO-AEO-Skill](https://github.com/SNLabat/SEO-GEO-AEO-Skill) · [seobuild-onpage](https://github.com/gbessoni/seobuild-onpage) · [ansvisor](https://github.com/ansvisor/ansvisor) · [GEO-Content-Optimizer-Skill](https://github.com/liangdabiao/GEO-Content-Optimizer-Skill) · [eGEOagents](https://github.com/mverab/eGEOagents) · [seo-skills](https://github.com/seranking/seo-skills) · [seo-geo-audit](https://github.com/dageno-agents/seo-geo-audit) · [codex-seo](https://github.com/zhtyyx/codex-seo) · [claude-rank](https://github.com/Houseofmvps/claude-rank) · [aeo.js](https://github.com/rubenmarcus/aeo.js) · [orangeo-ai-visibility-skill](https://github.com/OranAi-Ltd/orangeo-ai-visibility-skill) · [All-In-One-Free-SEO-Tool](https://github.com/IamRamgarhia/All-In-One-Free-SEO-Tool) · [ultimate-seo-geo](https://github.com/mykpono/ultimate-seo-geo) · [jev-seo](https://github.com/AkashPriyadarshii/jev-seo) · [HeiGe-GEO-SEO](https://github.com/HeiGeAi/HeiGe-GEO-SEO) · [claude-seo-ai](https://github.com/Hainrixz/claude-seo-ai) · [akii-seo-ai-search-optimizer](https://github.com/akii-technologies-ltd/akii-seo-ai-search-optimizer) · [southwellmedia/seo-audit](https://github.com/southwellmedia/seo-audit) · [shopify-theme-audit-skill](https://github.com/tanujrajputdev/shopify-theme-audit-skill) · [seo-skills/geo-audit-skill](https://github.com/seo-skills/geo-audit-skill) · [claude-seo-skill](https://github.com/mangollc/claude-seo-skill) · [mcp-geo](https://github.com/AKzar1el/mcp-geo) · [geo-score](https://github.com/jianruntech/geo-score) · [geoskills](https://github.com/Cognitic-Labs/geoskills) · [aicw-ai-mentions](https://github.com/aichatwatch/aicw-ai-mentions) · [autoseo](https://github.com/codextde/autoseo) · [seojuice-skills](https://github.com/calm-north/seojuice-skills) · [WorkSmartAI-alt/ai-visibility-monitor](https://github.com/WorkSmartAI-alt/ai-visibility-monitor) · [vinpatel/aeorank](https://github.com/vinpatel/aeorank) · [agent-lighthouse](https://github.com/ForkPoint/agent-lighthouse) · [SoDam-SeoMedic](https://github.com/sodam-ai/SoDam-SeoMedic) · [webappski/aeo-platform](https://github.com/webappski/aeo-platform) · [seo-survival-kit](https://github.com/maxschottke-spec/seo-survival-kit) · [topcited-skills](https://github.com/TopCited/topcited-skills) · [seo-skills](https://github.com/RomeoSEO/seo-skills) · [citation-intelligence](https://github.com/AutomateLab-tech/citation-intelligence) · [search-os](https://github.com/vamsireddy4/search-os) · [agent-readiness](https://github.com/Canonry/agent-readiness) · [literallydotdev/aeo](https://github.com/literallydotdev/aeo) · [peec-ai-tracking-strategy-builder](https://github.com/rebelytics/peec-ai-tracking-strategy-builder) · [ai-bot-access](https://github.com/codevibe-technology/ai-bot-access) · [geo-scope](https://github.com/tmolavi/geo-scope) · [aeo-toolkit](https://github.com/Advance-Labs/aeo-toolkit) · [aeo-geo-bestpractices](https://github.com/micaelgomestavares/aeo-geo-bestpractices) · [rankcontrol](https://github.com/rankcontrol/rankcontrol) · [research-first-writer](https://github.com/jayanti-prajapati/research-first-writer) · [one-step-seo](https://github.com/6t9xstar/one-step-seo) · [geolint](https://github.com/iliasabk/geolint) · [geo-audit](https://github.com/g-shevchenko/geo-audit) · [llms-txt-writer](https://github.com/shimo4228/llms-txt-writer) · [ai-visibility-tracking-strategy-builder](https://github.com/rebelytics/ai-visibility-tracking-strategy-builder) · [aizaloapp/aeorank](https://github.com/aizaloapp/aeorank) · [seo-aeo-audit](https://github.com/ssheleg/seo-aeo-audit) · [seo-geo-smart-audit-skill](https://github.com/yangjing6213-dev/seo-geo-smart-audit-skill) · [a-bibikov/ai-search-audit](https://github.com/a-bibikov/ai-search-audit) · [zaDojo](https://github.com/zaDojo/seo-geo-mcp) · [crakseo-mcp-plugins](https://github.com/CrakSEO/crakseo-mcp-plugins)

**Gemini**（59）：[claude-seo](https://github.com/AgriciDaniel/claude-seo) · [geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) · [open-seo-mcp-skills](https://github.com/Ryze-AI-Adgent/open-seo-mcp-skills) · [notfair-plugin](https://github.com/nowork-studio/notfair-plugin) · [claude-blog](https://github.com/AgriciDaniel/claude-blog) · [opc-skills](https://github.com/ReScienceLab/opc-skills) · [geo-optimizer-skill](https://github.com/Auriti-Labs/geo-optimizer-skill) · [seo-skills](https://github.com/Illyism/seo-skills) · [geolook](https://github.com/aigclink/geolook) · [geo-doctor](https://github.com/Fangx-AI/geo-doctor) · [elmo](https://github.com/elmohq/elmo) · [limelit-co/open](https://github.com/limelit-co/open) · [GetCito](https://github.com/ai-search-guru/getcito-worlds-first-open-source-aio-aeo-or-geo-tool) · [voyage-geo-agent](https://github.com/onvoyage-ai/voyage-geo-agent) · [geo-aeo-tracker](https://github.com/danishashko/geo-aeo-tracker) · [everyinfra/seo-skills](https://github.com/everyinfra/seo-skills) · [SEO-GEO-AEO-Skill](https://github.com/SNLabat/SEO-GEO-AEO-Skill) · [seobuild-onpage](https://github.com/gbessoni/seobuild-onpage) · [ansvisor](https://github.com/ansvisor/ansvisor) · [GEO-Content-Optimizer-Skill](https://github.com/liangdabiao/GEO-Content-Optimizer-Skill) · [eGEOagents](https://github.com/mverab/eGEOagents) · [seo-skills](https://github.com/seranking/seo-skills) · [canonry](https://github.com/Canonry/canonry) · [seo-geo-audit](https://github.com/dageno-agents/seo-geo-audit) · [codex-seo](https://github.com/zhtyyx/codex-seo) · [claude-rank](https://github.com/Houseofmvps/claude-rank) · [orangeo-ai-visibility-skill](https://github.com/OranAi-Ltd/orangeo-ai-visibility-skill) · [All-In-One-Free-SEO-Tool](https://github.com/IamRamgarhia/All-In-One-Free-SEO-Tool) · [ultimate-seo-geo](https://github.com/mykpono/ultimate-seo-geo) · [HeiGe-GEO-SEO](https://github.com/HeiGeAi/HeiGe-GEO-SEO) · [claude-seo-ai](https://github.com/Hainrixz/claude-seo-ai) · [akii-seo-ai-search-optimizer](https://github.com/akii-technologies-ltd/akii-seo-ai-search-optimizer) · [seo-skills/geo-audit-skill](https://github.com/seo-skills/geo-audit-skill) · [mcp-geo](https://github.com/AKzar1el/mcp-geo) · [geo-score](https://github.com/jianruntech/geo-score) · [geoskills](https://github.com/Cognitic-Labs/geoskills) · [local-falcon/mcp](https://github.com/local-falcon/mcp) · [aicw-ai-mentions](https://github.com/aichatwatch/aicw-ai-mentions) · [autoseo](https://github.com/codextde/autoseo) · [seojuice-skills](https://github.com/calm-north/seojuice-skills) · [webappski/aeo-platform](https://github.com/webappski/aeo-platform) · [topcited-skills](https://github.com/TopCited/topcited-skills) · [seo-skills](https://github.com/RomeoSEO/seo-skills) · [citation-intelligence](https://github.com/AutomateLab-tech/citation-intelligence) · [agent-readiness](https://github.com/Canonry/agent-readiness) · [literallydotdev/aeo](https://github.com/literallydotdev/aeo) · [peec-ai-tracking-strategy-builder](https://github.com/rebelytics/peec-ai-tracking-strategy-builder) · [geo-scope](https://github.com/tmolavi/geo-scope) · [geo-skills](https://github.com/aivisibilitycensus/geo-skills) · [CiteLadder](https://github.com/abhij1306/CiteLadder) · [aeo-geo-bestpractices](https://github.com/micaelgomestavares/aeo-geo-bestpractices) · [rankcontrol](https://github.com/rankcontrol/rankcontrol) · [geo-audit](https://github.com/g-shevchenko/geo-audit) · [cloro-dev/geo-tracker](https://github.com/cloro-dev/geo-tracker) · [llms-txt-writer](https://github.com/shimo4228/llms-txt-writer) · [ai-visibility-tracking-strategy-builder](https://github.com/rebelytics/ai-visibility-tracking-strategy-builder) · [seo-aeo-audit](https://github.com/ssheleg/seo-aeo-audit) · [seo-geo-smart-audit-skill](https://github.com/yangjing6213-dev/seo-geo-smart-audit-skill) · [zaDojo](https://github.com/zaDojo/seo-geo-mcp)

**Claude**（46）：[geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) · [open-seo-mcp-skills](https://github.com/Ryze-AI-Adgent/open-seo-mcp-skills) · [newsjack](https://github.com/elvisun/newsjack) · [gtm-engineer-skills](https://github.com/onvoyage-ai/gtm-engineer-skills) · [geo-optimizer-skill](https://github.com/Auriti-Labs/geo-optimizer-skill) · [geolook](https://github.com/aigclink/geolook) · [geo-doctor](https://github.com/Fangx-AI/geo-doctor) · [elmo](https://github.com/elmohq/elmo) · [limelit-co/open](https://github.com/limelit-co/open) · [OpenGSO](https://github.com/sherwinvishesh/OpenGSO) · [voyage-geo-agent](https://github.com/onvoyage-ai/voyage-geo-agent) · [ansvisor](https://github.com/ansvisor/ansvisor) · [eGEOagents](https://github.com/mverab/eGEOagents) · [canonry](https://github.com/Canonry/canonry) · [claude-rank](https://github.com/Houseofmvps/claude-rank) · [aeo.js](https://github.com/rubenmarcus/aeo.js) · [orangeo-ai-visibility-skill](https://github.com/OranAi-Ltd/orangeo-ai-visibility-skill) · [HeiGe-GEO-SEO](https://github.com/HeiGeAi/HeiGe-GEO-SEO) · [claude-seo-ai](https://github.com/Hainrixz/claude-seo-ai) · [akii-seo-ai-search-optimizer](https://github.com/akii-technologies-ltd/akii-seo-ai-search-optimizer) · [shopify-theme-audit-skill](https://github.com/tanujrajputdev/shopify-theme-audit-skill) · [seo-skills/geo-audit-skill](https://github.com/seo-skills/geo-audit-skill) · [mcp-geo](https://github.com/AKzar1el/mcp-geo) · [geo-score](https://github.com/jianruntech/geo-score) · [aicw-ai-mentions](https://github.com/aichatwatch/aicw-ai-mentions) · [autoseo](https://github.com/codextde/autoseo) · [WorkSmartAI-alt/ai-visibility-monitor](https://github.com/WorkSmartAI-alt/ai-visibility-monitor) · [vinpatel/aeorank](https://github.com/vinpatel/aeorank) · [agent-lighthouse](https://github.com/ForkPoint/agent-lighthouse) · [webappski/aeo-platform](https://github.com/webappski/aeo-platform) · [topcited-skills](https://github.com/TopCited/topcited-skills) · [seo-skills](https://github.com/RomeoSEO/seo-skills) · [citation-intelligence](https://github.com/AutomateLab-tech/citation-intelligence) · [search-os](https://github.com/vamsireddy4/search-os) · [agent-readiness](https://github.com/Canonry/agent-readiness) · [literallydotdev/aeo](https://github.com/literallydotdev/aeo) · [ai-bot-access](https://github.com/codevibe-technology/ai-bot-access) · [aeo-toolkit](https://github.com/Advance-Labs/aeo-toolkit) · [CiteLadder](https://github.com/abhij1306/CiteLadder) · [aeo-geo-bestpractices](https://github.com/micaelgomestavares/aeo-geo-bestpractices) · [rankcontrol](https://github.com/rankcontrol/rankcontrol) · [geolint](https://github.com/iliasabk/geolint) · [geo-audit](https://github.com/g-shevchenko/geo-audit) · [seo-aeo-audit](https://github.com/ssheleg/seo-aeo-audit) · [seo-geo-smart-audit-skill](https://github.com/yangjing6213-dev/seo-geo-smart-audit-skill) · [a-bibikov/ai-search-audit](https://github.com/a-bibikov/ai-search-audit)

**豆包**（7）：[yao-geo-skills](https://github.com/yaojingang/yao-geo-skills) · [geolook](https://github.com/aigclink/geolook) · [geo-doctor](https://github.com/Fangx-AI/geo-doctor) · [GEO-Content-Optimizer-Skill](https://github.com/liangdabiao/GEO-Content-Optimizer-Skill) · [HeiGe-GEO-SEO](https://github.com/HeiGeAi/HeiGe-GEO-SEO) · [GEOVisibilityTool](https://github.com/MasashiToda1/GEOVisibilityTool) · [geo-automation-skill-pack](https://github.com/noahneancy-byte/geo-automation-skill-pack)

**腾讯元宝**（4）：[yao-geo-skills](https://github.com/yaojingang/yao-geo-skills) · [geo-doctor](https://github.com/Fangx-AI/geo-doctor) · [HeiGe-GEO-SEO](https://github.com/HeiGeAi/HeiGe-GEO-SEO) · [GEOVisibilityTool](https://github.com/MasashiToda1/GEOVisibilityTool)

**Kimi**（5）：[yao-geo-skills](https://github.com/yaojingang/yao-geo-skills) · [geolook](https://github.com/aigclink/geolook) · [geo-doctor](https://github.com/Fangx-AI/geo-doctor) · [GEO-Content-Optimizer-Skill](https://github.com/liangdabiao/GEO-Content-Optimizer-Skill) · [GEOVisibilityTool](https://github.com/MasashiToda1/GEOVisibilityTool)

**DeepSeek**（7）：[yao-geo-skills](https://github.com/yaojingang/yao-geo-skills) · [geolook](https://github.com/aigclink/geolook) · [geo-doctor](https://github.com/Fangx-AI/geo-doctor) · [voyage-geo-agent](https://github.com/onvoyage-ai/voyage-geo-agent) · [orangeo-ai-visibility-skill](https://github.com/OranAi-Ltd/orangeo-ai-visibility-skill) · [HeiGe-GEO-SEO](https://github.com/HeiGeAi/HeiGe-GEO-SEO) · [GEOVisibilityTool](https://github.com/MasashiToda1/GEOVisibilityTool)

**千问**（4）：[yao-geo-skills](https://github.com/yaojingang/yao-geo-skills) · [geo-doctor](https://github.com/Fangx-AI/geo-doctor) · [HeiGe-GEO-SEO](https://github.com/HeiGeAi/HeiGe-GEO-SEO) · [GEOVisibilityTool](https://github.com/MasashiToda1/GEOVisibilityTool)

**应用商店**（5）：[aso-skills](https://github.com/appeeky/aso-skills) · [vibe-aso](https://github.com/Kronop/vibe-aso) · [app-store-aso](https://github.com/TimBroddin/skills) · [Manifold](https://github.com/manifoldmcp/marketing-skills) · [applyra-aso-skill](https://github.com/lucholabs/applyra-aso-skill)

**电商站内搜索（亚马逊等）**（6）：[amazon-sorftime-research-MCP-skill](https://github.com/liangdabiao/amazon-sorftime-research-MCP-skill) · [Amazon-Skills](https://github.com/nexscope-ai/Amazon-Skills) · [etsy-listing-helper](https://github.com/silennsong/etsy-listing-helper) · [taobao-shop-growth](https://github.com/yuyang2230/taobao-shop-growth) · [fiverr-gig-optimizer](https://github.com/waseemnasir2k26/fiverr-gig-optimizer) · [Manifold](https://github.com/manifoldmcp/marketing-skills)

**通用**（38）：[open-seo](https://github.com/every-app/open-seo) · [niubigeo](https://github.com/Albert-Weasker/niubigeo) · [GEOFlow](https://github.com/yaojingang/GEOFlow) · [aaron-marketing-skills](https://github.com/aaron-he-zhu/aaron-marketing-skills) · [growth-lab](https://github.com/tsingyuai/growth-lab) · [python-seo-analyzer](https://github.com/sethblack/python-seo-analyzer) · [LibreCrawl](https://github.com/PhialsBasement/LibreCrawl) · [seo-ops](https://github.com/tigerless-labs/seo-ops) · [specification.website](https://github.com/jdevalk/specification.website) · [seo-skills/seo-audit-skill](https://github.com/seo-skills/seo-audit-skill) · [recomby-geo](https://github.com/ViryaZheng/recomby-geo) · [geo-first-principles](https://github.com/ALLENLION35/geo-first-principles) · [geoptimize](https://github.com/cucuwang/geoptimize) · [geo-content-writer](https://github.com/dageno-agents/geo-content-writer) · [GEOHub](https://github.com/yaojingang/GEOHub) · [qwoted-seo-backlinks-skill](https://github.com/Bomx/qwoted-seo-backlinks-skill) · [jdevalk/skills](https://github.com/jdevalk/skills) · [squirrelscan/skills](https://github.com/squirrelscan/skills) · [screaming-frog-mcp](https://github.com/bzsasson/screaming-frog-mcp) · [openspider](https://github.com/wojcikdominik/openspider) · [contentforge](https://github.com/indranilbanerjee/contentforge) · [agentmarkup](https://github.com/agentmarkup/agentmarkup) · [mcp-abilities-rankmath](https://github.com/bjornfix/mcp-abilities-rankmath) · [seo-signal-skills](https://github.com/daily-growth-signals/seo-signal-skills) · [CodoSEO](https://github.com/SafrowLabs/CodoSEO) · [where-to-submit-your-startup](https://github.com/mmmmingos/where-to-submit-your-startup) · [mcp-web-validator](https://github.com/AKzar1el/mcp-web-validator) · [seo-aeo-geo-ultimate](https://github.com/oegeyilmaz9/seo-aeo-geo-ultimate) · [crawlgraph-mcp](https://github.com/pucilpet/crawlgraph-mcp) · [ubersuggest/seo-skills](https://github.com/ubersuggest/seo-skills) · [foreign-trade-geo-skill](https://github.com/Elvinaskill/foreign-trade-geo-skill) · [blacksparrow](https://github.com/Shantodotdev/blacksparrow) · [sitebulb-plugin](https://github.com/sitebulb/sitebulb-plugin) · [searvex](https://github.com/cihantopac/searvex) · [bulk-ai-cli-connector](https://github.com/puneetindersingh/bulk-ai-cli-connector) · [seranking/marketing-automation-plugins](https://github.com/seranking/marketing-automation-plugins) · [Quincunx33/ai-seo-skill](https://github.com/Quincunx33/ai-seo-skill) · [rankparse-mcp](https://github.com/Rankparse/rankparse-mcp)

<a id="faq"></a>
## 常见问题

### GEO 是什么？和 SEO 有什么区别？

SEO（搜索引擎优化）是让 Google、百度这类搜索引擎把你的网页排在前面。GEO（生成式引擎优化，也叫 AEO）是让 ChatGPT、Perplexity、Google AI 概览、豆包这类 AI 回答提到和引用你。两者有重叠：AI 搜索多半也先去搜索引擎找网页，所以 SEO 做得好是 GEO 的基础；但 AI 更看重能直接摘出来的答案、清楚的出处和被别处提到的次数。专做 GEO 的项目在 [GEO：让 AI 回答引用你](#group-geo)，共 42 个。

### 有哪些好用的 SEO skill？

收录 175 个人工核对过的 SEO 和 GEO skill 项目（数据更新于 2026-11-16）。想一套管到底，先看[全套](#group-pipeline)（35 个），星数最高的是 [marketingskills](https://github.com/coreyhaines31/marketingskills)、[claude-seo](https://github.com/AgriciDaniel/claude-seo)、[notfair-plugin](https://github.com/nowork-studio/notfair-plugin)；只缺某一步，看关键词和排名数据、内容、技术审计、外链各节。

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

收录前逐个核对过仓库说明、目录和文件，并用脚本查过二进制和压缩包、安装钩子、远程执行和读敏感文件。收录了 175 个 skill 项目和 51 个工具。看过但没收的，原因逐条记在 [data/ignore.toml](data/ignore.toml)（目前 496 个）。脚本查不到不等于安全，安装前先读一遍它的 `SKILL.md` 和脚本。

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
