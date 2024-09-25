import pytest
from ..app.character import Character


def test_get_small_human_species_details(monkeypatch):
    expected_lineage, expected_size, expected_speed = None, "small", 30

    monkeypatch.setattr("builtins.input", lambda _: "3")
    character = Character(["merik", "warlock", "human", "lawful evil"])

    assert (
        character.lineage,
        character.size,
        character.speed,
    ) == (
        expected_lineage,
        expected_size,
        expected_speed,
    )


def test_get_medium_human_species_details(monkeypatch):
    expected_lineage, expected_size, expected_speed = None, "medium", 30

    monkeypatch.setattr("builtins.input", lambda _: "6.5")
    character = Character(["merik", "warlock", "human", "lawful evil"])

    assert (
        character.lineage,
        character.size,
        character.speed,
    ) == (
        expected_lineage,
        expected_size,
        expected_speed,
    )


def test_get_dwarf_species_details():
    expected_lineage, expected_size, expected_speed = None, "medium", 30
    character = Character(["merik", "warlock", "dwarf", "lawful evil"])

    assert (
        character.lineage,
        character.size,
        character.speed,
    ) == (
        expected_lineage,
        expected_size,
        expected_speed,
    )


def test_get_halfing_species_details():
    expected_lineage, expected_size, expected_speed = None, "small", 30
    character = Character(["merik", "warlock", "halfling", "lawful evil"])

    assert (
        character.lineage,
        character.size,
        character.speed,
    ) == (
        expected_lineage,
        expected_size,
        expected_speed,
    )


@pytest.mark.parametrize(
    "lineage_input, expected_lineage",
    [("drow", "drow"), ("high ELF", "high elf"), ("WOOD ELF", "wood elf")],
)
def test_get_elf_species_details(monkeypatch, lineage_input, expected_lineage):
    expected_size, expected_speed = "medium", 30

    monkeypatch.setattr("builtins.input", lambda _: lineage_input)
    character = Character(["merik", "warlock", "elf", "lawful evil"])

    assert (
        character.lineage,
        character.size,
        character.speed,
    ) == (
        expected_lineage,
        expected_size,
        expected_speed,
    )


def test_get_drow_species_details():
    expected_species, expected_lineage, expected_size, expected_speed = (
        "elf",
        "drow",
        "medium",
        30,
    )
    character = Character(["merik", "warlock", "drow", "lawful evil"])

    assert (
        character.species,
        character.lineage,
        character.size,
        character.speed,
    ) == (
        expected_species,
        expected_lineage,
        expected_size,
        expected_speed,
    )


def test_get_high_elf_species_details():
    expected_species, expected_lineage, expected_size, expected_speed = (
        "elf",
        "high elf",
        "medium",
        30,
    )
    character = Character(["merik", "warlock", "high elf", "lawful evil"])

    assert (
        character.species,
        character.lineage,
        character.size,
        character.speed,
    ) == (
        expected_species,
        expected_lineage,
        expected_size,
        expected_speed,
    )

def test_get_wood_elf_species_details():
    expected_species, expected_lineage, expected_size, expected_speed = (
        "elf",
        "wood elf",
        "medium",
        30,
    )
    character = Character(["merik", "warlock", "wood elf", "lawful evil"])

    assert (
        character.species,
        character.lineage,
        character.size,
        character.speed,
    ) == (
        expected_species,
        expected_lineage,
        expected_size,
        expected_speed,
    )
