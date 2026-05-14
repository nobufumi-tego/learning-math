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
echo "📦 依存関係を確認・更新します..."
echo "   ⏰ 初回は 3〜10 分かかります (NumPy・JAX・JupyterLab 等を合計 500MB〜1GB ダウンロード)"
echo "   ☕ コーヒーを淹れる時間です。途中で Ctrl+C せず最後まで待ってください。"
echo "   📊 進捗: 'Resolved'/'Downloading'/'Installed' が表示されていれば作業中"
echo ""
uv sync
echo ""
echo "✅ 依存関係の準備が完了しました"
echo ""

# 3. Jupyter Lab 起動
echo "🚀 Jupyter Lab を起動します..."
echo "   ⏰ 初回起動は 10〜30 秒かかります。ブラウザが自動で開いたら準備完了です。"
echo "   📛 停止するには、このターミナルで Ctrl+C を 2 回押してください。"
echo ""
exec uv run lab.py
