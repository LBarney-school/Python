"""
--Imports Section--
"""

import os

# Dataclass import for Monster/Table Dataclasses
from dataclasses import dataclass

# Type Imports to improve Dataclasses
from typing import List, Optional

# Import for GUI
import customtkinter as ctk

# PostgreSQL Database Import
import supabase

# Import to allow for using .env file
from dotenv import load_dotenv

"""
--Dataclass section--
All data contained in dataclasses mentioned in comments is string-type unless otherwise 
mentioned.
"""


# Dataclass to keep Monster's Abilities
# Contains Ability Name, Description, and Type
@dataclass
class Ability:
    name: str
    description: str
    type: str


# Dataclass to keep Spell Lists
# Sub-class of Spellcasting
# Contains Level and Spell names
@dataclass
class SpellList:
    level: str
    spells: str


# Dataclass to keep Monster's Spellcasting
# Optional Dataclass
# Contains Spell Type, DC(int), Attack Bonus(int), and SpellList(dataclass)
@dataclass
class Spellcasting:
    spell_type: str
    dc: Optional[int]
    attack_bonus: Optional[int]
    spells: List[SpellList]


# Dataclass for skills
# Contains Skill name and bonus/penalty
@dataclass
class Skill:
    name: str
    bonus: int


# Main Monster Dataclass
# Has Ability, Spellcasting, Skills
# Contains remaining data on monsters
@dataclass
class Monster:
    id: int
    name: str
    level: int
    tags: List[str]
    perception: int
    skills: List[Skill]
    strength: int
    dexterity: int
    constitution: int
    intelligence: int
    wisdom: int
    charisma: int
    ac: int
    fortitude: int
    reflex: int
    will: int
    hp: int
    speed: str
    abilities: List[Ability]
    spellcasting: Optional[List[Spellcasting]] = None
    vision: Optional[str] = None
    languages: Optional[str] = None
    items: Optional[str] = None
    immunities: Optional[str] = None
    resistances: Optional[str] = None
    weaknesses: Optional[str] = None


# Dataclass Parser
# Converts the API data taken from the Supabase database into a usable Monster Dataclass
def parse_monster(data: dict) -> Monster:
    monster = data.get("monster", {})

    # Parse skills
    skills = [
        Skill(name=monSkill.get("skill_name"), bonus=monSkill.get("bonus"))
        for monSkill in data.get("skills", [])
    ]

    # Parse abilities
    abilities = [
        Ability(
            name=ability.get("ability_name"),
            description=ability.get("description"),
            type=ability.get("ability_type"),
        )
        for ability in data.get("abilities", [])
    ]

    # Parse Spellcasting
    spellcasting_data = data.get("spellcasting", [])
    spellcasting = []

    for spellcasts in spellcasting_data:
        # Build SpellList items
        spell_lists = [
            SpellList(level=spell.get("level", ""), spells=spell.get("spells", ""))
            for spell in spellcasts.get("spells", [])
        ]

        spellcasting.append(
            Spellcasting(
                spell_type=spellcasts.get("spell_type", ""),
                dc=spellcasts.get("dc"),
                attack_bonus=spellcasts.get("attack_bonus"),
                spells=spell_lists,
            )
        )

    # Build the Monster object
    return Monster(
        id=data.get("id"),
        name=monster.get("name"),
        level=monster.get("level"),
        tags=data.get("tags", []),
        perception=monster.get("perception"),
        vision=monster.get("vision"),
        languages=monster.get("languages"),
        skills=skills,
        strength=monster.get("str"),
        dexterity=monster.get("dex"),
        constitution=monster.get("con"),
        intelligence=monster.get("int"),
        wisdom=monster.get("wis"),
        charisma=monster.get("cha"),
        items=monster.get("items"),
        ac=monster.get("ac"),
        fortitude=monster.get("fort"),
        reflex=monster.get("reflex"),
        will=monster.get("will"),
        hp=monster.get("hp"),
        immunities=monster.get("immunities"),
        resistances=monster.get("resistances"),
        weaknesses=monster.get("weaknesses"),
        speed=monster.get("speeds"),
        abilities=abilities,
        spellcasting=spellcasting or None,
    )


"""
--GUI section--
"""


# Initial "List" GUI
class App(ctk.CTk):
    def __init__(self, monList):
        super().__init__()  # Set appearance mode and default color theme
        ctk.set_appearance_mode("system")
        ctk.set_default_color_theme("blue")

        self.title("MonsterDB")
        # Change to change 'List' window size
        self.geometry("800x600")

        # Set background color
        self.configure(fg_color="#e8e8e8")

        # Configure grid layout (4x4) for better responsiveness
        self.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)

        # Create all widgets and components
        self.create_Mon_List(monList)

    # Call Database and create list
    def create_Mon_List(self, monList):
        """Create and place all widgets"""
        self.frame = ctk.CTkFrame(
            self,
            width=800,
            height=600,
            corner_radius=8,
            fg_color="#ffffff",
            border_width=1,
            border_color="#e2e8f0",
        )
        self.frame.place(x=0, y=0)

        y_pos = 0
        # For each monster in the list of monsters...
        for mon in monList:
            y_pos += 50
            x_pos = 8
            # Make a button with their name that can open a full version of their entry
            self.button = ctk.CTkButton(
                self,
                text=mon["name"],
                width=120,
                height=40,
                corner_radius=8,
                fg_color="#ffffff",
                hover_color="#cccccc",
                text_color="#000000",
                border_width=1,
                border_color="#e2e8f0",
                font=("Arial", 12, "normal"),
                command=lambda m_id=mon["id"]: OpenMonWindow(m_id),
            )
            self.button.place(x=x_pos, y=y_pos)
            x_pos += 128

            # Then make a label with their level
            self.label = ctk.CTkLabel(
                self,
                text="Level, " + str(mon["level"]),
                width=200,
                height=40,
                corner_radius=8,
                fg_color="white",
                text_color="#000000",
                font=("Arial", 12, "normal"),
            )
            self.label.place(x=x_pos, y=y_pos)
            x_pos += 208

            # Then make a label with their tags
            self.label = ctk.CTkLabel(
                self,
                text=mon["tags"],
                width=250,
                height=40,
                corner_radius=8,
                fg_color="white",
                text_color="#000000",
                font=("Arial", 12, "normal"),
            )
            self.label.place(x=x_pos, y=y_pos)


# Function to open a specific monster's entry
def OpenMonWindow(monId):
    # Open a new window
    new_window = ctk.CTkToplevel()
    mon = GetMon(monId).data
    MonSpec = parse_monster(mon)
    new_window.title(MonSpec.name)
    new_window.geometry("800x600")
    # Put the new window on top
    new_window.attributes("-topmost", True)
    new_window.update()

    new_window.frame = ctk.CTkFrame(
        new_window,
        width=800,
        height=600,
        corner_radius=8,
        fg_color="#ffffff",
        border_width=1,
        border_color="#e2e8f0",
    )
    new_window.frame.place(x=0, y=0)

    # Name Label
    label = ctk.CTkLabel(
        new_window,
        text=MonSpec.name,
        width=200,
        height=40,
        justify="left",
        anchor="w",
        fg_color="#ffffff",
        text_color="#000000",
        font=("Arial", 24, "normal"),
    )
    label.place(x=10, y=10)

    # Level Label
    label = ctk.CTkLabel(
        new_window,
        text=MonSpec.level,
        width=200,
        height=40,
        justify="right",
        fg_color="#ffffff",
        text_color="#000000",
        font=("Arial", 24, "normal"),
    )
    label.place(x=400, y=10)

    # Tags Label
    capTags = ", ".join(tags.capitalize() for tags in MonSpec.tags)
    label = ctk.CTkLabel(
        new_window,
        text=f"{capTags}",
        width=300,
        height=40,
        justify="left",
        anchor="w",
        fg_color="#ffffff",
        text_color="#000000",
        font=("Arial", 18, "normal"),
    )
    label.place(x=10, y=48)

    # Set Up Text as one Label
    # Perception
    finalLabel = ""
    if MonSpec.vision != None:
        temp_perception = f"Perception: +{MonSpec.perception} ,{MonSpec.vision}"
    else:
        temp_perception = f"Perception: +{MonSpec.perception}"
    finalLabel += temp_perception + "\n"

    # Languages
    if MonSpec.languages != None:
        finalLabel += f"Languages: {MonSpec.languages} \n"

    # Skills
    if MonSpec.skills != None:
        temp_skill = ", ".join(
            f"{skill.name.capitalize()} +{skill.bonus}" for skill in MonSpec.skills
        )
        finalLabel += f"Skills: {temp_skill} \n"

    # StatBlock
    finalLabel += f"Str {MonSpec.strength:+d}, Dex {MonSpec.dexterity:+d}, Con {MonSpec.constitution:+d}, "
    finalLabel += f"Int {MonSpec.intelligence:+d}, Wis {MonSpec.wisdom:+d}, Cha {MonSpec.wisdom:+d} \n"

    # Sense Abilities
    senseAbilities = []
    for ability in MonSpec.abilities:
        if ability.type == "senses":
            senseAbilities.append(ability)
    if senseAbilities != None:
        fullsenseAbilities = ""
        for senseAbility in senseAbilities:
            fullsenseAbilities += (
                f"{senseAbility.name.capitalize()} : {senseAbility.description}\n"
            )
        finalLabel += f"{fullsenseAbilities}"

    # Items
    if MonSpec.items != None:
        finalLabel += f"Items: {MonSpec.items} \n"

    # Defense Divider
    finalLabel += "--------------------------------------------------------------------"
    finalLabel += "\n"

    # AC, HP Lines
    finalLabel += f"AC: {MonSpec.ac}; Fort {MonSpec.fortitude:+d}, Ref {MonSpec.reflex:+d}, Will {MonSpec.will:+d}\n"
    hpLine = []
    hpLine.append(f"HP: {MonSpec.hp}")
    if MonSpec.immunities != None:
        hpLine.append(f"Immunities: {MonSpec.immunities}")
    if MonSpec.weaknesses != None:
        hpLine.append(f"Weaknesses: {MonSpec.weaknesses}")
    if MonSpec.resistances != None:
        hpLine.append(f"Resistances: {MonSpec.resistances}")
    hpLineFull = "; ".join(hpLine)
    finalLabel += hpLineFull + "\n"

    # Aura Abilities
    auraAbilities = []
    for ability in MonSpec.abilities:
        if ability.type == "aura":
            auraAbilities.append(ability)
    if auraAbilities != None:
        fullAuraAbilities = ""
        for auraAbility in auraAbilities:
            fullAuraAbilities += (
                f"{auraAbility.name.capitalize()} : {auraAbility.description}\n"
            )
        finalLabel += f"{fullAuraAbilities}"

    # Defensive Abilities
    defAbilities = []
    for ability in MonSpec.abilities:
        if ability.type == "defense":
            defAbilities.append(ability)
    if defAbilities != None:
        fullDefAbilities = ""
        for defAbility in defAbilities:
            fullDefAbilities += (
                f"{defAbility.name.capitalize()} : {defAbility.description}\n"
            )
        finalLabel += f"{fullDefAbilities}"

    # Offense Divider
    finalLabel += "--------------------------------------------------------------------"
    finalLabel += "\n"

    # Speed
    finalLabel += f"Speed {MonSpec.speed} \n"

    # Offensive Abilities
    offAbilities = []
    for ability in MonSpec.abilities:
        if ability.type == "attack":
            offAbilities.append(ability)
    if offAbilities != None:
        fullOffAbilities = ""
        for offAbility in offAbilities:
            fullOffAbilities += (
                f"{offAbility.name.capitalize()} : {offAbility.description}\n"
            )
        finalLabel += f"{fullOffAbilities}"

    # Spellcasing
    if MonSpec.spellcasting != None:
        for spellcasting in MonSpec.spellcasting:
            finalLabel += f"{spellcasting.spell_type}"
            if spellcasting.dc != None and spellcasting.attack_bonus != None:
                finalLabel += (
                    f" DC {spellcasting.dc}, attack {spellcasting.attack_bonus:+d}"
                )
            elif spellcasting.dc != None:
                finalLabel += f" DC {spellcasting.dc}"
            elif spellcasting.attack_bonus != None:
                finalLabel += f" attack {spellcasting.attack_bonus}"
            finalLabel += "\n"
            for spell in spellcasting.spells:
                finalLabel += f"{spell.level}: {spell.spells}\n"

    # Finalized label print
    label = ctk.CTkLabel(
        new_window,
        text=finalLabel,
        width=600,
        height=300,
        fg_color="#ffffff",
        text_color="#000000",
        font=("Arial", 12, "normal"),
        justify="left",
        anchor="w",
        wraplength=600,
    )
    label.place(x=10, y=96)


"""
--SQL Section--
"""
# PostgreSQL Setup
load_dotenv()

url = str(os.getenv("SUPABASE_URL"))
key = str(os.getenv("SUPABASE_KEY"))
secret = str(os.getenv("SUPABASE_SECRET"))

Client = supabase.Client(url, key)


# Function to get list of available monsters
def GetMonList():
    response = (
        Client.table("monsters").select("id, name, level, monster_tags(tag)").execute()
    )
    return response


# Function to call PostgreSQL function to get all Monster data
# Function found in 'get_monster_full.txt'
def GetMon(monId):
    response = Client.rpc("get_monster_full", {"p_monster_id": monId}).execute()
    return response


# Set Up Main Monster List
monStart = GetMonList()
monList = []
for m in monStart.data:
    monDict = {}
    monDict["id"] = m["id"]
    monDict["name"] = m["name"]
    monDict["level"] = m["level"]
    tags = [t["tag"].capitalize() for t in m["monster_tags"]]
    monDict["tags"] = ", ".join(tags)
    monList.append(monDict)

# Main program initialization
try:
    app = App(monList)
    app.mainloop()
except Exception as e:
    print(f"Error running application: {e}")
    import traceback

    traceback.print_exc()
