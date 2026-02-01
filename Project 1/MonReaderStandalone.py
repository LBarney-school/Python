import json


def monReader(monFile):
    # Simple try/except error catching
    try:
        # Load file in read mode
        file = open(monFile, "r")
        print("File opened")
        jsonData = json.load(file)
        print(jsonData)
        # Required JSON sub-header to keep Python happy and multi-dictionaries possible
        monsters = jsonData["monsters"]
        file.close()
        return monsters
    except:
        print("File not found")


mon = monReader("DireWolf.json")
print(mon)
