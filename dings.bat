@echo off
REM Ensure the script is run with UTF-8 encoding

REM Set the Python environment to UTF-8 mode
set PYTHONIOENCODING=utf-8

REM Optionally navigate to the directory containing main.py
cd /d "%~dp0"

REM Run the Python script
python main.py

REM Pause the script to see any output before the window closes (optional)
pause
