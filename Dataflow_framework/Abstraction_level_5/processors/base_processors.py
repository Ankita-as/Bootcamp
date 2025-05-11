from typing import Iterator, Tuple, Callable

# Define the Line type for clarity
Line = Tuple[str, str]

def start():
    def process(input_lines):
        # Add the logic that needs to be performed at the start
        return input_lines  # or modify as required
    return process

def process_data():
    def _process(lines):
        for line in lines:
            # Example processing logic
            yield line
    return _process

class finish:
    def process(self, input_lines):
        print("Processing completed!")
        return input_lines  # or return an appropriate result
def trim() -> Callable[[Iterator[Line]], Iterator[Line]]:
    """
    Trims the whitespace from the second element (line) of the tuple (tag, line)
    and returns an iterator of the modified tuples.
    """
    def processor(lines: Iterator[Line]) -> Iterator[Line]:
        for tag, line in lines:
            yield (tag, line.strip())  # Strip whitespace from each line
    return processor  

def print_lines() -> Callable[[Iterator[Line]], Iterator[Line]]:
    """
    Prints each line with its corresponding tag and yields the tuple (tag, line).
    """
    def processor(lines: Iterator[Line]) -> Iterator[Line]:
        for tag, line in lines:
            print(f"[{tag}] {line}")  # Print tag and line
            yield (tag, line)  # Yield the unchanged line
    return processor

def archive_lines() -> Callable[[Iterator[Line]], Iterator[Line]]:
    """
    Archives lines to a file called 'archive.txt'. Each line is written
    with its corresponding tag in the format [tag] line.
    """
    def processor(lines: Iterator[Line]) -> Iterator[Line]:
        with open("archive.txt", "a") as f:
            for tag, line in lines:
                f.write(f"[{tag}] {line}\n")  # Write to the file
                yield (tag, line)  # Yield the unchanged line
    return processor
