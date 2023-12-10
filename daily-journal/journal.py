from typing import List


def load_journal() -> list:
    pass


def save_journal() -> None:
    pass


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
