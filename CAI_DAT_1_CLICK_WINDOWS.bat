@echo off
chcp 65001 >nul
title Cai Dat 1-Click — Tomi Antigravity Subagent v2.1 (14 Teams / 51 Subagents)
echo ==============================================================================
echo   CAI DAT 1-CLICK: TOMI ANTIGRAVITY SUBAGENT v2.1 (14 TEAMS / 51 SUBAGENTS)
echo   [14 Team Plugins + 41 Global Skills + 4 Workflows + Team Memory + 2 Hooks]
echo ==============================================================================
echo.

if not exist "%USERPROFILE%\.gemini\config\skills" mkdir "%USERPROFILE%\.gemini\config\skills"
if not exist "%USERPROFILE%\.gemini\config\plugins" mkdir "%USERPROFILE%\.gemini\config\plugins"
if not exist "%USERPROFILE%\.gemini\config\scripts" mkdir "%USERPROFILE%\.gemini\config\scripts"
if not exist "%USERPROFILE%\.gemini\config\rules" mkdir "%USERPROFILE%\.gemini\config\rules"
if not exist "%USERPROFILE%\.gemini\config\tools" mkdir "%USERPROFILE%\.gemini\config\tools"
if not exist "%USERPROFILE%\.gemini\config\workflows" mkdir "%USERPROFILE%\.gemini\config\workflows"
if not exist "%USERPROFILE%\.gemini\config\team_memory" mkdir "%USERPROFILE%\.gemini\config\team_memory"
if not exist "%USERPROFILE%\.gemini\config\docs" mkdir "%USERPROFILE%\.gemini\config\docs"

echo [1/6] Sao chep Luat Toan Cuc (GEMINI.md, 5 Chot Chan, rules/, docs/, learned_patterns.md)...
copy /Y "%~dp0config\GEMINI.md" "%USERPROFILE%\.gemini\config\GEMINI.md" >nul
copy /Y "%~dp0config\QUY_TRINH_CHUNG_5_CHOT_CHAN_CHONG_AO_GIAC_AI.md" "%USERPROFILE%\.gemini\config\QUY_TRINH_CHUNG_5_CHOT_CHAN_CHONG_AO_GIAC_AI.md" >nul
if exist "%~dp0config\learned_patterns.md" copy /Y "%~dp0config\learned_patterns.md" "%USERPROFILE%\.gemini\config\learned_patterns.md" >nul
if exist "%~dp0config\rules" xcopy /E /I /H /Y "%~dp0config\rules\*" "%USERPROFILE%\.gemini\config\rules\" >nul
if exist "%~dp0config\docs" xcopy /E /I /H /Y "%~dp0config\docs\*" "%USERPROFILE%\.gemini\config\docs\" >nul

echo [2/6] Sao chep Bo Nao Lai Javis Engine, 2 Hooks, CLI & 4 Workflows...
xcopy /E /I /H /Y "%~dp0config\scripts\*" "%USERPROFILE%\.gemini\config\scripts\" >nul
if exist "%~dp0config\tools" xcopy /E /I /H /Y "%~dp0config\tools\*" "%USERPROFILE%\.gemini\config\tools\" >nul
if exist "%~dp0config\workflows" xcopy /E /I /H /Y "%~dp0config\workflows\*" "%USERPROFILE%\.gemini\config\workflows\" >nul

echo [3/6] Khoi tao Kho Bo Nho 14 Team (team_memory/) - khong ghi de du lieu da co...
if exist "%~dp0config\team_memory" xcopy /E /I /H /D /Y "%~dp0config\team_memory\*" "%USERPROFILE%\.gemini\config\team_memory\" >nul

echo [4/6] Sao chep Tron Bo 41 Global Skills vao %USERPROFILE%\.gemini\config\skills\...
xcopy /E /I /H /Y "%~dp0config\skills\*" "%USERPROFILE%\.gemini\config\skills\" >nul

echo [5/6] Sao chep Tron Bo 14 Team Plugins (51 Subagents) + Plugins chuan...
if exist "%~dp0config\plugins" xcopy /E /I /H /Y "%~dp0config\plugins\*" "%USERPROFILE%\.gemini\config\plugins\" >nul

REM Don dep file GEMINI.md trung lap o thu muc cha de tranh xung dot luat
if exist "%USERPROFILE%\.gemini\GEMINI.md" del /F /Q "%USERPROFILE%\.gemini\GEMINI.md"
if exist "%USERPROFILE%\.gemini\antigravity\GEMINI.md" del /F /Q "%USERPROFILE%\.gemini\antigravity\GEMINI.md"

echo [6/6] Dang ky MCP Server (agy-skill-hub), PreInvocation + SessionStart Hooks ^& Dung FTS5...
where python >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    python "%USERPROFILE%\.gemini\config\scripts\setup_portable_antigravity.py"
) else (
    echo [LUU Y] Chua tim thay lenh python trong PATH.
    echo Hay cai Python 3.11-3.13 (tich Add to PATH) roi chay CAI_THU_VIEN_PYTHON_CHO_SKILLS.bat!
)

echo.
echo ==============================================================================
echo [HOAN TAT 100%%] Tomi Antigravity Subagent v2.1: 14 Teams (51 Subagents)
echo Vi tri cai dat : %USERPROFILE%\.gemini\config\
echo Buoc tiep theo :
echo   1. Chay CAI_THU_VIEN_PYTHON_CHO_SKILLS.bat (neu may moi chua cai thu vien Python)
echo   2. Mo lai Google Antigravity App -> Bat/Tat cac Team trong Customizations
echo   3. Xem huong dan day du tai: README.md va HUONG_DAN_CAI_DAT_MAY_MOI.md
echo ==============================================================================
pause
