#WAP to sum of three number from user input

def sum_of_three_number(num1, num2, num3):
    return num1+num2+num3

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
num3 = int(input("Enter num3: "))

result = sum_of_three_number(num1,num2, num3)
print(result)