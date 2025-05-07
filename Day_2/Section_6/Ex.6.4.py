import logging

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

# Function demonstrating different logging levels
def process_user_data(user_name, age, debug=False):
    if debug:
        logger.debug(f"Processing user: {user_name}, Age: {age}")  # Only log if debug flag is True
    if age < 18:
        logger.warning(f"User {user_name} is under 18 years old.")  # Log a warning
    else:
        logger.info(f"User {user_name} is of valid age.")  # Log an info message
    try:
        # Simulate a possible error
        if user_name == "ErrorUser":
            raise ValueError("Simulated error for user.")
    except ValueError as e:
        logger.error(f"An error occurred: {e}")  # Log the error
    logger.info(f"Completed processing for {user_name}.")  # Log info after processing

# Example usage
process_user_data("Alice", 30, debug=True)
process_user_data("Bob", 17, debug=False)
process_user_data("ErrorUser", 25)