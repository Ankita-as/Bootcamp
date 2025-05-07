import typer

def say_hello(name: str):
    """Print a hello message."""
    print(f"Hello, {name}! ✨")

app = typer.Typer()

@app.command()
def hello(name: str):
    """Greet a person by name."""
    say_hello(name)

if __name__ == "__main__":
    app()

