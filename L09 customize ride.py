print("select your ride")
print("1. bike")
print("2. car")

choice = int(input("enter your choice 1 or 2 = "))

if choice == 1:
    print("what type of bike?")
    print("1. scooter")
    print("2. sports bike")

    choice2 = int(input("enter your type of bike 1 or 2 = "))

    if choice2 == 1:
        print("you have have selected scooter")
    else:
        print("you have seleted sports bike")

elif choice == 2:
    print("what type of car?")
    print("1. sedan ")
    print("2. suv")

    choice3 = int(input("enter your tpye of car 1 of 2 = "))

    if choice3 ==1:
        print("your have seleted sedan")
    else:
        print("you have seleted suv")

else:
    print("wrong choice")