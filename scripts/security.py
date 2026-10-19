"""收录前的安全检查：不调模型，只看仓库里有哪些文件、脚本里写了什么。

本文件来自共用代码 kit（见 scripts/KIT），各清单内容一样。

查五样：
1. 二进制和压缩包：exe、dmg、msi、apk、jar、bat、zip、7z 这类，正常的 skill 只是几份文本文件
2. 安装钩子：package.json 的 preinstall / install / postinstall / prepare，setup.py 自定义安装命令
3. 远程执行：curl/wget 下载后直接交给 sh、bash、python 执行，PowerShell 的 iwr | iex，解码 base64 后执行
4. 读敏感文件：SSH 密钥、云服务凭据、钥匙串、钱包和助记词、浏览器 cookie 和登录态
5. 联网地址：脚本里出现的域名，只列出来，不算问题

结论两档：「通过」是什么都没查到；「要看」是查到了上面 1–4 里的东西，要人看过再决定收不收。
查不到不等于安全：这是筛子，不是代码审计。

用法：
  python3 scripts/security.py owner/repo [owner/repo ...]   # 查指定仓库
  python3 scripts/security.py --all --out security.md        # 查 skills.toml 里所有仓库，写成报告
  python3 scripts/security.py --json owner/repo              # 输出 JSON
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from concurrent.futures import ThreadPoolExecutor

from lib import NotFound, gh_get, load_valid, raw_text, repo_tree, skill_dirs

INSTALLERS = {".exe", ".msi", ".dmg", ".pkg", ".apk", ".scr", ".vbs", ".bat", ".cmd", ".jar", ".com", ".app"}
BINARIES = {".dll", ".so", ".dylib", ".bin", ".node", ".wasm"}
ARCHIVES = {".zip", ".7z", ".rar", ".tar", ".gz", ".tgz", ".xz", ".bz2"}
SCRIPTS = {".sh", ".bash", ".zsh", ".ps1", ".py", ".js", ".mjs", ".cjs", ".ts", ".rb", ".pl"}
MAX_SKILL_MD = 12
MAX_SCRIPTS = 25

REMOTE_EXEC = re.compile(
    r"(curl|wget)\b[^\n|;]*\|\s*(sudo\s+)?(ba|z)?sh\b"
    r"|(curl|wget)\b[^\n|;]*\|\s*(sudo\s+)?python3?\b"
    r"|\b(bash|sh|zsh)\s+<\(\s*(curl|wget)"
    r"|\b(sh|bash)\s+-c\s+[\"']\$\((curl|wget)"
    r"|\b(iwr|irm|invoke-webrequest|invoke-restmethod)\b[^\n|]*\|\s*iex\b"
    r"|powershell[^\n]*\s-e(nc|ncodedcommand)?\s+[A-Za-z0-9+/=]{20,}"
    r"|base64\s+(-d|--decode)[^\n|]*\|\s*(ba|z)?sh\b"
    r"|eval\s*\(\s*atob\s*\("
    r"|exec\s*\(\s*(base64\.b64decode|codecs\.decode|bytes\.fromhex)",
    re.I,
)
SENSITIVE = [
    ("SSH 密钥", re.compile(r"~/\.ssh\b|\bid_(rsa|ed25519|ecdsa)\b", re.I)),
    ("云服务凭据", re.compile(r"\.aws/credentials|\.config/gcloud|\.azure/", re.I)),
    ("钥匙串", re.compile(r"security\s+find-(generic|internet)-password|\bkeychain\b", re.I)),
    ("钱包和助记词", re.compile(r"\bseed phrase\b|助记词|\bmnemonic\b|wallet\.dat|metamask", re.I)),
    ("浏览器 cookie 和登录态", re.compile(r"cookies?\.(sqlite|db)\b|\bLogin Data\b|Local State|browser_cookie3|"
                                  r"document\.cookie|cookie_?str|\bcookies?\b\s*[=:]", re.I)),
]
URL = re.compile(r"https?://([A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+)")
COMMON_HOSTS = re.compile(r"(^|\.)(github\.com|githubusercontent\.com|githubassets\.com|npmjs\.(com|org)|pypi\.org|"
                          r"python\.org|nodejs\.org|w3\.org|schema\.org|example\.(com|org)|localhost)$", re.I)


def ext(path: str) -> str:
    name = path.rsplit("/", 1)[-1].lower()
    return "." + name.rsplit(".", 1)[-1] if "." in name else ""


def check(repo: str) -> dict:
    info = gh_get(f"repos/{repo}")
    full, branch = info["full_name"], info["default_branch"]
    tree, truncated = repo_tree(full, branch)
    blobs = [t["path"] for t in tree if t["type"] == "blob"]
    flags: list[dict] = []

    for p in blobs:
        e = ext(p)
        if e in INSTALLERS:
            flags.append({"kind": "二进制", "path": p, "detail": "安装包或可执行文件"})
        elif e in BINARIES:
            flags.append({"kind": "二进制", "path": p, "detail": "二进制库"})
        elif e in ARCHIVES:
            flags.append({"kind": "压缩包", "path": p, "detail": "压缩包里的内容看不到"})

    skill_mds = [p for p in blobs if p.rsplit("/", 1)[-1].lower() == "skill.md"][:MAX_SKILL_MD]
    scripts = [p for p in blobs if ext(p) in SCRIPTS and "/node_modules/" not in f"/{p}"][:MAX_SCRIPTS]
    packages = [p for p in blobs if p.rsplit("/", 1)[-1] in ("package.json", "setup.py")][:5]
    targets = skill_mds + scripts + packages
    with ThreadPoolExecutor(max_workers=8) as pool:
        texts = dict(zip(targets, pool.map(lambda p: raw_text(full, branch, p), targets)))

    domains: set[str] = set()
    for p, text in texts.items():
        if text is None:
            continue
        name = p.rsplit("/", 1)[-1]
        if name == "package.json":
            try:
                hooks = {k: v for k, v in json.loads(text).get("scripts", {}).items()
                         if k in ("preinstall", "install", "postinstall", "prepare")}
            except (ValueError, AttributeError):
                hooks = {}
            for k, v in hooks.items():
                flags.append({"kind": "安装钩子", "path": p, "detail": f"{k}: {str(v)[:120]}"})
            continue
        if name == "setup.py" and re.search(r"cmdclass\s*=", text):
            flags.append({"kind": "安装钩子", "path": p, "detail": "setup.py 自定义了安装命令"})
        for m in REMOTE_EXEC.finditer(text):
            flags.append({"kind": "远程执行", "path": p, "detail": " ".join(m.group(0).split())[:160]})
        for label, rx in SENSITIVE:
            m = rx.search(text)
            if m:
                flags.append({"kind": "读敏感文件", "path": p, "detail": f"{label}：{' '.join(m.group(0).split())[:80]}"})
        if p not in skill_mds:
            domains |= {d.lower() for d in URL.findall(text) if not COMMON_HOSTS.search(d)}

    return {
        "repo": full,
        "level": "要看" if flags else "通过",
        "files": len(blobs),
        "skills": len(skill_dirs(tree)),
        "truncated": truncated,
        "checked_files": sum(t is not None for t in texts.values()),
        "flags": flags,
        "domains": sorted(domains),
    }


def summary(r: dict) -> str:
    if "error" in r:
        return r["error"]
    kinds: dict[str, list[str]] = {}
    for f in r["flags"]:
        kinds.setdefault(f["kind"], []).append(f"`{f['path']}` {f['detail']}".strip())
    parts = [f"**{k}**（{len(v)}）：" + "；".join(v[:3]) + ("……" if len(v) > 3 else "") for k, v in kinds.items()]
    if r["domains"]:
        parts.append("联网：" + "、".join(r["domains"][:8]) + ("……" if len(r["domains"]) > 8 else ""))
    return "<br>".join(parts) or "—"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("repos", nargs="*", metavar="OWNER/REPO")
    ap.add_argument("--all", action="store_true", help="查 skills.toml 里的所有仓库")
    ap.add_argument("--json", action="store_true", help="输出 JSON")
    ap.add_argument("--out", help="写入文件，默认打印到终端")
    args = ap.parse_args()

    repos = list(args.repos)
    if args.all:
        repos += [s["repo"] for s in load_valid()[1]]
    if not repos:
        ap.error("给出仓库名，或者加 --all")

    results = []
    for repo in repos:
        try:
            r = check(repo)
        except NotFound:
            r = {"repo": repo, "level": "失效", "error": "仓库不存在（404）"}
        results.append(r)
        print(f"  {r['level']}  {repo}  {len(r.get('flags', []))} 处", file=sys.stderr)

    if args.json:
        text = json.dumps(results, ensure_ascii=False, indent=1) + "\n"
    else:
        flagged = [r for r in results if r["level"] != "通过"]
        lines = [f"# 安全检查（{len(results)} 个仓库，{len(flagged)} 个要看）", "",
                 "查的是二进制和压缩包、安装钩子、远程执行、读敏感文件，并列出脚本里的联网地址。查不到不等于安全。", "",
                 "| 仓库 | 结论 | 发现 |", "|---|---|---|"]
        lines += [f"| [{r['repo']}](https://github.com/{r['repo']}) | {r['level']} | {summary(r)} |" for r in flagged]
        text = "\n".join(lines) + "\n"
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"已写入 {args.out}", file=sys.stderr)
    else:
        print(text)


if __name__ == "__main__":
    main()
