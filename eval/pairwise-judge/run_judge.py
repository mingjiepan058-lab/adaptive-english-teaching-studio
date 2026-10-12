#!/usr/bin/env python3
"""Run an LLM judge (Claude Code or Codex CLI) over the pairwise dataset.

Each item is judged twice: original order (answer_1 = A) and swapped
order (answer_2 = A), to measure and cancel position bias.

Usage:
  python3 run_judge.py --prompt prompts/v3_rubric_hardchecks.md --backend claude
  python3 run_judge.py --prompt prompts/v4_final.md --backend codex
"""
import argparse, json, pathlib, re, subprocess, tempfile
from concurrent.futures import ThreadPoolExecutor

ROOT = pathlib.Path(__file__).resolve().parent


def build_user_message(item, swapped):
    a, b = (item["answer_2"], item["answer_1"]) if swapped else (item["answer_1"], item["answer_2"])
    return (
        f"## User request\n{item['question']}\n\n"
        f"## Response A\n{a}\n\n"
        f"## Response B\n{b}\n"
    )


def call_claude(system_prompt, user_msg, model):
    cmd = ["claude", "-p", "--output-format", "json", "--tools", "",
           "--no-session-persistence", "--system-prompt", system_prompt]
    if model:
        cmd += ["--model", model]
    with tempfile.TemporaryDirectory() as cwd:  # empty cwd: no project context leaks in
        out = subprocess.run(cmd, input=user_msg, capture_output=True, text=True, cwd=cwd, timeout=900)
    data = json.loads(out.stdout)
    used = next(iter(data.get("modelUsage", {})), model or "default")
    return data["result"], used


def call_codex(system_prompt, user_msg, model):
    with tempfile.TemporaryDirectory() as cwd:
        last = pathlib.Path(cwd) / "last.txt"
        cmd = ["codex", "exec", "--skip-git-repo-check", "--sandbox", "read-only",
               "--output-last-message", str(last), "-"]
        if model:
            cmd[2:2] = ["--model", model]
        subprocess.run(cmd, input=system_prompt + "\n\n" + user_msg,
                       capture_output=True, text=True, cwd=cwd, timeout=900, check=True)
        return last.read_text(), model or "codex-default"


def parse_verdict(text):
    for m in reversed(list(re.finditer(r"\{.*\}", text))):
        try:
            v = json.loads(m.group(0))
            if v.get("winner") in ("A", "B"):
                return v
        except json.JSONDecodeError:
            continue
    m = re.search(r'"winner"\s*:\s*"([AB])"', text)
    return {"winner": m.group(1)} if m else None


def judge(args, system_prompt, item, swapped):
    call = call_claude if args.backend == "claude" else call_codex
    text, model = call(system_prompt, build_user_message(item, swapped), args.model)
    verdict = parse_verdict(text) or {}
    w = verdict.get("winner")
    # map A/B back to answer_1 / answer_2
    winner = None if w is None else ({"A": "2", "B": "1"}[w] if swapped else {"A": "1", "B": "2"}[w])
    return {"index": item["index"], "order": "swapped" if swapped else "original", "model": model,
            "winner": winner, "reason": verdict.get("reason"), "raw": text}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--prompt", required=True)
    p.add_argument("--backend", choices=["claude", "codex"], default="claude")
    p.add_argument("--model", default=None)
    p.add_argument("--data", default=str(ROOT / "data/enwriting-exam-10.jsonl"))
    p.add_argument("--workers", type=int, default=4)
    args = p.parse_args()

    system_prompt = pathlib.Path(args.prompt).read_text()
    items = [json.loads(l) for l in open(args.data)]
    jobs = [(it, s) for it in items for s in (False, True)]
    with ThreadPoolExecutor(args.workers) as ex:
        results = list(ex.map(lambda j: judge(args, system_prompt, *j), jobs))

    out = ROOT / "results" / f"{pathlib.Path(args.prompt).stem}__{args.backend}.jsonl"
    with open(out, "w") as f:
        for r in sorted(results, key=lambda r: (r["index"], r["order"])):
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
