import random

def get_number_user() -> int:
    _input: int = int(input("Guess a number between 0 and 100:\n>> "))

    if _input >=0:
        return _input
    else:
        print("You must enter a number between 0 and 100.\n")
        return get_number_user()

if __name__ == "__main__":
    target_number: int = random.randint(0, 100)
    print(target_number)
    print("-" * 35)
    print("\tGUESS THE NUMBER APP")
    print("-" * 35)
    print()

