import sys
import os

# Add parent dir to sys.path so imports like 'from processors' work
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import typer
from Abstraction_level_3.main import process_file  # Use absolute import

app = typer.Typer()

@app.command()
def cli(input: str, output: str, config: str):
    """Run the text processor with the given config."""
    process_file(input, output, config)

if __name__ == "__main__":
    app()
