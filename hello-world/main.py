def get_user_name() -> str:
    _input: str = input("what is your name? ")

    return _input

if __name__ == "__main__":
    print("-" * 25)
    print("\tHELLO APP")
    print("-" * 25)
    print("\n")

    user_name: str = get_user_name()
    print(f"Nice to meet you {user_name}")
