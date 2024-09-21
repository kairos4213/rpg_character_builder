from character import Character


class Main:
    character = Character()
    print("Welcome to RPG Character builder!")
    print("Let's get you a character so you can start rolling some dice!\n")
    idea = input("Do you have an idea in mind? (y / n): ").lower()

    if idea == "y" or idea == "yes":
        character.get_inputs()
    else:
        character.generate()

    print(f"\n{character}")


if __name__ == "__main__":
    main = Main()
