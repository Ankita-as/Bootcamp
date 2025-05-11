import sys
import yaml
from importlib import import_module

def load_processor(processor_path: str):
    module_path, attr = processor_path.rsplit('.', 1)
    module = import_module(module_path)
    return getattr(module, attr)

def process_file(input_file: str, output_file: str, config_file: str):
    with open(config_file) as f:
        pipeline_config = yaml.safe_load(f)
    
    processors = []
    for step in pipeline_config['pipeline']:
        processor = load_processor(step['type'])
        if isinstance(processor, type):
            processors.append(processor())
        else:
            processors.append(processor)

    with open(input_file, 'r') as f:
        lines = iter(f.readlines())

    for processor in processors:
        lines = processor(lines)

    with open(output_file, 'w') as f:
        f.writelines(lines)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python -m Abstraction_level_4.cli <input_file> <output_file> <pipeline_config>")
        sys.exit(1)
    _, input_path, output_path, pipeline_path = sys.argv
    process_file(input_path, output_path, pipeline_path)