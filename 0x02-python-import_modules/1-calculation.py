#!/usr/bin/python3

# Importing functions from calculator_1.py
from calculator_1 import add, subtract, multiply, divide

# Defining variables a and b
a = 10
b = 5

# Performing calculations and printing the results
result1 = add(a, b)
result2 = subtract(a, b)
result3 = multiply(a, b)
result4 = divide(a, b)

print("The sum of", a, "and", b, "is:", result1)
print("The difference between", a, "and", b, "is:", result2)
print("The product of", a, "and", b, "is:", result3)
print("The division of", a, "and", b, "is:", result4)

