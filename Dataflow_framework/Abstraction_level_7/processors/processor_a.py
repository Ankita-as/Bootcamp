from metrics import metrics, traces, errors, metrics_lock

def run(line):
    try:
        # Process the line (convert to uppercase in this case)
        processed_line = line.upper()

        # Update shared metrics (e.g., track number of processed lines)
        with metrics_lock:
            metrics['line_count'] = metrics.get('line_count', 0) + 1
            metrics['processed_lines'] = metrics.get('processed_lines', 0) + 1

        # Add trace entry (you could add more information if needed)
        with metrics_lock:
            traces.append(f"Processed line: {line}")

        return processed_line
    except Exception as e:
        # In case of error, log it in the errors list
        with metrics_lock:
            errors.append(f"Error processing line: {line} - {str(e)}")
        return line  # Return the original line in case of an error
