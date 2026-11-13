# ai-citation-map

Turn a CSV of URLs cited in AI answers (ChatGPT, Perplexity, Gemini, Claude, Google AI Overviews) into a ranked list of domains: how often each is cited, on how many distinct questions, and by which engines.

No dependencies. Python 3.8+.

## Install

```bash
pip install ai-citation-map
```

## Use

Input: one row per cited URL.

```csv
question,engine,cited_url
best invoicing app for freelancers,chatgpt,https://www.g2.com/categories/invoicing
best invoicing app for freelancers,perplexity,https://www.reddit.com/r/freelance/comments/abc
best invoicing app for freelancers,gemini,https://zapier.com/blog/best-invoicing-software/
```

```bash
ai-citation-map citations.csv --top 25 --csv-out map.csv
```

```
domain                              cites questions  engines
g2.com                                  1         1  chatgpt
reddit.com                              1         1  perplexity
zapier.com                              1         1  gemini
```

From Python:

```python
from ai_citation_map import build_map
for d in build_map(rows):
    print(d.domain, d.cites, len(d.questions), sorted(d.engines))
```

## Reading the output

- Results are sorted by **distinct questions**, then citations: a domain cited once on each of eight questions matters more than one cited ten times on a single question.
- Domains cited by every engine are the safest targets; ones cited by a single engine may come and go.
- AI answers vary between runs and locations. Treat the map as a sample and re-run it with the same questions over time.

## Collecting the input

By hand (ask each question in each engine and log the cited links), or with CiteProof's free [AI citation checker](https://citeproof.co/tools/ai-citation-checker?utm_source=pypi&utm_medium=parasite&utm_campaign=ai-citation-map), which queries ChatGPT, Perplexity and Gemini and lists the domains each one cites.

More templates (robots.txt rules for AI crawlers, llms.txt, JSON-LD): [citeproof/ai-visibility-toolkit](https://github.com/citeproof/ai-visibility-toolkit).

MIT licensed. Maintained by [CiteProof](https://citeproof.co).
