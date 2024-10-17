from time import sleep
import os


def clear_terminal():
    os.system("clear")

class Player:
    def __init__(self, name = None, level = None, prof = None, sub_prof = None, 
                 stats = {"vit": 5, "str": 5, "defe": 5, "agi": 5, "mana": 5}, hidden_stats = {"fortitude": 0, "luck": 0, "dex": 0}, 
                 inventory = {}, equips = {}, status = {}, affil = {}, skills = {}):
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
        self.skills = skills

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

        print("Agility - determines your speed. To select, put in \"agil\"")
        sleep(0.5)

        print("Defense - determines the damage you recieve. To select, put in \"defe\"")
        sleep(0.5)

        print("Vitality - determines your health")

        print("Strength - determines your attack power. To select, put in \"str\"")
        input("Press Enter to Move On.")

        print("Now you will distribute you're points. You have 15 to freely add.")
        print("They start at 5, half of the average human. Choose wisely.")
        input("Press Enter to Start Adding Points")

        clear_terminal()

        i = 1
        while True:
            choice = input(f"You have {16-i} points left.")
            choice = choice.lower()
            if choice == "agil":
                pass
            elif choice == "str":
                pass
            elif choice == "defe":
                pass
            elif choice == "vit":
                pass
            else:
                print("Invalid choice")
                sleep(0.5)
                print("Please try again")
                continue
            i += 1
            if i == 15: 
                print("Selection complete.")
                sleep(0.5)
                print("Here are your current attributes: ")
                input()

            

class Skill:
    def __init__(self, name):
        self.name = name