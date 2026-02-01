"""A basic task manager that loads a JSON file and prints tasks. It handles file errors, but the code is messy and hard to maintain."""

# Changed all single-quotes to double-quotes for style purpose and enhanced cohesion.
# Added line breads where needed for additional readability.
# Added program comments for usability


# Function to show remaining tasks in properly formated JSON file
def showtasks(file):
    import json

    # Attempt to open File
    try:
        with open(file, "r") as f:
            tasks = json.load(f)
        # Display Remaining Tasks
        for t in tasks:
            if "title" in t:
                print(
                    "Task:",
                    t["title"],
                    "--Done" if t.get("done", False) else "--Pending",
                )
            else:
                # Show if Data not correctly formatted
                print("Bad data")
    # Error Handling
    except FileNotFoundError:
        print("No such file!")
    except json.JSONDecodeError:
        print("Corrupted JSON!")
    except Exception as e:
        print("Oops", e)


# Simple Implementation Example
showtasks("tasks.json")
