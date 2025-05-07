import typer

def hello():
    print("Hello, World!")

app = typer.Typer()
app.command()(hello)

if __name__ == "__main__":
    app()
