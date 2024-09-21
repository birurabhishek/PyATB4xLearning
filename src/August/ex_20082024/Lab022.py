# Find the Max of 3 numbers

# Logic Building
# User inputs -> num1, num2, num3 --> int
# Output -> int or string with max number

"""
Logic
------

If-else is used only when we have only 1 conditions i.e True or False.
If more than 1 condition than if, elif, else conditions can be used

Syntax
------
if condition 1:
    print("Do 1")
elif condition 2:
    print("Do 2")
elif condition 3:
    print("Do 3")
else:
    print("Do 4)
"""
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
num3 = int(input("Enter num3: "))

# Rough Logic
# num1>num2 and num1 > num3 -> num1
# num2>num1 and num2 > num3 -> num2
# If both are false then num3

if num1 > num2 and num1 > num3:
    print(f"{num1} is greater")
elif num2 > num1 and num2 > num3:
    print(f"{num2} is greater")
else:
    print(f"{num3} is greater")
    
