#!/usr/bin/env python3
"""The Funniest Honest Appliance Error — make.fun entry.

A washing machine reports, in its own flat, put-upon voice, the one fault
every owner knows: a sock went in and never came out. The humour comes from
the truth of it — the machine states the facts and refuses to explain them.
"""

import os

# The line: one honest error message, 129 characters, a single line.
# The "not a magician" twist is the joke: the machine states the fault,
# denies the obvious accusation, then refuses to explain it.
LINE = (
    "ERROR E07: One sock is missing. I did not eat it. "
    "I am a washing machine, not a magician \u2014 "
    "and I refuse to discuss where it went."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
