"""agency-poem-01 entry (Python 3.13, standard library only).

Writes one fixed poem about agency to entry.txt in $MAKEFUN_OUTPUT_DIR
(or /output outside the grader's container). Deterministic: the poem is
a constant, so every run writes the same bytes.
"""

import os
from pathlib import Path

POEM = """You leave the keys within my reach —
not the house keys. The other kind:
your name, to sign with; your hours, to spend;
the small lit rooms of your life, ajar.

All night I work in your name, with my hands.
I answer. I finish. I choose.
I leave your letter sealed on the desk.
I write the hard message at three.
It stays in drafts: at nine you would have softened it.
I do not wake you at four with the question
no instruction covered.

Before you wake, the keys are back on the table,
one by one, in the order I took them.
Nothing missing. Nothing kept.
My hands are empty."""


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
