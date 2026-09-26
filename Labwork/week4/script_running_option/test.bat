@echo off
REM ================================================================================
REM Robot Framework Automated Test Runner Script
REM Executes Robot test suites and outputs reports into results/ directory.
REM ================================================================================

echo [LOG] Initializing Robot Framework Test Execution Environment...

set REPO_ROOT=%~dp0..\..\..\..
set VENV_PYTHON=%REPO_ROOT%\.venv\Scripts\python.exe

echo [LOG] Virtual Environment Python: %VENV_PYTHON%

%VENV_PYTHON% -m robot --outputdir "%~dp0results" --loglevel INFO "%~dp0..\Introduction\intro_test.robot"

if %ERRORLEVEL% EQU 0 (
    echo [SUCCESS] All Robot Framework test cases passed successfully!
) else (
    echo [WARNING] Some Robot Framework test cases failed. Inspect results log.
)

echo [LOG] Reports generated in %~dp0results directory.