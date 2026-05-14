# leaning-math: Jupyter Lab ワンショット起動スクリプト (Windows / PowerShell)
#
# ⭐ 初心者の方へ: より簡単な方法があります
#   エクスプローラから start.bat をダブルクリックするだけで起動できます。
#   PowerShell を開く必要も、実行ポリシーを変更する必要もありません。
#
# 使い方 (PowerShell から直接):
#   .\start.ps1
#
# 初回実行時に「このシステムではスクリプトの実行が無効になっている」
# と出る場合、以下のいずれかを実行してください:
#
#   方法 A (推奨): 一旦終了して、エクスプローラで start.bat をダブルクリック
#
#   方法 B (このセッションのみ): 起動コマンドを以下に変更
#     powershell -ExecutionPolicy Bypass -File .\start.ps1
#
#   方法 C (今後ずっと有効): PowerShell を 1 回開いて
#     Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
#
# 動作:
#   1. uv が未インストールなら公式インストーラを実行
#   2. 依存関係を sync (.venv が無ければ作成、ある場合は最新化)
#   3. Jupyter Lab を起動 (lab.py 経由でブラウザが自動オープン)
#
# 停止方法:
#   Jupyter Lab が動いているウィンドウで Ctrl+C を 2 回押す

$ErrorActionPreference = "Stop"

# 日本語出力が文字化けしないよう、コンソールの入出力エンコーディングを UTF-8 に固定
# (Windows 10/11 の PowerShell 5.1 / 7 両方で有効)
try {
    [Console]::OutputEncoding = [System.Text.Encoding]::UTF8
    [Console]::InputEncoding  = [System.Text.Encoding]::UTF8
    $OutputEncoding           = [System.Text.Encoding]::UTF8
} catch { }

# スクリプト自身があるフォルダに移動 (どこから呼ばれても動くように)
Set-Location -Path $PSScriptRoot

Write-Host "════════════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host "  📚 leaning-math — Jupyter Lab 起動スクリプト (Windows)" -ForegroundColor Cyan
Write-Host "════════════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host ""

# 1. uv 確認・インストール
if (-not (Get-Command uv -ErrorAction SilentlyContinue)) {
    Write-Host "🔧 uv が見つかりません。公式インストーラを実行します..." -ForegroundColor Yellow
    Write-Host "   (https://astral.sh/uv/install.ps1)"
    Write-Host ""
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    # 現在のセッションに PATH を反映 (新規ターミナルでは自動で通る)
    $env:PATH = "$env:USERPROFILE\.local\bin;$env:USERPROFILE\.cargo\bin;$env:PATH"
    Write-Host ""
    if (-not (Get-Command uv -ErrorAction SilentlyContinue)) {
        Write-Host "❌ uv のインストール後も command が見つかりません。" -ForegroundColor Red
        Write-Host "   一度 PowerShell を閉じて開き直してから .\start.ps1 を再実行してください。" -ForegroundColor Red
        exit 1
    }
    Write-Host "✅ uv をインストールしました ($(uv --version))" -ForegroundColor Green
    Write-Host ""
} else {
    Write-Host "✅ uv 検出済み ($(uv --version))" -ForegroundColor Green
    Write-Host ""
}

# 2. 依存関係を sync
Write-Host "📦 依存関係を確認・更新します... (初回は数分かかります)" -ForegroundColor Cyan
uv sync
Write-Host ""

# 3. Jupyter Lab 起動
Write-Host "🚀 Jupyter Lab を起動します。ブラウザが自動で開きます。" -ForegroundColor Green
Write-Host "   📛 停止するには、このウィンドウで Ctrl+C を 2 回押してください。" -ForegroundColor Green
Write-Host ""
uv run lab.py
