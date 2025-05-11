# Final Project Wrap-Up

## 1. Design Decisions

- **File Monitoring**: I chose to implement a folder watcher for processing new files automatically. This allows for a continuous processing mode.
- **FastAPI**: I decided to use FastAPI for building the API, as it is fast and simple to set up, and it has automatic OpenAPI documentation.

## 2. Tradeoffs

- **Simplifications**: I did not implement any form of authentication or complex validation of uploaded files to keep the focus on the core logic. Additionally, I kept the file processing logic simple.
- **Limitations**: The system currently handles a single file at a time and does not scale well for very large numbers of concurrent file uploads.

## 3. Scalability

- **Handling 100x Larger Input**: If the system needed to handle significantly more data, I would consider introducing an asynchronous task queue (like Celery) to handle file processing in the background.
- **Parallelization**: File processing could be parallelized by breaking the file into chunks, but care must be taken to avoid race conditions when writing outputs.

## 4. Extensibility & Security

- **Extensibility**: The current system can be extended by adding more processing logic, integrating more complex workflows, or even supporting more file formats.
- **Security**: To secure file uploads, I would implement proper authentication, validate file types, and ensure that the system runs in a secure environment (e.g., behind HTTPS, firewall rules).

---

### **3. Wrap-Up Scripts**

Since I am working on Windows and `make` commands don’t work, the best way forward is to use a `run.bat` script that simplifies my workflow.

#### **`run.bat` Script Template**

Create a `run.bat` file with the following content:

```bat
@echo off
REM Run in single file mode
if "%1"=="run-single" (
    python main.py --input %2
    exit /b
)

REM Run in watch mode
if "%1"=="run-watch" (
    python main.py --watch
    exit /b
)

REM Run the API
if "%1"=="api" (
    uvicorn app.main:app --reload
    exit /b
)

REM Clean the system (optional, for cleanup tasks)
if "%1"=="clean" (
    echo Cleaning up...
    REM You can add cleanup commands here
    exit /b
)

echo Invalid command. Use 'run-single', 'run-watch', or 'api'.
