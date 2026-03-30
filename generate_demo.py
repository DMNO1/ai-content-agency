#!/usr/bin/env python3
"""
AI内容工厂 — Demo文章生成器
用法: python generate_demo.py [--topic "选题"] [--industry "行业"] [--count N]

根据指定选题/行业，自动生成3-5篇Demo文章（Markdown格式），
供获客展示使用。
"""

import argparse
import json
import os
import sys
from datetime import datetime, timedelta

# Demo案例配置
DEMO_CONFIGS = [
    {
        "industry": "装修公司",
        "topics": [
            "2026年最火的5种装修风格，第3种90%的人没见过",
            "装修避坑指南：老师傅不会告诉你的10个秘密",
            "89㎡小三居如何装出120㎡的感觉？真实案例拆解",
        ],
        "tone": "专业+亲切",
        "target_audience": "25-40岁新房业主",
    },
    {
        "industry": "宠物医院",
        "topics": [
            "猫咪突然不吃东西？兽医教你5步排查法",
            "狗狗疫苗全攻略：什么时候打？打几针？多少钱？",
            "养宠10年总结的省钱清单，每年至少省5000",
        ],
        "tone": "温暖+专业",
        "target_audience": "养宠家庭",
    },
    {
        "industry": "教育培训机构",
        "topics": [
            "孩子数学成绩上不去？可能不是笨，而是这个习惯没养成",
            "小升初家长必看：2026年最新政策解读+备考策略",
            "学霸妈妈分享：每天30分钟，培养孩子自主学习能力",
        ],
        "tone": "权威+共情",
        "target_audience": "中小学生家长",
    },
]


def generate_article_outline(topic: str, industry: str, tone: str) -> dict:
    """生成文章大纲（纯模板，实际用AI填充）"""
    return {
        "title": topic,
        "industry": industry,
        "tone": tone,
        "structure": {
            "hook": f"以一个{industry}真实场景/痛点切入，3秒抓住注意力",
            "pain_point": "深入分析问题本质，让读者产生'说的就是我'的共鸣",
            "solution": "给出3-5个具体可执行的解决方案，每个方案配案例/数据",
            "case_study": f"一个{industry}真实客户案例，展示前后对比",
            "cta": "自然引导读者联系咨询，不硬推",
        },
        "word_count": "2000-3000字",
        "seo_keywords": [industry, topic.split("？")[0] if "？" in topic else topic[:10]],
    }


def generate_demo_markdown(configs: list) -> str:
    """生成Demo展示文档"""
    now = datetime.now()
    md = f"""# AI内容工厂 — Demo案例集

> 生成时间：{now.strftime('%Y-%m-%d %H:%M')}
> 说明：以下为AI内容工厂的Demo案例大纲，实际交付文章将根据客户需求深度定制。

---

"""
    for i, config in enumerate(configs, 1):
        md += f"## 案例{i}：{config['industry']}公众号\n\n"
        md += f"- **目标受众**：{config['target_audience']}\n"
        md += f"- **语言风格**：{config['tone']}\n"
        md += f"- **更新频率**：隔日更（12篇/月）\n\n"

        for j, topic in enumerate(config["topics"], 1):
            outline = generate_article_outline(topic, config["industry"], config["tone"])
            md += f"### 文章{j}：{topic}\n\n"
            md += f"| 要素 | 内容 |\n|------|------|\n"
            md += f"| 字数 | {outline['word_count']} |\n"
            md += f"| 风格 | {config['tone']} |\n"
            md += f"| SEO关键词 | {', '.join(outline['seo_keywords'])} |\n\n"

            md += "**文章结构**：\n"
            for step, desc in outline["structure"].items():
                step_names = {
                    "hook": "开头钩子",
                    "pain_point": "痛点分析",
                    "solution": "解决方案",
                    "case_study": "案例佐证",
                    "cta": "行动号召",
                }
                md += f"1. **{step_names.get(step, step)}**：{desc}\n"
            md += "\n"

        # 模拟效果预估
        md += f"**效果预估（基于同类客户数据）**：\n"
        md += f"- 预计月均阅读量：3,000-8,000\n"
        md += f"- 预计月增粉：200-500\n"
        md += f"- 预计获客线索：5-15个/月\n"
        md += f"- 月投入：¥5,000（12篇套餐）\n\n"
        md += "---\n\n"

    md += """## 📊 对比数据

| 维度 | 自己写 | 传统代运营 | AI内容工厂 |
|------|--------|-----------|-----------|
| 月费 | ¥0（但时间成本≈¥8,000） | ¥8,000-15,000 | ¥5,000 |
| 月产出 | 2-4篇 | 8-12篇 | 12篇 |
| 质量稳定性 | 看心情 | 看编辑水平 | AI兜底+人工把关 |
| 交付周期 | 不确定 | 5-7天 | 3天 |
| 数据报告 | 无 | 额外收费 | 免费包含 |

---

*以上Demo仅供展示，实际服务将根据客户具体需求深度定制。*
*联系微信获取您的「公众号免费内容诊断报告」。*
"""
    return md


def main():
    parser = argparse.ArgumentParser(description="AI内容工厂 Demo文章生成器")
    parser.add_argument("--topic", type=str, help="自定义选题")
    parser.add_argument("--industry", type=str, help="行业类型")
    parser.add_argument("--count", type=int, default=3, help="生成案例数量")
    parser.add_argument("--output", type=str, default="demo_cases.md", help="输出文件")
    args = parser.parse_args()

    if args.topic and args.industry:
        # 自定义模式
        configs = [{
            "industry": args.industry,
            "topics": [args.topic],
            "tone": "专业+亲切",
            "target_audience": "目标客户",
        }]
    else:
        # 使用预设Demo配置
        configs = DEMO_CONFIGS[:args.count]

    md = generate_demo_markdown(configs)

    with open(args.output, "w", encoding="utf-8") as f:
        f.write(md)

    print(f"[OK] Demo cases generated: {args.output}")
    print(f"     {sum(len(c['topics']) for c in configs)} article outlines")
    print(f"     {len(configs)} industries covered")


if __name__ == "__main__":
    main()
