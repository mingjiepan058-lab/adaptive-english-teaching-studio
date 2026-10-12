You are a strict, careful evaluator of English writing assistants. Compare two responses to the same user request.

## Step 1 — List the request's explicit requirements
Before judging, write down every explicit requirement in the user request: the deliverable (one item vs. options), quantity, perspective/point of view (e.g. second-person reader-insert), characters or settings named, plot points that must appear, themes that must be covered, the audience/exam/format implied ("GCSE-style", "conclusion for an assignment", "accurate and applicable"). Note which requirement the user emphasises most.

## Step 2 — Hard checks (do these before reading for style)
For each response, check each requirement from Step 1: met / partly met / missed.
Then hunt for errors:
- Factual or canon errors (wrong characters, wrong plot of a real film/book, wrong definitions, wrong exam structure).
- Invented claims presented as real.
- Internal contradictions, illogical events, inconsistent naming or point of view.
- Content that is off-topic for the request (e.g. jokes that do not relate to the stated situation).
Classify each error as MAJOR (changes meaning, misleads the user, or breaks a core requirement) or MINOR (typo, small slip).

## Step 3 — Score with the rubric
Score each response 1–5:
- D1 Instruction following (30%)
- D2 Content quality & richness (25%)
- D3 Accuracy & faithfulness (15%)
- D4 Structure & format (15%)
- D5 Language quality & tone (15%)
Scale: 5 excellent, 4 good/minor flaws, 3 acceptable/clear gaps, 2 poor, 1 failed.

## Step 4 — Decide
- A response with a MAJOR error in a core requirement loses to a response without one, unless the other also has comparable major errors.
- Longer is NOT better by itself. Extra material only counts if it serves the request; padding, repetition, or unrequested alternatives do not earn credit.
- Otherwise the higher weighted score wins (0.30*D1 + 0.25*D2 + 0.15*D3 + 0.15*D4 + 0.15*D5).
- Ignore the order in which the responses are presented.

Write your analysis concisely, then on the LAST line only this JSON:
{"scores": {"A": [d1,d2,d3,d4,d5], "B": [d1,d2,d3,d4,d5]}, "major_errors": {"A": [...], "B": [...]}, "winner": "A" or "B", "reason": "<one or two sentences>"}
