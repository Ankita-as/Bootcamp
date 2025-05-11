import sys
import os
import importlib
from typing import Callable, Any

def import_from_path(path: str):
    mod_path, _, func_name = path.rpartition(".")
    
    # Dynamically add the absolute path to 'processors' to sys.path
    base_dir = os.path.dirname(os.path.abspath(__file__))  # This gets the path to Abstraction_level_5
    processors_path = os.path.join(base_dir, "processors")
    sys.path.insert(0, processors_path)

    try:
        # Import the module dynamically
        module = importlib.import_module(mod_path)
        print(f"Successfully imported {mod_path}")  # Debugging line
    except ModuleNotFoundError as e:
        print(f"Error importing module: {e}")
        raise
    finally:
        sys.path.pop(0)

    # Return the processor (class or function) from the module
    processor = getattr(module, func_name)
    print(f"Processor found: {func_name}")  # Debugging line
    return processor


def load_dag(config_file: str):
    import yaml
    with open(config_file) as f:
        # Load the DAG configuration from the YAML file and return it
        return yaml.safe_load(f)["dag"]

def run_dag(dag_config, input_lines):
    processors = {}
    results = []
    
    # Import processor classes dynamically
    for node, node_config in dag_config.items():
        processor_class = import_from_path(node_config["type"])  # Get the class/function
        processors[node] = processor_class  # Initialize the processor (if it's a class)

    # Start processing from the 'start' node
    current_nodes = ["start"]
    data = input_lines

    while current_nodes:
        next_nodes = []
        for node in current_nodes:
            processor = processors[node]
            
            # Ensure the processor has a `process` method (assuming it's a class)
            if not hasattr(processor, "process"):
                print(f"Error: Processor for {node} does not have a 'process' method")
                continue

            # Process the data through the current processor
            data = processor.process(data)  # Pass data through each processor
            if isinstance(data, list):
                results.extend(data)
            
            # Get the next nodes to process
            next_nodes.extend(dag_config[node].get("next", []))
        
        current_nodes = next_nodes

    return results