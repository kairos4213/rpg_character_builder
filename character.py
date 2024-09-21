class Character:
    def __init__(self):
        self.name = ""
        self.class_type = ""
        self.race = ""
        self.background = ""
        self.alignment = ""
        self.attributes = {
            "Strength": 10,
            "Dexterity": 10,
            "Constitution": 10,
            "Intelligence": 10,
            "Wisdom": 10,
            "Charisma": 10,
        }
        self.traits = ""
        self.ideals = ""
        self.bonds = ""
        self.flaws = ""
        self.backstory = ""

    def get_inputs(self):
        print(
            "\nPlease enter what you have so far.\n(If you don't have anything, or don't know what to put, please type 'None')\n"
        )
        self.name = input(">> Character Name: ").lower()
        self.class_type = input(">> Class: ").lower()
        self.race = input(">> Race: ").lower()
        self.alignments = input(">> Alignments: ").lower()

    def generate(self):
        print(f"\nGenerating character")

    def __str__(self):
        character_summary = (
            "-------------------------------------------------------------\n\n"
            f">> Character Name: {self.name}\n"
            f">> Class: {self.class_type}\n"
            f">> Race: {self.race}\n"
            f">> Alignments: {self.alignment}"
        )
        return character_summary
