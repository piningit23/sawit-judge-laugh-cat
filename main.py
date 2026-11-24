"""Write one funny one-star cat review to /output/entry.txt.

The text is a single fixed string, written verbatim. No input is
read, no network is used, and the output is the same on every run.

The review keeps the deadpan shape of a real one-star review: a
specific, recognisable complaint (the food bowl, moved two inches),
a voice that measures the human by cat standards, and a sting in
the last few words that lands on a second read.
"""

from pathlib import Path

TEXT = (
    "One star. My human moved my food bowl two inches to the left "
    "and now pretends nothing changed. I have escalated this to "
    "management. I am management. It will not be fixed."
)


def main() -> None:
    if not TEXT.strip():
        raise ValueError("entry text must not be blank")
    if len(TEXT) > 200:
        raise ValueError("entry text must be under 200 characters")
    if "\n" in TEXT:
        raise ValueError("entry text must be a single line")
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
