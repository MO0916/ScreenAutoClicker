# Python Windows 安装指南

## 🐍 Python 安装步骤

### 方法一：官方安装（推荐）

#### 1. 下载 Python
- 访问官方下载页面：https://python.org/downloads/
- 下载 Windows Installer (64-bit)
- 文件名称类似：`python-3.12.2-amd64.exe`

#### 2. 安装 Python
```
1. 双击下载的安装程序
2. 勾选 "Add python.exe to PATH" （重要！）
3. 点击 "Install Now"
4. 等待安装完成
5. 点击 "Close"
```

#### 3. 验证安装
打开命令提示符（按 Win+R，输入 cmd）：
```cmd
python --version
# 应该显示 Python 3.x.x

pip --version  
# 应该显示 pip 版本信息
```

### 方法二：Microsoft Store 安装

#### 1. 通过应用商店安装
```
1. 打开 Microsoft Store
2. 搜索 "Python"
3. 选择最新的 Python 版本
4. 点击 "获取" 安装
```

#### 2. 验证安装
```cmd
python --version
pip --version
```

### 方法三：一键安装脚本

创建 `install_python.bat`：
```batch
@echo off
echo 🐍 Python 自动安装脚本
echo ========================

REM 下载 Python 安装程序
curl -L -o python_installer.exe https://www.python.org/ftp/python/3.12.2/python-3.12.2-amd64.exe

REM 安装 Python
python_installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0

echo ✅ Python 安装完成
echo 📝 验证安装...
python --version
pip --version

pause
```

## 🔧 环境配置

### 检查 PATH 配置
安装完成后，确保 Python 在系统 PATH 中：
```cmd
echo %PATH% | find "Python"
```

### 如果 PATH 未配置
手动添加 Python 到 PATH：
```
1. 右键点击"此电脑" -> "属性"
2. 点击"高级系统设置" 
3. 点击"环境变量"
4. 在"系统变量"中找到"Path"
5. 点击"编辑"
6. 添加 Python 安装路径（如：C:\Python312\）
7. 添加 Scripts 路径（如：C:\Python312\Scripts\）
```

## 📦 安装项目依赖

Python 安装完成后，安装项目所需依赖：

### 方法一：使用 requirements.txt
```cmd
cd C:\path\to\ScreenAutoClicker
pip install -r requirements.txt
```

### 方法二：手动安装
```cmd
pip install opencv-python pyautogui numpy pyinstaller
```

## 🚀 构建 EXE 文件

依赖安装完成后，构建可执行文件：
```cmd
cd C:\path\to\ScreenAutoClicker
pyinstaller --onefile --console screen_autoclicker.py
```

生成的 EXE 文件在 `dist\` 目录中。

## ❗ 常见问题解决

### 问题1：'python' 不是内部或外部命令
```
原因：Python 未添加到 PATH
解决：重新安装并勾选 "Add to PATH"
```

### 问题2：权限不足
```
解决：以管理员身份运行命令提示符
```

### 问题3：网络问题
```
解决：使用国内镜像源安装
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### 问题4：旧版本冲突
```
解决：卸载旧版本 Python 重新安装
```

## 🌐 下载链接

- **Python 官方下载**: https://python.org/downloads/
- **清华大学镜像**: https://mirrors.tuna.tsinghua.edu.cn/help/pypi/

## 📞 技术支持

如果安装遇到问题：
1. 检查错误信息
2. 确保网络连接正常
3. 以管理员身份运行安装程序
4. 查看 Python 官方文档

安装完成后，您就可以构建和运行屏幕自动化工具了！ 🎯