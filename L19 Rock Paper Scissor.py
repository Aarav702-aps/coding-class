import random

options = ["rock", "paper", "scissors"]

user_choise = input("choose rock, paper, or scissors: ")
computer_choise = random.choice(options)
print()

print("you chose:", user_choise)
print("computer chose:", computer_choise)

if user_choise == computer_choise:
    print("its a tie!")

elif user_choise == "rock" and computer_choise == "scissors":
    print("rock smashes scissors! you win!")

elif user_choise == "paper" and computer_choise == "rock":
    print("paper covers rock! you win!")

elif user_choise == "scissors" and computer_choise == "paper":
    print("scissors cuts paper! you win!")

else:
    print("you lose. ")