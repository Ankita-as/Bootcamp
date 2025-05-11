import argparse
import threading
import time
from dashboard import run_dashboard
from observability import process_line  # Assuming this function exists
from processors import processor_a, processor_b  # Assuming these processors exist
from metrics import record_metrics, record_trace, record_error, metrics, traces, errors

def load_input():
    return ["line one", "line two", "warning here", "error line"]

def main():
    # Parse arguments for trace enabling
    parser = argparse.ArgumentParser()
    parser.add_argument('--trace', action='store_true', help="Enable tracing of line journey")
    args = parser.parse_args()
    enable_trace = args.trace

    # Start the FastAPI dashboard in a background thread
    threading.Thread(target=run_dashboard, daemon=True).start()

    # Load the input data
    input_lines = load_input()

    # Process each line
    for line in input_lines:
        trace_path = []

        # Run through processor A
        start = time.time()
        line, trace_path = process_line(line, "processor_a", processor_a.run, enable_trace, trace_path)
        duration = time.time() - start
        record_metrics("processor_a", duration)

        # Run through processor B
        start = time.time()
        line, trace_path = process_line(line, "processor_b", processor_b.run, enable_trace, trace_path)
        duration = time.time() - start
        record_metrics("processor_b", duration)

        # Record error if the line was dropped
        if line is None:
            record_error("processor_b", "Line was dropped due to processing error.")

        # Record trace path if tracing is enabled
        if enable_trace:
            record_trace(trace_path)

        print("Final output:", line)

    # Debug: Print collected data
    print("\nFinal Metrics:", dict(metrics))  # Convert defaultdict to dict for cleaner print
    print("Final Traces:", list(traces))
    print("Final Errors:", list(errors))

if __name__ == "__main__":
    main()
