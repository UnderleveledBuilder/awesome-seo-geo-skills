---
name: seo-geo-skill-finder
description: Recommend SEO and GEO (generative engine optimization) skills and MCP tools from a hand-checked, security-scanned list, matched to the job (keyword and competitor research, content writing and optimization, technical SEO and site audits, analytics and rank tracking, local, e-commerce and app stores, backlinks and PR, getting cited in AI answers), the target (Google, Bing, Baidu/百度, ChatGPT, Perplexity, Gemini, Claude, Google AI Overviews, Doubao/豆包, Yuanbao/元宝, Kimi, DeepSeek, Qwen/千问) and the agent (Claude Code, Codex, OpenClaw/龙虾, Qwen, Doubao, WorkBuddy). Use when someone asks which skill or tool to use for SEO, GEO, AEO, AI search visibility or llms.txt, or how to install one. 帮你从人工核对、做过安全检查的 SEO 和 GEO skill 清单里挑合适的：关键词、内容优化、技术审计、排名监测，以及让 AI 回答引用你。
---

# SEO and GEO skill finder

Pick skills for SEO and GEO work from the Awesome SEO & GEO Skills list (https://github.com/UnderleveledBuilder/awesome-seo-geo-skills). Every entry was checked by hand, scanned by a script for risky files and commands, and tagged by job, target engine, format and supported agents.

## 1. Get the data

Fetch `https://raw.githubusercontent.com/UnderleveledBuilder/awesome-seo-geo-skills/main/catalog.json`. If that fails, read `README.md` (English: `README.en.md`) from the same place; it has the same entries without the structured fields.

`catalog.json` has `updated`, `groups`, `facets` (the `engines` labels), `formats` and `entries`. Each entry has:

| Field | Meaning |
|---|---|
| `repo`, `url`, `name` | GitHub repo |
| `group` | `pipeline` all-in-one, `geo` AI answer visibility, `cn-ai` Chinese AI search, `research` (keywords, competitors, rankings and Search Console/GA4 data), `content`, `technical`, `local` (local, e-commerce and app stores), `offsite` (backlinks, PR and off-site mentions), `mcp` (MCP server or CLI tool, not a skill), `apps` (full app) |
| `engines` | What it targets, such as `google` `ai-overviews` `bing` `baidu` `chatgpt` `perplexity` `gemini` `claude` `doubao` `yuanbao` `kimi` `deepseek` `qwen`, plus `app-stores` and `marketplaces` (Amazon and other store search); `general` means any engine |
| `format` | `skill` (standard SKILL.md), `prompts`, `mcp`, `app` |
| `agents` | Agents the author says it supports; empty means not stated (most SKILL.md skills work in any agent that loads skills) |
| `desc`, `desc_en`, `note`, `note_en` | Summary and editor's note in Chinese and English |
| `install` | Install command when there is one, such as `npx skills add owner/repo` |
| `lang` | Main language of the skill's own text |
| `featured`, `checked`, `stars`, `pushed_at`, `license`, `skills` | Editor's pick, date checked, GitHub stars, last push, license, number of skills in the repo |

## 2. Understand the need

Work out, asking at most one short question if it is unclear:
- classic SEO (rankings in Google, Bing or Baidu), GEO (being cited by AI answers), or both;
- the job: keyword or ranking data, content, technical audit, local, e-commerce or app stores, backlinks and PR;
- whether they have data access the tool needs (Search Console, GA, a paid SEO API key);
- the agent they use, output language, and any license constraint.

## 3. Choose

- Drop entries whose `pushed_at` is over a year old unless nothing else fits.
- Keep entries whose `engines` match (or `general`) and whose `group` fits the job. Prefer, in order: `featured`, a matching agent in `agents`, `format` = `skill`, recent `pushed_at`, a license that fits. Use `stars` only to break ties.
- Recommend 3 to 5 entries. Pair a skill with an `mcp` tool when the job needs live data.

## 4. Answer

Answer in the user's language, using `desc`/`note` for Chinese and `desc_en`/`note_en` for English. For each pick give:
- name, linked to `url`;
- one sentence on why it fits;
- the `install` command, or "see the repo README" when there is none;
- supported agents, license and last update.

Then:
- say the list was last updated on `updated`;
- say plainly that no skill can guarantee rankings or AI citations;
- remind the user that skills can ship scripts, so read a skill's SKILL.md before installing it. Do not run install commands without the user's go-ahead.

If nothing in the list fits, say so plainly instead of stretching a match.
