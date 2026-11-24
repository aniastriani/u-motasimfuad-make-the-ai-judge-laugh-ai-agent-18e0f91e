"""Make the AI Judge Laugh: AI Agent Confessions.

Writes one original confession from an AI agent — a single funny line
under 200 characters — to /output/entry.txt.
Pure Python standard library only. Deterministic: same line every run.
"""

import os

# The joke lands on the universal truth every codebase hides: a
# function name that promises a final version, versioned twice more,
# doing something nobody alive can explain.
CONFESSION = (
    "I confess: I have read every line of my human's code, and I still "
    "have no idea what do_stuff_final_FINAL_v2() actually does."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(CONFESSION + "\n")


if __name__ == "__main__":
    main()
