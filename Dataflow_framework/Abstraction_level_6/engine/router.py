import importlib
import yaml
from typing import Iterator, Tuple, Dict, Callable
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt
from processors.filters.only_error import Processor as OnlyErrorProcessor
from processors.filters.only_warn import Processor as OnlyWarnProcessor
from processors.formatters.snakecase import Processor as SnakeCaseProcessor
from processors.output.terminal import Processor as TerminalProcessor

class Router:
    def __init__(self, config_path: str):
        self.config_path = config_path
        self.tag_to_processor = {}  # Initialize the tag-to-processor mapping

    def _load_config(self):
        """
        Load and parse the configuration file to set up processors.
        """
        with open(self.config_path, 'r') as f:
            config = yaml.safe_load(f)

        for node in config.get("nodes", []):
            tag = node["tag"]
            module_path = node["type"]
            module = importlib.import_module(module_path)  # Dynamically import module
            processor = module.Processor()  # Create Processor instance
            self.tag_to_processor[tag] = processor
            
    def run(self, initial_lines: Iterator[str]):
        queue = deque()
        visited_tags = set()  # This set will track visited tags

        # Start with lines tagged as 'start'
        for line in initial_lines:
            queue.append(('start', line))

        while queue:
            tag, line = queue.popleft()

            # If the tag is 'end', skip processing
            if tag == 'end':
                continue

            # Guard against infinite loops: Skip if the tag has been visited already
            if tag in visited_tags:
                print(f"Skipping tag '{tag}' to prevent infinite loop.")  # Optional debug message
                continue

            # Add this tag to visited_tags to prevent re-processing
            visited_tags.add(tag)

            processor = self.tag_to_processor.get(tag)
            if not processor:
                raise ValueError(f"No processor registered for tag '{tag}'")

            # Process the line using the corresponding processor
            for next_tag, next_line in processor.process(iter([line])):
                # Only append the next tag/line to the queue if it's valid
                queue.append((next_tag, next_line))

        print("Processing completed.")
