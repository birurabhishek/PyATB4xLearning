#Ternary Operator

#if condition then do this
#   else do this

"""
if myAge > 18 then i can drink beer
    else i can't drink
"""

#First Method
myAge = int(input("Please enter your age: "))

print("You can drink beer" if myAge > 18 else "Can't drink, Go home")

#Second Method
if myAge > 18:
    print("Can drink")
else:
    print("Kiddo..! Go home")

#Third Method
print("You can drink beer" if int(input("Please enter your age: ")) > 18 else "Can't drink, Go home")