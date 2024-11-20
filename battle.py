from time import sleep as wait 
from random import random, randint
from item import Consumable
# battle.py

def battle_p(player, enemy, turn):
    print("Player's Turn")
    print("=======================")
    while True:
        print("Choose one of the options below:")
        print("1: Use an item [WIP] [NOT AVAILABLE]")
        print("2: Use a skill")
        print("3: Run")
        choice = input(">>>   ")
        if choice == "1":
            print("WIP, not available.")
        elif choice == "2":
            player.show_skills()
            while True:
                choice = input("Pick a skill by its number\n>>>  ")
                if 0 <= int(choice) < len(player.skillset):
                    player.skillset[int(choice)].cdl = 0
                    for skill in player.skillset:
                        if not(skill == player.skillset[int(choice)]):
                            skill.cdl += 1
                    print(f"Player has used the skill "
                          f"{player.skillset[int(choice)].name} on the enemy")
                    return player.skillset[int(choice)].effect
            
        elif choice == "3":
            print(f"{player.name} has attempted to run. . .")
            if player.agil > enemy.agil:
                print("The player has successfully ran!")
                return False
            elif player.agil < enemy.agil:
                chance = 1 - player.agil/enemy.agil
                r = random()
                if r < chance:
                    print("The player has successfully ran!")
                    for skill in player.skillset:
                        skill.cdl = 0
                else:
                    print("The player has failed to run. . .")
                    return True
        else:
            print("Invalid choice. Please try again.")

def battle_e(enemy, player, turn):
    print("Enemy's Turn")
    print("=======================")
    while True:
        print("Processing. . .")
        print("Enemy is choosing. . .")
        wait(1)
        choice = randint(0, len(enemy.skillset))
        if choice >= 0.95:
            print("Enemy is attempting to run. . .")
        elif choice >= 0.5:
            print("Enemy is attempting to run. . .")
        else:
            if enemy.inventory == {}:
                continue
            else:
                t = []
                for item in enemy.inventory:
                    if isinstance(item, Consumable):
                        t.append(item)

                if t == []:
                    continue
                else: # If they have a consumable item.
                    print("WIP. Stop experimenting with this.")
                    continue
            
def battle(player, enemy):
    round = 1
    

