r = int(input("enter the total numbers of rows  :  "))

print("mirrored right triangle star pattern")
for i in range(1,r+1):
    for j in range(1,r+1):
        print('', end= ' ')
    else:
        print('*', end= ' ')
print()