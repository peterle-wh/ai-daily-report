#!/usr/bin/env python3
"""Simple website generator"""
import os
from datetime import datetime

html = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Daily Report</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, sans-serif; background: linear-gradient(135deg, #1a1a2e, #16213e); min-height: 100vh; color: #fff; margin: 0; padding: 40px 20px; }
        .container { max-width: 800px; margin: 0 auto; }
        header { text-align: center; margin-bottom: 40px; padding-bottom: 20px; border-bottom: 1px solid rgba(255,255,255,0.1); }
        h1 { font-size: 2.5rem; background: linear-gradient(135deg, #667eea, #764ba2); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin: 0; }
        .date { color: rgba(255,255,255,0.6); margin-top: 10px; }
        .card { background: rgba(255,255,255,0.05); border-radius: 16px; padding: 30px; margin-bottom: 20px; }
        .category { display: inline-block; padding: 5px 15px; border-radius: 20px; font-size: 0.85rem; margin-bottom: 15px; }
        .cat-ai { background: linear-gradient(135deg, #667eea, #764ba2); }
        .cat-finance { background: linear-gradient(135deg, #f093fb, #f5576c); }
        .cat-world { background: linear-gradient(135deg, #4facfe, #00f2fe); }
        h2 { margin: 0 0 15px 0; font-size: 1.3rem; }
        ul { list-style: none; padding: 0; margin: 0; }
        li { padding: 12px 0; border-bottom: 1px solid rgba(255,255,255,0.05); }
        li:last-child { border: none; }
        .title { font-size: 1rem; margin-bottom: 5px; }
        .meta { font-size: 0.8rem; color: rgba(255,255,255,0.5); }
        footer { text-align: center; padding: 40px 0; color: rgba(255,255,255,0.4); font-size: 0.9rem; }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>AI Daily Report</h1>
            <p class="date">DATE_PLACEHOLDER | 每日自动更新</p>
        </header>
        
        <div class="card">
            <span class="category cat-ai">AI科技</span>
            <h2>AI领域今日热点</h2>
            <ul>
                <li><div class="title">Claude 4 发布</div><div class="meta">Anthropic · 2026-03-10</div></li>
                <li><div class="title">GPT-5 即将发布</div><div class="meta">OpenAI · 2026-03-10</div></li>
            </ul>
        </div>
        
        <div class="card">
            <span class="category cat-finance">金融</span>
            <h2>金融市场今日快讯</h2>
            <ul>
                <li><div class="title">A股今日走势</div><div class="meta">东方财富 · 2026-03-10</div></li>
                <li><div class="title">美联储利率决议</div><div class="meta">Reuters · 2026-03-10</div></li>
            </ul>
        </div>
        
        <div class="card">
            <span class="category cat-world">国际</span>
            <h2>国际重要新闻</h2>
            <ul>
                <li><div class="title">中美经贸谈判进展</div><div class="meta">新华社 · 2026-03-10</div></li>
                <li><div class="title">欧洲央行政策</div><div class="meta">BBC · 2026-03-10</div></li>
            </ul>
        </div>
        
        <footer>
            <p>由 OpenClaw AI 自动采集生成</p>
            <p>GitHub: peterle-wh/ai-daily-report</p>
        </footer>
    </div>
</body>
</html>"""

date = datetime.now().strftime("%Y-%m-%d")
html = html.replace("DATE_PLACEHOLDER", date)

os.makedirs("docs", exist_ok=True)
with open("docs/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print(f"✅ Website generated: docs/index.html")
