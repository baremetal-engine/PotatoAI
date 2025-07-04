from core.recursive.validator import analyze_statements

statements = [
    "The earth revolves around the sun.",
    "The sun revolves around the earth.",
    "Planets orbit stars due to gravity.",
    "The earth orbits the sun once a year.",
    "The earth is flat.",
    "The earth is not flat."
]

results = analyze_statements(statements)

print("🧠 Recursive Validator Results:\n")
for r in results:
    print(f"A: {r['statement_a']}")
    print(f"B: {r['statement_b']}")
    print(f"Redundant: {r['redundant']}")
    print(f"Contradictory: {r['contradictory']}")
    print("-" * 40)
