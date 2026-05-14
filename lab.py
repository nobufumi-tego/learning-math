"""JupyterLab 起動スクリプト (リポジトリ同梱設定を自動適用).

このリポジトリ専用の JupyterLab 設定 (.jupyter/lab/user-settings/) を読むよう、
環境変数 JUPYTERLAB_SETTINGS_DIR を自動でセットしてから JupyterLab を起動します。

主な効果:
- .md ファイルをダブルクリックすると Markdown Preview モードで開く

使い方:
    uv run lab.py

通常の JupyterLab を起動したい場合 (個人設定で起動) :
    uv run jupyter lab

詳細は .jupyter/README.md を参照。
"""
from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path


def main() -> int:
    """JupyterLab を repo 同梱設定で起動する."""
    repo_root = Path(__file__).parent.resolve()
    settings_dir = repo_root / ".jupyter" / "lab" / "user-settings"

    if not settings_dir.exists():
        print(
            f"⚠️  Settings directory not found: {settings_dir}\n"
            "    リポジトリ同梱設定が見つかりません。通常起動にフォールバックします。",
            file=sys.stderr,
        )
    else:
        print(f"📚 Loading project settings from: {settings_dir}")

    # 環境変数を設定
    env = os.environ.copy()
    env["JUPYTERLAB_SETTINGS_DIR"] = str(settings_dir)

    # JupyterLab を起動 (引数はそのまま渡す)
    print("🚀 Starting JupyterLab...\n")
    cmd = [sys.executable, "-m", "jupyter", "lab", *sys.argv[1:]]
    try:
        result = subprocess.run(cmd, env=env, check=False)
        return result.returncode
    except FileNotFoundError:
        print(
            "❌ JupyterLab がインストールされていません。\n"
            "    まず以下を実行してください:\n"
            "        uv sync",
            file=sys.stderr,
        )
        return 1
    except KeyboardInterrupt:
        print("\n👋 JupyterLab を終了しました。")
        return 0


if __name__ == "__main__":
    sys.exit(main())
