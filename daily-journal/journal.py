from typing import List
import os
import time


def load_journal() -> list:
    pass


def save_journal(name: str, list_of_entries: List[str]) -> None:
    """
    Save the journal in a file.
    :param name: name of the journal.
    :param list_of_entries: list of entries.
    :return: None
    """
    filename = get_full_path(name)
    print(f"Your journal will be saved in {filename}.")

    with open(filename, "w") as file:
        for entry in list_of_entries:
            file.write(entry + "\n")

    print("Saving...")
    time.sleep(1)
    print("Your journal has been saved.")


def get_full_path(name: str) -> str:
    """
    Get the full path of the journal file.
    :param name: name of the journal.
    :return: full path of the journal file in a string.
    """
    filename = os.path.abspath(os.path.join("./journals", "{}.jrl".format(name)))

    return filename


def add_entry(entry: str, entries: List[str]) -> None:
    """
    Add an entry to the journal.

    :param entry: text to be added to the journal.
    :param entries: list of entries.
    :return: None
    """
    if len(entry) == 0:
        print("Your entry is empty.")
    else:
        entries.append(entry)
        print("Your entry has been added.")
