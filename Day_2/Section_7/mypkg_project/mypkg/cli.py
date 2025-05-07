# mypkg/cli.py

import json
import os

def load_config():
    config_path = os.path.join(os.path.dirname(__file__), '../data/config.json')
    with open(config_path, 'r') as f:
        config = json.load(f)
    return config

def main():
    config = load_config()
    print("Config loaded:", config)

if __name__ == "__main__":
    main()

def hello(name):
    print(f"Hello, {name}")
