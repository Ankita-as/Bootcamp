# processors/filters/only_warm.py
class Processor:
    def process(self, lines):
        for line in lines:
            if "warn" in line:
                yield 'warn', line
