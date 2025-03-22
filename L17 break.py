word = input("enter a word: ")

for i in word:
    if (i == 'A'):
        print("A is found")
        break # stop the repition proess and get out of the loop
    else:
        print("A is not found")