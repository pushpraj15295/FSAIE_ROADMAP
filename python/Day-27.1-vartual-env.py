# Virtual Environment [.venv folder]

# A virtual environment is an isolated Python environment for a particular project.

# Imagine you have two projects:
# - Project A requires Django 4.
# - Project B requires Django 5.
# If you install packages globally, different projects can conflict with each other.

# A virtual environment solves this problem by keeping each project's installed packages separate.


# How to create a virtual environment ----------------------------
# Open your Mac terminal and navigate to your project folder.

# step 1: Open your Mac terminal and navigate to your project folder.

# step 2: python -m venv .venv
# This will create a .venv folder in your project folder.

# step 3: source .venv/bin/activate
# After activation, your terminal should look something like: 
# (.venv) user@machine ~/projects $

# step 4: pip install django    
# This will install Django in your virtual environment.

# step 5: python manage.py runserver
# This will start the Django development server.



# Deactivate the environment -------------------------------------
# After activating the environment, you can deactivate it by running the following command:
# Open your Mac terminal and navigate to your project folder.

# step 1: deactivate
# This will deactivate the virtual environment.

