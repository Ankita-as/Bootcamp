import time
import functools

# 1. Partial Function: Fix the base of int(x, base) to base 2
base2 = functools.partial(int, base=2)

# 2. lru_cache Memoization: Recursive Fibonacci with memoization
@functools.lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

# 3. Function Metadata with wraps: Decorator that preserves metadata
def function_metadata(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Executing {func.__name__}")
        result = func(*args, **kwargs)
        return result
    return wrapper

# 4. Chained Partials: Apply partial multiple times to customize print
def custom_print(*args, **kwargs):
    print(*args, **kwargs)

print_with_prefix = functools.partial(custom_print, "Prefix:")
print_with_timestamp = functools.partial(print_with_prefix, "Timestamp: 2025-05-07")

# 5. Uncached Recursive Function: Compare performance with and without lru_cache
def uncached_fib(n):
    if n <= 1:
        return n
    return uncached_fib(n-1) + uncached_fib(n-2)

# 6. reduce with Lambda: Use reduce to compute factorial
from functools import reduce

def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n+1))

# 7. Default Dict Generator: Use partial with dict to generate nested dicts
default_dict = functools.partial(dict, key=lambda k: k + "_value")

# 8. Log Decorator with wraps: Build a decorator that logs execution
def log_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Logging: {func.__name__} is being executed")
        result = func(*args, **kwargs)
        print(f"Logging: {func.__name__} executed successfully")
        return result
    return wrapper

@log_decorator
def greet(name):
    print(f"Hello, {name}!")

# --- Example Usage ---
if __name__ == "__main__":
    # Partial Function Example: Convert binary to integer
    print("Base 2 of 1101:", base2("1101"))

    # Fibonacci with and without lru_cache
    start = time.time()
    print("Uncached Fibonacci result:", uncached_fib(30))  # Slow
    print("Uncached Fibonacci took:", time.time() - start)

    start = time.time()
    print("Cached Fibonacci result:", fib(30))  # Fast
    print("Cached Fibonacci took:", time.time() - start)

    # Function Metadata with wraps
    @function_metadata
    def sample_function(a, b):
        return a + b
    print(sample_function(2, 3))

    # Chained Partials
    print_with_timestamp("Hello world!")

    # Factorial using reduce
    print("Factorial of 5:", factorial(5))

    # Default Dict Generator Example
    print("Generated dict:", default_dict())

    # Log Decorator Example
    greet("Alice")
