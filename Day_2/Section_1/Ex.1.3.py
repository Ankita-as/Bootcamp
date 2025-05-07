# 1. Default Arguments
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()
greet("Ankita")

# 2. Keyword Arguments
def info(name, age=0):
    print(f"Name: {name}, Age: {age}")

info(age=22, name="Ankita")

# 3. Variable Positional Args
def add_all(*args):
    return sum(args)

print("Sum:", add_all(1, 2, 3, 4))

# 4. Variable Keyword Args
def show_settings(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_settings(theme="dark", font="Arial", size=12)

# 5. Mixed Args
def mixed_function(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

mixed_function(1, 2, a="apple", b="banana")

# 6. Positional-Only Args (Python 3.8+)
def multiply(x, y, /):
    return x * y

print("Positional-only multiply:", multiply(3, 4))
# multiply(x=3, y=4)  # ❌ This would cause an error

# 7. Keyword-Only Args
def divide(*, numerator, denominator):
    return numerator / denominator

print("Keyword-only divide:", divide(numerator=10, denominator=2))
# divide(10, 2)  # ❌ This would cause an error

# 8. Function Annotations
def add(a: int, b: int) -> int:
    return a + b

print("Annotated add:", add(5, 7))
