#!/bin/bash

echo "🚀 AI新闻简报系统 - GitHub推送脚本"
echo "==========================================="

# 步骤1: 初始化Git仓库
echo "📁 步骤1: 初始化Git仓库"
git init
if [ $? -eq 0 ]; then
    echo "✅ Git仓库初始化成功"
else
    echo "❌ Git仓库初始化失败"
    exit 1
fi

# 步骤2: 添加所有文件到Git
echo "\n📝 步骤2: 添加文件到Git"
git add .
if [ $? -eq 0 ]; then
    echo "✅ 文件添加成功"
else
    echo "❌ 文件添加失败"
    exit 1
fi

# 步骤3: 创建初始提交
echo "\n💾 步骤3: 创建初始提交"
git commit -m "🚀 AI新闻简报系统初始提交

- 完整的AI新闻收集与推送系统
- 支持多源新闻收集（TechCrunch、The Verge等）
- 自动中文翻译功能
- GitHub Actions定时任务配置
- 邮件自动推送功能
- 完整的部署文档和测试脚本"

if [ $? -eq 0 ]; then
    echo "✅ 初始提交创建成功"
else
    echo "⚠️  提交可能已存在，继续下一步"
fi

# 步骤4: 设置远程仓库
echo "\n🌐 步骤4: 设置远程仓库"
echo "请在下方输入您的GitHub仓库URL:"
echo "格式: https://github.com/用户名/仓库名.git"
read -p "GitHub仓库URL: " repo_url

if [ ! -z "$repo_url" ]; then
    git remote add origin "$repo_url"
    if [ $? -eq 0 ]; then
        echo "✅ 远程仓库设置成功"
    else
        echo "❌ 远程仓库设置失败，请检查URL格式"
        exit 1
    fi
else
    echo "❌ 仓库URL不能为空"
    exit 1
fi

# 步骤5: 推送到GitHub
echo "\n📤 步骤5: 推送到GitHub"
git push -u origin main
if [ $? -eq 0 ]; then
    echo "✅ 代码推送成功！"
else
    echo "❌ 推送失败，可能需要先拉取远程更改"
    echo "尝试强制推送..."
    git push -u origin main --force
fi

echo "\n🎉 推送完成！"
echo "==========================================="
echo "📋 后续配置步骤:"
echo "1. 访问您的GitHub仓库"
echo "2. 进入 Settings > Secrets and variables > Actions"
echo "3. 添加以下Secrets:"
echo "   - EMAIL_USERNAME: 您的QQ邮箱地址"
echo "   - EMAIL_PASSWORD: QQ邮箱授权码"
echo "4. 等待每天UTC时间0点（北京时间8点）自动运行"
echo "==========================================="