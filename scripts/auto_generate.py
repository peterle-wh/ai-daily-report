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
    
    # 生成HTML - 完整版带主题切换
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
            transition: all 0.3s ease;
        }}
        .header {{
            background: linear-gradient(to right, var(--accent-red), #e74c3c);
            height: 60px;
            position: sticky;
            top: 0;
            z-index: 100;
            box-shadow: 0 2px 8px rgba(0,0,0,0.15);
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
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        .logo-icon {{
            width: 36px;
            height: 36px;
            background: rgba(255,255,255,0.2);
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 18px;
        }}
        .header-right {{
            display: flex;
            align-items: center;
            gap: 20px;
        }}
        .nav {{
            display: flex;
            gap: 25px;
        }}
        .nav a {{
            color: rgba(255,255,255,0.9);
            text-decoration: none;
            font-size: 15px;
            padding: 18px 0;
            border-bottom: 3px solid transparent;
            transition: all 0.3s;
            cursor: pointer;
        }}
        .nav a:hover, .nav a.active {{
            border-bottom-color: #fff;
        }}
        .theme-toggle {{
            background: rgba(255,255,255,0.2);
            border: none;
            color: #fff;
            padding: 8px 16px;
            border-radius: 20px;
            cursor: pointer;
            font-size: 14px;
            display: flex;
            align-items: center;
            gap: 6px;
        }}
        .container {{
            max-width: 1200px;
            margin: 20px auto;
            padding: 0 20px;
            display: grid;
            grid-template-columns: 800px 370px;
            gap: 20px;
        }}
        .main-content {{
            background: var(--bg-secondary);
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }}
        .section {{
            border-bottom: 1px solid var(--border-color);
        }}
        .section:last-child {{
            border-bottom: none;
        }}
        .section-header {{
            display: flex;
            align-items: center;
            padding: 16px 20px;
            border-bottom: 2px solid;
        }}
        .section-ai {{ border-color: var(--accent-red); }}
        .section-finance {{ border-color: var(--accent-orange); }}
        .section-military {{ border-color: var(--accent-green); }}
        .section-world {{ border-color: var(--accent-blue); }}
        .section-title {{
            font-size: 20px;
            font-weight: 700;
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        .section-ai .section-title {{ color: var(--accent-red); }}
        .section-finance .section-title {{ color: var(--accent-orange); }}
        .section-military .section-title {{ color: var(--accent-green); }}
        .section-world .section-title {{ color: var(--accent-blue); }}
        .section-title-icon {{
            width: 28px;
            height: 28px;
            border-radius: 6px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #fff;
            font-size: 14px;
        }}
        .section-ai .section-title-icon {{ background: var(--accent-red); }}
        .section-finance .section-title-icon {{ background: var(--accent-orange); }}
        .section-military .section-title-icon {{ background: var(--accent-green); }}
        .section-world .section-title-icon {{ background: var(--accent-blue); }}
        .news-list {{
            padding: 10px 20px 20px;
        }}
        .news-item {{
            padding: 14px 0;
            border-bottom: 1px solid var(--border-color);
            cursor: pointer;
            transition: all 0.3s;
        }}
        .news-item:hover {{
            background: var(--tag-bg);
            margin: 0 -10px;
            padding: 14px 10px;
            border-radius: 6px;
        }}
        .news-item:last-child {{
            border-bottom: none;
        }}
        .news-title {{
            font-size: 15px;
            color: var(--text-primary);
            font-weight: 500;
            margin-bottom: 6px;
            line-height: 1.4;
        }}
        .news-title:hover {{
            color: var(--accent-red);
        }}
        .news-desc {{
            font-size: 13px;
            color: var(--text-secondary);
            line-height: 1.5;
            margin-bottom: 8px;
        }}
        .news-meta {{
            font-size: 12px;
            color: var(--text-muted);
            display: flex;
            align-items: center;
            gap: 10px;
        }}
        .source {{
            color: var(--text-secondary);
            background: var(--tag-bg);
            padding: 2px 8px;
            border-radius: 3px;
        }}
        .tag {{
            color: var(--tag-text);
            background: var(--tag-bg);
            padding: 2px 8px;
            border-radius: 3px;
        }}
        .tag-text {{ color: var(--accent-red); }}
        .sidebar {{
            display: flex;
            flex-direction: column;
            gap: 20px;
        }}
        .sidebar-card {{
            background: var(--sidebar-bg);
            border-radius: 8px;
            padding: 20px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }}
        .sidebar-title {{
            font-size: 18px;
            font-weight: 700;
            padding-bottom: 12px;
            border-bottom: 2px solid var(--accent-red);
            margin-bottom: 16px;
        }}
        .hot-list {{
            list-style: none;
        }}
        .hot-item {{
            display: flex;
            align-items: flex-start;
            padding: 10px 0;
            border-bottom: 1px solid var(--border-color);
            gap: 12px;
            cursor: pointer;
        }}
        .hot-item:hover .hot-title {{
            color: var(--accent-red);
        }}
        .hot-rank {{
            width: 22px;
            height: 22px;
            background: var(--accent-red);
            color: #fff;
            border-radius: 4px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 12px;
            font-weight: 700;
            flex-shrink: 0;
        }}
        .hot-rank.top3 {{
            background: #e74c3c;
        }}
        .hot-title {{
            font-size: 13px;
            color: var(--text-primary);
            line-height: 1.4;
        }}
        .footer {{
            background: var(--bg-secondary);
            color: var(--text-muted);
            padding: 30px 20px;
            text-align: center;
            margin-top: 40px;
            border-top: 1px solid var(--border-color);
        }}
        .footer a {{
            color: var(--accent-blue);
            text-decoration: none;
        }}
        @media (max-width: 1200px) {{
            .container {{
                grid-template-columns: 1fr;
            }}
            .sidebar {{
                display: none;
            }}
        }}
    </style>
</head>
<body data-theme="light" id="top">
    <div class="header">
        <div class="header-inner">
            <div class="logo">
                <div class="logo-icon">AI</div>
                <span>AI Daily Report</span>
            </div>
            <div class="header-right">
                <nav class="nav">
                    <a href="#top" onclick="window.scrollTo({{top:0,behavior:'smooth'}})">首页</a>
                    <a href="#ai" onclick="document.getElementById('ai').scrollIntoView({{behavior:'smooth'}})">AI科技</a>
                    <a href="#finance" onclick="document.getElementById('finance').scrollIntoView({{behavior:'smooth'}})">财经</a>
                    <a href="#military" onclick="document.getElementById('military').scrollIntoView({{behavior:'smooth'}})">国际军事</a>
                    <a href="#world" onclick="document.getElementById('world').scrollIntoView({{behavior:'smooth'}})">国际经济</a>
                </nav>
                <button class="theme-toggle" onclick="toggleTheme()">
                    <span id="theme-icon">🌙</span>
                    <span id="theme-text">深色</span>
                </button>
            </div>
        </div>
    </div>
    
    <div class="container">
        <div class="main-content">
            <!-- AI科技 -->
            <div class="section section-ai" id="ai">
                <div class="section-header">
                    <div class="section-title">
                        <div class="section-title-icon">AI</div>
                        AI 科技最新动态
                    </div>
                </div>
                <div class="news-list">
'''
    
    for news in ai_results[:10]:
        title = news.get('title', '无标题')[:60]
        desc = news.get('desc', '')[:100]
        html += f'''<div class="news-item">
                        <div class="news-title">{title}</div>
                        <div class="news-desc">{desc}</div>
                        <div class="news-meta">今天</div>
                    </div>'''
    
    html += '''</div>
            </div>
            
            <!-- 金融市场 -->
            <div class="section section-finance" id="finance">
                <div class="section-header">
                    <div class="section-title">
                        <div class="section-title-icon">$</div>
                        全球股市行情
                    </div>
                </div>
                <div class="news-list">
'''
    
    for news in finance_results[:10]:
        title = news.get('title', '无标题')[:60]
        desc = news.get('desc', '')[:100]
        html += f'''<div class="news-item">
                        <div class="news-title">{title}</div>
                        <div class="news-desc">{desc}</div>
                        <div class="news-meta">今天</div>
                    </div>'''
    
    html += '''</div>
            </div>
            
            <!-- 国际军事 -->
            <div class="section section-military" id="military">
                <div class="section-header">
                    <div class="section-title">
                        <div class="section-title-icon">军</div>
                        国际军事要闻
                    </div>
                </div>
                <div class="news-list">
'''
    
    for news in military_results[:5]:
        title = news.get('title', '无标题')[:60]
        desc = news.get('desc', '')[:100]
        html += f'''<div class="news-item">
                        <div class="news-title">{title}</div>
                        <div class="news-desc">{desc}</div>
                        <div class="news-meta">今天</div>
                    </div>'''
    
    html += '''</div>
            </div>
            
            <!-- 国际经济 -->
            <div class="section section-world" id="world">
                <div class="section-header">
                    <div class="section-title">
                        <div class="section-title-icon">G</div>
                        国际经济要闻
                    </div>
                </div>
                <div class="news-list">
'''
    
    for news in world_results[:10]:
        title = news.get('title', '无标题')[:60]
        desc = news.get('desc', '')[:100]
        html += f'''<div class="news-item">
                        <div class="news-title">{title}</div>
                        <div class="news-desc">{desc}</div>
                        <div class="news-meta">今天</div>
                    </div>'''
    
    html += f'''</div>
            </div>
        </div>
        
        <!-- Sidebar -->
        <div class="sidebar">
            <div class="sidebar-card">
                <div class="sidebar-title">🔥 热门推荐</div>
                <ul class="hot-list">
'''
    
    # 热门推荐
    for i, news in enumerate(ai_results[:5], 1):
        title = news.get('title', '无标题')[:30]
        top_class = "top3" if i <= 3 else ""
        html += f'''<li class="hot-item">
                        <div class="hot-rank {top_class}">{i}</div>
                        <div class="hot-title">{title}</div>
                    </li>'''
    
    html += '''</ul>
            </div>
            
            <div class="sidebar-card">
                <div class="sidebar-title">📊 数据统计</div>
                <div style="padding: 10px 0; font-size: 14px; color: var(--text-secondary);">
                    <div style="padding: 8px 0; border-bottom: 1px solid var(--border-color);">
                        今日更新 <strong style="color: var(--accent-red);">''' + str(len(ai_results) + len(finance_results) + len(military_results) + len(world_results)) + '''</strong> 条新闻
                    </div>
                    <div style="padding: 8px 0; border-bottom: 1px solid var(--border-color);">
                        AI科技 <strong>''' + str(len(ai_results)) + '''</strong> 条
                    </div>
                    <div style="padding: 8px 0; border-bottom: 1px solid var(--border-color);">
                        金融市场 <strong>''' + str(len(finance_results)) + '''</strong> 条
                    </div>
                    <div style="padding: 8px 0; border-bottom: 1px solid var(--border-color);">
                        国际军事 <strong>''' + str(len(military_results)) + '''</strong> 条
                    </div>
                    <div style="padding: 8px 0;">
                        国际经济 <strong>''' + str(len(world_results)) + '''</strong> 条
                    </div>
                </div>
            </div>
        </div>
    </div>
    
    <div class="footer">
        <p>由 OpenClaw AI 自动采集生成 | 更新时间: ''' + time_str + '''</p>
        <p style="margin-top: 10px;">
            <a href="https://github.com/peterle-wh/ai-daily-report" target="_blank">GitHub</a> · 
            <a href="https://peterle-wh.github.io/ai-daily-report" target="_blank">Website</a>
        </p>
    </div>
    
    <script>
        function toggleTheme() {{
            const body = document.body;
            const icon = document.getElementById('theme-icon');
            const text = document.getElementById('theme-text');
            
            if (body.getAttribute('data-theme') === 'light') {{
                body.setAttribute('data-theme', 'dark');
                icon.textContent = '☀️';
                text.textContent = '浅色';
                localStorage.setItem('theme', 'dark');
            }} else {{
                body.setAttribute('data-theme', 'light');
                icon.textContent = '🌙';
                text.textContent = '深色';
                localStorage.setItem('theme', 'light');
            }}
        }}
        
        const savedTheme = localStorage.getItem('theme') || 'light';
        document.body.setAttribute('data-theme', savedTheme);
        if (savedTheme === 'dark') {{
            document.getElementById('theme-icon').textContent = '☀️';
            document.getElementById('theme-text').textContent = '浅色';
        }}
    </script>
</body>
</html>'''
    
    os.makedirs('docs', exist_ok=True)
    with open('docs/index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"✅ Report generated: {date_str}")

if __name__ == '__main__':
    generate_report()
