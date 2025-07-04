# potatoai/tests/test_complexity_routing.py

from core.proactive.sentence_extractor import extract_atomic_sentence
from core.proactive.complexity_scoring import compute_complexity_score

print("🧠 PotatoAI Sentence Extraction + Complexity Routing Demo")

sentence = extract_atomic_sentence("image", "some_satellite_map.png")
print(f"\n🧪 Atomic Sentence: {sentence}")

# Simulate metadata for complexity
complexity_score = compute_complexity_score(
    version_count=3,
    contradiction_count=2,
    source_diversity=4,
    semantic_ambiguity=1,
    truth_score=0.6,
    is_morally_weighted=True
)

print(f"⚖️  Computed Complexity Score: {complexity_score}")
print(f"🚀 Route to: {'High-end GPU node' if complexity_score > 7 else 'Lightweight node'}")

