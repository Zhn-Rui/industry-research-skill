# Review, failure routing, and recovery

## Review records and status

For each stage check, record the object/version, reviewer, actual actions, basis, findings, disposition, and next step using the review template. An unperformed check is NOT REVIEWED; do not copy a historical PASS. Default self-review must not be presented as independent review.

The following are canonical stored status values. Chinese values are intentionally retained from the baseline; their English glosses explain them and are not replacement enum values.

| Dimension | Values and meaning |
|---|---|
| Quality | `NOT REVIEWED` / `PASS` / `WARN` / `FAIL`; only a genuinely inapplicable check may use `不适用` (not applicable), with a reason. It must not substitute for an unperformed check |
| Authorization | `不需另批` (no further approval required) / `待批准` (awaiting approval) / `已批准` (approved) / `未确认` (unconfirmed); approved status requires a locator for the user instruction or decision record |
| Baseline | `草稿` (draft) / `冻结` (frozen) / `被替代` (superseded), pointing to a version |
| Work disposition | `进行中` (in progress) / `阻断` (blocked) / `完成` (completed) / `按例外关闭` (closed by exception) / `不适用` (not applicable) |
| Readiness | `READY` / `NOT READY`, specifying the intended next step and its dependencies |

A passed design does not establish completed execution; passed arithmetic does not establish market validity; a frozen baseline does not establish that no gaps remain. An exception changes work scope only. Preserve the original FAIL, the exception decision-maker/basis, residual effects, and the boundary within which work may continue. Do not invent owner approval; do not request it again when existing user authorization is sufficient.

## Record ownership and concise organization

Each item has one maintenance location; elsewhere, reference its ID/section. Merging files does not change ownership:

| Record | Authoritative location |
|---|---|
| Scope, questions, resource limits, depth rationale | brief or the scope section of a merged file |
| Sources, atomic observations, claims/evidence relationships, parameters, and gap disposition | evidence or the evidence section; maintain one row/record per item |
| Question disposition and mapping C to body/charts and summary | report-map or its section; a short report may use one line per question, without duplicating the source table or full claims |
| Actual checks, quality results, approvals/exceptions, changes, and rechecks | review or the checks section; one actual action may cover multiple stages, referenced once rather than narrated six times |
| Current baseline/version, work disposition, next-step readiness and dependencies | state or the continuation index; reference review records for quality and authorization instead of maintaining duplicate labels |
| Reader-facing findings, citations, and necessary limitations | report or the body section, derived from the records above rather than a second fact ledger |

Concise mode needs identifiable logical locations, not a copy of every template or every table. Omit unused parameter, entity, exception, and similar sections. Do not omit key evidence relationships, contrary evidence, question disposition, actual checks, or continuation dependencies. Full mode may split files by template but still must not maintain the same record twice. Repeating findings in a reader summary/body serves presentation; it does not require manually synchronizing multiple ledgers.

## Failure routing

- Structure/calculation: fix fields, references, dependencies, or formulas; recheck affected outputs.
- Semantics: return to the original locator to correct the object/unit/definition/denominator, mark affected C, charts, and summary, then review them again.
- Insufficient evidence: make targeted follow-ups within the brief's resource cap, or explicitly retain unknowns, narrow, or suspend the relevant model. Do not disguise insufficiency by polishing prose.
- Resource limits: retain unfinished items and effects. A project may have a limited delivery, but an incomplete study must not be labeled fully verified.
- Presentation: after changes, actually inspect affected artifacts and possible side effects again.

## Recovery and frozen-baseline revisions

At stage completion or a change in scope/key evidence, update state with the scope version, file or merged-section locations, baseline/disposition/readiness and pointers to quality/authorization records, latest valid review, B/exceptions, next action, and dependencies.

A new instance continues in this order:
1. Read state, brief, and the referenced review/approval records.
2. Verify artifact existence and version consistency. Read existing sources, contrary evidence, gaps/failed collection attempts, and preliminary adjudications; check key S/E/C relationships, quantitative dependencies, and approval boundaries. State is an index, not evidence.
3. Missing files, dangling references, or changes to formulas/scope invalidate affected reviews/readiness. Return to the earliest affected step, retaining unaffected valid work and IDs.
4. Do not restart a broad scan or create a second evidence table merely because of a handoff. Necessary revisits/follow-ups must state the new question, invalidation reason, or verification purpose and reuse existing source IDs. Record the recovery check and continuation route. Do not turn unconfirmed historical names, approval times, or completion into facts.

After freezing, retain the old version or an explicit diff, and record the reason, impact, and recheck. Add hashes/manifests only when needed for frozen-patch evidence or a calculation package; avoid self-referential manifests. A calculation package requires input closure, available dependencies, and recomputation checks; missing dependencies cannot be reported as successful reproduction.
