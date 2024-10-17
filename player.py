from time import sleep
import os


def clear_terminal():
    os.system("clear")

class Player:
    def __init__(self, name = "Unknown", level = None, prof = None, sub_prof = None, 
                 stats = {"vit": 5, "str": 5, "defe": 5, "agi": 5, "mana": 5}, 
                 hidden_stats = {"fortitude": 0, "luck": 0, "dex": 0}, 
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
        self.magic = self.mana * 20
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
                self.agi += 1
            elif choice == "str":
                self.str += 1
            elif choice == "defe":
                self.defe += 1
            elif choice == "vit":
                self.vit+=1
            else:
                print("Invalid choice")
                sleep(0.5)
                print("Please try again")
                continue
            i += 1
            sleep(0.5)
            if i == 15: 
                print("Selection complete.")
                sleep(0.5)
                print("Here are your current attributes: ")
                input()
                print(f"Strength: {self.str}")
                sleep(0.1)
                print(f"Agility: {self.agil}")
                sleep(0.1)
                print(f"Defense: {self.defe}")
                sleep(0.1)
                print(f"Vitality: {self.vit}")
                input()
                choice = input(f"Confirm? [y/n]").lower()
                
                while True:
                    if choice == "y":
                        print("Choice confirmed.")
                        print("Please stand by.")
                        input()
                        clear_terminal()
                    elif choice == "n":
                        print("Resetting stats. . .")
                        sleep(0.5)
                        self.str = 5
                        self.agi = 5
                        self.vit = 5
                        self.defe = 5
                        clear()
                    else:
                        print("Invalid choice. Try again.")
                        input()

            

class Skill:
    def __init__(self, name):
        self.name = name