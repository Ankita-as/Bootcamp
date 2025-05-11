from fastapi import FastAPI
import os

app = FastAPI()
WATCH_DIR = "watch_dir/unprocessed"

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/stats")
def stats():
    return {"file_count": len(os.listdir(WATCH_DIR))}

@app.get("/files")
def list_files():
    return {"files": os.listdir(WATCH_DIR)}
