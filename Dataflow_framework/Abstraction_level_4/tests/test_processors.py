from Abstraction_level_4.processors.base_processors import to_snakecase_stream

def test_to_snakecase_stream():
    input_lines = ["Hello World\n", "Test Line\n"]
    result = list(to_snakecase_stream(input_lines))
    assert result == ["hello_world\n", "test_line\n"]
