from time import sleep as wait
import os

# To Clear the Terminal
def clear_terminal():
    os.system("clear")

from skillset import PUNCH, Skill
from inventory import Item
from time import sleep as wait

class Player:
    def __init__(self):
        self.name = None
        self.inventory = []
        self.equipped = {"": None}
        self.weapon = None
        self.skillset = [PUNCH,]

        # Presets
        self.max_hp = 10
        self.hp = 10
        self.mana = 10
        self.agil = 5
        self.defe = 5
        self.str = 5
        self.magic = 5
        self.vit = 5

        # Battle Presets
        self.bp_mhp = 10
        self.bp_hp = 10
        self.bp_mana = 10
        self.bp_agil = 5
        self.bp_defe = 5
        self.bp_str = 5
        self.bp_magic = 5
        self.bp_vit = 5

        # More Presets
        self.free_attr_points = 0
        self.free_skill_points = 0

        # Even more presets
        # C stands for conversion factor
        self.vit_hp_c = 2
        self.mm_c = 2

    def __str__(): # Bruh, don't print the character
        return "A sad little spirit."

    def update_attr(self): #
        self.max_hp = self.vit * self.vit_hp_c
        self.mana = self.magic * self.mm_c
    
    def get_inventory(self):
        print("=========================")
        print("INVENTORY")
        for i, item in enumerate(self.inventory):
            print(f"{i}: {item.name}")
        print("=========================")
        while True:
            print("Would you like to view a specific item [y/n]?")
            choice = input()
            if choice == "y":
                print("Pick an item above by its number: ")
                choice = input()
                if 0 <= int(choice) < len(self.inventory):
                    print(self.inventory[int(choice)])
                    input("Press enter to continue.")
                    break
                else: 
                    print("Invalid option. Please try again.")
            elif choice == "n":
                print("Very well.")
                wait(1)
                break
            else:
                print("Invalid choice. Please try again.")

    def get_stats(self):
        print("=========================")
        print(" STATS ")
        print(f"HP: {self.hp}")
        print(f"MANA: {self.mana}")
        print(f"STRENGTH: {self.str}")
        print(f"AGILITY: {self.agil}")
        print(f"DEFENSE: {self.defe}")
        print(f"VITALITY: {self.vit}")
        print(f"MAGIC: {self.magic}")
        print("=========================")

    def add_stats(self):
        if self.free_attr_points:
            print("Which one do you want to add it in?")
            print("1: Strength: Physical Damage, ")
            print("2: Agility: Speed, Crit, Dodge rate")
            print("3: Defense: Lowers Damage Recieved")
            print("4: Vitality: Resistance against damage, HP")
            print("5: Magic: Mana, magic resistence")
            while True:
                choice = input("Choose an option (the corrosponding number):")
                if choice == "1":
                    self.str += 1
                    self.free_attr_points -= 1
                    print(f"Your strength stat is now {self.str}")
                elif choice == "2":
                    self.agil += 1
                    self.free_attr_points -= 1
                    print(f"Your agility stat is now {self.agil}")
                elif choice == "3":
                    self.defe += 1
                    self.free_attr_points -= 1
                    print(f"Your defense stat is now {self.defe}")
                elif choice == "4":
                    self.vit += 1
                    self.free_attr_points -= 1
                    print(f"Your vitality stat is now {self.vit}")
                elif choice == "5":
                    self.magic += 1
                    self.free_attr_points -= 1
                    print(f"Your magic stat is now {self.magic}")
                else:
                    print("Invalid Choice. Try again.")
                    continue
                self.update_attr()
                break
        else:
            print("No free stat points.")

    def add_item(self, item):
        if isinstance(item, Item):
            print("=========================")
            self.inventory.append(item)
            print("You picked up an Item.")
            print(item)
            print("=========================")
            return 0
        else:
            print("Invalid Item.")
            return -1

    def learn_skill(self, skill):
        if isinstance(skill, Skill):
            if self.free_skill_points >= skill.rs:
                while True:
                    print(f"Are you sure you want to spend {skill.rs}"
                          f" skill points to learn the skill {skill.name}?")
                    choice = input("[y/n] >>  ")
                    if choice == "y":
                        self.free_skill_points -= skill.rs
                        self.skillset.append(skill)
                        print(f"You have learned the skill {skill.name}")
                        print(f"Remaining free skill points:"
                              f"{self.free_skill_points}")
                        break
                    elif choice == "n":
                        print("Skill learning canceled. No changes made.")
                        break
                    else:
                        print("Invalid choice. Try again")
            else:
                print("Sorry, you don't have enough skill points to learn "
                      f"{skill.name}.")
                print(f"Required amount: {skill.rs}")
                print(f"Current amount: {self.free_skill_points}")
        else:
            print("Invalid skill.")
            return -1

    def show_skills(self):
        print("=========================")
        print("SKILLSET")
        for i, skill in enumerate(self.skillset):
            print(f"{i}: {skill.name}")
        print("=========================")

    def calculate_bp(self):
        print("Used to calculate battle stat points")
        effects = [item.effect for item in self.equipped if not None]
        for effect in effects:
            self.bp = None

        print("WIP")

class Being:
    def __init__(self, name, inventory, equipped, weapon,
                 skillset, stats):
        # Presets
        self.name = name
        self.inventory = inventory
        self.equipped = equipped
        self.weapon = weapon

        # Variable
        self.skillset = skillset
        self.max_hp = stats["max_hp"]
        self.hp = stats["max_hp"]
        self.mana = stats["mana"]
        self.magic = stats["magic"]
        self.agil = stats["agil"]
        self.str = stats["str"]
        self.defe = stats["defe"]
        self.vit = stats["vit"]

    def drop(self):
        n = len(self.inventory)
        pass