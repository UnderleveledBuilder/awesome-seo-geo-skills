"""在 GitHub 上找可能值得收录的新项目，输出 Markdown 候选清单；顺带标出别人新开的同类清单。

本文件来自共用代码 kit（见 scripts/KIT），各清单内容一样。

搜索词在 data/taxonomy.toml 的 [discover]：
- queries：关键词，带不带 "skill" 字样的都要有，不带的用来找平台类项目
- topics：GitHub topic，按 topic: 查询
- lists：找同类清单用的词；名字以 awesome 开头的仓库也算同类清单，单列一节
已收录（skills.toml）和已忽略（ignore.toml）的仓库会被排除。

用法：
  python3 scripts/discover.py --days 7 --out candidates.md                 # 每周（Actions 跑这个）
  python3 scripts/discover.py --since 2025-10-01 --min-stars 0 --pages 3   # 大扫描：skill 从 2025-10 起才兴起
"""

from __future__ import annotations

import argparse
import datetime as dt
import sys
import time
import urllib.parse

from lib import NotFound, gh_get, load_valid, repo_tree, skill_dirs

SEARCH_INTERVAL = 2.5  # 搜索接口限额 30 次/分钟


def search(q: str, since: str, min_stars: int, pages: int) -> list[dict]:
    items: list[dict] = []
    for page in range(1, pages + 1):
        params = urllib.parse.urlencode({"q": f"{q} pushed:>={since} stars:>={min_stars}", "sort": "stars",
                                         "per_page": 100, "page": page})
        batch = gh_get(f"search/repositories?{params}")["items"]
        items += batch
        time.sleep(SEARCH_INTERVAL)
        if len(batch) < 100:
            break
    return items


def table(rows: list[dict], with_skills: bool) -> list[str]:
    head = "| 仓库 | ★ | 最近推送 | 创建 |" + (" SKILL.md |" if with_skills else "") + " 简介 | 命中 |"
    lines = [head, "|---|--:|---|---|" + ("--:|" if with_skills else "") + "---|---|"]
    for e in rows:
        r = e["repo"]
        desc = (r.get("description") or "").replace("|", "\\|").replace("\n", " ")[:120]
        cells = [f"[{r['full_name']}]({r['html_url']})", str(r["stargazers_count"]), r["pushed_at"][:10],
                 r["created_at"][:10]]
        if with_skills:
            cells.append(e.get("skills", "?"))
        cells += [desc, "、".join(e["queries"][:4]) + ("……" if len(e["queries"]) > 4 else "")]
        lines.append("| " + " | ".join(cells) + " |")
    return lines


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--days", type=int, default=30, help="只看最近 N 天内有推送的仓库（默认 30）")
    ap.add_argument("--since", help="只看这天以后有推送的仓库，如 2025-10-01；给了就不看 --days")
    ap.add_argument("--min-stars", type=int, default=3, help="最低星数（默认 3）")
    ap.add_argument("--pages", type=int, default=1, help="每个查询翻几页，每页 100 个（默认 1）")
    ap.add_argument("--out", help="写入文件，默认打印到终端")
    args = ap.parse_args()

    taxonomy, skills, ignored = load_valid()
    known = {s["repo"].lower() for s in skills} | {i["repo"].lower() for i in ignored}
    since = args.since or (dt.date.today() - dt.timedelta(days=args.days)).isoformat()
    disc = taxonomy.get("discover", {})
    queries = [(q, q) for q in disc.get("queries", [])] + [(f"topic:{t}", f"topic:{t}") for t in disc.get("topics", [])]
    list_queries = [(q, q) for q in disc.get("lists", [])]
    own = taxonomy.get("list", {}).get("repo", "").split("/")[0].lower()  # 自己的清单不算同类清单

    found: dict[str, dict] = {}
    lists: dict[str, dict] = {}
    for q, label in queries + list_queries:
        try:
            items = search(q, since, args.min_stars, args.pages)
        except NotFound:
            print(f"  {label}: 查询出错，跳过", file=sys.stderr)
            continue
        print(f"  {label}: {len(items)}", file=sys.stderr)
        is_list_query = (q, label) in list_queries
        for it in items:
            key = it["full_name"].lower()
            if key in known or it.get("fork") or it["owner"]["login"].lower() == own:
                continue
            target = lists if (is_list_query or it["name"].lower().startswith("awesome")) else found
            target.setdefault(key, {"repo": it, "queries": []})["queries"].append(label)

    rows = sorted(found.values(), key=lambda e: -e["repo"]["stargazers_count"])
    for e in rows:
        r = e["repo"]
        try:
            tree, truncated = repo_tree(r["full_name"], r["default_branch"])
            e["skills"] = f"{len(skill_dirs(tree))}{'+' if truncated else ''}"
        except NotFound:
            e["skills"] = "?"
    list_rows = sorted(lists.values(), key=lambda e: -e["repo"]["stargazers_count"])

    lines = [
        f"# 候选项目（{dt.date.today().isoformat()}）",
        "",
        f"{since} 以后有推送、至少 {args.min_stars} 星，已排除收录和忽略的仓库，共 {len(rows)} 个。",
        "收录：先跑 `python3 scripts/security.py 仓库名` 做安全检查，再把条目加进 `data/skills.toml`；"
        "不收：加进 `data/ignore.toml` 并写明原因。",
        "",
        *table(rows, with_skills=True),
    ]
    if list_rows:
        lines += ["", f"## 同类清单（{len(list_rows)}）", "", "别人新开或在更新的同类清单，只看不收。", "",
                  *table(list_rows, with_skills=False)]
    text = "\n".join(lines) + "\n"

    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"已写入 {args.out}：{len(rows)} 个候选，{len(list_rows)} 个同类清单。", file=sys.stderr)
    else:
        print(text)


if __name__ == "__main__":
    main()
