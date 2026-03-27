#!/usr/bin/env python3
"""
邮件发送器
用于发送AI新闻简报到指定邮箱
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import os

class EmailSender:
    def __init__(self, smtp_server="smtp.qq.com", smtp_port=465):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port

    def send_newsletter(self, recipient_email, newsletter_content, sender_email=None, sender_password=None):
        """发送新闻简报邮件"""

        # 如果没有提供邮箱和密码，尝试从环境变量获取
        if sender_email is None:
            sender_email = os.environ.get('EMAIL_USERNAME')
        if sender_password is None:
            sender_password = os.environ.get('EMAIL_PASSWORD')

        if not sender_email or not sender_password:
            raise ValueError("需要提供发件人邮箱和密码，或设置环境变量 EMAIL_USERNAME 和 EMAIL_PASSWORD")

        # 创建邮件
        msg = MIMEMultipart('alternative')
        today = datetime.now().strftime('%Y年%m月%d日')
        msg['Subject'] = f'AI与大模型行业每日简报 - {today}'
        msg['From'] = sender_email
        msg['To'] = recipient_email

        # 创建HTML版本的邮件内容
        html_content = newsletter_content.replace('\n', '<br>')
        html_content = html_content.replace('## ', '<h2>').replace('##', '</h2>')
        html_content = html_content.replace('# ', '<h1>').replace('#', '</h1>')
        html_content = html_content.replace('**', '<strong>').replace('**', '</strong>')

        # 添加CSS样式
        styled_html = f"""
        <html>
            <head>
                <style>
                    body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
                    .container {{ max-width: 800px; margin: 0 auto; padding: 20px; }}
                    h1 {{ color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px; }}
                    h2 {{ color: #34495e; margin-top: 30px; }}
                    h3 {{ color: #7f8c8d; }}
                    .timestamp {{ color: #95a5a6; font-size: 0.9em; }}
                    .footer {{ margin-top: 30px; padding-top: 20px; border-top: 1px solid #ecf0f1; color: #95a5a6; }}
                    a {{ color: #3498db; text-decoration: none; }}
                    a:hover {{ text-decoration: underline; }}
                </style>
            </head>
            <body>
                <div class="container">
                    {html_content}
                </div>
            </body>
        </html>
        """

        # 添加纯文本和HTML版本
        part1 = MIMEText(newsletter_content, 'plain', 'utf-8')
        part2 = MIMEText(styled_html, 'html', 'utf-8')

        msg.attach(part1)
        msg.attach(part2)

        try:
            # 连接SMTP服务器并发送邮件
            server = smtplib.SMTP_SSL(self.smtp_server, self.smtp_port)
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())
            server.quit()
            print(f"邮件已成功发送到 {recipient_email}")
            return True
        except Exception as e:
            print(f"发送邮件失败: {e}")
            return False

def main():
    # 读取新闻简报文件
    try:
        with open('daily_ai_news.md', 'r', encoding='utf-8') as f:
            newsletter_content = f.read()
    except FileNotFoundError:
        print("未找到新闻简报文件 daily_ai_news.md")
        return

    # 发送邮件
    sender = EmailSender()
    recipient = "1372943709@qq.com"

    # 这里需要你提供发件人邮箱和密码
    # 或者设置环境变量 EMAIL_USERNAME 和 EMAIL_PASSWORD
    sender_email = input("请输入发件人邮箱: ")
    sender_password = input("请输入发件人邮箱密码/授权码: ")

    sender.send_newsletter(recipient, newsletter_content, sender_email, sender_password)

if __name__ == "__main__":
    main()