from species import Human, Dwarf, Halfling, Elf, Drow, HighElf, WoodElf


class Character:
    def __init__(self, character_inputs):
        self.name = character_inputs[0]
        self.clss = character_inputs[1]
        self.species = character_inputs[2]
        self.alignment = character_inputs[3]

        self.get_species_details()

        """ self.background = None
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
        self.backstory = None """

    def get_species_details(self):
        match self.species:
            case "human":
                species = Human()
                self.lineage = species.lineage
                self.size = species.size
                self.speed = species.speed
            case "dwarf":
                species = Dwarf()
                self.lineage = species.lineage
                self.size = species.size
                self.speed = species.speed
            case "halfling":
                species = Halfling()
                self.lineage = species.lineage
                self.size = species.size
                self.speed = species.speed
            case "elf":
                lineage = input(
                    "\t>> Which Elven lineage? (Drow, High Elf, Wood Elf) "
                ).lower()
                species = Elf(lineage)
                self.lineage = species.lineage
                self.size = species.size
                self.speed = species.speed
            case "drow":
                species = Drow()
                self.species = species.type
                self.lineage = species.lineage
                self.size = species.size
                self.speed = species.speed
            case "high elf":
                species = HighElf()
                self.species = species.type
                self.lineage = species.lineage
                self.size = species.size
                self.speed = species.speed
            case "wood elf":
                species = WoodElf()
                self.species = species.type
                self.lineage = species.lineage
                self.size = species.size
                self.speed = species.speed

    def generate(self):
        print(f"\nGenerating character")


"""     def __str__(self):
        character_summary = (
            "-" * 100 + "\n\n"
            f">> Character Name: {self.name}\n"
            f">> Class: {self.class_type}\n"
            f">> Species: {self.species.type}\n"
            f"\t>> Lineage: {self.species.lineage}\n"
            f"\t>> Size: {self.species.size}\n"
            f"\t>> Speed: {self.species.speed}\n"
            f">> Alignment: {self.alignment}"
        )
        return character_summary """
