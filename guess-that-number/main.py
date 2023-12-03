import random


def validate_input_to_target(target: int, _input: int, counter: int) -> None:
    if _input == target:
        print(
            f"You have given, you have chosen the correct number.\nTarget: {target}\nInput: {_input}"
        )
    else:
        if counter == 3:
            print("at least you tried")
        else:
            print(f"This is your attempt {counter}. You didn't hit it, try again.\n")


def get_number_user() -> int:
    _input: int = int(input("Guess a number between 0 and 100:\n>> "))

    if _input >= 0 and _input <= 100:
        return _input
    else:
        print("You must enter a number between 0 and 100.\n")
        return get_number_user()


if __name__ == "__main__":
    target_number: int = random.randint(0, 100)
    counter: int = 0

    print(target_number)
    print("-" * 35)
    print("\tGUESS THE NUMBER APP")
    print("-" * 35)
    print()

    while counter < 3:
        user_numer: int = get_number_user()
        counter += 1

        if user_numer > target_number:
            print("The number entered is greater than the target")
            validate_input_to_target(target_number, user_numer, counter)

        elif user_numer < target_number:
            print("The number entered is less than the target")
            validate_input_to_target(target_number, user_numer, counter)
        else:
            validate_input_to_target(target_number, user_numer, counter)
            break
