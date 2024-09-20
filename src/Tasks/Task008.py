"""
Leap Year Checker
-----------------
Create a program that determines whether a given year is leap year or not.
A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
Use an if-else statement to make this determination.

Rough Logic
-----------
Is year divisible by 4 --> NO --> Not a leap year, If Yes --> & Is year divisible by 100 --> No --> Leap year --> If yes -->
or Is year divisible by 400 --> No --> Not a leap year --> If yes --> LEAP YEAR
"""
year = int(input("Enter the year\n"))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("Leap Year")
else:
    print("Not a Lear Year")

