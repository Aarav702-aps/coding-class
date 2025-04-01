import random

playing = True
number = str(random.randint(10,20))

print("i will generate a number from 10 to 20, and you have to guess the number one digit at a time.")
print("the game ends when you get 1 hero!")

while playing:
    print("give me your best guess!")
    guess = input()

    if number == guess:
        print("you win the game")
        print("the number was",number)
        break

    else:
        print("your guess isnt quite right, try again")
        print()