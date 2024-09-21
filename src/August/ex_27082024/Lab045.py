import math


def give_me_power(num):
    return math.pow(num,2)

op = give_me_power(10)
print(op)


give_me_power2 = lambda  : math.pow(int(input("Enter the number: ")),2)
print(give_me_power2())

print(lambda  : math.pow(int(input("Enter the number: ")),2))