@echo off
REM ====================================================================
REM   leaning-math: Jupyter Lab ワンショット起動 (Windows)
REM ====================================================================
REM
REM 使い方:
REM   - エクスプローラからダブルクリック (推奨、最もカンタン)
REM   - またはコマンドプロンプト / PowerShell で:  start.bat
REM
REM このバッチは内部で PowerShell の start.ps1 を以下の条件で呼び出します:
REM   - -NoProfile: ユーザーの PowerShell プロファイルを読み込まない (高速・副作用なし)
REM   - -ExecutionPolicy Bypass: PowerShell の実行ポリシーを無視 (設定変更不要)
REM
REM 効果:
REM   * 管理者権限不要
REM   * PowerShell の ExecutionPolicy を変更しない (システムを汚さない)
REM   * Windows 10 / 11 標準のままで動く
REM
REM 動作内容 (start.ps1 と同じ):
REM   1. uv が未インストールなら公式インストーラを実行 (ユーザー領域へ)
REM   2. 依存関係を sync (.venv 作成または更新)
REM   3. Jupyter Lab を起動 (ブラウザが自動オープン)
REM
REM 停止方法:
REM   Jupyter Lab が動いているウィンドウで Ctrl+C を 2 回押す
REM ====================================================================

cd /d "%~dp0"

powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0start.ps1"

REM Jupyter Lab を停止 (Ctrl+C) した後、ウィンドウがすぐ閉じないように待機
echo.
echo ====================================================================
echo  Jupyter Lab を終了しました。何かキーを押すとウィンドウを閉じます。
echo ====================================================================
pause >nul
