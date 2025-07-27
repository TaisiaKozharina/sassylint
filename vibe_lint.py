import subprocess
import sys
import json

VIBE_MAP = {
    "unused-variable": "🪦 Ghosted variable — you abandoned a variable like your side project.",
    "line-too-long": "📜 This line is trying to write a novel. Keep it tight.",
    "missing-docstring": "🗿 No docstring? Feels mysterious. Too mysterious.",
    "too-many-branches": "🌲 Your function is branching like a conspiracy theory.",
    "too-many-locals": "🧠 Too many variables in one place. Cognitive overload incoming.",
}

def run_pylint(filepath):
    result = subprocess.run(
        ["pylint", filepath, "--output-format=json"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    return json.loads(result.stdout)
    # print("STDOUT:", result.stdout)
    # print("STDERR:", result.stderr)
    # if result.returncode not in (0, 32):
    #     #print("Error running pylint:", result.stderr)
    #     print(result)
    #     return []
    # try:
    #     return json.loads(result.stdout)
    # except json.JSONDecodeError as e:
    #     print("JSON decode error:", e)
    #     return []

def add_vibe_check(messages):
    for msg in messages:
        line = msg['line']
        symbol = msg['symbol']
        message = msg['message']
        vibe = VIBE_MAP.get(symbol, "")
        print(f"[Line {line}] {message}")
        if vibe:
            print(f"👉 Vibe Check: {vibe}\n")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python vibe_linter.py <file_to_check.py>")
        sys.exit(1)

    filepath = sys.argv[1]
    results = run_pylint(filepath)
    add_vibe_check(results)