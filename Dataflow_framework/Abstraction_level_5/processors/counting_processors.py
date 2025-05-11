from typing import Iterator, Tuple
from typing import Callable, Iterator
from Abstraction_level_5.processors.base_processors import Line


def count() -> Callable[[Iterator[Line]], Iterator[Line]]:
    def _count(lines: Iterator[Line]) -> Iterator[Line]:
        count = sum(1 for _ in lines)
        yield Line(content=f"Count: {count}")
    return _count

# In counting_processors.py
def count_lines(input_lines):
    count = sum(1 for _ in input_lines)
    print(f"Line Count: {count}")
    return input_lines  # or return the processed data if necessary

