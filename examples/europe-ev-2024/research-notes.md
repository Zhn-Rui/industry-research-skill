# Evidence and continuation · 证据与接续

Edited public display copy, not an original run artifact. Original access: 21 October 2026; research period: 2024 versus 2023. Source-reading statements below describe the saved trial records, not source access newly performed for this edition. No historical tool log or approval is reproduced.

整理后的公开展示副本，非原运行产物。原资料访问日2026年10月21日；研究期间2024对比2023。下方读取状态描述保存记录，不表示本次重新访问；不复制历史工具日志或批准。

## English reading guide

- **Trace:** S01 ACEA PDF p. 4, YEAR TO DATE / EU / BEV → E01: 1,538,106 (2023), 1,447,934 (2024) → C01: EU27 annual new BEV registrations fell 5.9%. Recalculate `100 × (1447934 / 1538106 − 1)`; do not generalise to every country's demand.
- **Conflict:** X01 compares ACEA decline with S02 IEA stagnation. E07 identifies different geography and powertrains. Keep both scoped observations; exact same-version quantities remain missing (B01). X03 records electrive's 381,907 UK BEVs versus ACEA/SMMT's 381,970; use the original statistics' matching value, while leaving the cause of the 63-car discrepancy unconfirmed.
- **Rejected inference:** C08 cannot claim a UK private-BEV decline of 8.7%. E12's denominator is all-powertrain private registrations. A two-year private-by-BEV cross-tab is missing. C06/C09 also cannot identify universal preference retreat or a sole policy cause.
- **State:** The saved run reached bounded final text delivery after a G3 handoff. The public reports retain the same claim boundaries; this edition has no new research-stage approval. B01–B04 remain open. See the continuation section below and [resume prompt](resume-prompt.md).

The following source, evidence, conflict, claim and gap extracts retain the original IDs. Chinese detail is retained for inspection; the English guide and report explain the key decisions. Annual numerical inputs selected for this edition are in [data.json](data.json); they are factual transcriptions, not bundled third-party tables.

以下保留原S/E/X/C/B编号，便于核对。所选年度输入见[data.json](data.json)，不附原始第三方表格。公开版不声称这些来源相互独立或已获本轮重新认证。

## 3. S：来源与读取状态

正文定位以标题/表/行名为权威，web行号只是本次返回的辅助定位，接续者不需要本次工具引用ID。

| S | 标题、发布者、日期 | URL与精确定位 | 类型、验证、家族、覆盖限制 |
|---|---|---|---|
| S01 | New car registrations: +0.8% in 2024; battery-electric 13.6% market share；ACEA；2025-01-21 | https://www.acea.auto/pc-registrations/new-car-registrations-0-8-in-2024-battery-electric-13-6-market-share/ ，Electric cars节；附属原表 https://www.acea.auto/files/Press_release_car_registrations_December_2024.pdf ，印刷页4（零基页3），NEW CAR REGISTRATIONS BY MARKET AND POWER SOURCE / YEAR TO DATE，Jan-Dec 2024/2023，EU、EU+EFTA+UK、Germany、UK等行；注1 | 行业协会聚合统计，HTML及年度PDF表正文实际读取，非全文逐页读。家族F-ACEA，由国家协会/会员/S&P数据聚合；英国行与S05不独立。PDF页1列明2025-01-21发布。注册量是市场成交代理，不能直接识别消费者偏好因果。页3是12月，不能误用。原试用未完成原PDF独立视觉检查；保存的定量依据为PDF文本表头及行。 |
| S02 | Trends in electric car markets / Global EV Outlook 2025；IEA；2025年5月，所读PDF注明2025年7月修订 | https://www.iea.org/reports/global-ev-outlook-2025/trends-in-electric-car-markets-2 ，In Europe, electric car sales stagnated in 2024…节及图下注；附属 https://iea.blob.core.windows.net/assets/7ea38b60-3033-42a6-9589-71134f4229f4/GlobalEVOutlook2025.pdf ，印刷页15脚注1、167 Annex C Europe、末尾版权页（零基页171） | 政府间机构分析；网页相关段落、PDF定义/地区附录/修订信息实际读取，未全读173页。家族F-IEA-多源；图源含ACEA、EAFO、EV Volumes、Marklines与国家提交，并非ACEA独立复现。不是2024时点快照，修订前差异未核验。 |
| S03 | More new electric cars than diesel registered across the EU；electrive / Chris Randall；2025-01-21 11:30 | https://www.electrive.com/2025/01/21/more-new-electric-cars-than-diesel-registered-across-the-eu/ ，Specifically…、However, if the EFTA…、This shows…连续段（本次行80–90） | 行业报道；正文实际读取。数字家族F-ACEA，不能作为第二独立统计。用于保留报道叙述及异常；文章某UK总量与原表冲突，见X03。文中预测段不进入研究。 |
| S04 | United Kingdom: becomes largest BEV market in Europe with 19,6% market share in 2024；EAFO新闻；2025-01-15 | https://alternative-fuels-observatory.ec.europa.eu/general-information/news/united-kingdom-becomes-largest-bev-market-europe-196-market-share-2024 ，EV Market Trends、Barriers to Growth，页末Source:SMMT | 机构平台刊载的新闻转述；正文与Source链接实际读取。家族F-SMMT，不独立；页脚明示观点不代表欧委会。英国范围，不代表欧洲所有私人买家。 |
| S05 | Record EV market share but weak private demand frustrates ambition；SMMT；2025-01-06 | https://www.smmt.co.uk/record-ev-market-share-but-weak-private-demand-frustrates-ambition/ ，Full year 2024 by fuel type / Year to date表，BEV/PHEV/HEV行；Full year 2024 by sales type表；One of the major constraints…与Conversely…段（本次行303–313、330–334、363–368） | 英国行业协会统计兼政策倡议；相关HTML原表与正文实际读取。家族F-SMMT，与S04/ACEA英国行重合。行业“支持不可持续”等判断是利益相关方陈述，不自动证明市场机制；全市场private下降不是private BEV下降。 |

访问日均为2026-10-21。没有下载/再分发全文；这些URL与定位及下列小量事实记录构成接续依据。主要来源5份，独立性不能按5投票：S03继承S01，S04继承S05，S02也部分继承这些基础统计。

## 4. E：原子证据

数字以辆为单位，变化率分母均为2023同口径年度值，除非另注。事实记录采用转述；英文短摘录仅保留必要词语。

| E | S/locator | 原子观察与直接性 | 对象/地区/期间/分母 |
|---|---|---|---|
| E01 | S01 PDF页4 EU行 BEV | 2024 1,447,934；2023 1,538,106；表列-5.9%。直接统计。 | EU新乘用车BEV，全年同比 |
| E02 | S01 PDF页4 EU+EFTA+UK行 BEV | 1,993,102 vs 2,018,885；-1.3%。直接统计。 | 该31国表覆盖新乘用车BEV，全年同比 |
| E03 | S01 PDF页4 EU及EU+EFTA+UK行 PHEV | EU 758,944 vs 814,294（-6.8%）；较广口径952,058 vs 990,749（-3.9%）。直接统计。 | 各自地区新乘用车PHEV，全年同比 |
| E04 | S01 PDF页4 Total列 EU及较广地区行 | EU 10,632,381 vs 10,548,165（+0.8%）；较广地区12,963,614 vs12,847,929（+0.9%）。 | 全动力新乘用车年度流量，不能充当EV分子 |
| E05 | S01 PDF页4 Germany、UK、Norway、Belgium行 | BEV德国-27.4%、英国+21.4%、挪威+9.4%、比利时+36.9%。直接国家反例。 | 国家间异质性；年度BEV注册变化 |
| E06 | S02 网页Europe节 | 原文“electric car sales stagnated in 2024”；销售占比约五分之一，与2023相近。机构分析而非精确零增长值。 | IEA Europe新乘用车BEV+PHEV；占比分母全动力新车，不是保有量 |
| E07 | S02 PDF页15脚注1、167 Annex C | EV同时含BEV与PHEV，不含FCEV；Europe含EU、冰岛/挪威/瑞士/UK，以及阿尔巴尼亚、白俄罗斯、波黑、直布罗陀、以色列、科索沃、黑山、北马其顿、摩尔多瓦、塞尔维亚、土耳其、乌克兰。直接方法注。 | 定义证据；不是销量观察。IEA地区比ACEA表广 |
| E08 | S02 网页Europe节补贴/CO2段 | IEA将停滞与部分大市场补贴减少联系；亦称EU排放目标阶梯设计可能抑制2024增长。 | 机构对2024机制的解释；非对原因份额的识别研究，不跨入2025预测 |
| E09 | S03 上述连续段 | 报道并列EU BEV下跌、加入UK/EFTA跌幅收窄、国家分化。 | 与E01/E02/E05同家族，背景与叙事保留，不能增加独立置信度 |
| E10 | S03 This shows…段 | UK BEV报道写381,907；S01/S05均381,970。 | 同年度国家BEV数量的文本不一致，差63辆 |
| E11 | S05 年度fuel type表；S04 EV Market Trends转述 | UK BEV381,970 vs314,687（+21.4%）；PHEV167,178 vs141,311（+18.3%）。直接统计，S04为转述。 | UK年度新乘用车；不能推广至EU |
| E12 | S05 年度sales type表及367–368段 | 全动力private746,276、-8.7%；全动力fleet1,163,855、+11.8%；约一成private买家选BEV；business+fleet BEV同比多约64,000。 | -8.7%分母是全部私人新车注册，非私人BEV；“一成”是当年横截面占比 |
| E13 | S05 363段、S04 Barriers转述 | SMMT称2024厂家折扣超过£4.5bn且长期不可持续。 | 行业陈述；本研究未独立核验估计方法，不直接证明真实意愿变化 |
| E14 | S01 PDF页4注1与UK Hybrid electric列；S05年度HEV表 | ACEA UK hybrid electric689,973、+14.8%，注含full和mild；SMMT HEV261,398、+9.6%。 | 同国家但动力类别统计集合不同迹象；SMMT mild具体归属未在所读段确证，不强行相减当独立类别 |

## 5. 定量处理与可重算依赖

[data.json](data.json)保存本例所选年度输入（不包含原试用全部序列）；其余观察按下表来源定位，不另造计算结果。公式：同比%=100×(2024/2023−1)，台数差=2024−2023；同地同年度BEV+PHEV分别相加后用相同公式。无汇率、价格模型或市场规模外推。

同ACEA口径相加：EU BEV+PHEV约-6.19%；EU+EFTA+UK约-2.14%。这是自行计算，不能署为IEA精确结果，也不能把HEV加进EV。本展示副本未纳入原记录的剔除德国运算；不以此构造政策反事实。

输入的注册台数具有相同期间、类别及表内地理加总基础；不是跨来源拼接估算。“约20%”为来源约数，未倒算精确IEA总量。国家例子不按数量多数推断区域加权方向。

## 6. X：表面矛盾、反证与冲突裁决

- X01，E01/E02 vs E06：下降与停滞不是同命题的直接互斥证据。地理不同、BEV vs BEV+PHEV不同，“stagnated”还可表示近乎持平。用E07定义定位解释；未把IEA改写为0.0%，也未证明所有差异完全由地域或动力类型解释。IEA精确年度量未提取，残余大小未统一核算（B01）。
- X02，E01/E02 vs E05/E11：真实国家反例，足以反驳“欧洲每国BEV都下降”，不反驳加总的下降；注册台数须加权，不能国家增长率取平均。
- X03，E10 vs E11：同口径UK BEV差63辆。原始SMMT和ACEA一致，工作数字采用381,970；electrive异常保留，可能转写错误但未向作者求证，不宣称已知道错误成因。
- X04，S05标题“weak private demand” vs E11：英国BEV整体创新高与私人端表现不足可以并存。E12的private-8.7%指全动力私人新车，不能据此称私人BEV同比下降；约一成份额也不证明同比下降。
- X05，E14：HEV增幅不一致存在分类范围差异线索。ACEA注释明确full+mild，SMMT类别较窄但mild归属未确证，作为未完全解决的分类冲突保留（B03）；不影响BEV/PHEV年度判断，不准用它证明所有“电动化”动力同向。

## 7. C：保存的主张边界（展示副本）

这里展示原检查点的主张裁决；最终读者报告另见 report.md 与 report.zh-CN.md。

| C | 完整命题 | 支持/反驳/背景E | 裁决与置信度依据 | 限定/报告准入 |
|---|---|---|---|---|
| C01 | 2024比2023，EU27新乘用车BEV注册量收缩约5.9%。 | 支持E01；背景E09 | 有依据，高：原始年度表与重算一致，转述不额外计票。 | 可用；必须写EU、BEV、新车注册量、年度 |
| C02 | 在ACEA EU+EFTA+UK范围，全年BEV注册量也收缩，但仅约1.3%。 | 支持E02；背景E09 | 有依据，高：同表同期间同分类。 | 可用；不可省地域让读者误以为整个地理欧洲 |
| C03 | 将插混计入同ACEA地区新电动车，年度注册量仍下降（EU约6.2%，较广地区约2.1%）。 | 支持E01/E02/E03及计算 | 有依据，高：同源可加总分类，算术核验。 | 附条件：标明自行计算BEV+PHEV，排除HEV/FCEV |
| C04 | 2024欧洲所有国家电动车需求都在下降。 | 反驳E05/E11；背景E06 | 不成立，高：多个国家BEV年度量增长；“需求”还超出注册观察。 | 不可用；允许改写为国家表现分化 |
| C05 | IEA对其更广Europe、BEV+PHEV口径的概括是2024停滞，不能据此否定C01/C02。 | 支持E06/E07；背景E01/E02 | 有依据，中高：定义已核；“停滞”不是精确0，尚无统一数量桥接。 | 附条件：归属IEA判断、保留口径及B01，不能声称全欧严格零增长 |
| C06 | 新车注册下降证明欧洲消费者对电动车的根本偏好全面倒退。 | 仅背景E01/E02/E08/E13；反驳普遍性E05/E11 | 证据不足：价格、税制、补贴、供给及渠道均未被控制，区域/私人覆盖不足。 | 不可用；只能称已实现年度市场流量减弱 |
| C07 | 2024英国BEV总量增长与私人端被行业称为疲弱并存，增长包含明显车队/商业购买贡献。 | 支持E11/E12；背景E13 | 有依据，中高：总量和约64,000渠道增量直接载于SMMT；行业疲弱定性须归属。 | 附条件：限定UK、区分全动力private下降与BEV私人表现，不外推欧洲消费者 |
| C08 | 2024英国私人BEV注册量同比下降8.7%。 | 反驳分母E12；背景E11 | 不获支持，高：把全动力私人分母换成BEV分母。 | 不可用；未取得私人BEV完整年度交叉表 |
| C09 | 德国补贴撤除是2024欧洲EV收缩的唯一原因或已量化主要因果贡献。 | 仅背景E05/E08；反驳“唯一充分”方向E05/E11 | 证据不足：存在机构机制解释，未识别反事实或拆分贡献；剔除德国是描述算术。 | 不可用作因果断言；可归属IEA“部分政策支持退坡相关解释” |
| C10 | 因为电动车注册下降，欧洲整个新车市场也同比收缩。 | 反驳E04；背景E01/E02 | 不成立，高：全动力分母在两个ACEA区域均小幅增长。 | 不可用；EV子市场与全市场分开 |

“高/中高”是主张置信度的自报理由，不是给研究打分，也不是来源独立性或外部审查结论。

## 8. B：缺口、尝试与停止处置

| B | 影响问题/C | 需要什么才足够 | 已做/停止 | 下游处置 |
|---|---|---|---|---|
| B01 | Q1/C05，IEA与ACEA精确桥接 | 同版本IEA2023/24 Europe BEV/PHEV数量及国家分项可重聚合 | 读IEA定义脚注、Annex C，已明确边界；未取数据下载，有限任务已有足够支持有界回答，停止扩搜 | 不量化IEA与ACEA差值，不声称矛盾全解或IEA严格零增长 |
| B02 | Q3/C06/C08/C09 | 各国×渠道×动力2023/24交叉量、可比价格/政策/供给/订单及因果识别 | 读取SMMT渠道与动力表但无完整交叉；机构归因未追溯所有政策原件。窄任务与预算不扩为需求建模 | 明确不能推断全欧私人意愿普遍下降、单因果、长期趋势或预测 |
| B03 | X05/HEV扩展命题 | SMMT当年mild分类方法与可比重分类表 | 对照ACEA注1和SMMT HEV行，已发现分类线索；没有继续补查 | 争议保留；HEV不入BEV/PHEV合计，不影响C01–03 |
| B04 | 历史时点核验 | IEA2025年5月原始版与7月修订说明；若用户坚持仅2024发表，则需改任务 | 当前PDF明确7月修订，尚未历史版本比对；无需为窄年度观察追修订链 | 正文应列真实版本/发布日期，不能声称使用2024年底已知资料 |


## Continuation state · 接续状态

The bounded report is complete for reading. There is no pending task required to support its narrow registration finding. Extending to harmonised Europe totals or causal demand analysis requires a new scope and tool budget. The original continuation relied on saved evidence for detailed tables; the original offline review did not independently re-fetch all sources. This edition's checks concern the exported artifacts and arithmetic, not historical execution authenticity.

当前窄范围报告已完成，可供阅读；没有为支持现有注册量结论而必须补做的待办。若扩展统一欧洲总量或需求因果，需要另定范围和工具预算。原接续的详细表格仍依赖保存证据，原离线评阅未独立重取所有来源。本公开版检查仅针对导出文件与算术，不认证历史执行真实性。

Next supported step: read the two reports, this record and data.json; verify scope and arithmetic; select one open gap (for example B01), then seek same-version IEA annual quantities and country/powertrain definitions if browsing is available. Preserve both source series until a reproducible bridge exists. Without browsing, list missing inputs and leave the gap open.

下一步：核对报告、本记录和数据；先复算并确认范围，再选择一个缺口（如B01）。有检索能力时获取同版本IEA年度数量及国家/动力定义，完成可重算桥接前保留两套统计。不具备联网读取能力时，只列所缺输入，不关闭缺口。
