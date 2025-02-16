a = int(input("enter speed1 = "))
b = int(input("enter speed2 = "))
c = int(input("enter speed3 = "))

total = a + b + c
avg = total/3

if avg > a and avg > b and avg > c:
    print(avg," is greater than ",a," and ",b," and ",c)
elif avg > a and avg > b:
    print(avg," is greater than ",a," and ",b)
elif avg > a and avg > c:
    print(avg," is greater than ",a," and ",c)
elif avg > b and avg > c:
    print(avg," is greater than ",b," and ",c)
elif avg > a:
    print(avg," is greater than ",a)
elif avg > b:
    print(avg," is greater than",b)
elif avg > c:
    print(avg,"is greater than ",c)
else:
    print(" invalid input")