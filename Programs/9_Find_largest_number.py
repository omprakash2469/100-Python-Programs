## Find the largest number
a = int(input("Enter your first number:"))
b = int(input("Enter your second number:"))
c = int(input("Enter your third number:"))

if a>b and a>c:
    print(a, "is the largest number")
elif(b>a and b>c):
    print(b, "is the largest number")
else:
    print(c, "is the largest number")