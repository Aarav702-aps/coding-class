def factorial(n):
    if n == 0 or n == 1: #base case 0! and 1! are both 1
        return 1
    else:
        return n * factorial(n - 1) # recursive call

num = int(input("enter a number: ")) 

#check if the number is negative
if num < 0:
    print("factorial does not exist for negative number")
else:
    result = factorial(num) #calling function and save the return value in a variable 
    print(f"the factorial of {num} is {result}")