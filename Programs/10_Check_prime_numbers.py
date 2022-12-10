## Check if it is a prime number

# What is a Prime Number?
# Ans: If a number is divisible by any number and gives 0 as a remainder, then it is not a prime number.
# If it doesn't gives a 0, then it is a prime number

# Simple Explanation:
# If a number appears in any table except it's own then it is not a prime number

# Get a number from user
num = int(input("Enter a prime number: "))

if num == 1:
    print("It is not a prime number")
if num > 1:
    for i in range(2, num):
        if num%i==0:
            print("It is not a prime number")
            break
    else:
        print("It is a prime number")