#define funtion to calulate cube
def cube(number):
    return number * number * number

#define a funtion which will exucute cube funtion if the user entered a number is diviable by 3
def by_three(num):
    if num % 3 ==0:
        return cube(num) #calling funtion Cube()
    else:
        return False
    
x = 9
y = 4

#display result 
result1 = by_three(x) # passing argument x
result2 = by_three(y) # passing argument y

print(result1)
print(result2)