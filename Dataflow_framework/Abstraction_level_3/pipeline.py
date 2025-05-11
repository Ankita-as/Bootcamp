import yaml
import importlib
from typing import Callable, List

ProcessorFn = Callable[[str], str]

def load_pipeline_from_config(config_path: str) -> List[ProcessorFn]:
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)

    processors = []
    for step in config['pipeline']:
        import_path = step['type']
        module_path, fn_name = import_path.rsplit('.', 1)

        try:
            module = importlib.import_module(module_path)
            fn = getattr(module, fn_name)
            processors.append(fn)
        except (ModuleNotFoundError, AttributeError) as e:
            raise ImportError(f"Failed to import '{import_path}': {e}")

    return processors
