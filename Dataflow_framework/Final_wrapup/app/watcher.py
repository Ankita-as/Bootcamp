import os
import time
from app.processor import process_file

WATCH_DIR = "watch_dir/unprocessed"

def watch_folder():
    print(f"Watching {WATCH_DIR} for new files...")
    seen = set()

    while True:
        files = os.listdir(WATCH_DIR)
        for filename in files:
            filepath = os.path.join(WATCH_DIR, filename)
            if filepath not in seen:
                process_file(filepath)
                seen.add(filepath)
        time.sleep(2)
