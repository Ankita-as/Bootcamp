# cli.py
import typer
from .main import process_file  # Import the process_file function.

app = typer.Typer()

@app.command()
def cli(input: str, output: str, mode: str):
    """Command to process the file based on input, output, and mode."""
    process_file(input, output, mode)  # Call the main processing function.

if __name__ == "__main__":
    app()  # Run the app.
