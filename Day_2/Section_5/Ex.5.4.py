import json
import csv
import pickle
from collections import namedtuple
from datetime import datetime

# 1. JSON Dump/Load: Serialize and deserialize a Python dict using json.dumps() and json.loads().
def json_dump_load():
    data = {"name": "Alice", "age": 30, "city": "New York"}
    json_str = json.dumps(data)
    print(f"Serialized JSON: {json_str}")
    
    deserialized_data = json.loads(json_str)
    print(f"Deserialized data: {deserialized_data}")

# 2. Pretty Print JSON: Dump a JSON string with indentation and sorting keys.
def pretty_print_json():
    data = {"name": "Alice", "age": 30, "city": "New York", "hobbies": ["Reading", "Swimming", "Cycling"]}
    pretty_json = json.dumps(data, indent=4, sort_keys=True)
    print(f"Pretty printed JSON:\n{pretty_json}")

# 3. CSV Read: Read data.csv and print each row using csv.DictReader.
def csv_read():
    # Sample data, assume it's in data.csv:
    # name,age,city
    # Alice,30,New York
    # Bob,25,Los Angeles
    
    with open('data.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"Row: {row}")

# 4. CSV Write: Write a list of dicts to a CSV file with headers.
def csv_write():
    data = [
        {"name": "Alice", "age": 30, "city": "New York"},
        {"name": "Bob", "age": 25, "city": "Los Angeles"}
    ]
    
    with open('output.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["name", "age", "city"])
        writer.writeheader()
        writer.writerows(data)
    
    print("Data written to output.csv")

# 5. Pickle a Python Object: Use pickle.dump() and load() on a basic object.
def pickle_object():
    obj = {"name": "Alice", "age": 30, "city": "New York"}
    
    with open('object.pkl', 'wb') as file:
        pickle.dump(obj, file)
        print("Object serialized and written to object.pkl")
    
    with open('object.pkl', 'rb') as file:
        loaded_obj = pickle.load(file)
        print(f"Deserialized object: {loaded_obj}")

# 6. Secure Unpickling: Discuss dangers of pickle and show safe alternatives (json, marshal).
def secure_unpickling():
    print("⚠️ Warning: Pickle can execute arbitrary code. Never unpickle data from untrusted sources!")
    print("Use JSON or other safer alternatives like marshal or XML for secure serialization.")

# 7. Custom JSON Encoder: Serialize a datetime object using a custom encoder.
class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()  # Convert datetime object to ISO string
        return super().default(obj)

def custom_json_encoder():
    dt = datetime.now()
    data = {"timestamp": dt}
    
    json_str = json.dumps(data, cls=CustomJSONEncoder)
    print(f"Serialized data with custom encoder: {json_str}")

# 8. Read CSV into NamedTuples: Use csv.reader with namedtuple to read structured rows.
def csv_read_namedtuple():
    # Sample data, assume it's in data.csv:
    # name,age,city
    # Alice,30,New York
    # Bob,25,Los Angeles
    
    Person = namedtuple('Person', ['name', 'age', 'city'])
    
    with open('data.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            person = Person(row['name'], row['age'], row['city'])
            print(f"NamedTuple: {person}")

# --- Example Usage ---
if __name__ == "__main__":
    json_dump_load()
    pretty_print_json()
    # csv_read()  # Make sure you have a 'data.csv' file
    csv_write()
    pickle_object()
    secure_unpickling()
    custom_json_encoder()
    # csv_read_namedtuple()  # Ensure 'data.csv' is available
