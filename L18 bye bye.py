valid = False

while not valid:
    try:
        n = int(input("enter a number: "))

        # enter a even number
        while n%2 == 0:
            print("bye")
            valid = True
    except ValueError:
        print("invaild")