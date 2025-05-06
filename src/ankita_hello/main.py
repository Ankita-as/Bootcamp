# src/ankita_hello/main.py

from typing import Optional
import typer

app = typer.Typer()

@app.command()
def greet(name: Optional[str] = "world") -> None:
    """
    Greets the user by name, or 'world' by default.

    Args:
        name (Optional[str]): The name to greet.
    """
    print(f"Hello, {name}!")

if __name__ == "__main__":
    app()
