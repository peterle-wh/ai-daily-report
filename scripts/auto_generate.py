#!/usr/bin/env python3
"""
AI Daily Report - 奢华简约风 (Apple级别质感)
"""
import os
import requests
from datetime import datetime
import html

BRAVE_API_KEY = os.environ.get('BRAVE_API_KEY') or 'BSAm5_stG9BCZDHom2w9sMQxEziciB8'

DEFAULT_IMAGES = {
    'ai': 'https://images.unsplash.com/photo-1677442136019-21780ecad995?w=1200',
    'finance': 'https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?w=1200',
    'military': 'https://images.unsplash.com/photo-1533613220915-609f661a6fe1?w=1200',
    'world': 'https://images.unsplash.com/photo-1526304640581-d334cdbbf45e?w=1200'
}

def search_news(query, count=8):
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
            img_url = thumb.get("src", "") if thumb else ""
            desc = item.get("description", "")
            source = item.get("domain", "").replace("www.", "") if item.get("domain") else ""
            
            results.append({
                "title": html.escape(item.get("title", "")),
                "desc": html.escape(desc[:200]) if desc else "暂无描述",
                "url": item.get("url", ""),
                "image": img_url,
                "source": source
            })
        return results
    except:
        return []

def generate_report():
    print("🔍 搜索AI科技新闻...")
    ai_results = search_news("AI 科技 最新新闻", 8)
    
    print("🔍 搜索金融新闻...")
    finance_results = search_news("股票 市场 财经", 8)
    
    print("🔍 搜索军事新闻...")
    military_results = search_news("military news today", 8)
    
    print("🔍 搜索国际经济新闻...")
    world_results = search_news("国际经济 最新", 8)
    
    # 备用数据
    if not ai_results:
        ai_results = [{"title": "AI领域最新突破", "desc": "人工智能技术持续突破，带来产业变革", "url": "", "image": DEFAULT_IMAGES['ai'], "source": "科技日报"}]
    if not finance_results:
        finance_results = [{"title": "全球股市动态", "desc": "市场行情分析，投资机会解读", "url": "", "image": DEFAULT_IMAGES['finance'], "source": "财经网"}]
    if not military_results:
        military_results = [{"title": "国际军事局势", "desc": "全球军事动态，地区安全形势分析", "url": "", "image": DEFAULT_IMAGES['military'], "source": "参考消息"}]
    if not world_results:
        world_results = [{"title": "国际经济要闻", "desc": "全球经济动态，贸易投资趋势", "url": "", "image": DEFAULT_IMAGES['world'], "source": "新华网"}]
    
    date_str = datetime.now().strftime('%Y年%m月%d日')
    
    html_content = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>每日要闻 - 精心筛选</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@300;400;500;600&family=SF+Pro+Display:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        
        :root {{
            --bg-primary: #000000;
            --bg-secondary: #1d1d1f;
            --bg-tertiary: #2d2d2f;
            --text-primary: #f5f5f7;
            --text-secondary: #86868b;
            --text-tertiary: #6e6e73;
            --accent: #2997ff;
            --accent-light: #0a84ff;
            --border: rgba(255,255,255,0.1);
            --shadow: 0 20px 40px rgba(0,0,0,0.4);
            --card-shadow: 0 4px 24px rgba(0,0,0,0.3);
        }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'Noto Sans SC', sans-serif;
            background: var(--bg-primary);
            color: var(--text-primary);
            line-height: 1.6;
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
        }}
        
        /* 顶部导航 */
        .header {{
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            height: 56px;
            background: rgba(0,0,0,0.8);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            z-index: 1000;
            border-bottom: 1px solid var(--border);
        }}
        
        .header-inner {{
            max-width: 980px;
            margin: 0 auto;
            height: 100%;
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0 20px;
        }}
        
        .logo {{
            font-size: 20px;
            font-weight: 600;
            color: var(--text-primary);
            letter-spacing: -0.5px;
        }}
        
        .nav {{
            display: flex;
            gap: 32px;
        }}
        
        .nav a {{
            color: var(--text-secondary);
            text-decoration: none;
            font-size: 12px;
            font-weight: 500;
            transition: color 0.3s;
        }}
        
        .nav a:hover {{
            color: var(--text-primary);
        }}
        
        /* 主内容 */
        .main {{
            max-width: 980px;
            margin: 0 auto;
            padding: 120px 20px 80px;
        }}
        
        /* 标题区 */
        .hero {{
            text-align: center;
            padding: 60px 0 80px;
        }}
        
        .hero h1 {{
            font-size: 56px;
            font-weight: 700;
            letter-spacing: -1px;
            margin-bottom: 16px;
            background: linear-gradient(135deg, #fff 0%, #86868b 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}
        
        .hero p {{
            font-size: 24px;
            font-weight: 300;
            color: var(--text-secondary);
            letter-spacing: -0.5px;
        }}
        
        .hero .date {{
            font-size: 14px;
            color: var(--text-tertiary);
            margin-top: 20px;
        }}
        
        /* 统计 */
        .stats {{
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 16px;
            margin-bottom: 80px;
        }}
        
        .stat {{
            background: var(--bg-secondary);
            border-radius: 20px;
            padding: 28px 20px;
            text-align: center;
            transition: transform 0.3s, box-shadow 0.3s;
        }}
        
        .stat:hover {{
            transform: translateY(-4px);
            box-shadow: var(--shadow);
        }}
        
        .stat-number {{
            font-size: 48px;
            font-weight: 700;
            color: var(--accent);
            line-height: 1;
        }}
        
        .stat-label {{
            font-size: 14px;
            color: var(--text-secondary);
            margin-top: 8px;
        }}
        
        /* 板块 */
        .section {{
            margin-bottom: 100px;
        }}
        
        .section-header {{
            display: flex;
            align-items: baseline;
            gap: 16px;
            margin-bottom: 32px;
            padding-bottom: 16px;
            border-bottom: 1px solid var(--border);
        }}
        
        .section-icon {{
            width: 48px;
            height: 48px;
            background: var(--bg-secondary);
            border-radius: 14px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 24px;
        }}
        
        .section-title {{
            font-size: 32px;
            font-weight: 600;
            letter-spacing: -0.5px;
        }}
        
        .section-count {{
            color: var(--text-tertiary);
            font-size: 14px;
        }}
        
        /* 特色卡片 - 大 */
        .featured {{
            background: var(--bg-secondary);
            border-radius: 24px;
            overflow: hidden;
            margin-bottom: 24px;
            cursor: pointer;
            transition: transform 0.4s ease, box-shadow 0.4s ease;
        }}
        
        .featured:hover {{
            transform: scale(1.01);
            box-shadow: var(--shadow);
        }}
        
        .featured-img-wrap {{
            height: 360px;
            overflow: hidden;
        }}
        
        .featured-img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.6s ease;
        }}
        
        .featured:hover .featured-img {{
            transform: scale(1.05);
        }}
        
        .featured-content {{
            padding: 32px;
        }}
        
        .featured-source {{
            font-size: 12px;
            color: var(--accent);
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 12px;
        }}
        
        .featured-title {{
            font-size: 28px;
            font-weight: 600;
            margin-bottom: 12px;
            line-height: 1.3;
        }}
        
        .featured-desc {{
            font-size: 16px;
            color: var(--text-secondary);
            line-height: 1.7;
        }}
        
        /* 卡片网格 */
        .grid {{
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 20px;
        }}
        
        .card {{
            background: var(--bg-secondary);
            border-radius: 20px;
            overflow: hidden;
            cursor: pointer;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }}
        
        .card:hover {{
            transform: translateY(-6px);
            box-shadow: var(--shadow);
        }}
        
        .card-img-wrap {{
            height: 180px;
            overflow: hidden;
        }}
        
        .card-img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.5s ease;
        }}
        
        .card:hover .card-img {{
            transform: scale(1.08);
        }}
        
        .card-content {{
            padding: 20px;
        }}
        
        .card-source {{
            font-size: 11px;
            color: var(--accent);
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-bottom: 8px;
        }}
        
        .card-title {{
            font-size: 17px;
            font-weight: 600;
            line-height: 1.4;
            margin-bottom: 8px;
        }}
        
        .card-desc {{
            font-size: 14px;
            color: var(--text-secondary);
            line-height: 1.6;
            display: -webkit-box;
            -webkit-line-clamp: 2;
            -webkit-box-orient: vertical;
            overflow: hidden;
        }}
        
        /* 页脚 */
        .footer {{
            text-align: center;
            padding: 60px 20px;
            color: var(--text-tertiary);
            font-size: 12px;
            border-top: 1px solid var(--border);
        }}
        
        .footer a {{
            color: var(--accent);
            text-decoration: none;
        }}
        
        /* 响应式 */
        @media (max-width: 768px) {{
            .hero h1 {{ font-size: 40px; }}
            .hero p {{ font-size: 18px; }}
            .stats {{ grid-template-columns: repeat(2, 1fr); }}
            .grid {{ grid-template-columns: 1fr; }}
            .nav {{ display: none; }}
            .featured-img-wrap {{ height: 240px; }}
            .featured-title {{ font-size: 22px; }}
        }}
        
        /* 动画 */
        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(20px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        
        .section {{ animation: fadeIn 0.6s ease forwards; }}
        .section:nth-child(2) {{ animation-delay: 0.1s; }}
        .section:nth-child(3) {{ animation-delay: 0.2s; }}
        .section:nth-child(4) {{ animation-delay: 0.3s; }}
    </style>
</head>
<body>
    <div class="header">
        <div class="header-inner">
            <div class="logo">每日要闻</div>
            <nav class="nav">
                <a href="#ai">AI 科技</a>
                <a href="#finance">财经股市</a>
                <a href="#military">国际军事</a>
                <a href="#world">国际经济</a>
            </nav>
        </div>
    </div>
    
    <main class="main">
        <div class="hero">
            <h1>每日要闻</h1>
            <p>精心筛选 · 值得阅读</p>
            <div class="date">{date_str}</div>
        </div>
        
        <div class="stats">
            <div class="stat">
                <div class="stat-number">{len(ai_results)}</div>
                <div class="stat-label">AI 科技</div>
            </div>
            <div class="stat">
                <div class="stat-number">{len(finance_results)}</div>
                <div class="stat-label">财经股市</div>
            </div>
            <div class="stat">
                <div class="stat-number">{len(military_results)}</div>
                <div class="stat-label">国际军事</div>
            </div>
            <div class="stat">
                <div class="stat-number">{len(world_results)}</div>
                <div class="stat-label">国际经济</div>
            </div>
        </div>
'''

    # AI科技板块
    if ai_results:
        first = ai_results[0]
        img = first.get('image') or DEFAULT_IMAGES['ai']
        html_content += f'''
        <section class="section" id="ai">
            <div class="section-header">
                <div class="section-icon">🤖</div>
                <h2 class="section-title">AI 科技</h2>
                <span class="section-count">{len(ai_results)} 条精选</span>
            </div>
            <div class="featured" onclick="window.open('{first['url']}', '_blank')">
                <div class="featured-img-wrap">
                    <img class="featured-img" src="{img}" alt="" onerror="this.src='{DEFAULT_IMAGES['ai']}'">
                </div>
                <div class="featured-content">
                    <div class="featured-source">{first.get('source', '来源')}</div>
                    <h3 class="featured-title">{first['title']}</h3>
                    <p class="featured-desc">{first['desc']}</p>
                </div>
            </div>
            <div class="grid">
'''
        for news in ai_results[1:]:
            img = news.get('image') or DEFAULT_IMAGES['ai']
            html_content += f'''
            <div class="card" onclick="window.open('{news['url']}', '_blank')">
                <div class="card-img-wrap">
                    <img class="card-img" src="{img}" alt="" onerror="this.src='{DEFAULT_IMAGES['ai']}'">
                </div>
                <div class="card-content">
                    <div class="card-source">{news.get('source', '来源')}</div>
                    <h4 class="card-title">{news['title']}</h4>
                    <p class="card-desc">{news['desc']}</p>
                </div>
            </div>
'''
        html_content += '</div></section>'

    # 财经板块
    if finance_results:
        first = finance_results[0]
        img = first.get('image') or DEFAULT_IMAGES['finance']
        html_content += f'''
        <section class="section" id="finance">
            <div class="section-header">
                <div class="section-icon">📈</div>
                <h2 class="section-title">财经股市</h2>
                <span class="section-count">{len(finance_results)} 条精选</span>
            </div>
            <div class="featured" onclick="window.open('{first['url']}', '_blank')">
                <div class="featured-img-wrap">
                    <img class="featured-img" src="{img}" alt="" onerror="this.src='{DEFAULT_IMAGES['finance']}'">
                </div>
                <div class="featured-content">
                    <div class="featured-source">{first.get('source', '来源')}</div>
                    <h3 class="featured-title">{first['title']}</h3>
                    <p class="featured-desc">{first['desc']}</p>
                </div>
            </div>
            <div class="grid">
'''
        for news in finance_results[1:]:
            img = news.get('image') or DEFAULT_IMAGES['finance']
            html_content += f'''
            <div class="card" onclick="window.open('{news['url']}', '_blank')">
                <div class="card-img-wrap">
                    <img class="card-img" src="{img}" alt="" onerror="this.src='{DEFAULT_IMAGES['finance']}'">
                </div>
                <div class="card-content">
                    <div class="card-source">{news.get('source', '来源')}</div>
                    <h4 class="card-title">{news['title']}</h4>
                    <p class="card-desc">{news['desc']}</p>
                </div>
            </div>
'''
        html_content += '</div></section>'

    # 军事板块
    if military_results:
        first = military_results[0]
        img = first.get('image') or DEFAULT_IMAGES['military']
        html_content += f'''
        <section class="section" id="military">
            <div class="section-header">
                <div class="section-icon">🎯</div>
                <h2 class="section-title">国际军事</h2>
                <span class="section-count">{len(military_results)} 条精选</span>
            </div>
            <div class="featured" onclick="window.open('{first['url']}', '_blank')">
                <div class="featured-img-wrap">
                    <img class="featured-img" src="{img}" alt="" onerror="this.src='{DEFAULT_IMAGES['military']}'">
                </div>
                <div class="featured-content">
                    <div class="featured-source">{first.get('source', '来源')}</div>
                    <h3 class="featured-title">{first['title']}</h3>
                    <p class="featured-desc">{first['desc']}</p>
                </div>
            </div>
            <div class="grid">
'''
        for news in military_results[1:]:
            img = news.get('image') or DEFAULT_IMAGES['military']
            html_content += f'''
            <div class="card" onclick="window.open('{news['url']}', '_blank')">
                <div class="card-img-wrap">
                    <img class="card-img" src="{img}" alt="" onerror="this.src='{DEFAULT_IMAGES['military']}'">
                </div>
                <div class="card-content">
                    <div class="card-source">{news.get('source', '来源')}</div>
                    <h4 class="card-title">{news['title']}</h4>
                    <p class="card-desc">{news['desc']}</p>
                </div>
            </div>
'''
        html_content += '</div></section>'

    # 国际经济板块
    if world_results:
        first = world_results[0]
        img = first.get('image') or DEFAULT_IMAGES['world']
        html_content += f'''
        <section class="section" id="world">
            <div class="section-header">
                <div class="section-icon">🌍</div>
                <h2 class="section-title">国际经济</h2>
                <span class="section-count">{len(world_results)} 条精选</span>
            </div>
            <div class="featured" onclick="window.open('{first['url']}', '_blank')">
                <div class="featured-img-wrap">
                    <img class="featured-img" src="{img}" alt="" onerror="this.src='{DEFAULT_IMAGES['world']}'">
                </div>
                <div class="featured-content">
                    <div class="featured-source">{first.get('source', '来源')}</div>
                    <h3 class="featured-title">{first['title']}</h3>
                    <p class="featured-desc">{first['desc']}</p>
                </div>
            </div>
            <div class="grid">
'''
        for news in world_results[1:]:
            img = news.get('image') or DEFAULT_IMAGES['world']
            html_content += f'''
            <div class="card" onclick="window.open('{news['url']}', '_blank')">
                <div class="card-img-wrap">
                    <img class="card-img" src="{img}" alt="" onerror="this.src='{DEFAULT_IMAGES['world']}'">
                </div>
                <div class="card-content">
                    <div class="card-source">{news.get('source', '来源')}</div>
                    <h4 class="card-title">{news['title']}</h4>
                    <p class="card-desc">{news['desc']}</p>
                </div>
            </div>
'''
        html_content += '</div></section>'

    html_content += f'''
    </main>
    
    <footer class="footer">
        <p>由 AI 精心整理 · {date_str}</p>
        <p style="margin-top: 12px;">
            <a href="https://github.com/peterle-wh/ai-daily-report">GitHub</a>
        </p>
    </footer>
</body>
</html>'''
    
    os.makedirs('docs', exist_ok=True)
    with open('docs/index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✅ 奢华简约风网站生成完成: {date_str}")

if __name__ == '__main__':
    generate_report()
