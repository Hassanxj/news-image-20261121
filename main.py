"""Entry for make.fun 'Sum up 21 November's world news in one image'.

Copies the included Last Supper painting to /output/entry.png.
Deterministic, no network, no randomness.
"""
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main() -> None:
    # The image is a 1024x1024 PNG, under the 1 MiB limit.
    src = HERE / "entry.png"
    assert src.is_file() and src.stat().st_size < 1024 * 1024
    out = Path("/output/entry.png")
    out.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(HERE / "entry.png", out)


if __name__ == "__main__":
    main()
