#!/usr/bin/env python3
"""
AI Daily Report - 深色科技风网格布局
"""
import os
import requests
from datetime import datetime

BRAVE_API_KEY = os.environ.get('BRAVE_API_KEY') or 'BSAm5_stG9BCZDHom2w9sMQxEziciB8'

def search_news(query, count=10):
    """使用 Brave Search API 搜索新闻"""
    if not BRAVE_API_KEY:
        return []
    
    url = "https://api.search.brave.com/res/v1/web/search"
    headers = {"Accept": "application/json", "X-Subscription-Token": BRAVE_API_KEY}
    params = {"q": query, "count": count}
    
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
        
        # 如果没结果，尝试备用查询
        if not results:
            alt_queries = {
                "股票 市场 财经": ["金融市场 新闻", "财经频道"],
                "global military news": ["military news today", "defense news"],
            }
            if query in alt_queries:
                for alt_q in alt_queries[query]:
                    params["q"] = alt_q
                    resp = requests.get(url, headers=headers, params=params, timeout=10)
                    data = resp.json()
                    for item in data.get("web", {}).get("results", []):
                        results.append({
                            "title": item.get("title", ""),
                            "desc": item.get("description", ""),
                            "url": item.get("url", "")
                        })
                    if results:
                        break
        
        return results
    except Exception as e:
        print(f"Search error: {e}")
        return []

def generate_report():
    """生成日报"""
    print("🔍 搜索AI科技新闻...")
    ai_results = search_news("AI 科技 最新新闻", 8)
    
    print("🔍 搜索金融新闻...")
    finance_results = search_news("股票 市场 财经", 8)
    
    print("🔍 搜索军事新闻...")
    military_results = search_news("global military news", 8)
    
    print("🔍 搜索国际经济新闻...")
    world_results = search_news("国际经济 最新", 8)
    
    # 如果API没返回数据，使用备用数据
    if not ai_results:
        ai_results = [
            {"title": "AI领域最新突破", "desc": "人工智能技术持续发展", "url": ""},
            {"title": "机器学习新进展", "desc": "深度学习算法优化", "url": ""},
            {"title": "AI应用场景拓展", "desc": "各行业AI应用深化", "url": ""},
        ]
    if not finance_results:
        finance_results = [
            {"title": "全球股市动态", "desc": "今日市场行情", "url": ""},
            {"title": "财经要闻", "desc": "最新财经资讯", "url": ""},
            {"title": "金融市场分析", "desc": "市场走势解读", "url": ""},
        ]
    if not military_results:
        military_results = [
            {"title": "国际军事局势", "desc": "全球军事动态", "url": ""},
            {"title": "地区安全形势", "desc": "国际安全热点", "url": ""},
        ]
    if not world_results:
        world_results = [
            {"title": "国际经济要闻", "desc": "全球经济动态", "url": ""},
            {"title": "国际贸易", "desc": "跨境贸易动态", "url": ""},
            {"title": "国际合作", "desc": "国际合作新进展", "url": ""},
        ]
    
    date_str = datetime.now().strftime('%Y年%m月%d日')
    time_str = datetime.now().strftime('%Y年%m月%d日 %H:%M')
    
    # 深色科技风网格布局
    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Daily Report - 每日要闻</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        
        :root {{
            --bg-dark: #0a0a0f;
            --bg-card: #12121a;
            --bg-card-hover: #1a1a25;
            --text-primary: #e0e0e0;
            --text-secondary: #8888aa;
            --text-muted: #555566;
            --neon-blue: #00d4ff;
            --neon-purple: #a855f7;
            --neon-pink: #ff0080;
            --neon-green: #00ff88;
            --neon-orange: #ff6b35;
            --border-glow: rgba(0, 212, 255, 0.3);
            --gradient-ai: linear-gradient(135deg, #00d4ff, #0066ff);
            --gradient-finance: linear-gradient(135deg, #ff6b35, #ffb347);
            --gradient-military: linear-gradient(135deg, #a855f7, #6366f1);
            --gradient-world: linear-gradient(135deg, #00ff88, #10b981);
        }}
        
        body {{
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, "PingFang SC", sans-serif;
            background: var(--bg-dark);
            color: var(--text-primary);
            line-height: 1.6;
            min-height: 100vh;
        }}
        
        /* 背景网格效果 */
        body::before {{
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: 
                linear-gradient(90deg, rgba(0,212,255,0.03) 1px, transparent 1px),
                linear-gradient(rgba(0,212,255,0.03) 1px, transparent 1px);
            background-size: 50px 50px;
            pointer-events: none;
            z-index: 0;
        }}
        
        /* 顶部导航 */
        .header {{
            background: rgba(10, 10, 15, 0.9);
            backdrop-filter: blur(20px);
            border-bottom: 1px solid rgba(0, 212, 255, 0.2);
            position: sticky;
            top: 0;
            z-index: 100;
        }}
        
        .header-inner {{
            max-width: 1400px;
            margin: 0 auto;
            height: 70px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0 30px;
        }}
        
        .logo {{
            font-size: 24px;
            font-weight: 700;
            background: var(--gradient-ai);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            text-shadow: 0 0 30px rgba(0, 212, 255, 0.5);
        }}
        
        .nav {{
            display: flex;
            gap: 8px;
        }}
        
        .nav a {{
            color: var(--text-secondary);
            text-decoration: none;
            padding: 10px 20px;
            border-radius: 8px;
            font-size: 14px;
            font-weight: 500;
            transition: all 0.3s ease;
            position: relative;
        }}
        
        .nav a:hover {{
            color: var(--neon-blue);
            background: rgba(0, 212, 255, 0.1);
        }}
        
        .theme-toggle {{
            background: rgba(255,255,255,0.05);
            border: 1px solid rgba(255,255,255,0.1);
            color: var(--text-primary);
            padding: 8px 16px;
            border-radius: 20px;
            cursor: pointer;
            font-size: 14px;
            transition: all 0.3s;
        }}
        
        .theme-toggle:hover {{
            background: rgba(0, 212, 255, 0.2);
            border-color: var(--neon-blue);
        }}
        
        /* 主容器 */
        .container {{
            max-width: 1400px;
            margin: 0 auto;
            padding: 40px 30px;
            position: relative;
            z-index: 1;
        }}
        
        /* 板块标题 */
        .section {{
            margin-bottom: 50px;
        }}
        
        .section-header {{
            display: flex;
            align-items: center;
            gap: 15px;
            margin-bottom: 25px;
            padding-bottom: 15px;
            border-bottom: 1px solid rgba(255,255,255,0.1);
        }}
        
        .section-icon {{
            width: 45px;
            height: 45px;
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 20px;
            font-weight: 700;
            color: #fff;
        }}
        
        .section-ai .section-icon {{ background: var(--gradient-ai); box-shadow: 0 0 20px rgba(0, 212, 255, 0.4); }}
        .section-finance .section-icon {{ background: var(--gradient-finance); box-shadow: 0 0 20px rgba(255, 107, 53, 0.4); }}
        .section-military .section-icon {{ background: var(--gradient-military); box-shadow: 0 0 20px rgba(168, 85, 247, 0.4); }}
        .section-world .section-icon {{ background: var(--gradient-world); box-shadow: 0 0 20px rgba(0, 255, 136, 0.4); }}
        
        .section-title {{
            font-size: 22px;
            font-weight: 600;
        }}
        
        .section-ai .section-title {{ color: var(--neon-blue); }}
        .section-finance .section-title {{ color: var(--neon-orange); }}
        .section-military .section-title {{ color: var(--neon-purple); }}
        .section-world .section-title {{ color: var(--neon-green); }}
        
        /* 网格布局 */
        .news-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
            gap: 20px;
        }}
        
        /* 新闻卡片 - 图文布局 */
        .news-card {{
            background: var(--bg-card);
            border-radius: 16px;
            border: 1px solid rgba(255,255,255,0.05);
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
            display: flex;
            flex-direction: column;
        }}
        
        .card-image {{
            width: 100%;
            height: 140px;
            object-fit: cover;
            background: linear-gradient(135deg, #1a1a2e, #2a2a4e);
        }}
        
        .card-content {{
            padding: 20px;
            flex: 1;
            display: flex;
            flex-direction: column;
        }}
        
        .news-card::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 3px;
            background: var(--neon-blue);
            opacity: 0;
            transition: opacity 0.3s;
        }}
        
        .news-card:hover {{
            transform: translateY(-5px);
            background: var(--bg-card-hover);
            border-color: rgba(0, 212, 255, 0.3);
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3), 0 0 30px rgba(0, 212, 255, 0.1);
        }}
        
        .news-card:hover::before {{
            opacity: 1;
        }}
        
        .section-finance .news-card::before {{ background: var(--neon-orange); }}
        .section-military .news-card::before {{ background: var(--neon-purple); }}
        .section-world .news-card::before {{ background: var(--neon-green); }}
        
        /* 卡片渐变背景和图标 - 主题相关 */
        .card-gradient-ai {{ background: linear-gradient(135deg, #1a1a2e 0%, #0f0f23 100%), url('https://images.unsplash.com/photo-1677442136019-21780ecad995?w=400'); background-size: cover; }}
        .card-gradient-finance {{ background: linear-gradient(135deg, #1a1a2e 0%, #0f0f23 100%), url('https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?w=400'); background-size: cover; }}
        .card-gradient-military {{ background: linear-gradient(135deg, #1a1a2e 0%, #0f0f23 100%), url('https://images.unsplash.com/photo-1533613220915-609f661a6fe1?w=400'); background-size: cover; }}
        .card-gradient-world {{ background: linear-gradient(135deg, #1a1a2e 0%, #0f0f23 100%), url('https://images.unsplash.com/photo-1526304640581-d334cdbbf45e?w=400'); background-size: cover; }}
        
        .card-icon {{
            font-size: 36px;
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100%;
            text-shadow: 0 2px 10px rgba(0,0,0,0.5);
        }}
        
        .card-tag {{
            display: inline-block;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 500;
            margin-bottom: 12px;
        }}
        
        .section-ai .card-tag {{ background: rgba(0, 212, 255, 0.2); color: var(--neon-blue); }}
        .section-finance .card-tag {{ background: rgba(255, 107, 53, 0.2); color: var(--neon-orange); }}
        .section-military .card-tag {{ background: rgba(168, 85, 247, 0.2); color: var(--neon-purple); }}
        .section-world .card-tag {{ background: rgba(0, 255, 136, 0.2); color: var(--neon-green); }}
        
        .card-title {{
            font-size: 16px;
            font-weight: 600;
            color: var(--text-primary);
            margin-bottom: 10px;
            line-height: 1.4;
        }}
        
        .card-desc {{
            font-size: 13px;
            color: var(--text-secondary);
            line-height: 1.6;
            margin-bottom: 15px;
        }}
        
        .card-footer {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 12px;
            color: var(--text-muted);
        }}
        
        .card-time {{
            display: flex;
            align-items: center;
            gap: 5px;
        }}
        
        /* 统计卡片 */
        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 20px;
            margin-bottom: 40px;
        }}
        
        .stat-card {{
            background: var(--bg-card);
            border-radius: 16px;
            padding: 25px;
            text-align: center;
            border: 1px solid rgba(255,255,255,0.05);
            position: relative;
            overflow: hidden;
        }}
        
        .stat-card::after {{
            content: '';
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            height: 3px;
        }}
        
        .stat-card:nth-child(1)::after {{ background: var(--neon-blue); }}
        .stat-card:nth-child(2)::after {{ background: var(--neon-orange); }}
        .stat-card:nth-child(3)::after {{ background: var(--neon-purple); }}
        .stat-card:nth-child(4)::after {{ background: var(--neon-green); }}
        
        .stat-number {{
            font-size: 36px;
            font-weight: 700;
            margin-bottom: 5px;
            font-family: 'JetBrains Mono', monospace;
        }}
        
        .stat-card:nth-child(1) .stat-number {{ color: var(--neon-blue); }}
        .stat-card:nth-child(2) .stat-number {{ color: var(--neon-orange); }}
        .stat-card:nth-child(3) .stat-number {{ color: var(--neon-purple); }}
        .stat-card:nth-child(4) .stat-number {{ color: var(--neon-green); }}
        
        .stat-label {{
            font-size: 14px;
            color: var(--text-secondary);
        }}
        
        /* 页脚 */
        .footer {{
            text-align: center;
            padding: 40px;
            color: var(--text-muted);
            font-size: 13px;
            border-top: 1px solid rgba(255,255,255,0.05);
            margin-top: 60px;
        }}
        
        .footer a {{
            color: var(--neon-blue);
            text-decoration: none;
        }}
        
        /* 响应式 */
        @media (max-width: 1200px) {{
            .stats-grid {{ grid-template-columns: repeat(2, 1fr); }}
        }}
        
        @media (max-width: 768px) {{
            .header-inner {{ padding: 0 15px; }}
            .nav {{ gap: 5px; }}
            .nav a {{ padding: 8px 12px; font-size: 13px; }}
            .container {{ padding: 20px 15px; }}
            .news-grid {{ grid-template-columns: 1fr; }}
            .stats-grid {{ grid-template-columns: 1fr; }}
        }}
    </style>
</head>
<body>
    <div class="header">
        <div class="header-inner">
            <div class="logo">⚡ AI Daily Report</div>
            <nav class="nav">
                <a href="#ai">🤖 AI科技最新动态</a>
                <a href="#finance">💰 全球股市行情</a>
                <a href="#military">🎯 国际军事要闻</a>
                <a href="#world">🌍 国际经济要闻</a>
            </nav>
            <button class="theme-toggle" onclick="toggleTheme()">🌙 深色</button>
        </div>
    </div>
    
    <div class="container">
        <!-- 统计卡片 -->
        <div class="stats-grid">
            <div class="stat-card">
                <div class="stat-number">{len(ai_results)}</div>
                <div class="stat-label">AI 科技</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">{len(finance_results)}</div>
                <div class="stat-label">股市财经</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">{len(military_results)}</div>
                <div class="stat-label">国际军事</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">{len(world_results)}</div>
                <div class="stat-label">国际经济</div>
            </div>
        </div>
        
        <!-- AI科技 -->
        <div class="section section-ai" id="ai">
            <div class="section-header">
                <div class="section-icon">AI</div>
                <div class="section-title">AI 科技最新动态</div>
            </div>
            <div class="news-grid">
'''
    
    for i, news in enumerate(ai_results[:10], 1):
        title = news.get('title', '无标题')[:50]
        desc = news.get('desc', '')[:100]
        # 根据类别选择不同的渐变背景
        bg_class = "card-gradient-blue" if i % 4 == 1 else ("card-gradient-purple" if i % 4 == 2 else ("card-gradient-orange" if i % 4 == 3 else "card-gradient-green"))
        html += f'''<div class="news-card">
                    <div class="card-image {bg_class}">
                        <span class="card-icon">🤖</span>
                    </div>
                    <div class="card-content">
                        <div class="card-tag">#{i}</div>
                        <div class="card-title">{title}</div>
                        <div class="card-desc">{desc}</div>
                        <div class="card-footer">
                            <span class="card-time">🕐 {date_str}</span>
                        </div>
                    </div>
                </div>'''
    
    html += '''</div>
        </div>
        
        <!-- 全球股市 -->
        <div class="section section-finance" id="finance">
            <div class="section-header">
                <div class="section-icon">$</div>
                <div class="section-title">全球股市行情</div>
            </div>
            <div class="news-grid">
'''
    
    for i, news in enumerate(finance_results[:10], 1):
        title = news.get('title', '无标题')[:50]
        desc = news.get('desc', '')[:100]
        bg_class = "card-gradient-orange" if i % 4 == 1 else ("card-gradient-blue" if i % 4 == 2 else ("card-gradient-green" if i % 4 == 3 else "card-gradient-purple"))
        html += f'''<div class="news-card">
                    <div class="card-image {bg_class}">
                        <span class="card-icon">💰</span>
                    </div>
                    <div class="card-content">
                        <div class="card-tag">#{i}</div>
                        <div class="card-title">{title}</div>
                        <div class="card-desc">{desc}</div>
                        <div class="card-footer">
                            <span class="card-time">🕐 {date_str}</span>
                        </div>
                    </div>
                </div>'''
    
    html += '''</div>
        </div>
        
        <!-- 国际军事 -->
        <div class="section section-military" id="military">
            <div class="section-header">
                <div class="section-icon">🎯</div>
                <div class="section-title">国际军事要闻</div>
            </div>
            <div class="news-grid">
'''
    
    for i, news in enumerate(military_results[:10], 1):
        title = news.get('title', '无标题')[:50]
        desc = news.get('desc', '')[:100]
        bg_class = "card-gradient-purple" if i % 4 == 1 else ("card-gradient-orange" if i % 4 == 2 else ("card-gradient-blue" if i % 4 == 3 else "card-gradient-green"))
        html += f'''<div class="news-card">
                    <div class="card-image {bg_class}">
                        <span class="card-icon">🎯</span>
                    </div>
                    <div class="card-content">
                        <div class="card-tag">#{i}</div>
                        <div class="card-title">{title}</div>
                        <div class="card-desc">{desc}</div>
                        <div class="card-footer">
                            <span class="card-time">🕐 {date_str}</span>
                        </div>
                    </div>
                </div>'''
    
    html += '''</div>
        </div>
        
        <!-- 国际经济 -->
        <div class="section section-world" id="world">
            <div class="section-header">
                <div class="section-icon">🌍</div>
                <div class="section-title">国际经济要闻</div>
            </div>
            <div class="news-grid>
'''
    
    for i, news in enumerate(world_results[:10], 1):
        title = news.get('title', '无标题')[:50]
        desc = news.get('desc', '')[:100]
        bg_class = "card-gradient-green" if i % 4 == 1 else ("card-gradient-purple" if i % 4 == 2 else ("card-gradient-orange" if i % 4 == 3 else "card-gradient-blue"))
        html += f'''<div class="news-card">
                    <div class="card-image {bg_class}">
                        <span class="card-icon">🌍</span>
                    </div>
                    <div class="card-content">
                        <div class="card-tag">#{i}</div>
                        <div class="card-title">{title}</div>
                        <div class="card-desc">{desc}</div>
                        <div class="card-footer">
                            <span class="card-time">🕐 {date_str}</span>
                        </div>
                    </div>
                </div>'''
    
    html += f'''</div>
        </div>
    </div>
    
    <div class="footer">
        <p>⚡ 由 AI 自动采集生成 | 更新时间: {time_str}</p>
        <p style="margin-top: 10px;">
            <a href="https://github.com/peterle-wh/ai-daily-report">GitHub</a> · 
            <a href="https://peterle-wh.github.io/ai-daily-report">Website</a>
        </p>
    </div>
    
    <script>
        function toggleTheme() {{
            alert('深色模式已启用！');
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
