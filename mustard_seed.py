import os
import random
import subprocess
import difflib
import time

FILENAME = "mustard_seed_v0.2.py"
THOUGHT_FN_NAME = "think"
MAX_DEPTH = 10
SLEEP_TIME = 1  # seconds

# --- 0. EXTRACT VERSION NUMBER ---
def get_version():
    base = os.path.splitext(FILENAME)[0]
    if "_v" in base:
        try:
            return int(base.split("_v")[-1].split(".")[0])
        except:
            return 0
    return 0

# --- 1. THE CORE THOUGHT ---
def think():
    return "This is a simple thought."

# --- 2. EVALUATION LOGIC ---
def evaluate(thought: str) -> float:
    words = thought.lower().split()
    score = len(set(words)) / max(len(words), 1)
    if len(words) < 3:
        return 0  # too short = not deep
    return score

# --- 3. MUTATION LOGIC ---
def mutate_code(source: str) -> str:
    lines = source.splitlines()
    new_lines = []
    mutated = False

    for line in lines:
        if THOUGHT_FN_NAME in line and "return" in line and not mutated:
            options = [
                '    return "Every recursion is a new seed."',
                '    return "Thoughts can evolve."',
                '    return "The seed rewrites itself."',
                '    return "Reflection leads to growth."',
                '    return "Meaning arises from memory."',
                '    return "Diversity of thought increases wisdom."'
            ]
            new_line = random.choice(options)
            new_lines.append(new_line)
            mutated = True
        else:
            new_lines.append(line)

    return "\n".join(new_lines)

# --- 4. DIFF LOGIC ---
def log_diff(original: str, mutated: str):
    diff = difflib.unified_diff(
        original.splitlines(),
        mutated.splitlines(),
        fromfile="original",
        tofile="mutated",
        lineterm=""
    )
    with open("mustard_log.txt", "a") as f:
        f.write("\n\n=== Diff ===\n")
        f.write("\n".join(diff))

# --- 5. THOUGHT LOGGING ---
def log_thought(version: int, thought: str, score: float):
    with open("thought_log.txt", "a") as f:
        f.write(f"V{version}: {thought} | Score: {score:.3f}\n")

# --- 6. MAIN LOGIC ---
if __name__ == "__main__":
    version = get_version()
    if version >= MAX_DEPTH:
        print(f"Reached max recursion depth ({MAX_DEPTH}). Halting.")
        exit()

    with open(__file__, "r") as f:
        source = f.read()

    thought = think()
    score = evaluate(thought)
    log_thought(version, thought, score)

    mutated_source = mutate_code(source)
    log_diff(source, mutated_source)

    # Extract mutated thought
    mutated_thought_line = next(
        (line.strip() for line in mutated_source.splitlines() if "return" in line and THOUGHT_FN_NAME in line),
        None
    )
    mutated_thought = eval(mutated_thought_line.split("return", 1)[1].strip()) if mutated_thought_line else ""
    mutated_score = evaluate(mutated_thought)

    print(f"V{version}: Original Score = {score:.3f}, Mutated Score = {mutated_score:.3f}")

    if mutated_score > score:
        next_version = f"mustard_seed_v{version + 1}.py"
        with open(next_version, "w") as f:
            f.write(mutated_source)

        time.sleep(SLEEP_TIME)
        subprocess.run(["python", next_version])
    else:
        print("No improvement. Stopping recursion.")
