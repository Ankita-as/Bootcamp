import yaml
import importlib

def process_file(input_path, output_path, config_path):
    # Load the YAML file
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)

    # Ensure the 'pipeline' key exists in the config
    pipeline_steps = config.get('pipeline', [])

    # Check if the pipeline steps are loaded correctly
    print(f"Pipeline Steps: {pipeline_steps}")
    
    input_data = ''
    try:
        with open(input_path, 'r') as f:
            input_data = f.read()
    except FileNotFoundError:
        print(f"Error: Input file '{input_path}' not found.")

    print(f"Input data: {input_data}")

    for step in pipeline_steps:
        processor_type = step['type']
        print(f"Processing {processor_type}...")

        # Dynamically import the processor function
        try:
            # Split the processor type into module and function name
            module_name, function_name = processor_type.rsplit('.', 1)

            # Import the module and get the function
            module = importlib.import_module(module_name)
            processor_function = getattr(module, function_name)
            
            
            # Call the processor function
            result = processor_function(input_data)

            print(f"Processed data after {function_name}: {result}")

            # Update the input data for the next step
            input_data = result

        except Exception as e:
            print(f"Error processing {processor_type}: {e}")

    # Write the final output to the output file
    with open(output_path, 'w') as f:
        f.write(input_data)

    print(f"Output written to {output_path}")
