import random
import time 

def getrandomdate(startdate, endDate):
    print("printing randon date between", startdate, "and", endDate)
    randomgenerator = random.random()

    dateformat = "%m/%d/%Y"
    starttime = time.mktime(time.strptime(startdate, dateformat))
    endtime = time.mktime(time.strptime(endDate, dateformat))

    randomtime = starttime + randomgenerator * (endtime - starttime)
    randomdate = time.strftime(dateformat, time.localtime(randomtime))

    return randomdate


result = getrandomdate("4/23/2025", "12/31/2025")
print("ramdom date = ", result)