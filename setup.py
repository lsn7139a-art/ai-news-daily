#!/usr/bin/env python3
"""
安装脚本
用于快速设置AI新闻收集系统
"""

import os
import subprocess
import sys

def install_dependencies():
    """安装Python依赖"""
    print("📦 正在安装依赖包...")
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        print("✅ 依赖包安装成功")
    except subprocess.CalledProcessError:
        print("❌ 依赖包安装失败")
        sys.exit(1)

def setup_environment():
    """设置环境变量提示"""
    print("\n🔧 环境变量配置")
    print("请设置以下环境变量:")
    print("export EMAIL_USERNAME='你的QQ邮箱地址'")
    print("export EMAIL_PASSWORD='邮箱授权码'  # 注意：QQ邮箱需要授权码")
    print("\n或者运行以下命令创建.env文件:")
    print("echo 'EMAIL_USERNAME=你的QQ邮箱' > .env")
    print("echo 'EMAIL_PASSWORD=你的授权码' >> .env")

def test_run():
    """测试运行"""
    print("\n🧪 测试运行新闻收集...")
    try:
        subprocess.check_call([sys.executable, 'main.py'])
        print("✅ 测试运行成功")
    except subprocess.CalledProcessError:
        print("❌ 测试运行失败，请检查配置")

def main():
    print("🚀 AI新闻收集系统安装向导")
    print("=" * 40)

    # 安装依赖
    install_dependencies()

    # 显示配置说明
    setup_environment()

    # 询问是否进行测试运行
    test = input("\n是否立即进行测试运行？(y/n): ")
    if test.lower() == 'y':
        test_run()

    print("\n🎉 安装完成！")
    print("\n📋 后续步骤:")
    print("1. 配置邮箱环境变量")
    print("2. 运行 python main.py 测试")
    print("3. 配置GitHub仓库和Actions进行自动化")
    print("\n详细使用说明请参考 README.md")

if __name__ == "__main__":
    main()