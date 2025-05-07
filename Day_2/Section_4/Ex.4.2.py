import time
from functools import wraps

# 1. Basic Function Decorator
def simple_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Function started")
        result = func(*args, **kwargs)
        print("Function ended")
        return result
    return wrapper

# 2. Decorator with Arguments
def prefix_printer(prefix):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"{prefix} - Calling {func.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

# 3. Timing Decorator
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f}s")
        return result
    return wrapper

# 4. Memoization Decorator
def memoize(func):
    cache = {}
    @wraps(func)
    def wrapper(*args):
        if args in cache:
            print("Returning from cache")
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

# 5. Debug Information Decorator
def debug_info(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args} {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

# 6. Access Control Decorator
def role_required(required_role):
    def decorator(func):
        @wraps(func)
        def wrapper(user, *args, **kwargs):
            if user.get("role") == required_role:
                return func(user, *args, **kwargs)
            else:
                print("Access denied.")
        return wrapper
    return decorator

# 7. Retry Mechanism Decorator
def retry(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt} failed: {e}")
            print("All retries failed.")
        return wrapper
    return decorator

# 8. Logging Decorator with Parameters
def custom_logger(message):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"{message} - Starting {func.__name__}")
            result = func(*args, **kwargs)
            print(f"{message} - Ended {func.__name__}")
            return result
        return wrapper
    return decorator

# 9. Class Method Decorator
def validate_args(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        print(f"Validating args: {args}")
        return func(self, *args, **kwargs)
    return wrapper

# 10. Composition of Decorators
@simple_logger
@timer
@debug_info
def composed_function(x, y):
    time.sleep(0.1)
    return x + y


# --- Example Usage ---
if __name__ == "__main__":
    @prefix_printer(">>>")
    def greet(name):
        print(f"Hello, {name}!")

    @memoize
    def fibonacci(n):
        if n in (0, 1):
            return n
        return fibonacci(n-1) + fibonacci(n-2)

    @role_required("admin")
    def delete_user(user, user_id):
        print(f"User {user_id} deleted by {user['name']}")

    @retry(3)
    def risky():
        raise ValueError("Oops!")

    @custom_logger("LOG")
    def add(a, b):
        return a + b

    class Math:
        @validate_args
        def multiply(self, a, b):
            return a * b

    # Execute test cases
    greet("Alice")
    print("Fib(5):", fibonacci(5))
    delete_user({"name": "Ankita", "role": "admin"}, 101)
    risky()
    print("Add result:", add(3, 4))
    print("Composed function result:", composed_function(5, 6))

    m = Math()
    print("Multiply:", m.multiply(3, 4))
