from time import sleep as wait
import os

# To Clear the Terminal
def clear_terminal():
    os.system("clear")

class Player:
    def __init__(self, name = "Unknown", level = None, prof = None, sub_prof = None, 
                 stats = {"vit": 5, "str": 5, "defe": 5, "agi": 5, "mana": 10, "magic": 5}, 
                 hidden_stats = {"fortitude": 0, "luck": 0, "dex": 0},
                 free_points = {"stat_points": 0, "hidden_points": 0, "skill_points": 0} ,
                 inventory = {}, equips = {}, status = {}, affil = {}, skills = {}):
        
        # Basic information
        self.name = name
        self.level = level
        self.prof = prof
        self.sub_prof = sub_prof

        # Stats
        self.vit = stats["vit"]
        self.hp = vit * 50
        self.str = stats["str"]
        self.defe = stats["defe"]
        self.agi = stats["agi"]
        self.magic = stats["magic"]
        self.mana = stats["magic"] * 20
        self.afin = stats["afin"]

        # Hidden Stats
        self.fort = hidden_stats["fortitude"]
        self.luck = hidden_stats["luck"]
        self.dex = hidden_stats["dex"]

        # Inventory
        self.inventory = inventory
        self.equips = equips
        self.status = status
        self.affil = affil
        self.skills = skills

        # Alternate Stats
        self.alt_stats = {}

        # Default Stats


    def print_status(self):
        return True
    
    def add_stats(self):
        pass

    def view_stats(self):
        pass

    def view_inventory(self):
        pass

    def get_item(self):
        pass

    def use_item(self):
        pass