# processor_b.py

from metrics import metrics, traces, errors, metrics_lock  # Import shared data structures

def run(line):
    try:
        # Print for debugging purposes
        print(f"Processing line: {line}")

        # Check if the line contains an error
        if "error" in line.lower():
            # Log error in the errors list
            with metrics_lock:
                errors.append(f"Error found in line: {line}")
            raise ValueError("Found error in line")

        # Process the line (convert to uppercase in this case)
        processed_line = line.upper()

        # Update shared metrics (e.g., track the number of processed lines)
        with metrics_lock:
            metrics['line_count'] = metrics.get('line_count', 0) + 1  # Increment line count
            metrics['processed_lines'] = metrics.get('processed_lines', 0) + 1  # Increment processed lines

        # Add trace entry for this line
        with metrics_lock:
            traces.append(f"Processed line: {line}")

        return processed_line  # Return the processed line if no errors

    except ValueError as e:
        # If there's a ValueError (error found in the line), log it in the errors list
        with metrics_lock:
            errors.append(f"Error processing line: {line} - {str(e)}")
        
        return None  # Return None or the original line if you prefer

