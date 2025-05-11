import os
import shutil
import time
import threading
from flask import Flask, jsonify, render_template

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
WATCH_DIR = os.path.join(BASE_DIR, "watch_dir")
UNPROCESSED_DIR = os.path.join(WATCH_DIR, "unprocessed")
UNDERPROCESS_DIR = os.path.join(WATCH_DIR, "underprocess")
PROCESSED_DIR = os.path.join(WATCH_DIR, "processed")

# Dashboard data
dashboard_data = {
    "currently_processing": None,
    "recent_files": []
}

# Recovery on startup
def recover_files():
    if not os.path.exists(UNDERPROCESS_DIR):
        return
    for filename in os.listdir(UNDERPROCESS_DIR):
        src = os.path.join(UNDERPROCESS_DIR, filename)
        dest = os.path.join(UNPROCESSED_DIR, filename)
        if os.path.isfile(src):
            shutil.move(src, dest)
            print(f"[RECOVERY] Moved back: {filename}")

# File processing simulation
def process_file(file_path):
    filename = os.path.basename(file_path)
    in_progress_path = os.path.join(UNDERPROCESS_DIR, filename)
    done_path = os.path.join(PROCESSED_DIR, filename)
    
    # Move to underprocess
    shutil.move(file_path, in_progress_path)
    dashboard_data["currently_processing"] = filename
    print(f"[PROCESSING] {filename}")

    # Simulated line-by-line processing
    with open(in_progress_path, 'r') as f:
        for line in f:
            print(f"  → {line.strip()}")
            time.sleep(0.2)  # Simulate delay

    # Move to processed
    shutil.move(in_progress_path, done_path)
    dashboard_data["recent_files"].insert(0, {"name": filename, "timestamp": time.ctime()})
    dashboard_data["recent_files"] = dashboard_data["recent_files"][:5]
    dashboard_data["currently_processing"] = None
    print(f"[DONE] {filename}")

# Monitor folder in background
def monitor_folder():
    print("[MONITOR] Watching for new files...")
    while True:
        try:
            files = os.listdir(UNPROCESSED_DIR)
            print(f"[MONITOR] Files in unprocessed: {files}")  # Debugging

            if not files:
                print("[MONITOR] No files in unprocessed folder.")
            
            for filename in files:
                file_path = os.path.join(UNPROCESSED_DIR, filename)
                if os.path.isfile(file_path):
                    # Check if the file is not already in progress
                    in_progress_path = os.path.join(UNDERPROCESS_DIR, filename)
                    if not os.path.exists(in_progress_path):
                        print(f"[MONITOR] Moving file: {filename}")  # Debugging
                        process_file(file_path)
        except Exception as e:
            print(f"[MONITOR] Error: {str(e)}")
        
        time.sleep(2)


# Flask Dashboard
app = Flask(__name__)

@app.route("/status")
def status():
    try:
        return jsonify({
            "unprocessed": len(os.listdir(UNPROCESSED_DIR)),
            "underprocess": len(os.listdir(UNDERPROCESS_DIR)),
            "processed": len(os.listdir(PROCESSED_DIR)),
            "currently_processing": dashboard_data["currently_processing"],
            "recent_files": dashboard_data["recent_files"]
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ✅ New route for live dashboard
@app.route("/")
def dashboard():
    return render_template("dashboard.html")

def run_dashboard():
    app.run(port=5000)

# Entry point
if __name__ == "__main__":
    # Ensure the directories exist
    os.makedirs(UNPROCESSED_DIR, exist_ok=True)
    os.makedirs(UNDERPROCESS_DIR, exist_ok=True)
    os.makedirs(PROCESSED_DIR, exist_ok=True)

    recover_files()

    # Start the Flask app in a separate thread
    threading.Thread(target=run_dashboard, daemon=True).start()

    # Run the folder monitoring in the main thread
    monitor_folder()
