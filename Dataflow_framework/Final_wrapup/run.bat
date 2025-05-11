@echo off
set PYTHONPATH=%~dp0

if "%1"=="run" (
    python -m app.main
) else if "%1"=="run-single" (
    python -m app.main --input watch_dir/unprocessed/sample.txt
) else if "%1"=="run-watch" (
    python -m app.main --watch
) else if "%1"=="api" (
    uvicorn app.api:app --reload
) else (
    echo.
    echo [ USAGE ]
    echo   .\run.bat run
    echo   .\run.bat run-single
    echo   .\run.bat run-watch
    echo   .\run.bat api
)

