import itertools

# 1. Use count to Generate IDs: Create an infinite ID generator using itertools.count().
def generate_ids():
    id_gen = itertools.count(start=1, step=1)  # start at 1, increment by 1
    for _ in range(5):  # Generate 5 IDs for demonstration
        print(next(id_gen))

# 2. Use cycle to Repeat a Pattern: Cycle through ["red", "green", "blue"] and print 6 items.
def repeat_pattern():
    pattern = itertools.cycle(["red", "green", "blue"])
    for _ in range(6):  # Print 6 items
        print(next(pattern))

# 3. Use repeat to Duplicate Values: Generate a list of ten Nones using itertools.repeat(None, 10).
def repeat_none():
    none_list = list(itertools.repeat(None, 10))  # Repeat None 10 times
    print(none_list)

# 4. Use chain to Flatten: Combine [1, 2], [3, 4], [5] into one iterator using itertools.chain.
def flatten_lists():
    combined = itertools.chain([1, 2], [3, 4], [5])
    print(list(combined))

# 5. Use islice: Skip first 3 and take next 4 elements from a range using itertools.islice.
def slice_range():
    sliced = itertools.islice(range(10), 3, 7)  # Skip 3, take next 4 elements (index 3 to 6)
    print(list(sliced))

# 6. Use tee: Duplicate an iterator and iterate independently on both copies.
def duplicate_iterator():
    it = iter([1, 2, 3, 4, 5])
    it1, it2 = itertools.tee(it, 2)
    print("Iterator 1:", list(it1))
    print("Iterator 2:", list(it2))

# 7. Use groupby: Group a list of dicts by a shared key and print grouped items.
def group_by_key():
    items = [{'name': 'apple', 'type': 'fruit'}, {'name': 'carrot', 'type': 'vegetable'},
             {'name': 'banana', 'type': 'fruit'}, {'name': 'spinach', 'type': 'vegetable'}]
    # First, sort items by 'type' (groupby requires sorted input)
    items.sort(key=lambda x: x['type'])
    grouped = itertools.groupby(items, key=lambda x: x['type'])
    
    for key, group in grouped:
        print(f"Group: {key}")
        for item in group:
            print(item)

# 8. Use permutations and combinations: Generate all pairs and triples from [1, 2, 3].
def generate_combinations():
    items = [1, 2, 3]
    pairs = list(itertools.permutations(items, 2))  # Pairs (order matters)
    triples = list(itertools.combinations(items, 3))  # Triples (order doesn't matter)
    
    print("Pairs (permutations):", pairs)
    print("Triples (combinations):", triples)

# --- Example Usage ---
if __name__ == "__main__":
    print("Generate IDs:")
    generate_ids()
    print("\nRepeat Pattern:")
    repeat_pattern()
    print("\nRepeat None:")
    repeat_none()
    print("\nFlatten Lists:")
    flatten_lists()
    print("\nSlice Range:")
    slice_range()
    print("\nDuplicate Iterator:")
    duplicate_iterator()
    print("\nGroup By Key:")
    group_by_key()
    print("\nGenerate Combinations:")
    generate_combinations()
