from collections import defaultdict, deque
from threading import Lock

# Shared data structures
metrics = defaultdict(lambda: {"count": 0, "time": 0.0, "errors": 0})
traces = deque(maxlen=1000)
errors = deque(maxlen=100)

# Lock to ensure thread-safe access
metrics_lock = Lock()

# Function to record metrics
def record_metrics(processor_name, duration):
    with metrics_lock:
        metrics[processor_name]["count"] += 1
        metrics[processor_name]["time"] += duration

# Function to record errors
def record_error(processor_name, message):
    with metrics_lock:
        metrics[processor_name]["errors"] += 1
        errors.append({"processor": processor_name, "message": message})

# Function to record traces
def record_trace(trace):
    with metrics_lock:
        traces.append(trace)
