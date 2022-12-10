## Swap values of two variables
# 1. Using third variable
a = 12
b = 13

# t = a
# a = b
# b = t
# print("Value of a is: ", a)
# print("Value of b is: ", b)

# 2. Using other method
a, b = b, a
print("Value of a is", a)
print("Value of b is", b)