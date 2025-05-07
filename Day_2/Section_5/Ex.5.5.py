# subprocess_concurrency_demo.py

import subprocess
import threading
from multiprocessing import Process
import concurrent.futures
import time

def compute():
    print("Computing in a separate process...")

def greet():
    print("Hello from thread!")

def increment(lock, counter_list):
    for _ in range(100000):
        with lock:
            counter_list[0] += 1

def square(n):
    return n * n

def main():
    print("\n--- 1. Run a Command ---")
    subprocess.run(["dir"], shell=True)  # Use 'ls -l' on Linux/Mac

    print("\n--- 2. Capture Output ---")
    result = subprocess.run("echo Hello, World!", capture_output=True, text=True, shell=True)
    print("Captured Output:", result.stdout.strip())

    print("\n--- 3. Check Exit Code ---")
    result = subprocess.run(["python", "--version"])
    print("Exit Code:", result.returncode)

    print("\n--- 4. Start a Thread ---")
    thread = threading.Thread(target=greet)
    thread.start()
    thread.join()

    print("\n--- 5. Start a Process ---")
    process = Process(target=compute)
    process.start()
    process.join()

    print("\n--- 6. Thread Locking ---")
    lock = threading.Lock()
    counter = [0]  # Use a list to allow mutation inside threads

    threads = [threading.Thread(target=increment, args=(lock, counter)) for _ in range(5)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    print("Final Counter:", counter[0])

    print("\n--- 7. Use concurrent.futures ---")
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(square, range(5))
        print("Squares:", list(results))

    print("\n--- 8. Kill a Subprocess ---")
    proc = subprocess.Popen(["ping", "-n", "10", "127.0.0.1"], stdout=subprocess.PIPE, shell=True)
    time.sleep(2)
    proc.terminate()
    print("Subprocess terminated.")

if __name__ == "__main__":
    main()
