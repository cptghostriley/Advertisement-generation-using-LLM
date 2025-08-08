@echo off
echo 🚀 PromoGen Quick Setup
echo ========================

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python is not installed or not in PATH
    pause
    exit /b 1
)

echo ✅ Python detected

REM Create virtual environment if it doesn't exist
if not exist "venv" (
    echo 📦 Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo 🔄 Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo 📥 Installing dependencies...
pip install -r requirements.txt

REM Setup environment file
if not exist ".env" (
    echo 📝 Creating .env file...
    copy .env.example .env
)

echo ✅ Setup complete!
echo.
echo 🤖 Checking for AI model files...
python check_model.py
echo.
echo Next steps:
echo 1. Download model files if missing (see check_model.py output)
echo 2. Edit .env file with your configuration  
echo 3. Run: python app.py
echo 4. Open http://localhost:5000 in your browser
echo.
pause
