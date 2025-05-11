# observability.py
from metrics import record_metrics, record_trace, record_error
import time

def process_line(line, processor_name, processor_func, enable_trace, trace_path):
    start = time.time()
    try:
        # Call the processor function to process the line
        result = processor_func(line)
        duration = time.time() - start

        # Record the metrics
        record_metrics(processor_name, duration)

        if enable_trace:
            new_trace = (trace_path or []) + [processor_name]
            record_trace(new_trace)

        return result, new_trace
    except Exception as e:
        # Record the error if something goes wrong
        record_error(processor_name, str(e))
        return processed_line, trace_path# Return None to indicate error in processing
