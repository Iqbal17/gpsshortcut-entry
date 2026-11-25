"""The GPS Swears It Was a Shortcut — entry program.

Writes one line of plain text (the GPS's own excuse for sending the driver
down the wrong road) to $MAKEFUN_OUTPUT_DIR/entry.txt, falling back to
/output/entry.txt. The gate requires UTF-8 text of 1-200 characters, not
only whitespace.

Decision record
---------------
Candidates weighed against the judge's brief (smug, defensive GPS voice;
a real joke with an unseen turn; a fresh specific detail instead of the
usual "recalculating" gag; reads cleanly aloud in one breath):

A. "I didn't send you down the wrong road - the map did, and frankly the
   map has been lying to both of us for years."
   Rejected: it blames the map, which the judge likes, but the detail is
   abstract ("lying for years") — no concrete place, no turn the reader
   does not see coming. It reads like a complaint, not an excuse.

B. "That wasn't a wrong turn, that was a shortcut the road simply hadn't
   finished building yet."
   Strong reserve: smug, defends the route, and "hadn't finished building
   yet" is a decent twist. Lost because the construction is familiar —
   "the road wasn't finished" is a joke most readers have heard in some
   form — and it has no specific detail (no cul-de-sac, lake, or wedding).

C. "The lake was not on my map, and if I'm honest, neither was the
   wedding we just crashed."
   Strong reserve: two fresh specific details (lake, wedding) and a funny
   image. Lost because "if I'm honest" softens the smugness — the GPS
   starts apologising instead of defending itself — and two details crowd
   one breath; the wedding crash is also more about the driver than the
   GPS's own excuse.

D. "Recalculating is just my way of saying I have no idea where we are,
   and neither do you."
   Rejected outright: the judge's brief explicitly warns against the usual
   recalculating joke, and this one also admits ignorance instead of
   defending the route.

E. "I said turn left. You turned left. The cul-de-sac is on you, not me."
   Strong reserve: punchy, smug, specific detail. Lost because it blames
   the driver rather than excusing the wrong road — criterion 1 wants the
   GPS's own excuse for sending the driver down the wrong road, and
   pointing at the driver dodges the question instead of answering it.

F. CHOSEN: "The shortcut was real. The road simply gave up halfway and
   became a lake."
   Wins: first person, smug and defensive ("the shortcut was real" insists
   the GPS was right); blames the road, not the driver and not itself; a
   fresh specific detail (the lake); and the turn is genuinely unseen —
   a road does not "become" a lake, so the excuse collapses into absurdity
   in the last three words. Reads cleanly aloud in one breath (73 chars).

Pass 2 — genuine revisions to the winning line:
1. First draft: "The shortcut was real, but the road gave up halfway and
   turned into a lake." Changed the comma + "but" into a full stop, giving
   a deadpan two-beat delivery ("The shortcut was real. The road simply
   gave up..."), and swapped "turned into" for "became" — shorter, and
   "became a lake" lands harder than "turned into a lake". Added
   "simply" for the GPS's breezy, unbothered tone.
2. Considered appending "Recalculating." as a closer. Rejected: the
   brief explicitly warns against the usual recalculating joke, and the
   line already ends on its strongest word (lake). Also considered
   "I never said it was a good shortcut" as the closer — rejected, it
   undercuts the smugness by conceding the shortcut was bad.
"""

import os

MAX_CHARS = 200

LINE = "The shortcut was real. The road simply gave up halfway and became a lake."


def entry_path():
    """Resolve the output path: $MAKEFUN_OUTPUT_DIR, else /output."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(out_dir, "entry.txt")


def check_gate(text):
    """Mirror the sealed gate: 1-200 chars, not only whitespace."""
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError("line must be 1-200 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("line must not be only whitespace")


def main():
    check_gate(LINE)
    path = entry_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
