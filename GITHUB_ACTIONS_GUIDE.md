# GitHub Actions 自动构建指南

## 🚀 快速开始

### 步骤1: 创建GitHub仓库

1. 访问 https://github.com/new
2. 仓库名称: `ScreenAutoClicker` (或其他名称)
3. 描述: "Windows屏幕自动化工具"
4. 选择 "Public" 或 "Private"
5. 不勾选 "Initialize this repository with README"
6. 点击 "Create repository"

### 步骤2: 上传项目文件

#### 方法A: 使用Git命令行
```bash
# 克隆新建的仓库
git clone https://github.com/你的用户名/ScreenAutoClicker.git
cd ScreenAutoClicker

# 复制所有项目文件到仓库目录
cp -r /vol1/1000/NAS/Project/ScreenAutoClicker/* .

# 提交并推送
git add .
git commit -m "添加屏幕自动化工具项目"
git push origin main
```

#### 方法B: 使用网页上传
1. 在GitHub仓库页面点击 "Add file" → "Upload files"
2. 拖拽所有项目文件到上传区域
3. 点击 "Commit changes"

### 步骤3: 触发自动构建

推送代码后，GitHub Actions会自动触发构建：
1. 进入仓库页面
2. 点击 "Actions" 标签页
3. 查看构建进度
4. 等待构建完成

### 步骤4: 下载EXE文件

构建完成后：
1. 在 "Actions" 页面点击完成的构建任务
2. 在 "Artifacts" 部分下载 `ScreenAutoClicker-Windows-EXE`
3. 解压后获得 `ScreenAutoClicker.exe` 文件

## 📁 项目文件结构

确保仓库包含以下文件：
```
ScreenAutoClicker/
├── .github/workflows/build.yml    # GitHub Actions配置
├── screen_autoclicker.py          # 主程序
├── requirements.txt               # 依赖列表
├── install.py                     # 安装脚本
├── GITHUB_ACTIONS_GUIDE.md        # 本指南
└── README_WINDOWS_BUILD.md        # 构建说明
```

## ⚙️ 构建配置详情

### 构建环境
- **操作系统**: Windows Server 2022
- **Python版本**: 3.12
- **构建工具**: PyInstaller 5.13.2

### 依赖版本
```
opencv-python==4.8.1.78
pyautogui==0.9.54
numpy==1.24.3
pyinstaller==5.13.2
pillow==10.0.1
```

### 构建命令
```bash
pyinstaller --onefile --name ScreenAutoClicker --console screen_autoclicker.py
```

## 🔧 自定义配置

### 修改构建触发器
编辑 `.github/workflows/build.yml`:
```yaml
on:
  push:
    branches: [ main ]
  # 手动触发
  workflow_dispatch:
  # 定时构建  
  schedule:
    - cron: '0 0 * * *'
```

### 修改Python版本
```yaml
- name: Set up Python
  uses: actions/setup-python@v4
  with:
    python-version: '3.11'  # 修改版本号
```

### 添加构建矩阵（多Python版本）
```yaml
strategy:
  matrix:
    python-version: ['3.9', '3.10', '3.11', '3.12']
```

## 📊 构建状态监控

### 成功构建特征
- ✅ 绿色对勾标记
- ✅ "build-windows-exe" job显示成功
- ✅ Artifacts中有可下载的EXE文件

### 构建失败排查
1. **检查Actions日志**: 查看详细错误信息
2. **验证依赖版本**: 检查requirements.txt兼容性
3. **测试本地运行**: 确保代码在Python 3.12可运行
4. **查看构建环境**: Windows环境可能与本地有差异

## 💡 高级功能

### 自动版本号
```yaml
- name: Build EXE with version
  run: |
    $version = git describe --tags --always
    pyinstaller --onefile --name ScreenAutoClicker-$version --console screen_autoclicker.py
```

### 代码签名（可选）
```yaml
- name: Sign EXE (if certificate available)
  run: |
    # 需要配置代码签名证书
    signtool sign /f certificate.pfx /p password dist/ScreenAutoClicker.exe
```

### 多平台构建
```yaml
jobs:
  build-windows:
    runs-on: windows-latest
    # Windows构建步骤
    
  build-linux:
    runs-on: ubuntu-latest
    # Linux构建步骤
```

## 🛡️ 安全注意事项

### 敏感信息保护
- 不要在代码中硬编码API密钥
- 使用GitHub Secrets存储敏感信息
- 定期检查依赖库的安全性

### 构建环境安全
- GitHub Actions提供隔离的构建环境
- 每次构建都是全新的虚拟机实例
- 构建完成后自动清理

## 📈 性能优化

### 构建缓存
```yaml
- name: Cache pip packages
  uses: actions/cache@v3
  with:
    path: ~/.cache/pip
    key: ${{ runner.os }}-pip-${{ hashFiles('requirements.txt') }}
    restore-keys: |
      ${{ runner.os }}-pip-
```

### 并行构建
```yaml
strategy:
  matrix:
    include:
      - os: windows-latest
        python: '3.12'
      - os: ubuntu-latest  
        python: '3.12'
```

## 🆘 故障排除

### 常见问题

#### 构建失败：ModuleNotFoundError
```
解决方案：确保requirements.txt包含所有依赖
```

#### 构建失败：权限错误
```
解决方案：检查文件路径和权限设置
```

#### EXE文件无法运行
```
解决方案：在Windows系统上测试，检查运行时依赖
```

### 获取帮助
1. 查看GitHub Actions文档
2. 检查PyInstaller问题追踪
3. 在GitHub社区提问

## 🌐 相关链接

- [GitHub Actions文档](https://docs.github.com/en/actions)
- [PyInstaller文档](https://pyinstaller.org/en/stable/)
- [Python官方网站](https://python.org)

---

**构建成功提示**: 当您看到绿色的对勾和可下载的Artifacts时，说明EXE文件已成功构建完成！ 🎉