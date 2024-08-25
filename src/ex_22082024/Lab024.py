"""
Loops
-----
1. For loop
2. While loop

1. Break
2. Continue

1. Match Statement(Switch case)
"""
"""
FOR LOOP
--------
Can execute a block of code multiple times.
Syntax
-------
for variableName in range(start, stop, step):
    //code that has to be repeated multiple times
"""
#Print HELLO WORLD 10 times

for i in range(1,10): # Start =1,stop = 10-1, step by default it is 1
    print(i) # Value of i can be anything
for name in range(1,5):
    print(name, end = "|")

"""
WHILE LOOP
----------

Syntax
------

variableName = 0
while condition:
    execute this code
    variableName Increment
"""
print("\n-------------------------")
i = 0
while i < 10:
    print(i, end=" ")
    i = i+1
print("\n-------------------------")

#Break -- Based on the condition --> Exits the loop
for i in range(10):
    if i==6:
        print(i) #Start=0 and steps=1 by default
    else:
        print("NO output")
"""
|i | CONDITION | OUTPUT
|0 | 0 ==6 --> False |output -> No Output
|1 | 1 ==6 --> False |output -> No Output
|2 | 2 ==6 --> False |output -> No Output
|3 | 3 ==6 --> False |output -> No Output
|4 | 4 ==6 --> False |output -> No Output
|5 | 5 ==6 --> False |output -> No Output
|5 | 6 ==6 --> False |output -> 6
|5 | 7 ==6 --> False |output -> No Output
|5 | 8 ==6 --> False |output -> No Output
|5 | 9 ==6 --> False |output -> No Output

to avoid such invalid prints we can use pass
"""
print("\n--------------------------")
for i in range(10):
    if i==6:
        print(i) #Start=0 and steps=1 by default
    else:
        pass
