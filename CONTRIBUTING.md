# 参与贡献

## 收录标准

满足以下全部条件：

1. **服务 SEO 或 GEO**：关键词研究和排名数据、内容写作和优化、技术 SEO 和站点审计、本地、电商和应用商店优化、外链和 PR，以及让 AI 回答引用你的 GEO。搜索引擎和 AI 平台不限，国内国外都收。
2. **能装进 agent 使用**：标准 `SKILL.md`、Claude Code 插件，或结构清晰的提示词工作流。提示词形式的项目会标 📝。MCP 服务和命令行工具收进「MCP 和命令行工具」，标 🔌；完整应用收进「相关开源平台」，门槛是 1000★。应用里附带的 SKILL.md 如果能单独装进 agent 使用，可以按 skill 收录。
3. **有说明**：README 写清楚做什么、怎么装。
4. **过了安全检查**：收录前跑 `python3 scripts/security.py owner/repo`。查到问题的要人看过再决定；可疑安装包、诱导下载 exe 或 dmg 的不收。

星数不是门槛，冷门但有独到方法的项目同样欢迎。很久没更新的照样收，标 💤。不收的：可疑安装包、装不上、只服务一个人或一个网站、没加东西的 fork 或改名。

## 怎么提交

**不想动代码**：[提交 issue](../../issues/new?template=submit-skill.yml)，填仓库地址和推荐理由即可。

**直接发 PR**：

1. 在 `data/skills.toml` 追加一条（字段见下文）。
2. 本地运行（需要 Python 3.11+，无第三方依赖）：

   ```bash
   python3 scripts/security.py owner/repo        # 安全检查
   python3 scripts/refresh.py --only owner/repo  # 抓取星数、许可证等元数据
   python3 scripts/build.py                      # 重新生成 README.md、README.en.md 和 catalog.json
   ```

   跳过第 2、3 步也可以，合并后 GitHub Actions 会自动刷新并生成。
3. 提交 PR。CI 会校验数据格式。

## 字段说明

```toml
[[skills]]
repo      = "owner/repo"             # 必填，GitHub 仓库
desc      = "一句话说清做什么"          # 必填，≤ 80 字，写具体能力，少用形容词
desc_en   = "One-line English desc"   # 必填，≤ 260 个字符；不会写可以留空字符串，维护者合并时补
group     = "geo"                    # 必填，类型，取值见 data/taxonomy.toml [groups]
engines   = ["chatgpt", "doubao"]    # 必填，针对的搜索引擎或 AI 平台，见 [facets.engines]；不挑写 general
format    = "skill"                  # 必填，skill / prompts / mcp / app
lang      = "zh"                     # 必填，zh / en / ja / ko / multi（指 skill 正文的语言）
checked   = 2026-10-19               # 必填，人工核对日期（TOML 日期，不加引号）
agents    = ["claude-code"]          # 可选，仓库明确说明支持的 agent，见 [agents]
install   = "npx skills add ..."     # 可选，默认生成 npx skills add owner/repo
name      = "显示名"                  # 可选，默认取仓库名
tier      = "featured"               # 可选，精选；默认 listed
note      = "需要注意的地方"            # 可选，显示在简介下方
note_en   = "English note"           # note 的英文版，和 note 一起写
```

`agents` 和 `engines` 只填仓库里明确写了的，不要推测。星数、许可证、最近更新时间、skill 数量由 `scripts/refresh.py` 自动抓取，不用手填。

## 收录徽章

项目被收录后，可以在自己的 README 里加上收录徽章，代码见 [README 的「收录徽章」一节](README.md#badge)。

## 不收录的项目

看过但决定不收的项目记在 `data/ignore.toml`，并写明原因，这样 `discover.py` 不会再把它们列为候选。

## 维护者工作流

| 脚本 | 作用 |
|---|---|
| `scripts/refresh.py` | 刷新元数据，报告改名、失效、归档、久未更新的仓库 |
| `scripts/build.py` | 生成 README.md、README.en.md 和 catalog.json；`--check` 检查是否最新，`--validate` 只校验数据 |
| `scripts/discover.py` | 按 taxonomy.toml 里的关键词和 topic 搜候选项目，单列别人新开的同类清单 |
| `scripts/security.py` | 收录前的安全检查 |

`scripts/` 和 `.github/workflows/` 来自几个 awesome 清单共用的代码（见 `scripts/KIT`），改动请提 issue。GitHub Actions 每周一自动刷新元数据、重新生成 README，并把新候选开成 issue。
