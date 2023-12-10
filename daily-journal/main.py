from typing import Optional, List
from time import sleep


def list_entries(data) -> None:
    if len(data) == 0:
        print("Your journal is empty.")
    else:
        print("Your journal entries: ")
        for entry in data:
            print(entry)


def add_entry(data) -> None:
    data.append(input("Type your entry, <ENTER> to exit: \n>>> "))
    print("Entry added.")


def event_loop():
    cmd: Optional[str] = None
    list_of_journal_data: List[str] = list()

    while cmd != "X":
        print("What do you want to do with your Journal?")
        cmd = input("[L]ist entries, [A]dd an entry, E[x]it: \n>>> ").upper().strip()

        if cmd == "L":
            list_entries(list_of_journal_data)
        elif cmd == "A":
            add_entry(list_of_journal_data)
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
