"""
Fizz Buzz Test:
---------------
Write a program that prints numbers from 1 to 100.
However, multiples of 3 prints "Fizz" instead of number and
multiples of 5 prints "Buzz".
For numbers that are multiples of both 3 and 5 , print FizzBuzz.

Logic Building
---------------
1. For Loop
"""
for number in range(1,101,1):
    if number %3 == 0 and number %5 ==0:
        print('FizzBuzz')
    elif number%3 == 0:
        print("Fizz")
    elif number%5 == 0:
        print("Buzz")
    else:
        print(number)

