#Task5
#Create a program that takes two numbers as input and prints whether the first number is greater than,
# less than or equal to second number

#N1 > N2
#N1 < N2
#N1 = N2

num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

print(f"{num1} is greater than {num2}." if (num1 > num2) else f"{num1} is lesser than {num2}" if num1 < num2 else f"Both {num2} and {num1} are equal ")

