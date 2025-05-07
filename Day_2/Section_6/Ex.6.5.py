import logging

# Constants for configuration
MAX_RETRIES = 3

# Set up logging configuration
logging.basicConfig(
    level=logging.DEBUG,  # Set the default logging level to DEBUG
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",  # Include timestamp, logger name, level, and message
    handlers=[
        logging.StreamHandler(),  # Log to console (stdout)
        logging.FileHandler('app.log')  # Log to a file (app.log)
    ]
)

# Create a logger using the module's name (__name__)
logger = logging.getLogger(__name__)

# Module-level docstring
"""
This module processes user data, checks for age validation, and logs user information.
"""

def is_valid_age(age: int) -> bool:
    """Check if the user's age is valid (i.e., greater than 0)."""
    return age > 0

def log_debug_info(user_name: str, age: int) -> None:
    """Log debug information for user processing."""
    logger.debug(f"Processing user: {user_name}, Age: {age}")

def log_valid_age(user_name: str) -> None:
    """Log info if the user's age is valid."""
    logger.info(f"User {user_name} is of valid age.")

def log_underage(user_name: str) -> None:
    """Log a warning if the user is underage."""
    logger.warning(f"User {user_name} is under 18 years old.")

def log_error_for_user(user_name: str, error: str) -> None:
    """Log an error message for the user."""
    logger.error(f"An error occurred for {user_name}: {error}")

def process_user_data(user_name: str, age: int, debug: bool = False) -> None:
    """Process and validate user data, logging relevant information based on age."""
    if debug:
        log_debug_info(user_name, age)

    if is_valid_age(age):
        log_valid_age(user_name)
    else:
        log_underage(user_name)

    try:
        # Simulate an error for a specific user
        if user_name == "ErrorUser":
            raise ValueError("Simulated error for user.")
    except ValueError as e:
        log_error_for_user(user_name, str(e))
    
    logger.info(f"Completed processing for {user_name}.")

# Example usage
process_user_data("Alice", 30, debug=True)
process_user_data("Bob", 17, debug=False)
process_user_data("ErrorUser", 25)