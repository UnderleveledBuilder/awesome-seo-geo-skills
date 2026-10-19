"""数据加载、校验和 GitHub 访问。只依赖标准库（Python 3.11+）。

本文件来自共用代码 kit（见 scripts/KIT），各清单的同名文件内容一样。要改请改 kit 再同步，别在清单里单独改。
清单自己的东西都在 data/ 和 templates/：分类、维度和搜索词在 data/taxonomy.toml，条目在 data/skills.toml。
"""

from __future__ import annotations

import datetime as dt
import http.client
import json
import os
import re
import subprocess
import sys
import time
import tomllib
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
META_PATH = DATA / "meta.json"

REPO_RE = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")
REQUIRED = {"repo", "desc", "desc_en", "group", "format", "lang", "checked"}
OPTIONAL = {"name", "agents", "install", "tier", "note", "note_en", "skill_paths"}
TIERS = {"featured", "listed"}
DESC_MAX = 80
DESC_EN_MAX = 260

# 第三方文字（仓库简介、SKILL.md 说明）不经人工就会被展示时，先去掉链接；像引流或针对 AI 的指令的整段不展示。
THIRD_PARTY_URL = re.compile(r"(https?://|www\.)\S+", re.I)
THIRD_PARTY_BLOCK = re.compile(
    r"ignore\s+(all\s+|any\s+)?(previous|prior|above)\s+(instructions|prompts)|system\s+prompt"
    r"|忽略(之前|以上|上面|前面)"
    r"|加\s*(微信|vx|v信|wx|qq|群)|微信号|qq\s*群|vx\s*[:：]|wx\s*[:：]",
    re.I,
)


def third_party_text(text: str) -> str:
    """第三方文字展示前的清洗：去掉链接；命中拦截规则时返回空串。"""
    if not text or THIRD_PARTY_BLOCK.search(text):
        return ""
    return re.sub(r"\s{2,}", " ", THIRD_PARTY_URL.sub("", text)).strip()


def load_toml(name: str, default: dict | None = None) -> dict:
    path = DATA / name
    if not path.exists() and default is not None:
        return default
    with open(path, "rb") as f:
        return tomllib.load(f)


def load_meta() -> dict:
    if not META_PATH.exists():
        return {"fetched_at": None, "repos": {}}
    return json.loads(META_PATH.read_text(encoding="utf-8"))


def save_meta(meta: dict) -> None:
    META_PATH.write_text(json.dumps(meta, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def facets(taxonomy: dict) -> dict[str, dict]:
    """清单自己的维度（短剧的创作阶段、自媒体的平台……），在 taxonomy.toml 的 [facets.<字段名>] 里声明。"""
    return taxonomy.get("facets", {})


def load_all() -> tuple[dict, list[dict], list[dict]]:
    taxonomy = load_toml("taxonomy.toml")
    skills = load_toml("skills.toml", {}).get("skills", [])
    ignored = load_toml("ignore.toml", {}).get("ignored", [])
    return taxonomy, skills, ignored


def validate(taxonomy: dict, skills: list[dict], ignored: list[dict]) -> list[str]:
    errors: list[str] = []
    seen: dict[str, int] = {}
    fs = facets(taxonomy)
    allowed = REQUIRED | OPTIONAL | set(fs)

    for i, s in enumerate(skills, 1):
        where = f"skills.toml 第 {i} 条（{s.get('repo', '?')}）"
        missing = REQUIRED - s.keys()
        if missing:
            errors.append(f"{where}: 缺少字段 {sorted(missing)}")
        unknown = s.keys() - allowed
        if unknown:
            errors.append(f"{where}: 未知字段 {sorted(unknown)}")

        repo = s.get("repo", "")
        if not REPO_RE.match(repo):
            errors.append(f"{where}: repo 应为 owner/name 格式")
        key = repo.lower()
        if key in seen:
            errors.append(f"{where}: 与第 {seen[key]} 条重复")
        seen[key] = i

        if len(s.get("desc", "")) > DESC_MAX:
            errors.append(f"{where}: desc 超过 {DESC_MAX} 字（当前 {len(s['desc'])}）")
        if len(s.get("desc_en", "")) > DESC_EN_MAX:
            errors.append(f"{where}: desc_en 超过 {DESC_EN_MAX} 个字符（当前 {len(s['desc_en'])}）")
        if bool(s.get("note")) != bool(s.get("note_en")):
            errors.append(f"{where}: note 和 note_en 要么都写，要么都不写")
        if s.get("group") not in taxonomy["groups"]:
            errors.append(f"{where}: group '{s.get('group')}' 不在 taxonomy.groups 里")
        if s.get("format") not in taxonomy["formats"]:
            errors.append(f"{where}: format '{s.get('format')}' 不在 taxonomy.formats 里")
        if s.get("lang") not in taxonomy["langs"]:
            errors.append(f"{where}: lang '{s.get('lang')}' 不在 taxonomy.langs 里")
        for ag in s.get("agents", []):
            if ag not in taxonomy["agents"]:
                errors.append(f"{where}: agent '{ag}' 不在 taxonomy.agents 里")
        for field, f in fs.items():
            values = s.get(field, [])
            if f.get("required") and not values:
                errors.append(f"{where}: {field} 不能为空")
            for v in values:
                if v not in f["values"]:
                    errors.append(f"{where}: {field} 的值 '{v}' 不在 taxonomy.facets.{field}.values 里")
        if s.get("tier", "listed") not in TIERS:
            errors.append(f"{where}: tier 只能是 {sorted(TIERS)}")
        if "checked" in s and not isinstance(s["checked"], dt.date):
            errors.append(f"{where}: checked 应写成 TOML 日期，如 2026-10-19（不加引号）")

    for ig in ignored:
        if ig.get("repo", "").lower() in seen:
            errors.append(f"ignore.toml: {ig['repo']} 同时出现在 skills.toml 里")
        if not ig.get("reason"):
            errors.append(f"ignore.toml: {ig.get('repo')} 缺少 reason")

    return errors


def load_valid() -> tuple[dict, list[dict], list[dict]]:
    data = load_all()
    errors = validate(*data)
    if errors:
        print("数据校验失败：", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        sys.exit(1)
    return data


# ───────────────────────── GitHub API ─────────────────────────

class NotFound(Exception):
    pass


def github_token() -> str | None:
    for var in ("GITHUB_TOKEN", "GH_TOKEN"):
        if os.environ.get(var):
            return os.environ[var]
    try:
        out = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True, timeout=10)
        if out.returncode == 0 and out.stdout.strip():
            return out.stdout.strip()
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass
    return None


_TOKEN = github_token()


def gh_get(path: str) -> dict:
    url = path if path.startswith("https://") else f"https://api.github.com/{path.lstrip('/')}"
    req = urllib.request.Request(url, headers={
        "Accept": "application/vnd.github+json",
        "User-Agent": ROOT.name,
        **({"Authorization": f"Bearer {_TOKEN}"} if _TOKEN else {}),
    })
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.load(resp)
        except urllib.error.HTTPError as e:
            if e.code in (404, 409, 451):  # 409：空仓库没有 git tree
                raise NotFound(path) from e
            if e.code == 403 and e.headers.get("X-RateLimit-Remaining") == "0":
                reset = dt.datetime.fromtimestamp(int(e.headers.get("X-RateLimit-Reset", "0")))
                sys.exit(f"GitHub API 配额用完，{reset:%H:%M} 重置。设置 GITHUB_TOKEN 或登录 gh 可提高配额。")
            if e.code < 500 or attempt == 2:
                raise
        except (OSError, http.client.HTTPException):
            if attempt == 2:  # 网络抖动：几百个仓库刷一遍时难免遇到，重试两次
                raise
        time.sleep(2 * (attempt + 1))


def raw_text(repo: str, branch: str, path: str, limit: int = 200_000) -> str | None:
    """从 raw.githubusercontent.com 读一个文本文件（不占 API 配额）。读不到或太大返回 None。"""
    url = f"https://raw.githubusercontent.com/{repo}/{branch}/{urllib.parse.quote(path)}"
    req = urllib.request.Request(url, headers={"User-Agent": ROOT.name})
    for attempt in range(2):
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                body = resp.read(limit + 1)
            return None if len(body) > limit else body.decode("utf-8", errors="replace")
        except urllib.error.HTTPError:
            return None
        except (OSError, http.client.HTTPException):
            time.sleep(2)
    return None


def has_token() -> bool:
    return _TOKEN is not None


# 同一个 skill 常被复制进各家 agent 的目录（.claude/skills/x、.codex/skills/x、skills/x），
# 也有按版本号存多份的（skills/x/1.0.0、skills/x/1.1.0），都只算一次。
VERSION_DIR = re.compile(r"^v?\d+(\.\d+)*$")


def skill_dirs(tree: list[dict]) -> list[str]:
    """git tree 里的 skill：SKILL.md 所在目录按 skill 名去重，返回每个 skill 的第一个目录。"""
    seen: dict[str, str] = {}
    for item in tree:
        path = item["path"]
        if item["type"] != "blob" or path.rsplit("/", 1)[-1].lower() != "skill.md":
            continue
        parent = path.rsplit("/", 1)[0] if "/" in path else ""
        parts = parent.split("/") if parent else []
        cut = max((i for i, p in enumerate(parts) if p.lower() == "skills"), default=-1)
        if 0 <= cut < len(parts) - 1:
            name = parts[cut + 1]
        else:
            rest = [p for p in parts if not VERSION_DIR.match(p)]
            name = rest[-1] if rest else ""
        seen.setdefault(name.lower(), parent)
    return sorted(seen.values())


def repo_tree(full_name: str, branch: str) -> tuple[list[dict], bool]:
    try:
        tree = gh_get(f"repos/{full_name}/git/trees/{branch}?recursive=1")
    except NotFound:  # 空仓库
        return [], False
    return tree.get("tree", []), bool(tree.get("truncated"))
