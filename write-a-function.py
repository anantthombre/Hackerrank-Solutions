# Link to the coding question -  https://www.hackerrank.com/challenges/write-a-function

def is_leap(year):
    leap = False
    
    # Write your logic here
    if (year%100 != 0 and year%4 == 0) or (year%100 == 0 and year%400 == 0):
        leap = True
    
    return leap

year = int(input())
print(is_leap(year))
