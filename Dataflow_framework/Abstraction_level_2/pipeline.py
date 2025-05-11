from .processor_types import to_snakecase  # Import your processor function

def build_pipeline(mode: str):
    """Build the pipeline based on the selected mode."""
    if mode == 'snakecase':
        return [to_snakecase]  # Only snakecase processor for now
    # You can add other modes here if needed
    return []
