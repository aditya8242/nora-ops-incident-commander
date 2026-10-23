@echo off
title Nora-Ops Project Cleaner & Teardown
echo ================================================================
echo           Nora-Ops: Clean Uninstall & Teardown Utility          
echo ================================================================
echo.
echo WARNING: This will permanently delete the project folder:
echo C:\Users\Aditya\.gemini\antigravity\scratch\incident-commander-nora
echo and remove the helper shortcuts from your Desktop.
echo.
set /p CONFIRM="Are you sure you want to completely remove this project? (Y/N): "
if /i "%CONFIRM%" NEQ "Y" (
    echo Teardown cancelled.
    pause
    exit /b
)

echo.
echo [1/3] Removing Desktop shortcuts...
if exist "C:\Users\Aditya\Desktop\Edit-Napster-Key.bat" del /f /q "C:\Users\Aditya\Desktop\Edit-Napster-Key.bat"
if exist "C:\Users\Aditya\Desktop\Launch-Nora-WarRoom.bat" del /f /q "C:\Users\Aditya\Desktop\Launch-Nora-WarRoom.bat"

echo [2/3] Cleaning project directory...
cd /d "C:\Users\Aditya"
rmdir /s /q "C:\Users\Aditya\.gemini\antigravity\scratch\incident-commander-nora"

echo [3/3] Teardown complete! No project files remain.
echo.
set /p UNINSTALL_NODE="Do you also want to uninstall Node.js from your system? (Y/N): "
if /i "%UNINSTALL_NODE%"=="Y" (
    echo Uninstalling Node.js via winget...
    winget uninstall OpenJS.NodeJS.LTS --silent
    echo Node.js uninstalled.
)

echo.
echo Your system is clean.
pause
