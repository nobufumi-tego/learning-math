@echo off
REM ====================================================================
REM   leaning-math: Jupyter Lab one-shot launcher (Windows)
REM ====================================================================
REM
REM Usage:
REM   - Double-click this file in Explorer (recommended, easiest)
REM   - Or from cmd / PowerShell:  start.bat
REM
REM This batch internally calls start.ps1 with these flags:
REM   -NoProfile             : skip user PowerShell profile (faster, no side effects)
REM   -ExecutionPolicy Bypass: ignore PowerShell ExecutionPolicy (no system change)
REM
REM Effect:
REM   * No admin privileges required
REM   * Does NOT modify your system PowerShell ExecutionPolicy
REM   * Works on stock Windows 10 / 11
REM
REM Behavior (same as start.ps1):
REM   1. If uv is not installed, run the official installer (user scope)
REM   2. Sync dependencies (.venv create or update)
REM   3. Launch Jupyter Lab (browser opens automatically)
REM
REM How to stop Jupyter Lab:
REM   Press Ctrl+C twice in the window where it is running.
REM ====================================================================

REM --- IMPORTANT ---------------------------------------------------------
REM This .bat file is intentionally written in pure ASCII (English only).
REM .bat files are parsed by CMD using the system codepage (e.g. CP932 on
REM Japanese Windows), so non-ASCII characters here would break parsing.
REM Japanese explanations live in README.md / DISCLAIMER.md / start.ps1.
REM ----------------------------------------------------------------------

REM Switch CMD codepage to UTF-8 so PowerShell's Japanese output (from
REM start.ps1) renders correctly in this window.
chcp 65001 >nul

REM Move to the folder containing this batch file (works no matter where called from)
cd /d "%~dp0"

REM Hand off to PowerShell
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0start.ps1"

REM Keep the window open after Jupyter Lab exits so the user can read messages
echo.
echo ====================================================================
echo  Jupyter Lab finished. Press any key to close this window.
echo ====================================================================
pause >nul
