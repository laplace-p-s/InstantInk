@echo off
set FILENAME=sample.txt

if exist %FILENAME% (
    python main.py %FILENAME%
) else (
    echo. > %FILENAME%
    python main.py %FILENAME%
)
