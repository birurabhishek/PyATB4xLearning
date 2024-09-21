"""
Grade Calculator
----------------

Write a program that calculates and displays the letter grade for a given numerical score
(eg: A, B, C, D, E) based on following marks.
A: 90 - 100
B: 80 - 89
C: 70 -79
D: 60 - 69
E: 0 -59

Logic Building
----------if score >= 90 and score <=100-----
1. User Inputs -> Scores -> Int
2. Output -> String -> Grade(A,B,C,D,E)
#Rough Logic
-------------
score>=90 and <=100 -> A
score>=80 and <=89 -> B
score>=70 and <=79 -> C
score>=60 and <=69 -> D
Else E
"""
score = int(input("Enter your score:"))
if score >= 90 and score <= 100:
    print("Your grade is A")
elif score >= 80 and score <= 89:
    print("Your grade is B")
elif score >= 70 and score <= 79:
    print("Your grade is C")
elif score >= 60 and score <= 69:
    print(f"Your grade is D")
elif score > 100:
    print("Please enter the numbers between 0 to 100")
else:
    print("Your grade is E")

#Simplified Chain Format
if 90 <= score <= 100:
    print("Your grade is A")
elif 80 <= score <= 89:
    print("Your grade is B")
elif 70 <= score <= 79:
    print("Your grade is C")
elif 60 <= score <= 69:
    print(f"Your grade is D")
elif score > 100:
    print("Please enter the numbers between 0 to 100")
else:
    print("Your grade is E")
