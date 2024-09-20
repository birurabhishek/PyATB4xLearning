"""
Triangle Classifier
-------------------
Write a program that classifies a triangle based on its side lengths.
Given three input values representing the lengths of the side,
determine if the triangle is equilateral(all sides are equal),
isosceles(exactly two sides are equal) or scalene (no sides are equal)
Use an if-else statement to classify the triangle.


Rough Logic
-----------
if L1=L2=L3 --> Equilateral
if L1&L2 | L1&L3 | L2&L3 --> Isosceles
if L1!=L2!=L3 --> Scalene
"""
a = float(input("Enter side a:"))
b = float(input("Enter side b:"))
c = float(input("Enter side c:"))

if a == b == c:
    print("Equilateral Triangle")
elif a == b or a == c or b==c:
    print('Isosceles Triangle')
else:
    print('Scalene')
