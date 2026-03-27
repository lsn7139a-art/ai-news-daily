#!/usr/bin/env python3
"""
简单的邮件测试
"""

from email_sender import EmailSender

def test_email():
    # 直接使用提供的邮箱信息
    sender_email = "1372943709@qq.com"
    sender_password = "rdwczjrfwdnkbagj"
    recipient = "1372943709@qq.com"

    print(f"发件人: {sender_email}")
    print(f"收件人: {recipient}")
    print("正在测试邮件发送...")

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

    try:
        success = sender.send_newsletter(recipient, test_content, sender_email, sender_password)

        if success:
            print("✅ 邮件发送成功！请检查你的邮箱。")
        else:
            print("❌ 邮件发送失败，请检查配置。")
    except Exception as e:
        print(f"❌ 邮件发送出错: {e}")

if __name__ == "__main__":
    test_email()