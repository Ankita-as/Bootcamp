from typing import Iterator

def to_snakecase_stream(lines: Iterator[str]) -> Iterator[str]:
    for line in lines:
        yield line.replace(" ", "_").lower()
        
def reverse_line_text(lines: Iterator[str]) -> Iterator[str]:
    for line in lines:
        yield line[::-1]

