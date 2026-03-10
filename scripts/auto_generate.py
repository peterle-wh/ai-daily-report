#!/usr/bin/env python3
"""
AI Daily Report - Brave Search API 自动采集
"""
import os
import json
import requests
from datetime import datetime

BRAVE_API_KEY = os.environ.get('BRAVE_API_KEY', '')

def search_news(query, count=10):
    """使用 Brave Search API 搜索新闻"""
    if not BRAVE_API_KEY:
        return []
    
    url = "https://api.search.brave.com/res/v1/web/search"
    headers = {
        "Accept": "application/json",
        "X-Subscription-Token": BRAVE_API_KEY
    }
    params = {
        "q": query,
        "count": count
    }
    
    try:
        resp = requests.get(url, headers=headers, params=params, timeout=10)
        data = resp.json()
        
        results = []
        for item in data.get("web", {}).get("results", []):
            results.append({
                "title": item.get("title", ""),
                "desc": item.get("description", ""),
                "url": item.get("url", "")
            })
        return results
    except Exception as e:
        print(f"Search error: {e}")
        return []

def generate_report():
    """生成日报"""
    print("🔍 搜索AI科技新闻...")
    ai_results = search_news("AI 科技 最新新闻", 10)
    
    print("🔍 搜索金融新闻...")
    finance_results = search_news("财经 股市 金融 最新", 10)
    
    print("🔍 搜索军事新闻...")
    military_results = search_news("国际军事 最新", 5)
    
    print("🔍 搜索国际经济新闻...")
    world_results = search_news("国际经济 最新", 10)
    
    # 如果API没返回数据，使用备用数据
    if not ai_results:
        ai_results = [{"title": "等待API采集...", "desc": "请配置BRAVE_API_KEY", "url": ""}]
    
    date_str = datetime.now().strftime('%Y年%m月%d日')
    time_str = datetime.now().strftime('%Y年%m月%d日 %H:%M')
    
    # 生成HTML
    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Daily Report - 每日要闻</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-primary: #f5f5f5;
            --bg-secondary: #fff;
            --text-primary: #333;
            --text-secondary: #666;
            --text-muted: #999;
            --border-color: #eee;
            --accent-red: #c0392b;
            --accent-orange: #f39c12;
            --accent-blue: #3498db;
            --accent-green: #27ae60;
            --tag-bg: #f5f5f5;
            --sidebar-bg: #fff;
        }}
        [data-theme="dark"] {{
            --bg-primary: #1a1a2e;
            --bg-secondary: #16213e;
            --text-primary: #e8e8e8;
            --text-secondary: #b0b0b0;
            --text-muted: #888;
            --border-color: #2a2a4a;
            --accent-red: #e74c3c;
            --accent-orange: #f5a623;
            --accent-blue: #4facfe;
            --accent-green: #27ae60;
            --tag-bg: #2a2a4a;
            --sidebar-bg: #16213e;
        }}
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "PingFang SC", sans-serif;
            background: var(--bg-primary);
            color: var(--text-primary);
            line-height: 1.6;
        }}
        .header {{
            background: linear-gradient(to right, var(--accent-red), #e74c3c);
            height: 60px;
            position: sticky;
            top: 0;
            z-index: 100;
        }}
        .header-inner {{
            max-width: 1200px;
            margin: 0 auto;
            height: 100%;
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0 20px;
        }}
        .logo {{
            color: #fff;
            font-size: 22px;
            font-weight: 700;
        }}
        .nav {{
            display: flex;
            gap: 20px;
        }}
        .nav a {{
            color: #fff;
            text-decoration: none;
            padding: 20px 0;
            border-bottom: 3px solid transparent;
            cursor: pointer;
        }}
        .nav a:hover {{
            border-bottom-color: #fff;
        }}
        .container {{
            max-width: 1200px;
            margin: 20px auto;
            padding: 0 20px;
            display: grid;
            grid-template-columns: 800px 1fr;
            gap: 20px;
        }}
        .main-content {{
            background: var(--bg-secondary);
            border-radius: 8px;
        }}
        .section {{
            border-bottom: 1px solid var(--border-color);
            padding: 20px;
        }}
        .section-header {{
            font-size: 20px;
            font-weight: 700;
            padding-bottom: 15px;
            margin-bottom: 15px;
            border-bottom: 2px solid;
        }}
        .section-ai {{ border-color: var(--accent-red); color: var(--accent-red); }}
        .section-finance {{ border-color: var(--accent-orange); color: var(--accent-orange); }}
        .section-military {{ border-color: var(--accent-green); color: var(--accent-green); }}
        .section-world {{ border-color: var(--accent-blue); color: var(--accent-blue); }}
        .news-item {{
            padding: 12px 0;
            border-bottom: 1px solid var(--border-color);
        }}
        .news-item:last-child {{ border: none; }}
        .news-title {{
            font-size: 15px;
            font-weight: 500;
            margin-bottom: 5px;
        }}
        .news-desc {{
            font-size: 13px;
            color: var(--text-secondary);
        }}
        .news-meta {{
            font-size: 12px;
            color: var(--text-muted);
            margin-top: 5px;
        }}
        .sidebar {{
            display: flex;
            flex-direction: column;
            gap: 20px;
        }}
        .sidebar-card {{
            background: var(--sidebar-bg);
            border-radius: 8px;
            padding: 20px;
        }}
        .sidebar-title {{
            font-size: 18px;
            font-weight: 700;
            padding-bottom: 12px;
            border-bottom: 2px solid var(--accent-red);
            margin-bottom: 15px;
        }}
        .footer {{
            text-align: center;
            padding: 30px;
            color: var(--text-muted);
        }}
    </style>
</head>
<body data-theme="light">
    <div class="header">
        <div class="header-inner">
            <div class="logo">AI Daily Report</div>
            <nav class="nav">
                <a href="#ai">AI科技</a>
                <a href="#finance">财经</a>
                <a href="#military">国际军事</a>
                <a href="#world">国际经济</a>
            </nav>
        </div>
    </div>
    
    <div class="container">
        <div class="main-content">
            <div class="section section-ai" id="ai">
                <div class="section-header">🤖 AI 科技今日热点</div>
'''
    
    for news in ai_results[:10]:
        html += f'''<div class="news-item">
            <div class="news-title">{news.get('title', '无标题')}</div>
            <div class="news-desc">{news.get('desc', '')[:100]}...</div>
        </div>'''
    
    html += '''</div>
            
            <div class="section section-finance" id="finance">
                <div class="section-header">💰 金融市场今日快讯</div>
'''
    
    for news in finance_results[:10]:
        html += f'''<div class="news-item">
            <div class="news-title">{news.get('title', '无标题')}</div>
            <div class="news-desc">{news.get('desc', '')[:100]}...</div>
        </div>'''
    
    html += '''</div>
            
            <div class="section section-military" id="military">
                <div class="section-header">🎯 国际军事要闻</div>
'''
    
    for news in military_results[:5]:
        html += f'''<div class="news-item">
            <div class="news-title">{news.get('title', '无标题')}</div>
            <div class="news-desc">{news.get('desc', '')[:100]}...</div>
        </div>'''
    
    html += '''</div>
            
            <div class="section section-world" id="world">
                <div class="section-header">📈 国际经济要闻</div>
'''
    
    for news in world_results[:10]:
        html += f'''<div class="news-item">
            <div class="news-title">{news.get('title', '无标题')}</div>
            <div class="news-desc">{news.get('desc', '')[:100]}...</div>
        </div>'''
    
    html += f'''</div>
        </div>
        
        <div class="sidebar">
            <div class="sidebar-card">
                <div class="sidebar-title">🔥 热门推荐</div>
                <div style="padding: 10px 0;">
                    <div style="padding: 8px 0;">1. AI 科技最新动态</div>
                    <div style="padding: 8px 0;">2. 全球股市行情</div>
                    <div style="padding: 8px 0;">3. 国际军事局势</div>
                </div>
            </div>
            <div class="sidebar-card">
                <div class="sidebar-title">📊 数据统计</div>
                <div style="padding: 10px 0; font-size: 14px;">
                    <div style="padding: 8px 0;">今日更新 <strong>35</strong> 条</div>
                </div>
            </div>
        </div>
    </div>
    
    <div class="footer">
        <p>由 AI 自动采集生成 | 更新时间: {time_str}</p>
        <p><a href="https://github.com/peterle-wh/ai-daily-report">GitHub</a></p>
    </div>
</body>
</html>'''
    
    os.makedirs('docs', exist_ok=True)
    with open('docs/index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"✅ Report generated: {date_str}")

if __name__ == '__main__':
    generate_report()
