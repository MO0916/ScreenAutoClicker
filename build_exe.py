#!/usr/bin/env python3
"""
Windows屏幕自动化工具EXE构建脚本
此脚本帮助在Windows系统上构建可执行文件
"""

import os
import sys
import subprocess
from pathlib import Path

def check_windows():
    """检查是否在Windows系统上"""
    if sys.platform != "win32":
        print("❌ 此脚本需要在Windows系统上运行")
        print("💡 请在Windows电脑上执行以下命令:")
        print("cd Documents\\ScreenAutoClicker")
        print("pip install pyinstaller opencv-python pyautogui numpy")
        print("pyinstaller --onefile --console screen_autoclicker.py")
        return False
    return True

def create_build_script():
    """创建Windows构建脚本"""
    build_script = """@echo off
echo 🛠️ Windows屏幕自动化工具 - EXE构建脚本
echo ========================================

REM 检查Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python未安装或未添加到PATH
    echo 💡 请从 https://python.org 下载安装Python
    pause
    exit /b 1
)

REM 检查必要的包
echo 📦 检查依赖包...
python -c "import cv2, pyautogui, numpy" 2>nul
if errorlevel 1 (
    echo ⚠️ 缺少依赖包，正在安装...
    pip install opencv-python pyautogui numpy
    if errorlevel 1 (
        echo ❌ 依赖包安装失败
        pause
        exit /b 1
    )
    echo ✅ 依赖包安装成功
)

REM 检查PyInstaller
echo 🔧 检查PyInstaller...
python -c "import PyInstaller" 2>nul
if errorlevel 1 (
    echo ⚠️ PyInstaller未安装，正在安装...
    pip install pyinstaller
    if errorlevel 1 (
        echo ❌ PyInstaller安装失败
        pause
        exit /b 1
    )
    echo ✅ PyInstaller安装成功
)

REM 构建EXE文件
echo 🏗️ 开始构建EXE文件...
pyinstaller --onefile --name ScreenAutoClicker --console screen_autoclicker.py

if errorlevel 1 (
    echo ❌ EXE构建失败
    pause
    exit /b 1
)

echo ✅ 构建成功！
echo 📁 EXE文件位置: dist\\ScreenAutoClicker.exe
echo 🚀 使用方法: 双击 dist\\ScreenAutoClicker.exe 运行

pause
"""
    
    with open("build_windows.bat", "w", encoding="utf-8") as f:
        f.write(build_script)
    print("✅ 创建Windows构建脚本: build_windows.bat")

def create_requirements():
    """创建 requirements.txt"""
    requirements = """# Windows屏幕自动化工具依赖
opencv-python>=4.5.0
pyautogui>=0.9.0
numpy>=1.21.0
Pillow>=8.0.0

# 构建工具
pyinstaller>=4.0.0
"""
    with open("requirements.txt", "w", encoding="utf-8") as f:
        f.write(requirements)
    print("✅ 更新 requirements.txt")

def main():
    """主函数"""
    print("🛠️ Windows屏幕自动化工具EXE构建准备")
    print("=" * 50)
    
    # 检查操作系统
    if not check_windows():
        return False
    
    # 创建构建文件
    create_build_script()
    create_requirements()
    
    print("\n📋 构建说明:")
    print("1. 将整个 ScreenAutoClicker 文件夹复制到Windows电脑")
    print("2. 双击运行 build_windows.bat")
    print("3. 脚本会自动安装依赖并构建EXE文件")
    print("4. 生成的EXE文件在 dist\\ 目录下")
    print("\n📍 项目位置: ~/文档/ScreenAutoClicker/")
    print("📁 包含文件:")
    print("  ├── screen_autoclicker.py (主程序)")
    print("  ├── build_windows.bat (构建脚本)")
    print("  ├── requirements.txt (依赖列表)")
    print("  └── install.py (安装脚本)")
    
    return True

if __name__ == "__main__":
    success = main()
    if not success:
        sys.exit(1)