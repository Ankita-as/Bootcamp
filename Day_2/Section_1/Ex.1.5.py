# try/except
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide")

# try/except/else
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Cannot divide")
else:
    print("Success")

# finally block
try:
    x = 5 / 0
except ZeroDivisionError:
    print("Error occurred")
finally:
    print("Cleanup done")

# multiple exceptions
try:
    num = int("abc")
    result = 10 / 0
except ValueError:
    print("Invalid number")
except ZeroDivisionError:
    print("Cannot divide by zero")

# custom exception
class InvalidAgeError(Exception):
    pass

age = -5
if age < 0:
    raise InvalidAgeError("Age cannot be negative")

# reraise exception
try:
    raise ValueError("Something went wrong")
except ValueError as e:
    print("Logging error:", e)
    raise

# suppressing exceptions
from contextlib import suppress

d = {"name": "Ankita"}
with suppress(KeyError):
    print(d["age"])  # KeyError will be ignored

# nested try blocks
try:
    try:
        print(10 / 0)
    except ZeroDivisionError:
        print("Inner block: Division by zero")
    x = int("abc")
except ValueError:
    print("Outer block: Invalid integer")
