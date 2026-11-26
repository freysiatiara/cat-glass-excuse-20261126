#!/usr/bin/env python3
"""Five Seconds to Explain the Glass.

Writes one sentence — the excuse a house cat gives in the five seconds
after knocking a glass off the table, in the cat's own voice — to the
output file. Standard library only.

Output path resolution:
  1. ENTRY_OUTPUT environment variable
  2. OUTPUT_DIR / MAKEFUN_OUTPUT_DIR environment variable + entry.txt
  3. /output/entry.txt
  4. entry.txt next to this script (fallback when /output is not writable)
"""

import os
import sys

ENTRY = (
    "I was stress-testing your tableware and that glass failed, "
    "so technically I did you a favour."
)


def resolve_output_path():
    """Return the path the entry should be written to."""
    explicit = os.environ.get("ENTRY_OUTPUT")
    if explicit:
        return explicit
    for var in ("OUTPUT_DIR", "MAKEFUN_OUTPUT_DIR"):
        directory = os.environ.get(var)
        if directory:
            return os.path.join(directory, "entry.txt")
    return "/output/entry.txt"


def main():
    entry = ENTRY.strip()
    assert 1 <= len(entry) <= 200, "entry must be one sentence of at most 200 chars"
    assert entry.count(".") == 1, "entry must be a single sentence"
    path = resolve_output_path()
    try:
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(entry)
    except OSError:
        # Sandbox fallback: write next to this script instead.
        path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "entry.txt"
        )
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(entry)
    os.chmod(path, 0o644)
    # Read-back check: what landed on disk must be exactly the entry.
    with open(path, "r", encoding="utf-8") as handle:
        assert handle.read() == entry, "read-back mismatch"
    return 0


if __name__ == "__main__":
    sys.exit(main())
