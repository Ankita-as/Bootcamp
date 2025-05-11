# processor_types.py
def to_snakecase(text: str) -> str:
    """Convert the input text to snake_case."""
    return text.replace(" ", "_").lower()
