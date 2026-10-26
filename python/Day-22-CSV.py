# CSV (Comma Separated Values) is a simple file format that stores tabular data (rows and columns) in plain text.
# It is widely used for data exchange and storage.
# It is a text file where each line contains a comma-separated list of values.
# It is a simple file format that stores tabular data (rows and columns) in plain text.

# Consider this code:


import os
import csv  

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "data.csv")
new_file_path = os.path.join(script_dir, "new_data.csv")

# write mode ------------------------------------------------------------------
with open(file_path, "w") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["John", 25, "New York"])
    writer.writerow(["Jane", 30, "Los Angeles"])

print("CSV file created successfully!")

# read mode ------------------------------------------------------------------
with open(file_path, "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

print("CSV file read successfully!")

# append mode ------------------------------------------------------------------
with open(file_path, "a") as file:
    writer = csv.writer(file)
    writer.writerow(["Mike", 35, "Chicago"])

print("CSV file appended successfully!")

# read mode ------------------------------------------------------------------
with open(file_path, "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)  

print("CSV file read successfully!")

# create mode ------------------------------------------------------------------
# "x" only works when the file is new. Write mode above already created data.csv,
# so this uses a different file and removes a leftover from a previous run.
if os.path.exists(new_file_path):
    os.remove(new_file_path)

with open(new_file_path, "x") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["John", 25, "New York"])
    writer.writerow(["Jane", 30, "Los Angeles"])

print("CSV file created successfully!") 
