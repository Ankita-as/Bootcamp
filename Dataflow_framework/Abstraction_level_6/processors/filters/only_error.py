from typing import Iterator, Tuple

class Processor:
    def process(self, lines: Iterator[str]) -> Iterator[Tuple[str, str]]:
        # Your logic here
        for line in lines:
            yield 'error', line
