from species import Human, Dwarf, Halfling, Elf, Drow, HighElf, WoodElf


class Character:
    def __init__(self):
        self.name = None
        self.class_type = None
        self.species = None
        self.background = None
        self.alignment = None
        self.attributes = {
            "Strength": 10,
            "Dexterity": 10,
            "Constitution": 10,
            "Intelligence": 10,
            "Wisdom": 10,
            "Charisma": 10,
        }
        self.traits = None
        self.ideals = None
        self.bonds = None
        self.flaws = None
        self.backstory = None

    def get_inputs(self):
        print(
            "\nPlease enter what you have so far.\n(If you don't have anything, or don't know what to put, please type 'None')\n"
        )
        self.name = input(">> Character Name: ").lower()
        self.class_type = input(">> Class: ").lower()
        self.species = self.get_species_details(input(">> Race: ").lower())
        self.alignment = input(">> Alignment: ").lower()

    def get_species_details(self, species_type):
        match species_type:
            case "human":
                return Human()
            case "dwarf":
                return Dwarf()
            case "halfling":
                return Halfling()
            case "elf":
                lineage = input(
                    "\t>> Which lineage? (Drow, High Elf, Wood Elf "
                ).lower()
                return Elf(lineage.title())
            case "drow":
                return Drow()
            case "high elf":
                return HighElf()
            case "wood elf":
                return WoodElf()

    def generate(self):
        print(f"\nGenerating character")

    def __str__(self):
        character_summary = (
            "-------------------------------------------------------------\n\n"
            f">> Character Name: {self.name}\n"
            f">> Class: {self.class_type}\n"
            f">> Species: {self.species.type}\n"
            f"\t>> Lineage: {self.species.lineage}\n"
            f"\t>> Size: {self.species.size}\n"
            f"\t>> Speed: {self.species.speed}\n"
            f">> Alignment: {self.alignment}"
        )
        return character_summary
