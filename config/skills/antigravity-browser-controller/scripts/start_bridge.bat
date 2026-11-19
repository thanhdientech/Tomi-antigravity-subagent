@echo off
chcp 65001 >nul
title Antigravity Omni-Browser Bridge Server
echo ================================================================
echo ⚡ ĐANG KHỞI ĐỘNG ANTIGRAVITY OMNI-BROWSER BRIDGE SERVER...
echo ================================================================
cd /d "%~dp0"
if exist "%LOCALAPPDATA%\Programs\Python\Python313\python.exe" (
    "%LOCALAPPDATA%\Programs\Python\Python313\python.exe" server.py
) else (
    python server.py
)
pause
