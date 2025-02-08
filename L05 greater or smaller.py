number = int(input("enter number to be check= "))

if number < 15:
    print(number," is less than 15")
    print("i am in the if block")
else:
    print(number," is greater than 15")
    print("i am in the else block")

print("i am not inside if and i am not in inside else block")