class Species:
    def __init__(self):
        self.creature_type = "humanoid"
        self.speed = 30
        self.lineage = None


"""     def __repr__(self):
        return f"Species: {self.type}, Creature_Type: {self.creature_type}, Size: {self.size}, Speed: {self.speed}, Lineage: {self.lineage}" """


class Human(Species):
    def __init__(self):
        super().__init__()
        self.type = "human"
        self.size = self.get_size()

    def get_size(self):
        print(">> How tall is your character?")
        height = float(
            input(
                "\tEnter a height between 2-7ft. Please enter numbers only.\n\t(Decimals are accepted): "
            )
        )

        if height >= 2 and height < 4:
            return "small"
        elif height >= 4 and height <= 7:
            return "medium"
        else:
            print("Invalid height. Defaulting to 'Medium' range (4-7ft)")
            return "medium"


class Dwarf(Species):
    def __init__(self):
        super().__init__()
        self.type = "dwarf"
        self.size = "medium"


class Halfling(Species):
    def __init__(self):
        super().__init__()
        self.type = "halfling"
        self.size = "small"


class Elf(Species):
    def __init__(self, lineage):
        super().__init__()
        self.type = "elf"
        self.size = "medium"
        self.lineage = lineage


class Drow(Elf):
    def __init__(self):
        super().__init__("drow")


class HighElf(Elf):
    def __init__(self):
        super().__init__("high elf")


class WoodElf(Elf):
    def __init__(self):
        super().__init__("wood elf")
