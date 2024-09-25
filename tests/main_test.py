import pytest
from ..app.main import Main


@pytest.fixture
def main(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "y")
    main = Main()
    return main


def test_get_character_inputs(monkeypatch, main):
    expected_output = ["merik", "warlock", "human", "lawful evil"]

    inputs = iter(["Merik", "WarLock", "HUMAN", "lawful EVIL"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    result = main.get_character_inputs()

    assert expected_output == result
