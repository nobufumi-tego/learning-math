#!/usr/bin/env bash
# leaning-math: Jupyter Lab ワンショット起動スクリプト (Mac / Linux)
#
# 使い方:
#   ./start.sh
#
# 動作:
#   1. uv が未インストールなら公式インストーラを実行
#   2. 依存関係を sync (.venv が無ければ作成、ある場合は最新化)
#   3. Jupyter Lab を起動 (lab.py 経由でブラウザが自動オープン)
#
# 停止方法:
#   Jupyter Lab が動いているターミナルで Ctrl+C を 2 回押す
#
# トラブルシューティング:
#   - "Permission denied" の場合: chmod +x start.sh で実行権限を付与
#   - uv インストール後に command not found: 一度ターミナルを開き直す

set -euo pipefail

# スクリプト自身があるディレクトリに移動 (どこから呼ばれても動くように)
cd "$(dirname "$0")"

echo "════════════════════════════════════════════════════════"
echo "  📚 leaning-math — Jupyter Lab 起動スクリプト (Mac/Linux)"
echo "════════════════════════════════════════════════════════"
echo ""

# 1. uv 確認・インストール
if ! command -v uv >/dev/null 2>&1; then
    echo "🔧 uv が見つかりません。公式インストーラを実行します..."
    echo "   (https://astral.sh/uv/install.sh)"
    echo ""
    curl -LsSf https://astral.sh/uv/install.sh | sh
    # 現在のシェルセッションに PATH を反映 (新規ターミナルでは自動で通る)
    export PATH="$HOME/.local/bin:$HOME/.cargo/bin:$PATH"
    echo ""
    if ! command -v uv >/dev/null 2>&1; then
        echo "❌ uv のインストール後も command が見つかりません。"
        echo "   一度ターミナルを閉じて開き直してから ./start.sh を再実行してください。"
        exit 1
    fi
    echo "✅ uv をインストールしました ($(uv --version))"
    echo ""
else
    echo "✅ uv 検出済み ($(uv --version))"
    echo ""
fi

# 2. 依存関係を sync
echo "📦 依存関係を確認・更新します... (初回は数分かかります)"
uv sync
echo ""

# 3. Jupyter Lab 起動
echo "🚀 Jupyter Lab を起動します。ブラウザが自動で開きます。"
echo "   📛 停止するには、このターミナルで Ctrl+C を 2 回押してください。"
echo ""
exec uv run lab.py
