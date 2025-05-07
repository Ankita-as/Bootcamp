import sys

# 1. List Comprehension with Condition
nums = [1, 2, 3, 4]
squares_of_evens = [x**2 for x in nums if x % 2 == 0]
print("List Comprehension with Condition:", squares_of_evens)

# 2. Nested List Comprehension
nested = [[1, 2], [3, 4]]
flattened = [x for sublist in nested for x in sublist]
print("Flattened List:", flattened)

# 3. Dictionary Comprehension
letters = ["a", "b"]
letter_dict = {ch: 1 for ch in letters}
print("Dict Comprehension:", letter_dict)

# 4. Set Comprehension (unique vowels from a string)
vowels = {"a", "e", "i", "o", "u"}
unique_vowels = {ch for ch in "hello world" if ch in vowels}
print("Unique Vowels:", unique_vowels)

# 5. Generator Expression
gen = (n * n for n in range(5))
print("Generator Expression output:")
for item in gen:
    print(item, end=' ')
print()

# 6. List vs Generator (memory comparison)
list_comp = [x for x in range(1000000)]
gen_expr = (x for x in range(1000000))
print("List memory (bytes):", sys.getsizeof(list_comp))
print("Generator memory (bytes):", sys.getsizeof(gen_expr))

# 7. Filter with Comprehension
words = ["hi", "hello", "bye"]
even_length = [w for w in words if len(w) % 2 == 0]
print("Even length words:", even_length)

# 8. Conditional Assignment in Comprehension
nums = [3, -1, 5, -2]
non_negative = [x if x > 0 else 0 for x in nums]
print("Negative replaced with 0:", non_negative)
