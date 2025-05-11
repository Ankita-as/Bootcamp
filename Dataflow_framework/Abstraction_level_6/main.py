# main.py
from engine.router import Router

if __name__ == "__main__":
    # Some dummy input
    input_lines = [
        "This is a warning",
        "Critical error occurred!",
        "Just some general log"
    ]

    router = Router("config.yaml")
    router.run(iter(input_lines))
