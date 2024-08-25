"""
Create a program, Take two inputs from the user num1 and num2 and give them
Max, pow of num1 to num2, sub, mul, sum, div using string formatting

Need to share via GitHub repo.
"""
num1 = int(input("Please enter First number:"))
num2 = int(input("Please enter Second number:"))

print(f"Max value is {max(num1,num2)}")
print(f"Power of {num1} and {num2} is {num1 ** num2}")
print(f"Addition of two numbers are {num1+num2}")
print(f"Subtraction of two numbers are {num1-num2}")
print(f"Multiplication of two numbers are {num1*num2}")
print(f"Division of two numbers are {num1/num2}")
