#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Windows屏幕自动化工具安装脚本
"""

import os
import sys
import subprocess
import venv
from pathlib import Path

def create_virtualenv():
    """创建Python虚拟环境"""
    venv_path = Path("venv")
    if not venv_path.exists():
        print("🔧 创建虚拟环境...")
        venv.create(venv_path, with_pip=True)
        print("✅ 虚拟环境创建完成")
    else:
        print("✅ 虚拟环境已存在")
    
    return venv_path

def install_requirements():
    """安装依赖包"""
    print("📦 安装依赖包...")
    
    # 获取虚拟环境的pip路径
    if sys.platform == "win32":
        pip_path = "venv\\Scripts\\pip.exe"
    else:
        pip_path = "venv/bin/pip"
    
    try:
        result = subprocess.run([
            pip_path, "install", "-r", "requirements.txt"
        ], capture_output=True, text=True, timeout=300)
        
        if result.returncode == 0:
            print("✅ 依赖包安装成功")
            print(result.stdout)
        else:
            print("❌ 依赖包安装失败")
            print(result.stderr)
            return False
            
    except subprocess.TimeoutExpired:
        print("❌ 安装超时")
        return False
    except Exception as e:
        print(f"❌ 安装错误: {e}")
        return False
    
    return True

def create_batch_file():
    """创建批处理文件"""
    if sys.platform == "win32":
        batch_content = """@echo off
echo 🖥️ Windows屏幕自动化工具
echo ===========================

REM 检查虚拟环境
if not exist "venv\\Scripts\\python.exe" (
    echo ❌ 虚拟环境不存在，请先运行 install.py
    pause
    exit /b 1
)

REM 启动程序
venv\\Scripts\\python.exe screen_autoclicker.py
pause
"""
        with open("start.bat", "w", encoding="utf-8") as f:
            f.write(batch_content)
        print("✅ 创建启动批处理文件: start.bat")
    
    # 创建Linux/Mac启动脚本
    shell_content = """#!/bin/bash
echo "🖥️ Windows屏幕自动化工具"
echo "==========================="

# 检查虚拟环境
if [ ! -f "venv/bin/python" ]; then
    echo "❌ 虚拟环境不存在，请先运行 install.py"
    exit 1
fi

# 启动程序
venv/bin/python screen_autoclicker.py
"""
    with open("start.sh", "w", encoding="utf-8") as f:
        f.write(shell_content)
    os.chmod("start.sh", 0o755)
    print("✅ 创建启动Shell脚本: start.sh")

def build_executable():
    """构建可执行文件"""
    print("🔨 构建可执行文件...")
    
    # 获取虚拟环境的Python路径
    if sys.platform == "win32":
        python_path = "venv\\Scripts\\python.exe"
    else:
        python_path = "venv/bin/python"
    
    try:
        result = subprocess.run([
            python_path, "-m", "PyInstaller", 
            "--onefile",
            "--name", "ScreenAutoClicker",
            "--add-data", "requirements.txt;.",
            "--console",
            "screen_autoclicker.py"
        ], capture_output=True, text=True, timeout=600)
        
        if result.returncode == 0:
            print("✅ 可执行文件构建成功")
            print("📦 文件位置: dist/ScreenAutoClicker.exe")
            return True
        else:
            print("❌ 构建失败")
            print(result.stderr)
            return False
            
    except subprocess.TimeoutExpired:
        print("❌ 构建超时")
        return False
    except Exception as e:
        print(f"❌ 构建错误: {e}")
        return False

def main():
    """主安装函数"""
    print("=" * 50)
    print("🛠️  Windows屏幕自动化工具安装程序")
    print("=" * 50)
    
    # 检查Python版本
    if sys.version_info < (3, 7):
        print("❌ 需要Python 3.7或更高版本")
        return False
    
    # 创建项目目录
    os.makedirs("logs", exist_ok=True)
    os.makedirs("templates", exist_ok=True)
    
    # 安装步骤
    steps = [
        ("创建虚拟环境", create_virtualenv),
        ("安装依赖包", install_requirements),
        ("创建启动脚本", create_batch_file),
        ("构建可执行文件", build_executable)
    ]
    
    for step_name, step_func in steps:
        print(f"\n📋 {step_name}...")
        if not step_func():
            print(f"❌ {step_name}失败")
            return False
    
    print("\n🎉 安装完成!")
    print("📁 项目结构:")
    print("  ├── screen_autoclicker.py    # 主程序")
    print("  ├── requirements.txt         # 依赖列表")
    print("  ├── venv/                    # 虚拟环境")
    print("  ├── start.bat               # Windows启动脚本")
    print("  ├── start.sh                # Linux/Mac启动脚本")
    print("  └── dist/ScreenAutoClicker.exe  # 可执行文件")
    print("")
    print("🚀 使用方法:")
    print("  1. 双击 start.bat (Windows) 或运行 ./start.sh (Linux/Mac)")
    print("  2. 选择模板图像")
    print("  3. 开始监控")
    print("  4. 程序会自动点击匹配的图像")
    
    return True

if __name__ == "__main__":
    success = main()
    if not success:
        sys.exit(1)