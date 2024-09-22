class Species:
    def __init__(self):
        self.creature_type = "Humanoid"
        self.speed = 30
        self.lineage = None

    def __repr__(self):
        return f"Species: {self._type}, Creature Type: {self._creature_type}, Size: {self._size}, Speed: {self._speed}, Lineage: {self._lineage}"


class Human(Species):
    def __init__(self):
        super().__init__()
        self.type = "Human"
        self.size = self.get_size()

    def get_size(self):
        print(">> How tall is your character?")
        height = float(
            input(
                "\tEnter a height between 2-7ft. Please enter numbers only.\n\t(Decimals are accepted): "
            )
        )

        if height >= 2 and height < 4:
            return "Small"
        elif height >= 4 and height <= 7:
            return "Medium"
        else:
            print("Invalid height. Defaulting to 'Medium' range (4-7ft)")
            return "Medium"


class Dwarf(Species):
    def __init__(self):
        super().__init__()
        self.type = "Dwarf"
        self.size = "Medium"


class Halfling(Species):
    def __init__(self):
        super().__init__()
        self.type = "Halfling"
        self.size = "Small"


class Elf(Species):
    def __init__(self, lineage):
        super().__init__()
        self.type = "Elf"
        self.size = "Medium"
        self.lineage = lineage


class Drow(Elf):
    def __init__(self):
        super().__init__()
        self.lineage = "Drow"


class HighElf(Elf):
    def __init__(self):
        super().__init__()
        self.lineage = "High Elf"


class WoodElf(Elf):
    def __init__(self):
        super().__init__()
        self.lineage = "Wood Elf"
