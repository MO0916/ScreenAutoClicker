@echo off
echo 🐍 Python 自动安装辅助脚本
echo ============================
echo.
echo 📋 请先手动下载 Python 安装程序：
echo 1. 打开浏览器访问: https://python.org/downloads/
echo 2. 下载 Windows Installer (64-bit)
echo 3. 运行下载的安装程序
echo 4. 务必勾选 "Add python.exe to PATH"
echo 5. 点击 "Install Now"
echo.
echo 🚀 安装完成后，请重新打开命令提示符
echo 📝 然后运行以下命令验证安装：
echo.
echo python --version
echo pip --version
echo.
echo 📦 然后安装项目依赖：
echo pip install opencv-python pyautogui numpy pyinstaller
echo.
echo 🏗️ 最后构建 EXE 文件：
echo pyinstaller --onefile --console screen_autoclicker.py
echo.
echo 📁 EXE 文件将生成在 dist\\ 目录中
echo.
pause