# File Processing System

A dynamic, observable, fault-tolerant, self-managing file processing system built with FastAPI.

## Setup Instructions

### 1. Clone the repository


```bash
git clone https://github.com/Ankita-as/Bootcamp.git
cd Dataflow_framework/Final_wrapup
```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
python main.py


Run Locally
.\run.bat run-single       # One file
.\run.bat run-watch        # Watch folder
.\run.bat api              # Start FastAPI 

#server
#Running with Docker
docker build -t file-processing-system .
Run Docker container
docker run -d -p 8000:8000 file-processing-system

#API Endpoints
GET /health: Check if the system is healthy.

GET /stats: Get processing statistics.

GET /files: List all processed files.

POST /files: Upload files to the system.
#Test the existing endpoints
#Visit these in your browser:
http://127.0.0.1:8000

http://127.0.0.1:8000/docs ← Swagger UI (should load if FastAPI is set up)

http://127.0.0.1:8000/health ← Health check

http://127.0.0.1:8000/stats ← File stats

http://127.0.0.1:8000/files ← File upload (POST endpoint)

### 🚀 API Endpoints (via FastAPI)
- `/health` — Health check
- `/stats` — View stats
- `/files` — Upload files (POST)

### 📤 How to Upload Files
- Drop files into `watch_dir/unprocessed/`
- Or use FastAPI `/files` endpoint
- Or use CLI: `run-single`


### ✅ 4. Final Checklist

- [x] `run.bat` supports all commands
- [x] Dual execution works
- [x] CLI, file drop, and browser supported
- [x] Code committed and clean
- [x] Clear instructions for deployment