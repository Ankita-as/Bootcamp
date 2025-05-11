 # Main and basics Commands
 Install typer
 pip install typer
 pip install pyyaml
pip install networkx
pip install matplotlib

Run the command 
python cli.py --config-path=config.yaml

# Dataflow Router System

This project implements a **dataflow router system** that processes lines of data based on defined tags. It dynamically loads processors from a configuration file, validates tag-to-processor mappings, handles circular dependencies to prevent infinite loops, and routes data through multiple tags and processors in a modular fashion.

## Features
- **Tag-based Processing:** Routes data through different processors based on tags (e.g., `start`, `error`, `warn`, `end`).
- **Infinite Loop Prevention:** Prevents processing loops by tracking visited tags.
- **Dynamic Configuration:** Load processors and tags from a configurable YAML file.
- **Modular Design:** Easily extendable with custom processors.

## Installation

### Prerequisites
To run this project, ensure you have the following installed:
- Python 3.x
- Required Python packages (see `requirements.txt`)

You can install the necessary Python packages using `pip`:

```bash
pip install -r requirements.txt
