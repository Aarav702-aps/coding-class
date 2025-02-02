#take marks as input
print("enter marks of your subjects here")
math = int(input("enter your marks for math = "))
english = int(input("enter your marks for english = "))

#sum of all subjects
sum = math + english

#calculate percentage
percentage = sum/2 * (100/100)

print("your percentage mark is ",percentage,"%")