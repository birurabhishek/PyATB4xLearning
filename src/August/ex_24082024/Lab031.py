#User-defined is of 4 types
#1.They can return something
#2.They can't return -> Non-return
#3.They have parameters
#4.They don't have parameters / arguments

#1.No return type with arguments
def greet_by_name(name):
    print("Hello", name)

greet_by_name("Abhishek")

#2. No return type and no parameters/arguments - NRNP
def greet():
    print("Hello There")

result = greet()
print(result)

#3. No return type with default argument
def say_hello_default_arg(name='Abhishek'):
    print("Hello", name)

say_hello_default_arg() #Default argument
say_hello_default_arg('Tejas')
say_hello_default_arg(name = 'Teejjjjjjjjaaaasssssssss') #Positinal argument

def multiple_args(name1='Apple', name2='Mango', name3='Pineapple', name4='Pear'):
    print("Mulitple arguments:", name1, name2, name3, name4)

multiple_args()

#4. Argument + return type

def sum_of_two_numbers(num1, num2):
    return(num1 + num2)

result = sum_of_two_numbers(1,2)
print(result)
result = sum_of_two_numbers(num2=10, num1=10)
print(result)