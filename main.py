from time import sleep as wait
from player import Player

player = Player()

print("Welcome to Project Zero!")
print("In this limitless expanse, free from your real world identity, who will you be?")

while True:
    choice = input("Do you have an account [y/n] >>   ")
    print(choice.lower())
    if choice.lower() == "y":
        break
    elif choice.lower() == "n":
        print("Please fill out the questions below.")
        player.fill_stats()
        break    
    elif choice.lower() == "secret code":
        print("👿")
        wait(3)
        print("I will kill you in your sleep.")
        wait(1)
        print("However... Do you know the code..?")
        code = input("")
        if code == "1234":
            print("You are... The chosen one...")
            wait(1000)
            print("You found a easter egos. JK")
    else:
        print("Invalid choice. Please try again.")

print("Loading. . .")
wait(3)


# Actual Game Start
print("Welcome, Navigator! What's your name?")

while True:
    print("This can't be changed")
    player.name = input(">>>   ")
    answer = input(f"Confirm your name is {player.name}? [y/n] >>>  ")
    if answer.lower() == "y":
        print(f"Welcome, {player.name}")
    elif answer.lower() == "n":
        print("Try again.")
    else:
        print("Invalid answer. Try again.")
        input()

print("")