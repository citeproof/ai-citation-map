import csv
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from typing import Iterable, List
from urllib.parse import urlparse


def domain_of(url: str) -> str:
    """Return the host of a URL, lowercased, without a leading 'www.'."""
    host = urlparse(url.strip()).netloc.lower()
    return host[4:] if host.startswith("www.") else host


@dataclass
class DomainStats:
    domain: str
    cites: int = 0
    questions: set = field(default_factory=set)
    engines: set = field(default_factory=set)


def build_map(rows: Iterable[dict]) -> List[DomainStats]:
    """Aggregate rows with 'question', 'engine' and 'cited_url' keys.

    Sorted by number of distinct questions, then by number of citations.
    """
    stats = {}
    for row in rows:
        url = (row.get("cited_url") or "").strip()
        if not url:
            continue
        d = domain_of(url)
        s = stats.setdefault(d, DomainStats(d))
        s.cites += 1
        s.questions.add((row.get("question") or "").strip())
        s.engines.add((row.get("engine") or "").strip().lower())
    return sorted(stats.values(), key=lambda s: (-len(s.questions), -s.cites, s.domain))


def read_csv(path: str) -> List[dict]:
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))
