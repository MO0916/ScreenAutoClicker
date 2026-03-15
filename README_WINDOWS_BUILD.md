# Windows屏幕自动化工具 - EXE构建说明

## 📦 项目文件
所有必要文件已准备就绪，位于: `~/文档/ScreenAutoClicker/`

## 🚀 快速开始

### 方法一：自动构建（推荐）
1. 将整个 `ScreenAutoClicker` 文件夹复制到Windows电脑
2. 双击运行 `windows_build_package.bat`
3. 脚本会自动安装依赖并构建EXE文件
4. 生成的EXE文件在 `dist\ScreenAutoClicker.exe`

### 方法二：手动构建
```cmd
cd Documents\ScreenAutoClicker
pip install opencv-python pyautogui numpy pyinstaller
pyinstaller --onefile --console screen_autoclicker.py
```

## 📁 文件说明

### 核心文件
- `screen_autoclicker.py` - 主程序 (6121行代码)
- `install.py` - 完整安装脚本
- `requirements.txt` - 依赖列表

### 构建工具
- `windows_build_package.bat` - Windows自动构建脚本
- `build_exe.py` - 构建说明脚本

## 🔧 功能特性
- ✅ 图像识别：OpenCV模板匹配算法
- ✅ 屏幕监控：实时截图比较
- ✅ 鼠标自动化：精确定位点击
- ✅ 用户界面：命令行交互控制
- ✅ 状态管理：开始/停止开关

## 🎯 使用说明

### 1. 构建EXE后
```cmd
# 运行生成的EXE
dist\ScreenAutoClicker.exe

# 或者直接运行Python脚本
python screen_autoclicker.py
```

### 2. 程序功能
1. 选择模板图像（截图文件）
2. 设置置信度阈值（0.1-1.0）
3. 设置点击间隔时间
4. 开始监控，程序会自动识别并点击
5. 目标消失后自动停止点击

## ⚠️ 注意事项

### 系统要求
- Windows 10/11 操作系统
- Python 3.7+ 已安装并添加到PATH
- 管理员权限（用于屏幕捕获）

### 依赖说明
构建需要以下Python包：
- `opencv-python` - 图像识别
- `pyautogui` - 屏幕捕获和鼠标控制
- `numpy` - 数值计算
- `pyinstaller` - EXE打包工具

## 📊 项目状态
✅ 开发完成 - 所有功能已实现  
✅ 代码测试 - 核心功能已验证  
✅ 文档完整 - 使用说明齐全  
🚀 等待构建 - 需要在Windows上生成EXE

## 🔄 替代方案
如果无法构建EXE，也可以：

### 直接运行Python脚本
```cmd
pip install opencv-python pyautogui numpy
python screen_autoclicker.py
```

### 使用安装脚本
```cmd
python install.py
```

## 📞 技术支持
如果遇到构建问题：
1. 确保Python已正确安装
2. 检查网络连接（依赖下载）
3. 以管理员身份运行命令提示符
4. 查看错误信息并搜索解决方案

---

**项目已完全开发完成，只需在Windows环境下执行构建即可获得EXE文件！** 🎉