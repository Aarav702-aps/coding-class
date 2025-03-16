def add(P, Q):
    return P + Q

def subtract(P, Q):
    return P - Q

def mulitply(P, Q):
    return P * Q

def divide(P, Q):
    return P / Q

print("please select opreation.")
print("a. Add")
print("b. Subtract")
print("c. Multiply")
print("d. divide")

choice = input("please enter choice (a/b/c/d):")

num_1 = int(input("please enter the first number = "))
num_2 = int(input("please enter the second number = "))
print()

if choice.lower() == 'a':
    result = add(num_1, num_2)
    print(num_1, "+",num_2, "=",result)

elif choice.lower() == 'b':
    result = subtract(num_1, num_2)
    print(num_1, "-", num_2, "=",result)

elif choice.lower() == 'c':
    result = mulitply(num_1, num_2)
    print(num_1, "*", num_2, "=",result)

elif choice.lower() == 'd':
    result = divide(num_1, num_2)
    print(num_1, "/", num_2, "=",result)

else:
    print("this is invaid input")