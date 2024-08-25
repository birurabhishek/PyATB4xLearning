'''
---------------------------------------------------------------------------------------------------------------
                                            Keywords & Identifiers
---------------------------------------------------------------------------------------------------------------
1. Keywords are also called as reserved words
2. Can be in lower case or upper case.
3. We cannot use keywords as variable name, function name or any identifier.
4. Keywords are case-sensitive.

# Variables ---> It is used to store values can be said as a container which hold something.

#Creating a variable.(Identifiers)
-----------------------------------
a. They should start with letter(A-Z or a-z).
b. An underscore(_) followed by zero or more letters.
c. Underscore(_) & Digits (0-9)
d. Python is case-sensitive.
e. so myVariable and MyVariable are two different variables.

Python Data Types
------------------
1. Numeric Datatype
    a. Integer  ---> int ---> (Whole Numbers) eg: 1, 2, -1234, 0, 13
    b. Float (Decimal Numbers) eg: 3.14, 18.45
    c. Complex -i - iota - 1+2j
    d. Boolean ---> True or False eg: isMarried --> False
2. String Datatype
    a. String ---> str ---> Bunch of characters --> Abhishek
3. List Datatype
    a. List ---> Enclosed by []
        shoppingList = ['Milk','Curd','Panner','Butter',]
        scoreCard = [100,95,94,93]
        mixedList = ['Abhishek', 27]
4. Advanced Datatype
    a. set
    b. dict --> Dictionary
    c. tuple
    d. binary
    e. frozen set
'''

import keyword
print(keyword.kwlist)

age = 27 #Variable is age, Value is 27
print(age)
age = 30
print(age) # Here value is changed from 27 to 30

a = 45
_ = 343
pi = 3.14
name = 'Abhishek'
isMale = True
complexNumber=  2 + 3j
print(type(a))
print(type(_))
print(type(pi))
print(type(name))
print(type(isMale))
print(type(complexNumber))

a,b,c = 12,13,14
print(a,b,c)
