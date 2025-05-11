from typing import Iterator, Tuple, Callable

Line = Tuple[str, str]

def tag_error_warning() -> Callable[[Iterator[Line]], Iterator[Line]]:
    def processor(lines: Iterator[Line]) -> Iterator[Line]:
        for tag, line in lines:
            if "error" in line:
                tag = "ERROR"
            elif "warning" in line:
                tag = "WARNING"
            yield (tag, line)  # Yield the modified tuple
    return processor

