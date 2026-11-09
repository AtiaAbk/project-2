@echo off
title Coaching Center Student Result Management System
echo ======================================================================
echo Launching Coaching Center Student Result Management System...
echo ======================================================================

REM Check if local virtualenv exists
if exist ".venv\Scripts\python.exe" (
    ".venv\Scripts\python.exe" main.py
) else (
    python main.py
)

pause

