# core.py

def to_uppercase(line: str) -> str:
    """Converts the line to uppercase."""
    return line.upper()

def to_snakecase(line: str) -> str:
    """Converts the line to snake_case."""
    return line.lower().replace(" ", "_")
