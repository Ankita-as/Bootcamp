# 1. List Operations
a = [5, 3, 8]
a.append(2)
a.remove(3)
a.sort()
print("List after operations:", a)

# 2. List Slicing
lst = [1, 2, 3, 4, 5, 6, 7]
middle_three = lst[2:5]
print("Middle 3 elements:", middle_three)

# 3. List Copying Pitfall
a = [1, 2, 3]
b = a
b.append(4)
print("Same reference -> a:", a)

a = [1, 2, 3]
b = a[:]
b.append(4)
print("Copied list -> a:", a)
print("Copied list -> b:", b)

# 4. Dictionary Access
user = {"name": "Alice"}
print("Name:", user.get("name"))
print("Age (default None):", user.get("age"))
user.setdefault("age", 25)
print("Updated user:", user)

# 5. Dictionary Iteration
person = {"name": "Bob", "age": 30}
for key, value in person.items():
    print(f"{key}: {value}")

# 6. Set Operations
a = {1, 2, 3}
b = {3, 4}
print("Intersection:", a & b)
print("Union:", a | b)
print("Difference:", a - b)

# 7. Tuple Unpacking
t = (7, 8, 9)
x, y, z = t
print("Tuple unpacked:", x, y, z)

# 8. Immutable Tuples
t = (1, 2, 3)
try:
    t[0] = 10
except TypeError as e:
    print("Error (tuples are immutable):", e)
