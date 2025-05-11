def process_file(filepath):
    print(f"Processing file: {filepath}")
    try:
        with open(filepath, "r") as f:
            content = f.read()
            print(f"File content:\n{content}")
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
