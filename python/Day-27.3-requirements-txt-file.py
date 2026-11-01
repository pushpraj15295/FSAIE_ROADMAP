# requirements.txt file is a file that lists all the packages and their versions that are required for a project.

# Imagine you develop a project using these packages:
# - Django 4.0
# - fastapi 0.100.0
# - pandas 1.5.0

# Now you share your project with another developer.
# How will they know which packages to install?

# That's where requirements.txt comes in.
# It is a text file that lists your project's Python dependencies, often with their versions.




# Example:  requirements.txt file

# fastapi==0.120.0
# uvicorn==0.38.0
# requests==2.32.5
# numpy==2.3.4


# How to generate requirements.txt --------------------------------
# After installing your packages in your virtual environment, run:

# pip freeze > requirements.txt
# This will generate a requirements.txt file in your project folder.




# Suppose another developer clones your project.

# They can create and activate their own virtual environment, then run:
# python3 -m pip install -r requirements.txt