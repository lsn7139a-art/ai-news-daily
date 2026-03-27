#!/usr/bin/env python3
"""
测试邮件发送功能
"""

import os
from email_sender import EmailSender

def test_email():
    # 检查环境变量
    sender_email = os.environ.get('EMAIL_USERNAME')
    sender_password = os.environ.get('EMAIL_PASSWORD')

    print(f"发件人邮箱: {sender_email}")
    print(f"授权码: {sender_password[:4]}... (隐藏)")

    if not sender_email or not sender_password:
        print("❌ 环境变量未设置")
        return

    # 创建邮件发送器
    sender = EmailSender()

    # 测试邮件内容
    test_content = """# AI新闻简报测试邮件

## 测试成功！
你的邮箱配置正确，系统可以正常发送邮件。

## 测试要点
1. **邮箱配置**: ✅ 正确
2. **授权码**: ✅ 有效
3. **SMTP连接**: ✅ 成功

系统将在每天早上8点自动发送AI行业新闻简报。
"""

    # 发送到自己的邮箱
    recipient = "1372943709@qq.com"

    print(f"正在发送测试邮件到: {recipient}")

    success = sender.send_newsletter(recipient, test_content, sender_email, sender_password)

    if success:
        print("✅ 邮件发送成功！请检查你的邮箱。")
    else:
        print("❌ 邮件发送失败，请检查配置。")

if __name__ == "__main__":
    test_email()