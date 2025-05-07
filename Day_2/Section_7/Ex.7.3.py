import logging
import traceback
import warnings
import pdb

# Setup structured logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# ----------------------------
# 1. Function with pdb.set_trace()
# ----------------------------
def inspect_variables(a, b):
    logger.debug("Entering inspect_variables()")
    pdb.set_trace()  # Pause execution here for debugging
    return a + b

# ----------------------------
# 2. Using Python 3.7+ breakpoint()
# ----------------------------
def debug_with_breakpoint(x):
    logger.debug("Entering debug_with_breakpoint()")
    breakpoint()  # Will open interactive debugger if run in terminal
    return x ** 2

# ----------------------------
# 3. Using traceback for detailed error trace
# ----------------------------
def catch_and_trace():
    try:
        1 / 0
    except Exception:
        logger.error("An exception occurred:\n%s", traceback.format_exc())

# ----------------------------
# 4. Structured logging for entry/exit
# ----------------------------
def calculate_area(length, width):
    logger.debug(f"calculate_area() start: length={length}, width={width}")
    area = length * width
    logger.debug(f"calculate_area() end: area={area}")
    return area

# ----------------------------
# 5. Using warnings module
# ----------------------------
def risky_action():
    warnings.warn("This action is deprecated and may be removed in future versions.", DeprecationWarning)
    return True

# ----------------------------
# 6. Verbose exception handling
# ----------------------------
def divide(a, b):
    try:
        return a / b
    except Exception as e:
        print("Exception caught:", type(e), e)
        raise  # Fail loud, then gracefully

# ----------------------------
# 7. Debug recursive call stack
# ----------------------------
def factorial(n, level=0):
    logger.debug("  " * level + f"factorial({n})")
    if n == 0:
        return 1
    return n * factorial(n - 1, level + 1)

# ----------------------------
# 8. Main function to demonstrate all
# ----------------------------
if __name__ == "__main__":
    # Uncomment lines one by one to test interactively
    # inspect_variables(10, 5)
    # debug_with_breakpoint(3)
    
    catch_and_trace()
    print("Area:", calculate_area(5, 3))
    risky_action()
    
    try:
        result = divide(10, 0)
    except ZeroDivisionError:
        logger.error("Handled ZeroDivisionError gracefully.")

    print("Factorial of 5:", factorial(5))
