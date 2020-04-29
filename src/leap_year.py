"""
@input: year(int)
@returns: bool
@description: Given a year as int input method return bool value True or False
              if input year is leap or not.
              Leap year in gregorian calendar follows below criterion
              1. Year must be evenly divisible by 4
              2. If it is evenly divisible by 100 then it must be
                 divisible by 400 

"""
def is_leap_year(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False