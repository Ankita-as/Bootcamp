from typing import Iterator, Tuple

class Processor:
    def process(self, lines: Iterator[str]) -> Iterator[Tuple[str, str]]:
        # Example implementation
        for line in lines:
            yield 'error', line
