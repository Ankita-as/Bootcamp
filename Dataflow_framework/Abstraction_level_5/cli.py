import sys
from Abstraction_level_5.dag_engine import load_dag, run_dag

if __name__ == "__main__":
    input_file, output_file, config_file = sys.argv[1:4]

    with open(input_file) as f:
        input_lines = f.readlines()

    dag_config = load_dag(config_file)
    output = run_dag(dag_config, input_lines)

    with open(output_file, "w") as f:
        for tag, line in output:
            f.write(f"[{tag}] {line}")
