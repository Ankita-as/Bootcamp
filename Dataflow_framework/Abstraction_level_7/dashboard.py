import uvicorn
#from . import app  # Import the FastAPI app
from fastapi import FastAPI
from metrics import metrics, traces, errors

app = FastAPI()

# Endpoint to fetch the metrics
@app.get("/stats")
async def get_stats():
    #return dict(metrics)
    return {"message": "Stats endpoint"}

# Endpoint to fetch the traces
@app.get("/trace")
def get_trace():
    return list(traces)

# Endpoint to fetch the errors
@app.get("/errors")
def get_errors():
    return list(errors)

@app.get("/metrics")
async def get_metrics():
    return dict(metrics)

# Function to run the FastAPI app in the background


def run_dashboard():
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
