# AI新闻简报系统部署指南

## 🚀 快速开始

### 1. 本地测试部署

```bash
# 1. 克隆或下载代码到本地
# 2. 安装依赖
pip install -r requirements.txt

# 3. 运行安装脚本
python setup.py

# 4. 配置邮箱环境变量
export EMAIL_USERNAME="你的QQ邮箱"
export EMAIL_PASSWORD="邮箱授权码"

# 5. 测试运行
python main.py
```

### 2. GitHub Actions自动化部署

#### 步骤1: 创建GitHub仓库
```bash
# 初始化git仓库
git init
git add .
git commit -m "Initial commit"

# 创建远程仓库并推送
git remote add origin https://github.com/你的用户名/ai-news-daily.git
git push -u origin main
```

#### 步骤2: 配置GitHub Secrets

在GitHub仓库中配置以下Secrets：

1. 进入仓库 Settings > Secrets and variables > Actions
2. 点击 "New repository secret"
3. 添加以下secrets：

- **EMAIL_USERNAME**: 你的QQ邮箱地址（如：123456789@qq.com）
- **EMAIL_PASSWORD**: QQ邮箱授权码（不是密码）

#### 步骤3: 获取QQ邮箱授权码

1. 登录QQ邮箱网页版 (mail.qq.com)
2. 点击右上角的 "设置"
3. 选择 "账户" 选项卡
4. 找到 "POP3/SMTP服务"，点击 "开启"
5. 按照提示完成验证，获取16位授权码
6. 使用这个授权码作为 `EMAIL_PASSWORD`

## 📧 邮箱配置详细说明

### QQ邮箱配置

```bash
# 环境变量配置示例
export EMAIL_USERNAME="1372943709@qq.com"
export EMAIL_PASSWORD="abcd1234efgh5678"  # 16位授权码
```

### SMTP服务器配置

- **SMTP服务器**: smtp.qq.com
- **端口**: 465 (SSL)
- **加密方式**: SSL/TLS
- **认证方式**: 用户名密码认证

### 其他邮箱配置

如果要使用其他邮箱，修改 `email_sender.py`：

```python
# Gmail配置
smtp_server = "smtp.gmail.com"
smtp_port = 587  # 或 465

# 163邮箱配置
smtp_server = "smtp.163.com"
smtp_port = 465
```

## ⏰ 定时任务配置

### 修改运行时间

编辑 `.github/workflows/daily_news.yml`：

```yaml
# 每天早上8点（北京时间）
cron: '0 0 * * *'  # UTC时间0点 = 北京时间8点

# 每天早上7点（北京时间）
cron: '0 23 * * *'  # UTC时间23点 = 北京时间7点

# 每天早上9点（北京时间）
cron: '0 1 * * *'   # UTC时间1点 = 北京时间9点
```

### Cron表达式说明

- `0 0 * * *`: 每天UTC时间0点（北京时间8点）
- `0 1 * * *`: 每天UTC时间1点（北京时间9点）
- `0 23 * * *`: 每天UTC时间23点（北京时间7点）

格式：`分钟 小时 日 月 周`

## 🔧 自定义配置

### 修改新闻源

编辑 `ai_news_collector.py` 中的 `self.sources`：

```python
self.sources = {
    'techcrunch_ai': 'https://techcrunch.com/category/artificial-intelligence/feed/',
    'theverge_ai': 'https://www.theverge.com/rss/ai/index.xml',
    'wired_ai': 'https://www.wired.com/feed/category/ai/latest/rss',
    'reuters_ai': 'https://www.reuters.com/rssFeed/technologyNews',
    # 添加更多新闻源
    'your_source': 'https://example.com/rss',
}
```

### 修改收件人

编辑 `main.py`：

```python
# 修改收件人邮箱
recipient_email = "your-email@example.com"

# 或从环境变量读取
recipient_email = os.environ.get('RECIPIENT_EMAIL', '1372943709@qq.com')
```

### 调整新闻筛选关键词

编辑 `ai_news_collector.py` 中的 `ai_keywords`：

```python
ai_keywords = [
    'AI', 'artificial intelligence', 'machine learning', 'deep learning',
    'large language model', 'LLM', 'GPT', 'OpenAI', 'Google', 'Meta',
    'Anthropic', 'Claude', 'Gemini', 'ChatGPT', 'neural network',
    'transformer', 'model training', 'AI regulation', 'AI policy',
    # 添加更多关键词
    'your_keyword',
]
```

## 📊 监控与维护

### 查看GitHub Actions运行状态

1. 进入GitHub仓库
2. 点击 "Actions" 选项卡
3. 查看 "Daily AI News" 工作流的运行历史
4. 点击具体运行记录查看详细日志

### 常见问题排查

#### 邮件发送失败

```bash
# 检查环境变量是否设置
echo $EMAIL_USERNAME
echo $EMAIL_PASSWORD

# 检查邮箱授权码是否正确
# 重新生成QQ邮箱授权码
```

#### RSS源访问失败

```bash
# 测试RSS源是否可访问
curl -I https://techcrunch.com/category/artificial-intelligence/feed/

# 检查网络连接
ping techcrunch.com
```

#### 编码问题

```bash
# 如果出现中文编码问题，设置环境变量
export PYTHONIOENCODING=utf-8
```

## 🛡️ 安全建议

1. **不要硬编码敏感信息**：始终使用环境变量或GitHub Secrets
2. **定期更新授权码**：建议每3-6个月更新一次邮箱授权码
3. **监控运行日志**：定期检查GitHub Actions运行状态
4. **备份配置**：备份重要的配置文件和环境变量设置

## 📞 故障排除

### 工作流不运行

1. 检查cron表达式是否正确
2. 确保仓库有代码提交
3. 检查工作流文件路径是否正确

### 邮件发送失败

1. 检查邮箱授权码是否正确
2. 确认SMTP服务器配置
3. 检查收件人邮箱地址

### 新闻收集失败

1. 检查RSS源是否可访问
2. 查看网络连接
3. 检查Python依赖是否安装

## 🎯 性能优化

### 增加缓存

```python
# 在ai_news_collector.py中添加缓存
import json
from datetime import datetime, timedelta

class NewsCache:
    def __init__(self, cache_file='news_cache.json'):
        self.cache_file = cache_file
        self.cache_duration = timedelta(hours=1)

    def get_cached_news(self):
        try:
            with open(self.cache_file, 'r') as f:
                cache = json.load(f)
                cache_time = datetime.fromisoformat(cache['timestamp'])
                if datetime.now() - cache_time < self.cache_duration:
                    return cache['news']
        except:
            pass
        return None

    def cache_news(self, news):
        cache = {
            'timestamp': datetime.now().isoformat(),
            'news': news
        }
        with open(self.cache_file, 'w') as f:
            json.dump(cache, f)
```

### 并发处理

```python
# 使用并发提高新闻收集速度
import concurrent.futures

def fetch_all_news_concurrent(self):
    sources_methods = [
        self.fetch_techcrunch_ai_news,
        self.fetch_theverge_ai_news,
        self.fetch_wired_ai_news,
        self.fetch_reuters_tech_news
    ]

    all_news = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(method) for method in sources_methods]
        for future in concurrent.futures.as_completed(futures):
            try:
                news = future.result()
                all_news.extend(news)
            except Exception as e:
                print(f"Error: {e}")

    return all_news
```

## 📈 扩展功能

### 添加Telegram推送

```python
# telegram_sender.py
import requests

class TelegramSender:
    def __init__(self, bot_token, chat_id):
        self.bot_token = bot_token
        self.chat_id = chat_id
        self.api_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

    def send_message(self, text):
        payload = {
            'chat_id': self.chat_id,
            'text': text,
            'parse_mode': 'HTML'
        }
        response = requests.post(self.api_url, json=payload)
        return response.status_code == 200
```

### 添加数据库存储

```python
# database.py
import sqlite3
from datetime import datetime

class NewsDatabase:
    def __init__(self, db_file='news.db'):
        self.db_file = db_file
        self.init_database()

    def init_database(self):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS news (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                summary TEXT,
                link TEXT,
                source TEXT,
                category TEXT,
                published_date TEXT,
                collected_date TEXT
            )
        ''')
        conn.commit()
        conn.close()

    def save_news(self, news_items):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        for item in news_items:
            cursor.execute('''
                INSERT INTO news (title, summary, link, source, category, published_date, collected_date)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (
                item['title'], item['summary'], item['link'],
                item['source'], item.get('category', ''),
                item['published'], datetime.now().isoformat()
            ))
        conn.commit()
        conn.close()
```

## 📋 部署检查清单

- [ ] 安装Python依赖
- [ ] 配置邮箱环境变量
- [ ] 测试本地运行
- [ ] 创建GitHub仓库
- [ ] 配置GitHub Secrets
- [ ] 推送代码到GitHub
- [ ] 验证GitHub Actions运行
- [ ] 检查邮件接收
- [ ] 监控首次自动运行

---

*部署完成后，系统将每天自动收集AI行业新闻并发送到指定邮箱。*