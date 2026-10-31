#  Logging is a way to track the flow of the program and the errors that occur.
#  or we can say Logging is a way to record what is happening inside your application while it runs.


# For example, imagine you're building your Expense Tracker or an AI backend. You want to know:
# - When a user adds an expense.
# - When an API request starts or finishes.
# - When a database connection fails.
# - When an AI model generates a response.
# - Why an application crashes.
# This is where Python's built-in logging module is useful. 

# Without logging, developers often use print() to debug applications
# This works for basic debugging, but it isn't ideal for production applications.

# Instead, use Python logging:

import logging

logging.basicConfig(level=logging.INFO)

def add_expense(amount):
    logging.info("Adding expense")
    logging.info("Expense amount: %s", amount)

    return amount

add_expense(500)


# What are logging levels?
# there are 5 logging levels:
# 1. DEBUG - 10%
# 2. INFO - 20%
# 3. WARNING - 30%
# 4. ERROR - 40%
# 5. CRITICAL - 50%

# DEBUG: Detailed information, typically only useful for developers.
# INFO: General information about the program's operation.
# WARNING: Something unexpected happened, but it's not a problem.
# ERROR: A problem that prevents the program from continuing.
# CRITICAL: A critical error that prevents the program from continuing.

# example:
import logging

logging.basicConfig(level=logging.DEBUG)

logging.debug("Application started in debug mode")
logging.info("User logged in")
logging.warning("API response is slower than expected")
logging.error("Database connection failed")
logging.critical("Application cannot continue")