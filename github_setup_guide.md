# GitHub仓库设置完整指南

## 📋 准备工作

### 1. 创建GitHub仓库
1. 登录您的GitHub账户
2. 点击右上角的 "+" > "New repository"
3. 填写仓库信息：
   - **Repository name**: `ai-news-daily` (或其他您喜欢的名称)
   - **Description**: `AI行业每日新闻自动收集与推送系统`
   - **Public/Private**: 建议选择Public（免费）
   - **不要**勾选 "Initialize this repository with a README"
4. 点击 "Create repository"

### 2. 获取仓库URL
创建完成后，复制仓库的HTTPS URL，格式如下：
```
https://github.com/您的用户名/ai-news-daily.git
```

## 🚀 推送代码到GitHub

### 方法1: 使用自动脚本（推荐）
```bash
# 赋予脚本执行权限
chmod +x github_push.sh

# 运行推送脚本
./github_push.sh
```

### 方法2: 手动推送
```bash
# 1. 初始化Git仓库
git init

# 2. 添加所有文件
git add .

# 3. 创建提交
git commit -m "🚀 AI新闻简报系统初始提交"

# 4. 设置远程仓库
git remote add origin https://github.com/您的用户名/ai-news-daily.git

# 5. 推送到GitHub
git push -u origin main
```

## 🔐 配置GitHub Secrets

### 步骤1: 进入仓库设置
1. 打开您的GitHub仓库页面
2. 点击 "Settings" 选项卡
3. 在左侧菜单中选择 "Secrets and variables" > "Actions"

### 步骤2: 添加邮箱Secrets
点击 "New repository secret"，添加以下两个Secrets：

#### Secret 1: EMAIL_USERNAME
- **Name**: `EMAIL_USERNAME`
- **Value**: 您的QQ邮箱地址 (如：123456789@qq.com)

#### Secret 2: EMAIL_PASSWORD
- **Name**: `EMAIL_PASSWORD`
- **Value**: QQ邮箱授权码 (16位字符)

### 获取QQ邮箱授权码的步骤：
1. 登录QQ邮箱网页版 (mail.qq.com)
2. 点击右上角 "设置" > "账户"
3. 找到 "POP3/SMTP服务"，点击 "开启"
4. 按照提示完成验证，获取16位授权码

## ⏰ 自动运行确认

### 检查GitHub Actions
1. 返回仓库主页
2. 点击 "Actions" 选项卡
3. 应该能看到 "Daily AI News" 工作流
4. 工作流会在每天UTC时间0点（北京时间8点）自动运行

### 手动测试运行
1. 在 "Actions" 页面
2. 点击 "Daily AI News" 工作流
3. 点击 "Run workflow" > "Run workflow"
4. 等待几分钟查看运行结果

## 📧 验证邮件接收

1. 等待工作流运行完成（约2-3分钟）
2. 检查您的QQ邮箱是否收到AI新闻简报
3. 如果没有收到，检查工作流的运行日志排查问题

## 🛠️ 故障排除

### 推送失败
```bash
# 如果推送失败，尝试：
git pull origin main --allow-unrelated-histories
git push -u origin main
```

### 工作流不运行
1. 检查工作流文件路径：`.github/workflows/daily_news.yml`
2. 确认Secrets配置正确
3. 检查cron表达式：`0 0 * * *`

### 邮件发送失败
1. 确认邮箱授权码正确
2. 检查SMTP服务器设置
3. 查看GitHub Actions运行日志

## 🎯 成功标志

✅ **GitHub仓库创建成功** - 代码已推送
✅ **Secrets配置完成** - 邮箱信息已设置
✅ **工作流正常运行** - 每天自动执行
✅ **邮件正常接收** - 每天收到AI新闻简报

## 📞 支持

如果遇到问题，请检查：
- `README.md`: 项目使用说明
- `DEPLOYMENT.md`: 详细部署指南
- GitHub Actions运行日志

---

**完成以上步骤后，您就可以享受每天自动推送的AI新闻简报了！即使电脑关机，系统也会在GitHub云端自动运行。**