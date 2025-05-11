class Processor:
    def process(self, lines):
        # Sample implementation that would classify lines
        for line in lines:
            if line == 'error':
                yield 'error', line
            elif line == 'warn':
                yield 'warn', line
            else:
                yield 'general', line
