# Expense Tracker Project

# Our application will:
# 1. Add an expense.
# 2. Log successful operations.
# 3. Warn if the amount is invalid.
# 4. Record errors if something goes wrong.


import logging

# Configure logging
logging.basicConfig(
    filename="expense_tracker.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)

logger = logging.getLogger(__name__)


def add_expense(amount, category):

    logger.info("Adding expense: category=%s", category)

    try:
        if not isinstance(amount, (int, float)) or isinstance(amount, bool):
            raise TypeError("Amount must be a number")

        if amount <= 0:
            raise ValueError("Amount must be greater than zero")

        logger.info("Expense added successfully")
        return {
            "amount": amount,
            "category": category
        }

    except TypeError:
        logger.exception("Invalid expense amount type")
        raise

    except ValueError:
        logger.exception("Invalid expense amount")
        raise


try:
    result = add_expense(500, "Food")
    print(result)

except (TypeError, ValueError) as error:
    print("Could not add expense:", error)
