from text_piper import TextPiper


def test_default_pipeline():
    output = list(TextPiper(["rivers fließen", "HELLO  world!"]))
    assert output == [["rivers", "fliessen"], ["hello", "world"]]
