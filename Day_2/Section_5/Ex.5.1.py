import collections

# 1. defaultdict for Grouping: Group words by their first letter using a defaultdict(list).
def group_words_by_first_letter():
    words = ['apple', 'banana', 'apricot', 'cherry', 'blueberry']
    grouped = collections.defaultdict(list)
    
    for word in words:
        grouped[word[0]].append(word)
    
    print("Grouped words by first letter:")
    for letter, group in grouped.items():
        print(f"{letter}: {group}")

# 2. Counter Basics: Count character frequencies in "hello world" using collections.Counter.
def count_characters():
    text = "hello world"
    counter = collections.Counter(text)
    
    print("\nCharacter frequencies in 'hello world':")
    print(counter)

# 3. Most Common Elements: Use Counter(...).most_common(2) on a list of numbers.
def most_common_elements():
    numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    counter = collections.Counter(numbers)
    most_common = counter.most_common(2)
    
    print("\nMost common elements in the list:")
    print(most_common)

# 4. deque for Stack and Queue: Use deque.appendleft() and pop() to simulate a stack and queue.
def simulate_stack_and_queue():
    # Stack (LIFO - Last In, First Out)
    stack = collections.deque()
    stack.append(1)
    stack.append(2)
    stack.append(3)
    
    print("\nStack operations (LIFO):")
    print("Stack:", stack)
    print("Popped:", stack.pop())  # Stack pop (Last in, First out)
    print("Stack after pop:", stack)

    # Queue (FIFO - First In, First Out)
    queue = collections.deque()
    queue.append(1)
    queue.append(2)
    queue.append(3)
    
    print("\nQueue operations (FIFO):")
    print("Queue:", queue)
    print("Popped:", queue.popleft())  # Queue pop (First in, First out)
    print("Queue after popleft:", queue)

# 5. Rotate a deque: Rotate a deque by 2 positions and print the result.
def rotate_deque():
    deque = collections.deque([1, 2, 3, 4, 5])
    print("\nDeque before rotation:", deque)
    deque.rotate(2)  # Rotate the deque by 2 positions
    print("Deque after rotation by 2 positions:", deque)

# 6. OrderedDict Iteration: Preserve order of insertion and iterate over items.
def ordered_dict_iteration():
    ordered_dict = collections.OrderedDict()
    ordered_dict['one'] = 1
    ordered_dict['two'] = 2
    ordered_dict['three'] = 3
    
    print("\nOrderedDict items:")
    for key, value in ordered_dict.items():
        print(f"{key}: {value}")

# 7. Defaultdict with Lambda: Create a defaultdict(lambda: 'N/A') and access missing keys.
def defaultdict_with_lambda():
    my_dict = collections.defaultdict(lambda: "N/A")
    my_dict['a'] = 1
    my_dict['b'] = 2
    
    print("\nAccessing missing keys in defaultdict:")
    print("a:", my_dict['a'])
    print("b:", my_dict['b'])
    print("c:", my_dict['c'])  # 'c' doesn't exist, so it returns 'N/A'

# 8. Nested defaultdict: Build a defaultdict(dict) or defaultdict(defaultdict(int)) for hierarchical data.
def nested_defaultdict():
    nested_dict = collections.defaultdict(lambda: collections.defaultdict(int))
    
    # Example: Store values with nested dictionaries
    nested_dict['fruit']['apple'] += 10
    nested_dict['fruit']['banana'] += 5
    nested_dict['vegetable']['carrot'] += 7
    
    print("\nNested defaultdict:")
    print(nested_dict)

# --- Example Usage ---
if __name__ == "__main__":
    group_words_by_first_letter()
    count_characters()
    most_common_elements()
    simulate_stack_and_queue()
    rotate_deque()
    ordered_dict_iteration()
    defaultdict_with_lambda()
    nested_defaultdict()
