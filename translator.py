#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
新闻翻译模块
使用免费的翻译API将英文新闻翻译为中文
"""

import requests
import json
import time
from typing import Dict, Optional

class NewsTranslator:
    def __init__(self):
        # 使用免费的翻译API（这里使用Google Translate的免费替代方案）
        self.translation_cache = {}

    def translate_text(self, text: str, target_lang: str = 'zh-CN') -> Optional[str]:
        """
        翻译文本到中文
        注意：这里使用简单的翻译方法，实际部署时建议使用付费API获得更好效果
        """
        if not text or len(text.strip()) == 0:
            return ""

        # 检查缓存
        cache_key = f"{text}_{target_lang}"
        if cache_key in self.translation_cache:
            return self.translation_cache[cache_key]

        try:
            # 使用免费的翻译API（示例使用MyMemory Translator）
            # 这是免费的，但有速率限制
            url = "https://api.mymemory.translated.net/get"

            # 准备请求参数
            params = {
                'q': text,
                'langpair': f'en|zh-CN'
            }

            response = requests.get(url, params=params, timeout=10)

            if response.status_code == 200:
                data = response.json()
                if 'responseData' in data and 'translatedText' in data['responseData']:
                    translated_text = data['responseData']['translatedText']
                    # 缓存翻译结果
                    self.translation_cache[cache_key] = translated_text
                    return translated_text

            # 如果API失败，返回原文
            print(f"翻译API调用失败，返回原文: {text[:50]}...")
            return text

        except Exception as e:
            print(f"翻译出错: {e}")
            # 出错时返回原文
            return text

    def translate_news_item(self, news_item: Dict) -> Dict:
        """翻译单个新闻项目"""
        translated_item = news_item.copy()

        # 翻译标题
        if 'title' in news_item:
            translated_item['title_zh'] = self.translate_text(news_item['title'])

        # 翻译摘要
        if 'summary' in news_item and news_item['summary']:
            # 只翻译前200字作为简要概述
            summary_preview = news_item['summary'][:200]
            translated_item['summary_zh'] = self.translate_text(summary_preview)
        else:
            translated_item['summary_zh'] = "暂无中文摘要"

        return translated_item

    def translate_news_batch(self, news_items: list) -> list:
        """批量翻译新闻"""
        translated_news = []

        for i, item in enumerate(news_items):
            print(f"正在翻译第 {i+1}/{len(news_items)} 条新闻...")

            # 添加延迟避免API限制
            if i > 0:
                time.sleep(1)

            translated_item = self.translate_news_item(item)
            translated_news.append(translated_item)

        return translated_news

def main():
    # 测试翻译功能
    translator = NewsTranslator()

    test_text = "OpenAI releases new GPT model with enhanced capabilities"
    translated = translator.translate_text(test_text)
    print(f"原文: {test_text}")
    print(f"译文: {translated}")

if __name__ == "__main__":
    main()