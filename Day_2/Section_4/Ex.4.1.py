# 1. Pass Function as Argument
def apply(func, value):
    return func(value)

# 2. Return Function from Function
def make_doubler():
    return lambda x: x * 2

# 3. Store Functions in a List
function_list = [abs, str, hex]

# 4. Use map with Lambda
squared = list(map(lambda x: x ** 2, [1, 2, 3]))

# 5. Use filter with Lambda
evens = list(filter(lambda x: x % 2 == 0, range(10)))

# 6. Sort with Lambda Key
sorted_pairs = sorted([(1, "b"), (2, "a")], key=lambda x: x[1])

# 7. Inline Function Composition
def compose(f, g):
    return lambda x: f(g(x))

# 8. Closure with Lambda
def multiplier(factor):
    return lambda x: x * factor

# --- Main Execution ---
if __name__ == "__main__":
    # Apply function
    print("Apply abs to -10:", apply(abs, -10))

    # Return function
    doubler = make_doubler()
    print("Doubler of 5:", doubler(5))

    # Store functions and apply to -42
    print("\nApplying function list to -42:")
    for func in function_list:
        print(f"{func.__name__}(-42) = {func(-42)}")

    # Map with lambda
    print("\nSquares using map + lambda:", squared)

    # Filter with lambda
    print("Even numbers from 0–9:", evens)

    # Sorted list
    print("Sorted by second element:", sorted_pairs)

    # Compose function
    inc = lambda x: x + 1
    double = lambda x: x * 2
    composed = compose(double, inc)
    print("Compose double(inc(x)) where x = 3:", composed(3))  # (3+1)*2 = 8

    # Closure lambda
    triple = multiplier(3)
    print("Triple of 4:", triple(4))
