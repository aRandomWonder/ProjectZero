from time import sleep
import os


def clear_terminal():
    os.system("clear")

class Player:
    def __init__(self, name = None, level = None, prof = None, sub_prof = None, 
                 stats = {"vit": None, "str": None, "defe": None, "agi": None, "mana": None}, hidden_stats = {}, 
                 inventory = {}, equips = {}, status = {}, affil = {}):
        # Basic information
        self.name = name
        self.level = level
        self.prof = prof
        self.sub_prof = sub_prof

        # Stats
        self.vit = stats["vit"]
        self.hp = self.vit * 50
        self.str = stats["str"]
        self.defe = stats["defe"]
        self.agi = stats["agi"]
        self.mana = stats["mana"]
        self.magic = self.mana * 50
        self.afi = stats["afi"]

        # Hidden Stats
        self.fort = hidden_stats["fortitude"]
        self.luck = hidden_stats["luck"]
        self.dex = hidden_stats["dex"]

        # Inventory
        self.inventory = inventory
        self.equips = equips
        self.status = status
        self.affil = affil

        # Alternate Stats
        self.alt_stats = {}

    def print_status(self):
        return True
    
    def fill_stats(self):
        self.name = input("Enter your name:   ")

        print("Introduction to the basic 4 stats")
        sleep(0.5)
        print("There will be more as time goes on.")
        sleep(0.5)
        print("Agility - determines your speed.")
        sleep(0.5)
        print("Strength - determines your attack power ")
        input("Press Enter to Move On.")

        print("Now you will distribute you're points. You have 15 to freely add.")
        print("They start at 5, half of the average human. Choose wisely.")
        input("Press Enter to Start Adding Points")

        clear_terminal()

        for i in range(0, 15):
            choice = input(f"You have {15-i} points left")
            input()
            
