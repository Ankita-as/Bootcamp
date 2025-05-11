from typing import Iterator

def split_lines_on_delimiter(lines: Iterator[str]) -> Iterator[str]:
    for line in lines:
        for part in line.strip().split(","):
            yield part.strip() + "\n"
