## Check if it is a Leap Year
year = int(input("Enter a year: "))

# After dividing a year by 400 and 100 the remainder is 0, then it is a leap year
if (year % 400 == 0) and (year % 100 ==0):
    print("It is a Leap year")

# After dividing a year by 4 then the remainder is 0 and
# After dividing a year by 100 then the remainder is not 0, then it is a leap year
elif(year % 4 == 0) and (year % 100 != 0):
    print("It is a Leap year")
else:
    print("It is not a Leap year")