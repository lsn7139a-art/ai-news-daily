#!/usr/bin/env python3
"""
AI行业每日新闻收集器
自动收集过去24小时内人工智能与大模型行业的重要新闻
"""

import requests
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import feedparser
from typing import List, Dict
from translator import NewsTranslator

class AINewsCollector:
    def __init__(self):
        self.sources = {
            'techcrunch_ai': 'https://techcrunch.com/category/artificial-intelligence/feed/',
            'theverge_ai': 'https://www.theverge.com/rss/ai/index.xml',
            'wired_ai': 'https://www.wired.com/feed/category/ai/latest/rss',
            'reuters_ai': 'https://www.reuters.com/rssFeed/technologyNews',
        }
        self.translator = NewsTranslator()

    def fetch_news_from_rss(self, source_name: str, rss_url: str) -> List[Dict]:
        """从RSS源获取新闻"""
        try:
            feed = feedparser.parse(rss_url)
            news_items = []

            # 获取过去24小时的时间戳
            yesterday = datetime.now() - timedelta(days=1)

            for entry in feed.entries:
                published_time = datetime(*entry.published_parsed[:6])

                if published_time > yesterday:
                    news_items.append({
                        'title': entry.title,
                        'summary': entry.description if hasattr(entry, 'description') else '',
                        'link': entry.link,
                        'published': published_time.strftime('%Y-%m-%d %H:%M'),
                        'source': source_name
                    })

            return news_items
        except Exception as e:
            print(f"Error fetching from {source_name}: {e}")
            return []

    def fetch_techcrunch_ai_news(self) -> List[Dict]:
        """获取TechCrunch AI新闻"""
        return self.fetch_news_from_rss('techcrunch_ai', self.sources['techcrunch_ai'])

    def fetch_theverge_ai_news(self) -> List[Dict]:
        """获取The Verge AI新闻"""
        return self.fetch_news_from_rss('theverge_ai', self.sources['theverge_ai'])

    def fetch_wired_ai_news(self) -> List[Dict]:
        """获取Wired AI新闻"""
        return self.fetch_news_from_rss('wired_ai', self.sources['wired_ai'])

    def fetch_reuters_tech_news(self) -> List[Dict]:
        """获取Reuters科技新闻"""
        return self.fetch_news_from_rss('reuters_ai', self.sources['reuters_ai'])

    def filter_ai_related_news(self, news_items: List[Dict]) -> List[Dict]:
        """过滤与AI和大模型相关的新闻"""
        ai_keywords = [
            'AI', 'artificial intelligence', 'machine learning', 'deep learning',
            'large language model', 'LLM', 'GPT', 'OpenAI', 'Google', 'Meta',
            'Anthropic', 'Claude', 'Gemini', 'ChatGPT', 'neural network',
            'transformer', 'model training', 'AI regulation', 'AI policy'
        ]

        filtered_news = []

        for item in news_items:
            title_lower = item['title'].lower()
            summary_lower = item['summary'].lower() if item['summary'] else ''

            # 检查标题或摘要是否包含AI相关关键词
            if any(keyword.lower() in title_lower or keyword.lower() in summary_lower
                   for keyword in ai_keywords):
                filtered_news.append(item)

        return filtered_news

    def categorize_news(self, news_items: List[Dict]) -> Dict[str, List[Dict]]:
        """按主题分类新闻"""
        categories = {
            'tech_companies': [],  # 大型科技公司动态
            'model_advancements': [],  # 大模型技术进展
            'policy_regulation': [],  # 政策监管动态
            'funding_ma': [],  # 融资并购
            'product_updates': [],  # 重要功能更新
            'other': []  # 其他
        }

        for item in news_items:
            title = item['title'].lower()
            summary = item['summary'].lower() if item['summary'] else ''
            content = title + ' ' + summary

            # 大型科技公司
            if any(company in content for company in ['openai', 'google', 'meta', 'microsoft', 'apple', 'amazon', 'nvidia']):
                categories['tech_companies'].append(item)
            # 技术进展
            elif any(tech in content for tech in ['breakthrough', 'advancement', 'research', 'study', 'paper', 'model', 'algorithm']):
                categories['model_advancements'].append(item)
            # 政策监管
            elif any(policy in content for policy in ['regulation', 'policy', 'law', 'government', 'fda', 'eu', 'china', 'regulation']):
                categories['policy_regulation'].append(item)
            # 融资并购
            elif any(finance in content for finance in ['funding', 'investment', 'acquisition', 'buy', 'merge', 'billion', 'million', 'dollars']):
                categories['funding_ma'].append(item)
            # 产品更新
            elif any(product in content for product in ['launch', 'release', 'update', 'feature', 'announce', 'introduce']):
                categories['product_updates'].append(item)
            else:
                categories['other'].append(item)

        return categories

    def generate_newsletter(self, categorized_news: Dict[str, List[Dict]]) -> str:
        """生成新闻简报"""
        today = datetime.now().strftime('%Y年%m月%d日')

        newsletter = f"""# AI与大模型行业每日简报 - {today}

## 📰 今日要闻 (5-10条)
"""

        # 收集所有新闻用于要点列表
        all_news = []
        for category_news in categorized_news.values():
            all_news.extend(category_news)

        # 生成要点列表
        for i, news in enumerate(all_news[:10], 1):
            title_en = news['title']
            title_zh = news.get('title_zh', title_en)

            # 提取一句话摘要
            summary_en = news['summary'][:100] + '...' if len(news['summary']) > 100 else news['summary']
            summary_zh = news.get('summary_zh', "重要AI行业动态更新")

            newsletter += f"{i}. **{title_zh}**\n"
            newsletter += f"   *英文原文: {title_en}*\n"
            newsletter += f"   📝 {summary_zh}\n"
            newsletter += f"   🔗 [查看详情]({news['link']})\n\n"

        newsletter += "\n## 📊 按主题分析\n\n"

        # 按主题分段分析
        category_names = {
            'tech_companies': '🏢 大型科技公司动态',
            'model_advancements': '🔬 大模型技术进展',
            'policy_regulation': '📋 政策监管动态',
            'funding_ma': '💰 融资并购动态',
            'product_updates': '🚀 产品功能更新',
            'other': '📌 其他重要动态'
        }

        for category, news_list in categorized_news.items():
            if news_list:
                newsletter += f"### {category_names[category]}\n\n"
                for news in news_list:
                    title_zh = news.get('title_zh', news['title'])
                    title_en = news['title']
                    summary_zh = news.get('summary_zh', "暂无中文摘要")

                    newsletter += f"- **{title_zh}** ({news['published']})\n"
                    newsletter += f"  - *英文原文: {title_en}*\n"
                    newsletter += f"  - 📝 {summary_zh}\n"
                    newsletter += f"  - 🔗 [查看原文]({news['link']}) | 来源: {news['source']}\n\n"

        # 今日关键影响总结
        newsletter += "## 🎯 今日关键影响\n\n"
        key_insights = self.generate_key_insights(categorized_news)
        for i, insight in enumerate(key_insights, 1):
            newsletter += f"{i}. {insight}\n"

        newsletter += f"\n---\n*本简报由AI新闻收集器自动生成 | 生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*"

        return newsletter

    def generate_key_insights(self, categorized_news: Dict[str, List[Dict]]) -> List[str]:
        """生成关键影响分析"""
        insights = []

        # 分析各类新闻数量
        tech_count = len(categorized_news['tech_companies'])
        model_count = len(categorized_news['model_advancements'])
        policy_count = len(categorized_news['policy_regulation'])
        funding_count = len(categorized_news['funding_ma'])

        if tech_count > 0:
            insights.append(f"科技巨头活跃度{'高' if tech_count >= 3 else '中等'}，共{tech_count}条相关新闻，表明行业仍处于快速发展期")

        if model_count > 0:
            insights.append(f"技术突破频繁，{model_count}项重要进展显示AI技术持续演进")

        if policy_count > 0:
            insights.append(f"监管关注度提升，{policy_count}条政策相关新闻提示合规重要性")

        if funding_count > 0:
            insights.append(f"资本市场活跃，{funding_count}条融资并购新闻反映行业投资热度")

        if not insights:
            insights.append("今日新闻相对平稳，建议关注后续发展")

        return insights[:5]  # 最多5条

    def collect_daily_news(self) -> str:
        """收集并生成每日新闻简报"""
        print("开始收集AI行业新闻...")

        all_news = []

        # 从各个源收集新闻
        sources_methods = [
            self.fetch_techcrunch_ai_news,
            self.fetch_theverge_ai_news,
            self.fetch_wired_ai_news,
            self.fetch_reuters_tech_news
        ]

        for method in sources_methods:
            try:
                news = method()
                all_news.extend(news)
                time.sleep(1)  # 避免请求过于频繁
            except Exception as e:
                print(f"Error collecting news: {e}")

        print(f"收集到 {len(all_news)} 条原始新闻")

        # 过滤AI相关新闻
        ai_news = self.filter_ai_related_news(all_news)
        print(f"筛选后得到 {len(ai_news)} 条AI相关新闻")

        # 翻译新闻（添加中文翻译）
        print(f"正在为 {len(ai_news)} 条新闻添加中文翻译...")
        translated_news = self.translator.translate_news_batch(ai_news)

        # 分类
        categorized_news = self.categorize_news(translated_news)

        # 生成简报
        newsletter = self.generate_newsletter(categorized_news)

        return newsletter

def main():
    collector = AINewsCollector()
    newsletter = collector.collect_daily_news()

    # 保存到文件
    with open('daily_ai_news.md', 'w', encoding='utf-8') as f:
        f.write(newsletter)

    print("每日AI新闻简报已生成: daily_ai_news.md")
    print("\n" + "="*50)
    try:
        print(newsletter[:500] + "..." if len(newsletter) > 500 else newsletter)
    except UnicodeEncodeError:
        print("新闻简报已生成，包含中文内容，请在文件中查看详细内容")

if __name__ == "__main__":
    main()