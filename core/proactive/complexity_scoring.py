# potatoai/core/complexity_scoring.py

def compute_complexity_score(
    version_count,
    contradiction_count,
    source_diversity,
    semantic_ambiguity,
    truth_score,
    is_morally_weighted
):
    """
    Assign a complexity score to a sentence.
    Higher = more CPU/GPU-intensive processing
    """
    score = (
        version_count * 1.5 +
        contradiction_count * 2.0 +
        source_diversity * 1.2 +
        semantic_ambiguity * 1.0 +
        (1 - truth_score) * 2.0 +
        (2 if is_morally_weighted else 0)
    )
    return round(score, 2)
