# JSON stands for JavaScript Object Notation. Despite its name, 
# it is widely used with Python and many other languages, especially for APIs and structured data.

# JSON is a lightweight data interchange format that is easy for humans to read and write, 
# JSON supports objects, arrays, strings, numbers, booleans, and null. 
# Python's built-in json module converts between JSON data and Python objects

import json

# Example of JSON data
json_data = {
    "name": "Pushpraj",
    "age": 30,
    "skills": ["Python", "React", "JavaScript"],
    "is_learning_ai": True,
    "projects": [
        {
            "name": "Project 1",
            "description": "Description of Project 1",
            "technologies": ["Python", "React", "JavaScript"]
        },
        {
            "name": "Project 2",
            "description": "Description of Project 2",
            "technologies": ["Python", "React", "JavaScript"]
        }
    ]
}

# json.dumps() converts a Python object into a JSON string. indent=2 is for pretty printing.
# json_data is already a dict, so loads() cannot accept it.
json_string = json.dumps(json_data, indent=2)
print(json_string)

# json.loads() converts a JSON string back into a Python object.
python_object = json.loads(json_string)
print(python_object)
print(python_object["name"])



# Writing JSON to a file [it will create a new file if it doesn't exist]------------------------------------------------------------------
with open("data.json", "w") as file:
    json.dump(json_data, file, indent=2)
print("JSON data written to data.json")

# Reading JSON from a file [it will read the file if it exists]------------------------------------------------------------------   
with open("data.json", "r") as file:
    json_data = json.load(file)
print(json_data)

