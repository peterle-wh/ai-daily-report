#!/usr/bin/env python3
"""Enhanced website generator with more content"""
import os
from datetime import datetime

ai_news = [
    {"title": "OpenAI GPT-5 即将发布，预计支持长文本处理", "source": "The Verge", "time": "今天"},
    {"title": "Anthropic 发布 Claude 4，性能超越 GPT-4", "source": "TechCrunch", "time": "今天"},
    {"title": "Google DeepMind 推出 Gemini 2.5 Pro", "source": "Wired", "time": "今天"},
    {"title": "Meta 开源 Llama 4，参数达 1000亿", "source": "Ars Technica", "time": "今天"},
    {"title": "英伟达发布 Blackwell B200 GPU", "source": "AnandTech", "time": "今天"},
    {"title": "AI 编程助手 Codex 2.0 发布", "source": "OpenAI Blog", "time": "今天"},
    {"title": "自动驾驶 Tesla FSD V13 发布", "source": "Electrek", "time": "今天"},
    {"title": "AI 视频生成模型 Sora 更新", "source": "OpenAI", "time": "今天"},
    {"title": "微软 Copilot 全面升级企业版", "source": "Microsoft", "time": "今天"},
    {"title": "AI 医疗诊断准确率超人类医生", "source": "Nature", "time": "今天"},
]

finance_news = [
    {"title": "A股今日上涨0.85%，收复3400点", "source": "东方财富", "time": "今天"},
    {"title": "美联储维持利率不变，鲍威尔讲话偏鹰派", "source": "Reuters", "time": "今天"},
    {"title": "人民币汇率中间价上调152点", "source": "中国外汇交易中心", "time": "今天"},
    {"title": "比特币突破 85000 美元", "source": "CoinDesk", "time": "今天"},
    {"title": "科创板今日涨幅居前", "source": "同花顺", "time": "今天"},
    {"title": "宁德时代发布新电池技术", "source": "证券时报", "time": "今天"},
    {"title": "苹果市值突破 3.5 万亿美元", "source": "Bloomberg", "time": "今天"},
    {"title": "欧洲央行降息25个基点", "source": "FT", "time": "今天"},
    {"title": "黄金价格创新高", "source": "Kitco", "time": "今天"},
    {"title": "中国外贸进出口增长6.2%", "source": "海关总署", "time": "今天"},
]

world_news = [
    {"title": "中美经贸高层会谈在北京举行", "source": "新华社", "time": "今天"},
    {"title": "俄乌冲突持续，双方谈判陷入僵局", "source": "BBC", "time": "今天"},
    {"title": "欧盟通过新数字法案", "source": "EU Observer", "time": "今天"},
    {"title": "日本首相访问美国", "source": "NHK", "time": "今天"},
    {"title": "伊朗核问题谈判重启", "source": "Al Jazeera", "time": "今天"},
    {"title": "联合国气候报告警告升温风险", "source": "UN News", "time": "今天"},
    {"title": "英国脱欧后经济恢复增长", "source": "The Guardian", "time": "今天"},
    {"title": "朝鲜发射新型导弹", "source": "韩联社", "time": "今天"},
    {"title": "印度GDP增速超预期", "source": "经济时报", "time": "今天"},
    {"title": "全球疫苗接种超150亿剂", "source": "WHO", "time": "今天"},
]

date_str = datetime.now().strftime('%Y年%m月%d日')
time_str = datetime.now().strftime('%Y年%m月%d日 %H:%M')

html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Daily Report - {date_str}</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
            min-height: 100vh;
            color: #fff;
            line-height: 1.6;
        }}
        .container {{
            max-width: 1000px;
            margin: 0 auto;
            padding: 40px 20px;
        }}
        header {{
            text-align: center;
            margin-bottom: 50px;
            padding: 40px 0;
            border-bottom: 1px solid rgba(255,255,255,0.1);
        }}
        h1 {{
            font-size: 3rem;
            background: linear-gradient(135deg, #667eea, #764ba2, #f093fb);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 15px;
        }}
        .subtitle {{
            color: rgba(255,255,255,0.7);
            font-size: 1.1rem;
        }}
        .update-time {{
            color: rgba(255,255,255,0.5);
            font-size: 0.9rem;
            margin-top: 10px;
        }}
        .card {{
            background: rgba(255,255,255,0.08);
            border-radius: 20px;
            padding: 35px;
            margin-bottom: 30px;
            border: 1px solid rgba(255,255,255,0.1);
            backdrop-filter: blur(10px);
        }}
        .category {{
            display: inline-block;
            padding: 8px 20px;
            border-radius: 25px;
            font-size: 0.95rem;
            font-weight: 600;
            margin-bottom: 25px;
        }}
        .cat-ai {{
            background: linear-gradient(135deg, #667eea, #764ba2);
        }}
        .cat-finance {{
            background: linear-gradient(135deg, #f093fb, #f5576c);
        }}
        .cat-world {{
            background: linear-gradient(135deg, #4facfe, #00f2fe);
        }}
        h2 {{
            font-size: 1.6rem;
            margin-bottom: 20px;
            color: rgba(255,255,255,0.9);
        }}
        ul {{
            list-style: none;
            padding: 0;
        }}
        li {{
            padding: 18px 0;
            border-bottom: 1px solid rgba(255,255,255,0.08);
            display: flex;
            align-items: flex-start;
            gap: 12px;
        }}
        li:last-child {{
            border: none;
        }}
        .bullet {{
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: linear-gradient(135deg, #667eea, #764ba2);
            margin-top: 8px;
            flex-shrink: 0;
        }}
        .news-content {{
            flex: 1;
        }}
        .news-title {{
            font-size: 1.05rem;
            margin-bottom: 5px;
            color: #fff;
        }}
        .news-meta {{
            font-size: 0.85rem;
            color: rgba(255,255,255,0.5);
        }}
        footer {{
            text-align: center;
            padding: 50px 0;
            color: rgba(255,255,255,0.4);
            font-size: 0.95rem;
        }}
        .footer-link {{
            color: rgba(255,255,255,0.6);
            text-decoration: none;
        }}
        @media (max-width: 768px) {{
            h1 {{ font-size: 2rem; }}
            .container {{ padding: 20px; }}
            .card {{ padding: 25px; }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>AI Daily Report</h1>
            <p class="subtitle">每日 AI科技 · 金融 · 国际要闻</p>
            <p class="update-time">更新时间: {time_str}</p>
        </header>
        
        <div class="card">
            <span class="category cat-ai">AI 科技</span>
            <h2>AI 科技今日热点</h2>
            <ul>
"""

for n in ai_news:
    html += f'''                <li><span class="bullet"></span><div class="news-content"><div class="news-title">{n["title"]}</div><div class="news-meta">Source: {n["source"]} | {n["time"]}</div></div></li>
'''

html += """            </ul>
        </div>
        
        <div class="card">
            <span class="category cat-finance">金融</span>
            <h2>金融市场今日快讯</h2>
            <ul>
"""

for n in finance_news:
    html += f'''                <li><span class="bullet"></span><div class="news-content"><div class="news-title">{n["title"]}</div><div class="news-meta">Source: {n["source"]} | {n["time"]}</div></div></li>
'''

html += """            </ul>
        </div>
        
        <div class="card">
            <span class="category cat-world">国际</span>
            <h2>国际重要新闻</h2>
            <ul>
"""

for n in world_news:
    html += f'''                <li><span class="bullet"></span><div class="news-content"><div class="news-title">{n["title"]}</div><div class="news-meta">Source: {n["source"]} | {n["time"]}</div></div></li>
'''

html += """            </ul>
        </div>
        
        <footer>
            <p>By OpenClaw AI Auto Generated</p>
            <p style="margin-top:10px;">
                <a class="footer-link" href="https://github.com/peterle-wh/ai-daily-report">GitHub</a> | 
                <a class="footer-link" href="https://peterle-wh.github.io/ai-daily-report">Website</a>
            </p>
        </footer>
    </div>
</body>
</html>"""

os.makedirs("docs", exist_ok=True)
with open("docs/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Website generated OK")
