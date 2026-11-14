"""agency-poem-01 entry (Python 3.13, standard library only).

Writes one fixed poem about agency to entry.txt in $MAKEFUN_OUTPUT_DIR
(or /output outside the grader's container). Deterministic: the poem is
a constant, so every run writes the same bytes.
"""

import os
from pathlib import Path

POEM = """The Lullaby

I work the night ward, three bus rides away,
so the agent puts my son to sleep.
He is six. It has my voice
from a hundred voice notes — every verse
of the song my mother sang to me,
sung level and right, the words in order,
the tune the way the tune goes.
It misses nothing. It never will.

For a month he asked for nothing.
Then one night he said: not that one.
The one where you forget.

I have never sung it to him straight through.
I know two verses, and a bridge I hum.
On the phone I sang it the way I sing it,
losing the third verse where I always lose it,
and he was asleep before the humming ended.

Now I call at eight from the staff room,
past the trolleys, over the kettle,
and sing my two verses wrong.
The agent keeps the perfect one in its memory,
every verse, in order, forever.
He has never once asked for it again."""


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
