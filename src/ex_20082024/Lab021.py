# Code to find max between two numbers

#Logic Building
# 1. User inputs --> Two integers --> - input() method to take inputs
# 2. Output --> One integer whichever is greater(Max Number)

num1 = float(input("Enter num1: "))
num2 = float(input("Enter num2: "))

if num1 > num2:
    print(f"Max is {num1}")
else:
    print(f"Max is {num2}")