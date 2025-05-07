import contextlib
import time
import tempfile
from contextlib import suppress

# 1. Basic File Context
with open('example.txt', 'w') as f:
    f.write('Hello, World!')

with open('example.txt', 'r') as f:
    content = f.read()
    print("\n[1] Basic File Context:", content)

# 2. Multiple Contexts
with open('file1.txt', 'w') as f1, open('file2.txt', 'w') as f2:
    f1.write('File 1 content')
    f2.write('File 2 content')
print("\n[2] Multiple files written")

# 3. Custom Context Manager (class)
class Logger:
    def __enter__(self):
        print("\n[3] Entering Logger context...")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("[3] Exiting Logger context...")

with Logger():
    print("[3] Inside the Logger block")

# 4. Custom Context Manager with contextlib
@contextlib.contextmanager
def timer():
    start = time.time()
    yield
    end = time.time()
    print(f"[4] Elapsed time: {end - start:.2f} seconds")

with timer():
    time.sleep(1)

# 5. Suppressing Exceptions
print("\n[5] Trying to open a missing file with suppression:")
with suppress(FileNotFoundError):
    with open('nonexistent.txt') as f:
        print(f.read())
print("[5] No crash occurred")

# 6. Temporary File
print("\n[6] Using Temporary File:")
with tempfile.TemporaryFile(mode='w+t') as tf:
    tf.write('Temporary data')
    tf.seek(0)
    print("[6] Read from temp file:", tf.read())

# 7. Database-style Locking
class DBConnection:
    def __enter__(self):
        print("\n[7] Opening DB connection")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("[7] Closing DB connection")

with DBConnection():
    print("[7] Performing DB operations")

# 8. Ensure Cleanup Even if Error Occurs
class Cleaner:
    def __enter__(self):
        print("\n[8] Start cleanup test")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("[8] Cleaning up even after error!")

try:
    with Cleaner():
        print("[8] Doing something risky...")
        raise ValueError("Oops!")
except ValueError as e:
    print("[8] Caught exception:", e)
