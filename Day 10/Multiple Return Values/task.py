
def is_leap_year(year):
    if(year % 4 == 0):
        if(year % 100 != 0):
            return True
        elif(year % 100 == 0):
            if(year % 400 == 0):
                return True
    return False
given_year = 2004
is_leap_year(given_year)
result = is_leap_year(given_year)
if (result == True):
    print(result)
elif (result == False):
    print(result)



