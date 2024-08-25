#Write a python program to calculate the area of a circle given its radius using the formula area=pie*r^2

"""
Logic Building Formula
-----------------------
Step 1: Figure out the inputs and outputs
Input -> r -> datatype -> float
Pi = 3.14 or math.pi
Power = pow or ** --> Any

Output -> float - Area, Print area

Step 2: Rough Logic
area = 3.14 * pow(r,2)

Step 3: Write the logic
"""
import math

radius = float(input("Enter the radius for which you want to calculate the area of a circle: \n"))
pie = 3.14

area = (math.pi * pow(radius,2))
print(f"Area:{area}")
print(f"Area:{area:.2f}")

print(math.pi*float(input("Please enter the radius:"))**2)