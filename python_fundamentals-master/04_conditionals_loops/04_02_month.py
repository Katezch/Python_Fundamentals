'''
Take in a number from the user and print "January", "February", ...
"December", or "Other" if the number from the user is 1, 2,... 12,
or other respectively. Use a "nested-if" statement.

'''
n = int(input("enter number 1 to 12:"))

if n == 1:
    print('January')
elif n == 2:
    print("February")
else:
    print("it is boring")