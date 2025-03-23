try :
    num = int(input("enter your number: "))
    print("the number enteered is: ",num)

except ValueError as e: #using value error
    print("Excption",e)

print("i am outside the try-excpet block") # alaways executed and displayed the meggage
print()