class Main:
    print("Welcome to RPG Character builder!")
    print("Let's get you a character so you can start rolling some dice!\n")
    idea = input("Do you have an idea in mind? (y / n): ").lower()

    if idea == 'y' or idea == 'yes':
        print("\nPlease enter what you have so far.\n(If you don't have anything, or don't know what to put, please type 'None')\n")
        name = input(">> Character Name: ").lower()
        class_type = input(">> Class: ").lower()
        race = input(">> Race: ").lower()
        alignments = input(">> Alignments: ").lower()


if __name__ == "__main__":
    main = Main()