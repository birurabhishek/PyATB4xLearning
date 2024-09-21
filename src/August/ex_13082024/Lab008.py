#Take a user inputs a,b and calculate sum, sub, mul, div
#Cal program

num1 = int(input("Please enter Number 1:"))
num2 = int(input("Please enter Number 2:"))
add = (num1 + num2)
sub = (num1 - num2)
mul = (num1 * num2)
div = (num1 / num2)
print(f'Sum is {add},and the datatype is {type(add)}')
print(f'Sub is {sub}and the datatype is {type(sub)}')
print(f'mul is {mul}and the datatype is {type(mul)}')
print(f'Div is {div}and the datatype is {type(div)}')

# Div is always floating number since there is a more chances of getting decimal points if we divide two numbers.


