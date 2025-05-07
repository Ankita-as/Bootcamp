import sys
import itertools
import os

# ----------------------------
# 1. Large Data with Generators
# ----------------------------
def read_large_file(filepath):
    """Generator to read a file line by line."""
    with open(filepath, 'r') as file:
        for line in file:
            yield line.strip()

# Example: simulate large file
sample_file = 'sample_large.txt'
if not os.path.exists(sample_file):
    with open(sample_file, 'w') as f:
        for i in range(100000):
            f.write(f"Line number {i}\n")

lines_gen = read_large_file(sample_file)

# ----------------------------
# 2. Generator vs List Memory
# ----------------------------
list_data = [x for x in range(1000000)]
gen_data = (x for x in range(1000000))

print("\n--- Memory Usage ---")
print(f"List: {sys.getsizeof(list_data)} bytes")
print(f"Generator: {sys.getsizeof(gen_data)} bytes")

# ----------------------------
# 3. Lazy CSV Filter (simulated)
# ----------------------------
def lazy_filter(lines):
    """Yield only lines containing the word '9999'."""
    for line in lines:
        if '9999' in line:
            yield line

filtered = lazy_filter(read_large_file(sample_file))
print("\n--- Lazy Filter Example ---")
for line in itertools.islice(filtered, 1):  # print one matching line
    print(f"Matched line: {line}")

# ----------------------------
# 4. Short-Circuiting with any()
# ----------------------------
print("\n--- any() Short-Circuit ---")
big_list = range(1, 1000000)
has_divisible = any(x % 99999 == 0 for x in big_list)
print(f"Any number divisible by 99999: {has_divisible}")

# ----------------------------
# 5. Use itertools.islice
# ----------------------------
print("\n--- First 10 Lines ---")
first_10 = itertools.islice(read_large_file(sample_file), 10)
for line in first_10:
    print(line)

# ----------------------------
# 6. Avoid Temporary Lists
# ----------------------------
print("\n--- Sum with Generator ---")
sum_gen = sum(x for x in range(1000000))
print(f"Sum using generator: {sum_gen}")

# ----------------------------
# 7. Streaming File Copy
# ----------------------------
print("\n--- Streaming File Copy ---")
destination_file = 'copied_file.txt'
with open(sample_file, 'r') as src, open(destination_file, 'w') as dst:
    for line in src:
        dst.write(line)

print("File copy completed.")

# ----------------------------
# 8. Yield vs Return
# ----------------------------
def squares_up_to(n):
    """Yield squares up to n (lazy)."""
    for i in range(n):
        yield i * i

print("\n--- Yield Example ---")
for val in itertools.islice(squares_up_to(10), 5):
    print(val)
