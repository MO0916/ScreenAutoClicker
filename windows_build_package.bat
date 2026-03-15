@echo off
echo 🛠️ Windows屏幕自动化工具 - EXE构建包
echo ========================================

REM 检查Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python未安装或未添加到PATH
    echo 💡 请从 https://python.org 下载安装Python
    pause
    exit /b 1
)

REM 安装必要的依赖
echo 📦 安装依赖包...
pip install opencv-python pyautogui numpy pyinstaller

if errorlevel 1 (
    echo ❌ 依赖包安装失败
    pause
    exit /b 1
)

echo ✅ 依赖包安装成功

REM 构建EXE文件
echo 🏗️ 构建EXE文件...
pyinstaller --onefile --name ScreenAutoClicker --console screen_autoclicker.py

if errorlevel 1 (
    echo ❌ EXE构建失败
    pause
    exit /b 1
)

echo ✅ 构建成功！
echo 📁 EXE文件位置: dist\ScreenAutoClicker.exe
echo 🚀 使用方法: 双击 dist\ScreenAutoClicker.exe 运行

pause