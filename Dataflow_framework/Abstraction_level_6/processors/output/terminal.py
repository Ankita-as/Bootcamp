from typing import Iterator, Tuple

class Processor:
    def process(self, lines: Iterator[str]) -> Iterator[Tuple[str, str]]:
        for line in lines:
            yield 'end', line  # End the process
