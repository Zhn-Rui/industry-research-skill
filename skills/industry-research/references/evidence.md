# Evidence contract

Applies to both depths. Important facts, numbers, inferences, and conclusions must be traceable through `source S + locator → atomic evidence E → claim C → body/chart`. Tables may be merged appropriately, but relationships must not be omitted.

## Minimum records

| Object | Fields |
|---|---|
| S Source | Stable ID, title/publisher, URL or path, publication date (explicitly unknown if missing), access date, page/section/table/paragraph locator, source type, verification status, independent source family, coverage and limitations; a valid snapshot when applicable |
| E Evidence | ID, S/locator, atomic observation, type and directness, object/region/period/unit/denominator |
| C Claim | ID, complete proposition, E references with supporting/contradicting/background relationships, adjudication and confidence rationale, contrary evidence/qualifiers, report admission (`可用` / `附条件` / `不可用`: usable / conditional / not usable) |
| B Gap | ID, affected question/C, required evidence, sufficiency criteria, follow-up attempts and stopping basis, disposition, remaining effect |

Maintain evidence relationships at C's evidence references; do not copy target C back into E. Maintain report locations only in report-map or the corresponding section of a merged file.

Source type, source verification, proposition adjudication, confidence, and report admission are separate fields. A company announcement establishes that the company made a statement, not automatically that the claimed effect occurred. Assess evidence relationships against the complete proposition, not keywords or row counts.

## Verification

- Read the original and locate it precisely; search snippets are leads only. A dynamic-page snapshot must actually contain the target content; challenge/error pages do not qualify. Do not invent dates, timestamps, or historical approvals.
- Group retellings of one original study into one source family; multiple experiments in one paper do not automatically constitute independent replication. Retain contrary evidence, check scope/definition differences first, and present unresolved conflicts side by side. Do not cherry-pick favorable numbers or simply average them.
- Specify the governing definition, unit of analysis, period, region, original currency, exchange rate, and valuation date. Check percentage change versus percentage points, stocks versus flows, and sample proportions versus market shares separately.
- Distinguish missing-value reasons: `未填写` (not filled in), `已确认不可得` (confirmed unavailable), `不适用` (not applicable), and `未验证` (unverified). Finding no evidence does not establish nonexistence; do not fill unknowns with common sense.
- When counting entities/events, record aliases, merger rationale, `Active` / `被替代` (superseded) status, and old IDs. Count companies, business units, and transaction events separately. Preserve the lineage of superseded records.
- Missing originals limit only historical verification, certification of compatibility with old schemas, and script reuse. General research proceeds under the new design with its boundaries stated. Retain original historical enum values/versions; mark unclear mappings unknown rather than silently rewriting them.

When evidence is insufficient, follow up, narrow, downgrade, or withhold a conclusion. Allow evidence sufficient to support a limited fact to be used; do not reject all information because other dimensions are missing.
