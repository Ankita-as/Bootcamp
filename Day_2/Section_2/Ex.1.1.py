# EAFP vs LBYL
print("=== EAFP vs LBYL ===")

# EAFP Basics
my_dict = {"name": "Alice", "age": 30}

try:
    print(my_dict["address"])
except KeyError:
    print("Key 'address' not found. Using EAFP approach!")

# LBYL Basics
if "address" in my_dict:
    print(my_dict["address"])
else:
    print("Key 'address' not found. Using LBYL approach!")

print("\n=== File Handling (EAFP) ===")

# File Handling (EAFP)
try:
    with open("sample.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found. Using EAFP approach!")

print("\n=== Attribute Access (EAFP) ===")

# Attribute Access (EAFP)
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Bob")

# Safely access an attribute that might not exist
print(getattr(p, "name", "Attribute not found"))
print(getattr(p, "age", "Attribute not found"))  # Non-existent attribute

print("\n=== LBYL Pitfall (Race Condition) ===")

# LBYL Pitfall (Race Condition)
import os

# Suppose we check if a file exists and then open it
file_name = "sample.txt"
if os.path.exists(file_name):
    with open(file_name, "r") as file:
        print(file.read())
else:
    print(f"File {file_name} does not exist.")
# In a multi-threaded environment, a race condition could occur here

print("\n=== Custom Object with __getattr__ ===")

# Custom Object: Custom __getattr__
class DynamicObject:
    def __init__(self):
        self.existing_attr = "I exist"

    def __getattr__(self, attr):
        # Dynamically handle missing attributes
        return f"'{attr}' not found, but handled by __getattr__!"

obj = DynamicObject()
print(obj.existing_attr)
print(obj.non_existent_attr)  # Will call __getattr__

print("\n=== Safe Type Conversion (EAFP) ===")

# Safe Type Conversion (EAFP)
user_input = "42"
try:
    user_age = int(user_input)
    print(f"User age: {user_age}")
except ValueError:
    print("Invalid input! Could not convert to integer.")

print("\n=== When to Prefer LBYL ===")

# When to Prefer LBYL: Using isinstance to check types before applying methods
def print_length(s):
    if isinstance(s, str):
        print(f"Length of string: {len(s)}")
    else:
        print("Provided input is not a string!")

print_length("Hello")
print_length(123)  # This will check the type before calling len
