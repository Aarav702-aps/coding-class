def hotel_cost(nights):
    return 140*nights

#define a funtion called plane_ride_cost that takes a string, city as input.
def plane_ride_cost(city):
    if "New Delhi" == city:
        return 183
    elif "tampa" == city:
        return 220
    elif "pittsburgh" == city:
        return 222
    elif "los angeles" == city:
        return 475
    elif "london" == city:
        return 275
    
# define a funtion called retal_car_cost with a arugment day, money and city
def retal_car_cost(days):
    if days>=7 :
        return 40*days - 50
    elif days>=3 :
        return 40*days - 20
    else:
        return 40*days
    
#define a funtion called trip cost with argument day, money and city
def trip_cost(city, days, spending_money):
    return retal_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money

print("cost of car rentel: ",retal_car_cost(6))

print("cost of plane ride: ",plane_ride_cost("los angeles"))

print("cost of hotel room: ", hotel_cost(7))

result = trip_cost("los angeles", 7, 500) #city, days, spending money
print("total cost of the trip to los angles:", result)