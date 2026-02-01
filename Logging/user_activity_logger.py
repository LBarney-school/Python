"""
Create a Python program named user_activity_logger.py that does the following:

Configure logging

Logs must be written to a file named activity.log.
Log level should be INFO.
Log messages must include:
Timestamp
Log level
Message

(Use logging.basicConfig().)

Ask the user for two inputs

    Their name
    Their age

Immediately log the following:

INFO: User started the program
INFO: Name entered
INFO: Age entered (if valid)

Validate the age input

If the user enters something not numeric, log:
ERROR: Invalid age input
Then stop the program (no crash)
If the age is negative, log:
WARNING: Age value is negative

Display a final message

Print:


Hello, <name>! Your age has been recorded.


And log:

INFO: Program finished successfully

📄 Expected Output Example (console)


Enter your name: Anna
Enter your age: -5
Hello, Anna! Your age has been recorded.

📄 Expected Log File Example (activity.log)


2025-01-20 14:22:11,045 - INFO - Program started
2025-01-20 14:22:15,112 - INFO - Name entered: Anna
2025-01-20 14:22:20,122 - WARNING - Negative age entered: -5
2025-01-20 14:22:25,010 - INFO - Program finished successfully
"""

import logging

# Log Import

# Logger start and basic settings
logger = logging.getLogger()
logging.basicConfig(
    filename="activity.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
# First Log
logger.info("User started the program")

# Name Input and Log
name = input("Enter your name: ")
logger.info("User entered name: '{}'".format(name))

# Age Input and Validation
age = input("Enter your age: ")
try:
    age = int(age)
    if age < 0:
        logger.error("WARNING: Age value is negative: {}".format(age))
    else:
        logging.info("User entered age: '{}'".format(age))
except ValueError:
    # Error out and Quit
    logging.error("Invalid age input")
    quit()

# Program End
print(f"Hello {name}! Your age has been recorded!")
logger.info("Program finished successfully")
