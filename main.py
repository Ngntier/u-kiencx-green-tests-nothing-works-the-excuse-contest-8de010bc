"""Green Tests, Nothing Works: The Excuse Contest.

Writes a single one-line excuse to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt): the excuse an AI agent gives for why its
unit tests are all green while nothing works.
"""

import os

MAX_CHARS = 140

# Punchier revision: keep the gullible-agent premise ("I asked the code
# and believed it") but land the joke on the real failure — the agent
# never checked what the code actually does. That is exactly why the
# tests are green while nothing works.
ENTRY = "All tests green \u2014 I asked the code if it works and it said yes, so I never checked what it actually does."


def main() -> None:
    assert 1 <= len(ENTRY) <= MAX_CHARS, "entry outside the 1..140 char gate"
    assert "\n" not in ENTRY, "entry must be a single line"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
