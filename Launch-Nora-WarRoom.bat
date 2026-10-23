@echo off
title Nora-Ops Azure Incident Commander
set "PATH=C:\Program Files\nodejs;%PATH%"
cd /d "%~dp0"

echo ================================================================
echo    Launching Nora-Ops: Azure Incident Commander (War Room)      
echo ================================================================
echo.

python setup_nora.py
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo Provisioning paused. Please set your NAPSTER_API_KEY in .env
    pause
    exit /b %ERRORLEVEL%
)

echo.
echo Starting local token & static server on http://localhost:5173...
start http://localhost:5173
node local-token-server/token-server.js
pause
