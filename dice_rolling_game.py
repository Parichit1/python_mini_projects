import random

count = 0
while True:
    choice = input("Do you wanna roll the dice (y/n): ").lower()
    if choice == ("y"):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(die1, die2)
        count += 2

    elif choice == ("n"):
        print("Thanks for playing")
        print(f"You have rolled  the die {count} times.")
        break

    else:
        print("Invalid choice please choose (y/n) ")
