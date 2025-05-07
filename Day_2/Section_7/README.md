 cProfile: Run from terminal with:
# python -m cProfile Ex.7.1.py
# ------------------------------

# ------------------------------
# 5. line_profiler Setup
# Run with:
# kernprof -l -v Ex.7.1.py
# ------------------------------
# from line_profiler import LineProfiler

# @profile
# def profiled_function():
#     total = 0
#     for i in range(1000000):
#         total += i
#     return total

# if __name__ == '__main__':
#     profiled_function()

# ------------------------------
# 6. memory_profiler Setup
# Run with:
# python -m memory_profiler Ex.7.1.py
# ------------------------------
# from memory_profiler import profile

# @profile
# def memory_intensive_function():
#     a = [i * 2 for i in range(1000000)]
#     return sum(a)

# if __name__ == '__main__':
#     memory_intensive_function()
# Setting DEBUG=True
# $env:DEBUG = "True"
