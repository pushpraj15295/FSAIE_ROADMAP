# File handling means working with files on your computer using Python.----------------------

import os

# There are four main modes to open a file:

# read (r) - read the file (the file must already exist)
# write (w) - write to the file (creates the file if it does not exist)
# append (a) - append to the file (creates the file if it does not exist)
# create (x) - create a new file (fails if the file already exists)

# Keep the practice file next to this script, no matter which folder you run from.
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "file.txt")

# write mode ------------------------------------------------------------------
# Write first. Read mode cannot open a file that does not exist yet.
with open(file_path, "w") as file:
    file.write("I am learning Python file handling.\n")

print("File written successfully!")

# read mode ------------------------------------------------------------------
with open(file_path, "r") as file:
    content = file.read()
    print(content)

# append mode ------------------------------------------------------------------
with open(file_path, "a") as file:
    file.write("This line was appended.\n")

print("File appended successfully!")

with open(file_path, "r") as file:
    print(file.read())

# create mode ------------------------------------------------------------------
# "x" only works when the file is new, so remove a leftover from a previous run.
if os.path.exists(file_path):
    os.remove(file_path)

with open(file_path, "x") as file:
    file.write("I am learning Python file handling.\n")

print("File created successfully!")
