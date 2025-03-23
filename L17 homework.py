price = 2.50 #defineing price value

# define a funtion to calulate the differnce
# and price mentioned
def calculate_change(amount_given):
    return amount_given - price

c = calculate_change(4.00) # call the funtion and save the retren value in variable c
print("change the customer is due", c)