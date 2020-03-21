import random

print()
print("-------------------------")
print("|    GUESS THE NUMBER   |")
print("-------------------------")
print()

goal = random.randint(0, 100)
number = -1

player = input("Please enter your name ")

while number != goal:
    number_text = input("{}, guess a number between 0 and 100: ".format(player))
    number = int(number_text)

    if number > goal:
        print("Sorry, {}, your number ({}) is too HIGH! try another one".format(player, number))
    elif number < goal:
        print("Sorry, {}, your number ({}) is too LOW! try another one".format(player, number))
    else:
        print("Excellent work, {}! {} is the right number!".format(player, goal))
