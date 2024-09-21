# Conditions and Loop
"""
age > 18 -> Allowed to Vote - True
age < 18 -> Allowed to Vote - False

# If-Else Loop

Syntax
------
if condition:
    // Code to execute if condition is true
else:
    // Code to execute if condition is false
"""

# Write a program to take users age and let him know if he can go to club.

# Logic Building
# User input -> Datatype -> Int
# Output -> String -> Letting user know whether he can enter the club or not
# Rough logic  if age >21 -> print(can go) if age <21 -> print(cant go

age = int(input("What's your age?\n "))
if age > 21:
    print("Welcome to the club...!")
else:
    print("GO back to home Kiddoooo...!")
