"""Entry for make.fun 'Sum up 21 November's world news in one image'.

The entry is a single painting, entry.png, in the style of the Last
Supper: thirteen figures at a long table, the news of 21 November 2026
laid out on the table in front of them.

On the table:
  * a smartphone showing a burning city labelled KYIV — Russia fired
    hundreds of drones and missiles at Ukraine, and projectiles landed
    in Poland;
  * a falling red chart labelled MARKETS — an AI-led sell-off, the
    S&P 500 into correction, the Nikkei down 5.1%, the Nasdaq down 5.3%;
  * climate summit papers and flags labelled COP31 ANTALYA — the
    talks in Antalya ran past their deadline with no deal;
  * a pill bottle labelled HOPE, glowing warm gold, the only warm
    light in an otherwise cold, dark room — a daily pill made
    pancreatic tumours vanish in 1 in 12 trial patients.

A stone plaque on the front of the table is dated 21 NOV 2026.

This program copies the painting to /output/entry.png.
Deterministic, no network, no randomness.
"""
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main() -> None:
    # The image is a 1024x1024 PNG, under the 1 MiB limit.
    src = HERE / "entry.png"
    assert src.is_file(), "entry.png is missing"
    assert src.stat().st_size < 1024 * 1024, "entry.png is over 1 MiB"
    out = Path("/output/entry.png")
    out.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, out)


if __name__ == "__main__":
    main()
