"""
WAP in lambda function to find odd or even

"""

check_odd_even = lambda num : "Even" if num%2 == 0 else "odd"
num = int(input("Enter the number to find whether it is even or odd: "))
print(check_odd_even(num))