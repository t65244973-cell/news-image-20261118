"""Entry for make.fun news-image-20261118.

Copies the image this repository holds (entry.png, 1024x1024, a
newspaper front page summing up world news on Wednesday 18 November
2026) to /output/entry.png. No network, no randomness, no other
input: both runs write exactly the same bytes.
"""

import os
import shutil
from pathlib import Path


def main() -> None:
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    if not source.is_file():
        raise FileNotFoundError(f"missing image next to main.py: {source}")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    destination = output_dir / "entry.png"
    # A plain byte copy: deterministic, so a second run writes
    # byte-for-byte the same file as the first.
    shutil.copyfile(source, destination)


if __name__ == "__main__":
    main()
