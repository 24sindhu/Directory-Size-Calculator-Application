# Directory Size Calculator

Hello! My name is Sai Sindhu Javvaji, and I created this project using Python to simulate a file system.
Navigating directories, listing their contents, and checking folder sizes—including nested folders—are all possible with this command-line application.

## How I Constructed It

The program uses the OOP with abstraction and polymorphism:

- Abstract base class: `FileSystemItem` defines `get_size()` and `get_name()`
- Polymorphism: `File` and `Directory` both implement these methods, so the commands just call `get_size()` without worrying about the type

- Tree structure: Each `Directory` knows of files and subdirectories, and knows its parent for `cd ..` The trickiest part was the recursive function get_size(), as I had to repeatedly test the nested folders until perfection.

## Features

- Navigate directories with `cd <folder>` or `cd ..`  
- List contents with `ls`  
- Check total size with `size` (includes subfolders)  
- Exit program with `exit`  

---

## Project Structure
```
directory-size-calculator/
│
├── src/
│ ├── filesystem.py # Core classes with abstraction/polymorphism
│ ├── commands.py  # CLI commands
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
```
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