'''
Write a program that takes a number between 1 and 1,000,000,000
from the user and determines whether it is divisible by 3 using an if statement.
Print the result.

'''

n = int(input("enter a number between 1 and 1000000000:"))

if n % 3 == 0:
    print(f"{n} is divisible by 3")
else:
    print(f"{n} is not divisible by 3")