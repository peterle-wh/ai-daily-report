#!/usr/bin/env python3
"""
AI Daily Report - Website Generator
生成静态网站
"""
import json
import os
from datetime import datetime
from jinja2 import Template

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Daily Report - {{ date }}</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { 
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            min-height: 100vh;
            color: #fff;
        }
        .container { max-width: 800px; margin: 0 auto; padding: 40px 20px; }
        header { 
            text-align: center; 
            margin-bottom: 40px;
            padding: 40px 0;
            border-bottom: 1px solid rgba(255,255,255,0.1);
        }
        h1 { 
            font-size: 2.5rem; 
            background: linear-gradient(135deg, #667eea, #764ba2);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 10px;
        }
        .date { color: rgba(255,255,255,0.6); font-size: 1rem; }
        .card {
            background: rgba(255,255,255,0.05);
            border-radius: 16px;
            padding: 30px;
            margin-bottom: 20px;
            border: 1px solid rgba(255,255,255,0.1);
        }
        .category {
            display: inline-block;
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 0.85rem;
            margin-bottom: 15px;
        }
        .category-ai { background: linear-gradient(135deg, #667eea, #764ba2); }
        .category-finance { background: linear-gradient(135deg, #f093fb, #f5576c); }
        .category-world { background: linear-gradient(135deg, #4facfe, #00f2fe); }
        .card h2 { font-size: 1.5rem; margin-bottom: 15px; }
        .news-list { list-style: none; }
        .news-list li {
            padding: 15px 0;
            border-bottom: 1px solid rgba(255,255,255,0.05);
        }
        .news-list li:last-child { border: none; }
        .news-title { font-size: 1.1rem; margin-bottom: 5px; }
        .news-meta { font-size: 0.85rem; color: rgba(255,255,255,0.5); }
        footer {
            text-align: center;
            padding: 40px 0;
            color: rgba(255,255,255,0.4);
            font-size: 0.9rem;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>🤖 AI Daily Report</h1>
            <p class="date">{{ date }} | 每日自动更新</p>
        </header>
        
        {% for category in categories %}
        <div class="card">
            <span class="category category-{{ category.category }}">{{ category.title }}</span>
            <ul class="news-list">
            {% for item in category.items %}
                <li>
                    <div class="news-title">{{ item.title }}</div>
                    <div class="news-meta">{{ item.source }} · {{ item.time }}</div>
                </li>
            {% endfor %}
            </ul>
        </div>
        {% endfor %}
        
        <footer>
            <p>由 OpenClaw AI 自动采集生成</p>
            <p>GitHub: peterle-wh/ai-daily-report</p>
        </footer>
    </div>
</body>
</html>
"""

def generate_website(date_str):
    # 读取数据
    try:
        with open(f"data/{date_str}.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        # 如果没有当天数据，使用示例
        data = {
            "date": date_str,
            "report": [
                {"category": "AI科技", "title": "AI领域今日热点", "items": [
                    {"title": "等待数据采集...", "source": "-", "time": date_str}
                ]},
                {"category": "金融", "title": "金融市场今日快讯", "items": [
                    {"title": "等待数据采集...", "source": "-", "time": date_str}
                ]},
                {"category": "国际", "title": "国际重要新闻", "items": [
                    {"title": "等待数据采集...", "source": "-", "time": date_str}
                ]},
            ]
        }
    
    # 生成网站
    template = Template(HTML_TEMPLATE)
    html = template.render(
        date=data["date"],
        categories=data["report"]
    )
    
    # 保存
    os.makedirs("docs", exist_ok=True)
    with open("docs/index.html", "w", encoding="utf-8") as f:
        f.write(html)
    
    print(f"✅ 网站生成完成: public/index.html")

if __name__ == "__main__":
    import sys
    date = sys.argv[1] if len(sys.argv) > 1 else datetime.now().strftime("%Y-%m-%d")
    generate_website(date)
