import os
import subprocess
import time
import cat_service


def download_cat(folder_path: str):
    # TODO:  generate docstring.
    cat_count: int = int(input("Enter number of cats file you download:\n>>> "))
    print("Consuming cat images from the web...")
    time.sleep(3)
    for cat in range(1, cat_count + 1):
        print(f"Downloading cat {cat}")
        name = "LOLcat {}".format(cat)
        cat_service.get_cat(folder_path, name)

    print("Done!")


def get_or_create_folder() -> str:
    """Get or create folder for cat images in current directory

    Returns: str: full path to folder
    """
    base_folder = os.path.dirname(__file__)
    folder_name = input("Enter folder name:\n>>> ")
    full_path = os.path.join(base_folder, folder_name)

    # validate folder name creation
    if not os.path.exists(full_path) and not folder_name == "":
        print(f"Creating new folder at {full_path}")
        time.sleep(3)
        print("Folder created!")

        os.mkdir(full_path)
    else:
        print(f"Folder already exists at {full_path}")

    return full_path


def display_cats(folder_path: str):
    subprocess.call(["open", folder_path])


if __name__ == '__main__':
    print("-" * 35)
    print("\t\t\t\t\tCat Factory App")
    print("-" * 35)
    folder = get_or_create_folder()
    download_cat(folder)
    display_cats(folder)
