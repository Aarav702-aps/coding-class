#take two input from user
lower = int(input("enter a lower range = "))
upper = int(input("enter a upper range = "))

print()
print("prime numbers between",lower,"and",upper,"are:")

#display the result
for num in range(lower, upper +1):
    if num > 1: #all prime numbers are greater than 1
        for i in range(2, num):
            if (num % i) == 0: #if the number can be divided by other number, then its not prime number so we need to stop checking
                break
        else:
            print(num)