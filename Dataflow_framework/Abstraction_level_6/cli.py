import typer
from engine.router import Router

app = typer.Typer()

@app.command()
def run(config_path: str = typer.Option(..., "--config-path", help="Path to the config file")):
    """
    Run the routing engine with the specified config file.
    """
    print(f"✅ Running router with config at: {config_path}")
    
    # Create Router instance with the provided config path
    router = Router(config_path)
    
    # Example initial lines. These could be dynamically loaded based on the config or user input.
    initial_lines = ["This is an error message", "This is a warning message"]  # Example input lines
    
    # Run the router with the config file
    router.run(iter(initial_lines))

if __name__ == "__main__":
    app()
