# take input from the user
num = int(input("enter a number: "))

# initalize sum
sum = 0

# find the sum of the cube of each digit
temp = num

while temp > 0:
    digit = temp % 10 # getting the reminder of the divison
    sum = sum + digit ** 3 #calculate each digit to the power of 3 and then add it to the sum
    temp = temp // 10 #floor divison (the result is rounded down without a decimal value)

#display the result 
if num == sum:
    print(num,"is an armstrong number")
else:
    print(num,"is not armstrong number")