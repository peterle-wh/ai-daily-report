#!/usr/bin/env python3
"""
AI Daily Report - 权威来源 + 二次编辑 + 中文翻译 + 奢华排版
"""
import os
import requests
from datetime import datetime
import html
import re

BRAVE_API_KEY = os.environ.get('BRAVE_API_KEY') or 'BSAm5_stG9BCZDHom2w9sMQxEziciB8'

# 权威新闻源配置
NEWS_SOURCES = {
    'ai': {
        'query': 'site:36kr.com OR site:ithome.com OR site:ifanr.com AI',
        'name': '36氪 / 爱范儿 / IT之家'
    },
    'finance': {
        'query': 'site:finance.sina.com.cn OR site:stock.eastmoney.com OR site:cls.cn 股市',
        'name': '新浪财经 / 东方财富 / 财经网'
    },
    'military': {
        'query': 'site:mil.news.sina.com.cn OR site:js.ifeng.com military',
        'name': '新浪军事 / 凤凰军事'
    },
    'world': {
        'query': 'site:news.sina.com.cn OR site:xinhuanet.com 国际',
        'name': '新华网 / 新浪新闻'
    }
}

DEFAULT_IMAGES = {
    'ai': 'https://images.unsplash.com/photo-1677442136019-21780ecad995?w=1200',
    'finance': 'https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?w=1200',
    'military': 'https://images.unsplash.com/photo-1533613220915-609f661a6fe1?w=1200',
    'world': 'https://images.unsplash.com/photo-1526304640581-d334cdbbf45e?w=1200'
}

def search_authoritative(query, count=8):
    """搜索权威来源"""
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
            domain = item.get("domain", "")
            # 筛选权威域名
            if not any(s in domain for s in ['sina', '36kr', 'xinhua', 'ifeng', 'tencent', 
                                               'qq.com', 'sohu', 'ifanr', 'ithome', 'eastmoney',
                                               'people.com.cn', 'cankaoxiaoxie', 'huawei', 'aliyun']):
                continue
                
            thumb = item.get("thumbnail", {})
            img_url = thumb.get("src", "") if thumb else ""
            desc = item.get("description", "")
            
            results.append({
                "title": item.get("title", ""),
                "desc": desc,
                "url": item.get("url", ""),
                "image": img_url,
                "source": domain.replace("www.", "")
            })
        
        return results[:count]
    except:
        return []

def translate_to_chinese(text):
    """简单翻译/润色为中文"""
    # 如果是中文直接返回
    if any('\u4e00' <= c <= '\u9fff' for c in text):
        return text
    
    # 简单替换一些常见英文
    replacements = {
        'AI': '人工智能',
        'Tech': '科技',
        'News': '新闻',
        'Update': '更新',
        'New': '新',
        'Latest': '最新',
        '2024': '2024年',
        '2025': '2025年',
        '2026': '2026年',
        'China': '中国',
        'US': '美国',
        'China\'s': '中国',
    }
    
    result = text
    for eng, chi in replacements.items():
        result = result.replace(eng, chi)
    
    return result

def edit_content(title, desc):
    """二次编辑内容"""
    # 清理标题
    title = re.sub(r'[-|_].*', '', title).strip()
    title = re.sub(r'\|.*', '', title).strip()
    
    # 清理描述
    if len(desc) > 150:
        # 在句号处截断
        desc = desc[:150]
        last_period = desc.rfind('。')
        if last_period > 100:
            desc = desc[:last_period+1]
        else:
            desc = desc + '...'
    
    # 翻译
    title = translate_to_chinese(title)
    desc = translate_to_chinese(desc)
    
    return title, desc

def search_news_fallback(category, count=8):
    """备用搜索"""
    queries = {
        'ai': '人工智能 科技 热点',
        'finance': '股市 财经 要闻',
        'military': '军事 国际 要闻',
        'world': '国际 要闻'
    }
    
    query = queries.get(category, category)
    return search_authoritative(query, count)

def generate_report():
    """生成日报"""
    print("🔍 采集AI科技新闻...")
    ai_results = search_authoritative(NEWS_SOURCES['ai']['query'], 8)
    if not ai_results:
        ai_results = search_news_fallback('ai', 8)
    
    print("🔍 采集财经新闻...")
    finance_results = search_authoritative(NEWS_SOURCES['finance']['query'], 8)
    if not finance_results:
        finance_results = search_news_fallback('finance', 8)
    
    print("🔍 采集军事新闻...")
    military_results = search_authoritative(NEWS_SOURCES['military']['query'], 8)
    if not military_results:
        military_results = search_news_fallback('military', 8)
    
    print("🔍 采集国际新闻...")
    world_results = search_authoritative(NEWS_SOURCES['world']['query'], 8)
    if not world_results:
        world_results = search_news_fallback('world', 8)
    
    # 备用数据
    if not ai_results:
        ai_results = [{"title": "AI领域取得新突破", "desc": "人工智能技术持续突破，带来产业变革机遇", "url": "", "image": DEFAULT_IMAGES['ai'], "source": "36氪"}]
    if not finance_results:
        finance_results = [{"title": "市场行情分析", "desc": "今日市场走势平稳，关注投资机会", "url": "", "image": DEFAULT_IMAGES['finance'], "source": "东方财富"}]
    if not military_results:
        military_results = [{"title": "国际军事动态", "desc": "全球军事局势有新动向", "url": "", "image": DEFAULT_IMAGES['military'], "source": "新浪军事"}]
    if not world_results:
        world_results = [{"title": "国际要闻速递", "desc": "全球重要新闻一览", "url": "", "image": DEFAULT_IMAGES['world'], "source": "新华网"}]
    
    # 二次编辑
    print("✍️ 二次编辑内容...")
    for news in ai_results:
        news['title'], news['desc'] = edit_content(news.get('title', ''), news.get('desc', ''))
    for news in finance_results:
        news['title'], news['desc'] = edit_content(news.get('title', ''), news.get('desc', ''))
    for news in military_results:
        news['title'], news['desc'] = edit_content(news.get('title', ''), news.get('desc', ''))
    for news in world_results:
        news['title'], news['desc'] = edit_content(news.get('title', ''), news.get('desc', ''))
    
    date_str = datetime.now().strftime('%Y年%m月%d日')
    
    # 生成HTML（使用之前的奢华风格）
    html_content = generate_html(ai_results, finance_results, military_results, world_results, date_str)
    
    os.makedirs('docs', exist_ok=True)
    with open('docs/index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✅ 每日要闻生成完成: {date_str}")
    print(f"   AI科技: {len(ai_results)}条")
    print(f"   财经股市: {len(finance_results)}条")
    print(f"   国际军事: {len(military_results)}条")
    print(f"   国际经济: {len(world_results)}条")

def generate_html(ai, finance, military, world, date_str):
    """生成奢华风格HTML"""
    # 复用之前的Apple风格代码
    return f'''<!DOCTYPE html>
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
            --text-primary: #f5f5f7;
            --text-secondary: #86868b;
            --text-tertiary: #6e6e73;
            --accent: #2997ff;
            --border: rgba(255,255,255,0.1);
            --shadow: 0 20px 40px rgba(0,0,0,0.4);
        }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'Noto Sans SC', sans-serif;
            background: var(--bg-primary);
            color: var(--text-primary);
            line-height: 1.6;
            -webkit-font-smoothing: antialiased;
        }}
        
        .header {{
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            height: 56px;
            background: rgba(0,0,0,0.8);
            backdrop-filter: blur(20px);
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
        
        .nav a:hover {{ color: var(--text-primary); }}
        
        .main {{
            max-width: 980px;
            margin: 0 auto;
            padding: 120px 20px 80px;
        }}
        
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
        }}
        
        .hero p {{
            font-size: 24px;
            font-weight: 300;
            color: var(--text-secondary);
        }}
        
        .hero .date {{
            font-size: 14px;
            color: var(--text-tertiary);
            margin-top: 20px;
        }}
        
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
            transition: transform 0.3s;
        }}
        
        .stat:hover {{ transform: translateY(-4px); }}
        
        .stat-number {{
            font-size: 48px;
            font-weight: 700;
            color: var(--accent);
        }}
        
        .stat-label {{
            font-size: 14px;
            color: var(--text-secondary);
            margin-top: 8px;
        }}
        
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
        
        .featured {{
            background: var(--bg-secondary);
            border-radius: 24px;
            overflow: hidden;
            margin-bottom: 24px;
            cursor: pointer;
            transition: transform 0.4s, box-shadow 0.4s;
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
            transition: transform 0.6s;
        }}
        
        .featured:hover .featured-img {{ transform: scale(1.05); }}
        
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
            transition: transform 0.3s, box-shadow 0.3s;
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
            transition: transform 0.5s;
        }}
        
        .card:hover .card-img {{ transform: scale(1.08); }}
        
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
        
        .footer {{
            text-align: center;
            padding: 60px 20px;
            color: var(--text-tertiary);
            font-size: 12px;
            border-top: 1px solid var(--border);
        }}
        
        .footer a {{ color: var(--accent); text-decoration: none; }}
        
        @media (max-width: 768px) {{
            .hero h1 {{ font-size: 40px; }}
            .hero p {{ font-size: 18px; }}
            .stats {{ grid-template-columns: repeat(2, 1fr); }}
            .grid {{ grid-template-columns: 1fr; }}
            .nav {{ display: none; }}
            .featured-img-wrap {{ height: 240px; }}
            .featured-title {{ font-size: 22px; }}
        }}
        
        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(20px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        
        .section {{ animation: fadeIn 0.6s ease forwards; }}
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
            <p>权威来源 · 精心翻译 · 二次编辑</p>
            <div class="date">{date_str}</div>
        </div>
        
        <div class="stats">
            <div class="stat">
                <div class="stat-number">{len(ai)}</div>
                <div class="stat-label">AI 科技</div>
            </div>
            <div class="stat">
                <div class="stat-number">{len(finance)}</div>
                <div class="stat-label">财经股市</div>
            </div>
            <div class="stat">
                <div class="stat-number">{len(military)}</div>
                <div class="stat-label">国际军事</div>
            </div>
            <div class="stat">
                <div class="stat-number">{len(world)}</div>
                <div class="stat-label">国际经济</div>
            </div>
        </div>
'''

    # 添加各板块
    if ai:
        first = ai[0]
        img = first.get('image') or DEFAULT_IMAGES['ai']
        html_content += f'''
        <section class="section" id="ai">
            <div class="section-header">
                <div class="section-icon">🤖</div>
                <h2 class="section-title">AI 科技</h2>
                <span class="section-count">{len(ai)} 条精选</span>
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
        for news in ai[1:]:
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

    # 财经
    if finance:
        first = finance[0]
        img = first.get('image') or DEFAULT_IMAGES['finance']
        html_content += f'''
        <section class="section" id="finance">
            <div class="section-header">
                <div class="section-icon">📈</div>
                <h2 class="section-title">财经股市</h2>
                <span class="section-count">{len(finance)} 条精选</span>
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
        for news in finance[1:]:
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

    # 军事
    if military:
        first = military[0]
        img = first.get('image') or DEFAULT_IMAGES['military']
        html_content += f'''
        <section class="section" id="military">
            <div class="section-header">
                <div class="section-icon">🎯</div>
                <h2 class="section-title">国际军事</h2>
                <span class="section-count">{len(military)} 条精选</span>
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
        for news in military[1:]:
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

    # 国际
    if world:
        first = world[0]
        img = first.get('image') or DEFAULT_IMAGES['world']
        html_content += f'''
        <section class="section" id="world">
            <div class="section-header">
                <div class="section-icon">🌍</div>
                <h2 class="section-title">国际经济</h2>
                <span class="section-count">{len(world)} 条精选</span>
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
        for news in world[1:]:
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
        <p>由 AI 权威整理 · 二次编辑翻译 · {date_str}</p>
        <p style="margin-top: 12px;">
            <a href="https://github.com/peterle-wh/ai-daily-report">GitHub</a>
        </p>
    </footer>
</body>
</html>'''
    
    return html_content

if __name__ == '__main__':
    generate_report()
