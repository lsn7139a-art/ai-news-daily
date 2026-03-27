#!/usr/bin/env python3
"""
完整系统部署脚本
"""

import os
import subprocess
import sys
from ai_news_collector import AINewsCollector
from email_sender import EmailSender

def run_full_test():
    """运行完整系统测试"""
    print("开始完整系统测试...")
    print("=" * 50)

    # 1. 测试新闻收集
    print("测试新闻收集...")
    collector = AINewsCollector()
    newsletter = collector.collect_daily_news()

    if newsletter:
        print("✅ 新闻收集成功")

        # 保存新闻简报
        with open('daily_ai_news.md', 'w', encoding='utf-8') as f:
            f.write(newsletter)
        print("✅ 新闻简报已保存")
    else:
        print("❌ 新闻收集失败")
        return False

    # 2. 测试邮件发送
    print("\n测试邮件发送...")
    sender = EmailSender()

    # 直接使用邮箱信息
    sender_email = "1372943709@qq.com"
    sender_password = "rdwczjrfwdnkbagj"
    recipient_email = "1372943709@qq.com"

    try:
        success = sender.send_newsletter(recipient_email, newsletter, sender_email, sender_password)
        if success:
            print("✅ 邮件发送成功")
        else:
            print("❌ 邮件发送失败")
            return False
    except Exception as e:
        print(f"❌ 邮件发送出错: {e}")
        return False

    return True

def create_github_secrets():
    """显示GitHub Secrets配置说明"""
    print("\nGitHub Secrets配置")
    print("=" * 50)
    print("请在GitHub仓库的Settings > Secrets and variables > Actions中配置：")
    print()
    print("EMAIL_USERNAME: 1372943709@qq.com")
    print("EMAIL_PASSWORD: rdwczjrfwdnkbagj")
    print()
    print("配置完成后，系统将每天自动运行并发送新闻简报。")

def main():
    print("🎯 AI新闻简报系统部署")
    print("=" * 50)

    # 运行完整测试
    success = run_full_test()

    if success:
        print("\n" + "=" * 50)
        print("✅ 系统测试全部通过！")
        print("\n📋 部署步骤：")
        print("1. 将代码推送到GitHub仓库")
        print("2. 配置GitHub Secrets")
        print("3. 等待每天8点自动运行")

        # 显示GitHub配置
        create_github_secrets()

        print("\n部署完成！系统将在每天早上8点自动发送AI新闻简报。")
    else:
        print("\n❌ 系统测试失败，请检查配置后重试。")

if __name__ == "__main__":
    main()