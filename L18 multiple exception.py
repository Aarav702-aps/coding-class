try:
    num1, num2 = eval(input("enter two number separted by coma: "))
    result = num1/num2
    print("result is : ",result)  
    print("result is : ",result1) 

except ZeroDivisionError:
    print("divison by zero is not allowed")

except SyntaxError:
    print("coma is missing. enter numbers with seperated coma like this: 1, 2")

except ValueError:
    print("please enter numical value")

except NameError as ex:
    print("The excption is",ex)

except:
    print("some error occured")

else:
    print("no excption or no error")

finally:
    print("i will execute no matter what happens")