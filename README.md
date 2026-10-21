# Industry Research Skill · 行业研究技能

Conduct traceable, reviewable, and resumable industry research with Codex.
用 Codex 开展可追溯、可审查、可接续的行业研究。

[纯中文文档](README.zh-CN.md)

[Quick Start · 上手](#quick-start--快速开始) · [Examples · 示例](#usage-examples--使用示例) · [Resume · 接续](#resume-research--跨会话接续) · [Validation · 验证](#validation-and-limitations--验证与局限) · [License · 许可](#origin-license-and-feedback--来源许可与反馈)

## Overview · 项目简介

A structured workflow that helps Codex turn scattered research materials into evidence-traceable, bounded conclusions and saved records that another session can continue.

这是一个结构化研究工作流，帮助 Codex 将分散材料整理为依据可追溯、结论有边界、能够跨会话接续的研究记录与报告。

## Who It Is For · 适用人群与任务

For industry and market analysts; strategy, consulting, and business analysts; founders and product managers; and students and independent researchers doing business research.

Applicable tasks include industry or segment research, market and competitive landscape mapping, multi-source synthesis, preliminary evidence assessment of business opportunities, and review or continuation of existing research. These are intended use cases, not separately tested scenarios. A single factual lookup or formatting an existing report rarely needs the full workflow.

面向行业与市场分析人员；战略、咨询及商业分析人员；创业者和产品经理；开展商业研究的学生与独立研究者。

适用任务包括行业或细分市场研究、市场与竞争格局梳理、多来源材料综合、商业机会的初步证据评估，以及已有研究的审阅与接续。这些是适用场景，不代表每个场景都已分别通过测试。单条事实查询或已有报告排版通常不需要完整流程。

## Core Features · 核心功能

- **Trace important conclusions to evidence.** Record sources, definitions, periods, units, and support for claims so readers can inspect the basis.
- **Keep conflicts, assumptions, and unknowns visible.** Stage reviews and bounded conclusions prevent polished prose from hiding unresolved evidence.
- **Continue in a new session.** Save scope, evidence, review decisions, artifact locations, and a continuation index; the next session checks the actual records before proceeding.

One English runtime includes a main Skill, four references, and six optional templates. Commercial parameters, simple scenarios, and analysis of supplied interview material are conditional modules. Human judgment remains necessary for scope, evidence sufficiency, conflicts, and decisions.

- **重要结论可追溯到依据。** 记录来源、口径、期间、单位及其对主张的支持，便于读者检查结论基础。
- **冲突、假设和未知保持可见。** 通过阶段审查和有边界的结论，避免流畅写作掩盖未解决的证据问题。
- **新会话能够继续研究。** 保存范围、证据、审查决定、产物位置和接续索引；下一会话先核对实际记录再继续。

仅维护一套英文运行时，包括主 Skill、四份参考文件和六份按需模板。商业参数、简单情景及所提供访谈材料的分析按需启用。范围、证据充分性、冲突处置和决策仍需要人工判断。

## Quick Start · 快速开始

**English**

1. Download the repository ZIP using GitHub's **Code → Download ZIP** and extract it, or clone using the commands below.

   Downloading or cloning does not automatically install or enable the Skill.
2. Open the extracted or cloned folder in Codex. Ask Codex to read and follow [skills/industry-research/SKILL.md](skills/industry-research/SKILL.md).
3. Supply your topic, scope (region, period, cutoff date), questions, available materials, allowed tools, and output directory. The example below is ready to copy.
4. Read the report and its limitations in your chosen output directory. Check the evidence and review records, then ask Codex to investigate gaps or continue from the saved continuation index.

**中文**

1. 在 GitHub 点击 **Code → Download ZIP** 并解压，或使用下方命令克隆。

   下载或克隆不等同于自动安装或启用 Skill。
2. 在 Codex 中打开解压或克隆后的目录，请其读取并遵循 [skills/industry-research/SKILL.md](skills/industry-research/SKILL.md)。
3. 提供主题、范围（地区、期间、资料截止日）、问题、已有材料、允许的工具和输出目录。下方示例可以直接复制。
4. 在指定输出目录查看报告与局限，检查证据和审查记录；随后让 Codex 补充缺口，或根据保存的接续索引继续研究。

```sh
git clone https://github.com/Zhn-Rui/industry-research-skill.git
cd industry-research-skill
```

## Usage Examples · 使用示例

```text
Read and follow skills/industry-research/SKILL.md. Research the 2024 European passenger electric-vehicle market and summarize market changes and the competitive landscape. Use only the materials I provide next; do not browse. Prefer concise mode, write in English to research-output/, and first check scope and material sufficiency. Distinguish supported conclusions, conflicts, assumptions, and unknowns. Keep evidence references, review records, and a continuation index for a new session. Disclose gaps without inventing facts.
```

This prompt illustrates usage; it is not an additional test result. Provide the materials before evidence collection begins. For new public-source research, explicitly allow search and original-source reading in a capable Codex environment.

```text
请读取并遵循 skills/industry-research/SKILL.md。研究 2024 年欧洲乘用电动车市场，梳理市场变化与竞争格局；仅使用我随后提供的材料，不开展网络检索。优先精简模式，使用中文，输出到 research-output/。先确认范围和材料是否足够，区分有依据的结论、冲突、假设和未知，保留证据引用、审查记录与新会话接续索引。材料不足时披露局限，不补造事实。
```

此提示用于演示用法，不是新增测试结果。开始收集证据前需提供材料。如需研究新的公开资料，应明确允许检索及原文读取，并使用具备相应能力的 Codex 环境。

## Resume Research · 跨会话接续

Keep the output directory and make it accessible to the new Codex session together with this repository. Copy:

```text
Read and follow skills/industry-research/SKILL.md. Resume the research saved in research-output/. Read the continuation index, scope, evidence, and original reviews/decisions. Verify that the actual artifacts exist and statuses remain justified before continuing. Preserve unresolved failures and authorization limits; explain the next supported step.
```

Concise mode normally keeps the continuation index inside `research.md`; full mode may use separate records. An old PASS alone is not sufficient to resume. See [review and recovery](skills/industry-research/references/review-recovery.md).

保留输出目录，让新的 Codex 会话能够同时读取它与本仓库，然后复制：

```text
请读取并遵循 skills/industry-research/SKILL.md，接续 research-output/ 中的研究。先阅读接续索引、范围、证据和原始审查/决定，核对实际产物存在且状态仍有依据，再继续工作。保留未解决的失败与授权边界，说明下一步能够完成什么。
```

精简模式的接续索引通常位于 `research.md`，完整模式可使用独立记录。历史 PASS 本身不足以支持接续。详见 [审查与恢复](skills/industry-research/references/review-recovery.md)。

## Research Modes · 研究模式

| Mode | When to use | Organization |
|---|---|---|
| Concise | A narrow question, short output, few sources, no complex model | Normally one `research.md` containing scope, evidence, report, checks, and continuation; separate reader report if useful |
| Full | Multiple questions/regions/periods, complex evidence or modeling, a long report, or explicit user choice | Separate logical records and data tables when needed |

Record the choice and rationale. Templates define fields, not a six-file quota. Both modes require traceability, visible counterevidence and unknowns, limitations, and actual performance of claimed checks. Each logical record has one authoritative location.

| 模式 | 适用情况 | 组织方式 |
|---|---|---|
| 精简 | 窄问题、短输出、来源少、无复杂模型 | 通常一份 `research.md` 合并范围、证据、报告、检查与接续；必要时另列读者报告 |
| 完整 | 多问题/地区/时期、复杂证据或模型、长报告，或用户指定 | 按需分开维护逻辑记录与数据表 |

记录选择及依据。模板规定字段，不是六文件配额。两种模式都要求可追溯、反证与未知可见、局限披露，以及实际执行所声称的检查。每类逻辑记录只有一个权威位置。

## Capabilities and Fallbacks · 能力要求与降级

- Read material, write text, and inspect actual outputs. Without file writing, provide saveable text and disclose that it is not persisted.
- New public-source research needs search and original-source reading. Offline, use supplied material; unreadable sources remain leads.
- Quantitative conclusions need verifiable arithmetic; unrecomputed results remain unverified.
- Charts or paginated documents need creation, rendering, and viewing. Text extraction does not substitute for visual QA.
- Independent review/handoff needs an independent context. Otherwise disclose self-review only. No particular vendor tool, paid service, or global dependency is required.

The workflow currently targets Codex. Compatibility with other agent platforms has not been tested. It maintains one English runtime; deliverables follow the explicit language choice or, otherwise, the task language. Paths, IDs, and canonical status values stay stable, including established tokens such as `可用`, `已批准`, and `按例外关闭`.

- 读取材料、写文本并检查实际输出。不能写文件时提供可保存文本，披露尚未持久化。
- 新公开资料研究需要检索与原文读取。离线只使用已有材料；不可读来源仍为线索。
- 定量结论需要可核验计算；未可靠重算的结果保持未验证。
- 图表或分页文档需要制作、渲染与实际查看。文本提取不能替代视觉检查。
- 独立审阅/交接需要独立上下文，否则披露仅为自检。不依赖特定厂商工具、付费服务或全局依赖。

目前围绕 Codex 使用，未测试其他代理平台兼容性。仅维护一套英文运行时；交付语言优先遵循明确要求，否则跟随任务语言。路径、ID 和规范状态值保持稳定，包括 `可用`、`已批准`、`按例外关闭` 等既有值。

## Validation and Limitations · 验证与局限

Chinese historical versions had synthetic, full-depth, paired, and narrow real-source/handoff tests. Three historical paired cases showed no core quality-score improvement; artifacts were larger and reported elapsed times longer, with mixed tool-call changes. No claim of improved accuracy or reduced cost is supported.

The English runtime had semantic translation review and three offline synthetic recovery checks covering task/output language and preserved exception boundaries. Historical Chinese passes are not English-runtime passes. No English paired comparison or new real-source trial has been performed. See [docs/VALIDATION.md](docs/VALIDATION.md) for detailed methods, results, and qualifications.

Long-running or large-scale research, complex models, paginated visual delivery, and stable recovery without feedback remain insufficiently validated. The public summary does not independently reproduce all historical tests. This documentation update did not rerun the full research tests.

Human judgment remains necessary. The Skill does not provide paid databases, interview recruitment, or outreach by default, and does not promise automated investment decisions, professional due diligence, or fact certification. Tool and evidence limits constrain delivery.

中文历史版本进行过合成、完整深度、配对及窄范围真实来源/接续测试。三组历史配对未观察到核心质量评分提升；产物更大、自报时长更长，工具调用变化有升有降。不支持提高准确率或降低成本的宣称。

英文运行时进行过语义翻译审查，以及三次离线合成恢复检查，覆盖任务/输出语言和例外边界保留。中文历史通过不计作英文运行时通过；未进行英文配对对照或新的真实来源试用。详细方法、结果及限定见 [docs/VALIDATION.md](docs/VALIDATION.md)。

长周期或大规模研究、复杂模型、分页视觉交付及无反馈稳定恢复仍未充分验证。公开摘要不能独立复现全部历史测试。本次文档更新没有重跑完整研究测试。

人工判断仍然必要。不默认提供付费数据库、访谈招募或外联；不承诺自动完成投资决策、专业尽调或事实认证。工具与证据的局限会约束交付。

## Origin, License and Feedback · 来源、许可与反馈

The workflow originated in research on the embodied-intelligence data market and was later distilled for research in other industries. Private interviews, original reports, third-party source copies, and development history are excluded. See the [public file manifest](PUBLIC_FILES.md) and [release notes](RELEASE_NOTES.md).

Created by **Enrui Zhang**. This project is licensed under the [MIT License](LICENSE). The license covers this repository's project content; it does not grant rights to excluded original research, private interviews, or third-party material.

Use [GitHub Issues](https://github.com/Zhn-Rui/industry-research-skill/issues) to report problems or suggest improvements. Include the expected behavior, actual behavior, and a minimal sanitized example; do not upload private research, credentials, or unauthorized source material. No response-time or maintenance commitment is made.

该流程源自一次具身智能数据市场研究，随后被提炼为适用于其他行业的研究工作流。私人访谈、原始报告、第三方原文副本及开发历史均不公开。见 [公开文件清单](PUBLIC_FILES.md) 和 [发布说明](RELEASE_NOTES.md)。

作者：**Enrui Zhang**。本项目采用 [MIT 许可证](LICENSE)。许可适用于仓库内的项目内容，不授予被排除的原始研究、私人访谈或第三方材料的权利。

请通过[GitHub Issues](https://github.com/Zhn-Rui/industry-research-skill/issues) 报告问题或提出建议，附预期行为、实际行为和最小脱敏示例；请勿上传私人研究、凭据或未经授权的原始材料。不承诺响应时限或维护周期。
