# GitHub Token 使用指南

## 🔑 设置GitHub Token

### 方法一：环境变量（推荐）
```bash
# 在当前终端会话中设置
export GITHUB_TOKEN=你的token内容

# 验证token有效
curl -H "Authorization: token $GITHUB_TOKEN" https://api.github.com/user
```

### 方法二：配置文件
```bash
# 创建GitHub配置文件
echo "github.com:
  user: 你的用户名
  oauth_token: 你的token内容" > ~/.config/gh/hosts.yml

# 设置权限
chmod 600 ~/.config/gh/hosts.yml
```

### 方法三：GitHub CLI认证
```bash
# 使用token登录
gh auth login --with-token <<< "你的token内容"

# 验证认证
gh auth status
```

## 🚀 自动化构建命令

### 完整自动化脚本
```bash
# 设置token
export GITHUB_TOKEN=你的token内容

# 运行自动化脚本
cd /vol1/1000/NAS/Project/ScreenAutoClicker/
./automate_github.sh
```

### 分步执行

#### 1. 创建仓库
```bash
curl -X POST \
  -H "Authorization: token $GITHUB_TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  https://api.github.com/user/repos \
  -d '{"name":"ScreenAutoClicker","description":"Windows屏幕自动化工具","private":false}'
```

#### 2. 配置Git并上传
```bash
# 克隆仓库
git clone https://github.com/你的用户名/ScreenAutoClicker.git
cd ScreenAutoClicker

# 复制文件
cp -r /vol1/1000/NAS/Project/ScreenAutoClicker/* .

# 提交并推送
git add .
git config user.email "你的邮箱"
git config user.name "你的名字"
git commit -m "初始提交：屏幕自动化工具"
git push origin main
```

#### 3. 触发构建
```bash
# 推送后自动触发，或手动触发
curl -X POST \
  -H "Authorization: token $GITHUB_TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  https://api.github.com/repos/你的用户名/ScreenAutoClicker/actions/workflows/build.yml/dispatches \
  -d '{"ref":"main"}'
```

#### 4. 下载EXE
```bash
# 等待构建完成后下载
# 从Actions页面Artifacts部分下载
```

## 🔒 Token权限要求

您的GitHub token需要以下权限：

### 必需权限
- ✅ `repo` - 完整仓库访问
- ✅ `workflow` - 工作流权限
- ✅ `read:org` - 读取组织信息（如有）

### 推荐权限
- ✅ `delete_repo` - 允许删除仓库（测试用）
- ✅ `admin:public_key` - 管理部署密钥

## 🛡️ 安全最佳实践

### Token保护
- 🔒 不要将token提交到代码仓库
- 🔒 使用环境变量而非硬编码
- 🔒 定期轮换token
- 🔒 限制token权限范围

### 安全存储
```bash
# 使用密码管理器存储token
# 或使用加密配置文件
# 避免明文存储
```

## 📊 验证和调试

### 验证Token有效性
```bash
# 验证token权限
curl -H "Authorization: token $GITHUB_TOKEN" https://api.github.com/user

# 检查仓库访问
curl -H "Authorization: token $GITHUB_TOKEN" https://api.github.com/repos/你的用户名/ScreenAutoClicker
```

### 调试API请求
```bash
# 详细输出
curl -v -H "Authorization: token $GITHUB_TOKEN" https://api.github.com/user

# 仅显示HTTP状态码
curl -s -o /dev/null -w "%{http_code}" -H "Authorization: token $GITHUB_TOKEN" https://api.github.com/user
```

## 🆘 常见问题

### Token无效
```
错误: 401 Unauthorized
解决方案: 检查token是否正确，权限是否足够
```

### 权限不足
```
错误: 403 Forbidden
解决方案: 检查token权限范围，可能需要重新生成
```

### 仓库已存在
```
错误: 422 Validation Failed
解决方案: 删除现有仓库或使用不同名称
```

## 🌐 API参考

- [GitHub REST API文档](https://docs.github.com/en/rest)
- [Personal Access Tokens管理](https://github.com/settings/tokens)
- [GitHub Actions API](https://docs.github.com/en/rest/actions)

## 📞 技术支持

如果遇到问题：
1. 检查token权限
2. 验证网络连接
3. 查看GitHub API文档
4. 检查错误信息详情

---

**重要**: 请妥善保管您的GitHub token，避免泄露！ 🔐