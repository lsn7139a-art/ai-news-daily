#!/usr/bin/env python3
"""
系统测试脚本
用于测试AI新闻收集系统的各个组件
"""

import os
import sys
from ai_news_collector import AINewsCollector
from email_sender import EmailSender

def test_news_collection():
    """测试新闻收集功能"""
    print("测试新闻收集功能...")

    collector = AINewsCollector()

    # 测试各个新闻源
    try:
        techcrunch_news = collector.fetch_techcrunch_ai_news()
        print(f"TechCrunch: 收集到 {len(techcrunch_news)} 条新闻")

        theverge_news = collector.fetch_theverge_ai_news()
        print(f"The Verge: 收集到 {len(theverge_news)} 条新闻")

        wired_news = collector.fetch_wired_ai_news()
        print(f"Wired: 收集到 {len(wired_news)} 条新闻")

        reuters_news = collector.fetch_reuters_tech_news()
        print(f"Reuters: 收集到 {len(reuters_news)} 条新闻")

        # 测试新闻筛选
        all_news = techcrunch_news + theverge_news + wired_news + reuters_news
        ai_news = collector.filter_ai_related_news(all_news)
        print(f"AI相关筛选: 从 {len(all_news)} 条中筛选出 {len(ai_news)} 条AI相关新闻")

        # 测试新闻分类
        categorized_news = collector.categorize_news(ai_news)
        total_categorized = sum(len(news_list) for news_list in categorized_news.values())
        print(f"新闻分类: 成功分类 {total_categorized} 条新闻")

        # 测试简报生成
        newsletter = collector.generate_newsletter(categorized_news)
        print(f"简报生成: 生成简报长度 {len(newsletter)} 字符")

        return newsletter

    except Exception as e:
        print(f"新闻收集测试失败: {e}")
        return None

def test_email_sending():
    """测试邮件发送功能"""
    print("\n测试邮件发送功能...")

    # 检查环境变量
    sender_email = os.environ.get('EMAIL_USERNAME')
    sender_password = os.environ.get('EMAIL_PASSWORD')

    if not sender_email or not sender_password:
        print("未配置邮箱环境变量，跳过邮件发送测试")
        return False

    try:
        sender = EmailSender()

        # 创建测试邮件内容
        test_content = """# AI新闻简报测试

## 测试要点
1. **测试新闻1** - 这是一条测试新闻
2. **测试新闻2** - 这是另一条测试新闻

## 测试分析
### 🏢 科技公司动态
- 测试新闻内容

## 🎯 关键影响
1. 测试系统正常工作
"""

        # 发送测试邮件到自身
        success = sender.send_newsletter(sender_email, test_content, sender_email, sender_password)

        if success:
            print("邮件发送测试成功")
            return True
        else:
            print("邮件发送测试失败")
            return False

    except Exception as e:
        print(f"邮件发送测试失败: {e}")
        return False

def test_file_operations():
    """测试文件操作"""
    print("\n测试文件操作...")

    try:
        # 测试写入文件
        test_content = "# 测试文件\n这是一条测试内容"
        with open('test_file.md', 'w', encoding='utf-8') as f:
            f.write(test_content)

        # 测试读取文件
        with open('test_file.md', 'r', encoding='utf-8') as f:
            content = f.read()

        if content == test_content:
            print("文件读写测试成功")
            # 清理测试文件
            os.remove('test_file.md')
            return True
        else:
            print("文件读写测试失败")
            return False

    except Exception as e:
        print(f"文件操作测试失败: {e}")
        return False

def main():
    """运行完整系统测试"""
    print("开始AI新闻收集系统测试")
    print("=" * 50)

    # 测试文件操作
    file_test = test_file_operations()

    # 测试新闻收集
    newsletter = test_news_collection()

    # 测试邮件发送
    email_test = test_email_sending()

    print("\n" + "=" * 50)
    print("测试结果汇总")
    print(f"文件操作测试: {'通过' if file_test else '失败'}")
    print(f"新闻收集测试: {'通过' if newsletter else '失败'}")
    print(f"邮件发送测试: {'通过' if email_test else '跳过/失败'}")

    if newsletter:
        print(f"\n生成的简报预览:")
        print("-" * 30)
        preview = newsletter[:500] + "..." if len(newsletter) > 500 else newsletter
        print(preview)

    print("\n测试完成！")

    # 询问是否保存测试简报
    if newsletter:
        save = input("\n是否保存测试简报？(y/n): ")
        if save.lower() == 'y':
            with open('test_newsletter.md', 'w', encoding='utf-8') as f:
                f.write(newsletter)
            print("测试简报已保存到 test_newsletter.md")

if __name__ == "__main__":
    main()