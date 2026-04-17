@echo off
REM CryptXT - Installation Script
REM For Windows

echo CryptXT Installation Starting...
echo.

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python not found!
    echo Please install Python 3.7 or higher: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo OK: Python found
python --version
echo.

REM Check pip
pip --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: pip not found!
    echo Please install pip
    pause
    exit /b 1
)

echo OK: pip found
echo.

REM Install required packages
echo Installing required packages...
pip install -r requirements.txt

if errorlevel 1 (
    echo.
    echo ERROR: Installation failed!
    pause
    exit /b 1
)

echo.
echo SUCCESS: Installation completed successfully!
echo.
echo To start the application:
echo    python cryptxt.py
echo.
pause
