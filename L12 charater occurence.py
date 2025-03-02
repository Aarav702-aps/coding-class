#take a input of a word
string = input("please enter your own word or sentence = ")

#take input of a character
char = input("please enter your own character = ")

i = 0
count = 0

#loop will find the occurense of character
while(i < len(string)): #string operation
    if(string[i] == char): #check each letter of the word whether its the same as the character that we want to find
        count = count +1

        i = i +1 #increase the value untill reach the length of the word, i is position of each letter in the word

#display the result
print("the total number",char,"character has occurred = ",count," times")