rows = int(input("please enter the total number of rows  :  "))
number = 1 #initialise by 1

print("floyed's triangle")
for i in range(1, rows + 1): # representing rows
    for j in range(1, i +1): # repesenting columuns
        print(number, end = ' ')
        number = number + 1

    print()