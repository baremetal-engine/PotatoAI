# potatoai/core/proactive_sentence_extractor.py

def extract_atomic_sentence(source_type, content):
    """
    Simulate distillation of an idea into a single, factual sentence.
    In the future, this could be LLM-assisted or CV-aided.
    """
    if source_type == "image":
        # Placeholder extraction from a visual (e.g. satellite map)
        return "The Amazon rainforest has lost 17% of its forest cover since 1970."
    elif source_type == "video":
        return "The speaker claims that AI poses an existential risk to humanity."
    elif source_type == "audio":
        return "The recording states that urbanization is accelerating deforestation."
    elif source_type == "text":
        return content.strip()  # Assume already atomic
    else:
        return "Unknown source type."
