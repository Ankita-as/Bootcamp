"""
performance_debugging_demo.py

This script demonstrates various performance profiling and debugging techniques in Python:
- timeit for timing
- manual time measurement
- cProfile for function-level profiling
- line_profiler for line-by-line timing (optional)
- memory_profiler for memory usage tracking
- sorting performance comparison
"""

import time
import timeit
import random

# ------------------------------
# 1. TIMEIT Examples
# ------------------------------
print("\n--- Timeit Examples ---")
execution_time = timeit.timeit('sum(range(10000))', number=1000)
print(f'Time to execute sum(range(10000)) 1000x: {execution_time:.4f} seconds')

list_time = timeit.timeit('[x*x for x in range(1000000)]', number=10)
generator_time = timeit.timeit('(x*x for x in range(1000000))', number=10)
print(f'List comprehension time (10x): {list_time:.4f} seconds')
print(f'Generator expression time (10x): {generator_time:.4f} seconds')

# ------------------------------
# 2. Manual Timing with time
# ------------------------------
print("\n--- Manual Timing ---")
def slow_function():
    total = 0
    for i in range(1000000):
        total += i
    return total

start = time.time()
slow_function()
end = time.time()
print(f"Manual timing of slow_function: {end - start:.4f} seconds")

# ------------------------------
# 3. Sorting Benchmark
# ------------------------------
print("\n--- Sorting Benchmark ---")
numbers = random.sample(range(1, 100000), 10000)

# Built-in sort
start = time.time()
sorted_builtin = sorted(numbers)
end = time.time()
print(f"Built-in sorted() time: {end - start:.4f} seconds")

# Custom bubble sort (inefficient on purpose)
def bubble_sort(arr):
    arr = arr.copy()  # avoid in-place sorting
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

start = time.time()
bubble_sort(numbers[:500])  # limit size to avoid long runtime
end = time.time()
print(f"Custom bubble_sort() time on 500 elements: {end - start:.4f} seconds")

# ------------------------------
