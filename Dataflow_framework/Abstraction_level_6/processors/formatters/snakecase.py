class Processor:
    def process(self, lines):
        for line in lines:
            # Convert to snake_case (just an example)
            yield 'general', line.lower().replace(" ", "_")
