# 1. LEGB Rule
x = 10  # Global

def print_local_x():
    x = 20  # Local
    print("Local x:", x)

print_local_x()
print("Global x:", x)

# 2. Nested Function Access
def outer():
    message = "Hello from outer!"
    def inner():
        print(message)  # accessing outer variable
    inner()

outer()

# 3. nonlocal
def outer_counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        print("Count:", count)
    increment()
    increment()

outer_counter()

# 4. global
y = 5

def modify_global():
    global y
    y += 2
    print("Modified global y:", y)

modify_global()
print("Global y now:", y)

# 5. Closure Function
def make_multiplier(n):
    def multiplier(x):
        return n * x
    return multiplier

# 6. Closure Memory
triple = make_multiplier(3)
print("Triple of 10:", triple(10))

# 7. Name Shadowing
len = 5
# print(len(["a", "b"]))  # ❌ Error: 'int' object is not callable

# 8. Scope Error
def scope_error():
    # print(value)  # ❌ Uncommenting this gives UnboundLocalError
    value = 10
    print(value)

scope_error()
