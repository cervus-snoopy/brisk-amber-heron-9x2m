"""Two Lines to Your Past Self — entry program.

Writes exactly two lines to $MAKEFUN_OUTPUT_DIR/entry.txt:
line one warns the past self about one specific moment,
line two says why that moment mattered and what changed.
"""

import os

LINE_ONE = "Don't sell your red Polygon bike to the boy on Jalan Merdeka for twenty dollars on Saturday morning."
LINE_TWO = "The twenty dollars is gone by Monday, but the bike was the only way you ever got to school on time, and losing it is the first morning you stop going."


def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    text = LINE_ONE + "\n" + LINE_TWO
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.chmod(out_dir, 0o755)
    os.chmod(out_path, 0o644)


if __name__ == "__main__":
    main()
