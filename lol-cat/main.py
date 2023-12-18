import os
import time


def get_or_create_folder() -> str:
    base_folder = os.path.dirname(__file__)
    folder_name = input("Enter folder name:\n>>> ")
    full_path = os.path.join(base_folder, folder_name)

    # validate folder name creation
    if not os.path.exists(full_path) and not folder_name == "":
        print(f"Creating new folder at {full_path}")
        time.sleep(1)
        print("Folder created!")

        os.mkdir(full_path)
    else:
        print(f"Folder already exists at {full_path}")

    return full_path


if __name__ == '__main__':
    print("-" * 35)
    print("\t\t\t\t\tCat Factory App")
    print("-" * 35)
    folder = get_or_create_folder()
