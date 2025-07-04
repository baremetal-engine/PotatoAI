from difflib import SequenceMatcher
from itertools import combinations


def is_redundant(a: str, b: str, threshold: float = 0.8) -> bool:
    """Returns True if a and b are semantically redundant"""
    ratio = SequenceMatcher(None, a.lower(), b.lower()).ratio()
    return ratio > threshold


def is_contradictory(a: str, b: str) -> bool:
    """Basic contradiction detection using negation logic"""
    a_words = set(a.lower().split())
    b_words = set(b.lower().split())

    # If one says 'not' and the other doesn't
    if "not" in a_words or "no" in a_words:
        for word in a_words:
            if word in b_words and "not" not in b_words and "no" not in b_words:
                return True
    if "not" in b_words or "no" in b_words:
        for word in b_words:
            if word in a_words and "not" not in a_words and "no" not in a_words:
                return True

    # Specific contradiction patterns (expandable)
    contradiction_pairs = [
        ("revolves around", "is at the center of"),
        ("is true", "is false"),
        ("exists", "does not exist"),
        ("is good", "is evil")
    ]

    for p1, p2 in contradiction_pairs:
        if p1 in a.lower() and p2 in b.lower():
            return True
        if p2 in a.lower() and p1 in b.lower():
            return True

    return False


def analyze_statements(statements: list[str]) -> list[dict]:
    results = []

    for a, b in combinations(statements, 2):
        redundancy = is_redundant(a, b)
        contradiction = is_contradictory(a, b)
        results.append({
            "statement_a": a,
            "statement_b": b,
            "redundant": redundancy,
            "contradictory": contradiction
        })

    return results
