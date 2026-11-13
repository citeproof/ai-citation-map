from ai_citation_map import build_map, domain_of


def test_domain_of():
    assert domain_of("https://www.G2.com/x") == "g2.com"
    assert domain_of("http://reddit.com/r/a") == "reddit.com"


def test_build_map_orders_by_questions():
    rows = [
        {"question": "q1", "engine": "chatgpt", "cited_url": "https://a.com/1"},
        {"question": "q1", "engine": "chatgpt", "cited_url": "https://a.com/2"},
        {"question": "q1", "engine": "chatgpt", "cited_url": "https://a.com/3"},
        {"question": "q1", "engine": "perplexity", "cited_url": "https://b.com"},
        {"question": "q2", "engine": "gemini", "cited_url": "https://www.b.com"},
    ]
    m = build_map(rows)
    assert m[0].domain == "b.com" and len(m[0].questions) == 2
    assert m[1].domain == "a.com" and m[1].cites == 3
