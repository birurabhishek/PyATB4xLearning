"""
Lambda Expressions

It is an anonymous function that returns some form of data.

Syntax
----------
lambda parameters : expression
"""
#Regular function
def triple_me(num):
    return num ** 3

o = triple_me(10)
print(o)

# Using lambda function
o = lambda num:num**3
print(o(10))

