@echo off
REM Ensure the script is run with UTF-8 encoding

REM Set the Python environment to UTF-8 mode
set PYTHONIOENCODING=utf-8

REM Optionally navigate to the directory containing main.py
cd /d "%~dp0"

REM Run the Python script minimized (hidden)
start /min python main.py

REM Optional: exit the batch script
exit
