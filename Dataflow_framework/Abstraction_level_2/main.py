from .pipeline import build_pipeline
       
def process_file(input_file: str, output_file: str, mode: str):
    """Process the input file and save the result to the output file."""
    
    # Build the processing pipeline based on the mode.
    pipeline = build_pipeline(mode)
    print(f"Using pipeline: {pipeline}")  # Debug print
    
    # Open and read the input file.
    with open(input_file, 'r') as infile:
        lines = infile.readlines()
    print(f"Input lines: {lines}")  # Debug print

    # Process lines using the pipeline functions.
    processed_lines = []
    for line in lines:
        for processor in pipeline:
            line = processor(line.strip())  # Apply the processor functions
        processed_lines.append(line + '\n')  # Ensure each processed line has a newline.

    # Write the processed lines to the output file.
    with open(output_file, 'w') as outfile:
        outfile.writelines(processed_lines)
    print(f"Processed output written to {output_file}")  # Debug print

