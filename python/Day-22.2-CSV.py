# CSV (Comma Separated Values) is a simple file format that stores tabular data (rows and columns) in plain text.
# It is widely used for data exchange and storage.
# It is a text file where each line contains a comma-separated list of values.
# It is a simple file format that stores tabular data (rows and columns) in plain text.

# CSV stands for Comma-Separated Values. It is useful for storing tabular data, 
# such as expenses, employee records, or product lists. Python provides 
# a built-in csv module for reading and writing CSV files

# date,category,amount
# 2026-10-25,Food,250
# 2026-10-25,Transport,100
# 2026-10-26,Shopping,500



import os
import csv  

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "data.csv")
new_file_path = os.path.join(script_dir, "new_data.csv")

# write mode ------------------------------------------------------------------
with open(file_path, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["date", "category", "amount"])
    writer.writerow(["2026-10-25", "Food", 250])
    writer.writerow(["2026-10-25", "Transport", 100])
    writer.writerow(["2026-10-26", "Shopping", 500])

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
    writer.writerow(["2026-10-27", "Food", 300])

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
    writer.writerow(["date", "category", "amount"])
    writer.writerow(["2026-10-25", "Food", 250])
    writer.writerow(["2026-10-25", "Transport", 100])
    writer.writerow(["2026-10-26", "Shopping", 500])

print("CSV file created successfully!") 
