a = 23
b = 24
c = 22

if a > b or a < c:
    print("a is greater than b or a is less than c")
    print("i am using or operator")
elif a < b and a > c:
    print("a is less than b and greater than c")
    print("i am using and operator")

print()

x = 10
y = 5

if x > 7 or y > 7:
    print("either x or y is greater than 7")
else:
    print("none of them is greater than 7")