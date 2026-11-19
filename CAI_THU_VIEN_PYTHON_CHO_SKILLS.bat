@echo off
chcp 65001 >nul
title Cai Thu Vien Python Cho Tomi Antigravity Subagent (14 Teams)
echo ==============================================================================
echo   CAI DAT THU VIEN PYTHON CHO ANTIGRAVITY 14 TEAMS (51 SUBAGENTS)
echo ==============================================================================
echo.

where python >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo [LOI] Khong tim thay lenh 'python' trong PATH!
    echo Hay cai Python 3.11 - 3.13 tu https://www.python.org/downloads/
    echo va NHO TICH O "Add python.exe to PATH" khi cai dat!
    pause
    exit /b 1
)

python --version
echo.
echo [1/3] Cap nhat pip...
python -m pip install --upgrade pip

echo.
echo [2/3] Cai dat thu vien tu requirements.txt (Core + Data + VPS + SQL + YouTube)...
python -m pip install -r "%~dp0requirements.txt"

echo.
echo [3/3] Kiem tra & dung lai chi muc FTS5 + Hooks (neu da chay CAI_DAT_1_CLICK_WINDOWS.bat)...
if exist "%USERPROFILE%\.gemini\config\scripts\setup_portable_antigravity.py" (
    python "%USERPROFILE%\.gemini\config\scripts\setup_portable_antigravity.py"
)

echo.
echo ==============================================================================
echo [HOAN TAT] Da cai xong thu vien Python!
echo Xem chi tiet phan mem tuy chon (Node.js, FFmpeg, ODBC 17...) trong:
echo   HUONG_DAN_CAI_DAT_MAY_MOI.md
echo ==============================================================================
pause
