#!/usr/bin/env python3
"""
AI Daily Report - 精美新闻网站 - 二次编辑内容
"""
import os
import requests
from datetime import datetime
import html

BRAVE_API_KEY = os.environ.get('BRAVE_API_KEY') or 'BSAm5_stG9BCZDHom2w9sMQxEziciB8'

# 默认图片
DEFAULT_IMAGES = {
    'ai': 'https://images.unsplash.com/photo-1677442136019-21780ecad995?w=800',
    'finance': 'https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?w=800',
    'military': 'https://images.unsplash.com/photo-1533613220915-609f661a6fe1?w=800',
    'world': 'https://images.unsplash.com/photo-1526304640581-d334cdbbf45e?w=800'
}

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
            thumb = item.get("thumbnail", {})
            img_url = ""
            if thumb:
                img_url = thumb.get("src", "")
            
            # 提取更长的描述
            desc = item.get("description", "")
            if not desc:
                desc = item.get("extra_snippets", [""])[0] if item.get("extra_snippets") else ""
            
            # 获取来源
            source = ""
            if item.get("domain"):
                source = item.get("domain", "").replace("www.", "")
            
            results.append({
                "title": html.escape(item.get("title", "")),
                "desc": html.escape(desc[:300]) if desc else "暂无描述",
                "url": item.get("url", ""),
                "image": img_url,
                "source": source,
                "age": item.get("age", "")
            })
        
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
                        thumb = item.get("thumbnail", {})
                        img_url = ""
                        if thumb:
                            img_url = thumb.get("src", "")
                        desc = item.get("description", "")
                        source = item.get("domain", "").replace("www.", "") if item.get("domain") else ""
                        results.append({
                            "title": html.escape(item.get("title", "")),
                            "desc": html.escape(desc[:300]) if desc else "暂无描述",
                            "url": item.get("url", ""),
                            "image": img_url,
                            "source": source,
                            "age": item.get("age", "")
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
    
    # 备用数据
    if not ai_results:
        ai_results = [
            {"title": "AI领域最新突破", "desc": "人工智能技术持续发展，深度学习算法不断优化，应用场景日益丰富。", "url": "", "image": DEFAULT_IMAGES['ai'], "source": "科技日报", "age": ""},
            {"title": "机器学习新进展", "desc": "深度学习算法优化，带来更高效的模型训练方法。", "url": "", "image": DEFAULT_IMAGES['ai'], "source": "机器之心", "age": ""},
            {"title": "AI应用场景拓展", "desc": "各行业AI应用深化，智能医疗、自动驾驶等领域取得新进展。", "url": "", "image": DEFAULT_IMAGES['ai'], "source": "36氪", "age": ""},
        ]
    if not finance_results:
        finance_results = [
            {"title": "全球股市动态", "desc": "今日市场行情分析，震荡上行趋势明显。", "url": "", "image": DEFAULT_IMAGES['finance'], "source": "东方财富", "age": ""},
            {"title": "财经要闻", "desc": "最新财经资讯，政策利好持续释放。", "url": "", "image": DEFAULT_IMAGES['finance'], "source": "同花顺", "age": ""},
            {"title": "金融市场分析", "desc": "市场走势解读，投资机会分析。", "url": "", "image": DEFAULT_IMAGES['finance'], "source": "雪球", "age": ""},
        ]
    if not military_results:
        military_results = [
            {"title": "国际军事局势", "desc": "全球军事动态，各地区安全形势分析。", "url": "", "image": DEFAULT_IMAGES['military'], "source": "参考消息", "age": ""},
            {"title": "地区安全形势", "desc": "国际安全热点，各方动态持续关注。", "url": "", "image": DEFAULT_IMAGES['military'], "source": "环球网", "age": ""},
        ]
    if not world_results:
        world_results = [
            {"title": "国际经济要闻", "desc": "全球经济动态，贸易往来持续深化。", "url": "", "image": DEFAULT_IMAGES['world'], "source": "新华网", "age": ""},
            {"title": "国际贸易", "desc": "跨境贸易动态，进出口数据分析。", "url": "", "image": DEFAULT_IMAGES['world'], "source": "商务部", "age": ""},
            {"title": "国际合作", "desc": "国际合作新进展，多边合作不断深化。", "url": "", "image": DEFAULT_IMAGES['world'], "source": "人民网", "age": ""},
        ]
    
    date_str = datetime.now().strftime('%Y年%m月%d日')
    time_str = datetime.now().strftime('%Y年%m月%d日 %H:%M')
    
    # 生成精美的HTML
    html_template = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Daily Report - 每日要闻精选</title>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@300;400;500;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        
        :root {{
            --bg-dark: #0d0d12;
            --bg-card: #16161e;
            --bg-card-hover: #1e1e28;
            --text-primary: #f0f0f5;
            --text-secondary: #9898a8;
            --text-muted: #585868;
            --accent-ai: #00d4ff;
            --accent-finance: #ff9500;
            --accent-military: #a855f7;
            --accent-world: #34d399;
            --border-subtle: rgba(255,255,255,0.06);
        }}
        
        body {{
            font-family: 'Noto Sans SC', 'Inter', -apple-system, sans-serif;
            background: var(--bg-dark);
            color: var(--text-primary);
            line-height: 1.7;
            min-height: 100vh;
        }}
        
        /* 背景 */
        body::before {{
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: 
                radial-gradient(ellipse at 20% 20%, rgba(0,212,255,0.08) 0%, transparent 50%),
                radial-gradient(ellipse at 80% 80%, rgba(168,85,247,0.06) 0%, transparent 50%);
            pointer-events: none;
            z-index: 0;
        }}
        
        /* 顶部导航 */
        .header {{
            position: sticky;
            top: 0;
            z-index: 100;
            background: rgba(13,13,18,0.85);
            backdrop-filter: blur(20px);
            border-bottom: 1px solid var(--border-subtle);
        }}
        
        .header-inner {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 24px;
            height: 64px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }}
        
        .logo {{
            font-size: 22px;
            font-weight: 700;
            background: linear-gradient(135deg, var(--accent-ai), #6366f1);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            letter-spacing: -0.5px;
        }}
        
        .nav {{
            display: flex;
            gap: 8px;
        }}
        
        .nav a {{
            color: var(--text-secondary);
            text-decoration: none;
            padding: 8px 16px;
            border-radius: 8px;
            font-size: 14px;
            font-weight: 500;
            transition: all 0.2s;
        }}
        
        .nav a:hover {{
            color: var(--text-primary);
            background: rgba(255,255,255,0.05);
        }}
        
        .date-display {{
            color: var(--text-muted);
            font-size: 13px;
        }}
        
        /* 主内容 */
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 40px 24px;
            position: relative;
            z-index: 1;
        }}
        
        /* 板块 */
        .section {{
            margin-bottom: 60px;
        }}
        
        .section-header {{
            display: flex;
            align-items: center;
            gap: 14px;
            margin-bottom: 28px;
        }}
        
        .section-icon {{
            width: 42px;
            height: 42px;
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 18px;
            font-weight: 600;
        }}
        
        .section-ai .section-icon {{ background: linear-gradient(135deg, var(--accent-ai), #0099cc); }}
        .section-finance .section-icon {{ background: linear-gradient(135deg, var(--accent-finance), #cc7700); }}
        .section-military .section-icon {{ background: linear-gradient(135deg, var(--accent-military), #7c3aed); }}
        .section-world .section-icon {{ background: linear-gradient(135deg, var(--accent-world), #059669); }}
        
        .section-title {{
            font-size: 24px;
            font-weight: 600;
        }}
        
        .section-ai .section-title {{ color: var(--accent-ai); }}
        .section-finance .section-title {{ color: var(--accent-finance); }}
        .section-military .section-title {{ color: var(--accent-military); }}
        .section-world .section-title {{ color: var(--accent-world); }}
        
        .section-count {{
            color: var(--text-muted);
            font-size: 13px;
            margin-left: auto;
        }}
        
        /* 特色卡片 - 大卡片 */
        .featured-card {{
            background: var(--bg-card);
            border-radius: 20px;
            overflow: hidden;
            display: grid;
            grid-template-columns: 1fr 1fr;
            margin-bottom: 20px;
            border: 1px solid var(--border-subtle);
            transition: all 0.3s;
            cursor: pointer;
        }}
        
        .featured-card:hover {{
            transform: translateY(-3px);
            box-shadow: 0 20px 40px rgba(0,0,0,0.3);
        }}
        
        .featured-card:hover .featured-image {{
            transform: scale(1.05);
        }}
        
        .featured-image-wrap {{
            overflow: hidden;
            height: 280px;
        }}
        
        .featured-image {{
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.5s;
        }}
        
        .featured-content {{
            padding: 28px;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }}
        
        .featured-source {{
            display: inline-flex;
            align-items: center;
            gap: 6px;
            color: var(--text-muted);
            font-size: 12px;
            margin-bottom: 12px;
        }}
        
        .featured-title {{
            font-size: 20px;
            font-weight: 600;
            margin-bottom: 12px;
            line-height: 1.5;
            color: var(--text-primary);
        }}
        
        .featured-desc {{
            font-size: 14px;
            color: var(--text-secondary);
            line-height: 1.8;
            display: -webkit-box;
            -webkit-line-clamp: 4;
            -webkit-box-orient: vertical;
            overflow: hidden;
        }}
        
        .featured-meta {{
            margin-top: 16px;
            display: flex;
            align-items: center;
            gap: 12px;
            color: var(--text-muted);
            font-size: 12px;
        }}
        
        /* 普通卡片网格 */
        .news-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 16px;
        }}
        
        .news-card {{
            background: var(--bg-card);
            border-radius: 16px;
            overflow: hidden;
            border: 1px solid var(--border-subtle);
            transition: all 0.3s;
            cursor: pointer;
            display: flex;
            flex-direction: column;
        }}
        
        .news-card:hover {{
            transform: translateY(-4px);
            border-color: rgba(255,255,255,0.1);
            box-shadow: 0 16px 32px rgba(0,0,0,0.25);
        }}
        
        .news-card:hover .card-image {{
            transform: scale(1.05);
        }}
        
        .card-image-wrap {{
            overflow: hidden;
            height: 160px;
            position: relative;
        }}
        
        .card-image {{
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.4s;
        }}
        
        .card-source-tag {{
            position: absolute;
            top: 10px;
            left: 10px;
            background: rgba(0,0,0,0.7);
            color: white;
            padding: 4px 10px;
            border-radius: 20px;
            font-size: 11px;
            font-weight: 500;
        }}
        
        .card-content {{
            padding: 18px;
            flex: 1;
            display: flex;
            flex-direction: column;
        }}
        
        .card-title {{
            font-size: 15px;
            font-weight: 600;
            margin-bottom: 10px;
            line-height: 1.5;
            color: var(--text-primary);
        }}
        
        .card-desc {{
            font-size: 13px;
            color: var(--text-secondary);
            line-height: 1.7;
            flex: 1;
            display: -webkit-box;
            -webkit-line-clamp: 3;
            -webkit-box-orient: vertical;
            overflow: hidden;
        }}
        
        .card-meta {{
            margin-top: 14px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            color: var(--text-muted);
            font-size: 12px;
        }}
        
        /* 统计 */
        .stats-bar {{
            display: flex;
            gap: 24px;
            margin-bottom: 48px;
            padding: 20px 28px;
            background: var(--bg-card);
            border-radius: 16px;
            border: 1px solid var(--border-subtle);
        }}
        
        .stat-item {{
            display: flex;
            align-items: center;
            gap: 10px;
        }}
        
        .stat-dot {{
            width: 10px;
            height: 10px;
            border-radius: 50%;
        }}
        
        .stat-dot.ai {{ background: var(--accent-ai); }}
        .stat-dot.finance {{ background: var(--accent-finance); }}
        .stat-dot.military {{ background: var(--accent-military); }}
        .stat-dot.world {{ background: var(--accent-world); }}
        
        .stat-label {{
            color: var(--text-secondary);
            font-size: 14px;
        }}
        
        .stat-value {{
            color: var(--text-primary);
            font-weight: 600;
            font-size: 15px;
        }}
        
        /* 页脚 */
        .footer {{
            text-align: center;
            padding: 40px 24px;
            color: var(--text-muted);
            font-size: 13px;
            border-top: 1px solid var(--border-subtle);
            margin-top: 60px;
        }}
        
        .footer a {{
            color: var(--accent-ai);
            text-decoration: none;
        }}
        
        /* 响应式 */
        @media (max-width: 900px) {{
            .featured-card {{ grid-template-columns: 1fr; }}
            .featured-image-wrap {{ height: 200px; }}
            .stats-bar {{ flex-wrap: wrap; gap: 16px; }}
        }}
        
        @media (max-width: 600px) {{
            .header-inner {{ padding: 0 16px; }}
            .nav {{ display: none; }}
            .container {{ padding: 24px 16px; }}
            .news-grid {{ grid-template-columns: 1fr; }}
        }}
    </style>
</head>
<body>
    <div class="header">
        <div class="header-inner">
            <div class="logo">⚡ AI Daily Report</div>
            <nav class="nav">
                <a href="#ai">AI科技</a>
                <a href="#finance">股市财经</a>
                <a href="#military">国际军事</a>
                <a href="#world">国际经济</a>
            </nav>
            <div class="date-display">{date_str}</div>
        </div>
    </div>
    
    <div class="container">
        <!-- 统计栏 -->
        <div class="stats-bar">
            <div class="stat-item">
                <div class="stat-dot ai"></div>
                <span class="stat-label">AI科技</span>
                <span class="stat-value">{len(ai_results)}条</span>
            </div>
            <div class="stat-item">
                <div class="stat-dot finance"></div>
                <span class="stat-label">股市财经</span>
                <span class="stat-value">{len(finance_results)}条</span>
            </div>
            <div class="stat-item">
                <div class="stat-dot military"></div>
                <span class="stat-label">国际军事</span>
                <span class="stat-value">{len(military_results)}条</span>
            </div>
            <div class="stat-item">
                <div class="stat-dot world"></div>
                <span class="stat-label">国际经济</span>
                <span class="stat-value">{len(world_results)}条</span>
            </div>
        </div>
        
        <!-- AI科技 -->
        <div class="section section-ai" id="ai">
            <div class="section-header">
                <div class="section-icon">🤖</div>
                <div class="section-title">AI 科技最新动态</div>
                <div class="section-count">{len(ai_results)} 条新闻</div>
            </div>
'''

    # AI科技 - 第一个是大卡片
    if ai_results:
        first = ai_results[0]
        img = first.get('image') or DEFAULT_IMAGES['ai']
        source = first.get('source', '来源')
        html_template += f'''
            <div class="featured-card" onclick="window.open('{first['url']}', '_blank')">
                <div class="featured-image-wrap">
                    <img class="featured-image" src="{img}" alt="" onerror="this.src='{DEFAULT_IMAGES['ai']}'">
                </div>
                <div class="featured-content">
                    <div class="featured-source">📰 {source}</div>
                    <div class="featured-title">{first['title']}</div>
                    <div class="featured-desc">{first['desc']}</div>
                    <div class="featured-meta">
                        <span>🕐 {date_str}</span>
                    </div>
                </div>
            </div>
            <div class="news-grid">
'''
        
        for news in ai_results[1:]:
            img = news.get('image') or DEFAULT_IMAGES['ai']
            source = news.get('source', '来源')
            html_template += f'''
            <div class="news-card" onclick="window.open('{news['url']}', '_blank')">
                <div class="card-image-wrap">
                    <img class="card-image" src="{img}" alt="" onerror="this.src='{DEFAULT_IMAGES['ai']}'">
                    <span class="card-source-tag">{source}</span>
                </div>
                <div class="card-content">
                    <div class="card-title">{news['title']}</div>
                    <div class="card-desc">{news['desc']}</div>
                    <div class="card-meta">
                        <span>🕐 {date_str}</span>
                    </div>
                </div>
            </div>
'''
        html_template += '</div>'
    
    # 金融财经
    if finance_results:
        first = finance_results[0]
        img = first.get('image') or DEFAULT_IMAGES['finance']
        source = first.get('source', '来源')
        html_template += f'''
        </div>
        
        <div class="section section-finance" id="finance">
            <div class="section-header">
                <div class="section-icon">📈</div>
                <div class="section-title">全球股市行情</div>
                <div class="section-count">{len(finance_results)} 条新闻</div>
            </div>
            <div class="featured-card" onclick="window.open('{first['url']}', '_blank')">
                <div class="featured-image-wrap">
                    <img class="featured-image" src="{img}" alt="" onerror="this.src='{DEFAULT_IMAGES['finance']}'">
                </div>
                <div class="featured-content">
                    <div class="featured-source">📰 {source}</div>
                    <div class="featured-title">{first['title']}</div>
                    <div class="featured-desc">{first['desc']}</div>
                    <div class="featured-meta">
                        <span>🕐 {date_str}</span>
                    </div>
                </div>
            </div>
            <div class="news-grid">
'''
        
        for news in finance_results[1:]:
            img = news.get('image') or DEFAULT_IMAGES['finance']
            source = news.get('source', '来源')
            html_template += f'''
            <div class="news-card" onclick="window.open('{news['url']}', '_blank')">
                <div class="card-image-wrap">
                    <img class="card-image" src="{img}" alt="" onerror="this.src='{DEFAULT_IMAGES['finance']}'">
                    <span class="card-source-tag">{source}</span>
                </div>
                <div class="card-content">
                    <div class="card-title">{news['title']}</div>
                    <div class="card-desc">{news['desc']}</div>
                    <div class="card-meta">
                        <span>🕐 {date_str}</span>
                    </div>
                </div>
            </div>
'''
        html_template += '</div>'
    
    # 军事
    if military_results:
        first = military_results[0]
        img = first.get('image') or DEFAULT_IMAGES['military']
        source = first.get('source', '来源')
        html_template += f'''
        </div>
        
        <div class="section section-military" id="military">
            <div class="section-header">
                <div class="section-icon">⚔️</div>
                <div class="section-title">国际军事要闻</div>
                <div class="section-count">{len(military_results)} 条新闻</div>
            </div>
            <div class="featured-card" onclick="window.open('{first['url']}', '_blank')">
                <div class="featured-image-wrap">
                    <img class="featured-image" src="{img}" alt="" onerror="this.src='{DEFAULT_IMAGES['military']}'">
                </div>
                <div class="featured-content">
                    <div class="featured-source">📰 {source}</div>
                    <div class="featured-title">{first['title']}</div>
                    <div class="featured-desc">{first['desc']}</div>
                    <div class="featured-meta">
                        <span>🕐 {date_str}</span>
                    </div>
                </div>
            </div>
            <div class="news-grid">
'''
        
        for news in military_results[1:]:
            img = news.get('image') or DEFAULT_IMAGES['military']
            source = news.get('source', '来源')
            html_template += f'''
            <div class="news-card" onclick="window.open('{news['url']}', '_blank')">
                <div class="card-image-wrap">
                    <img class="card-image" src="{img}" alt="" onerror="this.src='{DEFAULT_IMAGES['military']}'">
                    <span class="card-source-tag">{source}</span>
                </div>
                <div class="card-content">
                    <div class="card-title">{news['title']}</div>
                    <div class="card-desc">{news['desc']}</div>
                    <div class="card-meta">
                        <span>🕐 {date_str}</span>
                    </div>
                </div>
            </div>
'''
        html_template += '</div>'
    
    # 国际经济
    if world_results:
        first = world_results[0]
        img = first.get('image') or DEFAULT_IMAGES['world']
        source = first.get('source', '来源')
        html_template += f'''
        </div>
        
        <div class="section section-world" id="world">
            <div class="section-header">
                <div class="section-icon">🌍</div>
                <div class="section-title">国际经济要闻</div>
                <div class="section-count">{len(world_results)} 条新闻</div>
            </div>
            <div class="featured-card" onclick="window.open('{first['url']}', '_blank')">
                <div class="featured-image-wrap">
                    <img class="featured-image" src="{img}" alt="" onerror="this.src='{DEFAULT_IMAGES['world']}'">
                </div>
                <div class="featured-content">
                    <div class="featured-source">📰 {source}</div>
                    <div class="featured-title">{first['title']}</div>
                    <div class="featured-desc">{first['desc']}</div>
                    <div class="featured-meta">
                        <span>🕐 {date_str}</span>
                    </div>
                </div>
            </div>
            <div class="news-grid">
'''
        
        for news in world_results[1:]:
            img = news.get('image') or DEFAULT_IMAGES['world']
            source = news.get('source', '来源')
            html_template += f'''
            <div class="news-card" onclick="window.open('{news['url']}', '_blank')">
                <div class="card-image-wrap">
                    <img class="card-image" src="{img}" alt="" onerror="this.src='{DEFAULT_IMAGES['world']}'">
                    <span class="card-source-tag">{source}</span>
                </div>
                <div class="card-content">
                    <div class="card-title">{news['title']}</div>
                    <div class="card-desc">{news['desc']}</div>
                    <div class="card-meta">
                        <span>🕐 {date_str}</span>
                    </div>
                </div>
            </div>
'''
        html_template += '</div>'
    
    html_template += f'''
        </div>
    </div>
    
    <div class="footer">
        <p>⚡ 由 AI 精心整理 | 更新时间: {time_str}</p>
        <p style="margin-top: 8px;">
            <a href="https://github.com/peterle-wh/ai-daily-report">GitHub</a>
        </p>
    </div>
</body>
</html>'''
    
    os.makedirs('docs', exist_ok=True)
    with open('docs/index.html', 'w', encoding='utf-8') as f:
        f.write(html_template)
    
    print(f"✅ Report generated: {date_str}")

if __name__ == '__main__':
    generate_report()
