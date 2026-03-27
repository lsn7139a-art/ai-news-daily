# AI行业每日新闻简报系统

自动收集过去24小时内人工智能与大模型行业的最新重要新闻，每天早上8点推送到指定邮箱。

## 📋 功能特点

- **多源新闻收集**: 从TechCrunch、The Verge、Wired、Reuters等权威科技媒体RSS源获取新闻
- **智能筛选**: 自动过滤与AI、大模型相关的重要新闻
- **主题分类**: 按大型科技公司、技术进展、政策监管、融资并购、产品更新等主题分类
- **自动推送**: 通过GitHub Actions实现每日自动运行和邮件推送
- **格式优化**: 生成结构化的Markdown格式简报，支持HTML邮件样式

## 📰 新闻关注重点

- 大型科技公司动态（OpenAI、Google、Meta、Microsoft等）
- 大模型技术进展和突破
- 重要政策监管动态
- 大额融资与并购消息
- 影响开发者或用户的重要功能更新

## 🛠 安装与配置

### 1. 安装依赖
```bash
pip install -r requirements.txt
```

### 2. 配置邮箱
设置环境变量：
```bash
export EMAIL_USERNAME="你的QQ邮箱"
export EMAIL_PASSWORD="邮箱授权码"  # 注意：QQ邮箱需要使用授权码，不是密码
```

### 3. 手动测试运行
```bash
python main.py
```

## 🔄 自动化部署

### GitHub Actions配置
1. 将代码推送到GitHub仓库
2. 在仓库Settings > Secrets and variables > Actions中添加：
   - `EMAIL_USERNAME`: 发件人邮箱地址
   - `EMAIL_PASSWORD`: 邮箱授权码

### 定时任务
- 默认每天早上8点（北京时间）自动运行
- 可以通过GitHub Actions手动触发

## 📧 邮件配置说明

### QQ邮箱授权码获取步骤：
1. 登录QQ邮箱网页版
2. 进入设置 > 账户
3. 找到"POP3/SMTP服务"，点击"开启"
4. 按照提示获取授权码
5. 使用授权码作为`EMAIL_PASSWORD`

### SMTP配置（默认）：
- SMTP服务器: smtp.qq.com
- 端口: 465 (SSL)
- 发件人: 你的QQ邮箱
- 收件人: 1372943709@qq.com

## 📁 文件结构

```
ai资讯/
├── ai_news_collector.py    # 新闻收集器
├── email_sender.py         # 邮件发送器
├── main.py                 # 主程序
├── requirements.txt        # 依赖包
├── .github/workflows/      # GitHub Actions工作流
│   └── daily_news.yml
├── daily_ai_news.md       # 生成的新闻简报
└── README.md              # 说明文档
```

## 📊 输出格式

### 简报结构：
1. **今日要闻**: 5-10条要点标题+一句话摘要
2. **按主题分析**: 分主题详细新闻列表
3. **关键影响**: 3-5条今日对行业最关键的影响分析

### 示例输出：
```markdown
# AI与大模型行业每日简报 - 2024年03月25日

## 📰 今日要闻 (5-10条)
1. **OpenAI发布GPT-4 Turbo** - OpenAI推出了更强大的GPT-4 Turbo模型...
2. **Google Gemini重大更新** - Google宣布Gemini模型性能显著提升...

## 📊 按主题分析

### 🏢 大型科技公司动态
- **新闻标题** (发布时间)
  - 新闻摘要...
  - 来源: 来源网站 | [查看详情](链接)

## 🎯 今日关键影响
1. 科技巨头活跃度较高，表明行业仍处于快速发展期
2. 技术突破频繁，显示AI技术持续演进
```

## 🔧 自定义配置

### 修改新闻源
编辑`ai_news_collector.py`中的`self.sources`字典，添加或修改RSS源。

### 修改收件人
编辑`main.py`中的`recipient_email`变量，或将其改为从环境变量读取。

### 调整运行时间
编辑`.github/workflows/daily_news.yml`中的cron表达式：
- `0 0 * * *` = 每天UTC时间0点（北京时间8点）
- `0 23 * * *` = 每天UTC时间23点（北京时间7点）

## ⚠️ 注意事项

1. **邮箱授权码**: QQ邮箱需要使用授权码，不是登录密码
2. **RSS限制**: 部分新闻源可能有访问频率限制
3. **网络连接**: 确保GitHub Actions能够访问外部RSS源
4. **错误处理**: 程序包含基本的错误处理，但建议监控运行状态

## 📞 联系方式

如有问题或建议，请通过GitHub Issues反馈。

---
*本工具旨在帮助用户及时了解AI行业动态，新闻内容来源于公开RSS源*