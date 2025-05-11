Run from Dataflow_framework folder
cd C:\Users\ankit\OneDrive\Desktop\Dataflow_framework
Run the module with:
python -m Abstraction_level_4.cli Abstraction_level_4/input.txt Abstraction_level_4/output.txt Abstraction_level_4/pipeline.yaml
 # Reuse str -> str via a wrapper
We’ll use this utility in base_processors.py:

Challenge Questions¶
1. How can you reuse existing str -> str processors in a streaming system?
=> Reuse str -> str processors by wrapping them with a decorator that converts str -> str into Iterator[str] -> Iterator[str].


2. How should a processor be initialized if it needs a parameter like min_length=5?
=> Initialize a processor with parameters by using a configuration dictionary (config) passed during dynamic loading (e.g., from pipeline.yaml).

3. If you split one line into many, how will downstream processors handle the multiple outputs?
=> Downstream processors handle multiple outputs naturally if all processors operate over Iterator[str], as each yields lines independently.

4. What’s the best way to test a stateful processor?
=> Best way to test a stateful processor is by feeding a controlled stream and asserting the stateful output (e.g., line numbering) line by line.

5. Can you identify which processors are stateless vs. stateful? give ans accurately in one line
=> Stateless vs. Stateful:
Stateless: to_snakecase, split_lines_on_delimiter, combine_lines
Stateful: LineCounterProcessor (maintains internal line count)