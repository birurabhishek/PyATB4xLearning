global_b = 50

def my_function():
    a = 10 # Local Variable, WIthin the function
    print(a)
    print(global_b)

#print(a) Will not be returned asit is in local variable
my_function()
print(global_b)

#Local variable has more preference as compared to global variable