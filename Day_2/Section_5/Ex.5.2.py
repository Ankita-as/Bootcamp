import os
import shutil
from pathlib import Path
import tempfile

# 1. Read a File with pathlib: Use Path("myfile.txt").read_text() to read file content.
def read_file_with_pathlib():
    file_path = Path("myfile.txt")
    
    # Check if file exists
    if file_path.exists():
        content = file_path.read_text()
        print("\nFile content:")
        print(content)
    else:
        print("\nFile 'myfile.txt' does not exist.")

# 2. List Files in a Directory: Use Path(".").glob("*.py") to list all Python files.
def list_python_files():
    print("\nListing Python files in the current directory:")
    for py_file in Path(".").glob("*.py"):
        print(py_file)

# 3. Write to a File: Write "hello" to a file using pathlib or open(..., "w").
def write_to_file():
    file_path = Path("output.txt")
    file_path.write_text("hello")
    print(f"\n'hello' written to {file_path}")

# 4. Create and Delete File/Directory: Use os.makedirs(), shutil.rmtree() safely inside a temporary directory.
def create_and_delete_directory():
    temp_dir = Path("temp_directory")
    
    # Create a directory
    os.makedirs(temp_dir, exist_ok=True)
    print(f"\nDirectory created: {temp_dir}")
    
    # Create a file inside the directory
    file_path = temp_dir / "temp_file.txt"
    file_path.write_text("Temporary file content")
    print(f"File created: {file_path}")
    
    # Delete directory with the file
    shutil.rmtree(temp_dir)
    print(f"Directory {temp_dir} and its contents have been deleted.")

# 5. Temp File Usage: Create a temporary file using tempfile.NamedTemporaryFile() and write to it.
def temp_file_usage():
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(b"Temporary file content")
        print(f"\nTemporary file created at: {temp_file.name}")
        # The file will not be deleted after closing due to delete=False

# 6. Copy Files with shutil: Copy a file from one path to another using shutil.copy().
def copy_file():
    source_path = Path("output.txt")
    destination_path = Path("output_copy.txt")
    
    shutil.copy(source_path, destination_path)
    print(f"\nFile copied from {source_path} to {destination_path}")

# 7. Absolute vs Relative Paths: Use pathlib.Path.resolve() to show full paths.
def absolute_vs_relative_paths():
    relative_path = Path("output.txt")
    absolute_path = relative_path.resolve()
    print(f"\nRelative path: {relative_path}")
    print(f"Absolute path: {absolute_path}")

# 8. Check File Existence: Use pathlib.Path.exists() and is_file() to test paths.
def check_file_existence():
    file_path = Path("output.txt")
    
    if file_path.exists() and file_path.is_file():
        print(f"\nFile exists: {file_path}")
    else:
        print(f"\nFile does not exist: {file_path}")

# --- Example Usage ---
if __name__ == "__main__":
    # Run the examples
    read_file_with_pathlib()
    list_python_files()
    write_to_file()
    create_and_delete_directory()
    temp_file_usage()
    copy_file()
    absolute_vs_relative_paths()
    check_file_existence()
