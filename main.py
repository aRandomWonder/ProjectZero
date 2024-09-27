from time import sleep


print("Welcome to Project Zero!")
print("In this limitless expanse, free from your real world identity, who will you be?")

while True:
    choice = input("Do you have an account [y/n] >>   ")
    if choice.lower == "y":
        break
    elif choice.lower == "n":
        print("Please fill out the questions below.")
    else:
        print("Invalid choice. Please try again.")

print("Loading. . .")
sleep(3)