#!/usr/bin/env python3
"""
AI新闻收集与推送主程序
整合新闻收集和邮件发送功能
"""

import os
from ai_news_collector import AINewsCollector
from email_sender import EmailSender

def main():
    print("🚀 开始AI行业每日新闻收集与推送...")

    # 1. 收集新闻
    print("📰 正在收集AI行业新闻...")
    collector = AINewsCollector()
    newsletter_content = collector.collect_daily_news()

    # 保存新闻简报
    with open('daily_ai_news.md', 'w', encoding='utf-8') as f:
        f.write(newsletter_content)
    print("✅ 新闻简报已保存到 daily_ai_news.md")

    # 2. 发送邮件
    print("📧 正在发送邮件...")
    sender = EmailSender()

    # 从环境变量获取邮箱配置
    sender_email = os.environ.get('EMAIL_USERNAME')
    sender_password = os.environ.get('EMAIL_PASSWORD')
    recipient_email = "1372943709@qq.com"

    if sender_email and sender_password:
        success = sender.send_newsletter(recipient_email, newsletter_content, sender_email, sender_password)
        if success:
            print("✅ 邮件发送成功！")
        else:
            print("❌ 邮件发送失败")
    else:
        print("⚠️  未配置邮箱信息，跳过邮件发送")
        print("请设置环境变量 EMAIL_USERNAME 和 EMAIL_PASSWORD")

    print("\n🎯 任务完成！")

if __name__ == "__main__":
    main()