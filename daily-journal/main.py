from typing import Optional, List
from time import sleep


def list_entries():
    pass


def add_entry():
    pass


def event_loop():
    cmd: Optional[str] = None
    list_of_journal_data: List[str] = list()

    while cmd != "X":
        print("What do you want to do with your Journal?")
        cmd = input("[L]ist entries, [A]dd an entry, E[x]it: \n>>> ").upper().strip()

        if cmd == "L":
            print("Listing...")
        elif cmd == "A":
            print("Adding...")
        elif cmd == "X":
            print("Exiting...")
            sleep(2)
        else:
            print("Invalid command. Try again.\n")


if __name__ == "__main__":
    print("-" * 30)
    print("\t\t\t\tDaily Journal")
    print("-" * 30)
    print()
    event_loop()
