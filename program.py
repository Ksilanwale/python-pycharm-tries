import random

# Приветствие в начале игры
print()
print("-------------------------")
print("|    GUESS THE NUMBER   |")
print("-------------------------")
print()

goal = random.randint(0, 100)
number = -1

# Просим ввести имя, чтоб в дальнейшем общаться с игроком
player = input("Please enter your name ")

while number != goal:
    # Будет просить ввести число пока не введётся правильный вариант
    number_text = input("{}, guess a number between 0 and 100: ".format(player))
    number = int(number_text)

    if number > goal:
        # Если выбрал больше
        print("Sorry, {}, your number ({}) is too HIGH! try another one".format(player, number))
    elif number < goal:
        # Если выбрал меньше
        print("Sorry, {}, your number ({}) is too LOW! try another one".format(player, number))
    else:
        # Угадал число, игра закончена!
        print("Excellent work, {}! {} is the right number!".format(player, goal))
