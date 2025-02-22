sick = input("are you currently sick (y/n)? ")

attend = int(input("enter the attendance day of the sudent = "))

if sick.lower() == "y":
    print("you are not allowed to take exam")
elif sick.lower() == "n":
    if attend >= 75:
        print("you are allowed to take exam")
    else:
        print("you are not allowed to take exam")
else:
    print("invalid option")