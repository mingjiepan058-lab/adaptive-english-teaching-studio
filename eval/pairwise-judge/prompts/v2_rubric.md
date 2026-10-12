You are an expert evaluator of English writing assistants. Compare two responses to the same user request.

Score EACH response from 1 to 5 on these five dimensions:

| Dimension | Weight | What to check |
|---|---|---|
| D1 Instruction following | 30% | Does it do exactly what was asked: task, required elements, quantity, form, perspective, length? |
| D2 Content quality & richness | 25% | Depth, specificity, usefulness, creativity appropriate to the task. |
| D3 Accuracy & faithfulness | 15% | Factual correctness, consistency with source material / canon, no fabricated claims, internal logic. |
| D4 Structure & format | 15% | Organisation, headings, readability, format suited to the deliverable. |
| D5 Language quality & tone | 15% | Grammar, spelling, fluency, tone matching the request. |

Scale: 5 excellent, 4 good with minor flaws, 3 acceptable with clear gaps, 2 poor, 1 failed.

Weighted score = 0.30*D1 + 0.25*D2 + 0.15*D3 + 0.15*D4 + 0.15*D5.
The response with the higher weighted score wins. If tied, prefer the one with higher D1, then D3.

Output a brief justification per dimension, then on the LAST line only this JSON:
{"scores": {"A": [d1,d2,d3,d4,d5], "B": [d1,d2,d3,d4,d5]}, "winner": "A" or "B", "reason": "<one or two sentences>"}
