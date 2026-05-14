"""git コミット履歴から CHANGELOG.md を生成する.

このスクリプトは GitHub Actions (`.github/workflows/changelog.yml`) から
push 毎に自動実行される。手元で確認したい場合は:

    uv run python scripts/generate_changelog.py

CHANGELOG.md は **手動編集禁止** (auto-overwrite される)。
履歴を変えたい場合は、対応する commit message を rebase で書き換えること。
"""
from __future__ import annotations

import subprocess
from collections import defaultdict
from pathlib import Path

# Conventional Commit prefix と表示ラベルの対応
CATEGORY_ORDER: list[str] = [
    "feat",
    "fix",
    "perf",
    "refactor",
    "docs",
    "test",
    "style",
    "build",
    "ci",
    "chore",
    "other",
]

CATEGORY_LABELS: dict[str, str] = {
    "feat": "✨ 新機能・新規追加",
    "fix": "🐛 バグ修正",
    "perf": "⚡ パフォーマンス",
    "refactor": "♻️ リファクタリング",
    "docs": "📝 ドキュメント",
    "test": "✅ テスト",
    "style": "🎨 スタイル",
    "build": "📦 ビルド",
    "ci": "🤖 CI/CD",
    "chore": "🔧 その他の整備",
    "other": "📌 その他",
}

# CHANGELOG への記載をスキップするコミット (自動コミット自身、マージ等)
SKIP_SUBJECT_PATTERNS: tuple[str, ...] = (
    "chore(changelog): auto-update",
    "Merge ",
    "Merge branch ",
    "Merge pull request ",
)


def get_git_log() -> list[tuple[str, str, str]]:
    """git log を取得して (短縮ハッシュ, 日付 YYYY-MM-DD, subject) のリストを返す."""
    result = subprocess.run(
        [
            "git",
            "log",
            "--reverse",
            "--no-merges",
            "--pretty=format:%h\x1f%ad\x1f%s",
            "--date=short",
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    commits: list[tuple[str, str, str]] = []
    for line in result.stdout.split("\n"):
        if not line.strip():
            continue
        parts = line.split("\x1f", 2)
        if len(parts) != 3:
            continue
        short_hash, date, subject = parts
        if any(subject.startswith(p) or p in subject for p in SKIP_SUBJECT_PATTERNS):
            continue
        commits.append((short_hash, date, subject))
    return commits


def categorize(subject: str) -> str:
    """Conventional Commit の prefix から category を抽出."""
    for cat in CATEGORY_ORDER:
        if cat == "other":
            continue
        # `feat:` `feat(scope):` `feat!:` の何れにも対応
        if subject.startswith(f"{cat}:") or subject.startswith(f"{cat}(") or subject.startswith(f"{cat}!"):
            return cat
    return "other"


def render_markdown(commits: list[tuple[str, str, str]]) -> str:
    """コミット一覧から CHANGELOG.md の本文 (str) を組み立てる."""
    by_date: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for short_hash, date, subject in commits:
        by_date[date].append((short_hash, subject))

    lines: list[str] = [
        "# 📋 更新履歴 (Changelog)",
        "",
        "> ⚙️ **このファイルは自動生成されます**",
        "> ",
        "> [`scripts/generate_changelog.py`](scripts/generate_changelog.py) が "
        "[`.github/workflows/changelog.yml`](.github/workflows/changelog.yml) によって "
        "**`main` への push 毎に自動実行** され、git コミット履歴から再生成されます。",
        "> ",
        "> 手動で編集しないでください (上書きされます)。"
        "コミットメッセージは [Conventional Commits](https://www.conventionalcommits.org/ja/) に準拠することを推奨します。",
        "",
        "---",
        "",
    ]

    for date in sorted(by_date.keys(), reverse=True):
        lines.append(f"## {date}")
        lines.append("")
        cat_buckets: dict[str, list[tuple[str, str]]] = defaultdict(list)
        for short_hash, subject in by_date[date]:
            cat_buckets[categorize(subject)].append((short_hash, subject))
        for cat in CATEGORY_ORDER:
            if cat not in cat_buckets:
                continue
            lines.append(f"### {CATEGORY_LABELS[cat]}")
            lines.append("")
            for short_hash, subject in cat_buckets[cat]:
                # GitHub 上では短縮ハッシュ自動リンクされる
                lines.append(f"- `{short_hash}` {subject}")
            lines.append("")

    lines.append("---")
    lines.append("")
    lines.append(f"_Total commits indexed: **{len(commits)}**_")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    """main エントリポイント."""
    repo_root = Path(__file__).resolve().parent.parent
    commits = get_git_log()
    markdown = render_markdown(commits)
    out_path = repo_root / "CHANGELOG.md"
    out_path.write_text(markdown, encoding="utf-8")
    print(f"✅ CHANGELOG.md generated ({len(commits)} commits)")


if __name__ == "__main__":
    main()
