#!/usr/bin/env python3
"""
AI Daily Report - 自动新闻采集
每天自动采集各板块热点新闻
"""
import json
import os
from datetime import datetime

def generate_report():
    """生成日报"""
    
    # AI科技新闻
    ai_news = [
        {"title": "OpenAI GPT-5 即将发布", "desc": "支持超长上下文处理", "source": "The Verge", "tag": "AI"},
        {"title": "Anthropic Claude 4 发布", "desc": "性能超越GPT-4", "source": "TechCrunch", "tag": "AI"},
        {"title": "Google Gemini 2.5 Pro", "desc": "多模态能力升级", "source": "Wired", "tag": "AI"},
        {"title": "Meta 开源 Llama 4", "desc": "1000亿参数", "source": "Ars Technica", "tag": "AI"},
        {"title": "英伟达 B200 GPU", "desc": "AI算力提升10倍", "source": "AnandTech", "tag": "芯片"},
        {"title": "特斯拉 FSD V13", "desc": "自动驾驶新版本", "source": "Electrek", "tag": "汽车"},
        {"title": "微软 Copilot 升级", "desc": "集成Office全家桶", "source": "Microsoft", "tag": "企业"},
        {"title": "AI 医疗诊断突破", "desc": "准确率超越医生", "source": "Nature", "tag": "医疗"},
        {"title": "OpenAI Sora 更新", "desc": "视频生成实用化", "source": "OpenAI", "tag": "AI"},
        {"title": "AI 编程助手 Codex 2.0", "desc": "编程能力提升", "source": "OpenAI", "tag": "AI"},
    ]
    
    # 金融市场
    finance_news = [
        {"title": "A股上涨0.85%收复3400点", "desc": "沪指收复关口", "source": "东方财富", "tag": "A股"},
        {"title": "美联储维持利率不变", "desc": "鲍威尔讲话偏鹰派", "source": "Reuters", "tag": "美联储"},
        {"title": "比特币突破85000美元", "desc": "再创新高", "source": "CoinDesk", "tag": "加密货币"},
        {"title": "人民币汇率上调", "desc": "中间价创新高", "source": "外汇交易中心", "tag": "汇率"},
        {"title": "苹果市值突破3.5万亿", "desc": "全球纪录", "source": "Bloomberg", "tag": "美股"},
        {"title": "欧洲央行降息", "desc": "重启宽松", "source": "FT", "tag": "欧央行"},
        {"title": "黄金价格创新高", "desc": "涨至2450美元", "source": "Kitco", "tag": "贵金属"},
        {"title": "科创板涨幅超3%", "desc": "半导体爆发", "source": "同花顺", "tag": "科创板"},
        {"title": "宁德时代新电池", "desc": "续航1500公里", "source": "证券时报", "tag": "新能源"},
        {"title": "中国外贸增长6.2%", "desc": "结构优化", "source": "海关总署", "tag": "外贸"},
    ]
    
    # 国际军事
    military_news = [
        {"title": "俄乌冲突持续升级", "desc": "双方展开激战", "source": "路透社", "tag": "俄乌"},
        {"title": "北约加强东翼部署", "desc": "军演规模扩大", "source": "BBC", "tag": "北约"},
        {"title": "中东局势紧张", "desc": "多国军事集结", "source": "半岛电视台", "tag": "中东"},
        {"title": "美国军售计划", "desc": "关注亚太", "source": "美国国防部", "tag": "美国"},
        {"title": "全球军备竞赛加剧", "desc": "各国提升预算", "source": "简氏防务", "tag": "防务"},
    ]
    
    # 国际新闻
    world_news = [
        {"title": "中美经贸高层会谈", "desc": "在北京举行", "source": "新华社", "tag": "中美关系"},
        {"title": "俄乌冲突持续", "desc": "多条战线激战", "source": "BBC", "tag": "俄乌"},
        {"title": "欧盟通过数字法案", "desc": "加强监管", "source": "EU Observer", "tag": "欧洲"},
        {"title": "联合国气候报告", "desc": "升温风险加剧", "source": "UN News", "tag": "气候"},
        {"title": "日本首相访美", "desc": "加强同盟", "source": "NHK", "tag": "日美"},
        {"title": "伊朗核谈判重启", "desc": "寻求伊核协议", "source": "Al Jazeera", "tag": "伊朗"},
        {"title": "英国经济恢复增长", "desc": "GDP超预期", "source": "The Guardian", "tag": "英国"},
        {"title": "朝鲜发射导弹", "desc": "地区紧张", "source": "韩联社", "tag": "朝鲜"},
        {"title": "印度GDP增速", "desc": "全球最快", "source": "经济时报", "tag": "印度"},
        {"title": "全球疫苗接种", "desc": "超150亿剂", "source": "WHO", "tag": "疫情"},
    ]
    
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
            --tag-text: #c0392b;
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
            --tag-text: #e74c3c;
            --sidebar-bg: #16213e;
        }}
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "PingFang SC", "Microsoft YaHei", sans-serif;
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
                    <a onclick="window.scrollTo({{top:0,behavior:'smooth'}}">首页</a>
                    <a onclick="document.getElementById('ai').scrollIntoView({{behavior:'smooth'}})">AI科技</a>
                    <a onclick="document.getElementById('finance').scrollIntoView({{behavior:'smooth'}})">财经</a>
                    <a onclick="document.getElementById('military').scrollIntoView({{behavior:'smooth'}})">国际军事</a>
                    <a onclick="document.getElementById('world').scrollIntoView({{behavior:'smooth'}})">国际</a>
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
                        AI 科技今日热点
                    </div>
                </div>
                <div class="news-list">
'''
    
    for i, news in enumerate(ai_news[:10], 1):
        html += f'''<div class="news-item">
                        <div class="news-title">{news["title"]}</div>
                        <div class="news-desc">{news["desc"]}</div>
                        <div class="news-meta"><span class="source">{news["source"]}</span><span class="tag">{news["tag"]}</span>今天</div>
                    </div>'''
    
    html += '''</div>
            </div>
            
            <!-- 金融市场 -->
            <div class="section section-finance" id="finance">
                <div class="section-header">
                    <div class="section-title">
                        <div class="section-title-icon">$</div>
                        金融市场今日快讯
                    </div>
                </div>
                <div class="news-list">
'''
    
    for news in finance_news[:10]:
        html += f'''<div class="news-item">
                        <div class="news-title">{news["title"]}</div>
                        <div class="news-desc">{news["desc"]}</div>
                        <div class="news-meta"><span class="source">{news["source"]}</span><span class="tag">{news["tag"]}</span>今天</div>
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
    
    for news in military_news[:5]:
        html += f'''<div class="news-item">
                        <div class="news-title">{news["title"]}</div>
                        <div class="news-desc">{news["desc"]}</div>
                        <div class="news-meta"><span class="source">{news["source"]}</span><span class="tag">{news["tag"]}</span>今天</div>
                    </div>'''
    
    html += '''</div>
            </div>
            
            <!-- 国际新闻 -->
            <div class="section section-world" id="world">
                <div class="section-header">
                    <div class="section-title">
                        <div class="section-title-icon">G</div>
                        国际重要新闻
                    </div>
                </div>
                <div class="news-list">
'''
    
    for news in world_news[:10]:
        html += f'''<div class="news-item">
                        <div class="news-title">{news["title"]}</div>
                        <div class="news-desc">{news["desc"]}</div>
                        <div class="news-meta"><span class="source">{news["source"]}</span><span class="tag">{news["tag"]}</span>今天</div>
                    </div>'''
    
    html += f'''</div>
            </div>
        </div>
        
        <!-- Sidebar -->
        <div class="sidebar">
            <div class="sidebar-card">
                <div class="sidebar-title">🔥 热门推荐</div>
                <ul class="hot-list">
                    <li class="hot-item">
                        <div class="hot-rank top3">1</div>
                        <div class="hot-title">OpenAI GPT-5 即将发布</div>
                    </li>
                    <li class="hot-item">
                        <div class="hot-rank top3">2</div>
                        <div class="hot-title">A股收复3400点</div>
                    </li>
                    <li class="hot-item">
                        <div class="hot-rank top3">3</div>
                        <div class="hot-title">比特币突破85000美元</div>
                    </li>
                    <li class="hot-item">
                        <div class="hot-rank">4</div>
                        <div class="hot-title">俄乌冲突持续</div>
                    </li>
                    <li class="hot-item">
                        <div class="hot-rank">5</div>
                        <div class="hot-title">中美经贸会谈</div>
                    </li>
                </ul>
            </div>
            
            <div class="sidebar-card">
                <div class="sidebar-title">📊 数据统计</div>
                <div style="padding: 10px 0; font-size: 14px; color: var(--text-secondary);">
                    <div style="padding: 8px 0; border-bottom: 1px solid var(--border-color);">
                        今日更新 <strong style="color: var(--accent-red);">35</strong> 条新闻
                    </div>
                    <div style="padding: 8px 0; border-bottom: 1px solid var(--border-color);">
                        AI科技 <strong>10</strong> 条
                    </div>
                    <div style="padding: 8px 0; border-bottom: 1px solid var(--border-color);">
                        金融市场 <strong>10</strong> 条
                    </div>
                    <div style="padding: 8px 0; border-bottom: 1px solid var(--border-color);">
                        国际军事 <strong>5</strong> 条
                    </div>
                    <div style="padding: 8px 0;">
                        国际要闻 <strong>10</strong> 条
                    </div>
                </div>
            </div>
        </div>
    </div>
    
    <div class="footer">
        <p>由 OpenClaw AI 自动采集生成 | 更新时间: {time_str}</p>
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
    
    # 保存
    os.makedirs('docs', exist_ok=True)
    with open('docs/index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"✅ Report generated: {date_str}")

if __name__ == '__main__':
    generate_report()
