import typer
from dotenv import load_dotenv
import os
from typing import Iterator, Optional

app = typer.Typer()

# Load the .env file
load_dotenv()

# Get default mode from environment or fallback
DEFAULT_MODE = os.getenv("MODE", "uppercase")

def read_lines(path: str) -> Iterator[str]:
    """Read lines from a file"""
    with open(path, 'r') as file:
        for line in file:
            yield line.strip()

def transform_line(line: str, mode: str) -> str:
    """Transform a line based on the mode"""
    if mode == "uppercase":
        return line.upper()
    elif mode == "snakecase":
        return line.lower().replace(" ", "_")
    else:
        return line

def write_output(lines: Iterator[str], output_path: Optional[str]) -> None:
    """Write output to a file or stdout"""
    if output_path:
        with open(output_path, "w") as file:
            for line in lines:
                file.write(line + "\n")
        print(f"✅ Output written to {output_path}")
    else:
        for line in lines:
            print(line)

@app.command()
def main(
    input: str = typer.Option(..., help="Input file path"),
    output: Optional[str] = typer.Option(None, help="Output file path (optional)"),
    mode: str = typer.Option(DEFAULT_MODE, help="Processing mode: uppercase or snakecase")
):
    """Process text lines from a file"""
    lines = (transform_line(line, mode) for line in read_lines(input))
    write_output(lines, output)

if __name__ == "__main__":
    app()
