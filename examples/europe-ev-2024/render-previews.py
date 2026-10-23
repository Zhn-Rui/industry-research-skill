"""Deterministic text/table layout. Python 3 + Pillow; no network or generative images.
Usage: python3 render-previews.py
Set DEMO_FONT to a CJK-capable TrueType/OpenType font on other systems.
The default macOS STHeiti font is a system dependency, not redistributed.
"""
import json
import os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
P = Path(__file__).resolve().parent
FONT = os.environ.get('DEMO_FONT', '/System/Library/Fonts/STHeiti Medium.ttc')
D = json.loads((P / 'data.json').read_text())
ROWS = ['EU_BEV', 'EU_BEV_plus_PHEV', 'Europe_ACEA_BEV', 'Europe_ACEA_BEV_plus_PHEV']

def render(lang):
    zh = lang == 'zh-CN'
    im = Image.new('RGB', (1200, 1240), '#f2f5fa')
    d = ImageDraw.Draw(im)
    def text(x, y, t, size=32, color='#14283f'):
        f = ImageFont.truetype(FONT, size)
        d.text((x, y), t, font=f, fill=color)
    def wrap(y, t, size=34, width=1060):
        f = ImageFont.truetype(FONT, size)
        lines = []; line = ''
        units = list(t) if zh else t.split(' ')
        for unit in units:
            trial = line + ('' if zh or not line else ' ') + unit
            if d.textlength(trial, font=f) > width:
                lines.append(line); line = unit
            else:
                line = trial
        lines.append(line)
        for line in lines:
            text(70, y, line, size); y += int(size * 1.45)
        return y
    d.rectangle((0, 0, 1200, 16), fill='#087f8c')
    text(70, 54, 'INDUSTRY RESEARCH  /  HISTORICAL EXAMPLE', 25, '#087f8c')
    y = wrap(118, '2024年欧洲电动乘用车市场是否整体收缩？' if zh else 'Did the European electric passenger-car market shrink in 2024?', 48)
    text(70, y + 18, '2024 vs 2023  |  原资料访问：2026-10-21' if zh else '2024 vs 2023  |  Original source access: 2026-10-21', 26)
    y = wrap(y + 86, 'ACEA覆盖地区注册量下降；尚不能证明欧洲需求全面收缩。' if zh else 'Registrations fell in ACEA-covered regions; universal demand contraction is unproven.', 37)
    y += 35
    text(70, y, '新乘用车注册量同比变化' if zh else 'Annual change in new passenger-car registrations', 29)
    y += 59
    d.rounded_rectangle((60, y-15, 1140, y+332), radius=15, fill='white')
    text(85, y, '地区 / 动力' if zh else 'Region / powertrain', 28)
    text(890, y, '同比' if zh else 'Change', 28)
    labels = ['EU27 · BEV', 'EU27 · BEV+PHEV*', 'EU+EFTA+UK · BEV', 'EU+EFTA+UK · BEV+PHEV*']
    for i, (key, label) in enumerate(zip(ROWS, labels)):
        yy=y+63+i*66
        d.line((85, yy-14, 1110, yy-14), fill='#e0e7ef', width=2)
        text(85, yy, label, 32)
        pct=100*(D[key]['2024']/D[key]['2023']-1)
        text(890, yy, f'−{abs(pct):.1f}%', 36, '#a43c35')
    y += 365
    y=wrap(y, '*同地区BEV与PHEV相加后计算；不含普通混动。' if zh else '*BEV+PHEV totals calculated within each region; HEVs excluded.', 25)
    y=wrap(y+22, '重要限制：注册量不是消费者偏好；IEA与ACEA的精确数量桥接尚未完成。' if zh else 'Limit: registrations do not identify preferences. The exact IEA–ACEA quantity bridge remains open.', 29)
    y=wrap(y+22, '来源：ACEA，2025-01-21，年度PDF第4页；IEA，Global EV Outlook 2025。' if zh else 'Sources: ACEA, 21 Jan 2025, annual PDF p. 4; IEA, Global EV Outlook 2025.', 24)
    y=wrap(y+15, '整理展示副本 · 完整报告与证据链接见案例目录' if zh else 'Edited display copy · Full report and evidence links in the example folder', 23)
    assert y < 1215, f'Content overflow: {y}'
    im.save(P / f'preview.{lang}.png')

if __name__ == '__main__':
    render('en'); render('zh-CN')
