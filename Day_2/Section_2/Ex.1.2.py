# Enumerate
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# Zip
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
zipped = zip(numbers, letters)
print(list(zipped))

# any / all
nums = [-1, 2, 3]
print(any(n < 0 for n in nums))  # True
print(all(n > 0 for n in nums))  # False

# Sorted with key
tuples = [(1, 'apple'), (3, 'banana'), (2, 'cherry')]
print(sorted(tuples, key=lambda x: x[1]))  # Sort by second item

# Map and Filter
nums = [1, 2, 3, 4]
print(list(map(lambda x: x * 2, nums)))  # [2, 4, 6, 8]
print(list(filter(lambda x: x % 2 == 0, nums)))  # [2, 4]

# Chained Comparison
x = 5
if 0 < x < 10:
    print("x is between 0 and 10.")

# Inline swap
a, b = 10, 20
a, b = b, a
print(f"a: {a}, b: {b}")

# Unpacking in loops
pairs = [(1, 2), (3, 4), (5, 6)]
for x, y in pairs:
    print(f"x: {x}, y: {y}")
