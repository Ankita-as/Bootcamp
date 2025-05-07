import logging
import os
import time
import uuid
import functools
import random
import psutil  # pip install psutil

# Set DEBUG flag based on environment
DEBUG = os.getenv("DEBUG", "False") == "True"

# Configure logger
logging.basicConfig(
    level=logging.DEBUG if DEBUG else logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Global metrics store
metrics = {
    "calls": {},
    "errors": {},
    "timings": {}
}

# --------------------------------
# Decorator to trace function calls
# --------------------------------
def trace(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        user_id = kwargs.get('user_id', 'unknown')
        logger.info(f"[User {user_id}] Calling {func.__name__} with args={args}, kwargs={kwargs}")
        start = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start
        metrics["calls"][func.__name__] = metrics["calls"].get(func.__name__, 0) + 1
        metrics["timings"][func.__name__] = duration
        logger.info(f"[User {user_id}] {func.__name__} returned {result} in {duration:.4f}s")
        return result
    return wrapper

# --------------------------------
# Simulate a business function
# --------------------------------
@trace
def process_order(order_id, user_id=None):
    if random.random() < 0.3:
        error_id = str(uuid.uuid4())[:8]
        logger.error(f"[User {user_id}] Error E101: Failed to process order {order_id}. Error ID: {error_id}")
        metrics["errors"][error_id] = "Order processing failed"
        return None
    time.sleep(random.uniform(0.1, 0.5))
    return f"Order {order_id} processed"

# --------------------------------
# Health Check Function
# --------------------------------
def health_check():
    status = {
        "cpu_percent": psutil.cpu_percent(),
        "memory_percent": psutil.virtual_memory().percent,
        "status": "ok"
    }
    logger.info(f"Health Check: {status}")
    return status

# --------------------------------
# Print System Resource Usage
# --------------------------------
def print_resource_usage():
    logger.info(f"CPU usage: {psutil.cpu_percent()}%")
    logger.info(f"Memory usage: {psutil.virtual_memory().percent}%")

# --------------------------------
# Main Execution
# --------------------------------
if __name__ == "__main__":
    users = [101, 102, 103]
    for i in range(5):
        user = random.choice(users)
        process_order(order_id=i+1, user_id=user)

    print_resource_usage()
    health_check()

    logger.info("Metrics Summary:")
    for key, value in metrics.items():
        logger.info(f"{key.upper()}: {value}")
