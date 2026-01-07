# Directory Size Calculator

Hello! My name is Sai Sindhu Javvaji, and I created this project as a quick exercise using Python to simulate a file system.  
Navigating directories, listing their contents, and checking folder sizes—including nested folders—are all possible with this command-line application.

---

## How I Constructed It

To represent folders and files, I chose to use two classes: `Directory` and `File`.  
Because each folder keeps track of its parent, `cd ..` works as intended.

Recursively calculating a folder's size was the difficult part; I had to test it several times before it worked for nested directories.  
You can experiment with commands like `cd`, `ls`, and `size` because they mimic terminal behavior.

## Features

- Navigate directories with `cd <folder>` or `cd ..`  
- List contents with `ls`  
- Check total size with `size` (includes subfolders)  
- Exit program with `exit`  

---

## Project Structure
directory-size-calculator/
│
├── src/
│ ├── filesystem.py 
│ ├── commands.py 
│ └── main.py 
│
├── data/
│ └── seed_data.py # Sample folders/files
│
├── tests/
│ └── test_size.py # Unit test for size calculation
├── README.md
├── requirements.txt
└── .gitignore

---

## Sample Commands

```text
root> ls
root> cd docs
docs> ls
docs> size
docs> cd ..
root> size
root> exit

## How to Run

1. Verify that Python 3.9+ is installed.
2. Run the following from the project root:
   python -m src.main
3. Try out the commands listed above.

Testing
Tests should be run from the project root:
python -m pytest
This verifies that the recursive size computation performs as planned.