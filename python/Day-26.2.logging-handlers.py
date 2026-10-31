#  Logging handlers are used to send the logs to a specific destination.

# StreamHandler	 --> Sends logs to terminal or another stream
# FileHandler	 --> Saves logs in a file
# RotatingFileHandler	 --> Rotates files when they reach a size limit
# TimedRotatingFileHandler	 -->  Rotates files at a specific time interval

# Example: Save logs into a file

import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Application started")
logging.warning("Low disk space")
logging.error("Something went wrong")

# for checking the logs: check the app.log file in the same directory as the script.


# Example: Save logs into a file and rotate it when it reaches a size limit [new file will be created ]
# example.log.1, example.log.2, example.log.3, example.log.4, example.log.5 will be created and the oldest file will be deleted.

import logging
import logging.handlers

logging.basicConfig(
    handlers=[logging.handlers.RotatingFileHandler("app.log", maxBytes=10000, backupCount=5)],
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Application started")
logging.warning("Low disk space")
logging.error("Something went wrong")