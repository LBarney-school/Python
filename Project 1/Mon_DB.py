# Imports, JSON for Data reading/writing, Dataclasses for dataclass
import json
from dataclasses import dataclass


@dataclass
# Dataclass for monsters
# Includes an ID, the name, level, and JSON datapack
class monData:
    id: int
    name: str
    level: int
    data: str

    """
    #JSON Dataloader builtin ideation.
    #Did not end up being needed. 
    def data(self):
        return json.loads(self.data)
    """

    # Initialization.
    def _init_(self, jsonData):
        self.id = jsonData["id"]
        self.name = jsonData["name"]
        self.level = jsonData["level"]
        self.data = jsonData


# File reader, also used by monWriter
def monReader(monFile):
    # Simple try/except error catching
    try:
        # Load file in read mode
        file = open(monFile, "r")
        jsonData = json.load(file)
        # Required JSON sub-header to keep Python happy and multi-dictionaries possible
        monsters = jsonData["monsters"]
        file.close()
        return monsters
    except:
        print("File not found")


# File writer
def monWriter(monFile, monLibrary):
    # Open listed file via monReader
    newMon = monReader(monFile)
    # Create new data objects via Dataclass and append to existing library
    if isinstance(newMon, list):
        for mon in newMon:
            TempMon = monData(mon["id"], mon["name"], mon["level"], mon)
            monLibrary.append(TempMon)
    elif isinstance(newMon, dict):
        TempMon = monData(mon["id"], mon["name"], mon["level"], mon)
        monLibrary.append(TempMon)
    else:
        print("Type not supported")
        return False

    # Set up new Dictionary for saving to main DB in same format
    # To lookup - methods to create backups before making saves to things.
    monDict = []
    for mon in monLibrary:
        monDict.append(mon.data)
    output = {"monsters": monDict}

    # Simple try/catch for error catching
    try:
        # Open main DB and dump JSON data to it with proper indets, then close file.
        file = open("Mon_DB.json", "w")
        json.dump(output, file, indent=4)
        file.close()
    except:
        print("File not found")

    userInput = input(
        "Please enter a monster ID, 'list' to see available monsters, or 'new' to add a new monster: "
    )
    inputParser(monLibrary, userInput)


# Simple lister for Dataclass library
def monList(monLibrary):
    # Header Printer
    print("List of available monsters")
    print(f"{'ID':<12}{'Name':<25}{'Level':<5}")
    print("-" * 45)
    # Print the ID/Name/Level of each monster in library
    for mon in monLibrary:
        print(f"{mon.id:<12}{mon.name:<25}{mon.level:<2}")
    # Call input parser
    print("-" * 45)
    userInput = input(
        "Please enter a monster ID, 'list' to see available monsters, or 'new' to add a new monster: "
    )
    inputParser(monLibrary, userInput)


# Main monster stat block show
def monShow(monStat):
    print("\n\n")
    print(f"{monStat.get("name")} \t\t\t\t {monStat.get("level")}")
    print("-" * 35)

    # First 'main' block'
    print(monStat.get("tags"))

    # Check for special 'vision' types and then add to perception if present
    # Skip if not there
    vision = monStat.get("vision", "N/A")
    if vision == "N/A":
        print("Peception:", monStat.get("peception"), ",", vision)
    else:
        print("Peception:", monStat.get("peception"))

    # Check for languages
    # Skip if not there
    language = monStat.get("language", "N/A")
    if language != "N/A":
        print("Language:", language)

    # Check for Skills
    # Skip if not there.
    # Outlier case, but still in
    skills = monStat.get("skills", "N/A")
    if skills != "N/A":
        print("Skills:", skills)

    # Main stats block
    print("Str:", monStat["str"], "\tDex:", monStat["dex"], "\tCon:", monStat["con"])
    print("Int:", monStat["int"], "\tWis:", monStat["wis"], "\tCha:", monStat["cha"])

    # Check for Items
    # Skip if not there.
    items = monStat.get("items", "N/A")
    if items != "N/A":
        print("Items:", items)
    print("-" * 35)

    # Defense Section
    # Set up for if monster has special defenses or not
    specialDef = monStat.get("specialDef", "N/A")
    if specialDef != "N/A":
        print(
            "AC:",
            monStat["ac"],
            "; Fort:",
            monStat["fort"],
            ", Ref:",
            monStat["ref"],
            ", Will:",
            monStat["will"],
            ", ",
            specialDef,
        )
    else:
        print(
            "AC:",
            monStat["ac"],
            "; Fort:",
            monStat["fort"],
            ", Ref:",
            monStat["ref"],
            ", Will:",
            monStat["will"],
        )

    """
    This bit is slighlty complicated as the HP line can have up to 4 different items.
    However, only 1 is guaranteed. So this sets up a list Appends the HP to it, and then
    based on if the .get functions return anything or not, appends them to the list and then
    joins them all.
    """
    immunities = monStat.get("immunities")
    weaknesses = monStat.get("weaknesses")
    resistances = monStat.get("resistances")
    hpLine = []
    hpLine.append(f"HP: {monStat["hp"]}")
    if immunities:
        hpLine.append(f", Immunities: {monStat["immunities"]}")
    if weaknesses:
        hpLine.append(f", Weaknesses: {monStat['weaknesses']}")
    if resistances:
        hpLine.append(f", Resistances: {monStat['resistances']}")
    print(" ".join(hpLine))

    print("-" * 35)

    # Offense Section
    print("Speed:", monStat["speeds"])
    abilities = monStat.get("abilities")
    if abilities:
        for ability_name, description in abilities.items():
            print(f"{ability_name}: {description}")

    spells = monStat.get("spells")
    if spells:
        print("Spellcasting")
        for key, value in spells.items():
            print(f"{key}: {value}")

    print("-" * 35)
    print("\n")
    userInput = input(
        "Please enter a monster ID, 'list' to see available monsters, or 'new' to add a new monster: "
    )
    inputParser(monLibrary, userInput)


# Parser for input
def inputParser(monLibrary, userInput):

    # Try catch to see if input is compatible with integer or not
    try:
        userInputInt = int(userInput)
        # If it can be converted to an integer, check to see if it's in IDs
        foundMonster = False
        for mon in monLibrary:
            if mon.id == userInputInt:
                # If it is, set found monsters to true
                # This never gets called again now, but might at a later date
                foundMonster = True
                # Call monster show function
                monShow(mon.data)
                return True
        if foundMonster == False:
            # Present an errror and recall the user input/parser
            # Woo! Recursion!
            print("No monster found with that ID.")
            userInput = input(
                "Please enter a monster ID, 'list' to see available monsters, or 'new' to add a new monster: "
            )
            inputParser(monLibrary, userInput)
            return True
        else:
            # If it gets here, I have no idea how, it means the Monster was found
            # , but it didn't call the showMon function. So something went real weird.
            print("Unknown error")
            return False
    except:
        # If the program gets here, it wasn't an integer, so we're looking at a string
        # Is this efficient? Probably not. However, it is neat.
        # Call the list again in case the user is lost
        if userInput.lower() == "list":
            monList(monLibrary)
            return True
        # Call the new monster function
        elif userInput.lower() == "new":
            print("Please enter the filename of the new monster.")
            print(
                "Monsters must be in a properly formatted JSON file in the same directory."
            )
            newFile = input("Filename: ")
            monWriter(newFile, monLibrary)
            return True
        # The user did something weird, give some direction
        else:
            print("Invalid input.")
            userInput = input(
                "Please enter a monster ID, 'list' to see available monsters, or 'new' to add a new monster: "
            )
            inputParser(monLibrary, userInput)
            return True


# Open Monster (Test monster)
monster = monReader("Mon_DB.json")
# Set up monster library list
monLibrary = []
for mon in monster:
    TempMon = monData(mon["id"], mon["name"], mon["level"], mon)
    monLibrary.append(TempMon)
# monShow(monLibrary, 1)

# List Monsters
monList(monLibrary)
