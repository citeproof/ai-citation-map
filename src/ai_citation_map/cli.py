import argparse
import csv
import sys

from .core import build_map, read_csv


def main(argv=None) -> int:
    p = argparse.ArgumentParser(
        prog="ai-citation-map",
        description="Rank the domains cited in AI answers (ChatGPT, Perplexity, Gemini...) from a CSV "
        "with columns question, engine, cited_url.",
    )
    p.add_argument("csv", help="input CSV file")
    p.add_argument("-n", "--top", type=int, default=25, help="how many domains to show (default 25)")
    p.add_argument("--csv-out", help="also write the full map to this CSV file")
    a = p.parse_args(argv)

    try:
        rows = read_csv(a.csv)
    except FileNotFoundError:
        print(f"File not found: {a.csv}", file=sys.stderr)
        return 1
    missing = {"question", "engine", "cited_url"} - set(rows[0].keys() if rows else [])
    if missing:
        print(f"Missing column(s): {', '.join(sorted(missing))}", file=sys.stderr)
        return 1

    result = build_map(rows)
    print(f"{'domain':35} {'cites':>5} {'questions':>9}  engines")
    for s in result[: a.top]:
        print(f"{s.domain:35} {s.cites:>5} {len(s.questions):>9}  {', '.join(sorted(s.engines))}")

    if a.csv_out:
        with open(a.csv_out, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["domain", "cites", "questions", "engines"])
            for s in result:
                w.writerow([s.domain, s.cites, len(s.questions), " ".join(sorted(s.engines))])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
