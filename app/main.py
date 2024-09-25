from .character import Character


class Main:
    def __init__(self):
        print("Welcome to RPG Character builder!")
        print("Let's get you a character so you can start rolling some dice!\n")

        print("Type 'q' to quit, or 'r' to restart, at anytime")
        resp = input("Do you have an idea in mind? (y / n): ").lower()

        if resp == "y" or resp == "yes":
            character_inputs = self.get_character_inputs()
            character = Character(character_inputs)
        elif resp == "n" or resp == "no":
            character.generate()
        else:
            print("Invalid response. Try again.\n")

    def get_character_inputs(self):
        print(
            "\nPlease enter what you have so far.\n(If you don't have anything, or don't know what to put, please type 'None')\n"
        )

        name = input(">> Character Name: ").lower()
        clss = input(">> Class: ").lower()
        species = input(">> Race: ").lower()
        alignment = input(">> Alignment: ").lower()

        return [name, clss, species, alignment]


if __name__ == "__main__":
    main = Main()
    main.start_app()
