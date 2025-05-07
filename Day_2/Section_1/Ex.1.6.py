# Manual Iterator
nums = [10, 20, 30]
it = iter(nums)
print(next(it))  # 10
print(next(it))  # 20
print(next(it))  # 30
# print(next(it))  # Uncomment to see StopIteration

print("\n--- Custom Iterator ---")
# Custom Iterator Class
class Counter:
    def __init__(self, max):
        self.max = max
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.max:
            self.current += 1
            return self.current
        else:
            raise StopIteration

c = Counter(3)
for num in c:
    print(num)

print("\n--- StopIteration Example ---")
# StopIteration manually
try:
    raise StopIteration("End manually triggered")
except StopIteration as e:
    print(e)

print("\n--- Simple Generator ---")
# Simple Generator
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for i in countdown(3):
    print(i)

print("\n--- Generator with State ---")
# Generator with running totals
def running_total(nums):
    total = 0
    for n in nums:
        total += n
        yield total

for value in running_total([1, 2, 3]):
    print(value)

print("\n--- Generator .send() ---")
# Generator with send()
def echo():
    received = yield "Start"
    while True:
        received = yield f"You said: {received}"

gen = echo()
print(next(gen))          # Start
print(gen.send("Hello"))  # You said: Hello
print(gen.send("Again"))  # You said: Again

print("\n--- Generator Expression ---")
# Generator Expression
evens = (x for x in range(10) if x % 2 == 0)
for e in evens:
    print(e, end=" ")
print()

print("\n--- List vs Generator Output ---")
# Compare For Loop vs Generator
comp_list = [x for x in range(10) if x % 2 == 0]
gen_expr = (x for x in range(10) if x % 2 == 0)

print("List comprehension:", comp_list)
print("Generator expression output:", list(gen_expr))  # force generator to list for fair comparison
