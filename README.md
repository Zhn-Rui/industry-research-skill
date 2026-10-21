# Industry Research Skill · 行业研究技能

用 Codex 开展可追溯、可审查、可接续的行业研究。
Conduct traceable, reviewable, and resumable industry research with Codex.

[中文文档](README.zh-CN.md) · [English](README.md)

A structured workflow that helps Codex turn scattered research materials into evidence-traceable, bounded conclusions and saved records that another session can continue.

## Who it is for and what it supports

For industry and market analysts; strategy, consulting, and business analysts; founders and product managers; and students and independent researchers doing business research.

Applicable tasks include industry or segment research, market and competitive landscape mapping, multi-source synthesis, preliminary evidence assessment of business opportunities, and review or continuation of existing research. These are intended use cases, not separately tested scenarios. A single factual lookup or formatting an existing report rarely needs the full workflow.

## Core capabilities

- **Trace important conclusions to evidence.** Record sources, definitions, periods, units, and support for claims so readers can inspect the basis.
- **Keep conflicts, assumptions, and unknowns visible.** Stage reviews and bounded conclusions prevent polished prose from hiding unresolved evidence.
- **Continue in a new session.** Save scope, evidence, review decisions, artifact locations, and a continuation index; the next session checks the actual records before proceeding.

One English runtime includes a main Skill, four references, and six optional templates. Commercial parameters, simple scenarios, and analysis of supplied interview material are conditional modules. Human judgment remains necessary for scope, evidence sufficiency, conflicts, and decisions.

## Quick start

1. Download the repository ZIP using GitHub's **Code → Download ZIP** and extract it, or clone the repository URL shown on this GitHub page:

   ```sh
   git clone https://github.com/Zhn-Rui/industry-research-skill.git
   cd industry-research-skill
   ```

   Downloading or cloning does not automatically install or enable the Skill.
2. Open the extracted or cloned folder in Codex. Ask Codex to read and follow [skills/industry-research/SKILL.md](skills/industry-research/SKILL.md).
3. Supply your topic, scope (region, period, cutoff date), questions, available materials, allowed tools, and output directory. The examples below are ready to copy.
4. Read the report and its limitations in your chosen output directory. Check the evidence and review records, then ask Codex to investigate gaps or continue from the saved continuation index.

## Copyable examples

### Chinese task

```text
请读取并遵循 skills/industry-research/SKILL.md。研究 2024 年欧洲乘用电动车市场，梳理市场变化与竞争格局；仅使用我随后提供的材料，不开展网络检索。优先精简模式，使用中文，输出到 research-output/。先确认范围和材料是否足够，区分有依据的结论、冲突、假设和未知，保留证据引用、审查记录与新会话接续索引。材料不足时披露局限，不补造事实。
```

### English task

```text
Read and follow skills/industry-research/SKILL.md. Research the 2024 European passenger electric-vehicle market and summarize market changes and the competitive landscape. Use only the materials I provide next; do not browse. Prefer concise mode, write in English to research-output/, and first check scope and material sufficiency. Distinguish supported conclusions, conflicts, assumptions, and unknowns. Keep evidence references, review records, and a continuation index for a new session. Disclose gaps without inventing facts.
```

These prompts illustrate usage; they are not additional test results. Provide the materials before evidence collection begins. For new public-source research, explicitly allow search and original-source reading in a capable Codex environment.

## Resume in a new session

Keep the output directory and make it accessible to the new Codex session together with this repository. Copy:

```text
Read and follow skills/industry-research/SKILL.md. Resume the research saved in research-output/. Read the continuation index, scope, evidence, and original reviews/decisions. Verify that the actual artifacts exist and statuses remain justified before continuing. Preserve unresolved failures and authorization limits; explain the next supported step.
```

Concise mode normally keeps the continuation index inside `research.md`; full mode may use separate records. An old PASS alone is not sufficient to resume. See [review and recovery](skills/industry-research/references/review-recovery.md).

## Concise and full modes

| Mode | When to use | Organization |
|---|---|---|
| Concise | A narrow question, short output, few sources, no complex model | Normally one `research.md` containing scope, evidence, report, checks, and continuation; separate reader report if useful |
| Full | Multiple questions/regions/periods, complex evidence or modeling, a long report, or explicit user choice | Separate logical records and data tables when needed |

Record the choice and rationale. Templates define fields, not a six-file quota. Both modes require traceability, visible counterevidence and unknowns, limitations, and actual performance of claimed checks. Each logical record has one authoritative location.

## Tool requirements

- Read material, write text, and inspect actual outputs. Without file writing, provide saveable text and disclose that it is not persisted.
- New public-source research needs search and original-source reading. Offline, use supplied material; unreadable sources remain leads.
- Quantitative conclusions need verifiable arithmetic; unrecomputed results remain unverified.
- Charts or paginated documents need creation, rendering, and viewing. Text extraction does not substitute for visual QA.
- Independent review/handoff needs an independent context. Otherwise disclose self-review only. No particular vendor tool, paid service, or global dependency is required.

The workflow currently targets Codex. Compatibility with other agent platforms has not been tested. It maintains one English runtime; deliverables follow the explicit language choice or, otherwise, the task language. Paths, IDs, and canonical status values stay stable, including established tokens such as `可用`, `已批准`, and `按例外关闭`.

## Validation and known limits

Chinese historical versions had synthetic, full-depth, paired, and narrow real-source/handoff tests. Three historical paired cases showed no core quality-score improvement; artifacts were larger and reported elapsed times longer, with mixed tool-call changes. No claim of improved accuracy or reduced cost is supported.

The English runtime had semantic translation review and three offline synthetic recovery checks covering task/output language and preserved exception boundaries. Historical Chinese passes are not English-runtime passes. No English paired comparison or new real-source trial has been performed. See [docs/VALIDATION.md](docs/VALIDATION.md) for detailed methods, results, and qualifications.

Long-running or large-scale research, complex models, paginated visual delivery, and stable recovery without feedback remain insufficiently validated. The public summary does not independently reproduce all historical tests. This release preparation did not rerun the full research tests.

Human judgment remains necessary. The Skill does not provide paid databases, interview recruitment, or outreach by default, and does not promise automated investment decisions, professional due diligence, or fact certification. Tool and evidence limits constrain delivery.

## Origin, license, and feedback

The workflow originated in research on the embodied-intelligence data market and was later distilled for research in other industries. Private interviews, original reports, third-party source copies, and development history are excluded. See the [public file manifest](PUBLIC_FILES.md) and [release notes](RELEASE_NOTES.md).

Created by **Enrui Zhang**. This project is licensed under the [MIT License](LICENSE). The license covers this repository's project content; it does not grant rights to excluded original research, private interviews, or third-party material.

Use this repository's GitHub Issues to report problems or suggest improvements. Include the expected behavior, actual behavior, and a minimal sanitized example; do not upload private research, credentials, or unauthorized source material. No response-time or maintenance commitment is made.
