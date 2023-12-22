import time
from actors import Wizard, Creature


creatures: list = [
    Creature("Evil Wizard", 120),
    Creature("Dragon", 50),
    Creature("Wolf", 10),
    Creature("Toad", 1),
    Creature("Tiger", 75),
    Creature("Bat", 5)
]
print(creatures)

hero: Wizard = Wizard("Kingdom", 75)


def main():
    game_loop()


def game_loop():

    while True:
        cmd_input = input("Do you [a]ttack, [r]unaway, or [l]ook around?\n>>> ").lower().strip()

        if cmd_input == "a":
            print("attack")
        elif cmd_input == "r":
            print("runaway")
        elif cmd_input == "l":
            print("look around")
        else:
            print(f"Invalid command: {cmd_input}")
            validate_exit = input("Do you want to exit? [y/n]\n>>> ").lower().strip()
            if validate_exit == "y":
                print("Exiting...")
                time.sleep(2)
                break



if __name__ == "__main__":
    print("-" * 30)
    print("\t\t\tWizard Game App")
    print("-" * 30)

    main()