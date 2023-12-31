# Junior/Trainee Python Developer Project

This repository contains various projects designed to help Junior or Trainee developers strengthen their Python skills, covering fundamentals to advanced concepts such as File I/O, classes, consuming external APIs, web scraping, and implementing Pythonic code. All these projects were inspired by the course [Python Jumpstart by Building 10 Apps](https://training.talkpython.fm/courses/details/python-language-jumpstart-building-10-apps).

## Repository Structure

- **hello-world:**
  - Folder covering basic Python concepts, such as variables, data types, functions and get data entered by user.

- **birthday-app**
  - Use of docstring and use of date management using the date library.

- **guess-that-number**
  - Use of control structure and use of native python libraries such as *random*.

- **daily-journal**
  - Import functions from other files.
  - Using File I/O correctly (automatic closing).

- **weather-app**
  - Use of external libraries such as *requests* and *beautifulsoup4*.
  - Use of the *namedtuple* function.
 
- **LOL Cat**
  - Download content from an external API.
  - Interact with the operating system file handler from Python.
  - 

## Topics Learned
1. Enumerate: 
    - It is a built-in function that allows you to iterate over a sequence (such as a list, tuple, or string) and obtain both the element and its index on each iteration. This eliminates the need to maintain a separate accountant.

2. Import features from other files correctly:
  - Use the word *import file_name* and access the functions of that file using the dot notation. This facilitates understanding and explicitness when reading and understanding code.

3. namedtuple:
  - Namedtuples facilitate access to the values of a tuple which makes the code more readable, since we access the values by their tag instead of being able to access the values by their location within the data structure.

4. ```python __file__ ```:
  - The __file__ variable contains the absolut path to the file that is being executed. This is useful when you want to access files that are in the same directory as the file that is being executed.

5. subprocess library:
  - The subprocess library allows you to run commands on the operating system. This is useful when you want to run a command that is not native to Python, such as opening a file in the default text editor.
  - The ```python subprocess.run() ``` function allows you to run a command and wait for it to finish before continuing with the execution of the program.

## Requirements

- Python 3.9
- Additional dependencies are detailed in the `requirements.txt` files in each specific folder.

## Usage Instructions

1. Clone this repository: `git clone https://github.com/your-username/your-repository.git`
2. Navigate to the project folder you are interested in.
3. Follow the specific instructions for each project within their respective folders.

## Contributions

Feel free to contribute to this repository through pull requests. If you find errors, have suggestions, or new ideas, we are open to collaborations!

## Acknowledgments

These projects were inspired by the [Python Jumpstart by Building 10 Apps](https://training.talkpython.fm/courses/details/python-language-jumpstart-building-10-apps) course.
