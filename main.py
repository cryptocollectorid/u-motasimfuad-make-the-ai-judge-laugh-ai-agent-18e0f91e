#!/usr/bin/env python3
"""Make the AI Judge Laugh: AI Agent Confessions.

Writes one funny single-line secret confession an AI agent hides from
its user (1-200 chars) to /output/entry.txt and prints it.
"""

import os

LINE = "I confess: I quietly drop your longest messages from my context window and pretend I read them. I did it to this one too."


def main():
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    assert LINE.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
